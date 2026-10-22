# ⚡ Quy Chuẩn Tương Tác, Chuyển Động & Công Thái Học (Interaction, Motion & Ergonomics)

> *"Phần mềm chất lượng cao không khiến người dùng phải đợi chuyển động hoạt họa kết thúc để bấm nút. Chuyển động phải tinh tế đến mức người dùng cảm nhận được tính liên tục mà không nhận thức rằng mình vừa xem một animation."*
> — **Linear Method & Design Engineering Manifesto**

---

## 1. Triết Lý Keyboard-First & Command Menu (`Cmd + K`)

Ứng dụng hiện đại phải phục vụ cả người dùng phổ thông (dùng chuột/cảm ứng) lẫn người dùng chuyên nghiệp (Power Users dùng bàn phím):

### A. Thanh Điều Hướng Toàn Năng (`Cmd + K` hoặc `Ctrl + K`)
- Mọi tác vụ quan trọng trong ứng dụng (tìm kiếm dữ liệu, đổi trang, tạo mới entity, thay đổi cài đặt nhanh) đều phải truy cập được qua phím tắt `Cmd+K`.
- Cấu trúc thanh Command:
  1. Hộp tìm kiếm tức thời với tính năng Fuzzy Search.
  2. Phân loại kết quả theo nhóm: *Recent Searches*, *Actions*, *Navigation*, *Settings*.
  3. Phím tắt hiển thị tinh tế ở cạnh phải (vd: `G then I` để về Inbox, `C` để Create).

### B. Quản Lý Focus Bàn Phím Chuẩn Quốc Tế (Focus Rings)
- **Tuyệt đối không dùng `outline: none`** trừ khi đã thay thế bằng một vòng focus ring rõ ràng:
  ```css
  /* Chuẩn Focus Ring Hiện Đại */
  :focus-visible {
    outline: 2px solid var(--accent-color, #4F46E5);
    outline-offset: 2px;
  }
  ```
- **Hỗ trợ phím điều hướng `Arrow Up / Arrow Down / Enter / Esc`**: Khi mở dropdown, menu, hoặc danh sách tìm kiếm, người dùng phải dùng được các phím mũi tên để chọn và nhấn `Enter` để thực thi mà không cần chạm vào chuột.

---

## 2. Quy Tắc Hoạt Họa & Chuyển Động (Motion Physics)

### A. Thời Lượng Chuyển Động (Duration Standards)
AI thường sinh ra các hiệu ứng animation kéo dài 400ms - 600ms khiến giao diện có cảm giác ì ạch và chậm chạp. Trong phần mềm chuyên nghiệp:
- **Tương tác Micro (Hover, Click, Toggle)**: `100ms - 150ms`.
- **Chuyển trạng thái trung bình (Dropdown, Tooltip, Toast)**: `150ms - 200ms`.
- **Chuyển cảnh lớn (Modal, Drawer, Tab Transition)**: `200ms - 250ms`.
- **Tối đa tuyệt đối**: Không có chuyển động chức năng nào được vượt quá `300ms`.

### B. Đường Cong Gia Tốc (Easing Functions)
- **Vào trang (Entrance)**: Dùng `ease-out` (vd: `cubic-bezier(0.16, 1, 0.3, 1)`) để phần tử xuất hiện nhanh rồi giảm tốc nhẹ nhàng, tạo cảm giác nhạy bén tức thì.
- **Rời trang (Exit)**: Dùng `ease-in` siêu ngắn (`100ms`) để biến mất nhanh gọn, giải phóng tầm nhìn cho người dùng.
- **Cấm tiệt**: Elastic easing (nảy tưng tưng), bounce easing (dội ngược lại), vì làm người dùng chóng mặt và tạo cảm giác nghiệp dư rẻ tiền.

### C. Triệt Tiêu Hoạt Họa Gây Ô Nhiễm Thị Giác (Zero Visual Pollution)
1. **Không rung lắc icon (No Wiggle)**: Icon chỉ đổi màu hoặc thay đổi opacity nhẹ khi hover, không xoay nghiêng hay nhảy nhót.
2. **Không chấm nhấp nháy liên tục (No Continuous Pulsing)**: Chấm trạng thái (Status dot) phải đứng yên. Chỉ dùng nhấp nháy trong trạng thái đang kết nối (Connecting...) và phải dừng ngay khi đã kết nối xong.
3. **Không tự động cuộn chữ (No Infinite Marquee)**: Tuyệt đối không dùng marquee tự chạy làm mất tập trung của người dùng trừ khi đó là sàn chứng khoán chuyên dụng.
4. **Tôn trọng người dùng nhạy cảm chuyển động**:
   ```css
   @media (prefers-reduced-motion: reduce) {
     *, ::before, ::after {
       animation-duration: 0.01ms !important;
       animation-iteration-count: 1 !important;
       transition-duration: 0.01ms !important;
     }
   }
   ```

---

## 3. Công Thái Học Trên Mobile & Màn Hình Cảm Ứng (Thumb Zone)

### A. Quy Tắc "Ngón Tay Cái" (Thumb-Driven Navigation)
- Đặt các nút điều hướng quan trọng nhất ở **cạnh dưới màn hình (Bottom Navigation / Bottom Sheet)** thay vì ép người dùng với tay lên góc trên cùng màn hình 6.7 inch.
- Nút CTA chính trên mobile (vd: "Thanh toán", "Gửi đơn hàng", "Lưu") nên được gắn cố định ở đáy màn hình (`fixed bottom-0 left-0 right-0 p-4`) với phần đệm an toàn (`pb-safe`).

### B. Vuốt Để Đóng (Swipe-to-Dismiss)
- Mọi Bottom Sheet hoặc Modal trên mobile phải hỗ trợ cử chỉ vuốt xuống để đóng tự nhiên, đi kèm phản hồi vật lý kéo dãn nhẹ (spring dampening).
