#!/usr/bin/env python3
"""Independent exact verifier for R_F2(<2,2,3>) >= 11.

The certificate generator is not imported. This verifier independently reconstructs:
* all 67 restriction subspaces of F2^4 and their 11 GL(2,2)^2 orbits;
* flattening bounds for the easy orbits;
* the difficult orbit-5 two-slice rank-9 check via a separate C++ exhaustive checker;
* monotonicity reductions for codimension-one orbits;
* finite substitution trees, including complete branch coverage.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
from collections import Counter
from pathlib import Path


def subspace(vectors) -> frozenset[int]:
    values = {0}
    for vector in vectors:
        values.update({x ^ vector for x in tuple(values)})
    return frozenset(values)


def mask_of(space: frozenset[int]) -> int:
    return sum(1 << x for x in space)


def dimension(space: frozenset[int]) -> int:
    size = len(space)
    assert size and size & (size - 1) == 0
    return int(math.log2(size))


def det2(a: int) -> int:
    return ((a & 1) & ((a >> 3) & 1)) ^ (((a >> 1) & 1) & ((a >> 2) & 1))


def multiply_2x2(a: int, b: int) -> int:
    answer = 0
    for row in range(2):
        for column in range(2):
            value = 0
            for middle in range(2):
                value ^= ((a >> (2 * row + middle)) & 1) & ((b >> (2 * middle + column)) & 1)
            answer |= value << (2 * row + column)
    return answer


GL2 = tuple(a for a in range(16) if det2(a))
assert len(GL2) == 6


def orbit_key(space: frozenset[int]) -> int:
    images = []
    for left in GL2:
        for right in GL2:
            transformed = subspace(multiply_2x2(multiply_2x2(left, x), right) for x in space)
            images.append(mask_of(transformed))
    return min(images)


def all_subspaces() -> set[frozenset[int]]:
    # Exhaust all generating subsets of the 15 nonzero vectors; deduplication must yield 67.
    answer = set()
    for generating_mask in range(1 << 15):
        answer.add(subspace(i + 1 for i in range(15) if (generating_mask >> i) & 1))
    return answer


def nullspace_basis(restrictions: frozenset[int]) -> tuple[int, ...]:
    allowed = [
        x for x in range(16)
        if all(((x & restriction).bit_count() & 1) == 0 for restriction in restrictions)
    ]
    basis: list[int] = []
    current = subspace(())
    for x in allowed[1:]:
        if x not in current:
            basis.append(x)
            current = subspace(basis)
    assert len(basis) == 4 - dimension(restrictions)
    assert set(current) == set(allowed)
    return tuple(basis)


def restricted_tensor(restrictions: frozenset[int]):
    basis = nullspace_basis(restrictions)
    tensor = [[[0 for _ in range(6)] for _ in range(6)] for _ in basis]
    for a_index, allowed_matrix in enumerate(basis):
        for i in range(2):
            for j in range(2):
                if (allowed_matrix >> (2 * i + j)) & 1:
                    for k in range(3):
                        tensor[a_index][3 * j + k][3 * i + k] ^= 1
    return basis, tensor


def binary_rank(rows: list[int]) -> int:
    pivots: dict[int, int] = {}
    rank = 0
    for row in rows:
        x = row
        while x:
            pivot = x.bit_length() - 1
            if pivot in pivots:
                x ^= pivots[pivot]
            else:
                pivots[pivot] = x
                rank += 1
                break
    return rank


def flattening_ranks(tensor) -> tuple[int, int, int]:
    a_dim = len(tensor)
    a_rows = []
    for a in range(a_dim):
        row = 0
        for b in range(6):
            for c in range(6):
                row |= tensor[a][b][c] << (6 * b + c)
        a_rows.append(row)
    b_rows = []
    for b in range(6):
        row = 0
        for a in range(a_dim):
            for c in range(6):
                row |= tensor[a][b][c] << (6 * a + c)
        b_rows.append(row)
    c_rows = []
    for c in range(6):
        row = 0
        for a in range(a_dim):
            for b in range(6):
                row |= tensor[a][b][c] << (6 * a + b)
        c_rows.append(row)
    return binary_rank(a_rows), binary_rank(b_rows), binary_rank(c_rows)


def packed_slice(tensor, a_index: int) -> int:
    packed = 0
    for b in range(6):
        row = sum(tensor[a_index][b][c] << c for c in range(6))
        packed |= row << (6 * b)
    return packed


def rank6_packed(matrix: int) -> int:
    return binary_rank([(matrix >> (6 * row)) & 63 for row in range(6)])


def minimal_coset_representatives(base: frozenset[int]) -> list[int]:
    return [r for r in range(1, 16) if r == min(r ^ s for s in base)]


def verify_tree(path: Path, orbit_rows, orbit_key_to_index, verified_lbs) -> dict[str, object]:
    raw = path.read_bytes()
    cert = json.loads(raw)
    assert cert["field"] == "F2" and cert["map"] == "<2,2,3>"
    base_index = cert["base_orbit_index"]
    base_row = orbit_rows[base_index]
    assert cert["base_restrictions"] == base_row["restrictions"]
    base = subspace(base_row["restrictions"])
    target = cert["target_lower_bound"]
    candidates = minimal_coset_representatives(base)
    assert cert["candidate_vectors"] == candidates

    leaves: dict[tuple[int, ...], dict] = {}
    all_prefixes: set[tuple[int, ...]] = {()}
    depth_hist = Counter()
    orbit_hist = Counter()
    for leaf in cert["leaves"]:
        sequence = tuple(leaf["sequence"])
        assert sequence not in leaves
        assert all(sequence[i] >= sequence[i + 1] for i in range(len(sequence) - 1))
        assert all(x in candidates for x in sequence)
        leaves[sequence] = leaf
        for p in range(len(sequence) + 1):
            all_prefixes.add(sequence[:p])
        depth_hist[len(sequence)] += 1
        orbit_hist[leaf["orbit_index"]] += 1

    # Prefix-free leaves are essential: a closed branch cannot also have descendants.
    for sequence in leaves:
        assert not any(sequence != other and other[: len(sequence)] == sequence for other in leaves)

    visited_leaves: set[tuple[int, ...]] = set()
    internal_count = 0
    max_depth = 0

    def recurse(prefix: tuple[int, ...], max_candidate_index: int) -> None:
        nonlocal internal_count, max_depth
        max_depth = max(max_depth, len(prefix))
        if prefix in leaves:
            leaf = leaves[prefix]
            mask = int(leaf["selected_mask"])
            assert mask > 0 and mask < (1 << len(prefix))
            selected = [prefix[p] for p in range(len(prefix)) if (mask >> p) & 1]
            extension = subspace(tuple(base) + tuple(selected))
            assert dimension(extension) > dimension(base)
            computed_orbit = orbit_key_to_index[orbit_key(extension)]
            assert computed_orbit == leaf["orbit_index"]
            assert computed_orbit in verified_lbs
            assert len(selected) + verified_lbs[computed_orbit] >= target
            visited_leaves.add(prefix)
            return

        internal_count += 1
        for child_index in range(max_candidate_index + 1):
            child = prefix + (candidates[child_index],)
            assert child in all_prefixes, f"missing branch at {child}"
            recurse(child, child_index)

    recurse((), len(candidates) - 1)
    assert visited_leaves == set(leaves)
    assert cert["leaf_count"] == len(leaves)
    assert cert["internal_count"] == internal_count
    assert cert["max_depth"] == max_depth
    assert cert["leaf_depth_histogram"] == {str(k): v for k, v in sorted(depth_hist.items())}
    assert cert["closure_orbit_histogram"] == {str(k): v for k, v in sorted(orbit_hist.items())}

    return {
        "sha256": hashlib.sha256(raw).hexdigest(),
        "leaves": len(leaves),
        "internal": internal_count,
        "max_depth": max_depth,
        "base_orbit": base_index,
        "target": target,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--orbits", type=Path, required=True)
    ap.add_argument("--full-cert", type=Path, required=True)
    ap.add_argument("--orbit7-cert", type=Path, required=True)
    ap.add_argument("--two-slice-exe", type=Path, required=True)
    args = ap.parse_args()

    orbit_doc = json.loads(args.orbits.read_text())
    assert orbit_doc["field"] == "F2"
    rows_list = orbit_doc["orbits"]
    orbit_rows = {row["index"]: row for row in rows_list}
    assert set(orbit_rows) == set(range(11))

    spaces = all_subspaces()
    assert len(spaces) == 67
    dimension_counts = Counter(dimension(space) for space in spaces)
    assert dimension_counts == Counter({0: 1, 1: 15, 2: 35, 3: 15, 4: 1})
    orbit_buckets: dict[tuple[int, int], list[frozenset[int]]] = {}
    for space in spaces:
        orbit_buckets.setdefault((dimension(space), orbit_key(space)), []).append(space)
    orbit_counts = Counter(key[0] for key in orbit_buckets)
    assert orbit_counts == Counter({0: 1, 1: 2, 2: 5, 3: 2, 4: 1})
    assert len(orbit_buckets) == 11

    orbit_key_to_index: dict[int, int] = {}
    for index, row in orbit_rows.items():
        space = subspace(row["restrictions"])
        assert dimension(space) == row["codimension"]
        key = orbit_key(space)
        assert key not in orbit_key_to_index
        orbit_key_to_index[key] = index
    assert len(orbit_key_to_index) == 11
    assert {orbit_key(space) for space in spaces} == set(orbit_key_to_index)

    verified_lbs: dict[int, int] = {0: 0}
    flattening_expected = {1: 3, 2: 6, 3: 6, 4: 6, 6: 6}
    flattening_actual = {}
    tensors = {}
    for index, row in orbit_rows.items():
        basis, tensor = restricted_tensor(subspace(row["restrictions"]))
        tensors[index] = (basis, tensor)
        flattening_actual[index] = flattening_ranks(tensor)
    for index, target in flattening_expected.items():
        ranks = flattening_actual[index]
        assert max(ranks) >= target, (index, ranks, target)
        verified_lbs[index] = target

    # Orbit 5: exact rank 9 for a 2-slice tensor. The separate C++ checker exhausts
    # every rank<=2 matrix around all three centers in the rank-metric formula.
    basis5, tensor5 = tensors[5]
    assert len(basis5) == 2
    m0, m1 = packed_slice(tensor5, 0), packed_slice(tensor5, 1)
    result = subprocess.run(
        [str(args.two_slice_exe), format(m0, "x"), format(m1, "x")],
        check=False,
        text=True,
        capture_output=True,
    )
    if result.stdout:
        print(result.stdout.strip())
    if result.stderr:
        print(result.stderr.strip())
    assert result.returncode == 0
    verified_lbs[5] = 9

    # Orbit 7: for its two slices, all three M0, M1, M0+M1 have matrix rank 6.
    # Pairwise matrix-rank triangle inequalities give 2R >= 6+6+6 = 18.
    basis7, tensor7 = tensors[7]
    assert len(basis7) == 2
    n0, n1 = packed_slice(tensor7, 0), packed_slice(tensor7, 1)
    triple = (rank6_packed(n0), rank6_packed(n1), rank6_packed(n0 ^ n1))
    assert triple == (6, 6, 6)
    verified_lbs[7] = 9

    # Codimension-one orbits inherit LB 9 after one further restriction to orbit 5.
    for index in (8, 9):
        row = orbit_rows[index]
        extension = subspace(tuple(row["restrictions"]) + (row["extra_restriction"],))
        assert orbit_key_to_index[orbit_key(extension)] == 5
        verified_lbs[index] = 9

    # Redundant independent substitution certificate for orbit 7, then the full tensor.
    orbit7_summary = verify_tree(
        args.orbit7_cert, orbit_rows, orbit_key_to_index, verified_lbs
    )
    assert orbit7_summary["leaves"] == 13 and orbit7_summary["target"] == 9

    full_summary = verify_tree(
        args.full_cert, orbit_rows, orbit_key_to_index, verified_lbs
    )
    assert full_summary["leaves"] == 1303 and full_summary["target"] == 11
    verified_lbs[10] = 11

    assert verified_lbs == {0: 0, 1: 3, 2: 6, 3: 6, 4: 6, 5: 9, 6: 6, 7: 9, 8: 9, 9: 9, 10: 11}
    print(
        "LOWER OK: 67 subspaces; 11 orbits; "
        f"flattenings={flattening_actual}; orbit7_ranks={triple}; "
        f"trees=({orbit7_summary['leaves']},{full_summary['leaves']})"
    )
    print(f"full_certificate_sha256={full_summary['sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
