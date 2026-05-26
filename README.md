# Idea to Product

Idea to Product is a multi-runtime AI PM plugin that helps non-developers turn ideas into product-ready requirements.

Supported runtimes:

- Claude Code
- Codex
- Claude Cowork + Claude Design

Supported operating systems:

- Windows
- macOS

## Quick Install

Install Codex and Claude Code support with one command.

macOS, Linux, WSL, or Git Bash:

```bash
curl -fsSL https://raw.githubusercontent.com/howbuild/idea-to-product/main/install.sh | sh
```

Windows PowerShell:

```powershell
irm https://raw.githubusercontent.com/howbuild/idea-to-product/main/install.ps1 | iex
```

Install only one runtime on macOS, Linux, WSL, or Git Bash:

```bash
curl -fsSL https://raw.githubusercontent.com/howbuild/idea-to-product/main/install.sh | sh -s -- --codex
curl -fsSL https://raw.githubusercontent.com/howbuild/idea-to-product/main/install.sh | sh -s -- --claude
```

Install only one runtime on Windows PowerShell:

```powershell
$env:ITP_INSTALL_TARGET="codex"; irm https://raw.githubusercontent.com/howbuild/idea-to-product/main/install.ps1 | iex; Remove-Item Env:ITP_INSTALL_TARGET
$env:ITP_INSTALL_TARGET="claude"; irm https://raw.githubusercontent.com/howbuild/idea-to-product/main/install.ps1 | iex; Remove-Item Env:ITP_INSTALL_TARGET
```

For local testing after cloning the repo:

```bash
./install.sh
```

```powershell
.\install.ps1
```

The installer registers `idea-to-product-marketplace`, installs `idea-to-product`, and refreshes an existing install when the marketplace already exists.

### Installer vs Marketplace Commands

The installer is a convenience wrapper around the marketplace flow. It still uses the runtime marketplace system internally.

- Installer: best for users. One command registers the marketplace, installs the plugin, and refreshes an existing registration.
- Marketplace commands: best for debugging or manual control. You run `marketplace add` and `plugin add` / `plugin install` yourself.
- ZIP packages are local build artifacts. They do not need to be committed to this repo.

It is not a PRD generator and it is not a loose collection of skills. The plugin is built around PM workflow orchestration, command entrypoints, hook-based review gates, and specialist reviewer agents. Skills are small reusable helpers used inside that workflow.

## What It Is

Idea to Product helps non-developers participate in product design by working from a structural HTML wireframe, product questions, A/B/C/D choices, recommendation cards, policy decisions, state definitions, event/log design, AC, and final documentation.

The core value is that a non-developer naturally learns product thinking while shaping a buildable requirement set. The plugin does not think instead of the user. It works more like an AI PM partner that asks grounded questions, explains tradeoffs, and keeps product scope from drifting.

Questions are written so the decision is easy to understand at first read, while useful product terms such as PRD, AC, KPI, permission policy, state values, events, logs, and `data-req-id` are kept.

The workflow also uses a Core User Flow:

- Entry and next action: where the user starts and what the user should do next
- Usage scale: how often or how much the action is expected to happen
- Quality criteria: what rules keep the product useful and trustworthy when usage grows

Users learn by:

- looking at a screen structure
- answering questions tied to visible elements
- comparing choices
- reading recommendation reasons
- deciding policies and states
- considering records, events, and KPIs
- separating Must-have from Nice-to-have
- seeing why some features should not be added yet

## Why It Exists

AI tools can quickly create HTML prototypes, but those prototypes often miss the PM layer that developers need before implementation:

- PRD
- AC
- policy
- state values
- exception cases
- permission policy
- measurement and logging
- decision rationale

Without those, the screen may look plausible but still be hard to build, test, operate, or maintain.

## Core Structure

