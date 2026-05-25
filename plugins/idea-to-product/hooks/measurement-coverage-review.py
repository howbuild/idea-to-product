#!/usr/bin/env python3
"""Check whether major actions and state changes have measurement/logging coverage."""

from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path


BUTTON_RE = re.compile(r"<button[^>]*>(.*?)</button>", re.IGNORECASE | re.DOTALL)
STATE_TERMS = ["접수", "처리중", "완료", "보류", "취소", "삭제", "수정", "등록"]


def read(path: str) -> str:
    file = Path(path)
    return file.read_text(encoding="utf-8") if file.exists() else ""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--wireframe", default="wireframe.html")
    parser.add_argument("--measurement", default="MEASUREMENT.md")
    parser.add_argument("--review-dir", default=os.environ.get("ITP_REVIEW_DIR", "reviews"))
    args = parser.parse_args()

    wireframe = read(args.wireframe)
    measurement = read(args.measurement)
    buttons = [re.sub(r"<[^>]+>", "", match).strip() for match in BUTTON_RE.findall(wireframe)]
    state_hits = [term for term in STATE_TERMS if term in wireframe]
    uncovered_buttons = [button for button in buttons if button and button not in measurement]
    uncovered_states = [term for term in state_hits if term not in measurement]

    warnings = []
    if uncovered_buttons:
        warnings.append("Some visible actions do not appear in MEASUREMENT.")
    if uncovered_states:
        warnings.append("Some state changes do not appear in MEASUREMENT.")
    if "기록하지 않을 정보" not in measurement:
        warnings.append("The measurement document should define information not to record.")
    if "KPI" not in measurement:
        warnings.append("Events should connect to KPI.")

    review_dir = Path(args.review_dir)
    review_dir.mkdir(parents=True, exist_ok=True)
    report_path = review_dir / "measurement-coverage-review.md"
    report_path.write_text(
        "\n".join(
            [
                "# Measurement Coverage Review",
                "",
                "## Visible Actions Without Measurement",
                *(f"- {button}" for button in uncovered_buttons),
                "",
                "## State Terms Without Measurement",
                *(f"- {state}" for state in uncovered_states),
                "",
                "## Warnings",
                *(f"- {warning}" for warning in warnings),
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "uncovered_buttons": uncovered_buttons,
                "uncovered_states": uncovered_states,
                "warnings": warnings,
                "report_path": str(report_path),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
