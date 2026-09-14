---
name: manim-layout-checker-pro
description: >-
  Quy chuẩn Kiểm Thẩm Bố Cục, Dual-Zone Grid, Chống Đè Chữ và Giao Thức AI Double-Check 2 Lớp trong Manim CE.
---

# Quy Chuẩn & Giao Thức AI Double-Check Bố Cục & Nội Dung Manim CE

Kỹ năng này chuẩn hóa quy trình **Thẩm định kép (Double-Check Protocol)** kết hợp giữa **Bộ lọc Heuristic 0ms** và **AI Inspector** nhằm loại bỏ 100% lỗi bố cục, lỗi rớt dòng công thức và va chạm thị giác trước khi render video bài giảng toán học.

---

## 1. Giao Thức Double-Check 2 Lớp (Dual-Layer Architecture)

```
[Mã Manim Python scene.py]
          │
          ▼
┌───────────────────────────────────────────────┐
│ LỚP 1: BỘ LỌC STATIC HEURISTIC (0ms, Local)   │
│ - Quét fit_width, công thức Intro, Axes cao   │
│ - Quét ALL CAPS, unicode mũ, font_size < 20   │
│ - Tự động sửa nhanh (Auto-Sanitizer)          │
└──────────────────────┬────────────────────────┘
                       │ Báo cáo Linter Report
                       ▼
┌───────────────────────────────────────────────┐
│ LỚP 2: AI DOUBLE-CHECK INSPECTOR (Giám định)  │
│ - Soi tính cân bằng thị giác Top vs Bottom    │
│ - Soi độ chuẩn sư phạm, thuật ngữ, bẫy trắc   │
│   nghiệm và khớp thoại TTS (~2.85 từ/giây)    │
│ - Xuất mã hoàn thiện 100% (Green-Pass Code)   │
└───────────────────────────────────────────────┘
```

---

## 2. Bảng Checklist 17 Điểm Vàng Bắt Buộc (Audit Checklist)

### Nhóm A: Bố Cục Hình Học & Tối Giản Khung Viền (Layout, Safe Zone & Anti-Box-Inception)
1. **Container Cards 93% màn hình**: Header Bar ($y \sim 7.05$), Top Card ($y \sim 3.15$, height 6.4), Bottom Card ($y \sim -3.75$, height 6.6), Outro Card (height 13.6).
2. **fit_width an toàn**: Mọi khối nội dung và `intro_core_rule` BẮT BUỘC gọi `fit_width(group, 7.6-7.8)`.
3. **Tối giản khung viền & Triệt tiêu box nhãn (Zero Redundant Boxes & Anti-Label-Box)**: Mỗi vùng chỉ có ĐÚNG 1 thẻ ngoài. TUYỆT ĐỐI CẤM bọc box/pill quanh các nhãn phân loại như "Ví dụ minh họa", "Ví dụ", "Dạng 1", "Dạng 2", "Thực chiến" (chỉ dùng Text trơn font_size=20-22). TUYỆT ĐỐI CẤM bọc box quanh: tiêu đề thẻ, đề bài, các bước giải, bảng biến thiên. CHỈ DUY NHẤT 1 hộp xanh khoanh đáp án đúng `SurroundingRectangle(opt_correct, buff=0.12-0.14)`.
4. **Công thức Intro đơn dòng (Anti-2x2)**: Mọi định lý Max/Min, Đơn điệu, Cực trị nằm trên ĐÚNG 1 DÒNG ĐƠN trong 1 `MathTex`. CẤM ngắt dòng `\\` và CẤM tách thành nhiều `MathTex`.
5. **Giới hạn hệ trục Axes**: `x_length <= 7.2`, `y_length <= 4.0` (CẤM đặt `y_length > 4.2` gây đè tiêu đề Top Card).
6. **Khóa 4 đáp án liền khối**: Dạng 4x1, 2x2 (khóa 2 cột thẳng tắp) hoặc 1x4. CẤM để chữ cái nhãn A/B/C/D đứng cô độc một dòng.
7. **Zero-Overlap**: `FadeOut` dọn sạch 100% giữa các cảnh. Riêng Outro cuối video: GIỮ NGUYÊN `self.wait(3.0)`, CẤM `FadeOut` làm đen màn hình.

