#!/usr/bin/env python3
"""Detect prompt intent and route risky product changes to review hooks."""

from __future__ import annotations

import json
import os
import sys


FEATURE_KEYWORDS = [
    "추가",
    "넣고 싶",
    "이것도",
    "그리고",
    "기능 하나 더",
    "화면 하나 더",
    "통계",
    "자동화",
    "알림",
    "실시간",
    "AI 추천",
    "대시보드",
    "관리자 기능",
    "결제",
    "권한",
    "상태",
]

DOCUMENT_KEYWORDS = ["문서", "PRD", "AC", "정책", "측정", "기록", "완성도", "생성"]
WIREFRAME_KEYWORDS = ["와이어프레임", "화면", "버튼", "필터", "상태", "HTML"]


def read_prompt() -> str:
    if len(sys.argv) > 1:
        return " ".join(sys.argv[1:])
    if os.environ.get("USER_PROMPT"):
        return os.environ["USER_PROMPT"]
    data = sys.stdin.read().strip()
    if not data:
        return ""
    try:
        parsed = json.loads(data)
    except json.JSONDecodeError:
        return data
    return str(parsed.get("prompt") or parsed.get("user_prompt") or parsed)


def main() -> int:
    prompt = read_prompt()
    found_features = [kw for kw in FEATURE_KEYWORDS if kw.lower() in prompt.lower()]
    found_docs = [kw for kw in DOCUMENT_KEYWORDS if kw.lower() in prompt.lower()]
    found_wireframe = [kw for kw in WIREFRAME_KEYWORDS if kw.lower() in prompt.lower()]

    if found_features:
        detected_intent = "feature_or_scope_change"
        suggested_next_hook = "feature-drift-gate.py"
    elif found_docs:
        detected_intent = "document_generation_or_review"
        suggested_next_hook = "completeness-gate.py"
    elif found_wireframe:
        detected_intent = "wireframe_change"
        suggested_next_hook = "wireframe-change-review.py"
    else:
        detected_intent = "general_product_work"
        suggested_next_hook = None

    result = {
        "detected_intent": detected_intent,
        "suspected_new_feature": bool(found_features),
        "requires_drift_review": bool(found_features),
        "matched_keywords": found_features + found_docs + found_wireframe,
        "suggested_next_hook": suggested_next_hook,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
