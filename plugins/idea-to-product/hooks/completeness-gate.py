#!/usr/bin/env python3
"""Score PRD completeness before document generation."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path


CATEGORIES = [
    ("문제와 배경", 10, ["문제", "배경"]),
    ("핵심 사용자", 10, ["핵심 사용자", "사용자"]),
    ("핵심 가치와 KPI", 10, ["핵심 가치", "KPI", "성공 지표"]),
    ("MVP 범위와 제외 범위", 10, ["MVP", "제외 범위"]),
    ("핵심 화면과 사용자 여정", 10, ["화면", "사용자 여정"]),
    ("핵심 유저 플로우", 10, ["핵심 유저 플로우", "진입", "사용 규모", "품질 기준"]),
    ("기능 요구사항", 10, ["기능", "요구사항"]),
    ("정책 정의", 10, ["정책", "권한"]),
    ("상태, 권한, 예외", 10, ["상태", "권한", "예외"]),
    ("측정/기록 설계", 10, ["측정", "기록", "이벤트"]),
    ("AC 작성", 5, ["Given", "When", "Then", "AC"]),
    ("결정근거 정리", 5, ["결정", "근거", "DECISION"]),
]


def bar(percent: int) -> str:
    filled = max(0, min(10, round(percent / 10)))
    return "█" * filled + "░" * (10 - filled)


def read_files(paths: list[str]) -> str:
    chunks = []
    for raw in paths:
        path = Path(raw)
        if path.exists():
            chunks.append(path.read_text(encoding="utf-8"))
    return "\n".join(chunks)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", nargs="*", default=["PRD.md", "POLICY.md", "MEASUREMENT.md", "AC.md", "DECISION_LOG.md"])
    parser.add_argument("--review-dir", default=os.environ.get("ITP_REVIEW_DIR", "reviews"))
    args = parser.parse_args()

    text = read_files(args.files)
    reference_research_exists = Path("REFERENCE_RESEARCH.md").exists() or "참고한 레퍼런스" in text or "Reference" in text
    reference_status = "완료" if reference_research_exists else "미완료 / 불필요 판단 필요"
    scores = []
    total = 0
    max_total = sum(weight for _, weight, _ in CATEGORIES)
    for name, weight, terms in CATEGORIES:
        hits = sum(1 for term in terms if term.lower() in text.lower())
        score = weight if hits == len(terms) else round(weight * hits / len(terms))
        scores.append({"name": name, "score": score, "max": weight, "percent": round(score / weight * 100)})
        total += score

    total_percent = round(total / max_total * 100)
    weak = [item for item in scores if item["percent"] < 50]
    warnings = []
    if total_percent < 70:
        warnings.append("총점 70점 미만입니다. draft 생성은 가능하지만 사용자 확인이 필요합니다.")
    if any(item["name"] == "정책 정의" and item["percent"] < 50 for item in scores):
        warnings.append("정책 정의 50점 미만입니다.")
    if any(item["name"] == "상태, 권한, 예외" and item["percent"] < 50 for item in scores):
        warnings.append("상태/권한/예외 50점 미만입니다.")
    if any(item["name"] == "측정/기록 설계" and item["percent"] < 50 for item in scores):
        warnings.append("측정/기록 50점 미만입니다.")
    if any(item["name"] == "AC 작성" and item["percent"] < 50 for item in scores):
        warnings.append("AC 50점 미만입니다.")

    next_questions = [f"{item['name']}를 구체화하는 질문이 필요합니다." for item in weak]

    review_dir = Path(args.review_dir)
    review_dir.mkdir(parents=True, exist_ok=True)
    report_path = review_dir / "completeness-review.md"
    lines = ["# Completeness Review", "", f"- Total: {total_percent}/100", f"- Reference Review: {reference_status}", "", "## Scores"]
    for item in scores:
        lines.append(f"- {item['name']:<18} {bar(item['percent'])} {item['percent']}%")
    lines.extend(["", "## Warnings", *(f"- {warning}" for warning in warnings), "", "## Next Question Candidates", *(f"- {q}" for q in next_questions), ""])
    report_path.write_text("\n".join(lines), encoding="utf-8")

    print(
        json.dumps(
            {
                "total": total_percent,
                "scores": scores,
                "warnings": warnings,
                "next_questions": next_questions,
                "reference_review": reference_status,
                "can_generate_final": total_percent >= 70,
                "report_path": str(report_path),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
