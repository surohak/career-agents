#!/usr/bin/env bash
# Check that a career workspace is complete before any skill drafts from it.
#   scripts/verify_kernel.sh [workspace dir]
set -euo pipefail
ROOT="${1:-.}"
fail=0
[[ -f "$ROOT/career.json" ]] || { echo "MISSING career.json"; fail=1; }
for f in identity.md voice.md constraints.md positioning.md cv-canonical.md accepted.md; do
  [[ -f "$ROOT/profile/$f" ]] || { echo "MISSING profile/$f"; fail=1; }
done
[[ -f "$ROOT/profile/decisions.md" ]] || echo "warning: no profile/decisions.md (copy templates/profile/decisions.md); the decisions log is empty"
if [[ -f "$ROOT/career.json" ]]; then
  python3 - "$ROOT/career.json" <<'PY' || fail=1
import json, sys
d = json.load(open(sys.argv[1]))
for k in ("person", "cv", "target"):
    if k not in d: print(f"career.json: missing '{k}'"); sys.exit(1)
if not d["person"].get("name"): print("career.json: person.name is empty"); sys.exit(1)
if "search" not in d or not d.get("person", {}).get("timezone"):
    print("career.json: no 'search' block or person.timezone; job-scan will ask for them (not fatal)")
tr = d.get("target", {}).get("track", "ic")
if tr not in ("ic", "management", "early", "change"):
    print("career.json: target.track must be ic | management | early | change"); sys.exit(1)
sch = d.get("schedule", {})
if sch and sch.get("runner") not in ("scheduled-tasks", "cron", "launchd"):
    print("career.json: schedule.runner must be scheduled-tasks | cron | launchd"); sys.exit(1)
nt = d.get("notify", {})
if nt and nt.get("channel") not in ("slack", "telegram", "email", "file", "none"):
    print("career.json: notify.channel must be slack | telegram | email | file | none"); sys.exit(1)
a = d.get("automation", {})
if a.get("mode", "draft") not in ("draft", "assisted", "auto"):
    print("career.json: automation.mode must be draft | assisted | auto"); sys.exit(1)
if a.get("mode") in ("assisted", "auto") and a.get("browser", "none") == "none":
    print("career.json: automation.browser is none; LinkedIn profile edits and posts fall back to draft")
pp = d.get("site", {}).get("push_policy", "ask")
if pp not in ("ask", "direct"):
    print("career.json: site.push_policy must be ask | direct"); sys.exit(1)
if not isinstance(d.get("rules", {}).get("word_perfect", False), bool):
    print("career.json: rules.word_perfect must be true or false"); sys.exit(1)
if d["cv"].get("adapter") not in ("canva", "docx", "markdown", "html", "pdf-only", "google-docs"):
    print("career.json: cv.adapter must be canva | docx | markdown | html | google-docs | pdf-only"); sys.exit(1)
PY
fi
if [[ -f "$ROOT/profile/identity.md" ]] && grep -q "<[A-Z][A-Za-z ]*>" "$ROOT/profile/identity.md"; then
  echo "profile/identity.md still has <PLACEHOLDER> fields"; fail=1
fi
if [[ -f "$ROOT/profile/voice.md" ]] && grep -q $'—' "$ROOT/profile/voice.md"; then
  echo "profile/voice.md contains an em dash"; fail=1
fi
[[ -f "$ROOT/.gitignore" ]] && grep -q "sources/" "$ROOT/.gitignore" || echo "warning: no .gitignore excluding sources/ (LinkedIn dumps contain personal data)"
[[ $fail -eq 0 ]] && echo "kernel OK" || exit 1
