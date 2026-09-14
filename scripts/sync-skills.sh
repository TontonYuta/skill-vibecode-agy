#!/usr/bin/env bash
# ==============================================================================
# 🔄 Skill Synchronizer: Local System <-> Repository
# ==============================================================================
# Usage:
#   ./scripts/sync-skills.sh          # Syncs ~/.gemini/config/skills -> Repo skills/
#   ./scripts/sync-skills.sh --push   # Syncs, commits, and pushes to GitHub
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
SKILLS_SRC="$HOME/.gemini/config/skills"
RULES_SRC="$HOME/.gemini/config/rules/AGENTS.md"

TARGET_SKILLS="$REPO_DIR/skills"
TARGET_RULES="$REPO_DIR/rules/AGENTS.md"

DO_PUSH=false
if [ "$1" = "--push" ]; then
    DO_PUSH=true
fi

echo "=========================================================="
echo "🔄 Synchronizing local skills into repository"
echo "Source: $SKILLS_SRC"
echo "Target: $TARGET_SKILLS"
echo "=========================================================="

if [ ! -d "$SKILLS_SRC" ]; then
    echo "❌ Local skills directory $SKILLS_SRC does not exist!"
    exit 1
fi

mkdir -p "$TARGET_SKILLS"
cp -r "$SKILLS_SRC"/* "$TARGET_SKILLS/"
echo "✓ Skills updated."

if [ -f "$RULES_SRC" ]; then
    mkdir -p "$(dirname "$TARGET_RULES")"
    cp "$RULES_SRC" "$TARGET_RULES"
    echo "✓ AGENTS.md rule updated."
fi

if [ "$DO_PUSH" = true ]; then
    cd "$REPO_DIR"
    git add .
    if git diff-index --quiet HEAD --; then
        echo "ℹ No changes to commit."
    else
        TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
        git commit -m "chore: sync latest skills and rules ($TIMESTAMP)"
        git push origin main
        echo "🚀 Pushed latest changes to GitHub."
    fi
fi

echo "=========================================================="
echo "🎉 Sync completed!"
echo "=========================================================="
