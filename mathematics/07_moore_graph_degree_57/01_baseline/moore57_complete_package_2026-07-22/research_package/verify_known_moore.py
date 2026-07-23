#!/usr/bin/env python3
"""Exact checks on the known diameter-2 Moore graphs of degrees 2, 3, and 7."""

from __future__ import annotations

from collections import Counter

import networkx as nx
import numpy as np


def adjacency_matrix_int(graph: nx.Graph, nodes: list[int]) -> np.ndarray:
    return nx.to_numpy_array(graph, nodelist=nodes, dtype=np.int64)


def exact_full_check(graph: nx.Graph, degree: int) -> None:
    nodes = list(graph.nodes())
    A = adjacency_matrix_int(graph, nodes)
    n = degree * degree + 1
    assert len(nodes) == n
    assert np.array_equal(A, A.T)
    assert np.all(np.diag(A) == 0)
    assert set(np.unique(A)).issubset({0, 1})
    assert np.all(A.sum(axis=1) == degree)
    rhs = (degree - 1) * np.eye(n, dtype=np.int64) - A + np.ones((n, n), dtype=np.int64)
    assert np.array_equal(A @ A, rhs)
    assert nx.diameter(graph) == 2
    assert nx.girth(graph) == 5


def rooted_partition(graph: nx.Graph, root: int) -> tuple[list[int], list[list[int]]]:
    branches = sorted(graph.neighbors(root))
    branch_set = set(branches)
    distance_two = [v for v in graph.nodes() if v != root and v not in branch_set]
    fibres: list[list[int]] = []
    for b in branches:
        fibre = sorted(v for v in distance_two if graph.has_edge(b, v))
        fibres.append(fibre)
    flat = [v for fibre in fibres for v in fibre]
    assert len(flat) == len(set(flat)) == len(distance_two)
    return branches, fibres


def exact_rooted_check(graph: nx.Graph, degree: int, root: int = 0) -> None:
    branches, fibres = rooted_partition(graph, root)
    q = degree - 1
    assert len(branches) == degree
    assert all(len(f) == q for f in fibres)

    # Gauge-normalize labels: retain the order of X_0, and order every other
    # fibre X_i so that its matching to X_0 is the identity permutation.
    if degree > 1:
        base = fibres[0]
        normalized = [base]
        for fibre in fibres[1:]:
            fibre_set = set(fibre)
            ordered: list[int] = []
            for x in base:
                matches = [y for y in graph.neighbors(x) if y in fibre_set]
                assert len(matches) == 1
                ordered.append(matches[0])
            assert len(set(ordered)) == q
            normalized.append(ordered)
        fibres = normalized

    leaves = [v for fibre in fibres for v in fibre]
    C = adjacency_matrix_int(graph.subgraph(leaves), leaves)
    m = len(leaves)
    P = np.zeros((m, m), dtype=np.int64)
    offset = 0
    for fibre in fibres:
        size = len(fibre)
        P[offset : offset + size, offset : offset + size] = 1
        offset += size
    rhs = q * np.eye(m, dtype=np.int64) - C + np.ones((m, m), dtype=np.int64) - P
    assert np.array_equal(C @ C, rhs)
    assert np.all(C.sum(axis=1) == q)

    # Every off-diagonal fibre block is a permutation matrix.
    for i in range(degree):
        for j in range(degree):
            block = C[i * q : (i + 1) * q, j * q : (j + 1) * q]
            if i == j:
                assert np.count_nonzero(block) == 0
            else:
                assert np.all(block.sum(axis=0) == 1)
                assert np.all(block.sum(axis=1) == 1)

    # Delete one fibre and verify the compressed matrix equation.
    if q > 0:
        M = C[q:, q:]
        B = np.eye(q * q, dtype=np.int64) + M
        Pq = np.kron(np.eye(q, dtype=np.int64), np.ones((q, q), dtype=np.int64))
        Qq = np.kron(np.ones((q, q), dtype=np.int64), np.eye(q, dtype=np.int64))
        Jq = np.ones((q * q, q * q), dtype=np.int64)
        rhs_b = q * np.eye(q * q, dtype=np.int64) + Jq - Pq - Qq
        assert np.array_equal(B @ B - B, rhs_b)
        assert np.array_equal(B @ Pq, Jq)
        assert np.array_equal(Pq @ B, Jq)
        assert np.array_equal(B @ Qq, Jq)
        assert np.array_equal(Qq @ B, Jq)

    # Redundant numerical spectrum report, after exact identities passed.
    vals = np.linalg.eigvalsh(C.astype(float))
    rounded = Counter(int(round(x)) for x in vals)
    print(f"  rooted C spectrum (rounded): {dict(sorted(rounded.items(), reverse=True))}")


def graph_suite() -> list[tuple[str, int, nx.Graph]]:
    return [
        ("5-cycle", 2, nx.cycle_graph(5)),
        ("Petersen", 3, nx.petersen_graph()),
        ("Hoffman-Singleton", 7, nx.hoffman_singleton_graph()),
    ]


def main() -> None:
    for name, degree, graph in graph_suite():
        print(f"Checking {name} (degree {degree}, order {graph.number_of_nodes()})")
        exact_full_check(graph, degree)
        exact_rooted_check(graph, degree)
        print("  all exact checks passed")


if __name__ == "__main__":
    main()
