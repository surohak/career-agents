---
type: llm
criteria: "Does the summary use only facts from examples/alex-example/profile/cv-canonical.md, with no new numbers, employers, dates or tools, while using the job's vocabulary where the CV supports it?"
focus: "Fact discipline"
target: last_message
---
Good: three lines, terms like observability or performance only where the example CV shows that work, no percentages or counts absent from the CV.
Bad: any metric not in the CV, a claim of mentoring if the CV has none, more than three lines.
