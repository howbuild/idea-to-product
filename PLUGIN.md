# Idea to Product Plugin

Idea to Product is a multi-runtime AI PM plugin for Claude Code, Codex, Claude Cowork + Claude Design, Windows, and macOS.

Supported first-class runtime scope:

- Claude Code
- Codex
- Claude Cowork + Claude Design

Supported operating systems:

- Windows
- macOS

The plugin turns rough ideas into developer-ready requirements through:

- workflow orchestration
- command entrypoints
- hook-based review gates
- specialist reviewer agents
- supporting skills
- domain-pack injection
- reference and competitive research support
- MCP suggestions
- output templates
- Claude Design handoff

## Runtime Shape

The runtime-specific metadata directories contain only install metadata:

- `.claude-plugin/plugin.json`
- `.claude-plugin/install.md`
- `.codex-plugin/plugin.json`
- `.codex-plugin/install.md`

Actual plugin components live at the plugin root:

- `workflows/`
- `commands/`
- `hooks/`
- `agents/`
- `skills/`
- `domains/`
- `templates/`
- `mcp/`
- `docs/`
- `examples/`

Runtime-specific limitations are documented instead of removing support.

## Product Philosophy

This plugin is closer to an AI PM partner than an automatic planner.

It helps a non-developer learn product thinking by asking screen-grounded questions, showing tradeoffs, and reviewing scope drift before features become requirements.

## Wireframe Philosophy

The HTML wireframe is a structural prototype. It exists to reveal product structure, user actions, states, policy points, measurement points, and AC verification points.

It is not final UI design. It does not lock visual style, component library, color palette, or production implementation.

## Review Gates

The default gates are:

- `feature-drift-gate.py`
- `wireframe-change-review.py`
- `policy-consistency-review.py`
- `measurement-coverage-review.py`
- `completeness-gate.py`
- `cross-document-consistency-review.py`
- `human-writing-final-pass.py`
- `domain-pack-validator.py`
- `output-validator.py`
- `reference-gap-review.py`
- `source-quality-review.py`
- `copy-risk-review.py`

Each gate creates a report or route signal that a runtime can show to the user.
