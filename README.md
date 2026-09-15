# ⚡ Skill Vibecode AGY (Google Antigravity & AI Agents)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform: Antigravity](https://img.shields.io/badge/Platform-Google%20Antigravity-4285F4.svg)](https://deepmind.google)
[![Skills: 8 Core](https://img.shields.io/badge/Skills-8%20Essential%20Core-success.svg)](#-danh-mục-8-bộ-skill-cốt-lõi)
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

## 🧭 Danh Mục 8 Bộ Skill Cốt Lõi

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

---

## 🚀 Cài Đặt 1-Click Cho Toàn Bộ Hệ Thống

Chạy lệnh cài đặt duy nhất để đưa toàn bộ 8 skills, quy chuẩn `AGENTS.md` và hook Auto-Accept vào Antigravity:

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
