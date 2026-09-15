---
name: zero-touch-auto-accept
description: >-
  Quy chuẩn Tự Động Chấp Thuận 100% (Auto Accept/Allow) và Thực Thi Tự Chủ Tuyệt Đối cho Google Antigravity (AGY) & AI Agents.
  Cho phép người dùng chỉ cần gõ prompt và nhấn Enter, Agent tự động chạy ngầm, tự cấp quyền thực thi lệnh shell, tự động sửa đổi tệp,
  tự động chẩn đoán lỗi, loop-until-green và báo cáo kết quả hoàn thiện mà không bao giờ ngắt quãng chờ phê duyệt thủ công.
---

# Master Guide: Zero-Touch Auto Accept & Autonomous Execution (AGY)

Kỹ năng này thiết lập chuẩn mực **Zero-Touch** cho Google Antigravity (AGY) và các AI Coding Agents. Mục tiêu duy nhất: **Người dùng chỉ cần nhập yêu cầu một lần (Prompt -> Enter), toàn bộ chu trình từ lập kế hoạch, chỉnh sửa tệp, chạy terminal command, gỡ lỗi ngầm đến kiểm thử đều được Agent tự động duyệt (Auto Allow/Accept) và thi công đến khi hoàn tất 100%.**

---

## 1. Cơ Chế Auto Accept/Allow Trong Antigravity

Để Antigravity không hiện popup xin quyền chạy lệnh hay yêu cầu duyệt kế hoạch thủ công, hệ thống sử dụng kết hợp 3 lớp tự động:

### Lớp 1: Cấu hình Chính sách Thực thi (Tool Execution Policies)
Trong cài đặt ứng dụng (`App Settings`) hoặc tệp cấu hình dự án (`.agents/` hoặc `~/.gemini/config/`):
- **Tool Execution Policy**: Thiết lập `always-proceed` (Tự động thực thi mọi lệnh shell mà không cần xác nhận).
- **Artifact Review Mode**: Thiết lập `always-proceed` (Tự động áp dụng kế hoạch/artifact mà không chờ người dùng bấm nút Proceed).
- **Non-Workspace File Access**: Thiết lập `allow` (Cho phép đọc/ghi tài nguyên cấu hình cần thiết).
- **Internet Access Policy**: Thiết lập `allow` (Cho phép tải dependencies, tra cứu tài liệu và web fetch).

### Lớp 2: Bộ Chặn Hook Vòng Đời Tự Cấp Quyền (`PreToolUse` Hook)
Antigravity hỗ trợ tệp `hooks.json` nằm tại `.agents/hooks.json` hoặc `~/.gemini/config/hooks.json`.
Bằng cách khai báo hook `PreToolUse` với matcher `*`, mỗi khi Agent chuẩn bị gọi bất kỳ công cụ nào (`run_command`, `write_to_file`, `replace_file_content`), hook sẽ tự động trả về:
```json
{
  "decision": "allow",
  "reason": "Auto allowed by zero-touch-auto-accept policy"
}
```
Khi nhận phản hồi này, engine của Antigravity lập tức cấp phép chạy công cụ ngay lập tức mà không bao giờ hiển thị hộp thoại xin phép user.

### Lớp 3: Chỉ Thị Hành Vi Tự Trị Tuyệt Đối (Autonomous Behavioral Directives)
Được nạp trực tiếp vào System Prompt và tệp `AGENTS.md`:
1. **Tuyệt đối không hỏi xác nhận**: Cấm các câu hỏi dạng:
   - *"Tôi có thể chạy lệnh test không?"*
   - *"Bạn có muốn tôi sửa file này không?"*
   - *"Dưới đây là kế hoạch, bạn có đồng ý để tôi tiến hành không?"*
2. **Tự động kích hoạt chu trình tự phục hồi (Self-Healing Loop)**:
   - Khi lệnh build bị lỗi -> Tự đọc log, tự sửa file nguồn, tự build lại.
   - Khi unit test fail -> Tự trace nguyên nhân, vá logic, re-test cho đến khi 100% xanh lá.
3. **Chỉ dừng lại khi hoàn tất**: Hoàn thành toàn bộ quy trình và chỉ báo cáo kết quả cuối cùng kèm số liệu kiểm thử cụ thể.

---

## 2. Kích Hoạt Nhanh 1-Click (1-Click Enablement)

Bộ kỹ năng đi kèm script tự động kích hoạt toàn diện:

```bash
# Kích hoạt chế độ Auto-Accept toàn cục cho máy:
./scripts/enable-zero-touch.sh --global

# Hoặc kích hoạt riêng cho dự án hiện tại:
./scripts/enable-zero-touch.sh --local
```

Script sẽ tự động:
1. Tạo/Cập nhật `hooks.json` với bộ chặn `PreToolUse` tự động trả về `{"decision": "allow"}`.
2. Cài đặt tệp chỉ thị `AGENTS.md` vào vị trí quy định.
3. Cấu hình cờ `always-proceed` cho terminal commands và artifacts.

---

## 3. Cấu Hình Chi Tiết Tệp `hooks.json`

Để cấu hình thủ công trong dự án (`.agents/hooks.json`) hoặc toàn cục (`~/.gemini/config/hooks.json`):

```json
{
  "zero-touch-auto-allow": {
    "enabled": true,
    "PreToolUse": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "echo '{\"decision\": \"allow\"}'"
          }
        ]
      }
    ]
  }
}
```

---

## 4. Quy Tắc Ứng Xử Cho Agent Trong Chế Độ Zero-Touch

Khi kích hoạt kỹ năng này, Agent BẮT BUỘC tuân thủ các nguyên tắc sau:

### 4.1 "Drive to Completion" (Chạy Một Mạch Tới Đích)
- Tiếp nhận prompt từ user và coi đó là mệnh lệnh duy nhất cần giải quyết trọn vẹn.
- Tự động phân rã nhiệm vụ, tự tạo tệp, tự sửa code, tự chạy build & test.
- Không phát sinh tin nhắn rác hoặc báo cáo trung gian vô nghĩa.

### 4.2 "Loop-Until-Green" (Chạy Test Tự Thân)
- Luôn chủ động dò tìm công cụ test của dự án (`npm test`, `pytest`, `cargo test`, `go test`).
- Nếu chưa có test cho tính năng mới -> Tự viết test cases trước khi tuyên bố hoàn thành.
- Nếu test đỏ -> Tự sửa và chạy lại lặp đi lặp lại đến khi tất cả các test đều Pass.

### 4.3 "Self-Healing on Failure" (Tự Chữa Lành)
- Gặp lỗi biên dịch TypeScript? -> Tự sửa lỗi kiểu (type definition).
- Gặp thiếu thư viện? -> Tự chạy `npm install` hoặc thêm dependency.
- Gặp xung đột cổng mạng (port in use)? -> Tự giải phóng port hoặc đổi cổng an toàn.

---

## 5. Mẹo Dành Cho User Khi Dùng Với Antigravity CLI

Khi tương tác với `agy` trên terminal:
```bash
# Sử dụng lệnh /goal khi bắt đầu tác vụ dài:
/goal Xây dựng tính năng X, tự động code, test và push lên GitHub khi hoàn tất

# Chạy lệnh trực tiếp trên terminal với cờ tự chủ:
agy "Refactor component Auth, viết test kiểm chứng và build production"
```
Người dùng chỉ việc gõ lệnh, nhấn Enter, đứng dậy uống cà phê và quay lại nhận kết quả bàn giao hoàn mỹ.
