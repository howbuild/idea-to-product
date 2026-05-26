#!/usr/bin/env python3
"""Warn about AI-like wording before final save."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from hook_context import existing_files, print_skipped


BANNED = [
    "좋은 질문입니다",
    "핵심은",
    "정리하면",
    "단순히",
    "하는 흐름이에요",
    "하는 결이에요",
    "혁신적인",
    "강력한",
    "원활한",
    "도움이 되었길 바랍니다",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", nargs="*", default=["PRD.md", "AC.md", "POLICY.md", "MEASUREMENT.md", "DECISION_LOG.md", "COMPLETENESS.md", "REVIEW_REPORT.md"])
    parser.add_argument("--review-dir", default=os.environ.get("ITP_REVIEW_DIR", "reviews"))
    args = parser.parse_args()

    files = existing_files(args.files)
    if not files:
        print_skipped("No Idea to Product final documents found; final writing review was not written.")
        return 0

    findings = []
    for path in files:
        raw = str(path)
        text = path.read_text(encoding="utf-8")
        for phrase in BANNED:
            if phrase in text:
                findings.append({"file": raw, "phrase": phrase})

    review_dir = Path(args.review_dir)
    review_dir.mkdir(parents=True, exist_ok=True)
    report_path = review_dir / "final-writing-review.md"
    report_path.write_text(
        "\n".join(
            [
                "# Final Writing Review",
                "",
                "## Findings",
                *(f"- {item['file']}: {item['phrase']}" for item in findings),
                "",
                "## Rule",
                "Apply human-writing-auditor before final save. Preserve practical terms such as PRD, AC, KPI, 권한정책, 상태값, 이벤트, and 로그.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(json.dumps({"findings": findings, "report_path": str(report_path), "warn": bool(findings)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
