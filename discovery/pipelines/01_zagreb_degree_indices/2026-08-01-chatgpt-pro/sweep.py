#!/usr/bin/env python3
"""Exact sweep of degree-based graph-index inequalities.

The census input is the canonical graph6 catalogue of connected unlabeled graphs
on 2..9 vertices from Brendan McKay's nauty data collection, plus K1 as '@'.
Every graph is decoded and indexed twice:
  1. a manual graph6/bitset implementation;
  2. NetworkX's independent graph6 reader and graph routines.

All inequality comparisons use integer cross-products or fractions.Fraction.
"""
from __future__ import annotations

import argparse
import csv
import itertools
import json
import math
import time
from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Callable, Iterable, Iterator

import networkx as nx

INDEX_FIELDS = ("M1", "M2", "F", "HM", "irr", "sigma")
COUNT_REFERENCE = {1: 1, 2: 1, 3: 2, 4: 6, 5: 21, 6: 112, 7: 853, 8: 11117, 9: 261080}
TREE_REFERENCE = {1: 1, 2: 1, 3: 1, 4: 2, 5: 3, 6: 6, 7: 11, 8: 23, 9: 47}


def decode_graph6_primary(g6: str) -> tuple[int, list[int], list[tuple[int, int]]]:
    """Independent graph6 decoder for n <= 62, returning bitset adjacency."""
    s = g6.strip()
    if not s:
        raise ValueError("empty graph6 line")
    values = [ord(c) - 63 for c in s]
    if not (0 <= values[0] <= 62):
        raise NotImplementedError("this sweep's primary decoder supports n <= 62")
    n = values[0]
    bits: list[int] = []
    for value in values[1:]:
        if not (0 <= value <= 63):
            raise ValueError(f"invalid graph6 character in {g6!r}")
        bits.extend((value >> shift) & 1 for shift in (5, 4, 3, 2, 1, 0))
    needed = n * (n - 1) // 2
    if len(bits) < needed:
        raise ValueError(f"truncated graph6 string {g6!r}")

    adjacency = [0] * n
    edges: list[tuple[int, int]] = []
    k = 0
    for j in range(1, n):
        for i in range(j):
            if bits[k]:
                adjacency[i] |= 1 << j
                adjacency[j] |= 1 << i
                edges.append((i, j))
            k += 1
    return n, adjacency, edges


def indices_primary(g6: str) -> dict[str, object]:
    n, adjacency, edges = decode_graph6_primary(g6)
    degrees = [mask.bit_count() for mask in adjacency]
    m = len(edges)
    M1 = sum(d * d for d in degrees)
    F = sum(d * d * d for d in degrees)
    M2 = HM = irr = sigma = 0
    M1_edge = F_edge = 0
    for u, v in edges:
        du, dv = degrees[u], degrees[v]
        M2 += du * dv
        HM += (du + dv) ** 2
        diff = du - dv
        irr += abs(diff)
        sigma += diff * diff
        M1_edge += du + dv
        F_edge += du * du + dv * dv

    # Internal exact identities, deliberately redundant.
    assert sum(degrees) == 2 * m
    assert M1 == M1_edge
    assert F == F_edge
    assert HM == F + 2 * M2
    assert sigma == F - 2 * M2

    Delta = max(degrees, default=0)
    delta = min(degrees, default=0)
    return {
        "n": n,
        "m": m,
        "degrees": tuple(degrees),
        "degree_sequence": tuple(sorted(degrees, reverse=True)),
        "Delta": Delta,
        "delta": delta,
        "M1": M1,
        "M2": M2,
        "F": F,
        "HM": HM,
        "irr": irr,
        "sigma": sigma,
        "tree": m == n - 1,
        "chemical": Delta <= 4,
        "regular": Delta == delta,
        "cyclomatic": m - n + 1,
    }


def indices_secondary(g6: str) -> dict[str, object]:
    """Independent verifier using NetworkX's parser and graph object."""
    G = nx.from_graph6_bytes(g6.encode("ascii"))
    degree_map = dict(G.degree())
    n = G.number_of_nodes()
    m = G.number_of_edges()
    degrees = tuple(degree_map[i] for i in range(n))
    M1 = sum(d * d for d in degree_map.values())
    F = sum(d * d * d for d in degree_map.values())
    M2 = HM = irr = sigma = 0
    for u, v in G.edges():
        du, dv = degree_map[u], degree_map[v]
        M2 += du * dv
        HM += (du + dv) ** 2
        irr += abs(du - dv)
        sigma += (du - dv) ** 2
    Delta = max(degree_map.values(), default=0)
    delta = min(degree_map.values(), default=0)
    return {
        "n": n,
        "m": m,
        "degrees": degrees,
        "degree_sequence": tuple(sorted(degrees, reverse=True)),
        "Delta": Delta,
        "delta": delta,
        "M1": M1,
        "M2": M2,
        "F": F,
        "HM": HM,
        "irr": irr,
        "sigma": sigma,
        "tree": nx.is_tree(G),
        "chemical": Delta <= 4,
        "regular": Delta == delta,
        "cyclomatic": m - n + 1,
    }


