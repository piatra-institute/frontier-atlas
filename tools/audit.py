#!/usr/bin/env python3
"""Lightweight repository auditor. Keeps the doctrine from silently decaying.

Checks: discovery counts vs the counts asserted in the READMEs (drift), that every
dated run folder has a CLAIM.md and a SHA256SUMS, large tracked artifacts that should
be regenerate-only (ARTIFACTS.md), and how many prompts still carry a bare `(verify)`
open-status flag (not yet pinned to a fresh source). Exits nonzero on hard problems.

Run:  python3 tools/audit.py
"""
from __future__ import annotations
import re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LARGE_MB = 2.0
problems, notes = [], []

def rel(p): return str(p.relative_to(ROOT))

# 1. discovery inventory
disc = ROOT / "discovery"
pipes = sorted(d for d in (disc / "pipelines").glob("[0-9]*") if d.is_dir())
seed = 1 if (disc / "graph_conjectures" / "PROMPT.md").exists() else 0
hunts = list((disc / "hunts").rglob("PROMPT.md"))
total = len(list(disc.rglob("PROMPT.md")))
print(f"discovery: {len(pipes)} numbered pipelines + {seed} seed + {len(hunts)} hunts "
      f"= {total} PROMPT.md")

# 2. README count consistency (catch drift)
for f, want in [(ROOT/"README.md", total), (disc/"README.md", total)]:
    txt = f.read_text()
    for n in re.findall(r"\b(19[0-9]|20[0-9])\b", txt):
        if int(n) != want and int(n) not in (200,):   # 200 = legacy bank, allowed
            problems.append(f"{rel(f)} mentions count {n}, actual discovery total is {want}")

# 3. run-folder packaging contract
runs = [d for d in disc.rglob("*") if d.is_dir() and re.match(r"20\d\d-\d\d-\d\d", d.name)]
for d in runs:
    if not (d / "CLAIM.md").exists():
        problems.append(f"run without CLAIM.md: {rel(d)}")
    if not (d / "SHA256SUMS").exists():
        notes.append(f"run without SHA256SUMS: {rel(d)}")
print(f"dated run folders: {len(runs)}")

# 4. large tracked artifacts (regenerate-only policy)
try:
    tracked = subprocess.run(["git", "-C", str(ROOT), "ls-files"], capture_output=True,
                             text=True, timeout=30).stdout.split("\n")
except Exception:
    tracked = []
big = []
for rp in tracked:
    if not rp:
        continue
    p = ROOT / rp
    if p.exists() and p.stat().st_size > LARGE_MB * 1e6:
        big.append((rp, p.stat().st_size / 1e6))
for rp, mb in sorted(big, key=lambda x: -x[1]):
    notes.append(f"large tracked artifact {mb:.1f} MB (move to generated/ per ARTIFACTS.md): {rp}")

# 5. open-status freshness proxy: prompts with a bare (verify)
verify = sum(1 for p in disc.rglob("PROMPT.md") if "(verify)" in p.read_text())
print(f"prompts with a bare (verify) open-status flag (need pinning): {verify}/{total}")

# report
print()
if problems:
    print(f"PROBLEMS ({len(problems)}):")
    for x in problems: print("  x", x)
else:
    print("no hard problems.")
if notes:
    print(f"\nnotes ({len(notes)}):")
    for x in notes[:20]: print("  -", x)
    if len(notes) > 20: print(f"  ... and {len(notes)-20} more")
sys.exit(1 if problems else 0)

if __name__ == "__main__":
    pass
