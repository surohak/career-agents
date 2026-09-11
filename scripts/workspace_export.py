#!/usr/bin/env python3
"""Export a workspace to a zip with an index, or delete it after a dry run."""
import argparse, os, sys, zipfile, shutil, datetime

DESC = {"profile": "the kernel: identity, voice, constraints, positioning, canonical CV",
        "sources": "fetched LinkedIn, CV text and site text (personal data)",
        "out": "everything the skills produced: audits, rebuild rounds, jobs, pipeline, briefs, logs",
        "history": "LinkedIn profile snapshots before and after automated edits"}

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("workspace"); ap.add_argument("--export"); ap.add_argument("--delete", action="store_true")
    ap.add_argument("--dry-run", action="store_true"); a = ap.parse_args()
    ws = os.path.abspath(a.workspace)
    if not os.path.exists(os.path.join(ws, "career.json")):
        print("refusing: no career.json in", ws); sys.exit(1)
    if a.export:
        lines = ["# Index", "", f"Exported {datetime.date.today()} from {ws}", ""]
        with zipfile.ZipFile(a.export, "w", zipfile.ZIP_DEFLATED) as z:
            for root, dirs, files in os.walk(ws):
                dirs[:] = [d for d in dirs if d not in (".git", "node_modules")]
                for f in files:
                    p = os.path.join(root, f); rel = os.path.relpath(p, ws)
                    z.write(p, rel); top = rel.split(os.sep)[0]
                    lines.append(f"- {rel} ({os.path.getsize(p)} B) : {DESC.get(top, 'workspace root')}")
            z.writestr("INDEX.md", "\n".join(lines) + "\n")
            z.writestr("WHAT-IS-WHERE.md", "Outside this zip: the LinkedIn MCP server's own session data on this machine; scheduled tasks (crontab -l, launchctl list, or Claude Code scheduled tasks); digests already sent to your notify channel; the CV inside its adapter tool (Canva, Docs, Word); the site repository; edits already applied to LinkedIn.\n")
        print(f"exported {len(lines)-4} files to {a.export}")
    if a.delete:
        targets = [ws]
        print("would remove:" if a.dry_run else "removing:")
        for t in targets: print("  ", t)
        print("then check by hand: crontab -l ; launchctl list | grep career ; your notify channel ; CV tool copies ; site repo ; LinkedIn edits (profile-history can restore before you delete)")
        if a.dry_run: return
        shutil.rmtree(ws); print("workspace removed")

if __name__ == "__main__":
    main()
