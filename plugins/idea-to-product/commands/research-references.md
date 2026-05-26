---
description: Research references and convert findings into product decision inputs.
---

# Command: research-references

Use when the user asks for reference or competitive research, or when the workflow needs better question candidates.

## Example Requests

- "이런 기능을 가진 서비스가 있는지 참고해서 질문해줘"
- "다른 제품들은 보통 어떻게 하는지 보고 싶어"
- "이 기능의 일반적인 정책을 조사해줘"

## Run

1. Confirm the research purpose from context.
2. Decide research targets.
3. Use Browser/Web/MCP when available and appropriate.
4. If external access is unavailable, use only user-provided documents or examples.
5. Summarize findings as product-relevant patterns.
6. Convert findings into question candidates.
7. Record sources, check date, observed pattern, application decision, and limitations.

## Output

Use `templates/reference-research.md` when research is performed.

Research should produce:

- questions
- policy candidates
- state candidates
- permission candidates
- measurement/logging candidates
- Must-have or Nice-to-have judgments
- AC candidates
