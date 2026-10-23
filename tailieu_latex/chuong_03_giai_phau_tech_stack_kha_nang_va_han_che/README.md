# Chương 3: Giải Phẫu Tech Stack Thực Chiến
## Làm Chủ Playwright, Công Cụ Thay Thế Tối Ưu, Sức Mạnh Của Python và Vòng Lặp Tự Sửa Lỗi

### 1. Tổng quan chương
Khác với các tài liệu lý thuyết bề mặt, chương này là bản giải phẫu thực hành chuyên sâu về các công cụ cốt lõi trong quy trình Vibecoding tác tử tự chủ (*Agentic Loop*). Chương học mổ xẻ 7 siêu năng lực thực chiến của Playwright, phân tích các điểm nghẽn bộ nhớ, so sánh trực diện với các công cụ tối ưu hơn như Crawl4AI, Browser-use và HTTPX; đồng thời cung cấp mã nguồn chuẩn cho 2 luồng công việc cốt tử: tự động thu thập bài báo nghiên cứu và tự động kiểm thử webapp kèm cơ chế xuất phản hồi máy đọc (`agent_feedback.json`) để AI tự sửa lỗi; cùng sức mạnh toàn diện của Python trong tương quan với TypeScript.

### 2. Các nội dung trọng tâm
- **7 siêu năng lực thực chiến của Playwright**: Headless execution, network interception & mocking, auto-waiting, console & pageerror monitoring, visual diff screenshots, storage state / cookies, DOM extraction from SPAs.
- **Bảng so sánh vũ khí thu thập dữ liệu**: Playwright vs Crawl4AI (LLM-friendly markdown) vs Browser-Use/Stagehand (Agentic natural language) vs HTTPX + BeautifulSoup (siêu nhẹ, tiết kiệm 95% RAM).
- **Mã nguồn mẫu Quy trình 1**: Thu thập bài báo khoa học arXiv siêu nhẹ kết hợp Playwright chụp ảnh minh chứng.
- **Mã nguồn mẫu Quy trình 2**: Kiểm thử WebApp tự động, lắng nghe 4 kênh lỗi và xuất `agent_feedback.json` có cấu trúc cho AI Agent tự sửa mã nguồn (Loop-until-green).
- **Sức mạnh toàn diện của Python trong Vibecoding**: 6 trụ cột (Tự động hóa kịch bản, Khai thác tri thức, FastAPI Backend, Xử lý PDF/KaTeX, Data processing, AI local orchestration).
- **Bảng so sánh chiến lược**: Khi nào dùng Python vs Khi nào dùng TypeScript khi Vibecode.
- **Cạm bẫy CORS, Serverless Timeout (SSE Streaming)** và Supabase PostgreSQL RLS vs SQLite.

### 3. Tệp tài liệu học thuật & Kịch bản thực hành
- Tệp nguồn LaTeX: [`chuong_03_giai_phau_tech_stack_kha_nang_va_han_che.tex`](./chuong_03_giai_phau_tech_stack_kha_nang_va_han_che.tex)
- Tệp xuất bản PDF (A4): [`chuong_03_giai_phau_tech_stack_kha_nang_va_han_che.pdf`](./chuong_03_giai_phau_tech_stack_kha_nang_va_han_che.pdf) (5 trang, chuẩn in ấn học thuật)
- Script thực hành đồng hành 1: [`paper_harvester.py`](./paper_harvester.py) - Thu thập bài báo khoa học kết hợp HTTPX API siêu tốc (0.8s, 15MB RAM) và Playwright chụp ảnh minh chứng.
- Script thực hành đồng hành 2: [`self_healing_test_runner.py`](./self_healing_test_runner.py) - Bộ chạy kiểm thử Playwright tự động quét 4 kênh lỗi (console, pageerror, HTTP 4xx/5xx, requestfailed) và xuất `agent_feedback.json` để AI tự sửa lỗi khép kín.

### 4. Cây quyết định lựa chọn Tech Stack
- **Lấy dữ liệu API / Trang tĩnh**: Dùng HTTPX (Async) để tiết kiệm 95% RAM và tăng tốc 10x so với trình duyệt không đầu.
- **Bóc tách bài viết sang Markdown cho AI**: Dùng Jina Reader (`r.jina.ai`).
- **Trang web chống bot mạnh / Cloudflare**: Dùng Nodriver hoặc Crawl4AI (CDP thuần).
- **Kiểm thử Webapp tương tác, Form, Click, Chụp ảnh**: Dùng Playwright.
- **Lưu trữ Cục bộ / MVP đơn giản**: SQLite (WAL mode, FTS5) hoặc PocketBase.
- **Hệ thống SaaS nhiều người dùng**: PostgreSQL (Supabase RLS).