def verified_indices(g6: str) -> dict[str, object]:
    a = indices_primary(g6)
    b = indices_secondary(g6)
    if a != b:
        raise AssertionError(f"independent index mismatch for {g6}:\nprimary={a}\nsecondary={b}")
    return a


def graph6_from_graph(G: nx.Graph) -> str:
    # Build a fresh graph so graph6 vertex labels agree with sorted input labels.
    nodes = sorted(G.nodes())
    mapping = {node: i for i, node in enumerate(nodes)}
    H = nx.Graph()
    H.add_nodes_from(range(len(nodes)))
    H.add_edges_from((mapping[u], mapping[v]) for u, v in G.edges())
    return nx.to_graph6_bytes(H, header=False).decode("ascii").strip()


def iter_census(data_dir: Path, max_n: int = 9) -> Iterator[tuple[int, str]]:
    if max_n < 1 or max_n > 9:
        raise ValueError("bundled exact census supports 1 <= max_n <= 9")
    yield 1, "@"
    for n in range(2, max_n + 1):
        path = data_dir / f"graph{n}c.g6"
        if not path.exists():
            raise FileNotFoundError(f"missing nauty catalogue: {path}")
        with path.open("r", encoding="ascii") as handle:
            for line in handle:
                g6 = line.strip()
                if g6:
                    yield n, g6


def scope_all(r: dict[str, object]) -> bool:
    return int(r["m"]) > 0


def scope_tree(r: dict[str, object]) -> bool:
    return int(r["m"]) > 0 and bool(r["tree"])


def scope_chemical(r: dict[str, object]) -> bool:
    return int(r["m"]) > 0 and bool(r["chemical"])


def scope_unicyclic(r: dict[str, object]) -> bool:
    return int(r["m"]) > 0 and int(r["cyclomatic"]) == 1


def scope_nonregular(r: dict[str, object]) -> bool:
    return int(r["m"]) > 0 and not bool(r["regular"])


@dataclass(frozen=True)
class Bound:
    id: str
    inequality: str
    scope_name: str
    source: str
    scope: Callable[[dict[str, object]], bool]
    check: Callable[[dict[str, object]], bool]
    status_note: str = "verified against literature"


