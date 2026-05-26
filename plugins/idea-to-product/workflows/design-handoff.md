# Design Handoff Workflow

## Purpose

Prepare a Claude Design handoff without replacing Claude Code or Codex support.

Claude Cowork + Design is a first-class support path. It is not a replacement for plugin automation in Claude Code and Codex.

## Steps

1. Confirm Core Intent Card.
2. Confirm requirement priority: Must-have and Nice-to-have.
3. Confirm Core User Flow: 진입과 다음 행동, 사용 규모, and 품질 기준.
4. Confirm screen list and screen purpose.
5. Confirm states, permissions, empty/error/permission-denied states, and policies.
6. Confirm measurement/logging requirements.
7. Generate `DESIGN_HANDOFF_BRIEF.md`.
8. Generate `CLAUDE_DESIGN_PROMPT.md`.
9. Mark features Claude Design must not add.
10. Mark unresolved product decisions.

## Claude Design Prompt Rules

- Do not force visual style.
- Do not force colors, fonts, or layout taste.
- Do not expand feature scope.
- Keep new feature ideas separate as suggestions.
- Visualize product structure, user actions, states, and constraints.
- Preserve the confirmed Core User Flow without turning it into new features.

## Output

- `DESIGN_HANDOFF_BRIEF.md`
- `CLAUDE_DESIGN_PROMPT.md`
