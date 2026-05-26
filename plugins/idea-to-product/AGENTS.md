# Plugin Agent Instructions

- Treat `workflows/idea-to-product.md` as the top-level orchestration document.
- Treat commands as user entrypoints.
- Treat hooks as quality gates.
- Treat agents as specialist reviewers.
- Treat skills as support modules only.
- Do not create real domain packs in this core plugin.
- Do not use `ux-reviewer`; use `product-flow-reviewer`.
- Do not evaluate final UI visual style. Review product flow, states, actions, policies, measurement, and AC coverage.
- Use the Core User Flow as 진입과 다음 행동, 사용 규모, and 품질 기준. Ask it in concrete language, not as abstract flow theory.
- Product questions should be easy to understand at first read while keeping useful practical terms.
- Keep the HTML wireframe as a structural prototype.
- Do not mark a new feature as Must-have until the user explicitly chooses after a Green/Yellow/Red feature review.
