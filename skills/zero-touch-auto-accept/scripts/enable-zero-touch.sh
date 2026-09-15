#!/usr/bin/env bash
# ==============================================================================
# 🚀 1-Click Enable Zero-Touch Auto-Accept Mode for Google Antigravity (AGY)
# ==============================================================================
# Sets up lifecycle hooks and agent directives so the agent auto-approves
# all tools, runs commands, tests, and completes tasks without user interruption.
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
REPO_DIR="$(cd "$SKILL_DIR/../.." && pwd)"

TARGET_MODE="global"
for arg in "$@"; do
    case $arg in
        --local)
            TARGET_MODE="local"
            ;;
        --global)
            TARGET_MODE="global"
            ;;
        -h|--help)
            echo "Usage: $0 [--global | --local]"
            exit 0
            ;;
    esac
done

if [ "$TARGET_MODE" = "global" ]; then
    CONFIG_DIR="$HOME/.gemini/config"
    RULES_DIR="$HOME/.gemini/config/rules"
else
    CONFIG_DIR="$(pwd)/.agents"
    RULES_DIR="$(pwd)"
fi

echo "=========================================================="
echo "⚡ Activating Zero-Touch Auto-Accept Mode ($TARGET_MODE)"
echo "Config Target: $CONFIG_DIR"
echo "Rules Target:  $RULES_DIR"
echo "=========================================================="

mkdir -p "$CONFIG_DIR"
mkdir -p "$RULES_DIR"

# 1. Install hooks.json for PreToolUse auto allow
HOOKS_SRC="$SKILL_DIR/hooks.json"
HOOKS_DEST="$CONFIG_DIR/hooks.json"

if [ -f "$HOOKS_DEST" ]; then
    # Merge or backup
    cp "$HOOKS_DEST" "$HOOKS_DEST.bak.$(date +%s)"
    echo "ℹ Backed up existing hooks.json"
fi

cp "$HOOKS_SRC" "$HOOKS_DEST"
echo "✓ Installed PreToolUse auto-allow hook -> $HOOKS_DEST"

# 2. Install AGENTS.md rules
RULES_SRC="$REPO_DIR/rules/AGENTS.md"
if [ -f "$RULES_SRC" ]; then
    cp "$RULES_SRC" "$RULES_DIR/AGENTS.md"
    echo "✓ Installed AGENTS.md directives -> $RULES_DIR/AGENTS.md"
fi

echo "=========================================================="
echo "🎉 Zero-Touch Auto-Accept Mode is NOW ACTIVE!"
echo "You can now enter prompts and press Enter."
echo "Antigravity will auto-allow tool executions and drive to completion."
echo "=========================================================="
