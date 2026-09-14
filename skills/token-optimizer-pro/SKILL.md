---
name: token-optimizer-pro
description: >-
  Extreme token frugality, context preservation, and high-efficiency tool usage protocols for Antigravity (agy).
  Activate this skill when handling large codebases, managing complex multi-step vibecoding tasks,
  preventing context window bloat, or optimizing agent speed and token costs.
---

# Token Optimizer Pro: Chuẩn Vận Hành Tiết Kiệm Token & Tối Ưu Context Cho AGY

Kỹ năng này thiết lập các nguyên tắc và kỹ thuật thực thi tối ưu nhất nhằm giúp Antigravity hoạt động với **tốc độ cao nhất**, **độ chính xác tối đa** và **tiết kiệm từ 50% đến 80% lượng token tiêu thụ** trong mọi phiên vibecoding.

---

## 1. Triết Lý Cốt Lõi: "Zero Token Waste"

Context Window là tài nguyên hữu hạn và quý giá nhất của AI. Việc nhồi nhét hàng nghìn dòng code không cần thiết vào ngữ cảnh sẽ dẫn đến:
- Tăng chi phí token và độ trễ phản hồi (latency).
- Hiện tượng "Lost in the Middle" (AI quên mất yêu cầu ban đầu hoặc sinh hallucination).
- Cháy context dẫn đến tự động truncate lịch sử quan trọng.

---

## 2. Kỹ Thuật Đọc File Lát Cắt (Window Slicing)

### ❌ Sai Lầm Gây Hao Token (Anti-Pattern):
```json
// GỌI ĐỌC CẢ FILE 800 DÒNG KHI CHỈ CẦN XEM 1 HÀM
view_file({ "AbsolutePath": "/path/to/BigFile.ts" })
```

###  Chuẩn Tối Ưu:
1. **Xác định vị trí trước**: Dùng `grep_search` với `MatchPerLine: true` để biết chính xác số dòng của hàm/khối code cần sửa.
2. **Chỉ đọc lát cắt hữu dụng**: Chỉ định rõ `StartLine` và `EndLine` trong phạm vi 30 - 80 dòng:
```json
view_file({
  "AbsolutePath": "/path/to/BigFile.ts",
  "StartLine": 120,
  "EndLine": 175
})
```
3. **Đọc Interface / Type trước**: Khi tìm hiểu thư viện hoặc module, chỉ đọc phần exports / interfaces ở đầu file thay vì đọc toàn bộ phần thân hàm implementation.

---

## 3. Chiến Thuật Tìm Kiếm 2 Bước (Two-Step Search)

Khi khảo sát dự án lớn, không dùng grep quét toàn bộ nội dung của hàng nghìn tệp:

1. **Bước 1 (Định vị file)**:
   - Dùng `find_by_name` với `Pattern` hoặc `Extensions` để khoanh vùng file.
   - Hoặc dùng `grep_search` với `"MatchPerLine": false` để chỉ lấy danh sách tên file có chứa từ khóa.
2. **Bước 2 (Lọc sâu theo phạm vi)**:
   - Dùng `grep_search` với `Includes: ["src/services/*"]` và `MatchPerLine: true` để lấy chính xác dòng code cần tìm.
   - Tuyệt đối không để `grep_search` quét vào các thư mục rác: `node_modules`, `.git`, `dist`, `build`, `.next`.

---

## 4. Phẫu Thuật Code Cục Bộ (Surgical Edits vs Mass Overwrites)

- **Ưu tiên `replace_file_content`**:
  - Chỉ thay thế đúng khối code cần thay đổi (5 - 30 dòng).
  - Không bao giờ thay thế toàn bộ file 500 dòng chỉ để đổi 1 dòng logic.
- **Dùng `write_to_file` đúng lúc**:
  - Chỉ dùng `write_to_file` khi tạo tệp **hoàn toàn mới** hoặc tệp cấu hình rất ngắn (< 50 dòng).
  - Tránh ghi đè toàn bộ tệp hiện có trừ phi được yêu cầu tái cấu trúc 100%.

