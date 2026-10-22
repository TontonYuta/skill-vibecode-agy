# 📐 Quy Chuẩn Hệ Thống Thiết Kế UX/UI Ứng Dụng Hiện Đại (Modern App Design System)

> Tài liệu này thiết lập các quy tắc kỹ thuật và thẩm mỹ bắt buộc cho các ứng dụng web và di động hiện đại. Được đúc kết từ triết lý thủ công phần mềm của **Linear**, **Raycast**, **Apple Human Interface Guidelines (HIG)** và **Vercel Design System**.

---

## 1. Kiến Trúc Token & Bảng Màu (Semantic Design Tokens)

### A. Triết Lý Màu Nền & Chiều Sâu (Surface Elevation)
Tuyệt đối không dùng màu đen thuần `#000000` (OLED black) làm nền chính cho toàn bộ app trên desktop/web vì gây mỏi mắt do độ tương phản quá gắt. Hãy dùng phân tầng xám ấm hoặc xám trung tính (Neutral Slate / Zinc):

```css
/* Dark Mode Elevation Tokens */
--surface-bg:        #090A0F; /* Nền sâu nhất (Canvas background) */
--surface-subtle:    #12131A; /* Thanh điều hướng, Sidebar, Header */
--surface-card:      #181924; /* Khối nội dung chính, Card cấp 1 */
--surface-elevated:  #222334; /* Popover, Dropdown, Menu, Modal */
--surface-border:    rgba(255, 255, 255, 0.08); /* Viền ngăn cách cực mảnh */
--surface-border-subtle: rgba(255, 255, 255, 0.04);
```

### B. Quy Tắc "1 Brand Accent duy nhất"
- Thay vì phối 4-5 màu cầu vồng, chọn **duy nhất 1 màu Accent chủ đạo** (vd: Xanh dương Indigo `#4F46E5`, Xanh lá Mint `#10B981`, hoặc Cam Hổ Phách `#F59E0B`).
- Màu Accent chỉ được xuất hiện ở:
  1. Nút kêu gọi hành động chính (Primary CTA).
  2. Trạng thái đang chọn (Active tab / Active item).
  3. Huy hiệu đếm số thông báo quan trọng.
- Tuyệt đối không dùng màu Accent bôi nền toàn bộ trang hoặc làm viền dày bao quanh các card.

### C. Đảm Bảo Tương Phản Theo Chuẩn WCAG 2.2 AA / AAA
- **Văn bản thông thường (Regular Text)**: Tỷ lệ tương phản tối thiểu **4.5:1** so với màu nền.
- **Văn bản lớn (Large Text >= 18pt hoặc >= 14pt Bold)**: Tỷ lệ tương phản tối thiểu **3:1**.
- **Thành phần giao diện tương tác (Input border, Checkbox, Icon)**: Tỷ lệ tương phản tối thiểu **3:1**.

---

## 2. Tiêu Chuẩn Typography & Phân Cấp Thị Giác

### A. Quy Chuẩn Font Chữ Hỗ Trợ Tiếng Việt Toàn Diện
- **Bộ font hệ thống chất lượng cao**:
  - `font-sans`: `system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Be Vietnam Pro", sans-serif;`
  - `font-mono`: `"JetBrains Mono", "SF Mono", Menlo, Consolas, monospace;`
- Tránh dùng font chỉ hỗ trợ tiếng Anh khiến các ký tự có dấu tiếng Việt (ắ, ệ, ỗ, ứ,...) bị biến dạng (fallback font giật cục).

### B. Bậc Thang Cỡ Chữ & Độ Co Giãn Dòng (Type Scale & Leading)

| Phân Cấp (Role) | Tailwind Class | Cỡ chữ / Line-height | Font Weight | Mục Đích Sử Dụng |
| :--- | :--- | :--- | :--- | :--- |
| **Display** | `text-4xl md:text-5xl` | 36px - 48px / 1.15 | Bold (700) | Banner chính, số liệu khổng lồ (Metrics) |
| **Heading 1** | `text-2xl md:text-3xl` | 24px - 30px / 1.25 | SemiBold (600) | Tiêu đề trang, Header module lớn |
| **Heading 2** | `text-xl md:text-2xl` | 20px - 24px / 1.3 | SemiBold (600) | Tiêu đề phân đoạn, Card lớn |
| **Heading 3** | `text-base md:text-lg` | 16px - 18px / 1.4 | Medium (500) | Tiêu đề danh mục, tiêu đề bảng |
| **Body (Chính)** | `text-sm md:text-base` | 14px - 16px / 1.6 | Regular (400) | Đoạn văn, nội dung đọc chính |
| **Caption / Meta** | `text-xs md:text-sm` | 12px - 13px / 1.5 | Regular (400) | Nhãn phụ, thời gian, trạng thái, breadcrumbs |
| **Code / Data** | `font-mono text-xs` | 12px - 13px / 1.4 | Regular (400) | Mã định danh, UUID, timestamp kỹ thuật |

