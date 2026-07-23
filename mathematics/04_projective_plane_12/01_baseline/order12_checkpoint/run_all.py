#!/usr/bin/env python3
from __future__ import annotations

import platform
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs"
EX = ROOT / "examples"
OUT.mkdir(exist_ok=True)
EX.mkdir(exist_ok=True)


def run(name: str, args: list[str]) -> None:
    print(f"== {name} ==")
    completed = subprocess.run([sys.executable, *args], cwd=ROOT, check=True, text=True, capture_output=True)
    text = completed.stdout
    print(text, end="")
    (OUT / f"{name}.txt").write_text(text, encoding="utf-8")


(OUT / "environment.txt").write_text(
    f"python={sys.version}\nplatform={platform.platform()}\n",
    encoding="utf-8",
)
for p in (3, 5):
    target = EX / f"PG2_{p}.json"
    run(f"generate_pg2_{p}", ["generate_pg2_prime.py", str(p), str(target)])
    run(f"verify_pg2_{p}_fast", ["verify_incidence.py", str(target), "--order", str(p)])
    run(f"verify_pg2_{p}_independent", ["verify_incidence_independent.py", str(target), "--order", str(p)])
run("algebra", ["verify_algebra.py"])
run("line_distribution", ["line_distribution.py"])
run("gleason", ["verify_gleason.py"])
run("macwilliams_rational", ["verify_macwilliams_rational.py"])
print("ALL CHECKS PASSED")
