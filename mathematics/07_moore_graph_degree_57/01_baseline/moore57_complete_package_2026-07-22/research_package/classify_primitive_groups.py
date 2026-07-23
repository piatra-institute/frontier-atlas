#!/usr/bin/env python3
"""Verify the complete primitive-group reduction in degree 56."""

from __future__ import annotations

from fractions import Fraction
import math
import numpy as np

from group_tools import N, fixed_points, load_group, metadata, point_suborbits


def orbital_adjacency(group, suborbit_size: int) -> np.ndarray:
    suborbits = point_suborbits(group)
    target = next(orbit for orbit in suborbits if len(orbit) == suborbit_size)
    representative = target[0]
    adjacency = np.zeros((N, N), dtype=np.int64)
    for g in group:
        adjacency[g[0], g[representative]] = 1
    assert np.array_equal(adjacency, adjacency.T)
    assert np.all(np.diag(adjacency) == 0)
    assert np.all(adjacency.sum(axis=1) == suborbit_size)
    return adjacency


def solve_three_multiplicities() -> tuple[int, int, int]:
    # For the valency-15 orbital graph, the nontrivial eigenvalues are 7, 1, -3.
    # Solve a+b+c=55, 7a+b-3c=-15, 49a+b+9c=615.
    for a in range(56):
        for b in range(56 - a):
            c = 55 - a - b
            if 7 * a + b - 3 * c == -15 and 49 * a + b + 9 * c == 615:
                return a, b, c
    raise AssertionError("No multiplicity solution")


def main() -> None:
    rows = metadata()
    assert len(rows) == 9
    print("Complete PrimGrp degree-56 list: 9 permutation-isomorphism classes")
    print("index | group | order | subdegrees | derangements | module test")
    print("------|-------|-------|------------|--------------|------------")

    for index in range(1, 8):
        row, _, group = load_group(index)
        suborbits = point_suborbits(group)
        subdegrees = sorted(len(orbit) for orbit in suborbits if len(orbit) > 1)
        declared = sorted(size for size, multiplicity in row["subdegrees"] for _ in range(multiplicity))
        assert subdegrees == declared
        derangements = sum(fixed_points(g) == 0 for g in group)

        if index <= 5:
            A = orbital_adjacency(group, 10)
            I = np.eye(N, dtype=np.int64)
            J = np.ones((N, N), dtype=np.int64)
            assert np.array_equal(A @ A, 8 * I - 2 * A + 2 * J)
            # Spectrum 10^1, 2^35, (-4)^20. Rank 3 makes both nontrivial eigenspaces irreducible.
            module_test = "20,35: pass"
        else:
            A = orbital_adjacency(group, 15)
            I = np.eye(N, dtype=np.int64)
            polynomial = (A - 15 * I) @ (A - 7 * I) @ (A - I) @ (A + 3 * I)
            assert np.count_nonzero(polynomial) == 0
            a, b, c = solve_three_multiplicities()
            assert (a, b, c) == (7, 20, 28)
            module_test = "7,20,28: fail"

        print(
            f"{index:>5} | {row['description']} | {len(group)} | {subdegrees} | "
            f"{derangements} | {module_test}"
        )

    # The symbolic Alt(56), Sym(56) entries are rank 2; the nontrivial module has dimension 55.
    for index in (8, 9):
        row = rows[index - 1]
        assert row["subdegrees"] == [(55, 1)]
        print(
            f"{index:>5} | {row['description']} | {row['order']} | [55] | not enumerated | 55: pass"
        )

    proper_block_counts = [2, 4, 7, 8, 14, 28]
    assert all((m - 1) % 5 != 0 for m in proper_block_counts)
    print("\nPrimitivity check:")
    print("proper numbers of blocks:", proper_block_counts)
    print("dimensions of block-constant zero-sum modules:", [m - 1 for m in proper_block_counts])
    print("none is divisible by 5, so an admissible generated group cannot be imprimitive")

    print("\nAfter the 5-divisibility test:")
    print("survive: groups 1-5, 8, 9")
    print("excluded: groups 6-7 (Alt(8), Sym(8) on 3-subsets)")


if __name__ == "__main__":
    main()
