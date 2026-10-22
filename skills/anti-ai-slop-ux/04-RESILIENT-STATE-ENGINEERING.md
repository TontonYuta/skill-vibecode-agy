# 🛡️ Kiến Trúc Trạng Thái Kiên Cường & Chống Trôi Layout (Resilient UI States & Zero CLS)

> *"Giao diện của lập trình viên sơ cấp chỉ được thiết kế cho ngày thời tiết đẹp (khi API trả về đúng dữ liệu, mạng 5G siêu tốc, danh sách có đúng 3 phần tử). Giao diện của kỹ sư thiết kế bậc thầy được kiến tạo cho những ngày giông bão: mạng chập chờn, danh sách rỗng không, dữ liệu tràn bờ và hệ thống gặp lỗi."*

---

## 1. Năm Trạng Thái Sống Còn Của Mọi Khối Giao Diện (The 5 Vital UI States)

Mỗi khi xây dựng một component dữ liệu (Bảng, Thẻ, Danh sách, Form), bắt buộc phải hiện thực hóa đủ 5 trạng thái sau:

```
+--------------------------------------------------------------------------+
| 1. LOADING: Skeleton Shimmer (Cùng kích thước với nội dung thật)          |
| 2. IDEAL:   Dữ liệu hiển thị cân đối, phân cấp rõ ràng                   |
| 3. EMPTY:   Hình minh họa tinh giản + Hướng dẫn + Nút CTA hành động       |
| 4. ERROR:   Giải thích nguyên nhân bằng tiếng người + Nút "Thử Lại"      |
| 5. PARTIAL: Hiển thị 8/10 phần tử + Cảnh báo nhẹ về dữ liệu chưa đồng bộ |
+--------------------------------------------------------------------------+
```

### 1. Trạng Thái Đang Tải (Loading State) - Chuẩn Skeleton Loader
- **Cấm Spinner xoay vòng che kín màn hình**: Vòng quay tròn vô định gây cảm giác hệ thống bị đơ và kéo dài thời gian chờ đợi nhận thức (Perceived Wait Time).
- **Quy chuẩn Skeleton Shimmer**:
  - Dùng các khối màu xám mờ nhẹ nhàng (`bg-zinc-800/50` hoặc `bg-zinc-200`) có hình dạng và kích thước mô phỏng chính xác khối văn bản hoặc hình ảnh sắp hiển thị.
  - Hiệu ứng chuyển màu sóng nhẹ: `animate-pulse` hoặc hiệu ứng shimmer gradient ngang với chu kỳ 1.5s.
  - Chiều cao và chiều rộng của Skeleton phải khớp 100% với nội dung thật để triệt tiêu hiện tượng giật cục layout khi dữ liệu tải xong.

### 2. Trạng Thái Rỗng (Empty State) - Nơi Kích Hoạt Hành Động
Khi một người dùng mới mở app và chưa có dữ liệu nào:
- **Tuyệt đối không để trang trắng rỗng trơ trọi**.
- **Cấu trúc một Empty State chuẩn mực**:
  1. Icon hoặc hình minh họa tối giản, thân thiện (kích thước tối đa 48px - 64px, không dùng hình 3D đồ sộ chiếm nửa trang).
  2. Tiêu đề rõ ràng: *"Chưa có dự án nào được tạo"*.
  3. Mô tả ngắn 1 câu về giá trị: *"Tạo dự án đầu tiên để bắt đầu theo dõi tiến độ công việc và mời cộng sự."*
  4. Nút bấm CTA trực tiếp: `[+ Tạo dự án mới]` (tập trung vào hành động cốt lõi).

