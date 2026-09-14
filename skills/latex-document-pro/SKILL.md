---
name: latex-document-pro
description: >-
  Chuẩn biên soạn tài liệu đa môn học LaTeX tiếng Việt chuyên nghiệp (Toán, Lý, Hóa, Sinh,
  Tiếng Anh, Lịch sử, Địa lý) cho đề thi, phiếu bài tập, lời giải chi tiết và giáo án tự động với pdflatex và TikZ.
---

# Quy Trình Biên Soạn Tài Liệu LaTeX Tiếng Việt Chuẩn Cao Cấp Đa Môn

Kỹ năng này chuẩn hóa cấu trúc và quy chuẩn biên soạn tài liệu sư phạm mọi môn học bằng LaTeX hỗ trợ 100% tiếng Việt Unicode, font chữ đồng bộ, chống lỗi biên dịch, và **bố cục trực quan thích ứng linh hoạt theo từng bài học/chủ đề (Adaptive Visual Layouts - không dập khuôn cứng nhắc)**.

---

## 1. Preamble Mẫu Chuẩn Cho Tiếng Việt (pdflatex) & Unicode An Toàn

BẮT BUỘC sử dụng gói `newunicodechar` cùng bảng ánh xạ ký tự Unicode để triệt tiêu hoàn toàn lỗi `! Package inputenc Error: Unicode character ... not set up for use with LaTeX`:

```latex
\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{vietnam}
\usepackage{amsmath,amssymb,amsfonts,amsthm}
\usepackage{tabularx}
\usepackage{array}
\usepackage{geometry}
\geometry{top=1.6cm,bottom=1.6cm,left=1.6cm,right=1.6cm}
\usepackage{graphicx}
\usepackage{tikz}
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}
\usetikzlibrary{arrows.meta, positioning, calc, angles, quotes, patterns}
\usepackage[table]{xcolor}
\definecolor{myblue}{RGB}{0,102,204}
\definecolor{darkgreen}{RGB}{0,128,0}
\definecolor{amber}{RGB}{217,119,6}
\definecolor{purpleaccent}{RGB}{124,58,237}

\usepackage[most]{tcolorbox}
\tcbset{sharp corners}
\usepackage{multicol}
\usepackage{enumitem}
\usepackage{hyperref}

% BẢNG ÁNH XẠ KÝ TỰ UNICODE AN TOÀN TUYỆT ĐỐI
\usepackage{newunicodechar}
\newunicodechar{↗}{\ensuremath{\nearrow}}
\newunicodechar{↘}{\ensuremath{\searrow}}
\newunicodechar{→}{\ensuremath{\rightarrow}}
\newunicodechar{←}{\ensuremath{\leftarrow}}
\newunicodechar{↔}{\ensuremath{\leftrightarrow}}
\newunicodechar{⇒}{\ensuremath{\Rightarrow}}
\newunicodechar{⇔}{\ensuremath{\Leftrightarrow}}
\newunicodechar{•}{\ensuremath{\bullet}}
\newunicodechar{≤}{\ensuremath{\le}}
\newunicodechar{≥}{\ensuremath{\ge}}
\newunicodechar{≠}{\ensuremath{\ne}}
\newunicodechar{≈}{\ensuremath{\approx}}
\newunicodechar{±}{\ensuremath{\pm}}
\newunicodechar{×}{\ensuremath{\times}}
\newunicodechar{÷}{\ensuremath{\div}}
\newunicodechar{∞}{\ensuremath{\infty}}
\newunicodechar{°}{\ensuremath{^\circ}}
\newunicodechar{℃}{\ensuremath{^\circ\mathrm{C}}}

% ====================================================
% BỘ MACRO BỐ CỤC TRỰC QUAN THÍCH ỨNG (VISUAL MACROS)
% ====================================================

% 1. Câu hỏi kèm hình vẽ / đồ thị bên cạnh (2 cột minipage trực quan)
\newcommand{\cauhoicohinh}[3]{%
\vspace{6pt}\noindent
\begin{minipage}[t]{0.65\linewidth}
    \textbf{Câu #1.} #2
\end{minipage}\hfill
\begin{minipage}[t]{0.32\linewidth}
    \centering\vspace{0pt}
    #3
\end{minipage}\par
\vspace{4pt}
}

% 2. Hệ thống thẻ màu sư phạm phân tầng
\newcommand{\hopkienthuc}[2]{%
\begin{tcolorbox}[colback=blue!4!white,colframe=myblue,title=\textbf{#1},fonttitle=\bfseries]
#2
\end{tcolorbox}
}
\newcommand{\phuongphap}[2]{%
\begin{tcolorbox}[colback=green!4!white,colframe=darkgreen,title=\textbf{Phương pháp giải: #1},fonttitle=\bfseries]
#2
\end{tcolorbox}
}
\newcommand{\luuy}[2]{%
\begin{tcolorbox}[colback=orange!5!white,colframe=amber,title=\textbf{Lưu ý & Bẫy đề thi: #1},fonttitle=\bfseries]
#2
\end{tcolorbox}
}
\newcommand{\meonhanh}[2]{%
\begin{tcolorbox}[colback=purple!4!white,colframe=purpleaccent,title=\textbf{Mẹo giải nhanh: #1},fonttitle=\bfseries]
#2
\end{tcolorbox}
}
\newcommand{\doanvan}[2]{%
\begin{tcolorbox}[colback=blue!3!white,colframe=myblue!70!black,title=\textbf{#1},fonttitle=\bfseries]
#2
\end{tcolorbox}
}

% 3. Không gian làm bài trực quan cho học sinh
\newcommand{\dongke}[1][4]{%
\par\vspace{2mm}\textit{Bài làm.}\par
\foreach \i in {1,...,#1}{\vspace{4.5mm}\noindent\makebox[\linewidth]{\dotfill}\par}\vspace{2mm}
}
\newcommand{\khungnhap}[1][3.5cm]{%
\par\vspace{2mm}
\noindent\begin{tcolorbox}[colback=white,colframe=gray!40!white,arc=1.5mm,height=#1,valign=top,boxrule=0.6pt,borderline={0.5pt}{0pt}{dashed,gray!60!black}]
\small\color{gray!70!black}\textit{Không gian vẽ hình & nháp bài làm...}
\end{tcolorbox}
\vspace{2mm}
}

% 4. Bộ macro đáp án linh hoạt chống tràn dòng
\newcommand{\dapan}[4]{
  \begin{tabularx}{\linewidth}{XXXX}
    \textbf{A.} #1 & \textbf{B.} #2 & \textbf{C.} #3 & \textbf{D.} #4
  \end{tabularx}
}
\newcommand{\dapanHaiCot}[4]{
  \begin{tabularx}{\linewidth}{XX}
    \textbf{A.} #1 & \textbf{B.} #2 \\
    \textbf{C.} #3 & \textbf{D.} #4
  \end{tabularx}
}
\newcommand{\dapanMotCot}[4]{
  \begin{tabularx}{\linewidth}{X}
    \textbf{A.} #1 \\
    \textbf{B.} #2 \\
    \textbf{C.} #3 \\
    \textbf{D.} #4
  \end{tabularx}
}
```

