#!/usr/bin/env bash
# ==============================================================================
# 🚀 1-Line Remote & Local Installer for Skill Vibecode AGY
# ==============================================================================
# Usage:
#   # Remote 1-Line Install (curl | bash):
#   curl -fsSL https://raw.githubusercontent.com/TontonYuta/skill-vibecode-agy/main/install.sh | bash
#
#   # Local Install:
#   ./install.sh                # Install globally (~/.gemini/config/)
#   ./install.sh --local        # Install to current project (.agents/)
#   ./install.sh --symlink      # Symlink for real-time updates
# ==============================================================================

set -e

REPO_URL="https://github.com/TontonYuta/skill-vibecode-agy.git"
INSTALL_DIR="$HOME/.skill-vibecode-agy"

# Terminal colors
BOLD='\033[1m'
CYAN='\033[0;36m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${CYAN}${BOLD}"
echo "=========================================================="
echo "⚡ Skill Vibecode AGY (Google Antigravity & AI Agents)"
echo "   Zero-Touch Auto-Accept | Loop-Until-Green | Anti-AI-Slop"
echo "=========================================================="
echo -e "${NC}"

# Detect if running inside an existing git checkout of skill-vibecode-agy
if [ -f "./scripts/install-skills.sh" ] && [ -d "./skills" ]; then
    echo -e "${GREEN}✓ Detected local repository.${NC}"
    ./scripts/install-skills.sh "$@"
    exit 0
fi

# Otherwise, running via remote curl | bash
echo -e "${YELLOW}➜ Installing via remote clone to ${INSTALL_DIR}...${NC}"

if [ -d "$INSTALL_DIR/.git" ]; then
    echo -e "Updating existing clone at ${INSTALL_DIR}..."
    git -C "$INSTALL_DIR" pull --ff-only origin main || true
else
    mkdir -p "$(dirname "$INSTALL_DIR")"
    git clone "$REPO_URL" "$INSTALL_DIR"
fi

cd "$INSTALL_DIR"
chmod +x ./scripts/*.sh ./install.sh
./scripts/install-skills.sh "$@"

echo -e "\n${GREEN}${BOLD}🎉 Installation Complete!${NC}"
echo -e "You can now prompt your agent and enjoy a 100% Zero-Touch workflow."