### 3. Trạng Thái Lỗi & Khả Năng Tự Phục Hồi (Error & Recovery State)
- **Thông điệp bằng ngôn ngữ con người**: Cấm hiển thị các đoạn mã lỗi thô như `Error 500: NullPointerException at line 42` cho người dùng phổ thông.
- **Cung cấp giải pháp xử lý**:
  - *"Không thể kết nối đến máy chủ. Vui lòng kiểm tra đường truyền mạng."*
  - Đi kèm nút bấm: `[Thử lại]` để gọi lại API ngay tại chỗ mà không bắt người dùng phải F5 tải lại toàn bộ trang web.

### 4. Trạng Thái Dữ Liệu Bộ Phận & Ngoại Tuyến (Partial & Offline State)
- Nếu ứng dụng mất kết nối mạng đột ngột, vẫn cho phép người dùng xem dữ liệu đã được cache từ trước.
- Hiển thị thanh banner mỏng trên cùng: *"Đang hoạt động ngoại tuyến. Dữ liệu sẽ tự động đồng bộ khi có mạng."*

---

## 2. Triệt Tiêu 100% Trôi Dạt Layout (Zero Cumulative Layout Shift - CLS)

Hiện tượng giật layout (layout shift) là một trong những trải nghiệm gây ức chế nhất, khiến người dùng bấm nhầm nút hoặc mất dấu vị trí đọc:

1. **Khóa tỷ lệ khung hình ảnh và video**:
   - Luôn khai báo `aspect-ratio` hoặc kích thước `width` và `height` rõ ràng trên thẻ `<img>` và `<video>`:
     ```html
     <div class="aspect-video w-full overflow-hidden rounded-lg bg-zinc-800">
       <img src="..." class="h-full w-full object-cover" loading="lazy" />
     </div>
     ```
2. **Dự trữ không gian cho nội dung động**:
   - Nếu một banner thông báo có thể xuất hiện trên cùng, hãy dùng animation mượt mà hoặc chừa sẵn khoảng trống tối thiểu thay vì đẩy đột ngột toàn bộ trang xuống 60px.
3. **Chống tràn vỡ chữ khi dịch thuật hoặc mở rộng**:
   - Sử dụng `truncate` hoặc `line-clamp-1`, `line-clamp-2` kết hợp `title="..."` hoặc Tooltip để ngăn chặn việc chuỗi ký tự dài bất thường phá vỡ cấu trúc grid.

---

## 3. Mô Thức "Hoàn Tác" Thay Vì Lạm Dụng Hộp Thoại (Undo Over Confirm Modal)

### Tại Sao Modal Xác Nhận Là Một Khuyết Tật UX Cổ Điển?
- Mỗi khi người dùng bấm nút "Xóa một mục", hầu hết các app sơ cấp đều bật lên hộp thoại: *"Bạn có chắc chắn muốn xóa không? [Hủy] [Xóa]"*.
- **Hệ quả tiêu cực**:
  - Làm gián đoạn luồng tư duy và tốc độ làm việc của người dùng.
  - Tạo thói quen bấm "OK" trong vô thức (Habituation bias) — đến khi người dùng vô tình xóa nhầm dữ liệu quan trọng thật, họ vẫn bấm OK như một phản xạ có điều kiện!

### Giải Pháp Tối Ưu Hiện Đại: Toast Hoàn Tác (The Undo Pattern)
1. Khi người dùng bấm xóa, thực hiện xóa ngay lập tức trên UI (Optimistic Delete).
2. Hiển thị một Toast thông báo nhỏ ở góc dưới màn hình trong 6 - 8 giây:
   - *"Đã xóa bài viết 'Kế hoạch Q3'. [Hoàn tác]"*
3. Nếu người dùng bấm `[Hoàn tác]`, phục hồi lại bản ghi ngay lập tức.
4. **Ngoại lệ duy nhất cần Modal xác nhận**: Khi hành động đó thực sự gây nguy hiểm vĩnh viễn không thể khôi phục (vd: Xóa vĩnh viễn tài khoản doanh nghiệp, Xóa toàn bộ Database). Khi đó, yêu cầu người dùng gõ lại tên entity để xác nhận.
