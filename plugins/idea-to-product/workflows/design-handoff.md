# Design Handoff Workflow

## Purpose

Prepare a Claude Design handoff without replacing Claude Code or Codex support.

Claude Cowork + Design is a first-class support path. It is not a replacement for plugin automation in Claude Code and Codex.

## Steps

1. Confirm Core Intent Card.
2. Confirm MVP scope and excluded scope.
3. Confirm screen list and screen purpose.
4. Confirm states, permissions, empty/error/permission-denied states, and policies.
5. Confirm measurement/logging requirements.
6. Generate `DESIGN_HANDOFF_BRIEF.md`.
7. Generate `CLAUDE_DESIGN_PROMPT.md`.
8. Mark features Claude Design must not add.
9. Mark unresolved product decisions.

## Claude Design Prompt Rules

- Do not force visual style.
- Do not force colors, fonts, or layout taste.
- Do not expand feature scope.
- Keep new feature ideas separate as suggestions.
- Visualize product structure, user actions, states, and constraints.

## Output

- `DESIGN_HANDOFF_BRIEF.md`
- `CLAUDE_DESIGN_PROMPT.md`
