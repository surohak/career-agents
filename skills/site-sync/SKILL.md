---
name: site-sync
description: Audit and update a personal website so its facts, CV download, chatbot knowledge base and metadata match the canonical CV. Uses the read-only site-auditor agent first, then proposes a patch in the site repo. Commit and push only with an explicit yes.
disable-model-invocation: false
allowed-tools: "Read Write Edit Grep Glob Bash(git *) Bash(npm *) Bash(pnpm *) Bash(yarn *) Bash(python3 *) Bash(${CLAUDE_PLUGIN_ROOT}/scripts/*)"
---

# Site sync

Needs `career.json` `site.url` and, for edits, `site.repo` plus `site.content_paths`
(files that hold the copy: about page, case studies, experience data, chatbot knowledge base).

## 1. Audit (agent `site-auditor`, read-only)

Give it `sources/site.txt` (live) and the content source files, plus `cv-canonical.md`,
`constraints.md`, `identity.md`. It returns findings in these groups:

- Facts: titles, dates, numbers, stack that disagree with the CV.
- Forbidden phrases: "open to work", "available for hire", "looking for", em dashes.
- Privacy: phone number, home address, employer internals from `constraints.md` item 4.
- Assets: served CV PDF older than `out/cv.pdf` or missing, OG image and `<title>`/description
  not matching the headline, broken links to LinkedIn/GitHub.
- Chatbot knowledge base (if any): outdated roles or claims.

## 2. Patch

For each accepted finding edit the source file. Keep the site's own code style. If a script
like `update_resume.sh` exists in the repo for copying the PDF, use it instead of copying by hand.
Run the site's build (`npm run build` or equivalent) and report the result.

Run `decisions_check.py <workspace> <changed files>` on the patch; a banned phrase blocks the
commit. Show `git diff --stat` and the full diff of content files. Then by `site.push_policy`:
`ask` (default): `draft` and `assisted` ask commit? push? as two separate yeses; `auto` commits
and pushes to the current branch unless `approvals.site_push` is true. `direct`: one yes covers
commit and push to the branch named in `site.branch` (default: the current branch) in `draft`
and `assisted`, and `auto` pushes without asking. Never push to a branch the user did not name
or configure. Never `git remote add`. Never force-push.

## 3. Verify

After deploy (the user's job unless they ask), re-run `scripts/site_text.py` and the differ:

```bash
${CLAUDE_PLUGIN_ROOT}/scripts/site_text.py <url> --out sources/site.txt
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/profile_diff.py --linkedin sources/linkedin.md --cv sources/site.txt --label Site
```
