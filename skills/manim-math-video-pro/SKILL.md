---
name: manim-math-video-pro
description: >-
  Chuẩn sản xuất video hoạt họa toán học Manim CE chất lượng cao (9:16 Dọc Shorts/TikTok & 16:9 Ngang)
  dựa trên cấu trúc 5 phân cảnh vàng của c1_HamSo_DonDieu.py & c1_HamSo_CucTri.py: Dual-Zone Container Cards, Mô phỏng động
  ValueTracker + always_redraw, Tiếp tuyến đổi màu, Bắt điểm cực trị real-time, Bảng biến thiên 3 tầng, Chữa đề thi RAG thực chiến
  và Thẻ Outro thương hiệu LaggedStart.
---

# Master Guide: Sản Xuất Video Toán Học Manim CE Chuyên Nghiệp

Kỹ năng này chuẩn hóa 100% quy trình thiết kế, lập trình và kiểm soát thẩm mỹ cho video hoạt họa toán học Manim CE (Python), kế thừa kiến trúc đỉnh cao từ bộ đôi bài giảng mẫu `c1_HamSo_DonDieu.py` và `c1_HamSo_CucTri.py`.

---

## 1. Cấu Trúc Khung Hình & Tọa Độ Hình Học

### 1.1 Khung Hình Dọc 9:16 (TikTok, YouTube Shorts, Reels)
- Kích thước pixel: `config.pixel_width = 1080`, `config.pixel_height = 1920`
- Kích thước không gian Manim:
  - Chiều rộng `config.frame_width = 9.0` (Biên trái -4.5, biên phải +4.5)
  - Chiều cao `config.frame_height = 16.0` (Đỉnh trên +8.0, đáy dưới -8.0)
- Tỷ lệ lấp đầy: Sử dụng tổng chiều cao 14.8 / 16.0 đơn vị (chiếm ~93% màn hình), triệt tiêu khoảng đen thừa.

### 1.2 Hàm Helper Bắt Buộc: `fit_width` (Chống tràn viền thẻ)
Mọi khối nội dung bên trong bất kỳ thẻ Card nào đều BẮT BUỘC gọi `fit_width(mobj, max_width=7.8)` trước khi `self.play`:
```python
def fit_width(mob: Mobject, max_width: float = 7.8) -> Mobject:
    """Tự động co tỷ lệ nếu chiều rộng vượt quá ngưỡng quy định để chống tràn mép thẻ."""
    if mob.width > max_width:
        mob.scale_to_fit_width(max_width)
    return mob
```

---

## 2. Kiến Trúc 5 Phân Cảnh Vàng (5-Chapter Cinematic Flow)
Toàn bộ video có thời lượng lý tưởng 90 - 120 giây (mở rộng linh hoạt 60s - 300s), chia thành đúng 5 chương rõ ràng:

### Chương 1: Mở Đầu Ấn Tượng (Intro, ~7s - 15s)
- **Cấu trúc**:
  1. Pill Badge chủ đề: `RoundedRectangle(width=badge_text.width + 0.65, height=badge_text.height + 0.35, color=TEAL, fill_color="#0F172A", fill_opacity=0.92)`
  2. Tiêu đề bài học: `Text("...", font_size=32, weight=BOLD, color=YELLOW)` bọc trong `SurroundingRectangle(title, buff=0.28, color=BLUE_C, corner_radius=0.18)`
  3. Phụ đề dẫn dắt: `Text("...", font_size=22, color=GRAY_B)`
  4. Xem trước quy tắc cốt lõi: 2-3 dòng `MathTex(r"...", font_size=26)`.
     - Với Đơn điệu: $y' > 0 \implies \text{Đồng biến } (\nearrow)$, $y' < 0 \implies \text{Nghịch biến } (\searrow)$.
     - Với Cực trị: Phân biệt $x_0$ (Điểm cực trị hàm số), $y_0 = f(x_0)$ (Giá trị cực trị), $M(x_0; y_0)$ (Điểm cực trị đồ thị).
     - **NGUYÊN TẮC CÔNG THỨC INTRO**: Mỗi công thức cốt lõi nằm trọn vẹn trên ĐÚNG 1 DÒNG ĐƠN duy nhất, TUYỆT ĐỐI KHÔNG ngắt dòng bằng `\\` bên trong công thức.
