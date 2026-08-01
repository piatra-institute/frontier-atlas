#!/usr/bin/env python3
"""Exact finite certificate that a cap in AG(7,3) has at most 291 points.

Premise: a(6) <= 112.  For a hypothetical 292-cap, intersect with the
three parallel affine hyperplanes in each of the 1093 hyperplane directions.
Each sorted intersection triple t=(a,b,c) has a+b+c=292 and 0<=c<=b<=a<=112.
The first three intersection moments are fixed by double counting.  The
integer slack/case calculation below proves no multiset of 1093 such triples
has those moments.

No floating-point arithmetic or solver is used.
"""
from __future__ import annotations

import json
from math import comb
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "upper291_certificate.json"

N = 7
M = 292
A6 = 112
DIRECTIONS = (3**N - 1) // 2          # 1093
PAIR_MULT = (3 ** (N - 1) - 1) // 2  # 364
TRIPLE_MULT = (3 ** (N - 2) - 1) // 2  # 121


def pair_moment(t: tuple[int, int, int]) -> int:
    return sum(comb(x, 2) for x in t)


def triple_moment(t: tuple[int, int, int]) -> int:
    return sum(comb(x, 3) for x in t)


def all_types() -> list[tuple[int, int, int]]:
    out: list[tuple[int, int, int]] = []
    for a in range(A6 + 1):
        for b in range(a + 1):
            c = M - a - b
            if 0 <= c <= b:
                out.append((a, b, c))
    return out


def nonnegative_partitions(total: int, values: list[int]) -> list[tuple[int, ...]]:
    solutions: list[tuple[int, ...]] = []

    def rec(i: int, rem: int, cur: list[int]) -> None:
        if i == len(values):
            if rem == 0:
                solutions.append(tuple(cur))
            return
        v = values[i]
        for k in range(rem // v + 1):
            cur.append(k)
            rec(i + 1, rem - k * v, cur)
            cur.pop()

    rec(0, total, [])
    return solutions


def main() -> None:
    types = all_types()
    assert len(types) == 184

    base = (98, 97, 97)
    endpoint = (112, 112, 68)
    p0, q0 = pair_moment(base), triple_moment(base)
    p1, q1 = pair_moment(endpoint), triple_moment(endpoint)

    # Primitive normal to the line through the two extremal moment points:
    # (q1-q0)/(p1-p0) = 3932/43.
    assert p1 - p0 == 645
    assert q1 - q0 == 58_980
    assert 3932 * (p1 - p0) == 43 * (q1 - q0)

    def slack(t: tuple[int, int, int]) -> int:
        return 43 * (triple_moment(t) - q0) - 3932 * (pair_moment(t) - p0)

    table = [
        {
            "type": list(t),
            "P": pair_moment(t),
            "Q": triple_moment(t),
            "dP": pair_moment(t) - p0,
            "slack": slack(t),
        }
        for t in types
    ]
    assert all(row["slack"] >= 0 for row in table)

    total_P = PAIR_MULT * comb(M, 2)
    total_Q = TRIPLE_MULT * comb(M, 3)
    total_slack = 43 * (total_Q - DIRECTIONS * q0) - 3932 * (
        total_P - DIRECTIONS * p0
    )
    assert total_P == 15_464_904
    assert total_Q == 496_944_580
    assert total_slack == 2328

    zero = [row for row in table if row["slack"] == 0]
    assert [row["type"] for row in zero] == [list(base), list(endpoint)]

    low = sorted(
        [row for row in table if 0 < row["slack"] <= total_slack],
        key=lambda row: row["slack"],
    )
    expected_low = [
        ((98, 98, 96), 1, 196),
        ((99, 97, 96), 2, 435),
        ((99, 98, 95), 4, 784),
        ((100, 96, 96), 5, 1152),
        ((100, 97, 95), 6, 1305),
        ((99, 99, 94), 8, 1482),
        ((100, 98, 94), 9, 1764),
    ]
    got_low = [(tuple(r["type"]), r["dP"], r["slack"]) for r in low]
    assert got_low == expected_low

    denominations = [row["slack"] for row in low]
    partitions = nonnegative_partitions(total_slack, denominations)
    expected_partitions = [
        (2, 0, 1, 1, 0, 0, 0),
        (3, 1, 0, 0, 1, 0, 0),
        (3, 4, 0, 0, 0, 0, 0),
        (6, 0, 0, 1, 0, 0, 0),
    ]
    assert partitions == expected_partitions

    target_dP = total_P - DIRECTIONS * p0
    endpoint_dP = p1 - p0
    cases = []
    for counts in partitions:
        positive_dP = sum(c * row["dP"] for c, row in zip(counts, low))
        residual = target_dP - positive_dP
        cases.append(
            {
                "positive_counts": list(counts),
                "positive_dP": positive_dP,
                "residual_dP_for_endpoint": residual,
                "endpoint_dP": endpoint_dP,
                "remainder": residual % endpoint_dP,
            }
        )
        assert positive_dP == 11
        assert residual == 91_848
        assert residual % endpoint_dP == 258 != 0

    CERT.parent.mkdir(parents=True, exist_ok=True)
    certificate = {
        "claim": "No 292-cap exists in AG(7,3); hence a(7) <= 291.",
        "premise": "a(6) <= 112",
        "parameters": {
            "n": N,
            "hypothetical_cap_size": M,
            "hyperplane_cap_max": A6,
            "directions": DIRECTIONS,
            "pair_multiplicity": PAIR_MULT,
            "triple_multiplicity": TRIPLE_MULT,
        },
        "moment_totals": {"sum_P": total_P, "sum_Q": total_Q},
        "base_type": list(base),
        "zero_slack_types": [row["type"] for row in zero],
        "slack_formula": "43*(Q-Q0)-3932*(P-P0)",
        "total_slack": total_slack,
        "low_positive_types": low,
        "slack_partitions": [list(x) for x in partitions],
        "divisibility_cases": cases,
        "number_of_admissible_types_checked": len(types),
        "all_admissible_types": table,
    }
    CERT.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print("PASS: exact hyperplane-distribution certificate")
    print(f"admissible sorted slice types checked: {len(types)}")
    print(f"aggregate slack: {total_slack}")
    print(f"positive-slack partitions checked: {len(partitions)}")
    print("each case leaves 91848 = 645*n_B, but 91848 mod 645 = 258")
    print("CONCLUSION (assuming a(6)<=112): a(7)<=291")
    print(CERT)


if __name__ == "__main__":
    main()
