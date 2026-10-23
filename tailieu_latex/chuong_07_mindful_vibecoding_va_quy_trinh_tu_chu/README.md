# Chương 7: Mindful Vibecoding & Quy Trình Tự Chủ Vòng Lặp Kép
## Vận Hành Hệ Thống Đại Tác Tử, Giao Thức 2-Strike Git Reset và Vòng Lặp Loop-Until-Green

### 1. Tổng quan chương
Chương cuối cùng của bộ giáo trình đúc kết toàn bộ triết lý **Mindful Vibecoding**; bắt buộc chuẩn hóa tài liệu `TECH_STACK.md`; ban hành quy tắc sống còn **2-Strike Git Reset Protocol** (`git reset --hard HEAD`); phân rã quy trình thành mô hình Vòng lặp kép (**Dual-Loop Architecture**); phân vai 4 tác tử AI chuyên biệt; và thiết lập chuẩn mực thực thi tự chủ (**Zero-Touch Loop-Until-Green**).

### 2. Các nội dung trọng tâm
- **Triết lý Nhạc Trưởng (Conductor vs Typist)**: Dẫn dắt dàn nhạc AI bằng bản thiết kế kiến trúc chuẩn.
- **Bắt buộc có `TECH_STACK.md`**: Giải thích danh sách thư viện, lý do lựa chọn và bản đồ luồng dữ liệu 1 chiều.
- **Giao thức 2-Strike Git Reset**: Nếu sửa 1 lỗi quá 2 lần mà không pass test, lập tức `git reset --hard HEAD` và lập biên bản *Root Cause Post-Mortem*.
- **Kiến trúc Vòng lặp kép (Dual-Loop)**: Outer Loop (Lead Architect con người kiểm soát spec/review) vs Inner Loop (AI Swarm tự code, tự test loop-until-green).
- **Phân vai 4 Subagents chuyên biệt**: Spec Architect $\rightarrow$ Code Implementer $\rightarrow$ Security Auditor $\rightarrow$ QA Automation Tester.
- **Chuẩn mực Zero-Touch Execution**: Tự động giải quyết đến cùng (Exit Code 0) trước khi thông báo hoàn thành.

### 3. Tệp tài liệu học thuật & Bộ mã nguồn Hacker đồng hành
- Tệp nguồn LaTeX: [`chuong_07_mindful_vibecoding_va_quy_trinh_tu_chu.tex`](./chuong_07_mindful_vibecoding_va_quy_trinh_tu_chu.tex)
- Tệp xuất bản PDF (A4): [`chuong_07_mindful_vibecoding_va_quy_trinh_tu_chu.pdf`](./chuong_07_mindful_vibecoding_va_quy_trinh_tu_chu.pdf) (5 trang, chuẩn in ấn học thuật)
- Script đồng hành 1: [`hacker_linux_daemon.sh`](./hacker_linux_daemon.sh) - Daemon IPC Linux với Named Pipes (FIFO), FD 3 `<>`, và signal trapping (`trap cleanup EXIT`).
- Script đồng hành 2: [`mobile_adb_controller.py`](./mobile_adb_controller.py) - Điều khiển Android bằng ADB framebuffer và trích xuất tọa độ UIAutomator XML.
- Script đồng hành 3: [`media_transcriber_pipeline.py`](./media_transcriber_pipeline.py) - Thu hoạch media với `yt-dlp` và chuẩn hóa âm thanh 16kHz mono bằng FFmpeg cho AI.
- Script đồng hành 4: [`office_headless_converter.sh`](./office_headless_converter.sh) - Tự động hóa chuyển đổi hàng loạt Office (Word/Excel/PowerPoint) sang PDF và hình ảnh bằng LibreOffice headless.

### 4. Cây quyết định lựa chọn môi trường tự động hóa
1. **Linux POSIX Shell / Pipes**: Tối ưu cho tiến trình ngầm, microservice daemons, CI/CD, Container, watcher tệp `inotify`.
2. **Windows PowerShell**: Tối ưu cho môi trường Windows, Object Pipeline .NET, Win32 API native hooks, COM office.
3. **AutoHotkey (AHK)**: Tối ưu cho tự động hóa ứng dụng desktop cũ không có API, macro phím chuột mức OS.
4. **Android ADB / scrcpy**: Tối ưu cho tương tác tự động hóa với thiết bị di động thật và máy ảo.
5. **Python Hybrid Automation**: Tối ưu cho các kịch bản kết hợp đa nền tảng, gọi LLM, xử lý file nhị phân.
