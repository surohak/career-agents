---
name: github-review
description: Recruiter-view audit of the GitHub profile: pinned repositories, README quality, activity pattern, profile README and bio consistency with the kernel, stale forks, secrets or personal data in public repos, with a scored report and the fixes. Use when the CV or site links to GitHub or the target role is hands-on.
disable-model-invocation: false
allowed-tools: "Read Write Bash(gh *) Bash(git *) Bash(python3 *) Bash(curl *)"
---

# GitHub review

Inputs: the GitHub URL from `identity.md`, `positioning.md`, `cv-canonical.md`, `gh` logged in
(read only). Output: `out/github-review-<date>.md`, score 0 to 100.

## Checks

1. **Profile**: name, bio (matches the headline's role), location, link to the site, the
   profile README present and consistent with `identity.md` (`multi-platform` writes it).
2. **Pinned (6)**: each has a README with what it is, how to run it, a screenshot or output,
   and the stack; commits in the last 12 months; no forks unless meaningfully changed; at least
   one repo per pinned skill in `positioning.md`. List what to pin and unpin.
3. **Activity**: `gh api users/<u>/events` for the pattern (bursty, steady, dead); private
   contribution display on or off; suggest the setting change but do not change it.
4. **Hygiene**: repos with default names, empty READMEs, node_modules committed, `.env` or
   keys in history (`gh api` search for common patterns in the user's own repos; report, never
   commit fixes to history without a yes), personal data (phone, home address) in READMEs.
5. **Consistency**: employer names in repo descriptions vs constraints item 4; project names in
   the CV that have no public repo (say "private" in the CV or remove the implication).

## Fixes

Ranked list with the exact edit; README rewrites drafted in `voice.md`; profile README through
`multi-platform`. Changes to repos are made only with the repo path and a yes per repo
(`approvals.site_push` gates the push). Never delete a repository.
