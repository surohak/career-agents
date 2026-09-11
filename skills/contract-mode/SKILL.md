---
name: contract-mode
description: For people who work on contract or freelance: a rate card from the salary benchmark, an availability line, the LinkedIn Services page and "open to contract" settings text, proposal templates per engagement type, invoicing checklist, and profiles for freelance marketplaces derived from the kernel. Use when target.engagement is contract or the user asks about freelancing.
disable-model-invocation: false
allowed-tools: "Read Write Bash(python3 *)"
---

# Contract mode

Set `career.json` `target.engagement` to `contract` or `both`. Inputs: `positioning.md`,
`cv-canonical.md`, `out/salary-benchmark-*.md`, `voice.md`, `constraints.md`. Output:
`out/contract/` with the files below.

1. **Rate card** (`rates.md`): hourly, daily and monthly retainer, derived from the benchmark
   with the user's chosen position in the range and the overhead they name (tax, insurance,
   unpaid time). Show the arithmetic. Three tiers by engagement (advisory, hands-on delivery,
   embedded team member). Not financial advice; a local accountant for tax.
2. **Availability line**: for the headline suffix and About: from when, hours per week,
   timezone overlap, not "open to work" wording.
3. **LinkedIn Services page** text and the Providing Services setting values; applied by the
   operator under `approvals.linkedin_edit` (it is a profile edit).
4. **Proposal templates** (`proposal-<type>.md`): fixed-scope project, retainer, audit or
   rescue. Each: understanding of the problem (from the brief), approach, deliverables, timeline,
   price from the rate card, assumptions, what is not included, next step. Filled per lead from
   the pipeline row.
5. **Marketplace profiles**: derived text for the platforms the user names (title 70 chars,
   overview 3 paragraphs, skills, portfolio items from `case-study`), through `multi-platform`.
   Never create accounts.
6. **Ops checklist**: contract template pointers (the person's lawyer), invoice fields,
   payment terms, currency, a simple `out/contract/invoices.md` log.

Pipeline rows for contract leads use `source: lead` and stages `found, proposal, negotiation,
won, delivering, closed`; `application-tracker` accepts both sets.
