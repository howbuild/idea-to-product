# Verification Report

Status: completed

Date: 2026-05-25

Update: marketplace manifests were adjusted for Claude Code and Codex plugin runtimes, hooks were converted to a Claude-compatible lifecycle map, and agent/skill frontmatter was added.

Update: support scope was restored and documented for Claude Code, Codex, Claude Cowork + Claude Design, Windows, and macOS. Claude/Codex hook configs were split into `hooks.claude.json` and `hooks.codex.json`. Design handoff workflow, command, agent, skill, templates, docs, and generic request-board examples were added.

## File Manifest Check

Command:

```bash
python3 plugins/idea-to-product/hooks/output-validator.py --manifest
```

Result:

```json
{
  "mode": "manifest",
  "missing": [],
  "ok": true
}
```

## Generic Output Check

Command:

```bash
python3 plugins/idea-to-product/hooks/output-validator.py --base-dir plugins/idea-to-product/examples/generic-output
```

Result:

```json
{
  "mode": "outputs",
  "missing": [],
  "ok": true
}
```

## Hook Syntax Check

Command:

```bash
python3 -m compileall plugins/idea-to-product/hooks
```

Result: all hook scripts compiled.

## Hook Definition Check

Command:

```bash
python3 -m json.tool plugins/idea-to-product/hooks/hooks.claude.json
python3 -m json.tool plugins/idea-to-product/hooks/hooks.codex.json
```

Result: valid JSON.

## Manifest Validation

Command:

```bash
python3 scripts/validate-manifests.py
```

Result: manifest validation passed.

## Python Hook Validation

Command:

```bash
python3 scripts/validate-python-hooks.py
```

Result: Python hook validation passed.

## Domain Pack Check

Command:

```bash
python3 plugins/idea-to-product/hooks/domain-pack-validator.py plugins/idea-to-product/domains/_template --review-dir /tmp/itp-check-reviews
```

Result: `_template` contains all required domain-pack template files, including `reference-sources.md`.

## Scope Router Check

Command:

```bash
python3 plugins/idea-to-product/hooks/user-prompt-scope-router.py '실시간 채팅도 넣고 싶어'
```

Result: detected `feature_or_scope_change` and suggested `feature-drift-gate.py`.

## Feature Drift Check

Command:

```bash
printf '%s' '{"candidate_feature":"실시간 채팅도 넣고 싶어"}' | python3 plugins/idea-to-product/hooks/feature-drift-gate.py --review-dir /tmp/itp-check-reviews
```

Result: `Red`, with MVP inclusion pending explicit user confirmation.

## Wireframe Check

Command:

```bash
python3 plugins/idea-to-product/hooks/wireframe-change-review.py --wireframe plugins/idea-to-product/examples/generic-output/wireframe.html --review-dir /tmp/itp-check-reviews
```

Result: 26 `data-req-id` values, no issues, and `measurement-coverage-review.py` suggested.

## Structural Rules

- plugin runtime metadata directories keep install metadata separate from workflows, commands, hooks, agents, skills, templates, and docs.
- `.claude-plugin/marketplace.json` exists at the repo root.
- `.agents/plugins/marketplace.json` uses a `plugins[]` marketplace structure.
- `.claude-plugin/` and `.codex-plugin/` contain runtime manifests and install docs.
- `agents/ux-reviewer.md` does not exist.
- `agents/product-flow-reviewer.md` is used instead.
- `domains/` contains only `_template`; no concrete domain pack exists.
- Reference research is documented as a support layer, not the product.
- Copy-risk and source-quality hooks exist.
- README includes Claude Code installation, Codex installation, Codex hooks trust review, domain-pack usage, human-writing-auditor, construction wrapper split, and Reference and Competitive Research.
- README states support for Claude Code, Codex, Claude Cowork + Claude Design, Windows, and macOS.
- Runtime capability matrix exists.
- Windows and macOS install docs exist.
- Claude Design handoff brief and prompt templates exist.

## Intentionally Not Connected

- No real marketplace publication has been performed.
- No real Claude Code, Codex, Cursor, or OpenCode runtime has installed the plugin in this run.
- No MCP server credentials or secrets were created.
- No concrete construction domain pack was added to the core repo.
