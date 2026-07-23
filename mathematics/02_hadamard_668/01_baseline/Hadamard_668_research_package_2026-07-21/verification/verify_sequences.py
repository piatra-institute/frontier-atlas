#!/usr/bin/env python3
"""Strict exact verifier for four length-167 GS sequences.

This verifies the sequence certificate directly.  An exact order-668
Goethals-Seidel construction requires every nonzero combined periodic
autocorrelation to vanish.
"""
from __future__ import annotations
import argparse
import csv
import json
from pathlib import Path

N = 167
R = 4

def read_sequences(path: Path) -> list[list[int]]:
    with path.open("r", newline="") as f:
        rows = list(csv.reader(f))
    if len(rows) != R:
        raise ValueError(f"expected {R} rows, found {len(rows)}")
    out: list[list[int]] = []
    for r, row in enumerate(rows):
        if len(row) != N:
            raise ValueError(f"row {r}: expected {N} entries, found {len(row)}")
        vals: list[int] = []
        for i, token in enumerate(row):
            if token.strip() not in {"-1", "1", "+1"}:
                raise ValueError(f"row {r}, column {i}: invalid token {token!r}")
            vals.append(int(token))
        out.append(vals)
    return out

def combined_paf(x: list[list[int]]) -> list[int]:
    return [
        sum(x[r][i] * x[r][(i + t) % N] for r in range(R) for i in range(N))
        for t in range(1, N)
    ]

def metrics(x: list[list[int]]) -> dict:
    c = combined_paf(x)
    unique = c[: (N - 1) // 2]
    full_score = sum(v * v for v in c)
    d = [v // 4 for v in unique]
    if any(v % 4 for v in unique):
        raise AssertionError("combined PAF is not divisible by 4")
    return {
        "shape": [R, N],
        "row_sums": [sum(row) for row in x],
        "combined_paf_all_shifts": c,
        "combined_paf_unique_shifts": unique,
        "full_score": full_score,
        "unique_score": sum(v * v for v in unique),
        "d_square": sum(v * v for v in d),
        "l1_d": sum(abs(v) for v in d),
        "max_abs_paf": max(abs(v) for v in c),
        "nonzero_unique": sum(v != 0 for v in unique),
        "exact_complementary_quad": all(v == 0 for v in c),
        "implied_order": 4 * N,
    }

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("csv", type=Path)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--require-exact", action="store_true")
    args = ap.parse_args()
    x = read_sequences(args.csv)
    m = metrics(x)
    if args.json:
        print(json.dumps(m, indent=2))
    else:
        print(f"shape={tuple(m['shape'])}")
        print(f"row_sums={m['row_sums']}")
        print(f"full_score={m['full_score']}")
        print(f"d_square={m['d_square']}")
        print(f"max_abs_paf={m['max_abs_paf']}")
        print(f"nonzero_unique={m['nonzero_unique']}")
        print(f"exact_complementary_quad={str(m['exact_complementary_quad']).lower()}")
    return 0 if (m["exact_complementary_quad"] or not args.require_exact) else 1

if __name__ == "__main__":
    raise SystemExit(main())
