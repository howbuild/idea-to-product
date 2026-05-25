# Idea to Product Plugin

Idea to Product is the plugin package inside the `idea-to-product` core repo.

Supported runtimes:

- Claude Code
- Codex
- Claude Cowork + Claude Design

Supported operating systems:

- Windows
- macOS

The plugin helps a non-developer turn an idea into developer-ready product requirements by using:

- PM workflows
- commands
- hook review gates
- specialist reviewer agents
- supporting skills
- domain-pack injection
- reference and competitive research support
- output templates
- MCP suggestions
- Claude Design handoff briefs and prompts

The main entry workflow is [idea-to-product.md](workflows/idea-to-product.md).

## Question and Flow Style

Questions should be easy to understand at first read while keeping useful product terms such as PRD, AC, KPI, permission policy, state values, events, logs, and `data-req-id`.

The workflow uses a Core User Flow:

- 진입과 다음 행동: where the user comes from and where the user goes next
- 사용 규모: how much usage or repeated action should pass through
- 품질 기준: what rules keep the product useful and trustworthy when usage grows

## Reference Research

Reference and competitive research are supported as a helper layer. The goal is not a market research report.

Use research to create better:

- questions
- policy candidates
- state candidates
- permission candidates
- measurement/logging candidates
- MVP and v2 decisions

Research findings must be connected to PRD, policy, measurement, AC, or decision log. Competitors must not be copied.

## What This Plugin Produces

- PRD
- AC
- policy document
- measurement/logging document
- decision log
- PRD completeness report
- review report
- structural HTML wireframe
- optional `REFERENCE_RESEARCH.md` when reference research is performed
- optional `DESIGN_HANDOFF_BRIEF.md` and `CLAUDE_DESIGN_PROMPT.md` when handing off to Claude Design

## What This Plugin Does Not Do

- It does not generate production application code.
- It does not treat the HTML wireframe as final UI design.
- It does not include concrete domain packs in core.
- It does not treat skills as the main orchestration layer.
- It does not reduce support to only one runtime surface.

## Main Components

- `workflows/`: process
- `commands/`: user entrypoints
- `hooks/`: review gates
- `agents/`: reviewers
- `skills/`: support modules
- `domains/`: injection template
- `templates/`: output formats
- `mcp/`: external context suggestions
