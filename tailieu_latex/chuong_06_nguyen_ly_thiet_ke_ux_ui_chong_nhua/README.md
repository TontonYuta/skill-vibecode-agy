# Chương 6: Kỹ Nghệ Thiết Kế UX/UI Chống "Nhựa" (Anti-AI-Slop)
## Từ Thẩm Mỹ Sáo Rỗng Đến Trải Nghiệm Chuẩn Mực Nghệ Nhân & Bản Đồ 3 Hướng Đi Thực Chiến

### 1. Tổng quan chương
Chương này bóc tách tận gốc rễ 7 căn bệnh thẩm mỹ của AI Slop (Purple gradient craze, Cardocalypse bo tròn cực đại, Iconitis, Spastic motion, Hyperbolic micro-copy, Spinner-only loading, Empty state amnesia); xác lập hệ thống Design Tokens thủ công đạt chuẩn quốc tế (Linear, Apple HIG); thiết lập tỷ lệ vàng 60-30-10 và nhịp điệu khoảng trắng Lưới 8px; chuẩn hóa công thái học bàn phím (Cmd+K) và Skeleton Loader khớp tỷ lệ; đồng thời cung cấp một cây quyết định giúp người học tự định hình 3 hướng đi sản phẩm chuyên biệt.

### 2. Các nội dung trọng tâm
- **Bóc trần 7 căn bệnh AI Slop**: Phân tích chi tiết tại sao giao diện AI sinh ra thường trông rất rẻ tiền và cách khắc phục triệt để.
- **Hệ thống Design Tokens & Tỷ lệ 60-30-10**:
  - 60% Nền trung tính tĩnh lặng (`#09090b` Deep Zinc / `#ffffff`).
  - 30% Bề mặt phẳng và đường phân cách mỏng 1px (`#18181b`, `#27272a`).
  - 10% Màu nhấn chức năng duy nhất (`#2563eb` Cobalt hoặc `#10b981` Emerald).
- **Nhịp điệu khoảng trắng Lưới 8-Point Grid**:
  - Công thức: $\text{Spacing Token} = n \times 8\text{px}$. Bảng đối chiếu lớp Tailwind CSS từ 4px đến 64px.
- **Phân cấp Typography nghệ nhân**:
  - Inter / Geist Sans / System UI. Thang đo modular scale, `tabular-nums` cho số liệu, và **Luật cấm in hoa toàn bộ (NO ALL-CAPS)**.
- **Công thái học tương tác**:
  - Skeleton Loader đo ni đóng giày khớp từng pixel thay cho Spinner quay vòng.
  - Keyboard-First: Bảng lệnh Cmd+K, điều hướng phím mũi tên, focus rings chuẩn WCAG 2.2.
- **Cây quyết định 3 hướng đi thực chiến**:
  - *Hướng 1: B2B Enterprise & Productivity* (Linear / Raycast Style - dark mode sâu, density cao, phím tắt toàn diện).
  - *Hướng 2: B2C Consumer & Giáo Dục* (Apple / Notion Style - light mode chủ đạo, khoảng thở lớn, thân thiện).
  - *Hướng 3: Developer Tools & Terminal* (TUI Minimalist - Bubble Tea / Textual, font JetBrains Mono).
- **Bảng kiểm toán giao diện (De-Slop Audit Checklist)** 5 điều kiện tiên quyết.

### 3. Tệp thực hành & Mã nguồn đi kèm
- **File chạy thử nghiệm trực tiếp**: [`anti_slop_design_system_demo.html`](./anti_slop_design_system_demo.html) *(Mở trực tiếp trên bất kỳ trình duyệt nào để thấy ngay sự đối lập giữa AI Slop và Artisan UI)*.
- **Tệp nguồn LaTeX**: [`chuong_06_nguyen_ly_thiet_ke_ux_ui_chong_nhua.tex`](./chuong_06_nguyen_ly_thiet_ke_ux_ui_chong_nhua.tex)
- **Tệp xuất bản PDF (A4)**: [`chuong_06_nguyen_ly_thiet_ke_ux_ui_chong_nhua.pdf`](./chuong_06_nguyen_ly_thiet_ke_ux_ui_chong_nhua.pdf) (4 trang, chuẩn in ấn học thuật)
