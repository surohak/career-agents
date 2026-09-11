#!/usr/bin/env bash
# Create a private career workspace from the plugin templates.
#   scripts/new_workspace.sh ~/career
set -euo pipefail
DEST="${1:?destination dir}"
HERE="$(cd "$(dirname "$0")/.." && pwd)"
mkdir -p "$DEST"/{profile,sources,out}
for f in "$HERE"/templates/profile/*.md; do
  [[ -e "$DEST/profile/$(basename "$f")" ]] || cp "$f" "$DEST/profile/"
done
[[ -e "$DEST/career.json" ]] || cp "$HERE/templates/career.json" "$DEST/career.json"
[[ -e "$DEST/.gitignore" ]] || cat > "$DEST/.gitignore" <<'GI'
# LinkedIn dumps, CV text and rendered outputs contain personal data.
sources/
out/
*.pdf
GI
echo "workspace ready at $DEST"
echo "next: fill profile/identity.md, profile/constraints.md and career.json, then run scripts/verify_kernel.sh $DEST"