def literature_bounds() -> list[Bound]:
    return [
        Bound(
            "HV_general",
            "M1/n <= M2/m  [m*M1 <= n*M2]",
            "connected graphs, n>=2",
            "Hansen and Vukicevic, Comparing the Zagreb Indices, Croat. Chem. Acta 80 (2007), Conjecture 1 (disproved in the same paper)",
            scope_all,
            lambda r: int(r["m"]) * int(r["M1"]) <= int(r["n"]) * int(r["M2"]),
            "published conjecture, known false in general",
        ),
        Bound(
            "HV_trees",
            "M1/n <= M2/m",
            "trees, n>=2",
            "Vukicevic and Graovac, Comparing Zagreb M1 and M2 indices for acyclic molecules, MATCH 57 (2007) 587-590",
            scope_tree,
            lambda r: int(r["m"]) * int(r["M1"]) <= int(r["n"]) * int(r["M2"]),
        ),
        Bound(
            "HV_chemical",
            "M1/n <= M2/m",
            "chemical graphs (Delta<=4), n>=2",
            "Hansen and Vukicevic, Comparing the Zagreb Indices, Croat. Chem. Acta 80 (2007), Theorem 1",
            scope_chemical,
            lambda r: int(r["m"]) * int(r["M1"]) <= int(r["n"]) * int(r["M2"]),
        ),
        Bound(
            "HV_unicyclic",
            "M1/n <= M2/m",
            "connected unicyclic graphs",
            "Liu, On a conjecture about comparing Zagreb indices (2008), as catalogued in the 2011 Zagreb-comparison survey",
            scope_unicyclic,
            lambda r: int(r["m"]) * int(r["M1"]) <= int(r["n"]) * int(r["M2"]),
            "source statement verified via survey",
        ),
        Bound(
            "FG_lower_1",
            "F >= M1^2/(2m)  [2mF >= M1^2]",
            "connected graphs, n>=2",
            "Furtula and Gutman, A forgotten topological index, J. Math. Chem. 53 (2015), quoted in Che and Chen (2016)",
            scope_all,
            lambda r: 2 * int(r["m"]) * int(r["F"]) >= int(r["M1"]) ** 2,
        ),
        Bound(
            "FG_lower_2",
            "F >= M1^2/m - 2M2  [mF >= M1^2 - 2mM2]",
            "connected graphs, n>=2",
            "Furtula and Gutman (2015), quoted in Che and Chen (2016)",
            scope_all,
            lambda r: int(r["m"]) * int(r["F"]) >= int(r["M1"]) ** 2 - 2 * int(r["m"]) * int(r["M2"]),
        ),
        Bound(
            "FG_upper_corrected",
            "F <= 2M2 + m(n-2)^2",
            "connected graphs, n>=2",
            "Furtula and Gutman (2015), corrected form documented by Che and Chen (2016)",
            scope_all,
            lambda r: int(r["F"]) <= 2 * int(r["M2"]) + int(r["m"]) * (int(r["n"]) - 2) ** 2,
            "corrected missing-square typo",
        ),
        Bound(
            "FG_upper_literal_printed",
            "F <= 2M2 + m(n-2)",
            "connected graphs, n>=2",
            "literal printed form in Furtula and Gutman (2015); Che and Chen (2016) identify the missing square as a typo",
            scope_all,
            lambda r: int(r["F"]) <= 2 * int(r["M2"]) + int(r["m"]) * (int(r["n"]) - 2),
            "known typographical error, tested literally",
        ),
        Bound(
            "CheChen_lower_irr_M2",
            "F >= irr^2/m + 2M2  [mF >= irr^2 + 2mM2]",
            "connected graphs, n>=2",
            "Che and Chen, Lower and Upper Bounds of the Forgotten Topological Index, MATCH 76 (2016), Proposition 3.1",
            scope_all,
            lambda r: int(r["m"]) * int(r["F"]) >= int(r["irr"]) ** 2 + 2 * int(r["m"]) * int(r["M2"]),
        ),
        Bound(
            "CheChen_lower_irr_M1",
            "F >= (irr^2 + M1^2)/(2m)  [2mF >= irr^2 + M1^2]",
            "connected graphs, n>=2",
            "Che and Chen (2016), Proposition 3.3",
            scope_all,
            lambda r: 2 * int(r["m"]) * int(r["F"]) >= int(r["irr"]) ** 2 + int(r["M1"]) ** 2,
        ),
        Bound(
            "CheChen_upper_Delta_delta",
            "F <= (Delta+delta)M1 + (Delta-delta)irr/2 - 2mDelta*delta",
            "connected graphs, n>=2",
            "Che and Chen (2016), Proposition 4.2",
            scope_all,
            lambda r: 2 * int(r["F"]) <= 2 * (int(r["Delta"]) + int(r["delta"])) * int(r["M1"]) + (int(r["Delta"]) - int(r["delta"])) * int(r["irr"]) - 4 * int(r["m"]) * int(r["Delta"]) * int(r["delta"]),
        ),
        Bound(
            "M1_upper_Delta_delta",
            "M1 <= 2m(Delta+delta) - nDelta*delta",
            "connected graphs, n>=2",
            "Das bound, restated as Proposition 4.3 in Che and Chen (2016)",
            scope_all,
            lambda r: int(r["M1"]) <= 2 * int(r["m"]) * (int(r["Delta"]) + int(r["delta"])) - int(r["n"]) * int(r["Delta"]) * int(r["delta"]),
        ),
        Bound(
            "M1_common_lower",
            "M1 >= 4m^2/n  [nM1 >= 4m^2]",
            "connected graphs, n>=2",
            "Ilic and Stevanovic, On Comparing Zagreb Indices, MATCH 62 (2009), Theorem 2.1",
            scope_all,
            lambda r: int(r["n"]) * int(r["M1"]) >= 4 * int(r["m"]) ** 2,
        ),
        Bound(
            "M2_common_lower",
            "M2 >= 4m^3/n^2  [n^2 M2 >= 4m^3]",
            "connected graphs, n>=2",
            "Ilic and Stevanovic (2009), Theorem 2.2",
            scope_all,
            lambda r: int(r["n"]) ** 2 * int(r["M2"]) >= 4 * int(r["m"]) ** 3,
        ),
        Bound(
            "M2_common_upper",
            "M2/m <= Delta*M1/(2m)  [2M2 <= Delta*M1]",
            "connected graphs, n>=2",
            "Ilic and Stevanovic (2009), common upper bound",
            scope_all,
            lambda r: 2 * int(r["M2"]) <= int(r["Delta"]) * int(r["M1"]),
        ),
    ]


def witness_payload(g6: str, r: dict[str, object], family: str = "census", params: str = "") -> dict[str, object]:
    return {
        "graph6": g6,
        "family": family,
        "parameters": params,
        "n": r["n"],
        "m": r["m"],
        "degree_sequence": list(r["degree_sequence"]),
        "Delta": r["Delta"],
        "delta": r["delta"],
        "M1": r["M1"],
        "M2": r["M2"],
        "F": r["F"],
        "HM": r["HM"],
        "irr": r["irr"],
        "sigma": r["sigma"],
        "tree": r["tree"],
        "chemical": r["chemical"],
        "cyclomatic": r["cyclomatic"],
    }


def feature_value(r: dict[str, object], feature: str) -> Fraction:
    if feature in INDEX_FIELDS:
        return Fraction(int(r[feature]), 1)
    if feature == "M1/n":
        return Fraction(int(r["M1"]), int(r["n"]))
    if feature == "M2/m":
        return Fraction(int(r["M2"]), int(r["m"]))
    raise KeyError(feature)


FEATURES = ("M1", "M2", "F", "HM", "irr", "sigma", "M1/n", "M2/m")
ZERO_CAPABLE = {"irr", "sigma"}


def oriented_ratio_pair(a: str, b: str) -> tuple[str, str, str]:
    """Choose a denominator that is positive on the broadest natural domain."""
    if a in ZERO_CAPABLE and b not in ZERO_CAPABLE:
        return a, b, "all connected graphs with n>=2"
    if b in ZERO_CAPABLE and a not in ZERO_CAPABLE:
        return b, a, "all connected graphs with n>=2"
    if {a, b} == {"irr", "sigma"}:
        return "irr", "sigma", "connected nonregular graphs"
    return a, b, "all connected graphs with n>=2"


