# Plugin Package Manifest

This package contains the runtime-facing Idea to Product plugin.

Supported first-class runtime scope:

- Claude Code
- Codex
- Claude Cowork + Claude Design

Supported operating systems:

- Windows
- macOS

## Entrypoint

Start with:

- `commands/start.md`
- `workflows/idea-to-product.md`

## Required Gate Order

1. `user-prompt-scope-router.py`
2. `feature-drift-gate.py` when a new feature is suspected
3. `wireframe-change-review.py` after wireframe edits
4. `policy-consistency-review.py` when policy, state, or permission changes
5. `measurement-coverage-review.py` when actions, buttons, states, or key flows change
6. `reference-gap-review.py` when reference research is needed or mentioned
7. `source-quality-review.py` after external references are used
8. `copy-risk-review.py` when competitor patterns are applied
9. `completeness-gate.py` before document generation
10. `cross-document-consistency-review.py` after document generation
11. `human-writing-final-pass.py` before final save
12. `output-validator.py` before handoff

## Design Handoff

Use `commands/handoff-to-design.md` and `workflows/design-handoff.md` to produce:

- `DESIGN_HANDOFF_BRIEF.md`
- `CLAUDE_DESIGN_PROMPT.md`

Use `commands/import-design-feedback.md` and `workflows/design-feedback-loop.md` when Claude Design output introduces product-flow changes.

## Structural Wireframe

The wireframe is a reference surface for product discussion. It shows actions, states, policy points, and AC anchors through `data-req-id`.

It is not final UI design and does not prescribe visual style.
