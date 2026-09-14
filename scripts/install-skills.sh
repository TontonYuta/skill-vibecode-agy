#!/usr/bin/env bash
# ==============================================================================
# 🚀 1-Click Skill Installer for Antigravity & AI Coding Agents
# ==============================================================================
# Usage:
#   ./scripts/install-skills.sh           # Installs to ~/.gemini/config/skills & rules
#   ./scripts/install-skills.sh --local   # Installs to ./.agents/skills in current repo
#   ./scripts/install-skills.sh --symlink # Symlinks instead of copying
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
SKILLS_SRC="$REPO_DIR/skills"
RULES_SRC="$REPO_DIR/rules/AGENTS.md"

TARGET_DIR="$HOME/.gemini/config/skills"
RULES_TARGET_DIR="$HOME/.gemini/config/rules"
USE_SYMLINK=false

# Parse arguments
for arg in "$@"; do
    case $arg in
        --local)
            TARGET_DIR="$(pwd)/.agents/skills"
            RULES_TARGET_DIR="$(pwd)"
            ;;
        --symlink)
            USE_SYMLINK=true
            ;;
        --help|-h)
            echo "Usage: $0 [--local] [--symlink]"
            exit 0
            ;;
    esac
done

echo "=========================================================="
echo "📦 Installing Vibecoding Skills & Rules"
echo "Source: $SKILLS_SRC"
echo "Target Skills: $TARGET_DIR"
echo "Target Rules:  $RULES_TARGET_DIR"
echo "=========================================================="

mkdir -p "$TARGET_DIR"
mkdir -p "$RULES_TARGET_DIR"

COUNT=0
for skill in "$SKILLS_SRC"/*; do
    if [ -d "$skill" ]; then
        skill_name="$(basename "$skill")"
        dest="$TARGET_DIR/$skill_name"
        
        if [ "$USE_SYMLINK" = true ]; then
            rm -rf "$dest"
            ln -s "$skill" "$dest"
            echo "🔗 Symlinked: $skill_name"
        else
            rm -rf "$dest"
            cp -r "$skill" "$dest"
            echo "✓ Copied: $skill_name"
        fi
        COUNT=$((COUNT + 1))
    fi
done

# Copy or symlink AGENTS.md
if [ -f "$RULES_SRC" ]; then
    dest_rule="$RULES_TARGET_DIR/AGENTS.md"
    if [ "$USE_SYMLINK" = true ]; then
        rm -f "$dest_rule"
        ln -s "$RULES_SRC" "$dest_rule"
        echo "🔗 Symlinked: AGENTS.md -> $dest_rule"
    else
        cp "$RULES_SRC" "$dest_rule"
        echo "✓ Copied: AGENTS.md -> $dest_rule"
    fi
fi

echo "=========================================================="
echo "🎉 Successfully installed $COUNT skills and AGENTS.md rule!"
echo "Enjoy autonomous vibecoding with Google Antigravity & AI Agents!"
echo "=========================================================="
