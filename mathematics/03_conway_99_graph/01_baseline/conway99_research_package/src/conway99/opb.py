"""Proof-oriented pseudo-Boolean encoding of the reduced Conway-99 problem.

The generator is dependency-free and streams an OPB model.  It introduces:

* x_{i,j} for every possible edge of B;
* y_{i,j,k} <-> (x_{i,k} AND x_{j,k}) for every i<j and k distinct.

It then enforces the exact incidence equations BM=MT and the exact number of
common B-neighbors for every pair.  A normalized case fixes the perfect
matching induced by B on the point-star S_0.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from itertools import combinations
import json
from pathlib import Path
from typing import Iterable, Sequence, TextIO

from .model import ModelData, build_model, edge_index_map, mate
from .orbits import matching_representative


@dataclass(frozen=True)
class EncodingCounts:
    m: int
    b_vertices: int
    x_variables: int
    y_variables: int
    total_variables: int
    incidence_equalities: int
    and_constraints: int
    common_neighbor_equalities: int
    case_fix_constraints: int
    total_constraints: int

    def to_dict(self) -> dict[str, int]:
        return asdict(self)


def x_var(i: int, j: int) -> str:
    if i == j:
        raise ValueError("B has no diagonal variables")
    if i > j:
        i, j = j, i
    return f"x_{i}_{j}"


def y_var(i: int, j: int, k: int) -> str:
    if len({i, j, k}) != 3:
        raise ValueError("y indices must be distinct")
    if i > j:
        i, j = j, i
    return f"y_{i}_{j}_{k}"


def encoding_counts(m: int = 7, with_case: bool = True) -> EncodingCounts:
    model = build_model(m)
    q = model.second_layer_count
    pair_count = q * (q - 1) // 2
    y_count = pair_count * (q - 2)
    incidence = q * model.base_vertex_count
    and_constraints = 3 * y_count
    common = pair_count
    star_size = model.base_vertex_count - 2
    case_fixes = star_size * (star_size - 1) // 2 if with_case else 0
    total = incidence + and_constraints + common + case_fixes
    return EncodingCounts(
        m=m,
        b_vertices=q,
        x_variables=pair_count,
        y_variables=y_count,
        total_variables=pair_count + y_count,
        incidence_equalities=incidence,
        and_constraints=and_constraints,
        common_neighbor_equalities=common,
        case_fix_constraints=case_fixes,
        total_constraints=total,
    )


def _write_linear_constraint(
    handle: TextIO,
    terms: Iterable[tuple[int, str]],
    operator: str,
    rhs: int,
) -> None:
    if operator not in {"=", ">=", "<="}:
        raise ValueError(f"unsupported operator {operator}")
    pieces = [f"{coefficient:+d} {variable}" for coefficient, variable in terms]
    if not pieces:
        pieces = ["+0 __dummy"]
    handle.write(" ".join(pieces))
    handle.write(f" {operator} {rhs} ;\n")


def _star_indices(model: ModelData, fixed_base_vertex: int = 0) -> dict[int, int]:
    index = edge_index_map(model)
    result: dict[int, int] = {}
    for other in range(model.base_vertex_count):
        if other in {fixed_base_vertex, mate(fixed_base_vertex)}:
            continue
        edge = (fixed_base_vertex, other)
        if edge[0] > edge[1]:
            edge = (edge[1], edge[0])
        result[other] = index[edge]
    return result


def case_fixed_values(
    model: ModelData,
    partition: Sequence[int],
    fixed_base_vertex: int = 0,
) -> dict[tuple[int, int], int]:
    """Return all fixed x-values inside S_0 for a normalized case."""

    representative = matching_representative(
        partition,
        m=model.m,
        fixed_base_vertex=fixed_base_vertex,
    )
    star = _star_indices(model, fixed_base_vertex=fixed_base_vertex)
    selected = {
        tuple(sorted((star[a], star[b])))
        for a, b in representative
    }
    values: dict[tuple[int, int], int] = {}
    for i, j in combinations(sorted(star.values()), 2):
        values[(i, j)] = int((i, j) in selected)
    return values


def write_opb(
    path: str | Path,
    m: int = 7,
    partition: Sequence[int] | None = None,
    fixed_base_vertex: int = 0,
) -> EncodingCounts:
    """Write a complete exact OPB encoding.

    Parameters
    ----------
    path:
        Output .opb file.
    m:
        Generalized local-matching parameter.  Use 7 for Conway-99.
    partition:
        Optional normalized matching case.  For m=7 it must be a partition of
        6.  If omitted, no top-level symmetry case is fixed.
    """

    model = build_model(m)
    q = model.second_layer_count
    counts = encoding_counts(m=m, with_case=partition is not None)
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)

    with output.open("w", encoding="ascii", newline="\n") as handle:
        handle.write(
            f"* #variable= {counts.total_variables} #constraint= {counts.total_constraints}\n"
        )
        handle.write(f"* fixed-vertex reduction with m={m}, |B|={q}\n")
        if partition is not None:
            handle.write(f"* normalized point-star case partition={list(partition)}\n")

        # BM = MT, in entrywise incidence form.
        for i, edge in enumerate(model.base_edges):
            edge_set = set(edge)
            for u in range(model.base_vertex_count):
                terms = []
                for j, base_edge in enumerate(model.base_edges):
                    if j != i and u in base_edge:
                        terms.append((1, x_var(i, j)))
                rhs = 2 - int(u in edge_set) - int(mate(u) in edge_set)
                _write_linear_constraint(handle, terms, "=", rhs)

        # y_{i,j,k} is the conjunction x_{i,k} AND x_{j,k}; then the exact
        # common-neighbor equation is x_{i,j} + sum_k y_{i,j,k}=2-|e_i cap e_j|.
        for i in range(q):
            edge_i = model.base_edges[i]
            for j in range(i + 1, q):
                edge_j = model.base_edges[j]
                y_terms: list[tuple[int, str]] = []
                for k in range(q):
                    if k in {i, j}:
                        continue
                    y = y_var(i, j, k)
                    xik = x_var(i, k)
                    xjk = x_var(j, k)
                    # y <= xik
                    _write_linear_constraint(handle, ((1, xik), (-1, y)), ">=", 0)
                    # y <= xjk
                    _write_linear_constraint(handle, ((1, xjk), (-1, y)), ">=", 0)
                    # y >= xik + xjk - 1
                    _write_linear_constraint(
                        handle,
                        ((1, y), (-1, xik), (-1, xjk)),
                        ">=",
                        -1,
                    )
                    y_terms.append((1, y))
                overlap = len(set(edge_i).intersection(edge_j))
                _write_linear_constraint(
                    handle,
                    ((1, x_var(i, j)), *y_terms),
                    "=",
                    2 - overlap,
                )

        if partition is not None:
            for (i, j), value in sorted(
                case_fixed_values(
                    model,
                    partition,
                    fixed_base_vertex=fixed_base_vertex,
                ).items()
            ):
                _write_linear_constraint(handle, ((1, x_var(i, j)),), "=", value)

    return counts


def write_metadata(
    path: str | Path,
    counts: EncodingCounts,
    partition: Sequence[int] | None = None,
) -> None:
    payload = counts.to_dict()
    payload["partition"] = list(partition) if partition is not None else None
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