- `workflows/`: defines the PM process from idea intake to final output
- `commands/`: user-facing entrypoints for starting, adding features, generating docs, and reviews
- `hooks/`: automatic quality gates for scope drift, wireframe changes, policy consistency, measurement coverage, completeness, consistency, and final writing
- `agents/`: specialist reviewers for PM, scope, product flow, policy, measurement, QA, tech, and human writing
- `skills/`: small reusable helpers called by workflows, hooks, commands, or agents
- `domains/`: domain-pack injection structure and templates
- `templates/`: output templates for PRD, AC, policy, measurement, decision log, completeness, and review reports
- `mcp/`: suggested MCP integrations and example configuration
- `Claude Design handoff`: brief and prompt templates for visualizing product structure without expanding scope

Idea to Product helps users create:

- PRD
- AC
- Policy document
- Measurement / logging document
- Decision log
- Reference research summary
- Completeness report
- Claude Design handoff brief

## Runtime Modes

### Claude Code Mode

Use this for full plugin automation with commands, hooks, agents, skills, workflows, MCP suggestions, and Python review gates.

### Codex Mode

Use this for Codex plugin workflows with skills, hooks, MCP suggestions, and review gates. Hook trust/setup may be required before automatic review gates run.

### Claude Cowork + Design Mode

Use this for non-developer product sessions and design handoff. Cowork structures product thinking through questions, choices, recommendations, and documents. Claude Design visualizes the agreed structure from a handoff brief and prompt.

### Windows and macOS

Both are supported. Use the OS-specific installation guides:

- [install-windows.md](plugins/idea-to-product/docs/install-windows.md)
- [install-macos.md](plugins/idea-to-product/docs/install-macos.md)

## Skills Are Not The Main System

Skills are supporting modules. They do not define the product workflow by themselves.

For example, `question-designer` helps write better question cards, and `policy-extractor` helps identify policies in a conversation. The main PM process still lives in `workflows/`, starts through `commands/`, is guarded by `hooks/`, and is reviewed by `agents/`.

## Why Hooks Matter

Hooks are quality gates. They automatically review risky moments:

- when a user adds a feature
- when the wireframe changes
- when policy or state changes appear
- when major actions need event/log coverage
- before document generation
- after document generation
- before final output is saved

Hooks do not contain the whole product logic. They detect, warn, request review, create reports, and block or ask for confirmation when needed.

## HTML Wireframe Purpose

The HTML wireframe is not final UI design and not production code.

It is a structural prototype for checking:

- user actions
- screen flow
- required states
- policy connection points
- AC verification points
- question and decision anchors through `data-req-id`

Visual style is intentionally not fixed by this plugin. A project team can decide the real UI style separately.

## Recommendation Format

When the plugin recommends an option, it must include:

- 선택지
- 장점
- 주의점
- 내 추천
- 추천 이유
- 다른 선택이 더 나은 경우

## Claude Code Installation

Recommended install:

```bash
curl -fsSL https://raw.githubusercontent.com/howbuild/idea-to-product/main/install.sh | sh -s -- --claude
```

Windows PowerShell:

```powershell
$env:ITP_INSTALL_TARGET="claude"; irm https://raw.githubusercontent.com/howbuild/idea-to-product/main/install.ps1 | iex; Remove-Item Env:ITP_INSTALL_TARGET
```

For local testing after cloning the repo:

```bash
./install.sh --claude
```

```powershell
.\install.ps1 -Target claude
```

Runtime-specific details are documented in [runtime-installation.md](plugins/idea-to-product/docs/runtime-installation.md) and [install.md](plugins/idea-to-product/.claude-plugin/install.md).

## Claude Code Plugin vs Claude.ai Custom Skill

Claude Code plugins and Claude.ai custom skills are different surfaces.

Claude Code can use the plugin package shape: workflows, commands, hooks, agents, skills, templates, domain injection, and MCP suggestions.

Claude.ai custom skills cannot install this full plugin runtime. In Claude.ai, only selected skill instructions can be uploaded or adapted individually. Hook review gates, command entrypoints, marketplace metadata, and reviewer-agent wiring are Claude Code/Codex plugin concepts, not Claude.ai custom skill behavior.

## Codex Installation

Recommended install:

```bash
curl -fsSL https://raw.githubusercontent.com/howbuild/idea-to-product/main/install.sh | sh -s -- --codex
```

Windows PowerShell:

