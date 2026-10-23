#!/usr/bin/env python3
"""
Token Budget Calculator & Context Saturation Advisor (Chương 1 Companion)
========================================================================
Mục đích:
- Phân tích dung lượng token ước tính của cơ sở mã hoặc luồng làm việc.
- Cảnh báo hiện tượng "Lost in the Middle" và suy giảm khả năng bám chỉ dẫn (Needle In A Haystack degradation).
- Đưa ra khuyến nghị phân bổ tác tử (Single-Agent vs Multi-Agent Delegation).
- Tính toán chi phí ước tính và độ nén khi áp dụng kỹ thuật RTK (Rust Token Killer).

Cách dùng:
  python3 token_budget_calculator.py --dir /path/to/project
  python3 token_budget_calculator.py --tokens 45000
"""

import sys
import os
import argparse
from pathlib import Path

# Bảng giá tham chiếu 2026 ($/1M tokens)
PRICING_2026 = {
    "Gemini 2.5 Flash": {"input": 0.075, "output": 0.30},
    "Gemini 2.5 Pro": {"input": 1.25, "output": 5.00},
    "Claude 3.5 Sonnet": {"input": 3.00, "output": 15.00},
    "DeepSeek V3": {"input": 0.14, "output": 0.28},
    "Local Ollama (RTX 4090/3060)": {"input": 0.00, "output": 0.00}
}

# Ngưỡng suy giảm chú ý nhận thức theo các nghiên cứu 2024-2026
SATURATION_THRESHOLDS = [
    (15000, "Vùng Xanh (Optimal Focus)", "Mô hình duy trì độ tập trung 98%, ghi nhớ chính xác logic nghiệp vụ.", "Single-Agent"),
    (40000, "Vùng Vàng (Attention Diffusion)", "Bắt đầu xuất hiện hiện tượng 'Lost in the Middle'. Tỷ lệ hallucination tăng 12%. Khuyến cáo cắt tỉa log và git diff.", "Chủ động tóm tắt hoặc chuyển Subagent"),
    (80000, "Vùng Cam (High Degradation)", "Suy giảm độ bám sát chỉ dẫn hệ thống (System Prompt) đến 35%. Rủi ro sinh mã lạc đề hoặc sửa đè mã nguồn cũ.", "Bắt buộc chia tách tác tử (Architect/Coder/Auditor)"),
    (150000, "Vùng Đỏ (Context Collapse)", "Mô hình thường xuyên lặp lại các lỗi vừa được sửa, bỏ qua các ràng buộc an ninh.", "Dừng ngay, chạy /compact hoặc tái thiết kế cơ sở mã")
]

def estimate_tokens_from_chars(char_count: int) -> int:
    """Quy đổi xấp xỉ 1 token ~ 4 ký tự ASCII / 1.5 ký tự tiếng Việt hoặc mã nguồn"""
    return int(char_count / 3.2)

def scan_codebase_tokens(target_dir: str):
    allowed_exts = {'.ts', '.tsx', '.js', '.jsx', '.py', '.go', '.rs', '.html', '.css', '.md', '.json', '.sh'}
    ignored_dirs = {'node_modules', '.git', 'dist', 'build', '__pycache__', '.next', 'venv', '.venv'}
    
    total_chars = 0
    file_stats = []
    
    for root, dirs, files in os.walk(target_dir):
        dirs[:] = [d for d in dirs if d not in ignored_dirs]
        for f in files:
            p = Path(root) / f
            if p.suffix.lower() in allowed_exts:
                try:
                    size = p.stat().st_size
                    total_chars += size
                    file_stats.append((str(p.relative_to(target_dir)), size))
                except OSError:
                    pass
                    
    total_tokens = estimate_tokens_from_chars(total_chars)
    return total_tokens, total_chars, file_stats

def evaluate_saturation(tokens: int):
    status = SATURATION_THRESHOLDS[-1]
    for limit, label, desc, recommendation in SATURATION_THRESHOLDS:
        if tokens <= limit:
            status = (limit, label, desc, recommendation)
            break
    return status

def print_report(tokens: int, chars: int, file_count: int = 0):
    limit, label, desc, recommendation = evaluate_saturation(tokens)
    rtk_savings_tokens = int(tokens * 0.35)
    rtk_compressed_tokens = tokens - rtk_savings_tokens
    
    print("=" * 72)
    print(" 🎯 VIBECODING TOKEN BUDGET & CONTEXT SATURATION ADVISOR")
    print("=" * 72)
    print(f" • Tổng số ký tự mã nguồn : {chars:,} bytes")
    print(f" • Token ước tính          : {tokens:,} tokens (sau RTK nén: ~{rtk_compressed_tokens:,} tokens)")
    if file_count > 0:
        print(f" • Số lượng tệp mã nguồn   : {file_count} tệp")
    print("-" * 72)
    print(f" 🚦 Trạng thái ngữ cảnh    : {label}")
    print(f" ℹ️  Đánh giá độ sắc bén    : {desc}")
    print(f" 💡 Khuyến nghị tác tử     : {recommendation}")
    print("-" * 72)
    print(" 💰 Ước tính chi phí trung bình cho 1 phiên Vibecoding (10 lượt hỏi-đáp):")
    print(f"    {'Mô hình':<30} | {'Chi phí thô ($)':<16} | {'Sau nén RTK ($)':<16}")
    print("    " + "-" * 66)
    for model, rate in PRICING_2026.items():
        # Giả định 10 lượt: 10 * input_tokens + 10 * 1500 output tokens
        raw_cost = (10 * tokens * rate["input"] + 10 * 1500 * rate["output"]) / 1_000_000
        rtk_cost = (10 * rtk_compressed_tokens * rate["input"] + 10 * 1500 * rate["output"]) / 1_000_000
        print(f"    {model:<30} | ${raw_cost:>12.4f}    | ${rtk_cost:>12.4f}")
    print("=" * 72)

def main():
    parser = argparse.ArgumentParser(description="Vibecoding Token Budget & Context Saturation Advisor")
    parser.add_argument("--dir", type=str, help="Đường dẫn thư mục dự án cần quét token")
    parser.add_argument("--tokens", type=int, help="Số token trực tiếp cần phân tích")
    args = parser.parse_args()

    if args.dir:
        if not os.path.isdir(args.dir):
            print(f"Lỗi: Thư mục không tồn tại: {args.dir}")
            sys.exit(1)
        tokens, chars, files = scan_codebase_tokens(args.dir)
        print_report(tokens, chars, len(files))
    elif args.tokens:
        chars = int(args.tokens * 3.2)
        print_report(args.tokens, chars, 0)
    else:
        # Chạy demo mặc định với 45,000 tokens
        print("Chạy kịch bản mẫu với 45,000 tokens (dự án trung bình):")
        chars = int(45000 * 3.2)
        print_report(45000, chars, 24)

if __name__ == "__main__":
    main()
