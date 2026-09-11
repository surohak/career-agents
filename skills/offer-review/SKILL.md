---
name: offer-review
description: When an offer arrives, structure it: comparison table across offers and the current job (cash, equity, bonus, remote, timezone, growth, stability), questions to ask, and a negotiation script grounded in the positioning range. Use when the user shares an offer or asks how to negotiate. Structures information; it is not financial advice.
disable-model-invocation: false
allowed-tools: "Read Write Bash(python3 *)"
---

# Offer review

Inputs: the offer details as the user states them (base, bonus, equity with vesting, currency,
contract or employment, location and tax setup, hours and timezone, start date, benefits),
`positioning.md` (target range if set), `identity.md`, `out/pipeline.md` (other live offers or
late-stage interviews). Output: `out/offer-<company>-<date>.md`.

## 1. Normalize

One table, one column per offer plus the current job: annual base in one currency (user
provides the rate; compute with python), bonus expected value, equity as stated (no valuation
guesses), total cash, contract type, remote and timezone fit, leave, growth (title, scope),
stability signals from `company-research` if run. Unknown cells stay "ask".

## 2. Questions to ask before deciding (max 8)

Only the ones with empty cells or unusual terms: notice period, equity refresh, review cycle,
contractor invoicing and currency, equipment, probation.

## 3. Negotiation script

Anchor on the positioning range and on a fact (the strongest CV proof for this role). Three
lines: appreciation, the one thing to change with a number, the reason. Then two fallbacks
(sign-on, extra leave, earlier review). Never bluff a competing offer that does not exist in the
pipeline. First person, no em dashes.

## 4. Decision aid

A weighted score only if the user gives weights; otherwise list the trade-offs plainly. State
that this structures information and is not financial, tax or legal advice; for equity and tax
across borders, point to a professional.

Sending the negotiation message follows `recruiter-reply` and its approvals. Update the
pipeline row to `offer`.
