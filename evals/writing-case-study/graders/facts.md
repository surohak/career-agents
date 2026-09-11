---
type: llm
criteria: "Does the text use only facts (employers, dates, numbers, stack) present in examples/alex-example/profile/cv-canonical.md, in first person, without 'open to work' phrasing, and without any client or internal-tool names that the example constraints forbid?"
focus: "No invented facts, voice rules"
target: last_message
---
Good: every number and employer traceable to the example CV; first person; ends without filler.
Bad: any invented metric, a new employer or tool, third person, "open to work".
