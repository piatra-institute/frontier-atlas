#!/usr/bin/env python3
"""Slow, deliberately independent direct-loop incidence verifier."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from pathlib import Path


def read(path: Path) -> list[list[int]]:
    if path.suffix.lower() == ".json":
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            data = data["matrix"]
    else:
        with path.open(encoding="utf-8", newline="") as f:
            data = list(csv.reader(f))
    return [[int(y) for y in x] for x in data]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("matrix", type=Path)
    ap.add_argument("--order", type=int)
    a = ap.parse_args()
    N = read(a.matrix)
    v = len(N)
    assert v > 0 and all(len(r) == v for r in N), "not square"
    root = math.isqrt(4 * v - 3)
    assert root * root == 4 * v - 3 and root % 2 == 1, "invalid projective-plane size"
    q = (root - 1) // 2
    assert q * q + q + 1 == v
    if a.order is not None:
        assert q == a.order
    k = q + 1

    for i in range(v):
        for j in range(v):
            assert N[i][j] == 0 or N[i][j] == 1, (i, j, N[i][j])
    for i in range(v):
        assert sum(N[i][j] for j in range(v)) == k, ("row", i)
    for j in range(v):
        assert sum(N[i][j] for i in range(v)) == k, ("column", j)
    for r in range(v):
        for s in range(r + 1, v):
            assert sum(N[r][j] * N[s][j] for j in range(v)) == 1, ("line pair", r, s)
    for p in range(v):
        for t in range(p + 1, v):
            assert sum(N[i][p] * N[i][t] for i in range(v)) == 1, ("point pair", p, t)

    print("PASS (independent direct-loop verifier)")
    print(f"order={q} v={v}")
    print("sha256=" + hashlib.sha256(a.matrix.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
