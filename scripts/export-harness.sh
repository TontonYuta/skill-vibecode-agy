#!/usr/bin/env bash
# ==============================================================================
# 🔄 Cross-Harness Skill & Rule Exporter
# ==============================================================================
# Converts and exports skill-vibecode-agy rules & skills to:
#   - Cursor (.cursor/rules/*.mdc & .cursorrules)
#   - Claude Code (CLAUDE.md & .claude/rules/)
#   - OpenCode / Roo Code / Cline (.agents/)
#
# Usage:
#   ./scripts/export-harness.sh --all
#   ./scripts/export-harness.sh --cursor [target_dir]
#   ./scripts/export-harness.sh --claude [target_dir]
#   ./scripts/export-harness.sh --agents [target_dir]
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
SKILLS_DIR="$REPO_DIR/skills"
RULES_FILE="$REPO_DIR/rules/AGENTS.md"

TARGET_DIR="${2:-$(pwd)}"
ACTION="${1:---all}"

# Terminal colors
BOLD='\033[1m'
CYAN='\033[0;36m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

export_cursor() {
    local dest="$1"
    echo -e "${CYAN}➜ Exporting for Cursor (.cursor/rules/ & .cursorrules)...${NC}"
    mkdir -p "$dest/.cursor/rules"
    
    # Generate .cursor/rules/vibecode-core.mdc
    cat << 'EOF' > "$dest/.cursor/rules/vibecode-core.mdc"
---
description: Zero-Touch Autonomous Workflow & Testing Rules for Vibe Coding
globs: *
alwaysApply: true
---
EOF
    cat "$RULES_FILE" >> "$dest/.cursor/rules/vibecode-core.mdc"

    # Also copy or append to .cursorrules
    cp "$dest/.cursor/rules/vibecode-core.mdc" "$dest/.cursorrules"
    echo -e "${GREEN}✓ Created: $dest/.cursor/rules/vibecode-core.mdc & $dest/.cursorrules${NC}"
}

export_claude() {
    local dest="$1"
    echo -e "${CYAN}➜ Exporting for Claude Code (CLAUDE.md)...${NC}"
    mkdir -p "$dest/.claude/rules"
    
    cat << 'EOF' > "$dest/CLAUDE.md"
# CLAUDE.md - Autonomous Vibe Coding & Quality Guidelines
EOF
    cat "$RULES_FILE" >> "$dest/CLAUDE.md"
    cp "$RULES_FILE" "$dest/.claude/rules/AGENTS.md"
    echo -e "${GREEN}✓ Created: $dest/CLAUDE.md & $dest/.claude/rules/AGENTS.md${NC}"
}

export_agents() {
    local dest="$1"
    echo -e "${CYAN}➜ Exporting for OpenCode / Roo Code / Antigravity (.agents/)...${NC}"
    mkdir -p "$dest/.agents/rules"
    mkdir -p "$dest/.agents/skills"

    cp "$RULES_FILE" "$dest/.agents/rules/AGENTS.md"
    for s in "$SKILLS_DIR"/*; do
        if [ -d "$s" ]; then
            local sname="$(basename "$s")"
            mkdir -p "$dest/.agents/skills/$sname"
            cp -r "$s"/* "$dest/.agents/skills/$sname/"
        fi
    done
    echo -e "${GREEN}✓ Exported all skills and rules to: $dest/.agents/${NC}"
}

echo -e "${BOLD}🔄 Cross-Harness Exporter starting... Target directory: ${TARGET_DIR}${NC}"

case "$ACTION" in
    --cursor)
        export_cursor "$TARGET_DIR"
        ;;
    --claude)
        export_claude "$TARGET_DIR"
        ;;
    --agents)
        export_agents "$TARGET_DIR"
        ;;
    --all)
        export_cursor "$TARGET_DIR"
        export_claude "$TARGET_DIR"
        export_agents "$TARGET_DIR"
        ;;
    *)
        echo -e "${YELLOW}Usage: $0 [--cursor|--claude|--agents|--all] [target_dir]${NC}"
        exit 1
        ;;
esac

echo -e "\n${GREEN}${BOLD}🎉 Export completed successfully!${NC}"
