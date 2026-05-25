# Idea to Product

Idea to Product는 비개발자가 아이디어를 제품 요구사항으로 구체화하도록 돕는 멀티 런타임 AI PM 플러그인입니다.

지원 런타임:

- Claude Code
- Codex
- Claude Cowork + Claude Design

지원 운영체제:

- Windows
- macOS

## 빠른 설치

Codex와 Claude Code를 한 번에 설치합니다.

macOS, Linux, WSL, Git Bash:

```bash
curl -fsSL https://raw.githubusercontent.com/howbuild/idea-to-product/main/install.sh | sh
```

Windows PowerShell:

```powershell
irm https://raw.githubusercontent.com/howbuild/idea-to-product/main/install.ps1 | iex
```

하나만 설치할 수도 있습니다.

macOS, Linux, WSL, Git Bash:

```bash
curl -fsSL https://raw.githubusercontent.com/howbuild/idea-to-product/main/install.sh | sh -s -- --codex
curl -fsSL https://raw.githubusercontent.com/howbuild/idea-to-product/main/install.sh | sh -s -- --claude
```

Windows PowerShell:

```powershell
$env:ITP_INSTALL_TARGET="codex"; irm https://raw.githubusercontent.com/howbuild/idea-to-product/main/install.ps1 | iex; Remove-Item Env:ITP_INSTALL_TARGET
$env:ITP_INSTALL_TARGET="claude"; irm https://raw.githubusercontent.com/howbuild/idea-to-product/main/install.ps1 | iex; Remove-Item Env:ITP_INSTALL_TARGET
```

로컬에서 테스트할 때는 repo를 받은 뒤 실행합니다.

```bash
./install.sh
```

```powershell
.\install.ps1
```

설치 스크립트는 `idea-to-product-marketplace`를 등록하고 `idea-to-product` 플러그인을 설치합니다. 이미 등록되어 있으면 현재 소스로 다시 등록한 뒤 설치를 갱신합니다.

### 설치 스크립트와 marketplace 명령의 차이

설치 스크립트는 marketplace 방식을 대체하는 게 아니라, 그 명령들을 감싼 편의 래퍼입니다.

- 설치 스크립트: 사용자가 쓰기 편한 방식입니다. marketplace 등록, 플러그인 설치, 기존 등록 갱신을 한 번에 처리합니다.
- marketplace 직접 명령: 디버깅하거나 수동으로 제어할 때 좋습니다. `marketplace add`, `plugin add` / `plugin install`을 직접 실행합니다.
- ZIP 패키지는 로컬 빌드 산출물입니다. repo에 커밋할 필요는 없습니다.

## 무엇을 만드는가

- PRD
- AC
- 정책 문서
- 측정/기록 문서
- 결정근거 문서
- 레퍼런스 조사 요약
- 완성도 리포트
- Claude Design handoff brief
- 구조적 HTML wireframe

## 중요한 점

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

## 런타임 모드

### Claude Code

commands, hooks, agents, skills, workflows, Python review gate를 사용하는 전체 플러그인 자동화 경로입니다.

### Codex

plugin 설치, skills, hooks, MCP suggestions, review gate를 지원합니다. Hooks는 trust/setup이 필요할 수 있습니다.

### Claude Cowork + Claude Design

비개발자 세션과 디자인 handoff를 위한 경로입니다. Cowork는 제품 사고와 요구사항 정리를 돕고, Claude Design은 합의된 구조를 시각화합니다.

### Windows / macOS

두 운영체제를 모두 지원합니다. OS별 설치 문서는 `plugins/idea-to-product/docs/`를 참고합니다.
