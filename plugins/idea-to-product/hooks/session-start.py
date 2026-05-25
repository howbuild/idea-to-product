#!/usr/bin/env python3
"""Print a short plugin loading message."""


def main() -> int:
    print(
        "Idea to Product loaded.\n"
        "아이디어를 입력하면 화면 기반 질문으로 PRD, AC, 정책문서, 측정/기록 문서, 결정근거를 만들 수 있습니다."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