def build_ratio_candidates(training: list[tuple[str, dict[str, object]]]) -> list[dict[str, object]]:
    candidates: list[dict[str, object]] = []
    for a, b in itertools.combinations(FEATURES, 2):
        numerator, denominator, domain = oriented_ratio_pair(a, b)
        values: list[tuple[Fraction, str]] = []
        for g6, r in training:
            den = feature_value(r, denominator)
            if den == 0:
                continue
            values.append((feature_value(r, numerator) / den, g6))
        if not values:
            continue
        lower_value, lower_g6 = min(values, key=lambda item: (item[0], item[1]))
        upper_value, upper_g6 = max(values, key=lambda item: (item[0], item[1]))
        for side, coefficient, extremizer in (
            ("lower", lower_value, lower_g6),
            ("upper", upper_value, upper_g6),
        ):
            candidates.append({
                "id": f"{numerator}_over_{denominator}_{side}".replace("/", "_per_"),
                "numerator": numerator,
                "denominator": denominator,
                "side": side,
                "coefficient": coefficient,
                "domain": domain,
                "training_graphs": len(values),
                "training_extremizer_graph6": extremizer,
                "census_tested": 0,
                "census_broken": 0,
                "census_first_witness": None,
                "adversarial_tested": 0,
                "adversarial_broken": 0,
                "adversarial_first_witness": None,
            })
    return candidates


def test_ratio_candidates(candidates: list[dict[str, object]], g6: str, r: dict[str, object], phase: str, family: str = "census", params: str = "") -> None:
    for c in candidates:
        den = feature_value(r, str(c["denominator"]))
        if den == 0:
            continue
        ratio = feature_value(r, str(c["numerator"])) / den
        coefficient = c["coefficient"]
        assert isinstance(coefficient, Fraction)
        ok = ratio >= coefficient if c["side"] == "lower" else ratio <= coefficient
        c[f"{phase}_tested"] = int(c[f"{phase}_tested"]) + 1
        if not ok:
            c[f"{phase}_broken"] = int(c[f"{phase}_broken"]) + 1
            key = f"{phase}_first_witness"
            if c[key] is None:
                payload = witness_payload(g6, r, family, params)
                payload["observed_ratio"] = fraction_string(ratio)
                payload["coefficient"] = fraction_string(coefficient)
                c[key] = payload


