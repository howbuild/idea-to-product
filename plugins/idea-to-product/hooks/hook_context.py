#!/usr/bin/env python3
"""Shared guards for Idea to Product lifecycle hooks."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Iterable


ARTIFACT_NAMES = [
    "PM_NOTE.md",
    "PRD.md",
    "AC.md",
    "POLICY.md",
    "MEASUREMENT.md",
    "DECISION_LOG.md",
    "COMPLETENESS.md",
    "REVIEW_REPORT.md",
    "REFERENCE_RESEARCH.md",
    "DESIGN_HANDOFF_BRIEF.md",
    "CLAUDE_DESIGN_PROMPT.md",
    "wireframe.html",
]

ARTIFACT_SIGNATURES = {
    "PM_NOTE.md": ["PM_NOTE", "Idea to Product", "Core Intent Card"],
    "PRD.md": ["Must-have", "운영 의도", "확장 가능성"],
    "AC.md": ["Given", "When", "Then", "관련 요구사항"],
    "POLICY.md": ["정책 ID", "관련 요구사항", "운영 의도"],
    "MEASUREMENT.md": ["측정 ID", "기록할 행동", "운영 의도"],
    "DECISION_LOG.md": ["질문 ID", "사용자의 선택", "결정 이유"],
    "COMPLETENESS.md": ["COMPLETENESS", "기능 요구사항"],
    "REVIEW_REPORT.md": ["리뷰 유형", "관련 요구사항"],
    "REFERENCE_RESEARCH.md": ["REFERENCE_RESEARCH", "결정근거 연결"],
    "DESIGN_HANDOFF_BRIEF.md": ["DESIGN_HANDOFF_BRIEF", "Must-have"],
    "CLAUDE_DESIGN_PROMPT.md": ["CLAUDE_DESIGN_PROMPT", "Must-have"],
    "wireframe.html": ["data-req-id"],
}


def is_forced() -> bool:
    return os.environ.get("ITP_ACTIVE", "").lower() in {"1", "true", "yes", "on"}


def looks_like_itp_artifact(path: str | Path) -> bool:
    if is_forced():
        return Path(path).exists()

    file = Path(path)
    if not file.exists() or not file.is_file():
        return False

    markers = ARTIFACT_SIGNATURES.get(file.name)
    if not markers:
        return False

    try:
        text = file.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return False
    return all(marker in text for marker in markers)


def existing_files(paths: Iterable[str]) -> list[Path]:
    return [Path(raw) for raw in paths if looks_like_itp_artifact(raw)]


def has_active_artifacts(base_dir: str | Path = ".", paths: Iterable[str] | None = None) -> bool:
    if is_forced():
        return True
    if paths is not None:
        if existing_files(paths):
            return True

    base = Path(base_dir)
    return any(looks_like_itp_artifact(base / name) for name in ARTIFACT_NAMES)


def has_domain_pack(path: str | Path) -> bool:
    if is_forced():
        return True
    base = Path(path)
    required = ["domain.yaml", "question-bank.md", "policy-checklist.md", "measurement-checklist.md"]
    return base.exists() and all((base / name).exists() for name in required)


def has_prompt_intent(prompt: str) -> bool:
    if is_forced():
        return True
    lowered = prompt.lower()
    triggers = ["idea to product", "아이디어를 제품", "제품 요구사항", "prd", "정책문서", "측정/기록", "결정근거"]
    return any(trigger.lower() in lowered for trigger in triggers)


def should_review_prompt(prompt: str, base_dir: str | Path = ".") -> bool:
    if has_prompt_intent(prompt):
        return True
    return has_active_artifacts(base_dir=base_dir)


def print_skipped(reason: str) -> None:
    print(json.dumps({"skipped": True, "reason": reason}, ensure_ascii=False, indent=2))


def main() -> int:
    print(json.dumps({"ok": True, "module": "hook_context"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
