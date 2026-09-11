---
name: cv-update
description: Apply accepted audit findings to the CV through the configured adapter (Canva, DOCX, Markdown/HTML, Google Docs), export a PDF and verify it. Use after the user has chosen which findings to apply. Every commit and export needs an explicit yes.
disable-model-invocation: false
allowed-tools: "Read Write Edit Bash(pdftotext *) Bash(pdfinfo *) Bash(pdftoppm *) Bash(python3 *) Bash(pandoc *)"
---

# CV update

Order of truth: `profile/cv-canonical.md` first, then the rendered CV through the adapter.
Update the canonical file before touching the design or document, so the differ and the
cover letters see the same facts.

## Steps

1. Read the chosen findings (from the audit table or the user's message). Restate them as a
   numbered edit list: location in CV, old text, new text. Get a yes on the list.
2. Edit `profile/cv-canonical.md` accordingly. Apply `profile/decisions.md` (aliases, owners,
   fixed wording, `omit` rows for the CV) and run `decisions_check.py <workspace>
   profile/cv-canonical.md`; a banned phrase blocks the edit list.
3. Apply through the adapter in `career.json` `cv.adapter`:
   - `canva`: `docs/adapters/canva.md` (transactional, one page per call, finalize is irreversible)
     Moving a PDF or DOCX CV into Canva for the first time: the adapter's "Starting a Canva CV
     from another format" section, run after `intake`.
   - `docx`: `docs/adapters/docx.md` (python-docx, keep runs and styles)
   - `markdown` / `html`: `docs/adapters/markdown-html.md` (edit source, render with Chrome or pandoc)
   - `google-docs`: `docs/adapters/google-docs.md`
   - `pdf-only`: nothing to edit; tell the user which lines to change in their editor.
4. Export to `cv.output` only after a yes. Verify:

```bash
pdfinfo out/cv.pdf | grep -E "Pages|Page size"      # page count did not grow
pdftotext -layout out/cv.pdf - | grep -nE "—|ﬁ|ﬂ|  " # em dashes, ligatures, double spaces
pdftoppm -png -r 60 out/cv.pdf out/cv-preview        # then Read the PNG(s) and check layout
```

5. Re-run `profile-audit` against the new `sources/cv.txt`; expect zero FACT rows for the applied items.

## Hard rules

- Never add text boxes or pages; edit existing text so the layout holds. A new section is a
  copied block (`docs/limits.md`, Canva states), never a fresh box.
- Never rebuild a Canva or DOCX master in another format to ship a change; the rebuild drifts.
  Edit the master, export, verify.
- Preserve the person's formatting (bold company names, dates alignment).
- No em dashes, no ligature characters in the source text, no invented numbers.
- Commit/finalize/export/overwrite: `draft` and `assisted` need an explicit yes in this
  conversation ("go ahead" for the edit list is not a yes for export). `auto` proceeds unless
  `approvals.cv_commit` is true. A backup copy of the design or document is made first in every mode.
