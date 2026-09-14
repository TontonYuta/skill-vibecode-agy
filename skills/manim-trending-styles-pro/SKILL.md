---
name: manim-trending-styles-pro
description: >-
  Hiệu ứng Hoạt họa Xu Hướng Trending Đỉnh Cao cho Manim CE Toán Học: Tiếp tuyến đổi màu,
  Thanh trạng thái bắt điểm cực trị thời gian thực always_redraw, ValueTracker, LaggedStart Outro, Thẻ màu đa sắc, Bảng biến thiên 3 tầng.
---

# Kỹ Thuật Hoạt Họa Trending Cho Video Toán Học Manim CE

Kế thừa các kỹ thuật hoạt họa ấn tượng nhất từ bộ đôi bài giảng vàng `c1_HamSo_DonDieu.py` & `c1_HamSo_CucTri.py` giúp video thu hút học sinh ngay từ giây đầu tiên.

---

## 1. Tiếp Tuyến Trượt Đổi Màu Động Theo Độ Dốc (Dynamic Tangent)
```python
t_param = ValueTracker(-2.1)
moving_dot = always_redraw(lambda: Dot(axes.c2p(t_param.get_value(), f_func(t_param.get_value())), color=GOLD, radius=0.09))

def get_tangent():
    t = t_param.get_value()
    y = f_func(t)
    m = derivative_func(t)
    dx = 0.42
    p1 = axes.c2p(t - dx, y - m * dx)
    p2 = axes.c2p(t + dx, y + m * dx)
    # Xanh lá khi đồng biến (m > 0), Đỏ khi nghịch biến (m < 0), Vàng khi tiếp tuyến ngang (m = 0)
    col = GREEN_C if m > 0.1 else (RED_C if m < -0.1 else YELLOW)
    return Line(p1, p2, color=col, stroke_width=4.0)

tangent_line = always_redraw(get_tangent)
```

---

## 2. Thanh Trạng Thái Bắt Điểm Cực Trị Real-Time (Snap-to-Critical Status Badge)
Kỹ thuật từ `c1_HamSo_CucTri.py`: Khi tiếp tuyến chuyển động lướt qua lân cận cực trị, thanh trạng thái lập tức "bắt" và hiển thị trạng thái cực trị riêng biệt:
```python
def get_status_badge():
    t = t_param.get_value()
    m = derivative_func(t)
    if abs(t - (-1.0)) < 0.16:
        txt, b_col, bg_col = "x = -1 ➜ CỰC ĐẠI: y_{CĐ} = 2", GREEN_B, "#064E3B"
    elif abs(t - 1.0) < 0.16:
        txt, b_col, bg_col = "x = 1 ➜ CỰC TIỂU: y_{CT} = -2", RED_B, "#7F1D1D"
    elif m > 0.1:
        txt, b_col, bg_col = "y' > 0 ➜ ĐỒNG BIẾN (↗)", TEAL_B, "#0F172A"
    else:
        txt, b_col, bg_col = "y' < 0 ➜ NGHỊCH BIẾN (↘)", ORANGE, "#78350F"
    lbl = Text(txt, font=MAIN_FONT, font_size=22, weight=BOLD, color=WHITE)
    rect = RoundedRectangle(
        corner_radius=0.1, width=max(6.0, lbl.width + 0.5), height=0.52,
        color=b_col, fill_color=bg_col, fill_opacity=0.9, stroke_width=1.8
    ).move_to(lbl)
    return VGroup(rect, lbl).next_to(top_card.get_bottom(), UP, buff=0.16)

status_badge = always_redraw(get_status_badge)
```

---

## 3. Hộp Phát Sáng Đáp Án Đúng (Answer Callout Glow)
```python
ans_box = SurroundingRectangle(correct_option, color=GREEN, buff=0.14, corner_radius=0.1, stroke_width=2.8)
self.play(Create(ans_box), run_time=0.8)
```

---

## 4. Diễn Hoạt Outro Tuần Tự & Pop-up Thương Hiệu (Staggered LaggedStart)
Kỹ thuật từ `c1_HamSo_DonDieu.py` & `c1_HamSo_CucTri.py`: Xuất hiện 3 bí kíp bài học lướt nhẹ từ trái sang và thương hiệu pop-up phóng to:
```python
self.play(
    LaggedStart(
        FadeIn(b_p1, shift=LEFT * 0.2),
        FadeIn(b_p2, shift=LEFT * 0.2),
        FadeIn(b_p3, shift=LEFT * 0.2),
        lag_ratio=0.3
    ),
    run_time=2.0
)
self.play(FadeIn(brand_group, scale=0.85), run_time=1.0)
self.wait(3.0)  # BẮT BUỘC: Giữ nguyên màn hình Outro, KHÔNG FadeOut!
```
