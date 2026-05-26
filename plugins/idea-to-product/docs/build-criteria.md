# Build Criteria

This document is the implementation 기준 문서 for the core `idea-to-product` plugin.

## Required Product Identity

Idea to Product is a multi-runtime AI PM plugin that helps a non-developer turn an idea into developer-ready requirements while learning product thinking through screen-based questions and choices.

Supported runtime scope:

- Claude Code
- Codex
- Claude Cowork + Claude Design

Supported OS scope:

- Windows
- macOS

It is not:

- a production app
- a simple skill collection
- a generic PRD generator
- a final UI design generator
- a concrete domain-pack repo
- a market research report generator

## Required Architecture

The plugin must center on:

1. workflows
2. commands
3. hooks
4. agents

Skills are supporting modules called by those layers.

## Required Outputs

- PRD
- AC
- POLICY
- MEASUREMENT
- DECISION_LOG
- COMPLETENESS
- REVIEW_REPORT
- `wireframe.html`

## Required Review Gates

- feature addition: `feature-drift-gate.py`
- wireframe change: `wireframe-change-review.py`
- policy/state/permission change: `policy-consistency-review.py`
- action/state/logging coverage: `measurement-coverage-review.py`
- before document generation: `completeness-gate.py`
- after document generation: `cross-document-consistency-review.py`
- before final save: `human-writing-final-pass.py`
- reference gap: `reference-gap-review.py`
- source quality: `source-quality-review.py`
- copy risk: `copy-risk-review.py`

Do not remove hooks or Python review gates. If a runtime has limitations, document the limitation.

## Domain Rule

The core repo includes only domain injection structure and `_template`.

It must not include concrete domain packs.

## Product-Flow Reviewer Rule

Use `product-flow-reviewer`, not `ux-reviewer`.

The reviewer checks user actions, states, policy links, AC links, and Core Intent alignment. It does not review visual style.

It must also check the Core User Flow:

- 진입과 다음 행동: where the user comes from and where the user goes next
- 사용 규모: how much usage or repeated action should pass through
- 품질 기준: what rules keep the product useful and trustworthy when usage grows

## Question Readability Rule

User-facing questions must be easy to understand at first read, but must keep useful practical terms such as PRD, AC, KPI, 권한정책, 상태값, 이벤트, 로그, and `data-req-id`.

## Reference Research Rule

Reference research is a support layer. It turns outside examples into question candidates, policy candidates, state candidates, permission candidates, measurement/logging candidates, Must-have/Nice-to-have judgments, operating-intent and scalability judgments, and AC candidates.

It must distinguish source facts from inference and must not copy competitors.

## Design Handoff Rule

Claude Design handoff is a first-class path. It produces a design brief and prompt, but Idea to Product still reviews product flow, Core User Flow, state, policy, measurement, AC, and scope. It does not judge visual style.