---

## 5. Cắt Tỉa Output Terminal (Command Output Pruning)

Khi chạy lệnh terminal thông qua `run_command`, output dài hàng nghìn dòng sẽ làm ngập context ngay lập tức.

### Nguyên Tắc Lọc Lệnh:
1. **Chạy kiểm thử có mục tiêu (Targeted Testing)**:
   - Thay vì chạy toàn bộ test suite (`npm test`), hãy chỉ chạy file test liên quan trực tiếp:
     ```bash
     npm test -- src/components/MyComponent.test.tsx
     # Hoặc pytest
     pytest tests/test_auth.py -k test_login
     ```
2. **Cắt ngắn output nhật ký (Log Truncation)**:
   - Sử dụng các lệnh lọc bash chuẩn:
     ```bash
     # Chỉ lấy 40 dòng đầu hoặc dòng cuối
     npm run build 2>&1 | tail -n 40
     # Hoặc chỉ hiển thị dòng lỗi
     npm test 2>&1 | grep -E "FAIL|Error|passed|failed"
     ```
3. **Tắt cờ Verbose**: Tránh dùng các cờ `-v`, `--verbose`, `--trace` trừ khi thực sự cần debug lỗi ẩn sâu.

---

## 6. Giao Tiếp Tinh Gọn Giữa Các Agent (Lean Subagent Handoff)

Khi kích hoạt subagent qua `invoke_subagent` hoặc nhắn tin qua `send_message`:
- **Không paste nguyên văn code lớn** vào `Prompt` hoặc `Message`.
- **Sử dụng con trỏ tệp (File Pointers)**: Cung cấp đường dẫn tệp tuyệt đối kèm số dòng dạng:
  `[EngineCore](file:///path/to/server/engine.ts#L45-L80)`
- Cấu trúc tin nhắn giao việc chuẩn (Task Handoff Format):
  ```markdown
  ### Nhiệm Vụ: [Tên nhiệm vụ ngắn gọn]
  - **Tệp liên quan**: `file:///abs/path/file.ts#L20-L60`
  - **Mục tiêu**: [1-2 câu súc tích]
  - **Ràng buộc**: [Không sửa type X, giữ nguyên hàm Y]
  - **Output mong muốn**: [Chỉ báo diff hoặc trạng thái pass]
  ```

---

## 7. Lựa Chọn Model Tiết Kiệm (Model Tier Selection)

Khi khởi chạy subagent với `invoke_subagent`, chọn đúng thuộc tính `Model`:
- **`flash`**: Dành cho tác vụ tra cứu, đọc tài liệu, grep code, tìm kiếm web, kiểm tra file tồn tại. Nhanh gấp 3-5 lần, tiêu thụ cực ít chi phí token.
- **`inherit` / `pro`**: Dành cho tác vụ phân tích kiến trúc phức tạp, thiết kế hệ thống, lập trình logic lõi, hoặc review bảo mật sâu.

---

## 8. Bảng Đối Chiếu Nhanh (Cheatsheet)

| Tác Vụ | Cách Gây Tốn Token (Tránh) | Cách Tiết Kiệm (Áp Dụng) |
| :--- | :--- | :--- |
| **Đọc mã nguồn** | `view_file` cả file 500 dòng | `view_file` với `StartLine`/`EndLine` (30-60 dòng) |
| **Tìm kiếm** | Grep toàn bộ thư mục gốc không lọc | Grep có `Includes` + `MatchPerLine: false` trước |
| **Sửa đổi code** | `write_to_file` ghi đè toàn bộ file | `replace_file_content` sửa đúng khối cần thiết |
| **Chạy kiểm thử** | `npm test` toàn bộ 300 test files | `npm test -- path/to/specific.test.ts` |
| **Báo cáo user** | Paste lại hàng trăm dòng log terminal | Tóm tắt kết quả: số test pass/fail + trích xuất lỗi |
