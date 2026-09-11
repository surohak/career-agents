#!/usr/bin/env python3
"""Validate a LinkedIn dump before the differ or an audit trusts it.

  scripts/linkedin_dump_check.py sources/linkedin.md

Prints which `=== section ===` blocks exist, how many experience entries parse, and which
sections the MCP profile read could not see (marked `(unreadable by MCP)` or empty). Warns
when projects stop at exactly ten, which is the MCP read limit, not the real count.
Exit 1 only when the experience section is missing or parses to zero entries.
"""
import os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from profile_diff import sections, parse_jobs  # noqa: E402

REQUIRED = ("name", "headline", "location", "about", "experience", "education", "skills")
BLIND = ("about", "projects")


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    text = open(sys.argv[1], encoding="utf-8").read()
    sec = sections(text)
    fail = 0
    for name in REQUIRED + ("projects", "languages", "certifications"):
        key = next((k for k in sec if name in k), None)
        lines = sec.get(key) or [] if key else []
        body = "\n".join(lines).strip()
        if not key:
            state = "missing"
        elif not body or "unreadable by mcp" in body.lower() or "not captured" in body.lower():
            state = "unreadable by MCP" if name in BLIND else "empty"
        else:
            state = "ok"
        extra = ""
        if name == "experience" and state == "ok":
            n = len(parse_jobs(lines))
            extra = f", {n} entries"
            if n == 0:
                state = "unparseable (see docs/linkedin-dump-format.md)"; fail = 1
        if name == "projects" and state == "ok":
            n = len([l for l in body.splitlines() if l.strip() and not l.startswith(("▸", "-", " "))])
            if n == 10:
                extra = ", exactly 10 headings: the MCP read stops at ten, verify the rest in the browser"
        if name in REQUIRED and state == "missing":
            fail = 1
        print(f"{name:15s} {state}{extra}")
    if fail:
        print("dump not usable for the differ"); sys.exit(1)
    print("dump OK; treat 'unreadable by MCP' as unknown, never as missing")


if __name__ == "__main__":
    main()