### C. Quy Tắc Chống Lỗi Typography Trình Duyệt
1. **Tiêu đề nhiều dòng**: Luôn dùng `text-wrap: balance` để các dòng tiêu đề tự cân bằng độ dài, không tạo ra dòng cuối cùng cụt lủn.
2. **Đoạn văn đọc**: Dùng `text-wrap: pretty` để loại bỏ chữ mồ côi (orphan word) ở cuối đoạn văn.
3. **Độ dài dòng lý tưởng (Optimal Measure)**: Giới hạn chiều rộng đoạn văn bản đọc từ **60 - 75 ký tự** (`max-w-prose` hoặc `max-w-2xl`). Tuyệt đối không để một dòng văn bản kéo dài từ góc trái sang tận góc phải màn hình 1920px.

---

## 3. Bố Cục, Khoảng Trắng & Loại Bỏ "Cardocalypse"

### A. Phân Cấp Bằng Khoảng Trắng & Đường Kẻ Thay Vì Đóng Hộp (Cardless Layouts)
- **Sai lầm AI Slop**: Cứ có một nhóm nội dung là bọc một thẻ Card (`rounded-2xl border bg-card p-6 shadow-md`).
- **Chuẩn Modern UI**:
  - Tận dụng khoảng cách thông minh: `mb-8` giữa các nhóm lớn, `mb-2` giữa tiêu đề và nội dung con.
  - Sử dụng đường kẻ phân tách cực mảnh (Hairline divider: `border-b border-white/5` hoặc `border-b border-zinc-200`) thay vì đóng khung 4 cạnh.
  - Sử dụng nền luân phiên nhẹ nhàng cho hàng dữ liệu thay vì bọc mỗi hàng vào một card riêng.

### B. Quy Tắc Lồng Container (Max 1 Level of Nesting)
- Không bao giờ lồng Card trong Card. Nếu bên trong một Card lớn cần chứa nhiều mục:
  - Dùng **List view** phân tách bằng khoảng cách hoặc đường kẻ ngang.
  - Dùng **Subgrid** phẳng thay vì tạo thêm một thẻ `div` có `border` và `rounded` bên trong.

### C. Hệ Thống Spacing Theo Lũy Thừa 4 (4px / 8px Base Grid)
- `4px` (gap-1): Khoảng cách giữa icon và nhãn chữ.
- `8px` (gap-2): Khoảng cách giữa các chip tag, filter pill.
- `16px` (gap-4, p-4): Padding trong của card nhỏ, form control.
- `24px` (gap-6, p-6): Khoảng cách giữa các cột trong grid chính.
- `32px - 48px` (gap-8, gap-12): Khoảng cách giữa các section nội dung lớn.

---

## 4. Trải Nghiệm Tương Tác Cảm Giác (Tactile & Ergonomics)

### A. Tốc Độ & Độ Trễ (Perceived Performance)
1. **Tốc độ là tính năng số một**: Mọi tương tác click hoặc phím tắt phải phản hồi thị giác trong vòng **dưới 100ms**.
2. **Optimistic Updates**: Khi người dùng nhấn "Lưu" hoặc "Xóa", UI cập nhật ngay lập tức trạng thái mới và gửi request ngầm. Nếu lỗi mạng, phục hồi lại dữ liệu kèm thông báo Toast cho phép "Thử lại".

### B. Tương Tác Nút Bấm Chân Thực (Button States)
Nút bấm hiện đại không chỉ đổi màu hover mà phải có độ lún tự nhiên:
```css
/* Micro Tactile Feedback */
.btn-primary {
  transition: all 150ms cubic-bezier(0.16, 1, 0.3, 1);
}
.btn-primary:hover {
  transform: translateY(-1px);
  filter: brightness(1.05);
}
.btn-primary:active {
  transform: translateY(1px);
  filter: brightness(0.95);
}
```

### C. Vùng Chạm Tối Thiểu (Touch Target Size)
- Trên mobile và thiết bị cảm ứng, mọi nút bấm, icon button, checkbox phải có diện tích chạm thực tế tối thiểu **44px x 44px** (theo chuẩn Apple HIG) dù kích thước hình ảnh hiển thị có thể là 20px (bằng cách dùng `p-3` hoặc `before:absolute before:inset-[-8px]`).
