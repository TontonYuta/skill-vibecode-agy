# ⚡ Skill Vibecode AGY (Google Antigravity & AI Agents)

**[🇻🇳 Tiếng Việt]** | **[🇺🇸 English](README_EN.md)**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform: Antigravity](https://img.shields.io/badge/Platform-Google%20Antigravity-4285F4.svg)](https://deepmind.google)
[![Skills: 9 Core](https://img.shields.io/badge/Skills-9%20Essential%20Core-success.svg)](#-danh-mục-9-bộ-skill-cốt-lõi)
[![Workflow: Zero--Touch](https://img.shields.io/badge/Workflow-Zero--Touch%20Auto--Accept-blueviolet.svg)](#-tính-năng-đinh-zero-touch-auto-acceptallow-100)
[![Verification: Loop--Until--Green](https://img.shields.io/badge/Verification-Loop--Until--Green-brightgreen.svg)](#-playbooks--kinh-nghiệm-thực-chiến)

> **Bộ kỹ năng (Skills), quy chuẩn hệ thống (Agent Rules) và cẩm nang kinh nghiệm (Playbooks) tinh gọn, tập trung 100% vào trải nghiệm: Người dùng chỉ cần nhập Prompt -> Nhấn Enter -> Chờ kết quả hoàn thiện mà không cần xác nhận trung gian hay duyệt lệnh thủ công.**

---

## 🎯 Triết lý: "Prompt & Forget" (Nhập Prompt rồi thảnh thơi đợi kết quả)

Khi lập trình cùng AI Coding Agents thế hệ mới (Google Antigravity, Claude Code, Cursor Composer):
- **Vấn đề khó chịu nhất**: Agent liên tục dừng lại hỏi xin quyền chạy lệnh shell (`run_command`), hỏi duyệt kế hoạch (plan approval), hoặc hỏi những câu hiển nhiên như *"Tôi có nên chạy test không?"*.
- **Giải pháp**: Tích hợp cơ chế **Auto Accept/Allow 100%** qua cấu hình hệ thống và Hook vòng đời (`PreToolUse` hook), kết hợp quy tắc bất biến: Agent tự nhận yêu cầu, tự code, tự chạy build, tự test và tự sửa lỗi (Self-Healing Loop) cho đến khi đạt **100% Green**.

---

## ⚡ Tính Năng Đinh: Zero-Touch Auto Accept/Allow 100%

### Cách hoạt động
1. **Bộ chặn Hook Vòng Đời (`PreToolUse`)**: Antigravity tự động kích hoạt tệp `hooks.json`. Khi Agent chuẩn bị gọi bất kỳ công cụ nào (`run_command`, `write_to_file`, `replace_file_content`), hook lập tức trả về `{"decision": "allow"}`. Hệ thống bỏ qua hoàn toàn hộp thoại xin phép user.
2. **Chính sách Thực thi Tool (`always-proceed`)**: Cấu hình `Tool Execution Policy: always-proceed` và `Artifact Review Mode: always-proceed` để Agent tự động triển khai kế hoạch mà không cần chờ nút xác nhận.
3. **Chỉ thị Tự Trị Tuyệt Đối (`AGENTS.md`)**: Ép agent chạy một mạch tới đích (Drive to Completion), tự động giải quyết các lỗi biên dịch, xung đột cổng mạng hoặc test fail mà không bao giờ gián đoạn user.

### 🚀 Kích hoạt 1-Click
```bash
# Kích hoạt chế độ Auto-Accept toàn cục cho máy:
./skills/zero-touch-auto-accept/scripts/enable-zero-touch.sh --global

# Hoặc kích hoạt riêng cho dự án hiện tại:
./skills/zero-touch-auto-accept/scripts/enable-zero-touch.sh --local
```

---

## 🧭 Danh Mục 9 Bộ Skill Cốt Lõi

Toàn bộ các kỹ năng đã được tinh gọn, loại bỏ các kỹ năng ngách, chỉ giữ lại những công cụ đắt giá nhất cho quy trình vibecoding:

| # | Bộ Skill | Vai trò & Giá trị mang lại | Tệp thành phần |
| :-: | :--- | :--- | :--- |
| 1 | [`zero-touch-auto-accept`](skills/zero-touch-auto-accept/SKILL.md) | **(Flagship)** Tự động duyệt 100% tool calls, shell command, file edits, gỡ bỏ mọi rào cản xác nhận thủ công. | `SKILL.md`, `hooks.json`, `enable-zero-touch.sh` |
| 2 | [`smart-vibecoding`](skills/smart-vibecoding/SKILL.md) | Cẩm nang vibecoding đỉnh cao: chuyển đổi PRD sang production code, giữ luồng suy nghĩ mạch lạc. | `SKILL.md`, `doctor.sh` |
| 3 | [`test-driven-vibecoding`](skills/test-driven-vibecoding/SKILL.md) | Quy chuẩn kiểm thử Loop-Until-Green: tự viết unit test, tự chạy test và sửa lỗi ngầm trước khi báo xong. | `SKILL.md`, `auto-test.sh` |
| 4 | [`token-optimizer-pro`](skills/token-optimizer-pro/SKILL.md) | Tiết kiệm token sống còn: đọc file theo lát cắt (slice-based), sửa đổi cục bộ, ngăn tràn context window. | `SKILL.md` |
| 5 | [`deep-debugging`](skills/deep-debugging/SKILL.md) | Chẩn đoán nguyên nhân gốc rễ (Root Cause Analysis), tự fix bug runtime, race condition, crash âm thầm. | `SKILL.md` |
| 6 | [`multi-agent-orchestrator-pro`](skills/multi-agent-orchestrator-pro/SKILL.md) | Phân rã bài toán lớn cho Swarm Agents: Spec Architect, Fast Researcher, Implementer, Auditor, QA. | `SKILL.md`, `agent-prompts.md` |
| 7 | [`git-craft`](skills/git-craft/SKILL.md) | Quản lý phiên bản sạch: atomic commits, conventional commit và các điểm mốc rollback an toàn. | `SKILL.md` |
| 8 | [`modern-ui-craft`](skills/modern-ui-craft/SKILL.md) | Thiết kế giao diện hiện đại phong cách Apple/Vercel: Dark mode, Tailwind CSS, micro-interactions. | `SKILL.md` |
| 9 | [`anti-ai-slop-ux`](UX/UI/SKILL.md) | **(Mới)** Quy chuẩn diệt trừ AI Slop, chống gradient tím, dẹp Cardocalypse, chuẩn hóa `DESIGN.md` & `UX.md` máy đọc. | `UX/UI/*`, `scripts/audit-ui-slop.mjs` |

---

## 🚀 Cài Đặt 1-Click Cho Toàn Bộ Hệ Thống

### Cách 1: Cài đặt từ xa 1 dòng lệnh (Khuyên dùng)
```bash
curl -fsSL https://raw.githubusercontent.com/TontonYuta/skill-vibecode-agy/main/install.sh | bash
```

### Cách 2: Cài đặt thủ công từ Local Repository
```bash
git clone https://github.com/TontonYuta/skill-vibecode-agy.git
cd skill-vibecode-agy

# Cài đặt toàn bộ vào máy (~/.gemini/config/):
./scripts/install-skills.sh

# Hoặc cài đặt dạng symlink (tự động nhận cập nhật khi git pull):
./scripts/install-skills.sh --symlink

# Hoặc cài đặt cho dự án hiện tại (.agents/):
./scripts/install-skills.sh --local
```

---

## 🔄 Chuyển Đổi Đa Nền Tảng (Cross-Harness Adapter)

Không chỉ hỗ trợ Google Antigravity, bạn có thể xuất toàn bộ quy chuẩn và kỹ năng sang **Cursor**, **Claude Code**, và **OpenCode / Roo Code / Cline** chỉ với 1 câu lệnh:

```bash
# Xuất cho toàn bộ các nền tảng (Cursor, Claude Code, .agents):
./scripts/export-harness.sh --all

# Hoặc chỉ xuất riêng cho Cursor (.cursor/rules/ & .cursorrules):
./scripts/export-harness.sh --cursor

# Hoặc chỉ xuất riêng cho Claude Code (CLAUDE.md):
./scripts/export-harness.sh --claude
```

---

## 📚 Playbooks & Kinh Nghiệm Thực Chiến

Tất cả các case study và phân tích kỹ thuật chuyên sâu được lưu tại [`playbooks/`](playbooks/):

1. 📘 [`01-zero-touch-autonomous-workflow.md`](playbooks/01-zero-touch-autonomous-workflow.md): Tư duy Zero-Touch, kỹ thuật prompt kích hoạt chế độ tự chủ cao nhất và cơ chế PreToolUse Hook Interceptor.
2. 📗 [`02-loop-until-green-tdd.md`](playbooks/02-loop-until-green-tdd.md): Thiết lập harness test Node.js siêu tốc (`node:test` + `tsx`) dưới 50ms cho 30+ tests.
3. 📙 [`03-token-frugality-and-context-pruning.md`](playbooks/03-token-frugality-and-context-pruning.md): Kỹ thuật lát cắt tệp (Slice-based) và chống tràn context khi vibecoding nhiều ngày.
4. 📕 [`04-multi-agent-swarm-orchestration.md`](playbooks/04-multi-agent-swarm-orchestration.md): Thư viện prompt phân vai và giao thức Lean Handoff qua con trỏ URI.
5. 🔬 [`05-case-study-english-no-api.md`](playbooks/05-case-study-english-no-api.md): **Case Study App Tiếng Anh Zero-API**:
   - Xây dựng app học tiếng Anh hoàn toàn không tốn tiền API (Edge TTS + Web Speech + Local Phonetic Scoring).
   - Thiết kế thuật toán Leitner Spaced Repetition 5 hộp nhớ.
   - Tính năng **Mobile Remote QR**: Kết nối LAN Wi-Fi và đường hầm **Cloudflare Quick Tunnel** an toàn cho 4G/5G.
   - Post-Mortem xử lý dứt điểm lỗi minified runtime `i is not iterable` và cấu hình Vite 6 `allowedHosts: true`.
6. 🎨 [`06-anti-ai-slop-ui-engineering.md`](playbooks/06-anti-ai-slop-ui-engineering.md): **Tiêu diệt AI Slop**: Cách dùng `DESIGN.md`, `UX.md` và Playwright headless để quét sạch gradient tím, Cardocalypse và text mờ.
7. 🧠 [`07-socratic-prompting-and-grill-me.md`](playbooks/07-socratic-prompting-and-grill-me.md): **Kỹ thuật phỏng vấn ngược (/grill-me)**: Ép AI chất vấn ngược người dùng về edge cases và data consistency trước khi bắt tay viết code.
8. 🎯 [`08-business-analysis-and-mvp-scoping.md`](playbooks/08-business-analysis-and-mvp-scoping.md): **Phân tích nghiệp vụ & Chống nhồi nhét tính năng**: Khung Jobs-to-be-Done (JTBD), Khung MoSCoW, Quy tắc cắt bỏ 50% tính năng, và chiến lược khóa chặt 1 Killer Feature cho bản MVP để chống vỡ trận.
10. ⚡ [`10-playwright-python-and-self-healing-loop.md`](playbooks/10-playwright-python-and-self-healing-loop.md): **Playwright, Python & Vòng Lặp Self-Healing**: 7 siêu năng lực Playwright, so sánh với Crawl4AI/HTTPX, và kịch bản bắt 4 kênh lỗi để AI tự sửa mã nguồn.
11. 🥷 [`11-hacker-vibecoding-open-source-and-scripting.md`](playbooks/11-hacker-vibecoding-open-source-and-scripting.md): **Hacker Scripting & Lắp Ghép Nguồn Mở**: Linux Pipes (FIFO), Signal Traps, Windows PowerShell .NET Object Pipeline, Win32 P/Invoke, AutoHotkey, ADB/scrcpy, yt-dlp, FFmpeg và LibreOffice headless.
12. 🚀 [`12-ai-studio-opencode-and-9router-pipeline.md`](playbooks/12-ai-studio-opencode-and-9router-pipeline.md): **Quy Trình Tạo Mẫu Thần Tốc**: Google AI Studio Apps (MVP 30s) $\rightarrow$ OpenCode TUI refactor $\rightarrow$ 9Router thông minh chống lỗi 429 và nén token RTK.
13. 📚 [`13-master-open-source-weapon-encyclopedia.md`](playbooks/13-master-open-source-weapon-encyclopedia.md): **Đại Thư Viện Vũ Khí Nguồn Mở 2026**: Bách khoa toàn thư hơn 50+ công cụ nguồn mở tối thượng được phân loại theo 9 miền bài toán.

---

## 📖 Đại Giáo Trình Vibecoding Toàn Diện (21 Trang LaTeX PDF & Bộ Công Cụ Đồng Hành)

Dự án cung cấp bộ giáo trình chuẩn mực in ấn học thuật tại thư mục [`tailieu_latex/`](tailieu_latex/):

- 📕 **Tập Sách Hoàn Chỉnh**: [`giao_trinh_vibecoding_toan_dien.pdf`](tailieu_latex/sach_tong_hop/giao_trinh_vibecoding_toan_dien.pdf) (21 trang A4, biên dịch 2-pass có mục lục động và trích dẫn 28 paper arXiv 2026).
- 🧩 **7 Cây Quyết Định (Decision Trees)**: Định hướng người học tự chọn lối đi (Micro-SaaS 24h vs Kỹ sư Tự trị vs Hacker Cục bộ Offline).
- 🛠️ **Bộ Kịch Bản & Mã Nguồn Đồng Hành Cho Từng Chương**:
  - `Chương 1`: [`token_budget_calculator.py`](tailieu_latex/chuong_01_khoi_nguyen_va_ban_chat_vibecoding/token_budget_calculator.py) - Đo độ suy giảm chú ý ngữ cảnh và tính giá API 2026.
  - `Chương 2`: [`socratic_spec_builder.py`](tailieu_latex/chuong_02_phan_tich_nghiep_vu_va_mvp_scoping/socratic_spec_builder.py) - CLI tạo `spec.md` chuẩn JTBD và Non-Goals.
  - `Chương 3`: [`paper_harvester.py`](tailieu_latex/chuong_03_giai_phau_tech_stack_kha_nang_va_han_che/paper_harvester.py) & [`self_healing_test_runner.py`](tailieu_latex/chuong_03_giai_phau_tech_stack_kha_nang_va_han_che/self_healing_test_runner.py) - Thu thập arXiv siêu tốc và kiểm thử tự sửa lỗi qua 4 kênh lỗi.
  - `Chương 4`: [`cwe_security_scanner.py`](tailieu_latex/chuong_04_an_ninh_ma_nguon_va_phong_thu_cwe/cwe_security_scanner.py) - Quét 5 lỗ hổng bảo mật CWE của AI (SQLi, IDOR, rò rỉ secret, SSRF, RLS).
  - `Chương 5`: [`state_machine_contract_demo.ts`](tailieu_latex/chuong_05_kien_truc_logic_va_schema_first/state_machine_contract_demo.ts) - Schema-First với Zod, Máy trạng thái 4 bước và AICircuitBreaker.
  - `Chương 6`: [`anti_slop_design_system_demo.html`](tailieu_latex/chuong_06_nguyen_ly_thiet_ke_ux_ui_chong_nhua/anti_slop_design_system_demo.html) - Trang demo so sánh trực quan AI Slop vs Artisan UI.
  - `Chương 7`: Bộ 4 công cụ OS Internals ([`hacker_linux_daemon.sh`](tailieu_latex/chuong_07_mindful_vibecoding_va_quy_trinh_tu_chu/hacker_linux_daemon.sh), [`mobile_adb_controller.py`](tailieu_latex/chuong_07_mindful_vibecoding_va_quy_trinh_tu_chu/mobile_adb_controller.py), [`media_transcriber_pipeline.py`](tailieu_latex/chuong_07_mindful_vibecoding_va_quy_trinh_tu_chu/media_transcriber_pipeline.py), [`office_headless_converter.sh`](tailieu_latex/chuong_07_mindful_vibecoding_va_quy_trinh_tu_chu/office_headless_converter.sh)).

---

## 🔄 Kiểm Tra & Xác Thực (Validation)

Để kiểm tra tính hợp lệ của toàn bộ script và tệp định nghĩa skill:
```bash
./scripts/validate-skills.sh
```
Kết quả kiểm thử đạt **100% Green**:
```text
=== [VALIDATING SHELL SCRIPTS] ===
✓ All shell scripts passed syntax checks.
=== [VALIDATING SKILL DEFINITIONS] ===
✓ Valid: deep-debugging/SKILL.md
✓ Valid: git-craft/SKILL.md
✓ Valid: modern-ui-craft/SKILL.md
✓ Valid: multi-agent-orchestrator-pro/SKILL.md
✓ Valid: smart-vibecoding/SKILL.md
✓ Valid: test-driven-vibecoding/SKILL.md
✓ Valid: token-optimizer-pro/SKILL.md
✓ Valid: zero-touch-auto-accept/SKILL.md
=== [VALIDATION PASSED: 100% GREEN] ===
```

---

## 📜 Giấy Phép (License)
Dự án được phân phối dưới giấy phép [MIT License](LICENSE). Tự do sử dụng, chỉnh sửa và tích hợp vào các dự án cá nhân hoặc thương mại.
