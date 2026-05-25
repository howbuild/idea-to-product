# Idea to Product Plugin

Idea to Product는 Claude Code, Codex, Claude Cowork + Claude Design, Windows, macOS를 모두 1급 지원 대상으로 두는 AI PM 플러그인입니다.

이 플러그인은 단순 skill 모음집이 아닙니다.

메인은 다음입니다.

- PM workflow orchestration
- command entrypoints
- hook-based review gates
- specialist reviewer agents
- domain injection
- product thinking education
- design handoff

Skills는 workflow, command, hook, agent가 호출하는 보조 능력입니다.

## 질문과 흐름 기준

질문은 한 번 읽고 결정할 내용이 바로 보여야 합니다. 다만 PRD, AC, KPI, 권한정책, 상태값, 이벤트, 로그, `data-req-id`처럼 실제 요구사항에 필요한 단어는 유지합니다.

핵심 유저 플로우는 다음 세 가지로 봅니다.

- 진입과 다음 행동: 사용자는 어디서 와서 어디로 가나요?
- 사용 규모: 얼마나 많이 지나가게 만들고 싶나요?
- 품질 기준: 사용자가 많아져도 계속 괜찮게 쓰려면 어떤 규칙이 필요할까요?

## 런타임별 사용

- Claude Code: commands, hooks, agents, skills, workflows, Python review gates
- Codex: skills, hooks, MCP suggestions, docs, commands/workflows
- Claude Cowork + Claude Design: 질문/선택지/추천, 제품 요구사항 정리, Design handoff brief, Claude Design prompt
- Windows/macOS: OS별 설치 문서와 검증 스크립트 제공
