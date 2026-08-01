#!/usr/bin/env python3
"""Generate the Calderbank-Fishburn 236-cap in F_3^7.

Construction follows Edel--Bierbrauer, Large caps in small spaces, Table 2:
  (0,D), (0,R), (1,Dbar), (1,R), (2,U)
where D is the 2-(6,3,2) design listed in the paper, Dbar its complementary
set of 3-subsets, R the full-support vectors with an even number of 2s,
and U the weight-one vectors.
"""
from __future__ import annotations

import csv
import json
from itertools import combinations, product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

D_BLOCKS = {
    (0, 1, 2), (1, 2, 5),
    (0, 1, 3), (1, 3, 4),
    (0, 2, 4), (1, 4, 5),
    (0, 3, 5), (2, 3, 4),
    (0, 4, 5), (2, 3, 5),
}
ALL_BLOCKS = set(combinations(range(6), 3))
DBAR_BLOCKS = ALL_BLOCKS - D_BLOCKS


def support_vectors(blocks: set[tuple[int, int, int]]) -> set[tuple[int, ...]]:
    out: set[tuple[int, ...]] = set()
    for block in blocks:
        for vals in product((1, 2), repeat=3):
            v = [0] * 6
            for idx, val in zip(block, vals):
                v[idx] = val
            out.add(tuple(v))
    return out


def build() -> list[tuple[int, ...]]:
    D = support_vectors(D_BLOCKS)
    Dbar = support_vectors(DBAR_BLOCKS)
    R = {
        tuple(v)
        for v in product((1, 2), repeat=6)
        if sum(x == 2 for x in v) % 2 == 0
    }
    U = {
        tuple(2 if i == pos and val == 2 else 1 if i == pos else 0 for i in range(6))
        for pos in range(6)
        for val in (1, 2)
    }

    assert len(D) == 80
    assert len(Dbar) == 80
    assert len(R) == 32
    assert len(U) == 12

    cap = (
        {(0,) + v for v in D | R}
        | {(1,) + v for v in Dbar | R}
        | {(2,) + v for v in U}
    )
    assert len(cap) == 236
    return sorted(cap)


def main() -> None:
    cap = build()
    json_path = ROOT / "cf236.json"
    csv_path = ROOT / "cf236.csv"
    txt_path = ROOT / "cf236.txt"

    json_path.write_text(json.dumps(cap, separators=(",", ":")) + "\n", encoding="utf-8")
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([f"x{i}" for i in range(7)])
        writer.writerows(cap)
    txt_path.write_text("\n".join("".join(map(str, p)) for p in cap) + "\n", encoding="ascii")
    print(f"generated {len(cap)} points")
    print(json_path)
    print(csv_path)
    print(txt_path)


if __name__ == "__main__":
    main()
