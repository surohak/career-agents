---
name: cv-tailor
description: Produce a per-application CV variant as a copy through the CV adapter: the summary rewritten toward the job, bullets reordered and reworded with the job's vocabulary from the job-match table, skills reordered, nothing invented, facts identical to cv-canonical. Use for apply-now jobs with a fit above 70 percent or when the user asks to tailor the CV.
disable-model-invocation: false
allowed-tools: "Read Write Bash(${CLAUDE_PLUGIN_ROOT}/scripts/*) Bash(python3 *) Bash(pdftotext *)"
---

# CV tailor

Inputs: `out/match-<company>-*.md` (run `job-match` first), `cv-canonical.md`, `voice.md`,
`constraints.md`, the adapter in `career.json`. Output: `out/cv-<company-slug>.pdf` and
`out/cv-<company-slug>.md` with the change list. The primary CV is never overwritten.

## Allowed changes

- Summary: 3 lines aimed at this role, using 3 to 5 exact terms from the JD that the CV already
  supports.
- Bullet order within each role: the most relevant first; at most 2 bullets reworded to use the
  JD's term for the same thing (say "observability" if they say it and you wrote "monitoring").
- Skills section: reorder, surface skills that are in the CV body but not the list; drop nothing.
- Title line: the target title only if the CV already shows equivalent scope; never inflate.
- Length: keep to the same page count.

## Forbidden

New numbers, new employers, new dates, new tools the person has not used, keyword stuffing,
hidden text, a different name or contact. Constraints item 4 still applies.

## Steps

1. Build the change list from the match table gaps marked "wording" (not "missing").
2. Apply via the adapter as a copy (Canva: duplicate the design first; DOCX: copy the file;
   Markdown: new file). See `docs/adapters/`.
3. Export, `pdftotext` the result, run `scripts/profile_diff.py --linkedin sources/cv.txt --cv out/cv-<slug>.txt --label Tailored`
   and confirm every difference is WORDING, none FACT.
4. Record the variant path on the pipeline row; `job-apply` uploads this file for that job.

Keep at most one variant per application; delete nothing (the person may want the history).
