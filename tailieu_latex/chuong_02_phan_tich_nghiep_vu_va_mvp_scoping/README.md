# Chương 2: Phân Tích Nghiệp Vụ & MVP Scoping
## Khắc Phục Hội Chứng Nhồi Nhét Tính Năng và Chuẩn Hóa Đặc Tả Kỹ Thuật

### 1. Tổng quan chương
Chương này cung cấp phương pháp luận phân tích nghiệp vụ chuẩn mực dành riêng cho Vibecoding: áp dụng khung **Jobs-to-be-Done (JTBD)**, sàng lọc tính năng theo thang đo **MoSCoW**, thực thi nghiêm ngặt **Quy tắc Cắt 50% tính năng**, và cô đọng yêu cầu thành tệp đặc tả kỹ thuật máy đọc được (`spec.md`) thông qua kỹ thuật phỏng vấn đối kháng Socratic (`/grill-me`).

### 2. Các nội dung trọng tâm
- **Bản chất hội chứng Feature Bloat**: Tại sao chi phí sinh mã rẻ khiến con người có xu hướng nhồi nhét tính năng làm hỏng sản phẩm và làm suy giảm sự chú ý của AI.
- **Khung JTBD thực chiến**: Chuyển đổi từ mô tả tính năng sang giải quyết "tiến trình chuyển đổi" của người dùng với công thức 3 vế chuẩn.
- **Thang đo MoSCoW & Quy tắc Cắt 50%**: Định nghĩa MVP hạt nhân: 1 Persona + 1 Core Loop + 1 North Star Metric. Loại bỏ dứt điểm các tính năng Could/Won't Have.
- **Kỹ thuật phỏng vấn đối kháng Socratic (`/grill-me`)**: Ép AI làm luật sư phản biện trước khi bắt tay viết code.
- **Cấu trúc chuẩn của tệp `spec.md`**: Bao gồm Non-Goals và Data Contract rõ ràng.

### 3. Tệp tài liệu học thuật & Mã nguồn thực hành
- Tệp nguồn LaTeX: [`chuong_02_phan_tich_nghiep_vu_va_mvp_scoping.tex`](./chuong_02_phan_tich_nghiep_vu_va_mvp_scoping.tex)
- Tệp xuất bản PDF (A4): [`chuong_02_phan_tich_nghiep_vu_va_mvp_scoping.pdf`](./chuong_02_phan_tich_nghiep_vu_va_mvp_scoping.pdf) (4 trang, chuẩn in ấn học thuật)
- Script thực hành đồng hành: [`socratic_spec_builder.py`](./socratic_spec_builder.py) - CLI tạo tệp `spec.md` chuẩn JTBD, Non-Goals và Security Constraints tự động.

### 4. Cây quyết định chọn hướng đi sản phẩm
1. **Hướng 1: Micro-SaaS Đơn Tính Năng (Killer SaaS)**: Next.js + Server Actions + Stripe / LemonSqueezy. 1 persona, 1 core loop.
2. **Hướng 2: Tiện Ích Cục Bộ (Local-First Tool)**: Python / Tauri + SQLite FTS5 + PocketBase nhúng. Tốc độ < 1s, 100% offline.
3. **Hướng 3: Tự Động Hóa & Bot Dòng Lệnh (CLI Automation)**: Python argparse/click + Linux Bash / Windows PowerShell. Tối ưu thời gian quy trình lặp đi lặp lại.
