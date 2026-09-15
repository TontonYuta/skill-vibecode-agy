# Playbook: Zero-Touch Autonomous Vibecoding Workflow

## 1. Bản chất của "Zero-Touch Vibecoding"
Trong kỷ nguyên của các AI Coding Agent thế hệ mới (Google Antigravity, Claude Code, Cursor Composer), mô hình tương tác truyền thống "Human Prompt -> AI Suggest -> Human Approve -> AI Code -> Human Test" đã trở nên chậm chạp và làm gián đoạn dòng suy nghĩ (flow state).

**Zero-Touch Vibecoding** định nghĩa lại mối quan hệ:
- Con người là **Product Director & High-Level Specifier** (đưa ra tầm nhìn, yêu cầu nghiệp vụ, tiêu chí chấp nhận).
- AI Agent là **Autonomous Principal Engineer** (tự khảo sát codebase, lập kế hoạch, code, build, fix lỗi, chạy test và hoàn tất từ A đến Z mà không cần xác nhận trung gian).

---

## 2. Nguyên tắc vàng của Zero-Touch

### 2.1 Không xin phép những hành động hiển nhiên
- **Sai lầm phổ biến**: Hỏi user *"Tôi có nên chạy `npm test` không?"*, *"Tôi có thể sửa file `App.tsx` không?"*.
- **Chuẩn Zero-Touch**: Tự động thực hiện các thao tác đọc, sửa, chạy lệnh an toàn trong workspace. Chỉ dừng lại khi thiếu thông tin mật (API credentials), hoặc có nguy cơ phá hủy dữ liệu nghiêm trọng không thể rollback.

### 2.2 Tự chủ sửa lỗi (Self-Healing Loop)
Khi một lệnh build hoặc test bị lỗi:
1. **Đọc kỹ traceback**: Định vị chính xác tệp nguồn và dòng phát sinh ngoại lệ.
2. **Khoanh vùng nguyên nhân**: Do thiếu dependency, import sai, lỗi cú pháp TypeScript, hay logic bất đồng bộ?
3. **Thực hiện bản vá**: Sử dụng `replace_file_content` sửa đúng vị trí.
4. **Tự động chạy lại test**: Lặp lại vòng lặp cho đến khi terminal trả về mã thoát `0`.

---

## 3. Cấu trúc Prompt khởi tạo tối ưu cho User
Để kích hoạt chế độ tự chủ cao nhất cho Agent, user nên dùng cấu trúc prompt sau:

```text
[MỤC TIÊU]: Thêm tính năng Mobile Remote QR cho ứng dụng.
[YÊU CẦU KỸ THUẬT]:
- Hỗ trợ cả mạng nội bộ LAN và đường hầm Cloudflare Tunnel (4G/5G).
- Không làm vỡ giao diện trên điện thoại.
- Không dùng API key bên thứ ba.
[ĐIỀU KIỆN HOÀN THÀNH]:
- Toàn bộ test suite phải chạy và Pass 100%.
```

---

## 4. Cơ chế Kỹ thuật Kích hoạt Auto Accept/Allow trong Antigravity (AGY)
Để loại bỏ 100% hộp thoại xác nhận quyền chạy lệnh terminal hoặc chỉnh sửa tệp:

1. **Chính sách Tool Execution Policy**: Thiết lập `always-proceed` trong cài đặt Antigravity hoặc cấu hình dự án.
2. **PreToolUse Hook Interceptor**: Sử dụng hook `PreToolUse` với matcher `*` trong `.agents/hooks.json` hoặc `~/.gemini/config/hooks.json`:
   ```json
   {
     "zero-touch-auto-allow": {
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
3. **Chỉ thị AGENTS.md**: Đặt tệp `AGENTS.md` ở thư mục gốc của dự án để ép agent vào chế độ tự chủ, tự vá lỗi và chỉ dừng lại khi test suite đạt 100% Pass.
