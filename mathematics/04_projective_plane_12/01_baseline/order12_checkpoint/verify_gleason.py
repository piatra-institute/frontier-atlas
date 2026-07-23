#!/usr/bin/env python3
"""Check that ordinary Type-III Gleason enumeration does not give a contradiction.

This constructs a FORMAL nonnegative Hamming weight enumerator satisfying the
forced low-weight coefficients. It does not construct a code.
"""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
out_path = ROOT / "outputs" / "gleason_formal_weight_enumerator.json"
t = sp.symbols("t")
f = 1 + 8 * t**3
g = t**3 * (1 - t**3) ** 3
basis = [sp.expand(f ** (40 - 3 * j) * g**j) for j in range(14)]
a = sp.symbols("a0:14")
W = sp.expand(sum(a[j] * basis[j] for j in range(14)))
conditions = {0: 1, 3: 2, 6: 0, 9: 0, 12: 0, 15: 942}
for weight in range(18, 40, 3):
    conditions[weight] = 0
solutions = sp.solve([sp.Eq(W.coeff(t, w), x) for w, x in conditions.items()], a, dict=True)
assert len(solutions) == 1
solution = solutions[0]
poly = sp.Poly(sp.expand(W.subs(solution)), t)
coeffs = {w: int(poly.coeff_monomial(t**w)) for w in range(161)}
assert all(x >= 0 for x in coeffs.values())
assert sum(coeffs.values()) == 3**80
assert coeffs[3] == 2 and coeffs[15] == 942
assert all(coeffs[w] == 0 for w in (6, 9, 12, 18, 21, 24, 27, 30, 33, 36, 39))
out_path.write_text(
    json.dumps(
        {
            "warning": "Formal Hamming weight enumerator only; not an existence certificate for a code.",
            "gleason_coefficients": [int(solution[x]) for x in a],
            "weight_distribution": {str(w): x for w, x in coeffs.items() if x},
        },
        indent=2,
    ),
    encoding="utf-8",
)
print("PASS")
print("A nonnegative integral formal Type-III Hamming weight enumerator exists.")
print("Therefore ordinary one-variable Gleason constraints alone do not obstruct the plane.")
print(f"wrote {out_path}")
