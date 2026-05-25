#!/usr/bin/env sh
set -eu

PLUGIN_NAME="idea-to-product"
MARKETPLACE_NAME="idea-to-product-marketplace"
DEFAULT_REMOTE_SOURCE="https://github.com/howbuild/idea-to-product"
TARGET="all"
SOURCE="${MARKETPLACE_SOURCE:-}"

usage() {
  cat <<'EOF'
Install Idea to Product for Codex and/or Claude Code.

Usage:
  sh install.sh [--all|--codex|--claude] [--source <marketplace-source>]

Examples:
  sh install.sh
  sh install.sh --codex
  sh install.sh --claude --source https://github.com/howbuild/idea-to-product

Environment:
  MARKETPLACE_SOURCE  Override marketplace source path or Git URL.
  CODEX_BIN           Override Codex CLI path.
  CLAUDE_BIN          Override Claude Code CLI path.
EOF
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --all)
      TARGET="all"
      shift
      ;;
    --codex)
      TARGET="codex"
      shift
      ;;
    --claude)
      TARGET="claude"
      shift
      ;;
    --source)
      if [ "$#" -lt 2 ]; then
        echo "Missing value for --source" >&2
        exit 1
      fi
      SOURCE="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      usage >&2
      exit 1
      ;;
  esac
done

if [ -z "$SOURCE" ]; then
  if [ -f ".agents/plugins/marketplace.json" ] && [ -d "plugins/$PLUGIN_NAME" ]; then
    SOURCE="$(pwd)"
  else
    SOURCE="$DEFAULT_REMOTE_SOURCE"
  fi
fi

resolve_codex() {
  if [ -n "${CODEX_BIN:-}" ]; then
    printf '%s\n' "$CODEX_BIN"
    return 0
  fi
  if [ -x "/Applications/Codex.app/Contents/Resources/codex" ]; then
    printf '%s\n' "/Applications/Codex.app/Contents/Resources/codex"
    return 0
  fi
  if command -v codex >/dev/null 2>&1; then
    command -v codex
    return 0
  fi
  return 1
}

resolve_claude() {
  if [ -n "${CLAUDE_BIN:-}" ]; then
    printf '%s\n' "$CLAUDE_BIN"
    return 0
  fi
  command -v claude
}

install_codex() {
  codex_bin="$(resolve_codex || true)"
  if [ -z "$codex_bin" ]; then
    echo "Skipping Codex: codex CLI was not found." >&2
    return 0
  fi

  echo "Installing $PLUGIN_NAME for Codex from: $SOURCE"
  if "$codex_bin" plugin marketplace list | awk '{print $1}' | grep -qx "$MARKETPLACE_NAME"; then
    "$codex_bin" plugin marketplace remove "$MARKETPLACE_NAME"
  fi
  "$codex_bin" plugin marketplace add "$SOURCE"
  "$codex_bin" plugin add "$PLUGIN_NAME@$MARKETPLACE_NAME"
}

install_claude() {
  claude_bin="$(resolve_claude || true)"
  if [ -z "$claude_bin" ]; then
    echo "Skipping Claude Code: claude CLI was not found." >&2
    return 0
  fi

  echo "Installing $PLUGIN_NAME for Claude Code from: $SOURCE"
  if "$claude_bin" plugin marketplace list | grep -F "$MARKETPLACE_NAME" >/dev/null 2>&1; then
    "$claude_bin" plugin marketplace remove "$MARKETPLACE_NAME"
  fi
  "$claude_bin" plugin marketplace add "$SOURCE"

  if "$claude_bin" plugin list | grep -F "$PLUGIN_NAME@$MARKETPLACE_NAME" >/dev/null 2>&1; then
    "$claude_bin" plugin update "$PLUGIN_NAME@$MARKETPLACE_NAME"
  else
    "$claude_bin" plugin install "$PLUGIN_NAME@$MARKETPLACE_NAME"
  fi
}

case "$TARGET" in
  all)
    install_codex
    install_claude
    ;;
  codex)
    install_codex
    ;;
  claude)
    install_claude
    ;;
esac

echo "Done."
