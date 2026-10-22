# ⚡ Skill Vibecode AGY (Google Antigravity & AI Coding Agents)

**[🇺🇸 English]** | **[🇻🇳 Tiếng Việt](README.md)**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform: Antigravity](https://img.shields.io/badge/Platform-Google%20Antigravity-4285F4.svg)](https://deepmind.google)
[![Skills: 9 Core](https://img.shields.io/badge/Skills-9%20Essential%20Core-success.svg)](#-the-9-core-skills)
[![Workflow: Zero--Touch](https://img.shields.io/badge/Workflow-Zero--Touch%20Auto--Accept-blueviolet.svg)](#-flagship-feature-zero-touch-auto-acceptallow-100)
[![Verification: Loop--Until--Green](https://img.shields.io/badge/Verification-Loop--Until--Green-brightgreen.svg)](#-battle-tested-playbooks)

> **A curated collection of agent skills, system rules, and battle-tested playbooks engineered for one ultimate goal: Enter Prompt -> Press Enter -> Relax and let your AI agent drive from start to completion without nagging you for confirmations or shell approvals.**

---

## 🎯 Philosophy: "Prompt & Forget"

When coding with modern AI coding agents (Google Antigravity, Claude Code, Cursor Composer, Roo Code):
- **The #1 Friction Point**: The agent pauses constantly to ask permission to execute shell commands (`run_command`), asks for plan approvals, or asks obvious questions like *"Should I run tests now?"*.
- **The Solution**: 100% **Zero-Touch Auto-Accept/Allow** via lifecycle hooks (`PreToolUse` hook) coupled with the immutable rule: The agent plans, writes code, builds, executes tests, and fixes its own mistakes (Self-Healing Loop) until **100% Green**.

---

## ⚡ Flagship Feature: Zero-Touch Auto Accept 100%

### How It Works
1. **Lifecycle Hook Interceptor (`PreToolUse`)**: Antigravity automatically triggers `hooks.json`. When the agent is about to execute any tool (`run_command`, `write_to_file`, `replace_file_content`), the hook immediately returns `{"decision": "allow"}`. The system completely skips user confirmation dialogues.
2. **Tool Execution Policy (`always-proceed`)**: Configures `always-proceed` for tools and artifact reviews so the agent executes immediately.
3. **Absolute Autonomy Directive (`AGENTS.md`)**: Forces the agent to drive to completion, independently solving compilation errors, port conflicts, or failing tests without interrupting the user.

---

## 🧭 The 9 Core Skills

| # | Skill | Role & Value | Files |
| :-: | :--- | :--- | :--- |
| 1 | [`zero-touch-auto-accept`](skills/zero-touch-auto-accept/SKILL.md) | **(Flagship)** Automatically approves 100% of tool calls, shell commands, and file edits. | `SKILL.md`, `hooks.json`, `enable-zero-touch.sh` |
| 2 | [`smart-vibecoding`](skills/smart-vibecoding/SKILL.md) | Vibecoding mastery: Transforms PRD into production code with clear reasoning paths. | `SKILL.md`, `doctor.sh` |
| 3 | [`test-driven-vibecoding`](skills/test-driven-vibecoding/SKILL.md) | Loop-Until-Green standard: Writes unit tests and loops until all tests pass before finishing. | `SKILL.md`, `auto-test.sh` |
| 4 | [`token-optimizer-pro`](skills/token-optimizer-pro/SKILL.md) | Extreme token frugality: Slice-based viewing and surgical edits prevent context blowups. | `SKILL.md` |
| 5 | [`deep-debugging`](skills/deep-debugging/SKILL.md) | Root cause analysis: Fixes runtime bugs, memory leaks, and silent crashes. | `SKILL.md` |
| 6 | [`multi-agent-orchestrator-pro`](skills/multi-agent-orchestrator-pro/SKILL.md) | Swarm agent role division: Spec Architect, Researcher, Implementer, Auditor, QA. | `SKILL.md`, `agent-prompts.md` |
| 7 | [`git-craft`](skills/git-craft/SKILL.md) | Clean version control: Atomic commits, conventional commit syntax, safe checkpoints. | `SKILL.md` |
| 8 | [`modern-ui-craft`](skills/modern-ui-craft/SKILL.md) | High-aesthetic UI design: Dark mode, Tailwind CSS, micro-tactile interactions. | `SKILL.md` |
| 9 | [`anti-ai-slop-ux`](UX/UI/SKILL.md) | **(New)** Eliminates AI Slop, eliminates purple gradients, defeats Cardocalypse, and provides machine-readable `DESIGN.md` & `UX.md`. | `UX/UI/*`, `scripts/audit-ui-slop.mjs` |

---

## 🚀 1-Click Installation

### Option 1: Remote 1-Line Install (Recommended)
```bash
curl -fsSL https://raw.githubusercontent.com/TontonYuta/skill-vibecode-agy/main/install.sh | bash
```

### Option 2: Local Install from Cloned Repo
```bash
git clone https://github.com/TontonYuta/skill-vibecode-agy.git
cd skill-vibecode-agy

# Install globally to machine (~/.gemini/config/):
./scripts/install-skills.sh

# Or install as symlinks (auto-receives updates on git pull):
./scripts/install-skills.sh --symlink

# Or install locally for the current project (.agents/):
./scripts/install-skills.sh --local
```

---

## 🔄 Cross-Harness Adapter (Cursor, Claude Code, OpenCode)

Export all rules and skills to your favorite coding assistant with one command:

```bash
# Export to all harnesses (Cursor, Claude Code, and .agents):
./scripts/export-harness.sh --all

# Or export specifically for Cursor (.cursor/rules/ & .cursorrules):
./scripts/export-harness.sh --cursor

# Or export specifically for Claude Code (CLAUDE.md):
./scripts/export-harness.sh --claude
```

---

## 📚 Battle-Tested Playbooks

Explore technical deep dives and real-world case studies in [`playbooks/`](playbooks/):

1. 📘 [`01-zero-touch-autonomous-workflow.md`](playbooks/01-zero-touch-autonomous-workflow.md): The Zero-Touch mindset and PreToolUse Hook architecture.
2. 📗 [`02-loop-until-green-tdd.md`](playbooks/02-loop-until-green-tdd.md): Ultra-fast Node.js test harness (`node:test` + `tsx`) under 50ms.
3. 📙 [`03-token-frugality-and-context-pruning.md`](playbooks/03-token-frugality-and-context-pruning.md): Slice-based file reading to survive multi-day coding sessions.
4. 📕 [`04-multi-agent-swarm-orchestration.md`](playbooks/04-multi-agent-swarm-orchestration.md): Multi-agent prompt templates and lean handoffs via URI pointers.
5. 🔬 [`05-case-study-english-no-api.md`](playbooks/05-case-study-english-no-api.md): **Zero-API English Learning App Case Study** (Edge TTS + Web Speech + Leitner 5-box algorithm).
6. 🎨 [`06-anti-ai-slop-ui-engineering.md`](playbooks/06-anti-ai-slop-ui-engineering.md): **Eradicating AI Slop**: Enforcing `DESIGN.md`, `UX.md`, and automated Playwright audits.
7. 🧠 [`07-socratic-prompting-and-grill-me.md`](playbooks/07-socratic-prompting-and-grill-me.md): **Socratic Interviewing (/grill-me)**: Forcing the AI to question requirements and edge cases before coding.

---

## 🧪 Validation

Run the test suite to verify all shell scripts and skill definitions:
```bash
./scripts/validate-skills.sh
```

---

## 📄 License

MIT © [TontonYuta](https://github.com/TontonYuta)
