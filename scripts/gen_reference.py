#!/usr/bin/env python3
"""Generate docs/reference/*.md from skill and agent frontmatter. --check exits 1 if stale."""
import os, re, sys, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def fm(path):
    t = open(path, encoding="utf-8").read()
    m = re.match(r"---\n(.*?)\n---\n", t, re.S)
    d = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1); d[k.strip()] = v.strip().strip('"')
    return d

def build():
    skills = sorted(glob.glob(os.path.join(ROOT, "skills", "*", "SKILL.md")))
    agents = sorted(glob.glob(os.path.join(ROOT, "agents", "*.md")))
    out = ["---\ntitle: Skill reference\n---\n", "# Skill reference\n", f"{len(skills)} skills, {len(agents)} agents. Invoke a skill with `/career-agents:<name>`.\n",
           "| Skill | What it does |", "|-------|--------------|"]
    for s in skills:
        d = fm(s); out.append(f"| [`{d.get('name')}`](../../skills/{d.get('name')}/SKILL.md) | {d.get('description','')} |")
    out += ["", "## Agents", "", "| Agent | Role |", "|-------|------|"]
    for a in agents:
        d = fm(a); out.append(f"| `{d.get('name')}` | {d.get('description','')} |")
    return "\n".join(out) + "\n"

if __name__ == "__main__":
    target = os.path.join(ROOT, "docs", "reference", "skills.md")
    text = build()
    if "--check" in sys.argv:
        cur = open(target, encoding="utf-8").read() if os.path.exists(target) else ""
        if cur != text: print("docs/reference/skills.md is stale"); sys.exit(1)
        print("reference up to date"); sys.exit(0)
    os.makedirs(os.path.dirname(target), exist_ok=True)
    open(target, "w", encoding="utf-8").write(text); print(f"wrote {target}")
