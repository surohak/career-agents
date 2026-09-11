---
name: intake
description: Guided onboarding interview that fills a new person's whole workspace kernel from a conversation, their CV PDF, their LinkedIn and three things they wrote. Infers voice from real writing. Use for a new person after career-setup, or when verify_kernel reports placeholders.
disable-model-invocation: false
allowed-tools: "Read Write Edit Bash(pdftotext *) Bash(${CLAUDE_PLUGIN_ROOT}/scripts/*) Bash(python3 *)"
---

# Intake

Goal: `career.json` and all six `profile/*.md` files filled with facts, in 20 minutes, with no
placeholder left. Run `scripts/verify_kernel.sh` at the end.

## Order

1. **Sources first, questions second.** Ask for a CV PDF (or `pdftotext` it if it is in the
   folder) and the LinkedIn URL; run `profile-fetch`. Read both. Everything they already answer
   is not asked again.
2. **Facts** (from the sources, confirm only the unclear ones): name, current title and company,
   location, country, timezone, work authorization, languages with levels, degrees, links.
   Write `identity.md` and `cv-canonical.md`. Dates in "Mon YYYY".
3. **Target** (ask, max 5 questions): the next role title, seniority, remote or local, markets,
   the three things they are proudest of (each must map to a CV fact), what they want to stop
   being labelled as. Write `positioning.md` and `career.json` `target` and `search`.
4. **Voice**: ask for three things they wrote (posts, emails, a README). If they have LinkedIn
   posts, `search_posts` by their name is not reliable; ask for links. From the texts, note:
   sentence length, first or third person, humour or not, words they repeat, words they never use,
   punctuation habits. Write `voice.md` with observed rules, quote one sentence of theirs as the
   reference tone. Default rules (no em dashes, no invented numbers) stay.
5. **Constraints**: ask what must never appear (clients, internal tools, phone, salary), and
   which automation mode they want with the approvals table explained in one paragraph. Write
   `constraints.md` and `career.json` `automation`.
6. **CV adapter**: where the CV lives (Canva, Word, Google Docs, Markdown, only a PDF) and the
   site URL and repo if any. Write `career.json` `cv` and `site`.
7. Show a one-screen summary, fix what they correct, run `verify_kernel.sh`, then run
   `profile-review` so they see the starting score.

Ask one question at a time. Never ask for passwords. Never fill a fact you did not read or hear.
