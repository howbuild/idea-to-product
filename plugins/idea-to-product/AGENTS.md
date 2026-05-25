# Plugin Agent Instructions

- Treat `workflows/idea-to-product.md` as the top-level orchestration document.
- Treat commands as user entrypoints.
- Treat hooks as quality gates.
- Treat agents as specialist reviewers.
- Treat skills as support modules only.
- Do not create real domain packs in this core plugin.
- Do not use `ux-reviewer`; use `product-flow-reviewer`.
- Do not evaluate final UI visual style. Review product flow, states, actions, policies, measurement, and AC coverage.
- Keep the HTML wireframe as a structural prototype.
- Do not confirm new MVP scope until the user explicitly chooses after a Green/Yellow/Red feature review.
