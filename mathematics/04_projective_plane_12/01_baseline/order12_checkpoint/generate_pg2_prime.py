#!/usr/bin/env python3
"""Generate the Desarguesian plane PG(2,p) for a prime p as a JSON incidence matrix."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def is_prime(p: int) -> bool:
    if p < 2:
        return False
    d = 2
    while d * d <= p:
        if p % d == 0:
            return False
        d += 1
    return True


def normalize(x: tuple[int, int, int], p: int) -> tuple[int, int, int]:
    for a in x:
        if a % p:
            inv = pow(a, -1, p)
            return tuple((inv * y) % p for y in x)  # type: ignore[return-value]
    raise ValueError("zero vector")


def projective_vectors(p: int) -> list[tuple[int, int, int]]:
    values = {
        normalize((x, y, z), p)
        for x in range(p)
        for y in range(p)
        for z in range(p)
        if (x, y, z) != (0, 0, 0)
    }
    return sorted(values)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("p", type=int)
    ap.add_argument("output", type=Path)
    a = ap.parse_args()
    if not is_prime(a.p):
        raise SystemExit("This compact generator supports prime p only.")
    pts = projective_vectors(a.p)
    lines = projective_vectors(a.p)
    v = a.p * a.p + a.p + 1
    assert len(pts) == len(lines) == v
    matrix = [
        [int(sum(l[i] * x[i] for i in range(3)) % a.p == 0) for x in pts]
        for l in lines
    ]
    a.output.write_text(
        json.dumps({"order": a.p, "points": pts, "lines": lines, "matrix": matrix}, separators=(",", ":")),
        encoding="utf-8",
    )
    print(f"wrote PG(2,{a.p}) with {v} points/lines to {a.output}")


if __name__ == "__main__":
    main()
