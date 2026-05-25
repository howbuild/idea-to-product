#!/usr/bin/env bash
set -euo pipefail

PLUGIN_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET_DIR="${1:-${CODEX_AGENTS_DIR:-$HOME/.codex/agents/idea-to-product}}"

mkdir -p "$TARGET_DIR"
cp "$PLUGIN_ROOT"/agents/*.md "$TARGET_DIR"/

echo "Installed Idea to Product reviewer agents to: $TARGET_DIR"
