---
name: recommendations
description: Plan LinkedIn social proof: pick ex-colleagues and managers to ask for recommendations, draft the request notes and a suggested recommendation text each can adapt, plus a skills endorsement plan. Use when the profile has fewer than 3 recommendations or the user asks for social proof.
disable-model-invocation: false
allowed-tools: "Read Write"
---

# Recommendations

Read `cv-canonical.md`, `identity.md`, `voice.md`, `sources/linkedin.md` (recommendations
section if present, else assume none). Output: `out/recommendations.md`.

## 1. Who to ask

From each role in the last 8 years, up to 3 people: a manager, a peer, a person you unblocked
(a report, a client contact, a designer). Ask the user for names if the CV does not carry them;
`search_people` with company and role can help find current titles, one call per company.
Priority: people who saw the strongest CV facts happen. Target 5 requests, 3 accepted.

## 2. Request notes (under 300 chars each, LinkedIn's limit)

Personal, one specific shared thing, what the recommendation would help with (the target
role), an offer to write one for them first. No pressure line.

## 3. Suggested text for each (150 to 220 words)

Written in the recommender's likely voice, not the user's: what they saw the user do, one
concrete outcome from the CV, one working trait shown by a fact, a closing line about hiring
again. Mark it clearly as "adapt freely". Never fabricate an outcome the recommender did not
witness; pick facts from the role they shared.

## 4. Endorsements

Top 5 pinned skills from `positioning.md`; list which of the people above can credibly endorse
each; suggest endorsing them back first on real skills.

## Sending

Recommendation requests are messages: `draft` lists them; `assisted` and `auto` send through
the LinkedIn MCP `send_message` under `approvals.message` (default on). Track in
`out/pipeline.md`? No: track in `out/recommendations.md` with asked, received, thanked dates.
