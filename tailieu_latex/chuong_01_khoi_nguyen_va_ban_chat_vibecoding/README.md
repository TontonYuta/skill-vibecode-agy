# Chương 1: Khởi Nguyên và Bản Chất Vibecoding
## Sự Chuyển Dịch Từ Thợ Gõ Mã Lệnh Sang Tổng Kiến Trúc Sư Hệ Thống

### 1. Tổng quan chương
Chương này bóc tách nguồn gốc lịch sử, bản chất nhận thức học và cơ chế vận hành nền tảng của phương pháp **Vibecoding** (*Agentic Software Engineering*). Tài liệu phân tích nguyên nhân tại sao vibecoding ngẫu hứng dẫn đến nợ nhận thức (*Cognitive Debt* - arXiv:2609.09022) và bẫy tái triển khai (*Reimplementation Trap* - arXiv:2609.29410), từ đó định vị lại vai trò của người lập trình như một **Lead Architect**.

### 2. Các nội dung trọng tâm
- **Tiến trình 4 giai đoạn**: Autocomplete (Copilot 2021) $\rightarrow$ Chat-Assisted (2023) $\rightarrow$ IDE Agents (Cursor 2024) $\rightarrow$ Autonomous Dual-Loop (Antigravity 2026).
- **Kinh tế học Token & Giới hạn Attention**: Phân tích hiện tượng *Lost-in-the-Middle* khi ngữ cảnh vượt quá 32.000 tokens và cách ngăn chặn ô nhiễm ngữ cảnh (*Context Pollution*).
- **Nguyên tắc Zero-Trust Code Generation**: Mọi dòng mã sinh ra từ AI phải được kiểm chứng tự động qua static typing, unit tests và linter trước khi đưa vào codebase.
- **Bảng đối chiếu Blind Vibecoding vs Mindful Vibecoding**.

### 3. Tệp tài liệu học thuật & Mã nguồn thực hành
- Tệp nguồn LaTeX: [`chuong_01_khoi_nguyen_va_ban_chat_vibecoding.tex`](./chuong_01_khoi_nguyen_va_ban_chat_vibecoding.tex)
- Tệp xuất bản PDF (A4): [`chuong_01_khoi_nguyen_va_ban_chat_vibecoding.pdf`](./chuong_01_khoi_nguyen_va_ban_chat_vibecoding.pdf) (5 trang, chuẩn in ấn học thuật)
- Script thực hành đồng hành: [`token_budget_calculator.py`](./token_budget_calculator.py) - CLI phân tích token cơ sở mã, tính toán ngưỡng suy giảm chú ý và bảng giá API 2026.

### 4. Cây quyết định chọn lộ trình Vibecoding
1. **Lộ trình A: Thần tốc MVP (24h Ship)**: AI Studio Apps + OpenCode TUI + 9Router (Dành cho Indie Hacker, xác thực ý tưởng).
2. **Lộ trình B: Kỹ sư Tự trị (Autonomous Swarm)**: Antigravity CLI / OpenCode Headless + Multi-Agent Swarm + TDD Loop-Until-Green.
3. **Lộ trình C: Hacker Cục bộ (Local-First & Offline)**: Local Ollama (DeepSeek R1) + PocketBase / DuckDB + Bash/Python (Dành cho dữ liệu nhạy cảm, offline 100%).
