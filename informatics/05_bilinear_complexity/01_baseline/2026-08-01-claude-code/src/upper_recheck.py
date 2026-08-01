#!/usr/bin/env python3
"""Independent re-derivation of the upper bound R_F2(<2,2,3>) <= 11.

Self-contained: hardcodes the 11 products from the chatgpt-pro package's
ALGORITHM.md and checks, over F2, that they compute the full 2x2-by-2x3 product
for all 2^10 = 1024 input pairs. This is our own second implementation, not a
replay of their verifier.
"""
from __future__ import annotations
import itertools, json, sys
from pathlib import Path

def true_mul(A, B):                          # A 2x2, B 2x3 -> C 2x3, over F2
    return [[(A[i][0] * B[0][k] + A[i][1] * B[1][k]) % 2 for k in range(3)]
            for i in range(2)]

def algo(a, b, c, d, e, f, g, h, i, j):      # the 11-product F2 algorithm
    m = lambda x, y: (x * y) % 2
    p1 = m((a + d) % 2, (e + i) % 2); p2 = m((c + d) % 2, e); p3 = m(a, (f + i) % 2)
    p4 = m(d, (h + e) % 2); p5 = m((a + b) % 2, i); p6 = m((c + a) % 2, (e + f) % 2)
    p7 = m((b + d) % 2, (h + i) % 2); p8 = m(a, g); p9 = m(b, j)
    p10 = m(c, g); p11 = m(d, j)
    return [[(p1 + p4 + p5 + p7) % 2, (p3 + p5) % 2, (p8 + p9) % 2],
            [(p2 + p4) % 2, (p1 + p2 + p3 + p6) % 2, (p10 + p11) % 2]]

def main():
    bad = 0
    for bits in itertools.product([0, 1], repeat=10):
        a, b, c, d, e, f, g, h, i, j = bits
        C = algo(*bits)
        if C != true_mul([[a, b], [c, d]], [[e, f, g], [h, i, j]]):
            bad += 1
    ok = (bad == 0)
    print(f"upper: checked 1024 input pairs, mismatches={bad} -> "
          f"{'R_F2(<2,2,3>) <= 11 CONFIRMED (independent)' if ok else 'INVALID'}")
    outdir = Path(__file__).resolve().parents[1] / "certificates"
    outdir.mkdir(exist_ok=True)
    (outdir / "upper_recheck.json").write_text(json.dumps(
        dict(map="<2,2,3>", field="F2", products=11, inputs_checked=1024,
             mismatches=bad, upper_bound_confirmed=ok), indent=2))
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
