#!/usr/bin/env python3
"""Review source quality for external reference research."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path


REQUIRED_MARKERS = ["출처", "확인 날짜", "관찰한", "추론", "한계"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--reference", default="REFERENCE_RESEARCH.md")
    parser.add_argument("--review-dir", default=os.environ.get("ITP_REVIEW_DIR", "reviews"))
    args = parser.parse_args()

    path = Path(args.reference)
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    missing = [marker for marker in REQUIRED_MARKERS if marker not in text]
    warnings = []
    if not text:
        warnings.append("No reference research document found.")
    if missing:
        warnings.append("Reference research should separate source, check date, observed facts, inference, and limitations.")
    if "미확인" not in text and "추론" in text and text:
        warnings.append("Inference exists; mark unverified assumptions when appropriate.")

    review_dir = Path(args.review_dir)
    review_dir.mkdir(parents=True, exist_ok=True)
    report_path = review_dir / "source-quality-review.md"
    report_path.write_text(
        "\n".join(
            [
                "# Source Quality Review",
                "",
                f"- Reference file: {args.reference}",
                "",
                "## Missing Markers",
                *(f"- {item}" for item in missing),
                "",
                "## Warnings",
                *(f"- {warning}" for warning in warnings),
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(json.dumps({"missing": missing, "warnings": warnings, "report_path": str(report_path)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
