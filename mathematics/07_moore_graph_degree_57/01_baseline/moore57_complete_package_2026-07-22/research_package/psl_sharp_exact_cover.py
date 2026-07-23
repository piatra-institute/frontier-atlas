#!/usr/bin/env python3
"""Exact exclusion of a sharply transitive 56-set in the degree-56 PSL(3,4) action."""

from __future__ import annotations

import argparse
from pathlib import Path
import hashlib
import numpy as np

from group_tools import (
    N,
    conjugacy_classes,
    cycle_type,
    fixed_points,
    is_derangement,
    load_group,
    point_suborbits,
)


def orbital_adjacency(group) -> np.ndarray:
    stabilizer_orbits = point_suborbits(group)
    representative = next(orbit[0] for orbit in stabilizer_orbits if len(orbit) == 10)
    A = np.zeros((N, N), dtype=np.int64)
    for g in group:
        A[g[0], g[representative]] = 1
    I = np.eye(N, dtype=np.int64)
    J = np.ones((N, N), dtype=np.int64)
    assert np.array_equal(A, A.T)
    assert np.array_equal(A @ A, 8 * I - 2 * A + 2 * J)
    return A


def character_values(permutation, numerator: np.ndarray, denominator: int) -> int:
    value = sum(int(numerator[i, permutation[i]]) for i in range(N))
    assert value % denominator == 0
    return value // denominator


def exact_cover_rows(fixed, derangements):
    cells = [
        (x, y)
        for x in range(N)
        for y in range(N)
        if y != x and y != fixed[x]
    ]
    assert len(cells) == 3024
    cell_index = {cell: i for i, cell in enumerate(cells)}
    candidates = [p for p in derangements if all(p[x] != fixed[x] for x in range(N))]
    candidates.sort()
    rows = [tuple(cell_index[(x, p[x])] for x in range(N)) for p in candidates]
    assert all(len(set(row)) == N for row in rows)
    return cells, candidates, rows


def solve_exact_cover(n_columns: int, rows: list[tuple[int, ...]]) -> tuple[bool, int, int]:
    n_rows = len(rows)
    column_rows = [0] * n_columns
    row_masks: list[int] = []
    for r, columns in enumerate(rows):
        bit = 1 << r
        mask = 0
        for c in columns:
            column_rows[c] |= bit
            mask |= 1 << c
        row_masks.append(mask)

    conflicts: list[int] = []
    for columns in rows:
        conflict = 0
        for c in columns:
            conflict |= column_rows[c]
        conflicts.append(conflict)

    all_rows = (1 << n_rows) - 1
    all_columns = (1 << n_columns) - 1
    nodes = 0
    max_depth = 0

    def dfs(active_rows: int, uncovered: int, depth: int) -> bool:
        nonlocal nodes, max_depth
        nodes += 1
        max_depth = max(max_depth, depth)
        if uncovered == 0:
            return depth == 54
        if depth >= 54:
            return False

        scan = uncovered
        best_size = n_rows + 1
        choices = 0
        while scan:
            low = scan & -scan
            column = low.bit_length() - 1
            scan -= low
            available = column_rows[column] & active_rows
            size = available.bit_count()
            if size < best_size:
                best_size = size
                choices = available
                if size <= 1:
                    break
        if best_size == 0:
            return False

        while choices:
            low = choices & -choices
            row = low.bit_length() - 1
            choices -= low
            if dfs(active_rows & ~conflicts[row], uncovered & ~row_masks[row], depth + 1):
                return True
        return False

    satisfiable = dfs(all_rows, all_columns, 0)
    return satisfiable, nodes, max_depth


def serialize_instance(fixed, rows, row_orders) -> bytes:
    lines = [f"3024 {len(rows)}", " ".join(str(x + 1) for x in fixed)]
    for order, row in zip(row_orders, rows):
        lines.append(str(order) + " " + " ".join(str(c) for c in row))
    return ("\n".join(lines) + "\n").encode("ascii")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-inputs", type=Path, default=None)
    args = parser.parse_args()

    row, generators, group = load_group(1)
    assert row["description"] == "PSL(3, 4)"
    assert len(group) == 20160
    classes = conjugacy_classes(group, generators)

    A = orbital_adjacency(group)
    I = np.eye(N, dtype=np.int64)
    numerator_20 = (A - 10 * I) @ (A - 2 * I)       # divide by 84
    numerator_35 = -(A - 10 * I) @ (A + 4 * I)      # divide by 48

    derangement_classes = []
    for cls in classes:
        representative = cls[0]
        if not is_derangement(representative):
            continue
        chi20 = character_values(representative, numerator_20, 84)
        chi35 = character_values(representative, numerator_35, 48)
        assert 1 + chi20 + chi35 == fixed_points(representative)
        derangement_classes.append(
            {
                "size": len(cls),
                "cycle_type": cycle_type(representative),
                "chi20": chi20,
                "chi35": chi35,
                "representative": representative,
                "class": cls,
            }
        )
    derangement_classes.sort(key=lambda item: (item["cycle_type"], item["representative"]))

    print("PSL(3,4), degree-56 rank-3 action")
    print("order:", len(group))
    print("derangement conjugacy classes:")
    for i, item in enumerate(derangement_classes):
        print(
            i,
            "size", item["size"],
            "cycle", item["cycle_type"],
            "chi20", item["chi20"],
            "chi35", item["chi35"],
        )

    assert len(derangement_classes) == 4
    assert sum(item["size"] for item in derangement_classes) == 8280
    order4_classes = [item for item in derangement_classes if item["cycle_type"][0] == 4]
    order7_classes = [item for item in derangement_classes if item["cycle_type"][0] == 7]
    assert len(order4_classes) == len(order7_classes) == 2
    assert all((item["chi20"], item["chi35"]) == (0, -1) for item in order4_classes)
    assert all((item["chi20"], item["chi35"]) == (-1, 0) for item in order7_classes)
    print("trace equations force exactly 35 order-4 and 20 order-7 elements")

    derangements = sorted(p for p in group if is_derangement(p))
    assert len(derangements) == 8280
    results = []
    if args.write_inputs is not None:
        args.write_inputs.mkdir(parents=True, exist_ok=True)

    for branch, item in enumerate(order4_classes):
        fixed = item["representative"]
        cells, candidates, rows = exact_cover_rows(fixed, derangements)
        assert len(candidates) == 3400
        orders = [cycle_type(p)[0] for p in candidates]
        payload = serialize_instance(fixed, rows, orders)
        digest = hashlib.sha256(payload).hexdigest()
        if args.write_inputs is not None:
            path = args.write_inputs / f"psl_exactcover_branch_{branch}.txt"
            path.write_bytes(payload)
        satisfiable, nodes, max_depth = solve_exact_cover(len(cells), rows)
        print(
            f"branch {branch}: fixed class size={item['size']}, candidates={len(candidates)}, "
            f"sha256={digest}, satisfiable={satisfiable}, nodes={nodes}, max_depth={max_depth}"
        )
        assert not satisfiable
        results.append((nodes, max_depth))

    assert results == [(2416, 8), (2526, 11)]
    print("CONCLUSION: PSL(3,4) contains no sharply transitive set in this action.")


if __name__ == "__main__":
    main()
