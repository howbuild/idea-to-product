#!/usr/bin/env python3
"""Review structural wireframe changes for new actions, states, policies, and AC anchors."""

from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path

from hook_context import has_active_artifacts, print_skipped


REQ_RE = re.compile(r"data-req-id=[\"']([^\"']+)[\"']")
ACTION_RE = re.compile(r"<button|role=[\"']button|type=[\"']submit", re.IGNORECASE)
STATE_WORDS = ["empty", "error", "permission", "권한", "빈 상태", "오류", "완료", "보류", "처리중"]


def read_text(path: Path) -> str:
    if path.exists():
        return path.read_text(encoding="utf-8")
    return ""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--wireframe", default=os.environ.get("ITP_WIREFRAME", "wireframe.html"))
    parser.add_argument("--review-dir", default=os.environ.get("ITP_REVIEW_DIR", "reviews"))
    args = parser.parse_args()

    if not has_active_artifacts(paths=[args.wireframe]):
        print_skipped("No wireframe found; wireframe review was not written.")
        return 0

    text = read_text(Path(args.wireframe))
    if not text.strip():
        print_skipped("No wireframe content found; wireframe review was not written.")
        return 0

    req_ids = sorted(set(REQ_RE.findall(text)))
    action_count = len(ACTION_RE.findall(text))
    state_hits = [word for word in STATE_WORDS if word.lower() in text.lower()]

    issues = []
    if not req_ids:
        issues.append("No data-req-id values found.")
    if action_count and "policy" not in text.lower() and "정책" not in text:
        issues.append("Actions exist but policy connection is not visible in the wireframe.")
    if action_count and "AC" not in text:
        issues.append("Actions exist but AC anchors are not visible.")
    if not state_hits:
        issues.append("No obvious empty, error, permission, or workflow state markers found.")

    suggested_next_hooks = []
    if any("policy" in issue.lower() or "정책" in issue for issue in issues):
        suggested_next_hooks.append("policy-consistency-review.py")
    if action_count:
        suggested_next_hooks.append("measurement-coverage-review.py")

    review_dir = Path(args.review_dir)
    review_dir.mkdir(parents=True, exist_ok=True)
    report_path = review_dir / "wireframe-change-review.md"
    report_path.write_text(
        "\n".join(
            [
                "# Wireframe Change Review",
                "",
                f"- Wireframe: {args.wireframe}",
                f"- data-req-id count: {len(req_ids)}",
                f"- Action count: {action_count}",
                f"- State markers: {', '.join(state_hits) if state_hits else 'none'}",
                "",
                "## Issues",
                *(f"- {issue}" for issue in issues),
                "",
                "## Suggested Next Hooks",
                *(f"- {hook}" for hook in suggested_next_hooks),
                "",
            ]
        ),
        encoding="utf-8",
    )

    print(
        json.dumps(
            {
                "data_req_id_count": len(req_ids),
                "action_count": action_count,
                "issues": issues,
                "suggested_next_hooks": suggested_next_hooks,
                "report_path": str(report_path),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
