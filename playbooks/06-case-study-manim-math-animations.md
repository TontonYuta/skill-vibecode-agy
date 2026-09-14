# Case Study: Sản Xuất Hoạt Họa Toán Học Đỉnh Cao Với Manim CE

## 1. Bối cảnh & Yêu cầu sản xuất Video Toán học Hiện đại
Trong các bài giảng toán phổ thông (Đạo hàm, Tính đơn điệu, Cực trị, Hình học không gian 3D), video dạng bảng viết truyền thống thường gây nhàm chán và khó truyền tải bản chất trực quan.
Sử dụng thư viện **Manim Community Edition (Python)** kết hợp chuẩn thiết kế TikTok/Shorts (9:16) và YouTube (16:9) giải quyết triệt để bài toán này.

---

## 2. Kiến trúc 5 Phân Cảnh Vàng (The 5 Golden Scenes)

1. **Scene 1: Hook & Card Giới thiệu**:
   - Thẻ thương hiệu bật mở với hiệu ứng `GrowFromCenter` hoặc `LaggedStart`.
   - Đặt vấn đề trực quan (ví dụ: "Tại sao đạo hàm bằng 0 lại là đỉnh núi hay đáy thung lũng?").
2. **Scene 2: Mô phỏng động Dual-Zone (Khu vực kép)**:
   - **Khu vực trên (Upper Zone)**: Hệ trục tọa độ `Axes`, đồ thị hàm số $y=f(x)$, tiếp tuyến trượt đổi màu theo thời gian thực.
   - **Khu vực dưới (Lower Zone)**: Thẻ phân tích giá trị $x$, $f'(x)$, dấu của đạo hàm và kết luận tăng/giảm.
3. **Scene 3: Bảng biến thiên 3 tầng (3-Tier Variation Table)**:
   - 3 dòng chuẩn: Dòng $x$ (điểm tới hạn $-\infty, x_1, x_2, +\infty$), dòng $f'(x)$ (mang dấu $+$, $-$, $0$), dòng $f(x)$ (mũi tên dốc lên / dốc xuống).
4. **Scene 4: Giải đề thực chiến (RAG Problem Solving)**:
   - Đưa đề bài thi THPT Quốc Gia vào thẻ câu hỏi.
   - Áp dụng ngay quy tắc vừa học để loại trừ phương án sai và chốt đáp án đúng trong 30 giây.
5. **Scene 5: Outro nhận diện thương hiệu**:
   - Tóm tắt công thức trọng tâm.
   - Nút đăng ký kênh / theo dõi với hiệu ứng gợn sóng nổi bật.

---

## 3. Kỹ thuật Lập trình Manim CE Cốt lõi

### 3.1 Hàm chống tràn viền bắt buộc (`fit_width`)
Trong khung hình 9:16 dọc, chiều rộng rất hẹp (`config.frame_width = 9.0`). Mọi mobject trước khi xuất hiện phải được kiểm soát độ rộng:
```python
def fit_width(mobj, max_width=7.8):
    if mobj.width > max_width:
        mobj.width = max_width
    return mobj
```

### 3.2 Tiếp tuyến đổi màu động với `always_redraw` & `ValueTracker`
```python
tracker_x = ValueTracker(-2.5)

tangent_line = always_redraw(lambda:
    get_tangent_line(
        axes=axes,
        curve=graph,
        x=tracker_x.get_value(),
        length=2.5,
        color=GREEN if df(tracker_x.get_value()) > 0 else RED
    )
)
self.add(tangent_line)
self.play(tracker_x.animate.set_value(2.5), run_time=6, rate_func=linear)
```

---

## 4. Kiểm định thẩm mỹ tự động (Layout Checker)
- **Quy tắc Safe-Zone 9:16**: Tránh đặt chữ và số liệu vào 10% đỉnh trên (thanh trạng thái điện thoại) và 15% đáy dưới (nút bình luận, chia sẻ của TikTok/Shorts).
- **Phối màu tương phản cao (Dark Mode)**: Nền tối `#0B0F19`, thẻ `#161F30` với viền `#2D3748`, văn bản trắng `#F8FAFC`, điểm nhấn vàng `#F59E0B` và ngọc `#10B981`.
