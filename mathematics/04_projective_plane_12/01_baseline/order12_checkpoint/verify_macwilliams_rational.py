#!/usr/bin/env python3
"""Exact checker for a rational MacWilliams-feasible dual weight distribution.

The certificate proves only feasibility of the rational linear-programming
relaxation. Actual code weight enumerators must be nonnegative integers.
"""
from __future__ import annotations

from fractions import Fraction
import json
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CERT = ROOT / "certificates" / "macwilliams_rational_feasible.json"
n = 157
M = 3**78
allowed = [0] + list(range(18, 157, 3))


def parse(value: str) -> Fraction:
    return Fraction(value)


def krawtchouk(i: int, j: int) -> int:
    lo = max(0, i - (n - j))
    hi = min(i, j)
    return sum(
        (-1) ** h * 2 ** (i - h) * comb(j, h) * comb(n - j, i - h)
        for h in range(lo, hi + 1)
    )


raw = json.loads(CERT.read_text(encoding="utf-8"))
A = {j: parse(raw[str(j)]) for j in allowed}
assert A[0] == 1
assert all(A[j] >= 0 for j in allowed)
assert sum(A.values()) == M
B: dict[int, Fraction] = {}
for i in range(n + 1):
    B[i] = sum(Fraction(krawtchouk(i, j)) * A[j] for j in allowed) / M
    if i % 3 == 0:
        assert B[i] == A.get(i, Fraction(0)), (i, B[i], A.get(i, 0))
    elif i % 3 == 2:
        assert B[i] == 0, (i, B[i])
    else:
        assert B[i] >= 0, (i, B[i])
assert all(B[i] == 0 for i in (1, 4, 7, 10))
assert B[13] == 314

print("PASS")
print("The exact rational MacWilliams relaxation is feasible.")
print("This rules out a claimed contradiction based only on those linear constraints.")
print("It does NOT prove that an integral weight enumerator or a code exists.")
