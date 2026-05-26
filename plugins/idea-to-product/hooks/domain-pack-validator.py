#!/usr/bin/env python3
"""Validate external domain pack structure."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from hook_context import has_domain_pack, print_skipped


REQUIRED = [
    "domain.yaml",
    "glossary.md",
    "question-bank.md",
    "policy-checklist.md",
    "measurement-checklist.md",
    "wireframe-patterns.md",
    "design-handoff-notes.md",
    "mcp-suggestions.md",
    "reference-sources.md",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("domain_path", nargs="?", default=os.environ.get("ITP_DOMAIN_PACK", "domains/_template"))
    parser.add_argument("--review-dir", default=os.environ.get("ITP_REVIEW_DIR", "reviews"))
    args = parser.parse_args()

    base = Path(args.domain_path)
    if not has_domain_pack(base):
        print_skipped("No Idea to Product domain pack found; domain-pack validation report was not written.")
        return 0

    missing = [name for name in REQUIRED if not (base / name).exists()]
    warning = "도메인팩은 질문 후보이며 확정 정책이 아닙니다. 사용자 확인 전까지 요구사항으로 확정하지 마세요."

    review_dir = Path(args.review_dir)
    review_dir.mkdir(parents=True, exist_ok=True)
    report_path = review_dir / "domain-pack-validation.md"
    report_path.write_text(
        "\n".join(
            [
                "# Domain Pack Validation",
                "",
                f"- Domain path: {base}",
                "",
                "## Missing Files",
                *(f"- {name}" for name in missing),
                "",
                "## Warning",
                warning,
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(json.dumps({"domain_path": str(base), "missing": missing, "warning": warning, "report_path": str(report_path)}, ensure_ascii=False, indent=2))
    return 0 if not missing else 1


if __name__ == "__main__":
    raise SystemExit(main())
