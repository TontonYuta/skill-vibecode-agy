---
name: manim-font-typography-pro
description: >-
  Quy chuẩn Font chữ, Typography và Phối màu chuẩn đẹp cho Video Manim CE Toán Học
  (Times New Roman, Be Vietnam Pro, Golden Size Hierarchy, Anti-Shrink & Title Hierarchy).
---

# Quy Chuẩn Font Chữ & Typography Cho Video Manim CE

Kỹ năng này quy định việc sử dụng font chữ, màu sắc và typography trực quan cho video bài giảng toán học chuyên nghiệp chuẩn studio (kế thừa từ `c1_HamSo_DonDieu.py` & `c1_HamSo_CucTri.py`).

---

## 1. Phân Cấp Kích Thước Chữ Vàng (Golden Size Hierarchy)

| Thành phần | Cỡ chữ (`font_size`) | Kiểu dáng / Màu sắc | Lưu ý quan trọng |
| :--- | :--- | :--- | :--- |
| **Tiêu đề chính Intro** | `28 - 32` | `weight=BOLD`, `color=YELLOW` | Sentence case, CẤM > 32 |
| **Tiêu đề Header Bar** | `22 - 24` | `weight=BOLD`, `color=YELLOW` | Pill text `20 - 22` |
| **Tiêu đề Thẻ Card** (`top_title`, `c1_title`...) | `20 - 22` | `weight=BOLD`, `color=TEAL_A/YELLOW` | **CẤM font_size > 22, CẤM bọc box** |
| **Công thức MathTex** | `24 - 28` | Toán học nổi bật, sắc nét | Raw string `r"..."` |
| **Đề bài & Văn bản diễn giải** | `22` | Chuẩn chính tả, `color=WHITE` | **CẤM font_size < 22** |
| **Bảng biến thiên LaTeX** | `22 - 24` | `arraystretch=1.25 - 1.3` | Thu nhỏ vừa vặn thẻ |
| **Nhãn tọa độ Oxy & cực trị** | `22 - 24` | `color=YELLOW/GREEN_B` | Đặt buff=0.1 quanh Dot |
| **Dòng kết luận bài tập** | `22` (text) + `24` (đáp án) | `color=GREEN_B`, `weight=BOLD` | 1 dòng đơn cô đọng |

---

## 2. Quy Tắc Chống Thu Nhỏ Nội Dung (Anti-Shrink Protocol)

1. **Khống chế độ dài mỗi dòng (<= 50-55 ký tự)**:
   - Khi một dòng text quá dài (> 55 ký tự), `fit_width(group, 7.8)` sẽ co toàn bộ nhóm làm chữ bị thu nhỏ li ti.
   - Nếu câu dài, chủ động ngắt thành 2 dòng ngắn `Text("Dòng 1")` và `Text("Dòng 2")` rồi `arrange(DOWN, aligned_edge=LEFT, buff=0.1)`. Chiều rộng tự nhiên luôn <= 6.8 unit, không bị co kéo!
2. **Khoảng cách dọc tối ưu**: Dùng `buff=0.14 - 0.18` khi `arrange(DOWN)` cho các phần tử trong thẻ.
3. **CẤM `.scale(< 0.85)`**: Tuyệt đối không dùng lệnh scale ép nhỏ nội dung bài toán.

---

## 3. Font Chữ & Tiếng Việt Unicode

- **Font có chân mặc định (Serif)**: `Times New Roman` (Linux tự động fallback `Liberation Serif` hoặc `DejaVu Serif`).
- **Font không chân (Sans-serif)**: `Be Vietnam Pro` hoặc `Inter`.
- **Số mũ & chỉ số dưới**: 100% dùng `MathTex(r"...")`. CẤM unicode mũ trong `Text(...)`.

---

## 4. Bảng Màu Chuẩn Giáo Dục (Color Palette)

- **Nền chính**: `#0B1120` (Dark Navy sang trọng).
- **Thẻ nền (Card)**: `#0F172A` (Slate tối), `#1E293B` (Thẻ dưới).
- **Thẻ khẳng định / Đồng biến / Cực đại**: Viền `GREEN_D`, nền `#064E3B` (độ đục 0.35).
- **Thẻ phủ định / Nghịch biến / Cực tiểu**: Viền `RED_D`, nền `#7F1D1D` (độ đục 0.35).
- **Điểm nhấn**: `YELLOW` (tiêu đề), `TEAL_A` (thẻ trên/nhãn), `GREEN_B` (đáp án đúng).
