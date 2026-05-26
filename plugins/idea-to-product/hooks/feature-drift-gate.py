#!/usr/bin/env python3
"""Review whether a feature candidate should be Must-have or Nice-to-have."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

from hook_context import has_active_artifacts, print_skipped


RED_HINTS = ["실시간 채팅", "결제", "관리자 기능", "별도 앱", "마켓플레이스"]
YELLOW_HINTS = ["통계", "대시보드", "자동화", "알림", "AI 추천", "권한", "상태", "화면 하나 더"]


def read_payload() -> dict:
    data = sys.stdin.read().strip()
    if not data:
        return {}
    try:
        return json.loads(data)
    except json.JSONDecodeError:
        return {"user_prompt": data}


def decide(candidate: str) -> tuple[str, str]:
    text = candidate.lower()
    if any(hint.lower() in text for hint in RED_HINTS):
        return "Red", "별도 제품처럼 커지거나 Must-have 운영 복잡도를 크게 늘릴 수 있습니다."
    if any(hint.lower() in text for hint in YELLOW_HINTS):
        return "Yellow", "핵심 목적과 연결될 수 있지만 정책, 상태, 운영, 측정 부담이 늘어납니다."
    return "Green", "Core Intent와 직접 연결된다면 Must-have로 둘 수 있습니다."


def write_report(review_dir: Path, result: dict) -> Path:
    review_dir.mkdir(parents=True, exist_ok=True)
    path = review_dir / "feature-drift-review.md"
    path.write_text(
        "\n".join(
            [
                "# Feature Drift Review",
                "",
                f"- Candidate feature: {result['candidate_feature']}",
                f"- Decision: {result['decision']}",
                f"- Reason: {result['decision_reason']}",
                f"- Priority status: {result['priority_status']}",
                f"- Operating intent impact: {result['operating_intent_impact']}",
                f"- Scalability impact: {result['scalability_impact']}",
                "",
                "## 장점",
                result["benefit"],
                "",
                "## 주의점",
                result["caution"],
                "",
                "## 내 추천",
                result["recommendation"],
                "",
                "## 추천 이유",
                result["recommendation_reason"],
                "",
                "## 다른 선택이 더 나은 경우",
                result["when_other_choice_is_better"],
                "",
                "## Required Confirmation",
                result["required_confirmation"],
                "",
            ]
        ),
        encoding="utf-8",
    )
    return path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--review-dir", default=os.environ.get("ITP_REVIEW_DIR", "reviews"))
    args = parser.parse_args()

    payload = read_payload()
    candidate = payload.get("candidate_feature") or payload.get("user_prompt") or payload.get("prompt")
    if not candidate:
        print_skipped("No feature candidate found; feature drift review was not written.")
        return 0
    if not has_active_artifacts():
        print_skipped("No active Idea to Product artifact found; feature drift review was not written.")
        return 0

    decision, reason = decide(candidate)

    if decision == "Green":
        recommendation = "Must-have 가능"
        required_confirmation = "권장 사항을 사용자에게 보여주고 DECISION_LOG에 기록합니다."
    elif decision == "Yellow":
        recommendation = "축소 Must-have 또는 Nice-to-have로 검토"
        required_confirmation = "사용자가 선택하기 전까지 Must-have로 확정 반영하지 않습니다."
    else:
        recommendation = "Nice-to-have 또는 보류 권장"
        required_confirmation = "Must-have 반영 전 사용자 명시 확인이 필요합니다."

    result = {
        "candidate_feature": candidate,
        "decision": decision,
        "decision_reason": reason,
        "priority_status": "pending_user_confirmation" if decision in {"Yellow", "Red"} else "reviewed",
        "operating_intent_impact": "Production/Pilot에서는 정책과 운영 책임 확인이 필요합니다. Demo/Test/One-off라면 Nice-to-have나 보류가 더 적합할 수 있습니다.",
        "scalability_impact": "반복 사용과 사용자 수 증가를 전제로 할수록 권한, 기록, 예외 처리가 필요합니다.",
        "benefit": "사용자 요청이나 운영 편의를 더 직접적으로 다룰 수 있습니다.",
        "caution": "새 정책, 상태, 권한, 기록, AC가 필요할 수 있습니다.",
        "recommendation": recommendation,
        "recommendation_reason": reason,
        "when_other_choice_is_better": "이미 현장 검증된 강한 수요가 있고 운영 리소스가 준비되어 있다면 더 적극적으로 포함할 수 있습니다.",
        "required_confirmation": required_confirmation,
    }
    report_path = write_report(Path(args.review_dir), result)
    result["report_path"] = str(report_path)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
