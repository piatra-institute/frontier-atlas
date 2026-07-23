"""Canonical fixed-vertex reduction for srg(1 + 2m^2, 2m, 1, 2).

For Conway's problem, m=7.  Fixing one vertex x forces its neighborhood to
be m disjoint edges.  The distance-two vertices are canonically indexed by
the edges of K_{2,2,...,2} with m parts.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Iterable, Tuple

import numpy as np
from numpy.typing import NDArray

IntMatrix = NDArray[np.int64]
BaseEdge = Tuple[int, int]


def mate(vertex: int) -> int:
    """Return the partner of ``vertex`` in the fixed matching (0,1),(2,3),..."""

    if vertex < 0:
        raise ValueError("vertex must be nonnegative")
    return vertex ^ 1


def part(vertex: int) -> int:
    """Return the fixed matching-pair index containing ``vertex``."""

    if vertex < 0:
        raise ValueError("vertex must be nonnegative")
    return vertex // 2


@dataclass(frozen=True)
class ModelData:
    """Matrices and labels for the fixed-vertex reduction."""

    m: int
    base_vertex_count: int
    second_layer_count: int
    full_vertex_count: int
    degree: int
    base_edges: tuple[BaseEdge, ...]
    L: IntMatrix
    T: IntMatrix
    M: IntMatrix

    @property
    def b_degree(self) -> int:
        return self.degree - 2

    @property
    def all_ones_base(self) -> IntMatrix:
        return np.ones((self.base_vertex_count, self.base_vertex_count), dtype=np.int64)

    @property
    def all_ones_second(self) -> IntMatrix:
        return np.ones((self.second_layer_count, self.second_layer_count), dtype=np.int64)


def _base_edges(vertex_count: int) -> tuple[BaseEdge, ...]:
    return tuple(
        (u, v)
        for u, v in combinations(range(vertex_count), 2)
        if v != mate(u)
    )


def build_model(m: int = 7) -> ModelData:
    """Build the canonical matrices for the fixed-vertex reduction.

    Parameters
    ----------
    m:
        Number of edges in the fixed vertex's local matching.  Conway's
        problem has ``m=7``.
    """

    if m < 2:
        raise ValueError("m must be at least 2")

    n = 2 * m
    edges = _base_edges(n)
    q = len(edges)
    expected_q = 2 * m * (m - 1)
    if q != expected_q:
        raise AssertionError((q, expected_q))

    L = np.zeros((n, n), dtype=np.int64)
    for u in range(0, n, 2):
        L[u, u + 1] = 1
        L[u + 1, u] = 1

    T = np.ones((n, n), dtype=np.int64) - np.eye(n, dtype=np.int64) - L

    M = np.zeros((q, n), dtype=np.int64)
    for i, (u, v) in enumerate(edges):
        M[i, u] = 1
        M[i, v] = 1

    return ModelData(
        m=m,
        base_vertex_count=n,
        second_layer_count=q,
        full_vertex_count=1 + 2 * m * m,
        degree=2 * m,
        base_edges=edges,
        L=L,
        T=T,
        M=M,
    )


def edge_index_map(model: ModelData) -> dict[BaseEdge, int]:
    """Map every canonical base edge to its second-layer index."""

    return {edge: i for i, edge in enumerate(model.base_edges)}


def canonical_edge(u: int, v: int) -> BaseEdge:
    """Canonicalize an unordered edge."""

    if u == v:
        raise ValueError("an edge needs two distinct endpoints")
    return (u, v) if u < v else (v, u)


def share_endpoint(e: BaseEdge, f: BaseEdge) -> int:
    """Return 1 when two distinct base edges share an endpoint, else 0."""

    return int(bool(set(e).intersection(f)))


def validate_model_identities(model: ModelData) -> dict[str, bool]:
    """Check the exact identities used by the block reduction."""

    n = model.base_vertex_count
    expected_mtm = model.degree - 2
    checks = {
        "L_is_involution": np.array_equal(model.L @ model.L, np.eye(n, dtype=np.int64)),
        "T_definition": np.array_equal(
            model.T,
            np.ones((n, n), dtype=np.int64) - np.eye(n, dtype=np.int64) - model.L,
        ),
        "M_row_sums_2": bool(np.all(model.M.sum(axis=1) == 2)),
        "M_column_sums": bool(np.all(model.M.sum(axis=0) == expected_mtm)),
        "MTM_identity": np.array_equal(
            model.M.T @ model.M,
            expected_mtm * np.eye(n, dtype=np.int64) + model.T,
        ),
    }
    return checks
