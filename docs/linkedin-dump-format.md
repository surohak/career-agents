# LinkedIn dump format

`sources/linkedin.md` is what the differ, the audit and `verify-edits` read. `fetch_linkedin.sh`
and `profile-fetch` write it; when you assemble it from an MCP call or a browser read, follow
this layout exactly.

```
=== name ===
<full name>
=== headline ===
<headline, one line>
=== location ===
<city, country>
=== about ===
<about text, or the marker: (unreadable by MCP)>
=== experience ===
<Title>
<Company> · <Employment type>
<Mon YYYY> - <Mon YYYY or Present> · <N yrs N mos>
<Location> · <Remote|Hybrid|On-site>
<intro line, optional>
▸ <bullet>
▸ <bullet>
Stack: <comma list>

<next position, same shape, one blank line between positions>
=== education ===
<school, degree, years>
=== skills ===
<comma list, pinned first>
=== languages ===
<name (level), ...>
=== projects ===
<Project name>
<description>
<blank line between projects>
=== certifications ===
<name, issuer, date>
```

Rules the parser relies on:

- The title is the first non-blank line of a position; `Company · Type` is the next line
  with a middle dot; dates come as `Mon YYYY - Mon YYYY` (a `· duration` suffix is ignored).
- The simple shape `Title / Company / Mon YYYY - Mon YYYY / lines` (no middle dots, no
  durations) also parses; see `examples/alex-example/sources/linkedin.md`.
- Grouped positions at one company: `Company` / `N yrs N mos` / location, then each role as
  `Title` / `Employment type` / dates.
- Bullets start with `▸ ` or `- `. `Stack:` lines are kept but not diffed.
- Sections the MCP cannot read carry the marker `(unreadable by MCP)` on their own line.
  `linkedin_dump_check.py` reports them as unknown; nothing treats them as missing.

Validate before use:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/linkedin_dump_check.py sources/linkedin.md
```