### Nhóm B: Phân Cấp Tiêu Đề, Typography & Chống Thu Nhỏ (Title Hierarchy & Anti-Shrink)
8. **Phân cấp tiêu đề chuẩn (Title Hierarchy Guard)**:
   - Tiêu đề Intro: `28 - 32` BOLD, Sentence case (CẤM > 32).
   - Tiêu đề Header Bar: `22 - 24` BOLD.
   - **Tiêu đề Thẻ Card (`top_title`, `c1_title`...)**: BẮT BUỘC `20 - 22` BOLD (CẤM font_size > 22!). Đặt tại `.next_to(card.get_top(), DOWN, buff=0.18)`. CẤM bọc box quanh tiêu đề thẻ!
9. **Kết luận bài tập tinh gọn (Lean 1-Line Conclusion)**:
   - 1 dòng đơn cô đọng: `VGroup(Text("➜ ... Chọn", font_size=22), MathTex(r"\mathbf{...}", font_size=24)).arrange(RIGHT, buff=0.15)`.
   - CẤM font_size > 24 cho kết luận, CẤM tạo thẻ con riêng cho kết luận.
10. **Chống thu nhỏ nội dung (Anti-Shrink Protocol)**:
   - Mọi dòng Text/MathTex KHÔNG dài quá 50-55 ký tự (ngắt thành 2 dòng ngắn nếu dài) để `fit_width` không co nhỏ chữ li ti!
   - Cỡ chữ chuẩn: MathTex `24 - 28`, diễn giải `22` (CẤM `font_size < 22`), BBT `22 - 24`.
   - CẤM TUYỆT ĐỐI dùng `.scale(< 0.85)` trên các khối nội dung thẻ. Dùng `buff=0.14 - 0.18`.
11. **Sentence case & Font chuẩn**: `Times New Roman` (hoặc `Be Vietnam Pro`). CẤM viết hoa toàn bộ (ALL CAPS).
12. **Chỉ số trên/dưới**: 100% số mũ ($x^2, x^3$), chỉ số ($x_0$), đạo hàm ($y'$) dùng `MathTex(r"...")`. CẤM unicode mũ trong `Text(...)`.

### Nhóm C: Sư Phạm & Thoại (Pedagogy & Sync)
11. **VOICEOVER_SCRIPT**: Số từ $\approx$ Thời lượng (giây) $\times 2.85$.
12. **Thanh trạng thái bắt điểm cực trị**: `status_badge` có `abs(t - x_0) < 0.16` để nhận diện cực đại/cực tiểu.
13. **Độ sâu sư phạm**: Phân biệt rõ $x_0, y_0, M(x_0; y_0)$ và chỉ ra bẫy nghiệm bội chẵn.
14. **Outro LaggedStart**: 3 bí kíp xuất hiện tuần tự lướt từ trái sang (`lag_ratio=0.3`), pop-up logo (`scale=0.85`).
15. **Triệt tiêu từ ngữ Meta (Zero Meta Jargon)**: TUYỆT ĐỐI CẤM từ "RAG", "Trích từ tài liệu", "Theo tài liệu đính kèm" trong `Text(...)` và `VOICEOVER_SCRIPT`.

### Nhóm D: Chống Ảo Giác Cú Pháp (Zero-Hallucination Guard)
16. Không dùng `font_color` (dùng `color=...`).
17. Không nhét `ImageMobject` vào `VGroup` (phải dùng `Group`).
18. Không dùng `Transform` giữa 2 `MathTex` lệch độ dài (dùng `ReplacementTransform`).

---

## 3. Mẫu Prompt Gọi AI Double-Check Tự Động

Khi thực hiện lượt Double-Check, truyền mã nguồn và danh sách lỗi vào prompt mẫu:

```markdown
Đóng vai Chuyên gia Giám định Kỹ thuật Hoạt họa Manim CE & Sư phạm Studio (Yuta Academy QA Inspector).
Nhiệm vụ của bạn là THẨM ĐỊNH KÉP (DOUBLE-CHECK) VÀ TỰ ĐỘNG CHỮA LỖI HOÀN THIỆN 100% cho file mã nguồn Manim Python:

1. Rà soát lại toàn bộ 17 Quy Tắc Vàng (bố cục Dual-Zone, fit_width, công thức Intro đơn dòng, 4 đáp án liền khối, cỡ chữ >= 20, thanh trạng thái bắt điểm cực trị, an toàn Outro).
2. Tự động sửa triệt để mọi lỗi rớt dòng, tràn viền hoặc xung đột thị giác.
3. Xuất toàn bộ file mã nguồn Manim Python (scene.py) HOÀN THIỆN 100% trong duy nhất 1 khối mã ```python ... ```.
```
