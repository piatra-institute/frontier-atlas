#!/usr/bin/env python3
"""Independent exact verifier for lrc_grid_obstruction_certificate.json.

This file intentionally does not import lrc_exact.py.  It independently
recomputes every finite numerical claim in the JSON certificate with Python's
Fraction arithmetic, including the complete critical-time maximum.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import gcd
from pathlib import Path
from typing import Sequence


def parse_fraction(text: str) -> Fraction:
    return Fraction(text)


def norm(x: Fraction) -> Fraction:
    residue = x.numerator % x.denominator
    return Fraction(min(residue, x.denominator - residue), x.denominator)


def minimum(speeds: Sequence[int], t: Fraction) -> Fraction:
    return min(norm(Fraction(abs(v), 1) * t) for v in speeds)


def exact_maximum(speeds: Sequence[int]) -> tuple[Fraction, tuple[Fraction, ...]]:
    values = sorted(set(abs(v) for v in speeds))
    candidates: set[Fraction] = set()
    for index, a in enumerate(values):
        for b in values[index:]:
            denominator = a + b
            candidates.update(Fraction(n, denominator) for n in range(denominator))

    best = max(minimum(speeds, t) for t in candidates)
    witnesses = tuple(sorted(t for t in candidates if minimum(speeds, t) == best))
    return best, witnesses


def grid_witnesses(speeds: Sequence[int], d: int) -> tuple[Fraction, ...]:
    alpha = Fraction(1, len(speeds) + 1)
    return tuple(
        Fraction(a, d)
        for a in range(d)
        if minimum(speeds, Fraction(a, d)) >= alpha
    )


def verify_record(record: dict) -> str:
    speeds = tuple(int(v) for v in record["speeds"])
    k = int(record["k_relative_speeds"])
    d = int(record["grid_denominator"])
    alpha = Fraction(1, k + 1)
    t = parse_fraction(record["strict_witness"])

    assert len(speeds) == k
    assert record["total_runners"] == k + 1
    assert parse_fraction(record["threshold"]) == alpha
    assert len(set(speeds)) == len(speeds) == k
    assert all(v > 0 for v in speeds)
    assert gcd(*speeds) == int(record["gcd_of_speeds"]) == 1
    assert record["all_speeds_distinct"] is True
    assert record["all_speeds_coprime_to_grid_denominator"] == all(
        gcd(v, d) == 1 for v in speeds
    )

    distances = tuple(norm(Fraction(v, 1) * t) for v in speeds)
    stated_distances = tuple(parse_fraction(x) for x in record["distances_at_strict_witness"])
    assert distances == stated_distances
    assert min(distances) == parse_fraction(record["minimum_distance_at_strict_witness"])
    assert min(distances) > alpha
    assert record["strict_witness_verified"] is True

    grid = grid_witnesses(speeds, d)
    assert len(grid) == int(record["grid_witness_count"]) == 0
    assert list(record["grid_witnesses"]) == []
    assert record["no_grid_witness_verified"] is True

    maximum, maximizing_times = exact_maximum(speeds)
    assert maximum == parse_fraction(record["exact_maximum_loneliness"])
    assert maximizing_times == tuple(parse_fraction(x) for x in record["exact_maximizing_times"])

    bound = Fraction(k * (k + 1) * (k - 1), 2)
    assert bound == parse_fraction(record["sufficient_last_speed_bound"])
    assert speeds[-1] == int(record["last_speed"])
    assert (speeds[-1] > bound) == bool(record["bound_condition_holds"])

    kind = record["kind"]
    if kind == "diagonal":
        assert speeds == tuple(range(1, k)) + (d,)
        # Independent symbolic check: the last coordinate vanishes at a/d.
        assert all(norm(Fraction(d * a, d)) == 0 for a in range(d))
    elif kind == "congruence":
        assert speeds == tuple(range(1, k)) + (d + k,)
        assert gcd(d, k + 1) == 1
        assert all((speeds[i] - (i + 1)) % d == 0 for i in range(k))
    else:
        raise AssertionError(f"unknown certificate kind: {kind}")

    return (
        f"verified {kind}: k={k}, d={d}, "
        f"grid witnesses=0, exact maximum={maximum}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args()

    data = json.loads(args.certificate.read_text(encoding="utf-8"))
    assert data["schema"] == "piatra-institute/lrc-grid-obstruction-certificate/v1"
    assert data["arithmetic"] == "exact rational arithmetic; no floating point"
    examples = data["examples"]
    assert len(examples) == 2
    for record in examples:
        print(verify_record(record))
    print("independent certificate verification: PASS")


if __name__ == "__main__":
    main()
