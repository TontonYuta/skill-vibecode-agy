---
name: manim-3d-geometry-pro
description: >-
  Chuẩn Hoạt Họa Hình Học Không Gian 3D và Hệ Tọa Độ Oxyz trong Manim CE (ThreeDScene):
  Thiết lập Camera góc vàng, ambient rotation, phân biệt nét đứt/nét liền, mặt phẳng trong suốt, vector pháp tuyến và thẻ chú giải.
---

# Chuẩn Hoạt Họa Hình Học Không Gian 3D Manim CE

Kỹ thuật dựng hình và phân tích hình học không gian 3D (Khối chóp, lăng trụ, mặt cầu, hệ tọa độ $Oxyz$, góc và khoảng cách) chuẩn mực giáo khoa Việt Nam trong Manim CE.

---

## 1. Khung ThreeDScene Mẫu Chuẩn (Zero-Crash Template)
```python
from manim import *

class MainScene(ThreeDScene):
    def construct(self):
        # 1. Thiết lập góc quay camera tối ưu (Isometric 3D)
        self.set_camera_orientation(phi=70 * DEGREES, theta=-35 * DEGREES, zoom=0.85)

        # 2. Xoay camera nhẹ nhàng tạo chiều sâu không gian (Ambient Rotation)
        self.begin_ambient_camera_rotation(rate=0.10)
        self.wait(1.5)
        self.stop_ambient_camera_rotation()
```

---

## 2. Quy Tắc Phân Biệt Nét Thấy / Nét Khuất (Solid vs. Dashed Lines)
- **Cạnh thấy (Solid Lines)**: Sử dụng `Line3D(start, end, color=..., thickness=0.03)` hoặc `Line(start, end, color=..., stroke_width=3.5)`.
- **Cạnh khuất bên trong (Dashed Lines)**: BẮT BUỘC sử dụng `DashedLine(start, end, color=GRAY_B, stroke_width=2.5, dash_length=0.15)`.

### Ví dụ Dựng Hình Chóp Đáy Bình Hành $S.ABCD$:
```python
# Tọa độ các đỉnh
A = np.array([-2.0, -1.0, 0.0])
B = np.array([1.0, -1.0, 0.0])
C = np.array([2.5, 0.8, 0.0])
D = np.array([-0.5, 0.8, 0.0])
S = np.array([0.0, 0.0, 3.2])

# Cạnh thấy
edges_visible = VGroup(
    Line(A, B, color=WHITE, stroke_width=3.5),
    Line(B, C, color=WHITE, stroke_width=3.5),
    Line(S, A, color=BLUE_B, stroke_width=3.5),
    Line(S, B, color=BLUE_B, stroke_width=3.5),
    Line(S, C, color=BLUE_B, stroke_width=3.5),
)

# Cạnh khuất (Đáy AD, CD và cạnh bên SD nếu khuất)
edges_hidden = VGroup(
    DashedLine(A, D, color=GRAY_B, stroke_width=2.5, dash_length=0.12),
    DashedLine(C, D, color=GRAY_B, stroke_width=2.5, dash_length=0.12),
    DashedLine(S, D, color=GRAY_B, stroke_width=2.5, dash_length=0.12),
)
```

---

## 3. Nhãn Đỉnh 3D Cố Định Hướng Nhìn
Để chữ nhãn đỉnh ($S, A, B, C, D$) không bị méo mó khi camera xoay, sử dụng hàm chuyển đổi tọa độ sang 2D màn hình hoặc đặt nhãn:
```python
def label_3d(text, point, direction=UP):
    mob = MathTex(text, font_size=24, color=YELLOW)
    mob.move_to(point + direction * 0.3)
    return mob
```

---

## 4. Hệ Tọa Độ Không Gian $Oxyz$ & Mặt Phẳng $(P)$
```python
# Hệ trục ThreeDAxes
axes_3d = ThreeDAxes(
    x_range=[-3, 3, 1],
    y_range=[-3, 3, 1],
    z_range=[-1, 4, 1],
    x_length=6,
    y_length=6,
    z_length=4,
)

# Mặt phẳng mờ bán trong suốt (Semi-transparent Plane)
plane_p = Polygon(
    np.array([-2, -2, 0]),
    np.array([2, -2, 0]),
    np.array([2, 2, 0]),
    np.array([-2, 2, 0]),
    color=BLUE,
    fill_color=BLUE_E,
    fill_opacity=0.35,
    stroke_width=2.0
)

# Vector pháp tuyến n vuông góc mặt phẳng
normal_vec = Arrow3D(
    start=np.array([0, 0, 0]),
    end=np.array([0, 0, 1.8]),
    color=YELLOW,
    thickness=0.03
)
```

---

## 5. Thẻ Ghi Chú 2D Cố Định Trên Khung Hình (Fixed 2D HUD)
Trong `ThreeDScene`, các thẻ bài toán, công thức và bước giải phải được giữ cố định trên màn hình (không bị xoay theo 3D):
```python
# Tạo thẻ nội dung 2D
hud_card = VGroup(
    Text("Xác định góc giữa SC và (ABCD):", font="DejaVu Serif", font_size=22, weight=BOLD),
    MathTex(r"\text{Hình chiếu của } SC \text{ lên } (ABCD) \text{ là } AC", font_size=24, color=YELLOW),
    MathTex(r"\implies \widehat{(SC, (ABCD))} = \widehat{SCA}", font_size=25, color=GREEN_B)
).arrange(DOWN, buff=0.18, aligned_edge=LEFT)

hud_box = SurroundingRectangle(hud_card, buff=0.2, corner_radius=0.12, color=BLUE_B, fill_color="#0F172A", fill_opacity=0.92)
hud_group = VGroup(hud_box, hud_card).to_corner(DR, buff=0.4)

# BẮT BUỘC: Khóa cố định trên màn hình 2D
self.add_fixed_in_frame_mobjects(hud_group)
self.play(FadeIn(hud_group), run_time=0.8)
```
