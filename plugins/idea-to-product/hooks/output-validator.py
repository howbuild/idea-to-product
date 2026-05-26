#!/usr/bin/env python3
"""Validate final outputs or required repo manifest files."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


FINAL_OUTPUTS = [
    "PRD.md",
    "AC.md",
    "POLICY.md",
    "MEASUREMENT.md",
    "DECISION_LOG.md",
    "COMPLETENESS.md",
    "REVIEW_REPORT.md",
    "wireframe.html",
]

REPO_REQUIRED = [
    "README.md",
    "README.ko.md",
    "AGENTS.md",
    "PLUGIN.md",
    "FILE_MANIFEST.md",
    "plugin.yaml",
    ".claude-plugin/marketplace.json",
    ".agents/plugins/marketplace.json",
    "plugins/idea-to-product/.claude-plugin/plugin.json",
    "plugins/idea-to-product/.codex-plugin/plugin.json",
    "plugins/idea-to-product/README.ko.md",
    "plugins/idea-to-product/workflows/idea-to-product.md",
    "plugins/idea-to-product/workflows/feature-addition-review.md",
    "plugins/idea-to-product/workflows/question-interview.md",
    "plugins/idea-to-product/workflows/reference-discovery.md",
    "plugins/idea-to-product/workflows/competitive-pattern-review.md",
    "plugins/idea-to-product/workflows/design-handoff.md",
    "plugins/idea-to-product/workflows/design-feedback-loop.md",
    "plugins/idea-to-product/commands/start.md",
    "plugins/idea-to-product/commands/add-feature.md",
    "plugins/idea-to-product/commands/review-scope.md",
    "plugins/idea-to-product/commands/research-references.md",
    "plugins/idea-to-product/commands/compare-products.md",
    "plugins/idea-to-product/commands/handoff-to-design.md",
    "plugins/idea-to-product/commands/import-design-feedback.md",
    "plugins/idea-to-product/hooks/hooks.json",
    "plugins/idea-to-product/hooks/hooks.claude.json",
    "plugins/idea-to-product/hooks/hooks.codex.json",
    "plugins/idea-to-product/hooks/hooks.claude.windows.json",
    "plugins/idea-to-product/hooks/hooks.codex.windows.json",
    "plugins/idea-to-product/hooks/hook_context.py",
    "plugins/idea-to-product/hooks/feature-drift-gate.py",
    "plugins/idea-to-product/hooks/wireframe-change-review.py",
    "plugins/idea-to-product/hooks/policy-consistency-review.py",
    "plugins/idea-to-product/hooks/measurement-coverage-review.py",
    "plugins/idea-to-product/hooks/completeness-gate.py",
    "plugins/idea-to-product/hooks/cross-document-consistency-review.py",
    "plugins/idea-to-product/hooks/human-writing-final-pass.py",
    "plugins/idea-to-product/hooks/reference-gap-review.py",
    "plugins/idea-to-product/hooks/source-quality-review.py",
    "plugins/idea-to-product/hooks/copy-risk-review.py",
    "plugins/idea-to-product/agents/scope-guard.md",
    "plugins/idea-to-product/agents/pm-reviewer.md",
    "plugins/idea-to-product/agents/policy-reviewer.md",
    "plugins/idea-to-product/agents/measurement-reviewer.md",
    "plugins/idea-to-product/agents/product-flow-reviewer.md",
    "plugins/idea-to-product/agents/design-handoff-writer.md",
    "plugins/idea-to-product/agents/reference-researcher.md",
    "plugins/idea-to-product/agents/competitive-pattern-reviewer.md",
    "plugins/idea-to-product/skills/question-designer/SKILL.md",
    "plugins/idea-to-product/skills/wireframe-builder/SKILL.md",
    "plugins/idea-to-product/skills/policy-extractor/SKILL.md",
    "plugins/idea-to-product/skills/measurement-designer/SKILL.md",
    "plugins/idea-to-product/skills/human-writing-auditor/SKILL.md",
    "plugins/idea-to-product/skills/design-brief-writer/SKILL.md",
    "plugins/idea-to-product/skills/reference-synthesizer/SKILL.md",
    "plugins/idea-to-product/skills/competitive-pattern-extractor/SKILL.md",
    "plugins/idea-to-product/templates/prd.md",
    "plugins/idea-to-product/templates/pm-note.md",
    "plugins/idea-to-product/templates/acceptance-criteria.md",
    "plugins/idea-to-product/templates/policy.md",
    "plugins/idea-to-product/templates/measurement.md",
    "plugins/idea-to-product/templates/decision-log.md",
    "plugins/idea-to-product/templates/completeness-report.md",
    "plugins/idea-to-product/templates/review-report.md",
    "plugins/idea-to-product/templates/reference-research.md",
    "plugins/idea-to-product/templates/design-handoff-brief.md",
    "plugins/idea-to-product/templates/claude-design-prompt.md",
    "plugins/idea-to-product/templates/design-feedback-log.md",
    "plugins/idea-to-product/domains/README.md",
    "plugins/idea-to-product/domains/_template/domain.yaml",
    "plugins/idea-to-product/domains/_template/reference-sources.md",
    "plugins/idea-to-product/domains/_template/design-handoff-notes.md",
    "plugins/idea-to-product/docs/install-claude-code.md",
    "plugins/idea-to-product/docs/install-codex.md",
    "plugins/idea-to-product/docs/install-cowork-design.md",
    "plugins/idea-to-product/docs/install-windows.md",
    "plugins/idea-to-product/docs/install-macos.md",
    "plugins/idea-to-product/docs/runtime-capability-matrix.md",
    "plugins/idea-to-product/docs/domain-pack-usage.md",
    "plugins/idea-to-product/docs/hook-review-system.md",
    "plugins/idea-to-product/docs/codex-agent-installation.md",
    "plugins/idea-to-product/scripts/install-agents.sh",
    "scripts/validate-manifests.py",
    "scripts/validate-python-hooks.py",
    "scripts/package-claude-plugin.py",
    "scripts/package-codex-plugin.py",
    "scripts/run-hook.py",
    "scripts/validate.ps1",
    "scripts/validate.sh",
    "plugins/idea-to-product/examples/generic-request-board/PRD.md",
    "plugins/idea-to-product/examples/generic-request-board/AC.md",
    "plugins/idea-to-product/examples/generic-request-board/POLICY.md",
    "plugins/idea-to-product/examples/generic-request-board/MEASUREMENT.md",
    "plugins/idea-to-product/examples/generic-request-board/DECISION_LOG.md",
    "plugins/idea-to-product/examples/generic-request-board/REFERENCE_RESEARCH.md",
    "plugins/idea-to-product/examples/generic-request-board/COMPLETENESS.md",
    "plugins/idea-to-product/examples/generic-request-board/REVIEW_REPORT.md",
    "plugins/idea-to-product/examples/generic-request-board/DESIGN_HANDOFF_BRIEF.md",
    "plugins/idea-to-product/examples/generic-request-board/CLAUDE_DESIGN_PROMPT.md",
    "plugins/idea-to-product/examples/generic-request-board/wireframe.html",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-dir", default=".")
    parser.add_argument("--manifest", action="store_true")
    args = parser.parse_args()

    base = Path(args.base_dir)
    required = REPO_REQUIRED if args.manifest else FINAL_OUTPUTS
    missing = [path for path in required if not (base / path).exists()]
    result = {"mode": "manifest" if args.manifest else "outputs", "missing": missing, "ok": not missing}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not missing else 1


if __name__ == "__main__":
    raise SystemExit(main())
