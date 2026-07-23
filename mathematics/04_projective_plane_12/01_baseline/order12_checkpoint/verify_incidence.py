#!/usr/bin/env python3
"""Fast exact verifier for a finite-projective-plane incidence matrix.

Accepted input:
  * JSON: a list of rows, or {"matrix": [...]}.
  * CSV: one row per matrix row, comma-separated 0/1 entries.

The order is inferred from v = q^2 + q + 1 unless --order is supplied.
All checks use exact integer/bit operations.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
from typing import Any


def load_matrix(path: Path) -> list[list[int]]:
    if path.suffix.lower() == ".json":
        obj: Any = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(obj, dict):
            obj = obj.get("matrix")
        if not isinstance(obj, list):
            raise ValueError("JSON must contain a matrix list or {'matrix': list}.")
        return [[int(x) for x in row] for row in obj]
    with path.open(newline="", encoding="utf-8") as f:
        return [[int(x.strip()) for x in row] for row in csv.reader(f) if row]


def infer_order(v: int) -> int:
    disc = 4 * v - 3
    s = math.isqrt(disc)
    if s * s != disc or s % 2 == 0:
        raise ValueError(f"v={v} is not q^2+q+1 for an integer q")
    q = (s - 1) // 2
    if q * q + q + 1 != v:
        raise ValueError(f"v={v} is not q^2+q+1")
    return q


def verify(matrix: list[list[int]], claimed_order: int | None = None) -> tuple[int, int]:
    v = len(matrix)
    if v == 0 or any(len(row) != v for row in matrix):
        raise AssertionError("matrix must be nonempty and square")
    q = infer_order(v)
    if claimed_order is not None and q != claimed_order:
        raise AssertionError(f"inferred order {q}, expected {claimed_order}")
    k = q + 1

    for i, row in enumerate(matrix):
        bad = [x for x in row if x not in (0, 1)]
        if bad:
            raise AssertionError(f"row {i} has nonbinary entries")
        if sum(row) != k:
            raise AssertionError(f"row {i} sum is {sum(row)}, expected {k}")

    col_sums = [sum(matrix[i][j] for i in range(v)) for j in range(v)]
    for j, value in enumerate(col_sums):
        if value != k:
            raise AssertionError(f"column {j} sum is {value}, expected {k}")

    row_bits = []
    for row in matrix:
        bits = 0
        for j, x in enumerate(row):
            bits |= x << j
        row_bits.append(bits)

    for i in range(v):
        for j in range(i + 1, v):
            meet = (row_bits[i] & row_bits[j]).bit_count()
            if meet != 1:
                raise AssertionError(f"rows {i},{j} meet in {meet} columns, expected 1")

    col_bits = []
    for j in range(v):
        bits = 0
        for i in range(v):
            bits |= matrix[i][j] << i
        col_bits.append(bits)
    for i in range(v):
        for j in range(i + 1, v):
            meet = (col_bits[i] & col_bits[j]).bit_count()
            if meet != 1:
                raise AssertionError(f"columns {i},{j} meet in {meet} rows, expected 1")

    # These pairwise checks are exactly NN^T = qI+J and N^TN = qI+J.
    return q, v


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("matrix", type=Path)
    parser.add_argument("--order", type=int)
    args = parser.parse_args()

    raw = args.matrix.read_bytes()
    matrix = load_matrix(args.matrix)
    q, v = verify(matrix, args.order)
    print("PASS")
    print(f"order={q} points={v} lines={v} incidences_per_row={q+1}")
    print(f"sha256={hashlib.sha256(raw).hexdigest()}")
    print("verified: binary entries, row/column sums, all line-pair and point-pair intersections")


if __name__ == "__main__":
    main()
