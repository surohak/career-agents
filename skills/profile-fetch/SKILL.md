---
name: profile-fetch
description: Fetch the three sources into sources/: LinkedIn profile dump (own or any public profile), CV text (PDF, DOCX, Canva or markdown) and personal website text. Use before an audit or whenever a source is older than 60 minutes.
disable-model-invocation: false
allowed-tools: "Bash(${CLAUDE_PLUGIN_ROOT}/scripts/*) Bash(pdftotext *) Bash(pdfinfo *) Bash(find *) Read"
---

# Profile fetch

All outputs go to `sources/` in the workspace. Reuse a file younger than 60 minutes unless the
user says "fresh". Report file name, size and age for each source.

## LinkedIn

Preferred (works even if this session cannot see the MCP tools):

```bash
${CLAUDE_PLUGIN_ROOT}/scripts/fetch_linkedin.sh --out sources/linkedin.md --max-age 60
# someone else's public profile:
${CLAUDE_PLUGIN_ROOT}/scripts/fetch_linkedin.sh --url https://www.linkedin.com/in/<handle>/ --out sources/linkedin-<handle>.md
```

If the MCP tools are visible in this session, call `get_my_profile` (or `get_person_profile`)
once with all sections and write the result verbatim with `=== section ===` headers to the same
file. Required sections: name, headline, location, about, experience, education, skills,
languages, projects, certifications. One call. Do not retry in a loop; if it times out, tell the
user to run the login command from `career-setup`.

## CV

By `career.json` `cv.adapter`:

- `pdf-only`, `markdown`, `html`, `docx` with a PDF export: `pdftotext -layout <pdf> sources/cv.txt`
- `docx` without PDF: `python3 -c "import docx"` and extract paragraphs, or ask the user to export a PDF
- `canva`: read the design with the Canva connector (`read-design`, text only) and write the text
  in reading order to `sources/cv.txt`. See `docs/adapters/canva.md`.
- `google-docs`: ask the user to export PDF, or use a Google Docs connector if attached.

Also record page count and fonts: `pdfinfo <pdf>`.

## Website

```bash
${CLAUDE_PLUGIN_ROOT}/scripts/site_text.py https://<site> --out sources/site.txt
```

If the script warns that there is very little text, the site is client-rendered. Options:
pass built HTML with `--files`, or, if `career.json` has `site.repo`, read the content source
files listed in `site.content_paths` directly and note that the audit runs against source, not
the live page.

## Privacy

`sources/` is personal data. It stays in the workspace, gitignored, never quoted at length in
chat beyond what the audit needs.
