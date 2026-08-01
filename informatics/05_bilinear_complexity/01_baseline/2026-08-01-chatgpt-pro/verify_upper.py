#!/usr/bin/env python3
"""Independent exact verifier for the rank-11 upper bound over F2."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Iterable


def dot2(a: Iterable[int], b: Iterable[int]) -> int:
    return sum(x * y for x, y in zip(a, b, strict=True)) & 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("decomposition", type=Path)
    args = ap.parse_args()

    raw = args.decomposition.read_bytes()
    data = json.loads(raw)
    assert data["field"] == "F2"
    assert data["map"] == "<2,2,3>"
    assert data["rank"] == 11
    terms = data["terms"]
    assert len(terms) == 11

    # Target tensor in coordinate order A=(i,j), B=(j,k), C=(i,k).
    target = [[[0 for _ in range(6)] for _ in range(6)] for _ in range(4)]
    for i in range(2):
        for j in range(2):
            for k in range(3):
                ai = 2 * i + j
                bi = 3 * j + k
                ci = 3 * i + k
                target[ai][bi][ci] = 1

    got = [[[0 for _ in range(6)] for _ in range(6)] for _ in range(4)]
    for term in terms:
        u, v, w = term["u"], term["v"], term["w"]
        assert len(u) == 4 and len(v) == 6 and len(w) == 6
        assert all(x in (0, 1) for x in u + v + w)
        assert any(u) and any(v) and any(w)
        for a in range(4):
            for b in range(6):
                if u[a] & v[b]:
                    for c in range(6):
                        got[a][b][c] ^= w[c]

    mismatches = []
    for a in range(4):
        for b in range(6):
            for c in range(6):
                if got[a][b][c] != target[a][b][c]:
                    mismatches.append((a, b, c, target[a][b][c], got[a][b][c]))
    assert not mismatches, f"tensor identity failed: {mismatches[:10]}"

    # Independent functional check on every A and B over F2: 16*64=1024 pairs.
    checked = 0
    for xa in range(1 << 4):
        x = [(xa >> q) & 1 for q in range(4)]
        for yb in range(1 << 6):
            y = [(yb >> q) & 1 for q in range(6)]
            out = [0] * 6
            for term in terms:
                p = dot2(term["u"], x) & dot2(term["v"], y)
                if p:
                    out = [z ^ w for z, w in zip(out, term["w"], strict=True)]
            expected = [0] * 6
            for i in range(2):
                for k in range(3):
                    expected[3 * i + k] = (
                        x[2 * i] * y[k] ^ x[2 * i + 1] * y[3 + k]
                    )
            assert out == expected, (x, y, out, expected)
            checked += 1

    print(f"UPPER OK: 11 terms; 144 tensor coefficients; {checked} input pairs")
    print(f"decomposition_sha256={hashlib.sha256(raw).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
