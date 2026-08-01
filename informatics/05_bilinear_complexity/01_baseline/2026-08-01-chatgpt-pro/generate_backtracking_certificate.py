#!/usr/bin/env python3
"""Generate finite substitution/backtracking certificates.

This is the search/generator. The verifier is a separate implementation in verify_lower.py.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from functools import lru_cache
from itertools import combinations
from pathlib import Path


def span_mask(vectors: list[int] | tuple[int, ...]) -> int:
    values = {0}
    for vector in vectors:
        values |= {x ^ vector for x in tuple(values)}
    return sum(1 << x for x in values)


def elements(mask: int) -> list[int]:
    return [x for x in range(16) if (mask >> x) & 1]


def dimension(mask: int) -> int:
    return mask.bit_count().bit_length() - 1


def mul2(a: int, b: int) -> int:
    out = 0
    for i in range(2):
        for j in range(2):
            bit = 0
            for k in range(2):
                bit ^= ((a >> (2 * i + k)) & 1) & ((b >> (2 * k + j)) & 1)
            out |= bit << (2 * i + j)
    return out


def det2(a: int) -> int:
    return ((a & 1) & ((a >> 3) & 1)) ^ (((a >> 1) & 1) & ((a >> 2) & 1))


GL2 = [a for a in range(16) if det2(a)]


def act(matrix: int, left: int, right: int) -> int:
    return mul2(mul2(left, matrix), right)


@lru_cache(maxsize=None)
def canonical_orbit(mask: int) -> int:
    best = None
    for left in GL2:
        for right in GL2:
            transformed = span_mask(tuple(act(x, left, right) for x in elements(mask)))
            if best is None or transformed < best:
                best = transformed
    assert best is not None
    return best


def minimal_coset_representatives(base_mask: int) -> list[int]:
    base = elements(base_mask)
    return [r for r in range(1, 16) if r == min(r ^ s for s in base)]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--orbits", type=Path, required=True)
    ap.add_argument("--orbit-index", type=int, required=True)
    ap.add_argument("--target", type=int, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    orbit_data = json.loads(args.orbits.read_text())
    orbit_rows = orbit_data["orbits"]
    by_index = {row["index"]: row for row in orbit_rows}
    base_row = by_index[args.orbit_index]
    base_mask = span_mask(tuple(base_row["restrictions"]))

    canonical_to_orbit: dict[int, int] = {}
    lower_bounds: dict[int, int] = {}
    for row in orbit_rows:
        key = canonical_orbit(span_mask(tuple(row["restrictions"])))
        assert key not in canonical_to_orbit
        canonical_to_orbit[key] = row["index"]
        lower_bounds[row["index"]] = row["lower_bound"]

    candidates = minimal_coset_representatives(base_mask)
    leaves: list[dict[str, object]] = []
    internal_count = 0
    max_depth = 0

    def closure(sequence: list[int]):
        n = len(sequence)
        # Larger selected subsets first. This deterministic policy reproduces the compact trees.
        for selected_count in range(n, 0, -1):
            for positions in combinations(range(n), selected_count):
                selected = [sequence[p] for p in positions]
                extension = span_mask(tuple(elements(base_mask) + selected))
                if dimension(extension) <= dimension(base_mask):
                    continue
                orbit_index = canonical_to_orbit[canonical_orbit(extension)]
                lb = lower_bounds[orbit_index]
                if selected_count + lb >= args.target:
                    mask = sum(1 << p for p in positions)
                    return mask, orbit_index
        return None

    def recurse(sequence: list[int], max_candidate_index: int) -> None:
        nonlocal internal_count, max_depth
        max_depth = max(max_depth, len(sequence))
        hit = closure(sequence)
        if hit is not None:
            mask, orbit_index = hit
            leaves.append({"sequence": sequence, "selected_mask": mask, "orbit_index": orbit_index})
            return
        internal_count += 1
        for candidate_index in range(max_candidate_index + 1):
            recurse(sequence + [candidates[candidate_index]], candidate_index)

    recurse([], len(candidates) - 1)

    depth_hist = Counter(len(row["sequence"]) for row in leaves)
    orbit_hist = Counter(int(row["orbit_index"]) for row in leaves)
    result = {
        "schema": "piatra.substitution_backtracking_certificate.v1",
        "field": "F2",
        "map": "<2,2,3>",
        "base_orbit_index": args.orbit_index,
        "base_restrictions": base_row["restrictions"],
        "target_lower_bound": args.target,
        "candidate_vectors": candidates,
        "ordering": "nonincreasing candidate index",
        "closure_rule": "For selected terms I, rank(T_base) >= |I| + LB(T_restricted_by_span(I)).",
        "leaf_count": len(leaves),
        "internal_count": internal_count,
        "max_depth": max_depth,
        "leaf_depth_histogram": {str(k): v for k, v in sorted(depth_hist.items())},
        "closure_orbit_histogram": {str(k): v for k, v in sorted(orbit_hist.items())},
        "leaves": leaves,
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        f"generated {args.output}: leaves={len(leaves)} internal={internal_count} "
        f"max_depth={max_depth} candidates={candidates}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
