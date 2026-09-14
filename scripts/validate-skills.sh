#!/usr/bin/env bash
# ==============================================================================
# 🧪 Validation Runner for Skills and Shell Scripts
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "=== [VALIDATING SHELL SCRIPTS] ==="
bash -n "$REPO_DIR/scripts/install-skills.sh"
bash -n "$REPO_DIR/scripts/sync-skills.sh"
bash -n "$REPO_DIR/scripts/validate-skills.sh"
bash -n "$REPO_DIR/skills/smart-vibecoding/scripts/doctor.sh"
bash -n "$REPO_DIR/skills/test-driven-vibecoding/scripts/auto-test.sh"
echo "✓ All shell scripts passed syntax checks."

echo "=== [VALIDATING SKILL DEFINITIONS] ==="
for skill_dir in "$REPO_DIR/skills"/*; do
  if [ -d "$skill_dir" ]; then
    skill_name="$(basename "$skill_dir")"
    if [ ! -f "$skill_dir/SKILL.md" ]; then
      echo "❌ Missing SKILL.md in $skill_name"
      exit 1
    fi
    echo "✓ Valid: $skill_name/SKILL.md"
  fi
done

echo "=== [VALIDATION PASSED: 100% GREEN] ==="
