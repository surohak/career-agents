# Running the flow for someone else

The flow is per person. Each person gets their own workspace; the plugin stays shared.

```
~/career/alex/    career.json profile/ sources/ out/
~/career/maria/   career.json profile/ sources/ out/
```

1. `scripts/new_workspace.sh ~/career/alex` then `career-setup` in that directory.
2. LinkedIn: the person's own profile needs their own login session for `get_my_profile`.
   Two options: they run `uvx mcp-server-linkedin@latest --login` on their machine and run the
   flow there, or you fetch their public profile with
   `scripts/fetch_linkedin.sh --url https://www.linkedin.com/in/<handle>/` from your session.
   Public profiles show less (no email, sometimes fewer sections), so ask them for a PDF export
   of their profile (LinkedIn: More > Save to PDF) and put its text in `sources/linkedin.md`
   with `=== section ===` headers if the fetch is thin.
3. CV: pick the adapter they actually use. Most people are `docx` or `pdf-only`.
4. Fill `profile/voice.md` with them, not for them. Read three of their old posts or emails and
   note the patterns. A wrong voice file produces copy they will not paste.
5. Constraints: ask what must never appear (clients under NDA, internal tools, phone).
6. Run stages 1 to 3, hand over `out/linkedin-rebuild-*.md`, let them paste, then re-audit.

Consent and privacy: only run this for someone who asked. Keep their workspace on your machine
out of any repo. Delete `sources/` when done if they want.
