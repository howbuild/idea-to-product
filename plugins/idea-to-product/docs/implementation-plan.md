# Implementation Plan

## Phase 1. 기준 문서 작성

- Capture product philosophy and constraints.
- Fix architecture boundaries.
- Record domain-pack exclusions.
- Record review gate requirements.

## Phase 2. 문서 기반 플랜 세우기

- Create root marketplace metadata.
- Create plugin package metadata.
- Create workflows, commands, hooks, agents, skills, templates, domains, MCP docs, and examples.
- Add reference research support as a helper layer, not as the main product.
- Keep runtime-specific metadata directories limited to `plugin.json` and `install.md`.

## Phase 3. 완성 목표 세우기

- Define required files.
- Define self-check criteria.
- Define sample output coverage.
- Define what remains intentionally unconnected.

## Phase 4. 구현

- Generate the complete repo structure.
- Fill all required markdown, YAML, JSON, HTML, and Python hook files.
- Avoid concrete domain packs.
- Replace `ux-reviewer` with `product-flow-reviewer`.

## Phase 5. 검증

- Verify required files exist.
- Verify hook wiring.
- Verify no concrete domain pack directories exist.
- Verify docs describe skills as support modules.
- Verify README includes Claude Code and Codex installation guidance.
- Verify examples include all required output files.
- Verify reference research files, source-quality review, and copy-risk review exist.
- Verify Claude Code, Codex, Claude Cowork + Design, Windows, and macOS remain documented as supported.
- Verify Design handoff command, workflow, skill, agent, and templates exist.

## Phase 6. 보고

- Report structure, workflows, commands, gates, agents, skills, injection modes, feature review flow, measurement design, writing audit, sample output, runtime usage, construction wrapper split, unconnected parts, and next steps.
