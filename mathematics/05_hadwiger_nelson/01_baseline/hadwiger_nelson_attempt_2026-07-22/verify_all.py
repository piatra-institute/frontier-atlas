#!/usr/bin/env python3
"""Exact verifier for the certified partial Hadwiger-Nelson result.

This script verifies, without floating-point geometry, that:
  1. the 510 coordinate expressions are distinct elements of
     Q(sqrt(3), sqrt(5), sqrt(11));
  2. the supplied edge list is exactly the set of coordinate pairs at
     Euclidean distance 1;
  3. the stated distance-phi and distance-1/phi pairs are exact;
  4. every row in colorings_84.csv is a proper coloring with colors 0..4;
  5. for every nonedge {u,v}, some supplied coloring has c(u)=c(v), and
     another supplied coloring has c(u)!=c(v).
"""

from __future__ import annotations

import csv
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Sequence, Tuple

import sympy as sp
from sympy.parsing.mathematica import parse_mathematica

ROOT = Path(__file__).resolve().parent
N_EXPECTED = 510
M_EXPECTED = 2504

# Basis mask convention:
# bit 0 -> sqrt(3), bit 1 -> sqrt(5), bit 2 -> sqrt(11).
# Thus the eight coefficients represent
# 1, sqrt(3), sqrt(5), sqrt(15), sqrt(11), sqrt(33), sqrt(55), sqrt(165).
FieldElement = Tuple[Fraction, Fraction, Fraction, Fraction,
                     Fraction, Fraction, Fraction, Fraction]
ZERO: FieldElement = tuple(Fraction(0) for _ in range(8))  # type: ignore[assignment]
ONE: FieldElement = (Fraction(1),) + tuple(Fraction(0) for _ in range(7))  # type: ignore[assignment]
PHI_SQUARED: FieldElement = (
    Fraction(3, 2), Fraction(0), Fraction(1, 2), Fraction(0),
    Fraction(0), Fraction(0), Fraction(0), Fraction(0),
)
INV_PHI_SQUARED: FieldElement = (
    Fraction(3, 2), Fraction(0), Fraction(-1, 2), Fraction(0),
    Fraction(0), Fraction(0), Fraction(0), Fraction(0),
)


def add(a: FieldElement, b: FieldElement) -> FieldElement:
    return tuple(x + y for x, y in zip(a, b))  # type: ignore[return-value]


def sub(a: FieldElement, b: FieldElement) -> FieldElement:
    return tuple(x - y for x, y in zip(a, b))  # type: ignore[return-value]


def mul(a: FieldElement, b: FieldElement) -> FieldElement:
    out = [Fraction(0) for _ in range(8)]
    for i, ai in enumerate(a):
        if ai == 0:
            continue
        for j, bj in enumerate(b):
            if bj == 0:
                continue
            common = i & j
            rational_factor = 1
            if common & 1:
                rational_factor *= 3
            if common & 2:
                rational_factor *= 5
            if common & 4:
                rational_factor *= 11
            out[i ^ j] += ai * bj * rational_factor
    return tuple(out)  # type: ignore[return-value]


def squared_distance(
    p: Tuple[FieldElement, FieldElement],
    q: Tuple[FieldElement, FieldElement],
) -> FieldElement:
    dx = sub(p[0], q[0])
    dy = sub(p[1], q[1])
    return add(mul(dx, dx), mul(dy, dy))


_s3, _s5, _s11 = sp.symbols("s3 s5 s11")
_RADICAL_SUBSTITUTIONS = {
    sp.sqrt(3): _s3,
    sp.sqrt(5): _s5,
    sp.sqrt(11): _s11,
    sp.sqrt(15): _s3 * _s5,
    sp.sqrt(33): _s3 * _s11,
    sp.sqrt(55): _s5 * _s11,
    sp.sqrt(165): _s3 * _s5 * _s11,
}


