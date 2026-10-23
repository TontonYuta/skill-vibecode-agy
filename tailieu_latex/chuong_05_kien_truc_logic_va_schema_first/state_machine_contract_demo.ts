/**
 * State Machine Contract & Circuit Breaker Demo (Chương 5 Companion)
 * =================================================================
 * Minh họa thực chiến:
 * 1. Schema-First với Zod: Khóa cứng hợp đồng dữ liệu ở biên (Boundary Gatekeeper).
 * 2. Máy trạng thái 4 bước: Triệt tiêu hoàn toàn impossible states (IDLE -> LOADING -> SUCCESS -> ERROR).
 * 3. Bộ ngắt mạch Circuit Breaker: Tự động cô lập khi dịch vụ LLM/API liên tục gặp sự cố.
 */

import { z } from 'zod';

// ==========================================
// 1. SCHEMA-FIRST DATA CONTRACTS (ZOD)
// ==========================================
export const UserQuerySchema = z.object({
  query: z.string().min(3, "Truy vấn phải có ít nhất 3 ký tự").max(200, "Truy vấn không vượt quá 200 ký tự"),
  temperature: z.number().min(0.0).max(1.0).default(0.7),
  maxTokens: z.number().int().min(50).max(4000).default(1000)
});

export type UserQueryInput = z.infer<typeof UserQuerySchema>;

export const LLMResponseSchema = z.object({
  answer: z.string().min(1),
  model: z.string(),
  tokensUsed: z.number().int().nonnegative(),
  timestamp: z.string().datetime()
});

export type LLMResponseData = z.infer<typeof LLMResponseSchema>;

// ==========================================
// 2. EXPLICIT 4-STATE MACHINE TYPES
// ==========================================
export type AsyncState<T> =
  | { status: 'IDLE' }
  | { status: 'LOADING'; startedAt: number }
  | { status: 'SUCCESS'; data: T; durationMs: number }
  | { status: 'ERROR'; errorMessage: string; errorCode?: string; retryable: boolean };

// ==========================================
// 3. CIRCUIT BREAKER FOR AI SERVICES
// ==========================================
export type CircuitState = 'CLOSED' | 'OPEN' | 'HALF_OPEN';

export class AICircuitBreaker {
  private state: CircuitState = 'CLOSED';
  private failureCount: number = 0;
  private readonly failureThreshold: number;
  private readonly cooldownPeriodMs: number;
  private nextAttemptTimestamp: number = 0;

  constructor(failureThreshold: number = 3, cooldownPeriodMs: number = 10000) {
    this.failureThreshold = failureThreshold;
    this.cooldownPeriodMs = cooldownPeriodMs;
  }

  public getState(): CircuitState {
    if (this.state === 'OPEN' && Date.now() >= this.nextAttemptTimestamp) {
      this.state = 'HALF_OPEN';
    }
    return this.state;
  }

  public async execute<T>(action: () => Promise<T>, fallback: () => T): Promise<T> {
    const currentState = this.getState();
    if (currentState === 'OPEN') {
      console.warn(`[CircuitBreaker] ⚠️ Mạch đang MỞ (OPEN). Trả về fallback cache tức thì!`);
      return fallback();
    }

    try {
      const result = await action();
      this.onSuccess();
      return result;
    } catch (err) {
      this.onFailure();
      throw err;
    }
  }

  private onSuccess() {
    this.failureCount = 0;
    this.state = 'CLOSED';
  }

  private onFailure() {
    this.failureCount++;
    console.warn(`[CircuitBreaker] Ghi nhận thất bại (${this.failureCount}/${this.failureThreshold})`);
    if (this.failureCount >= this.failureThreshold) {
      this.state = 'OPEN';
      this.nextAttemptTimestamp = Date.now() + this.cooldownPeriodMs;
      console.error(`[CircuitBreaker] 🚨 Ngưỡng thất bại vượt quá! Ngắt mạch (OPEN) trong ${this.cooldownPeriodMs}ms.`);
    }
  }
}

// ==========================================
// 4. RUNNABLE DEMO & SIMULATION
// ==========================================
async function simulateVibecodingWorkflow() {
  console.log("============================================================");
  console.log(" 🧩 DEMO KIẾN TRÚC SCHEMA-FIRST & STATE MACHINE VIBECODING");
  console.log("============================================================");

  // Bước 1: Khởi tạo State ở trạng thái IDLE
  let currentState: AsyncState<LLMResponseData> = { status: 'IDLE' };
  console.log("1. Trạng thái khởi tạo:", currentState.status);

  // Bước 2: Kiểm thực Schema dữ liệu đầu vào
  const rawInput = { query: "Tóm tắt bài báo Attention Is All You Need", temperature: 0.5 };
  const parseResult = UserQuerySchema.safeParse(rawInput);
  
  if (!parseResult.success) {
    currentState = {
      status: 'ERROR',
      errorMessage: parseResult.error.message,
      retryable: false
    };
    console.error("Lỗi Schema Gatekeeper:", currentState);
    return;
  }

  console.log("2. Dữ liệu vượt qua Schema-First Gatekeeper hợp lệ:", parseResult.data.query);

  // Bước 3: Chuyển sang trạng thái LOADING
  const startTime = Date.now();
  currentState = { status: 'LOADING', startedAt: startTime };
  console.log("3. Chuyển sang trạng thái:", currentState.status);

  // Bước 4: Khởi tạo Circuit Breaker và giả lập gọi dịch vụ
  const breaker = new AICircuitBreaker(2, 3000);

  // Giả lập cuộc gọi thành công
  try {
    const fakeLLMCall = async () => {
      // Giả lập phản hồi từ LLM
      return LLMResponseSchema.parse({
        answer: "Bài báo giới thiệu kiến trúc Transformer dựa hoàn toàn trên cơ chế Attention.",
        model: "gemini-2.5-flash",
        tokensUsed: 420,
        timestamp: new Date().toISOString()
      });
    };

    const result = await breaker.execute(fakeLLMCall, () => ({
      answer: "Phản hồi dự phòng từ bộ nhớ đệm (Fallback Cache)",
      model: "cache",
      tokensUsed: 0,
      timestamp: new Date().toISOString()
    }));

    currentState = {
      status: 'SUCCESS',
      data: result,
      durationMs: Date.now() - startTime
    };
    console.log("4. Trạng thái cuối cùng:", currentState.status);
    console.log("   Dữ liệu nhận được:", currentState.data.answer);
    console.log("   Thời gian xử lý :", currentState.durationMs, "ms");
  } catch (err: any) {
    currentState = {
      status: 'ERROR',
      errorMessage: err.message,
      retryable: true
    };
    console.error("4. Trạng thái lỗi:", currentState);
  }

  console.log("============================================================");
}

// Chạy mô phỏng khi tệp được thực thi trực tiếp
if (typeof require !== 'undefined' && require.main === module) {
  simulateVibecodingWorkflow();
}
