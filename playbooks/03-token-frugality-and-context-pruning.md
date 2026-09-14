# Playbook: Token Frugality & Context Window Preservation

## 1. Vấn đề "Context Bloat" trong Agentic Coding
Context window của LLM là tài nguyên quý giá nhất:
- Khi context bị phình to (100k - 200k tokens), tốc độ phản hồi của agent giảm dần.
- Khả năng suy luận logic suy giảm, dễ quên các chỉ thị ở đầu cuộc hội thoại ("Lost in the Middle").
- Chi phí token tăng vọt theo cấp số nhân.

**Mục tiêu**: Hoàn thành các dự án lớn nhiều ngày mà Agent vẫn duy trì độ nhạy bén sắc bén như lượt chat đầu tiên.

---

## 2. Các kỹ thuật tiết kiệm Token sống còn

### 2.1 Lát cắt tệp có chủ đích (Slice-Based File Viewing)
- **Cấm kỵ**: Dùng `view_file` đọc trọn vẹn 1 file 500 - 1000 dòng.
- **Kỹ thuật chuẩn**:
  1. Dùng `grep_search` tìm kiếm hàm hoặc biến mục tiêu.
  2. Xác định khoảng dòng (ví dụ từ dòng 120 đến 165).
  3. Gọi `view_file` với `StartLine=115` và `EndLine=170` (chỉ 55 dòng thay vì 1000 dòng).

### 2.2 Sửa đổi cục bộ thay vì viết đè (Surgical Edits vs Full Rewrite)
- Tránh dùng `write_to_file` để ghi đè lại toàn bộ tệp nguồn khi chỉ sửa đổi vài dòng logic.
- Dùng `replace_file_content` nhắm trúng khối mã cần đổi. Thao tác này chỉ tiêu thụ vài chục token thay vì hàng ngàn token cho mỗi lượt sửa.

### 2.3 Cắt gọt đầu ra Terminal (Bash Output Pruning)
- Các lệnh `npm install`, `find`, `ls -R`, `git log` có thể in ra hàng ngàn dòng văn bản làm tràn context.
- Luôn sử dụng bộ lọc:
  - `git log -n 5 --oneline`
  - `find ... | head -n 30`
  - Chạy file test cụ thể: `npm test -- tests/target.test.ts` thay vì chạy toàn bộ khi đang debug dở.

### 2.4 Không nhồi nhét log dài vào câu trả lời cho User
- Khi thông báo cho user, chỉ trích xuất các thông số cốt lõi: số lượng test pass, thời gian chạy, mã commit, URL tunnel.
- Tránh copy nguyên văn output màn hình hàng trăm dòng vào chat transcript.