---

## 2. Nguyên Tắc Bố Cục Trực Quan Theo Từng Chủ Đề (Không Cứng Nhắc)

Không áp dụng máy móc một mẫu duy nhất cho mọi tài liệu. Bố cục phải thích ứng tự nhiên theo đặc thù từng chủ đề:

### 2.1 Chủ đề Hình học Không gian & Đồ thị Hàm số
- **Bố cục 2 cột song song (`minipage`)**:
  * Cột trái (65% chiều rộng): Đề bài câu hỏi, dữ kiện và 4 phương án trắc nghiệm.
  * Cột phải (32% chiều rộng): Hình vẽ TikZ không gian (đỉnh, nét đứt `[dashed]`, nét liền `[thick]`, góc vuông `\pic`) hoặc đồ thị hàm số `pgfplots`.
  * Dùng macro `\cauhoicohinh{số câu}{nội dung}{hình TikZ}`.
- **TUYỆT ĐỐI KHÔNG** đặt hình vẽ lẻ loi ở một dòng riêng bên dưới chiếm trọn trang giấy trong khi hai bên để trắng lãng phí.

### 2.2 Chủ đề Lý Thuyết & Khảo Sát Biến Thiên
- **Bảng biến thiên 3 tầng LaTeX chuẩn mực**:
  ```latex
  \renewcommand{\arraystretch}{1.3}
  \begin{array}{|c|ccccccc|}
  \hline
  x & -\infty & & x_1 & & x_2 & & +\infty \\
  \hline
  y' & & + & 0 & - & 0 & + & \\
  \hline
  & & & y_{CD} & & & & +\infty \\
  y & & \nearrow & & \searrow & & \nearrow & \\
  & -\infty & & & & y_{CT} & & \\
  \hline
  \end{array}
  ```
- **Phân tầng thị giác bằng thẻ màu**:
  * Lý thuyết trọng tâm: `\hopkienthuc{Tên định lý}{Nội dung}`
  * Phương pháp giải bài toán: `\phuongphap{Dạng toán}{Các bước giải}`
  * Cảnh báo bẫy sai lầm: `\luuy{Chú ý / Sai lầm}{...}`

### 2.3 Chủ đề Phiếu Bài Tập (Worksheet)
- **Header tinh gọn (Compact Visual Header Box)**: Bố trí khung thông tin học sinh (Họ tên, Lớp, Ngày, Điểm số, Mã đề) gọn gàng trong 3-4cm đầu trang 1. Bắt đầu làm bài ngay từ trang 1, TUYỆT ĐỐI KHÔNG làm trang bìa `titlepage` riêng gây lãng phí giấy in.
- **Không gian làm bài trực quan**:
  * Bài đại số, giải phương trình, tính toán: Dùng `\dongke[3]` hoặc `\dongke[4]`.
  * Bài hình học cần vẽ hình: Dùng `\khungnhap[3.5cm]`.

### 2.4 Chủ đề Đề Thi Chuẩn Bộ GD&ĐT 2025--2026
- Cấu trúc 3 phần rõ ràng:
  * Phần I: Trắc nghiệm 4 lựa chọn (A, B, C, D) -> dùng `\dapan` hoặc `\cauhoicohinh`.
  * Phần II: Trắc nghiệm Đúng/Sai (4 mệnh đề a, b, c, d) -> dùng `\yDungSai`.
  * Phần III: Trả lời ngắn (điền kết quả) -> dùng `\traLoiNgan`.
- Bảng đáp án ma trận và hướng dẫn giải cô đọng, dứt khoát.

---

## 3. Điều Phối Dung Lượng & Chống Cắt Cụt Token

- Hướng dẫn giải chi tiết phải tập trung vào bước ngoặt logic then chốt và đáp số cuối cùng, tránh giải thích dài dòng.
- Đảm bảo tài liệu được đóng `\end{document}` hoàn chỉnh 100%.

---

## 4. Lệnh Biên Dịch Local Fast Render

```bash
pdflatex -interaction=nonstopmode -output-directory=~/Downloads tailieu.tex
```
Chạy 2 lượt để hoàn thiện tham chiếu chéo và số trang.
