# Hook Review System

Hooks are quality gates for the Idea to Product workflow.

They are responsible for:

- detecting scope changes
- routing prompts to review gates
- warning before risky changes become requirements
- generating review reports
- connecting changes to reviewer agents

They are not responsible for replacing the full PM workflow.

## Runtime Strategy

If a runtime supports agent-based hooks, pair each script with the listed reviewer agents.

If a runtime does not support agent-based hooks, the scripts still generate structured JSON and markdown review reports.

Runtime hook files:

- `hooks.claude.json`: Claude Code lifecycle hook config
- `hooks.codex.json`: Codex-compatible lifecycle hook config
- `hooks.claude.windows.json`: Claude Code hook config using Windows Python launcher
- `hooks.codex.windows.json`: Codex hook config using Windows Python launcher
- `hooks.json`: compatibility copy for tools that expect the generic name

These files use a Claude-compatible lifecycle map:

```json
{
  "hooks": {
    "SessionStart": [],
    "UserPromptSubmit": [],
    "PreToolUse": [],
    "PostToolUse": [],
    "Stop": []
  }
}
```

Each hook entry runs a command hook through `python3 "${CLAUDE_PLUGIN_ROOT}/hooks/<script>.py"`.

Windows variants use `py -3 "${CLAUDE_PLUGIN_ROOT}/hooks/<script>.py"` so Windows users are not blocked by missing `python3`.

## Review Output Directory

By default, scripts write reports to:

```text
reviews/
```

Override with:

```bash
ITP_REVIEW_DIR=/path/to/reviews
```