- **Animation**: `FadeIn` với hướng trượt nhẹ, `Write` tiêu đề, dừng `self.wait(2.2)`.
- **Chuyển cảnh**: `self.play(FadeOut(intro_group))` dọn sạch 100% màn hình. TUYỆT ĐỐI KHÔNG để biểu tượng co nhỏ trôi nổi ở góc UL làm watermark để tránh va chạm đè chữ tiêu đề ở phân cảnh tiếp theo!

### Chương 2: Lý Thuyết Cốt Lõi - Cặp Thẻ Màu Tương Phản (~14s - 30s)
- **Header đỉnh**: `Text(..., font_size=26, color=YELLOW).to_edge(UP, buff=0.6)` + Phụ đề `Text(..., font_size=22, color=GRAY_B)`.
- **Cặp Thẻ Màu Chuyên Biệt**:
  - **Thẻ 1 (Đồng biến / Cực đại / Khẳng định)**: Viền `GREEN_D`, nền `#064E3B` (độ đục 0.35), `height=4.2, width=8.4`.
  - **Thẻ 2 (Nghịch biến / Cực tiểu / Phủ định)**: Viền `RED_D`, nền `#7F1D1D` (độ đục 0.35), `height=4.2, width=8.4`.
- **Nội dung thẻ**: Tiêu đề thẻ (`font_size=24, BOLD`) + Công thức đạo hàm (`font_size=28-30`) + Hướng mũi tên đồ thị ($\nearrow$ hoặc $\searrow$) + Định lý 2 ($f'(x_0) = 0$ và $f''(x_0) < 0$ hoặc $> 0$).
- Cả 2 thẻ xếp dọc: `theory_stack = VGroup(block1, block2).arrange(DOWN, buff=0.4)`.
- Chuyển cảnh: `self.play(FadeOut(theory_all))` sau `self.wait(3.0)`.

### Chương 3: Dual-Zone Container Mô Phỏng Động Tương Tác (~38s - 60s)
- **Header Bar cố định**:
  - `header_card = RoundedRectangle(width=8.4, height=1.1, color=BLUE_D, fill_color="#1E293B", fill_opacity=0.95).to_edge(UP, buff=0.35)`
  - Chứa Pill Badge ("Ví dụ minh họa" hoặc "Ví dụ") + Tiêu đề hàm số.
- **Top Card (Visual Simulation, height=6.4, width=8.4)**:
  - Hệ trục: `Axes(x_range=[-2.4, 2.4, 1], y_range=[-2.8, 2.8, 1], x_length=7.2, y_length=4.0)`. (CHÚ Ý: `y_length` không vượt quá 4.0 để tránh đè tiêu đề thẻ và nhãn cực trị).
  - Đồ thị: `graph = axes.plot(f_func, color=TEAL_C, stroke_width=4.0)`.
  - Đường gióng cực trị: `axes.get_lines_to_point(pt).set_color(GREEN_C / RED_C / YELLOW_B)`.
  - Tiếp tuyến đổi màu: `Line(p1, p2, color=col, stroke_width=4.0)` với $dx = 0.38 - 0.42$.
  - **THANH TRẠNG THÁI BẮT ĐIỂM CỰC TRỊ REAL-TIME (Snap-to-Critical Status Badge)**:
```python
def get_status_badge():
    t = t_param.get_value()
    m = 3 * (t**2) - 3
    if abs(t - (-1.0)) < 0.16:
        txt, b_col, bg_col = "x = -1 ➜ CỰC ĐẠI: y_{CĐ} = 2", GREEN_B, "#064E3B"
    elif abs(t - 1.0) < 0.16:
        txt, b_col, bg_col = "x = 1 ➜ CỰC TIỂU: y_{CT} = -2", RED_B, "#7F1D1D"
    elif m > 0.1:
        txt, b_col, bg_col = "y' > 0 ➜ ĐỒNG BIẾN (↗)", TEAL_B, "#0F172A"
    else:
        txt, b_col, bg_col = "y' < 0 ➜ NGHỊCH BIẾN (↘)", ORANGE, "#78350F"
    lbl = Text(txt, font=MAIN_FONT, font_size=22, weight=BOLD, color=WHITE)
    rect = RoundedRectangle(corner_radius=0.1, width=max(6.0, lbl.width + 0.5), height=0.52, color=b_col, fill_color=bg_col, fill_opacity=0.9, stroke_width=1.8).move_to(lbl)
    return VGroup(rect, lbl).next_to(top_card.get_bottom(), UP, buff=0.16)

status_badge = always_redraw(get_status_badge)
```
- **Bottom Card (height=6.6, width=8.4)**:
  - Đạo hàm: `MathTex(r"y' = 3x^2 - 3 = 0 \iff x = \pm 1", font_size=26)`.
  - **BẢNG BIẾN THIÊN 3 TẦNG LATEX CHUẨN MỰC**:
```latex
\renewcommand{\arraystretch}{1.3}
\begin{array}{|c|ccccccc|}
\hline
x & -\infty & & -1 & & 1 & & +\infty \\
\hline
y' & & + & 0 & - & 0 & + & \\
\hline
& & & 2 & & & & +\infty \\
y & & \nearrow & & \searrow & & \nearrow & \\
& -\infty & & & & -2 & & \\
\hline
\end{array}
```
  - Kết luận (phân biệt điểm cực trị $x$, giá trị cực trị $y$, điểm cực trị đồ thị $M$) đóng khung `SurroundingRectangle(conclusions, color=GREEN, buff=0.14, corner_radius=0.12, stroke_width=2.5)`.
  - Di chuyển `t_param` với nhịp điệu vừa vặn: `self.play(t_param.animate.set_value(2.1), run_time=4.0, rate_func=smooth)`.
  - Chuyển cảnh: `self.play(FadeOut(sim_all))` dọn sạch toàn bộ.

### Chương 4: Chữa Đề Thi & Bài Tập Thực Chiến (~38s - 120s)
- **Quy tắc Zero-Overlap**: Mỗi màn hình chỉ hiển thị ĐÚNG 2 CÂU trên 2 thẻ (Top Card = Câu lẻ, Bottom Card = Câu chẵn).
- **Phân cấp tiêu đề thẻ con**: `c1_title`, `c2_title` BẮT BUỘC `font_size=20 - 22` (weight=BOLD, Sentence case, TEAL_A/YELLOW), đặt tại `.next_to(card.get_top(), DOWN, buff=0.18)`. TUYỆT ĐỐI CẤM `font_size > 22` và CẤM bọc box quanh tiêu đề thẻ!
- **Triệt tiêu toàn bộ Box không cần thiết (Anti-Label-Box & Zero Redundant Boxes)**:
  - CẤM TUYỆT ĐỐI tạo box / pill quanh nhãn phân loại: "Ví dụ minh họa", "Ví dụ", "Dạng 1", "Dạng 2", "Thực chiến". Dùng Text trơn (`font_size=20-22`, `weight=BOLD`, `color=TEAL_A` hoặc `YELLOW`) đặt trực tiếp cùng dòng hoặc gắn vào tiêu đề.
  - CẤM bọc SurroundingRectangle quanh câu hỏi / đề bài.
  - CẤM bọc box quanh từng bước giải (Bước 1, Bước 2, Bước 3).
  - CHỈ DUY NHẤT 1 hộp xanh khoanh đáp án đúng: `SurroundingRectangle(opt_correct, color=GREEN, buff=0.12-0.14, corner_radius=0.08, stroke_width=2.5)` ôm quanh ĐÚNG phương án đúng (chữ A/B/C/D) trong hàng đáp án.
- **Kết luận bài tập tinh gọn (Lean 1-Line Conclusion)**:
  ```python
  c_concl = VGroup(
      Text("➜ [Khẳng định ngắn gọn]. Chọn", font=MAIN_FONT, font_size=22, color=GREEN_B, weight=BOLD),
      MathTex(r"\mathbf{D}", font_size=24, color=GREEN)
  ).arrange(RIGHT, buff=0.15)
  ans_box = SurroundingRectangle(optD, color=GREEN, buff=0.14, corner_radius=0.1, stroke_width=2.5)
  ```
  CẤM `font_size > 24` cho kết luận, CẤM tạo thẻ con RoundedRectangle riêng cho kết luận!
- **Chống thu nhỏ nội dung (Anti-Shrink Protocol)**:
  - Mọi dòng Text/MathTex KHÔNG dài quá 50-55 ký tự (ngắt thành 2 dòng ngắn nếu dài) để `fit_width` không co nhỏ chữ li ti!
  - Cỡ chữ chuẩn: MathTex `24 - 28` (to rõ, nổi bật), Text diễn giải `22` (CẤM `font_size < 22`), BBT `22 - 24`.
  - CẤM TUYỆT ĐỐI dùng `.scale(< 0.85)` trên các khối nội dung thẻ. Dùng khoảng cách dọc tối ưu `buff=0.14 - 0.18`.
- Chuyển cảnh: `self.play(FadeOut(qz_all))` dọn sạch.

### Chương 5: Tổng Kết & Outro Thương Hiệu (~8s - 15s)
- **Outro Card toàn màn hình**: `RoundedRectangle(corner_radius=0.25, width=8.4, height=13.6, color=GOLD_E, fill_color="#0F172A", fill_opacity=0.96).move_to(ORIGIN)`
- Tiêu đề: `Text("TỔNG KẾT BÍ KÍP ...", font_size=28-30, weight=BOLD, color=YELLOW)`
- 3 gạch đầu dòng cô đọng kiến thức cốt lõi.
- Diễn hoạt xuất hiện tuần tự bằng `LaggedStart`:
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

---

## 3. Quy Chuẩn Typography & Font Chữ

1. **Font Chữ Ưu Tiên**:
   - `MAIN_FONT = "Times New Roman"` (chuẩn tài liệu giáo khoa, tạp chí toán học Việt Nam; polyfill tự động nạp tiếng Việt và dự phòng sang `DejaVu Serif` trên Linux).
   - `MAIN_FONT = "Be Vietnam Pro"` nếu ưu tiên giao diện Sans-Serif hiện đại.
2. **Cỡ Chữ An Toàn**:
   - Tiêu đề chính / Intro / Outro: `28 - 32` (BOLD, YELLOW)
   - Tiêu đề Card: `22 - 24` (BOLD)
   - Công thức MathTex: `24 - 30`
   - Chữ diễn giải: `20 - 24` (CẤM dùng font_size < 20 trên video dọc 9:16).
   - line_spacing = 1.2 cho văn bản nhiều dòng.
3. **Quy Tắc Superscript & Subscript**:
   - 100% công thức mũ, chỉ số dưới, đạo hàm dùng `MathTex(r"...")`. TUYỆT ĐỐI CẤM dùng ký tự unicode mũ ($x^2$, $y'$) trong `Text(...)`.

---

## 4. Kiểm Soát Cú Pháp Manim CE (Zero-Hallucination Guard)

- Không dùng `font_color` trong `Text` (dùng `color=...`).
- Không dùng `background_stroke` (dùng `stroke_width`, `stroke_color`).
- Không dùng `Transform` giữa các `MathTex` lệch độ dài (dùng `ReplacementTransform` hoặc `FadeTransform`).
- Không ngắt dòng bằng `\\` bên trong 1 `MathTex` đơn lẻ làm vỡ bố cục 2x2. Dùng `\quad \text{và} \quad` hoặc tách thành nhiều `MathTex`.
- Với `ImageMobject`: BẮT BUỘC dùng `Group(...)`, TUYỆT ĐỐI CẤM dùng `VGroup(...)`.

---

## 5. Ngôn Ngữ Sư Phạm Tự Nhiên & Thời Lượng Thích Ứng Theo Tài Liệu

### 5.1 Triệt Tiêu Thuật Ngữ Kỹ Thuật Meta ("RAG", "Trích từ tài liệu")
- TUYỆT ĐỐI CẤM các từ ngữ meta hậu trường trong cả màn hình (Text Mobject) và kịch bản thoại (VOICEOVER_SCRIPT):
  - CẤM "RAG", "Tài liệu RAG", "Dữ liệu RAG", "Trích từ RAG".
  - CẤM "Trích từ tài liệu", "Theo tài liệu đính kèm", "Dựa trên tài liệu tham khảo", "Theo file PDF", "Dữ liệu nguồn".
- BẮT BUỘC dùng ngôn ngữ sư phạm tự nhiên: "Bài toán thực chiến", "Ví dụ 1", "Câu 1", "Câu 2", "Đề bài", "Phương pháp giải", "Luyện tập trọng tâm".

### 5.2 Thời Lượng Thích Ứng Tự Động Theo Tài Liệu Đính Kèm (Adaptive Duration)
- Hệ thống tự động phân tích số trang, độ dài ký tự và số lượng câu hỏi trong file PDF đính kèm:
  - **Tài liệu ngắn** (<= 1 trang, < 1500 ký tự hoặc <= 2 câu): Video Shorts 75s cô đọng, 2 câu tiêu biểu, 1 dạng bài.
  - **Tài liệu trung bình** (2-3 trang, 1500 - 5500 ký tự hoặc 3-4 câu): Video chuẩn 120s (2 phút), 4 câu thực chiến, 2 dạng bài.
  - **Tài liệu dài / Chuyên đề** (>= 4 trang hoặc >= 5 câu): Video bài giảng 180s - 240s, 4-6 câu thực chiến, 2-3 dạng bài.