def sympy_to_field(expr: sp.Expr) -> FieldElement:
    """Convert one coordinate expression to the fixed 8-element basis."""
    normalized = sp.expand(sp.radsimp(sp.sqrtdenest(expr)))
    symbolic = sp.expand(
        normalized.subs(_RADICAL_SUBSTITUTIONS, simultaneous=True)
    )
    poly = sp.Poly(symbolic, _s3, _s5, _s11, domain=sp.QQ)
    out = [Fraction(0) for _ in range(8)]
    for monomial, coefficient in poly.terms():
        if any(exponent not in (0, 1) for exponent in monomial):
            raise AssertionError(
                f"Expression escaped the multiquadratic basis: {expr!s}"
            )
        mask = monomial[0] | (monomial[1] << 1) | (monomial[2] << 2)
        out[mask] += Fraction(int(coefficient.p), int(coefficient.q))
    return tuple(out)  # type: ignore[return-value]


def load_coordinates(path: Path) -> list[Tuple[FieldElement, FieldElement]]:
    coordinates: list[Tuple[FieldElement, FieldElement]] = []
    for line_number, line in enumerate(path.read_text().splitlines(), start=1):
        if not line.strip():
            continue
        parsed = parse_mathematica(line)
        if not isinstance(parsed, sp.Tuple) or len(parsed) != 2:
            raise AssertionError(f"Malformed vertex line {line_number}: {line}")
        coordinates.append(
            (sympy_to_field(parsed[0]), sympy_to_field(parsed[1]))
        )
    if len(coordinates) != N_EXPECTED:
        raise AssertionError(
            f"Expected {N_EXPECTED} vertices, found {len(coordinates)}"
        )
    if len(set(coordinates)) != len(coordinates):
        raise AssertionError("Two coordinate expressions denote the same point")
    return coordinates


def load_edges(path: Path) -> set[Tuple[int, int]]:
    declared_n = declared_m = None
    edges: set[Tuple[int, int]] = set()
    for line_number, line in enumerate(path.read_text().splitlines(), start=1):
        fields = line.split()
        if not fields:
            continue
        if fields[0] == "p":
            if len(fields) != 4 or fields[1] != "edge":
                raise AssertionError(f"Malformed problem line {line_number}: {line}")
            declared_n, declared_m = int(fields[2]), int(fields[3])
        elif fields[0] == "e":
            if len(fields) != 3:
                raise AssertionError(f"Malformed edge line {line_number}: {line}")
            u, v = int(fields[1]) - 1, int(fields[2]) - 1
            if not (0 <= u < N_EXPECTED and 0 <= v < N_EXPECTED):
                raise AssertionError(f"Out-of-range edge on line {line_number}")
            if u == v:
                raise AssertionError(f"Loop on line {line_number}")
            edge = (u, v) if u < v else (v, u)
            if edge in edges:
                raise AssertionError(f"Duplicate edge on line {line_number}")
            edges.add(edge)
        else:
            raise AssertionError(f"Unknown line type on line {line_number}: {line}")
    if declared_n != N_EXPECTED or declared_m != M_EXPECTED:
        raise AssertionError(
            f"Header says n={declared_n}, m={declared_m}; "
            f"expected n={N_EXPECTED}, m={M_EXPECTED}"
        )
    if len(edges) != M_EXPECTED:
        raise AssertionError(f"Expected {M_EXPECTED} edges, found {len(edges)}")
    return edges


def load_colorings(path: Path) -> list[Tuple[int, ...]]:
    with path.open(newline="") as handle:
        reader = csv.reader(handle)
        header = next(reader)
        expected_header = ["coloring_id"] + [f"v{i}" for i in range(1, N_EXPECTED + 1)]
        if header != expected_header:
            raise AssertionError("Unexpected coloring-certificate header")
        rows: list[Tuple[int, ...]] = []
        for expected_id, fields in enumerate(reader, start=1):
            if len(fields) != N_EXPECTED + 1:
                raise AssertionError(
                    f"Coloring row {expected_id} has {len(fields)-1} colors"
                )
            if int(fields[0]) != expected_id:
                raise AssertionError(f"Nonsequential coloring id in row {expected_id}")
            coloring = tuple(int(value) for value in fields[1:])
            if any(color < 0 or color > 4 for color in coloring):
                raise AssertionError(f"Color outside 0..4 in row {expected_id}")
            rows.append(coloring)
    if len(rows) != 84:
        raise AssertionError(f"Expected 84 certificate rows, found {len(rows)}")
    return rows


