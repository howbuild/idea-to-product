---
description: Generate PRD, policy, measurement, AC, decision log, and review outputs.
---

# Command: generate-docs

Use when the user wants to create the final output documents.

## Run

1. Run `completeness-gate.py`.
2. Generate `PRD.md`.
3. Generate `POLICY.md`.
4. Generate `MEASUREMENT.md`.
5. Generate `AC.md`.
6. Generate `DECISION_LOG.md`.
7. Generate `COMPLETENESS.md`.
8. Run `cross-document-consistency-review.py`.
9. Run `human-writing-final-pass.py`.
10. Save final files.

If the user asks for Claude Design handoff, also generate:

- `DESIGN_HANDOFF_BRIEF.md`
- `CLAUDE_DESIGN_PROMPT.md`

## Required Warning

If total completeness is below 70, warn the user and show missing question candidates. Draft generation is allowed only if the user accepts the draft state.
