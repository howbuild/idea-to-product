#!/usr/bin/env python3
"""Warn when reference review appears needed but is missing or not connected."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from hook_context import has_active_artifacts, print_skipped


REFERENCE_TERMS = ["레퍼런스", "경쟁", "유사", "다른 서비스", "벤치마크", "reference", "competitor"]
CONNECTION_TERMS = ["질문", "정책", "상태", "권한", "측정", "기록", "AC", "Must-have", "Nice-to-have", "운영 의도", "확장 가능성"]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-dir", default=".")
    parser.add_argument("--review-dir", default=os.environ.get("ITP_REVIEW_DIR", "reviews"))
    args = parser.parse_args()

    base = Path(args.base_dir)
    paths = [str(base / name) for name in ["PRD.md", "DECISION_LOG.md", "REFERENCE_RESEARCH.md"]]
    if not has_active_artifacts(base_dir=base, paths=paths):
        print_skipped("No Idea to Product reference context found; reference review was not written.")
        return 0

    docs = "\n".join(read(base / name) for name in ["PRD.md", "DECISION_LOG.md", "REFERENCE_RESEARCH.md"])
    if not docs.strip():
        print_skipped("No Idea to Product reference context content found; reference review was not written.")
        return 0

    reference_doc = read(base / "REFERENCE_RESEARCH.md")
    mentions_reference = any(term.lower() in docs.lower() for term in REFERENCE_TERMS)
    has_reference_doc = bool(reference_doc.strip())
    connected = any(term.lower() in reference_doc.lower() for term in CONNECTION_TERMS)

    warnings = []
    if mentions_reference and not has_reference_doc:
        warnings.append("Reference or competitor research is mentioned, but REFERENCE_RESEARCH.md is missing.")
    if has_reference_doc and not connected:
        warnings.append("Reference findings are not clearly connected to questions, policy, state, measurement, Must-have/Nice-to-have priority, operating intent, scalability, or AC.")
    if "출처" not in reference_doc and has_reference_doc:
        warnings.append("Reference research exists but sources are not visible.")

    review_dir = Path(args.review_dir)
    review_dir.mkdir(parents=True, exist_ok=True)
    report_path = review_dir / "reference-gap-review.md"
    report_path.write_text(
        "\n".join(
            [
                "# Reference Gap Review",
                "",
                f"- Mentions reference: {mentions_reference}",
                f"- Has REFERENCE_RESEARCH.md: {has_reference_doc}",
                f"- Connected to requirement artifacts: {connected}",
                "",
                "## Warnings",
                *(f"- {warning}" for warning in warnings),
                "",
                "## Rule",
                "Reference research is optional unless it is needed for better questions or ambiguous Must-have/Nice-to-have priority. If skipped, mark related claims as 미확인.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(json.dumps({"warnings": warnings, "report_path": str(report_path)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