def fraction_string(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def make_complete_bipartite(a: int, b: int) -> nx.Graph:
    return nx.complete_bipartite_graph(a, b)


def make_double_star(a: int, b: int) -> nx.Graph:
    G = nx.Graph()
    G.add_edge(0, 1)
    next_vertex = 2
    for _ in range(a):
        G.add_edge(0, next_vertex)
        next_vertex += 1
    for _ in range(b):
        G.add_edge(1, next_vertex)
        next_vertex += 1
    return G


def make_broom(handle_vertices: int, extra_leaves: int) -> nx.Graph:
    G = nx.path_graph(handle_vertices)
    next_vertex = handle_vertices
    for _ in range(extra_leaves):
        G.add_edge(0, next_vertex)
        next_vertex += 1
    return G


def make_kite(clique_order: int, tail_vertices: int) -> nx.Graph:
    G = nx.complete_graph(clique_order)
    previous = 0
    for vertex in range(clique_order, clique_order + tail_vertices):
        G.add_edge(previous, vertex)
        previous = vertex
    return G


def make_turan(order: int, parts: int) -> nx.Graph:
    q, rem = divmod(order, parts)
    sizes = [q + (1 if i < rem else 0) for i in range(parts)]
    return nx.complete_multipartite_graph(*sizes)


def make_general_barbell(left_order: int, right_order: int, internal_path_vertices: int) -> nx.Graph:
    G = nx.Graph()
    left = list(range(left_order))
    right_start = left_order + internal_path_vertices
    right = list(range(right_start, right_start + right_order))
    G.add_edges_from(itertools.combinations(left, 2))
    G.add_edges_from(itertools.combinations(right, 2))
    previous = left[-1]
    for vertex in range(left_order, right_start):
        G.add_edge(previous, vertex)
        previous = vertex
    G.add_edge(previous, right[0])
    return G


def make_subdivided_star(arms: int, arm_length: int) -> nx.Graph:
    G = nx.Graph()
    next_vertex = 1
    for _ in range(arms):
        previous = 0
        for _ in range(arm_length):
            G.add_edge(previous, next_vertex)
            previous = next_vertex
            next_vertex += 1
    return G


def make_dense_pendant(clique_order: int, leaves: int) -> nx.Graph:
    G = nx.complete_graph(clique_order)
    for vertex in range(clique_order, clique_order + leaves):
        G.add_edge(0, vertex)
    return G


def make_hv_family(nu: int, p: int) -> nx.Graph:
    """K_{2,nu+1} plus S_{p+1}, joined at one star leaf to the size-2 side."""
    G = nx.Graph()
    left = [0, 1]
    right = list(range(2, nu + 3))
    for u in left:
        for v in right:
            G.add_edge(u, v)
    center = nu + 3
    leaves = list(range(center + 1, center + 1 + p))
    for leaf in leaves:
        G.add_edge(center, leaf)
    G.add_edge(leaves[0], left[0])
    return G


def make_triangle_chain_star(a: int, b: int) -> nx.Graph:
    """A concrete C(a,b): S_{a+1} with a chain of b edge-sharing triangles at one leaf.

    The star has center 0 and selected leaf 1. Each new triangle shares one vertex
    with the previous triangle and contributes two new vertices; this implementation
    is included only as an adversarial construction, not as a claimed canonical
    reconstruction of every paper's drawing convention.
    """
    G = nx.Graph()
    for leaf in range(1, a + 1):
        G.add_edge(0, leaf)
    anchor = 1
    next_vertex = a + 1
    for _ in range(b):
        x, y = next_vertex, next_vertex + 1
        next_vertex += 2
        G.add_edges_from(((anchor, x), (x, y), (y, anchor)))
        anchor = y
    return G


def adversarial_instances(max_n: int = 60) -> Iterator[tuple[str, str, nx.Graph]]:
    # Explicit stars, even though they overlap K_{1,b}, retain family provenance.
    for n in range(2, max_n + 1):
        yield "star", f"n={n}", nx.star_graph(n - 1)

    for a in range(1, max_n):
        for b in range(a, max_n - a + 1):
            if a + b <= max_n:
                yield "complete_bipartite", f"a={a};b={b}", make_complete_bipartite(a, b)

    for a in range(1, max_n):
        for b in range(a, max_n):
            if a + b + 2 <= max_n:
                yield "double_star", f"a={a};b={b}", make_double_star(a, b)

    for handle in range(2, min(20, max_n - 1) + 1):
        for leaves in range(1, max_n - handle + 1):
            yield "broom", f"handle={handle};leaves={leaves}", make_broom(handle, leaves)

    for clique in range(3, min(20, max_n - 1) + 1):
        for tail in range(1, max_n - clique + 1):
            yield "kite", f"clique={clique};tail={tail}", make_kite(clique, tail)

    for n in range(3, max_n + 1):
        for parts in range(2, min(10, n) + 1):
            yield "turan", f"n={n};parts={parts}", make_turan(n, parts)

    for left in range(3, 13):
        for right in range(left, 13):
            for internal in range(0, max_n - left - right + 1):
                yield "barbell", f"left={left};right={right};internal={internal}", make_general_barbell(left, right, internal)

    for arms in range(3, min(25, max_n - 1) + 1):
        for length in (2, 3):
            if 1 + arms * length <= max_n:
                yield "subdivided_star", f"arms={arms};length={length}", make_subdivided_star(arms, length)

    for clique in range(3, min(25, max_n - 1) + 1):
        for leaves in range(1, max_n - clique + 1):
            yield "dense_plus_pendant", f"clique={clique};leaves={leaves}", make_dense_pendant(clique, leaves)

    for nu in range(2, min(20, max_n - 5) + 1):
        for p in range(1, max_n - nu - 3):
            if nu + p + 4 <= max_n:
                yield "HV_K2nu_star_bridge", f"nu={nu};p={p}", make_hv_family(nu, p)

    for b in range(1, 8):
        for a in range(2, max_n):
            G = make_triangle_chain_star(a, b)
            if G.number_of_nodes() <= max_n:
                yield "star_triangle_chain", f"a={a};b={b}", G


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=Path, default=Path(__file__).resolve().parent / "data")
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parent / "results")
    parser.add_argument("--max-n", type=int, default=9)
    parser.add_argument("--adversarial-max-n", type=int, default=60)
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    start = time.time()
    bounds = literature_bounds()
    bound_stats: dict[str, dict[str, object]] = {
        b.id: {
            "id": b.id,
            "inequality": b.inequality,
            "scope": b.scope_name,
            "source": b.source,
            "status_note": b.status_note,
            "census_candidates": 0,
            "census_broken": 0,
            "census_first_witness": None,
            "adversarial_candidates": 0,
            "adversarial_broken": 0,
            "adversarial_first_witness": None,
        }
        for b in bounds
    }

    counts = Counter()
    tree_counts = Counter()
    chemical_counts = Counter()
    chemical_tree_counts = Counter()
    cyclomatic_counts = Counter()
    exact_identity_checks = Counter()
    violations_by_order: dict[int, Counter[str]] = defaultdict(Counter)
    training: list[tuple[str, dict[str, object]]] = []
    push_records: list[tuple[str, dict[str, object]]] = []
    census_total = 0

    for n, g6 in iter_census(args.data_dir, args.max_n):
        r = verified_indices(g6)
        if int(r["n"]) != n:
            raise AssertionError(f"catalogue order mismatch: expected n={n}, got {r['n']} for {g6}")
        census_total += 1
        counts[n] += 1
        tree_counts[n] += int(bool(r["tree"]))
        chemical_counts[n] += int(bool(r["chemical"]))
        chemical_tree_counts[n] += int(bool(r["tree"]) and bool(r["chemical"]))
        cyclomatic_counts[int(r["cyclomatic"])] += 1
        exact_identity_checks["handshake"] += 1
        exact_identity_checks["M1_edge_identity"] += 1
        exact_identity_checks["F_edge_identity"] += 1
        exact_identity_checks["HM_equals_F_plus_2M2"] += 1
        exact_identity_checks["sigma_equals_F_minus_2M2"] += 1

        if int(r["m"]) > 0:
            violations_by_order[n]["connected_tested"] += 1
            if int(r["m"]) * int(r["M1"]) > int(r["n"]) * int(r["M2"]):
                violations_by_order[n]["HV_general_broken"] += 1
            if int(r["F"]) > 2 * int(r["M2"]) + int(r["m"]) * (int(r["n"]) - 2):
                violations_by_order[n]["FG_literal_typo_broken"] += 1

        for bound in bounds:
            if not bound.scope(r):
                continue
            stat = bound_stats[bound.id]
            stat["census_candidates"] = int(stat["census_candidates"]) + 1
            if not bound.check(r):
                stat["census_broken"] = int(stat["census_broken"]) + 1
                if stat["census_first_witness"] is None:
                    stat["census_first_witness"] = witness_payload(g6, r)

        if 2 <= n <= 7:
            training.append((g6, r))
        elif n >= 8:
            push_records.append((g6, r))

    # Count checks are hard failures.
    for n in range(1, args.max_n + 1):
        if counts[n] != COUNT_REFERENCE[n]:
            raise AssertionError(f"connected count mismatch at n={n}: {counts[n]} != {COUNT_REFERENCE[n]}")
        if tree_counts[n] != TREE_REFERENCE[n]:
            raise AssertionError(f"tree count mismatch at n={n}: {tree_counts[n]} != {TREE_REFERENCE[n]}")

    ratio_candidates = build_ratio_candidates(training)
    for g6, r in push_records:
        test_ratio_candidates(ratio_candidates, g6, r, "census")

    # Materialize and sort family instances to make first witnesses smallest-order.
    family_instances: list[tuple[int, str, str, str, nx.Graph]] = []
    for family, params, G in adversarial_instances(args.adversarial_max_n):
        family_instances.append((G.number_of_nodes(), family, params, graph6_from_graph(G), G))
    family_instances.sort(key=lambda item: (item[0], item[1], item[2], item[3]))

    family_counts = Counter()
    family_hv_broken = Counter()
    adversarial_witnesses: list[dict[str, object]] = []
    seen_witness_keys: set[tuple[str, str]] = set()
    for _, family, params, g6, _G in family_instances:
        r = verified_indices(g6)
        family_counts[family] += 1
        for bound in bounds:
            if not bound.scope(r):
                continue
            stat = bound_stats[bound.id]
            stat["adversarial_candidates"] = int(stat["adversarial_candidates"]) + 1
            if not bound.check(r):
                stat["adversarial_broken"] = int(stat["adversarial_broken"]) + 1
                if stat["adversarial_first_witness"] is None:
                    stat["adversarial_first_witness"] = witness_payload(g6, r, family, params)
                key = (bound.id, g6)
                if key not in seen_witness_keys and len(adversarial_witnesses) < 100:
                    w = witness_payload(g6, r, family, params)
                    w["bound_id"] = bound.id
                    adversarial_witnesses.append(w)
                    seen_witness_keys.add(key)
                if bound.id == "HV_general":
                    family_hv_broken[family] += 1
        test_ratio_candidates(ratio_candidates, g6, r, "adversarial", family, params)

    # Attach survivors and flatten witness fields for CSV.
    literature_rows: list[dict[str, object]] = []
    for bound in bounds:
        stat = bound_stats[bound.id]
        stat["census_survived"] = int(stat["census_candidates"]) - int(stat["census_broken"])
        stat["adversarial_survived"] = int(stat["adversarial_candidates"]) - int(stat["adversarial_broken"])
        for phase in ("census", "adversarial"):
            witness = stat[f"{phase}_first_witness"]
            stat[f"{phase}_first_graph6"] = witness["graph6"] if witness else ""
            stat[f"{phase}_first_n"] = witness["n"] if witness else ""
            stat[f"{phase}_first_family"] = witness["family"] if witness else ""
            stat[f"{phase}_first_parameters"] = witness["parameters"] if witness else ""
        literature_rows.append(stat)

    ratio_rows: list[dict[str, object]] = []
    for c in ratio_candidates:
        coefficient = c["coefficient"]
        assert isinstance(coefficient, Fraction)
        row = dict(c)
        row["coefficient_fraction"] = fraction_string(coefficient)
        row["coefficient_decimal"] = f"{float(coefficient):.17g}"
        row["census_survived"] = int(c["census_tested"]) - int(c["census_broken"])
        row["adversarial_survived"] = int(c["adversarial_tested"]) - int(c["adversarial_broken"])
        for phase in ("census", "adversarial"):
            witness = c[f"{phase}_first_witness"]
            row[f"{phase}_first_graph6"] = witness["graph6"] if witness else ""
            row[f"{phase}_first_n"] = witness["n"] if witness else ""
            row[f"{phase}_first_family"] = witness["family"] if witness else ""
            row[f"{phase}_first_parameters"] = witness["parameters"] if witness else ""
            row[f"{phase}_first_observed_ratio"] = witness.get("observed_ratio", "") if witness else ""
        # Non-JSON object removed later.
        ratio_rows.append(row)

    counts_rows = []
    for n in range(1, args.max_n + 1):
        counts_rows.append({
            "n": n,
            "connected": counts[n],
            "connected_reference_A001349": COUNT_REFERENCE[n],
            "trees": tree_counts[n],
            "trees_reference_A000055": TREE_REFERENCE[n],
            "chemical_connected_Delta_le_4": chemical_counts[n],
            "chemical_trees_Delta_le_4": chemical_tree_counts[n],
        })

    family_rows = []
    for family in sorted(family_counts):
        family_rows.append({
            "family": family,
            "parameter_instances": family_counts[family],
            "HV_general_broken": family_hv_broken[family],
            "HV_general_survived": family_counts[family] - family_hv_broken[family],
        })

    # Canonical requested witnesses.
    hv17 = make_hv_family(2, 11)
    hv17_g6 = graph6_from_graph(hv17)
    hv17_r = verified_indices(hv17_g6)
    hv17_edges = sorted(tuple(sorted(edge)) for edge in hv17.edges())
    hv17_gap = Fraction(int(hv17_r["M1"]), int(hv17_r["n"])) - Fraction(int(hv17_r["M2"]), int(hv17_r["m"]))
    typo_g6 = "CF"
    typo_r = verified_indices(typo_g6)
    key_witnesses = [
        {
            **witness_payload(hv17_g6, hv17_r, "HV_K2nu_star_bridge", "nu=2;p=11"),
            "bound_id": "HV_general",
            "edge_list": hv17_edges,
            "M1_over_n": fraction_string(Fraction(int(hv17_r["M1"]), int(hv17_r["n"]))),
            "M2_over_m": fraction_string(Fraction(int(hv17_r["M2"]), int(hv17_r["m"]))),
            "normalised_gap": fraction_string(hv17_gap),
            "cross_product_gap_mM1_minus_nM2": int(hv17_r["m"]) * int(hv17_r["M1"]) - int(hv17_r["n"]) * int(hv17_r["M2"]),
            "note": "17-vertex connected bicyclic counterexample from the K_{2,nu+1}-plus-star bridge family",
        },
        {
            **witness_payload(typo_g6, typo_r, "star", "K1,3"),
            "bound_id": "FG_upper_literal_printed",
            "edge_list": sorted(tuple(sorted(edge)) for edge in nx.from_graph6_bytes(typo_g6.encode()).edges()),
            "literal_lhs_F": int(typo_r["F"]),
            "literal_rhs": 2 * int(typo_r["M2"]) + int(typo_r["m"]) * (int(typo_r["n"]) - 2),
            "corrected_rhs": 2 * int(typo_r["M2"]) + int(typo_r["m"]) * (int(typo_r["n"]) - 2) ** 2,
            "note": "smallest census failure of the literal missing-square typo; corrected form is equality",
        },
    ]

    auto_summary = {
        "generated": len(ratio_candidates),
        "broken_on_n8_n9": sum(1 for c in ratio_candidates if int(c["census_broken"]) > 0),
        "survived_n8_n9": sum(1 for c in ratio_candidates if int(c["census_broken"]) == 0),
        "survived_n8_n9_but_broken_adversarial": sum(1 for c in ratio_candidates if int(c["census_broken"]) == 0 and int(c["adversarial_broken"]) > 0),
        "hardened_survivors": sum(1 for c in ratio_candidates if int(c["census_broken"]) == 0 and int(c["adversarial_broken"]) == 0),
        "training_graphs_n2_to_n7": len(training),
        "push_graphs_n8_to_n9": len(push_records),
        "adversarial_parameter_instances": len(family_instances),
    }

    elapsed = time.time() - start
    summary = {
        "max_n_exhaustive": args.max_n,
        "census_total_including_K1": census_total,
        "census_nontrivial_n2_to_n9": census_total - 1,
        "connected_counts": dict(sorted(counts.items())),
        "tree_counts": dict(sorted(tree_counts.items())),
        "chemical_counts": dict(sorted(chemical_counts.items())),
        "chemical_tree_counts": dict(sorted(chemical_tree_counts.items())),
        "category_totals_n2_to_n9": {
            "trees": sum(tree_counts[n] for n in range(2, args.max_n + 1)),
            "chemical_connected": sum(chemical_counts[n] for n in range(2, args.max_n + 1)),
            "chemical_trees": sum(chemical_tree_counts[n] for n in range(2, args.max_n + 1)),
            "unicyclic": cyclomatic_counts[1],
        },
        "cyclomatic_counts_including_K1": dict(sorted(cyclomatic_counts.items())),
        "exact_identity_checks": dict(exact_identity_checks),
        "literature_bounds": literature_rows,
        "autofit": auto_summary,
        "adversarial_family_counts": dict(sorted(family_counts.items())),
        "key_witnesses": key_witnesses,
        "n10_status": "not enumerated; official connected count is 11,716,571",
        "elapsed_seconds": elapsed,
        "networkx_version": nx.__version__,
    }

    write_csv(
        args.output_dir / "counts.csv",
        counts_rows,
        list(counts_rows[0].keys()),
    )
    order_rows = [
        {
            "n": n,
            "connected_tested": violations_by_order[n]["connected_tested"],
            "HV_general_broken": violations_by_order[n]["HV_general_broken"],
            "FG_literal_typo_broken": violations_by_order[n]["FG_literal_typo_broken"],
        }
        for n in range(2, args.max_n + 1)
    ]
    write_csv(
        args.output_dir / "violations_by_order.csv",
        order_rows,
        list(order_rows[0].keys()),
    )
    literature_fields = [
        "id", "inequality", "scope", "source", "status_note",
        "census_candidates", "census_broken", "census_survived",
        "census_first_graph6", "census_first_n", "census_first_family", "census_first_parameters",
        "adversarial_candidates", "adversarial_broken", "adversarial_survived",
        "adversarial_first_graph6", "adversarial_first_n", "adversarial_first_family", "adversarial_first_parameters",
    ]
    write_csv(args.output_dir / "literature_bounds.csv", literature_rows, literature_fields)
    ratio_fields = [
        "id", "numerator", "denominator", "side", "coefficient_fraction", "coefficient_decimal", "domain",
        "training_graphs", "training_extremizer_graph6",
        "census_tested", "census_broken", "census_survived", "census_first_graph6", "census_first_n", "census_first_observed_ratio",
        "adversarial_tested", "adversarial_broken", "adversarial_survived", "adversarial_first_graph6", "adversarial_first_n", "adversarial_first_family", "adversarial_first_parameters", "adversarial_first_observed_ratio",
    ]
    write_csv(args.output_dir / "autofit_ratio_bounds.csv", ratio_rows, ratio_fields)
    write_csv(args.output_dir / "adversarial_families.csv", family_rows, list(family_rows[0].keys()))
    write_csv(
        args.output_dir / "key_witnesses.csv",
        [
            {
                "bound_id": w["bound_id"], "graph6": w["graph6"], "family": w["family"], "parameters": w["parameters"],
                "n": w["n"], "m": w["m"], "degree_sequence": " ".join(map(str, w["degree_sequence"])),
                "M1": w["M1"], "M2": w["M2"], "F": w["F"], "HM": w["HM"], "irr": w["irr"], "sigma": w["sigma"],
                "edge_list": json.dumps(w["edge_list"]), "note": w["note"],
            }
            for w in key_witnesses
        ],
        ["bound_id", "graph6", "family", "parameters", "n", "m", "degree_sequence", "M1", "M2", "F", "HM", "irr", "sigma", "edge_list", "note"],
    )
    (args.output_dir / "key_witnesses.json").write_text(json.dumps(key_witnesses, indent=2), encoding="utf-8")
    (args.output_dir / "adversarial_violators_sample.json").write_text(json.dumps(adversarial_witnesses, indent=2), encoding="utf-8")
    (args.output_dir / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")

    # Human-readable compact report generated from exact outputs.
    report_lines = [
        "# Degree-index inequality sweep: exact results",
        "",
        f"Exhaustive connected-graph census: n=1..{args.max_n}, {census_total:,} graphs including K1; {census_total-1:,} nontrivial graphs.",
        f"Independent primary/secondary index agreement and five exact identities: {census_total:,}/{census_total:,} graphs.",
        "",
        "## Clean connected counterexample",
        "",
        f"graph6: `{hv17_g6}`",
        f"n={hv17_r['n']}, m={hv17_r['m']}, degrees={list(hv17_r['degree_sequence'])}",
        f"M1={hv17_r['M1']}, M2={hv17_r['M2']}",
        f"M1/n={fraction_string(Fraction(int(hv17_r['M1']), int(hv17_r['n'])))}; M2/m={fraction_string(Fraction(int(hv17_r['M2']), int(hv17_r['m'])))}",
        f"M1/n - M2/m = {fraction_string(hv17_gap)} > 0; m*M1 - n*M2 = {int(hv17_r['m'])*int(hv17_r['M1'])-int(hv17_r['n'])*int(hv17_r['M2'])}.",
        "",
        "## Literal printed typo counterexample",
        "",
        f"graph6: `{typo_g6}` (K1,3). F={typo_r['F']}; literal RHS={2*int(typo_r['M2'])+int(typo_r['m'])*(int(typo_r['n'])-2)}; corrected RHS={2*int(typo_r['M2'])+int(typo_r['m'])*(int(typo_r['n'])-2)**2}.",
        "",
        "## Auto-fit summary",
        "",
        json.dumps(auto_summary, indent=2),
    ]
    (args.output_dir / "REPORT.md").write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    print(json.dumps({
        "census_total": census_total,
        "literature": {row["id"]: {"census": [row["census_candidates"], row["census_broken"]], "adversarial": [row["adversarial_candidates"], row["adversarial_broken"]]} for row in literature_rows},
        "autofit": auto_summary,
        "hv17_graph6": hv17_g6,
        "hv17_gap": fraction_string(hv17_gap),
        "elapsed_seconds": elapsed,
    }, indent=2))


if __name__ == "__main__":
    main()
