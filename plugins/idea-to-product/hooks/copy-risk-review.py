#!/usr/bin/env python3
"""Warn if requirements appear to copy a competitor instead of adapting patterns."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path


RISK_TERMS = ["그대로", "복사", "동일하게", "경쟁사처럼", "clone", "copy"]
SEPARATION_TERMS = ["Core Intent", "현재 제품", "반영 여부", "반영하지 않은 이유", "결정근거"]


def read_all(base: Path, names: list[str]) -> str:
    chunks = []
    for name in names:
        path = base / name
        if path.exists():
            chunks.append(path.read_text(encoding="utf-8"))
    return "\n".join(chunks)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-dir", default=".")
    parser.add_argument("--review-dir", default=os.environ.get("ITP_REVIEW_DIR", "reviews"))
    args = parser.parse_args()

    text = read_all(Path(args.base_dir), ["PRD.md", "REFERENCE_RESEARCH.md", "DECISION_LOG.md"])
    risk_hits = [term for term in RISK_TERMS if term.lower() in text.lower()]
    has_separation = any(term.lower() in text.lower() for term in SEPARATION_TERMS)
    warnings = []
    if risk_hits:
        warnings.append("Copy-risk wording found. Confirm why the pattern fits this product.")
    if "경쟁" in text and not has_separation:
        warnings.append("Competitor reference should be separated from applied product requirements.")

    review_dir = Path(args.review_dir)
    review_dir.mkdir(parents=True, exist_ok=True)
    report_path = review_dir / "copy-risk-review.md"
    report_path.write_text(
        "\n".join(
            [
                "# Copy Risk Review",
                "",
                f"- Risk terms: {', '.join(risk_hits) if risk_hits else 'none'}",
                f"- Reference/application separation visible: {has_separation}",
                "",
                "## Warnings",
                *(f"- {warning}" for warning in warnings),
                "",
                "## Required Follow-Up",
                "If applying a reference pattern, record the reason in DECISION_LOG and connect it to Core Intent.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(json.dumps({"risk_terms": risk_hits, "warnings": warnings, "report_path": str(report_path)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
