---
name: multilingual
description: Produce a second-language version of the headline, About, experience descriptions and CV (German, French, Spanish, Portuguese, or any language the user names) that stays fact-identical to the canonical CV, with a back-translation check. Use for people targeting a local market or when a job post is in another language.
disable-model-invocation: false
allowed-tools: "Read Write Bash(python3 *)"
---

# Multilingual

Inputs: the target language and market, `cv-canonical.md`, the latest rebuild round,
`voice.md`, `positioning.md`. Output: `out/i18n/<lang>/cv.md`, `linkedin.md`, and
`glossary.md`.

## Rules

1. Facts identical: same dates, titles, employers, numbers. Titles are translated only if the
   market uses a local equivalent (say "Senior Software Engineer" stays in most markets; give
   the local convention and let the user choose).
2. Glossary first: stack names stay in English; recurring terms get one fixed translation,
   listed in `glossary.md` so rounds stay consistent.
3. Register: formal address where the market expects it in CVs (German Sie is not used in a CV
   but formal tone is; French CV conventions differ from LinkedIn tone). State the convention
   applied in one line.
4. Back-translate each block to English and diff against the source with
   `scripts/profile_diff.py` semantics in mind: any fact that changed is a bug, fix it.
5. LinkedIn supports secondary language profiles (Add profile in another language): produce
   the fields for that dialog. Apply through `linkedin-apply` by mode.
6. CV: through the adapter as a copy (`out/i18n/<lang>/cv.pdf`), never overwriting the primary.

No em dashes in any language. Do not translate proper nouns or product names.
