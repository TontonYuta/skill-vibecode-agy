# Chương 5: Kiến Trúc Logic & Schema-First
## Chống Trôi Ngữ Cảnh, Đóng Băng Hợp Đồng Dữ Liệu và Máy Trạng Thái Tường Minh

### 1. Tổng quan chương
Chương này xác lập phương pháp luận **Schema-First** để khóa chặt mô hình dữ liệu bằng TypeScript và Pydantic/Zod; chuẩn hóa mô hình máy trạng thái 4 bước (**Explicit 4-State Machine**); thiết lập quy tắc giới hạn mô-đun siêu nhỏ (**Micro-Modules under 200 lines**) và cơ chế ngắt mạch tự động (**Circuit Breaker**) khi tương tác với các dịch vụ AI.

### 2. Các nội dung trọng tâm
- **Triết lý Schema-First**: Ngăn chặn hiện tượng *Context Drift* và silent failures bằng cách khóa Data Contract trước khi sinh mã UI hoặc API.
- **Boundary Gatekeepers**: Sử dụng Zod/Pydantic `safeParse` kiểm soát chặt chẽ mọi dữ liệu đi vào ứng dụng từ máy khách và phản hồi LLM.
- **Explicit 4-State Machine**: Thay thế anti-pattern boolean rời rạc bằng 4 trạng thái độc lập: `IDLE` $\rightarrow$ `LOADING` $\rightarrow$ `SUCCESS` $\rightarrow$ `ERROR`. Xử lý riêng biệt *Empty State*.
- **Quy tắc Micro-Modules (< 200 lines)**: Phân rã tệp thành 4 lớp chuyên biệt (`types`, `service`, `ui`, `test`) để tránh suy giảm chú ý của AI và triệt tiêu lỗi hồi quy.
- **Cơ chế Circuit Breaker**: Phòng thủ khi API bên ngoài bị nghẽn (Rate limit 429, Server error 503) với 3 trạng thái Closed, Open, Half-Open.

### 3. Tệp tài liệu học thuật & Mã nguồn thực hành
- Tệp nguồn LaTeX: [`chuong_05_kien_truc_logic_va_schema_first.tex`](./chuong_05_kien_truc_logic_va_schema_first.tex)
- Tệp xuất bản PDF (A4): [`chuong_05_kien_truc_logic_va_schema_first.pdf`](./chuong_05_kien_truc_logic_va_schema_first.pdf) (4 trang, chuẩn in ấn học thuật)
- Script thực hành đồng hành: [`state_machine_contract_demo.ts`](./state_machine_contract_demo.ts) - Mẫu thiết kế Schema-First Zod, Máy trạng thái 4 bước và AICircuitBreaker hoàn chỉnh.

### 4. Cây quyết định lựa chọn mô hình kiến trúc
1. **Mô hình 1: Micro-Modules Monolith (< 200 dòng/file)**: Next.js / Vite SPA + Server Actions + Zod + SQLite/Supabase. Tối ưu cho MVP và ứng dụng dưới 50.000 người dùng.
2. **Mô hình 2: Serverless Edge Microservices**: Cloudflare Workers / Vercel Edge + Upstash Redis Queue + SSE Streaming. Tối ưu cho Chatbot AI và luồng dữ liệu thời gian thực.
3. **Mô hình 3: Local-First Event-Driven**: Tauri / Electron + SQLite FTS5 / PGlite + CRDTs sync. Tối ưu cho ứng dụng offline 100%, bảo mật tuyệt đối.
