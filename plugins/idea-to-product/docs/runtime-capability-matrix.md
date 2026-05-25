# Runtime Capability Matrix

| 기능 | Claude Code | Codex | Claude Cowork + Design |
|---|---|---|---|
| Plugin 설치 | 지원 | 지원 | 지원 |
| Commands | 지원 | 지원 또는 문서화된 entrypoint | Cowork command/workflow |
| Workflows | 지원 | 지원 | 지원 |
| Agents | 지원 | 지원 제한 가능, limitation 문서화 | sub-agent 또는 reviewer 문서 기반 |
| Skills | 지원 | 지원 | 지원 |
| Hooks 자동 실행 | 지원 | 지원, trust 필요 | 제한적일 수 있음 |
| Python review gate | 지원 | 지원 가능 | 기본 경로 아님 |
| Feature Drift Review | hook 자동 실행 | hook 자동 실행 또는 trust 후 실행 | Cowork workflow checkpoint |
| Policy Review | hook/agent | hook/agent | Cowork workflow checkpoint |
| Measurement Review | hook/agent | hook/agent | Cowork workflow checkpoint |
| PRD/AC/Policy 생성 | 지원 | 지원 | 지원 |
| Claude Design Handoff | 문서 생성 | 문서 생성 | 핵심 경로 |
| Windows | 지원 문서 제공 | 지원 문서 제공 | 지원 문서 제공 |
| macOS | 지원 문서 제공 | 지원 문서 제공 | 지원 문서 제공 |

## Notes

- Codex hook execution may require trust/setup.
- Codex configs omit `UserPromptExpansion` because support can vary by runtime surface.
- Codex custom agent installation may be limited by runtime surface.
- Claude Cowork + Design may use workflow checkpoints instead of automatic Python hooks.
- Windows hook configs use `py -3`; macOS hook configs use `python3`.
- Limitations are documented instead of removing runtime support.
