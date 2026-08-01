#!/usr/bin/env python3
"""Set-based independent coverage checker for a uniform covering array CSV."""
from __future__ import annotations

import argparse
import csv
import itertools
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("array", nargs="?", type=Path,
                        default=Path(__file__).resolve().parents[1] / "array_CA_13_2_8_3.csv")
    parser.add_argument("--strength", type=int, default=2)
    parser.add_argument("--alphabet", type=int, default=3)
    args = parser.parse_args()

    with args.array.open(newline="", encoding="utf-8") as handle:
        raw_rows = [row for row in csv.reader(handle) if row]
    if len(raw_rows) < 2:
        raise SystemExit("array CSV has no data rows")
    rows = [[int(x) for x in row] for row in raw_rows[1:]]
    if not rows or len({len(r) for r in rows}) != 1:
        raise SystemExit("malformed rectangular array")
    n, k, t, v = len(rows), len(rows[0]), args.strength, args.alphabet
    expected = set(itertools.product(range(v), repeat=t))
    checked = 0
    for cols in itertools.combinations(range(k), t):
        observed = {tuple(row[c] for c in cols) for row in rows}
        missing = expected - observed
        if missing:
            raise SystemExit(f"FAIL columns={cols} missing={sorted(missing)}")
        checked += 1
    print(f"coverage_checker=set-based-python")
    print(f"array=CA({n};{t},{k},{v})")
    print(f"column_subsets_checked={checked}")
    print(f"tuples_required_per_subset={v ** t}")
    print("result=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
