# Plugin evals

Run with the Claude Code plugin eval runner (early access; prints "plugin eval is currently in
early access" when not enabled for your organization):

```bash
claude plugin eval . --allow-tools Bash Read --report results/report.html
```

Cases use the fictional workspace in `examples/alex-example`. None of them calls LinkedIn.
Graders: deterministic (`tool_used`, `regex`) plus LLM rubrics for writing quality.
