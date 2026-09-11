#!/usr/bin/env bash
# Runs every deterministic part of the plugin on the fictional example and diffs the outputs
# against examples/alex-example/expected/. Pass --update to refresh the expected files.
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"
EX="$HERE/examples/alex-example"; EXP="$EX/expected"; TMP="$(mktemp -d)"
UPDATE="${1:-}"
fail=0
bash "$HERE/scripts/verify_kernel.sh" "$EX" > "$TMP/verify.txt" 2>&1 || { echo "FAIL verify_kernel"; cat "$TMP/verify.txt"; fail=1; }
python3 "$HERE/scripts/profile_diff.py" --linkedin "$EX/sources/linkedin.md" --cv "$EX/sources/cv.txt" > "$TMP/diff.txt"
python3 "$HERE/scripts/profile_diff.py" --linkedin "$EX/sources/linkedin.md" --cv "$EX/sources/cv.txt" --json "$TMP/diff.json" > /dev/null
mkdir -p "$TMP/ws/out"; cp "$HERE/templates/metrics.md" "$HERE/templates/pipeline.md" "$HERE/templates/linkedin-log.md" "$TMP/ws/out/"
python3 "$HERE/scripts/dashboard.py" "$TMP/ws" --out "$TMP/dashboard.html" > /dev/null
grep -q "Career dashboard" "$TMP/dashboard.html" || { echo "FAIL dashboard"; fail=1; }
python3 "$HERE/scripts/gen_reference.py" --check > "$TMP/ref.txt" || { echo "FAIL reference (run scripts/gen_reference.py)"; cat "$TMP/ref.txt"; fail=1; }
for f in skills/*/SKILL.md; do n=$(basename "$(dirname "$f")"); grep -q "^name: $n$" "$HERE/$f" || { echo "FAIL frontmatter $f"; fail=1; }; done
python3 - "$HERE" <<'PY' || fail=1
import json,sys,os
r=sys.argv[1]
for p in ['.claude-plugin/plugin.json','.claude-plugin/marketplace.json','.mcp.json','templates/career.json','templates/cohort.json','examples/alex-example/career.json']:
    json.load(open(os.path.join(r,p)))
PY
if [[ "$UPDATE" == "--update" ]]; then mkdir -p "$EXP"; cp "$TMP/diff.txt" "$TMP/diff.json" "$EXP/"; echo "expected files updated"; fi
for f in diff.txt diff.json; do
  if ! diff -q "$EXP/$f" "$TMP/$f" > /dev/null; then echo "FAIL $f differs from expected:"; diff "$EXP/$f" "$TMP/$f" | head -20; fail=1; fi
done
# Optional local scan: put one regex per line of terms that must never appear in the repo
# (your own name, client names) in scripts/forbidden.local; the file is gitignored.
if [[ -f "$HERE/scripts/forbidden.local" ]]; then
  if grep -rqiE -f "$HERE/scripts/forbidden.local" --exclude-dir=.git --exclude=forbidden.local "$HERE"; then echo "FAIL forbidden term found (see scripts/forbidden.local)"; fail=1; fi
fi
rm -rf "$TMP"
[[ $fail -eq 0 ]] && echo "smoke OK" || { echo "smoke FAILED"; exit 1; }
