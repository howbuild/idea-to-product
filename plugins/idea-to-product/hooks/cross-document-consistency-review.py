#!/usr/bin/env python3
"""Check consistency across PRD, AC, POLICY, MEASUREMENT, and DECISION_LOG."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path


REQUIRED = ["PRD.md", "AC.md", "POLICY.md", "MEASUREMENT.md", "DECISION_LOG.md"]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-dir", default=".")
    parser.add_argument("--review-dir", default=os.environ.get("ITP_REVIEW_DIR", "reviews"))
    args = parser.parse_args()

    base = Path(args.base_dir)
    docs = {name: read(base / name) for name in REQUIRED}
    missing_files = [name for name, text in docs.items() if not text]
    issues = []

    if "Given" not in docs["AC.md"] or "When" not in docs["AC.md"] or "Then" not in docs["AC.md"]:
        issues.append("AC does not clearly use Given / When / Then.")
    if "정책" in docs["PRD.md"] and "관련 AC" not in docs["POLICY.md"]:
        issues.append("POLICY should connect policies to AC.")
    if "이벤트" in docs["MEASUREMENT.md"] and "KPI" not in docs["PRD.md"]:
        issues.append("MEASUREMENT references events but PRD KPI is weak or missing.")
    if "보류" in docs["DECISION_LOG.md"] and "미결정" not in docs["PRD.md"]:
        issues.append("Decision log includes held items; PRD should keep unresolved items visible.")

    review_dir = Path(args.review_dir)
    review_dir.mkdir(parents=True, exist_ok=True)
    report_path = review_dir / "cross-document-consistency-review.md"
    report_path.write_text(
        "\n".join(
            [
                "# Cross-Document Consistency Review",
                "",
                "## Missing Files",
                *(f"- {name}" for name in missing_files),
                "",
                "## Issues",
                *(f"- {issue}" for issue in issues),
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(json.dumps({"missing_files": missing_files, "issues": issues, "report_path": str(report_path)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
