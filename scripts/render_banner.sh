#!/usr/bin/env bash
# Render an HTML banner to a LinkedIn cover PNG (1584x396 at 2x = 3168x792).
#   scripts/render_banner.sh out/banner.html out/banner.png
set -euo pipefail
IN="${1:?html file}"; OUT="${2:?png file}"
W="${BANNER_W:-1584}"; H="${BANNER_H:-396}"
for c in "${CHROME_BIN:-}" \
         "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
         "/Applications/Chromium.app/Contents/MacOS/Chromium" \
         "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge" \
         "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser" \
         google-chrome chromium chromium-browser microsoft-edge brave-browser; do
  [[ -n "${c:-}" ]] || continue
  if [[ -x "$c" ]] || command -v "$c" >/dev/null 2>&1; then CHROME="$c"; break; fi
done
[[ -n "${CHROME:-}" ]] || { echo "No Chromium-based browser found. Set CHROME_BIN=/path/to/chrome" >&2; exit 1; }
IN_ABS="$(cd "$(dirname "$IN")" && pwd)/$(basename "$IN")"
mkdir -p "$(dirname "$OUT")"
"$CHROME" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=2 \
  --window-size="$W,$H" --virtual-time-budget=8000 \
  --screenshot="$OUT" "file://$IN_ABS" >/dev/null 2>&1
echo "wrote $OUT ($(( W * 2 ))x$(( H * 2 )))"
