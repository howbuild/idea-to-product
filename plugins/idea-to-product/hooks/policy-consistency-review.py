#!/usr/bin/env python3
"""Check whether policy, state, and permission details are visible and connected."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from hook_context import has_active_artifacts, print_skipped


CHECKS = {
    "state_values": ["상태", "접수", "처리중", "완료", "보류"],
    "permissions": ["권한", "누가", "역할", "permission"],
    "exceptions": ["예외", "오류", "권한 없음", "empty", "error"],
    "state_reason": ["사유", "왜", "reason"],
    "related_ac": ["AC", "Given", "When", "Then"],
}


def load(paths: list[str]) -> str:
    combined = []
    for raw in paths:
        path = Path(raw)
        if path.exists():
            combined.append(path.read_text(encoding="utf-8"))
    return "\n".join(combined)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", nargs="*", default=["PRD.md", "POLICY.md", "AC.md", "wireframe.html"])
    parser.add_argument("--review-dir", default=os.environ.get("ITP_REVIEW_DIR", "reviews"))
    args = parser.parse_args()

    if not has_active_artifacts(paths=args.files):
        print_skipped("No Idea to Product policy documents found; policy review was not written.")
        return 0

    text = load(args.files)
    if not text.strip():
        print_skipped("No Idea to Product policy document content found; policy review was not written.")
        return 0

    missing = []
    for check, terms in CHECKS.items():
        if not any(term.lower() in text.lower() for term in terms):
            missing.append(check)

    review_dir = Path(args.review_dir)
    review_dir.mkdir(parents=True, exist_ok=True)
    report_path = review_dir / "policy-consistency-review.md"
    report_path.write_text(
        "\n".join(
            [
                "# Policy Consistency Review",
                "",
                f"- Checked files: {', '.join(args.files)}",
                "",
                "## Missing Or Weak Areas",
                *(f"- {item}" for item in missing),
                "",
                "## Recommendation",
                "Missing areas should become the next question candidates before final document generation.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(json.dumps({"missing": missing, "report_path": str(report_path)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
