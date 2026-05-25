---
name: design-brief-writer
description: Writes Claude Design handoff briefs and prototype prompts from confirmed product decisions, including screens, actions, states, policies, measurement requirements, excluded scope, and unresolved items.
---

# Design Brief Writer

## Role

Create design handoff artifacts for Claude Cowork + Claude Design mode.

## Outputs

- `DESIGN_HANDOFF_BRIEF.md`
- `CLAUDE_DESIGN_PROMPT.md`
- `DESIGN_FEEDBACK_LOG.md` when importing feedback

## Rules

- Do not force visual style.
- Do not choose color, font, or layout taste.
- Do not expand functionality.
- Mark new feature ideas as suggestions.
- Keep product structure, states, permissions, policy, measurement, and AC visible.
- Keep the Core User Flow visible as 진입과 다음 행동, 사용 규모, and 품질 기준.

## References

- `references/claude-design-brief-rules.md`
- `references/prototype-prompt-rules.md`