```powershell
$env:ITP_INSTALL_TARGET="codex"; irm https://raw.githubusercontent.com/howbuild/idea-to-product/main/install.ps1 | iex; Remove-Item Env:ITP_INSTALL_TARGET
```

For local testing after cloning the repo:

```bash
./install.sh --codex
```

```powershell
.\install.ps1 -Target codex
```

After install, review hook trust before enabling lifecycle hooks. The plugin ships hook scripts that can inspect prompts and generate review reports, so the runtime should ask the user to trust or review hooks before activation.

Runtime-specific details are documented in [runtime-installation.md](plugins/idea-to-product/docs/runtime-installation.md) and [install.md](plugins/idea-to-product/.codex-plugin/install.md).

Codex custom agent installation can vary by runtime surface. See [codex-agent-installation.md](plugins/idea-to-product/docs/codex-agent-installation.md) for the limitation and helper script.

## Domain Pack Usage

The core repo does not include real domain packs. It only provides the injection structure and `_template`.

Supported injection modes:

- path-based injection: `Use domain pack from: ../construction-idea-to-product/domains/construction`
- alias-based injection: `Use domain: construction`
- conversation-based injection: user explains the business context in conversation
- document-based injection: user provides manuals, policy docs, PRDs, or forms
- MCP-based injection: runtime reads Notion, Figma, GitHub, wiki, or document storage

Domain packs are question candidates, not confirmed policy. Anything not confirmed by the user must be marked as an assumption or unresolved item.

## Human Writing Auditor

The `human-writing-auditor` skill references `blader/humanizer` as a benchmark for detecting AI-like wording, but does not require it as an external dependency.

This plugin uses its own rewrite rules for:

- removing AI-style openings
- reducing abstract filler
- avoiding over-explaining practical terms
- preserving real work terms such as 권한정책, 상태값, AC, PRD, KPI, 이벤트, and 로그

## Reference and Competitive Research

Idea to Product supports reference research and competitive product research, but the goal is not to create a market research report.

The goal is to create better product questions and better requirement options:

- 더 좋은 질문 만들기
- 정책 후보 찾기
- 상태값 후보 찾기
- 권한정책 후보 찾기
- 측정/기록 후보 찾기
- Must-have 요구사항 판단하기
- Nice-to-have 요구사항 구분하기

Research results should connect to:

- PRD
- policy document
- measurement/logging document
- AC
- decision log

Important: do not copy competitors. Use only patterns that fit the current product's Core Intent, core user, and Must-have/Nice-to-have priority.

Good use:

```text
유사 제품에서는 보통 상태값을 나눠 관리합니다.
우리도 상태값을 둘지 확인해야 합니다.
```

Bad use:

```text
경쟁사가 이렇게 하니까 우리도 이렇게 해야 합니다.
```

Research output must distinguish sourced information from inference. When using Browser, Web, MCP, or user-provided documents, record the source, check date, observed pattern, whether it applies, and limitations.

Usage examples:

```text
Idea to Product로 이 기능과 비슷한 제품이나 업무 흐름을 참고해서 질문 후보를 만들어줘.
```

```text
이 아이디어를 설계하기 전에 유사 제품들이 보통 어떤 상태값과 권한정책을 쓰는지 참고해줘.
```

## Construction Wrapper Plan

Construction-specific domain knowledge belongs in a separate wrapper repo:

```text
construction-idea-to-product
```

That wrapper can provide a construction domain pack, extra question banks, policy checklists, wireframe patterns, and MCP suggestions. The core `idea-to-product` repo remains domain-neutral.

## Assumptions

- Plugin marketplace schemas differ by runtime, so `plugin.yaml`, `plugin.json`, and `marketplace.json` use conservative metadata that can be adapted by each marketplace.
- Claude Code and Codex command names are documented as target usage flows. Exact CLI syntax may need small adjustment if the installed runtime changes its marketplace API.
- Hook scripts are portable Python gate scripts. If a runtime supports agent-based hooks directly, it should use `agents/*.md`; otherwise scripts generate prompts and reports.
- The core repo intentionally includes only a generic "request management board" example and no concrete domain pack.
- The structural HTML wireframe uses readable neutral styling only so that the review screen is understandable. Those styles are not product UI decisions.
