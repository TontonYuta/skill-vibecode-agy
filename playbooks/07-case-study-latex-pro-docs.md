# Case Study: Soạn Thảo & Tự Động Hóa Tài Liệu LaTeX Đa Môn Học

## 1. Bối cảnh & Yêu cầu
Trong giáo dục và luyện thi phổ thông tại Việt Nam, việc tạo ra các đề thi, phiếu bài tập và lời giải chi tiết đòi hỏi:
1. Độ chuẩn xác cao về mặt ký hiệu toán học, công thức hóa học, sơ đồ mạch điện, và biểu đồ địa lý/lịch sử.
2. Hỗ trợ tiếng Việt Unicode hoàn hảo (bảng mã utf8x/vntex) mà không bị lỗi font hay dấu thanh.
3. Bố cục 2 cột (twocolumn), hộp định lý (tcolorbox), và đồ thị TikZ sắc nét xuất trực tiếp ra PDF chuẩn in ấn.

---

## 2. Cấu trúc Tài liệu Chuẩn Đa Môn Học

### 2.1 Tiền sảnh (Preamble) Tối ưu cho Tiếng Việt
```latex
\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{tikz}
\usepackage{tcolorbox}
\usepackage[top=2cm,bottom=2cm,left=2cm,right=2cm]{geometry}
```

### 2.2 Quy chuẩn TikZ Đồ thị Toán & Vật Lý
- **Trục tọa độ chuẩn**: Luôn gắn mũi tên `-latex`, nhãn $O, x, y$, các vạch chia tọa độ tỉ lệ chuẩn.
- **Hộp bài toán chuyên nghiệp**: Sử dụng `tcolorbox` phân biệt rõ giữa "Đề bài", "Phương pháp tư duy" và "Lời giải chi tiết".

---

## 3. Quy trình Tự Động Hóa (Automation Pipeline)
1. **Agent Sinh Mã LaTeX**: Tự động sinh file `.tex` hoàn chỉnh tuân thủ `latex-document-pro` skill.
2. **Kiểm tra cú pháp (Pre-flight Check)**:
   - Kiểm tra đóng mở ngoặc `\begin{...}` và `\end{...}`.
   - Kiểm tra các ký tự đặc biệt cần escape (`%`, `_`, `&`, `$`).
3. **Biên dịch nội bộ với pdflatex**:
   - Sử dụng TinyTeX hoặc TeX Live cài sẵn trên máy:
     ```bash
     pdflatex -interaction=nonstopmode output.tex
     ```
   - Tự động bắt lỗi biên dịch từ file `.log` để sửa ngay lập tức nếu thiếu gói (packages).
