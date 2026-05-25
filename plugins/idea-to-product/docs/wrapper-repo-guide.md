# Wrapper Repo Guide

A wrapper repo can package domain-specific content around the core plugin.

Recommended shape:

```text
domain-wrapper/
  README.md
  domains/
    domain-id/
      domain.yaml
      glossary.md
      question-bank.md
      policy-checklist.md
      measurement-checklist.md
      wireframe-patterns.md
      mcp-suggestions.md
```

The wrapper should depend on or reference `idea-to-product`, not copy core workflow logic unless there is a strong reason.
