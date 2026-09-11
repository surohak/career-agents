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
if [[ -f "$ROOT/career.json" ]]; then
  python3 - "$ROOT/career.json" <<'PY' || fail=1
import json, sys
d = json.load(open(sys.argv[1]))
for k in ("person", "cv", "target"):
    if k not in d: print(f"career.json: missing '{k}'"); sys.exit(1)
if not d["person"].get("name"): print("career.json: person.name is empty"); sys.exit(1)
if "search" not in d or not d.get("person", {}).get("timezone"):
    print("career.json: no 'search' block or person.timezone; job-scan will ask for them (not fatal)")
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
