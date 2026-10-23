# Chương 4: An Ninh Mã Nguồn Trong Kỷ Nguyên Vibecoding
## Phòng Thủ Các Lỗ Hổng Phổ Biến CWE, OWASP và Bảo Mật Toàn Vẹn Hệ Thống

### 1. Tổng quan chương
Chương này đi sâu vào thực trạng an ninh mã nguồn do AI sinh ra dựa trên khảo sát thực nghiệm *Last Secure Code Benchmark* (arXiv:2610.14766, 2026), giải phẫu Top 5 lỗ hổng bảo mật chết người (CWE-89, CWE-639 IDOR, CWE-284 Supabase RLS, CWE-798/200 rò rỉ secret, CWE-918 SSRF) và cung cấp ma trận phòng thủ 4 tầng toàn diện.

### 2. Các nội dung trọng tâm
- **Nghịch lý mã nguồn AI**: Đạt functional correctness nhưng 65% chứa lỗ hổng bảo mật CWE nghiêm trọng.
- **Top 5 CWE phân tích chi tiết**:
  - *CWE-89 (SQL Injection)*: Nối chuỗi qua `queryRawUnsafe` hoặc f-strings $\rightarrow$ Khắc phục bằng Parameterized Queries.
  - *CWE-639 / CWE-862 (IDOR \& BOLA)*: Đọc trộm tài nguyên qua ID mà thiếu kiểm tra `user_id` $\rightarrow$ Khắc phục bằng ràng buộc sở hữu tại mệnh đề WHERE.
  - *CWE-284 (Omission of Supabase RLS)*: Bỏ quên `ENABLE ROW LEVEL SECURITY` khiến lộ toàn bộ bảng dữ liệu qua `anon_key` $\rightarrow$ Khắc phục bằng quy chuẩn kích hoạt RLS và thiết lập Policy bắt buộc.
  - *CWE-798 & CWE-200 (Secret Leaks)*: Nhầm lẫn biến `NEXT_PUBLIC_` nhúng khóa API bí mật vào client bundle $\rightarrow$ Khắc phục bằng phân lập môi trường máy chủ.
  - *CWE-918 (SSRF)*: Gọi URL người dùng nhập mà không kiểm tra IP nội bộ $\rightarrow$ Khắc phục bằng IP Whitelist & Private Subnet blocking.
- **Ma trận phòng thủ 4 tầng**: Pre-commit scanners $\rightarrow$ SAST $\rightarrow$ Network boundary $\rightarrow$ Agentic Pentest bằng Playwright.

### 3. Tệp tài liệu học thuật & Mã nguồn thực hành
- Tệp nguồn LaTeX: [`chuong_04_an_ninh_ma_nguon_va_phong_thu_cwe.tex`](./chuong_04_an_ninh_ma_nguon_va_phong_thu_cwe.tex)
- Tệp xuất bản PDF (A4): [`chuong_04_an_ninh_ma_nguon_va_phong_thu_cwe.pdf`](./chuong_04_an_ninh_ma_nguon_va_phong_thu_cwe.pdf) (4 trang, chuẩn in ấn học thuật)
- Script thực hành đồng hành: [`cwe_security_scanner.py`](./cwe_security_scanner.py) - Bộ quét tự động 5 lỗ hổng CWE điển hình (SQLi, IDOR, NEXT_PUBLIC_ secret leaks, SSRF, Hardcoded keys), xuất báo cáo JSON máy đọc phục vụ Self-Healing.

### 4. Cây quyết định thiết lập thế trận phòng thủ
1. **Thế trận 1: Công cụ Công khai (Public Read-Only)**: Rate limit + Giấu API Key tại server + Chặn SSRF tới IP riêng tư.
2. **Thế trận 2: Tiện ích Cục bộ (Local-First Offline)**: Không mở cổng mạng công khai, phân quyền file nghiêm ngặt, rủi ro tấn công mạng xấp xỉ 0.
3. **Thế trận 3: Nền tảng SaaS Đa Khách Hàng (Multi-Tenant SaaS)**: Bắt buộc Supabase RLS, kiểm tra IDOR sở hữu tại mọi câu lệnh WHERE, Cookie HttpOnly và Pentest tự động trước khi deploy.
