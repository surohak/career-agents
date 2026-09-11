#!/usr/bin/env bash
# Fetch a LinkedIn profile through the linkedin MCP server in a one-shot headless
# Claude session. Works even when the interactive session was started before the
# MCP server was added (an open session cannot load new MCP tools).
#
#   scripts/fetch_linkedin.sh                       # your own profile -> sources/linkedin.md
#   scripts/fetch_linkedin.sh --url https://www.linkedin.com/in/someone/ --out sources/linkedin-someone.md
#   scripts/fetch_linkedin.sh --out sources/linkedin.md --max-age 60   # reuse a dump younger than 60 min
#
# Requires: claude CLI, the `linkedin` MCP server (see skills/career-setup), a logged-in
# LinkedIn session (`uvx mcp-server-linkedin@latest --login`).
set -euo pipefail

OUT="sources/linkedin.md"; URL=""; MAX_AGE=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --url) URL="$2"; shift 2;;
    --out) OUT="$2"; shift 2;;
    --max-age) MAX_AGE="$2"; shift 2;;
    -h|--help) sed -n '2,12p' "$0"; exit 0;;
    *) echo "unknown arg: $1" >&2; exit 2;;
  esac
done

if [[ -n "$MAX_AGE" && -f "$OUT" ]]; then
  if [[ -n "$(find "$OUT" -mmin "-$MAX_AGE" 2>/dev/null)" ]]; then
    echo "reusing $OUT (younger than $MAX_AGE min)"; exit 0
  fi
fi

command -v claude >/dev/null || { echo "claude CLI not found" >&2; exit 1; }
claude mcp get linkedin >/dev/null 2>&1 || {
  echo "MCP server 'linkedin' is not configured. Run: claude mcp add --scope user linkedin -e UV_HTTP_TIMEOUT=300 -- uvx mcp-server-linkedin@latest" >&2; exit 1; }

mkdir -p "$(dirname "$OUT")"
SECTIONS="name, headline, location, about, experience, education, skills, languages, projects, certifications"
if [[ -z "$URL" ]]; then
  TOOL="mcp__linkedin__get_my_profile"
  PROMPT="Call $TOOL once with every section available ($SECTIONS). Return the text verbatim as markdown with one '=== section ===' header per section (for example === experience ===). Inside === experience === write each position as: title line, then 'Company · Employment type', then 'Mon YYYY - Mon YYYY', then location, then the description lines with bullets as '▸ '. Keep the wording exactly as returned. If a section is not in the tool output, write the section header followed by the single line '(unreadable by MCP)'. No commentary, no summary."
else
  TOOL="mcp__linkedin__get_person_profile"
  PROMPT="Call $TOOL once for the profile URL $URL with every section available ($SECTIONS). Return the text verbatim as markdown with one '=== section ===' header per section (for example === experience ===). Inside === experience === write each position as: title line, then 'Company · Employment type', then 'Mon YYYY - Mon YYYY', then location, then the description lines with bullets as '▸ '. Keep the wording exactly as returned. If a section is not in the tool output, write the section header followed by the single line '(unreadable by MCP)'. No commentary, no summary."
fi

TMP="$(mktemp)"
claude -p "$PROMPT" --allowedTools "$TOOL" --output-format text > "$TMP"
if ! grep -q '^=== experience ===' "$TMP"; then
  echo "fetch failed: no '=== experience ===' section. Output kept at $TMP" >&2
  echo "If the tool timed out, log in again: uvx mcp-server-linkedin@latest --login" >&2
  exit 1
fi
mv "$TMP" "$OUT"
echo "wrote $OUT ($(wc -l < "$OUT") lines)"
python3 "$(dirname "$0")/linkedin_dump_check.py" "$OUT" || true