def verify() -> None:
    coordinates = load_coordinates(ROOT / "data" / "510.vtx")
    listed_edges = load_edges(ROOT / "data" / "510.edge")

    exact_unit_pairs: set[Tuple[int, int]] = set()
    exact_phi_pairs: set[Tuple[int, int]] = set()
    exact_inv_phi_pairs: set[Tuple[int, int]] = set()

    for u in range(N_EXPECTED):
        for v in range(u + 1, N_EXPECTED):
            distance_squared = squared_distance(coordinates[u], coordinates[v])
            if distance_squared == ZERO:
                raise AssertionError(f"Coincident vertices {u+1} and {v+1}")
            if distance_squared == ONE:
                exact_unit_pairs.add((u, v))
            if distance_squared == PHI_SQUARED:
                exact_phi_pairs.add((u, v))
            if distance_squared == INV_PHI_SQUARED:
                exact_inv_phi_pairs.add((u, v))

    if exact_unit_pairs != listed_edges:
        missing = sorted(exact_unit_pairs - listed_edges)[:10]
        spurious = sorted(listed_edges - exact_unit_pairs)[:10]
        raise AssertionError(
            "Edge file does not equal the exact unit-distance graph; "
            f"missing listed edges for {missing}, spurious listed edges {spurious}"
        )

    expected_phi = {(211, 489), (217, 490), (223, 488)}
    expected_inv_phi = {(211, 490), (217, 488), (223, 489)}
    if exact_phi_pairs != expected_phi:
        raise AssertionError(
            f"Unexpected exact phi pairs: {sorted((u+1,v+1) for u,v in exact_phi_pairs)}"
        )
    if exact_inv_phi_pairs != expected_inv_phi:
        raise AssertionError(
            "Unexpected exact inverse-phi pairs: "
            f"{sorted((u+1,v+1) for u,v in exact_inv_phi_pairs)}"
        )

    colorings = load_colorings(ROOT / "certificates" / "colorings_84.csv")
    for row_id, coloring in enumerate(colorings, start=1):
        for u, v in listed_edges:
            if coloring[u] == coloring[v]:
                raise AssertionError(
                    f"Coloring {row_id} is monochromatic on edge {(u+1, v+1)}"
                )

    nonedge_count = 0
    for u in range(N_EXPECTED):
        for v in range(u + 1, N_EXPECTED):
            if (u, v) in listed_edges:
                continue
            nonedge_count += 1
            equality_values = [coloring[u] == coloring[v] for coloring in colorings]
            if not any(equality_values):
                raise AssertionError(
                    f"No same-color witness for nonedge {(u+1, v+1)}"
                )
            if all(equality_values):
                raise AssertionError(
                    f"No different-color witness for nonedge {(u+1, v+1)}"
                )

    expected_nonedges = N_EXPECTED * (N_EXPECTED - 1) // 2 - M_EXPECTED
    if nonedge_count != expected_nonedges:
        raise AssertionError(
            f"Expected {expected_nonedges} nonedges, checked {nonedge_count}"
        )

    print("VERIFIED")
    print(f"  vertices: {N_EXPECTED}; exact unit pairs/edges: {len(exact_unit_pairs)}")
    print(
        "  exact phi pairs: "
        f"{sorted((u + 1, v + 1) for u, v in exact_phi_pairs)}"
    )
    print(
        "  exact 1/phi pairs: "
        f"{sorted((u + 1, v + 1) for u, v in exact_inv_phi_pairs)}"
    )
    print(f"  certificate colorings: {len(colorings)}")
    print(
        "  conclusion: every one of the "
        f"{nonedge_count} nonedges is same-colored in at least one proper "
        "5-coloring and differently colored in at least one other."
    )


if __name__ == "__main__":
    verify()
