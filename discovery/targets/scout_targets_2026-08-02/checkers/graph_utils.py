#!/usr/bin/env python3
"""Small exact graph utilities used by Stage-0 target checkers."""
from __future__ import annotations

from itertools import combinations
from typing import Iterable, Sequence
import networkx as nx


def graph_from_graph6(s: str) -> nx.Graph:
    s = s.strip()
    if not s:
        raise ValueError("empty graph6 string")
    g = nx.from_graph6_bytes(s.encode("ascii"))
    return nx.convert_node_labels_to_integers(g, ordering="sorted")


def graph6(g: nx.Graph) -> str:
    h = nx.convert_node_labels_to_integers(g, ordering="sorted")
    return nx.to_graph6_bytes(h, header=False).decode("ascii").strip()


def zero_forcing_closure(g: nx.Graph, initial: Iterable[int]) -> set[int]:
    black = set(initial)
    changed = True
    while changed:
        changed = False
        for u in tuple(black):
            white = [v for v in g.neighbors(u) if v not in black]
            if len(white) == 1:
                black.add(white[0])
                changed = True
    return black


def is_zero_forcing_set(g: nx.Graph, initial: Iterable[int]) -> bool:
    return len(zero_forcing_closure(g, initial)) == g.number_of_nodes()


def zero_forcing_number(g: nx.Graph) -> int:
    nodes = list(g.nodes())
    n = len(nodes)
    if n == 0:
        return 0
    for k in range(1, n + 1):
        for ss in combinations(nodes, k):
            if is_zero_forcing_set(g, ss):
                return k
    return n


def zero_forcing_set_count(g: nx.Graph, k: int) -> int:
    if k < 0 or k > g.number_of_nodes():
        return 0
    return sum(is_zero_forcing_set(g, ss) for ss in combinations(g.nodes(), k))


def chromatic_number(g: nx.Graph) -> int:
    """Exact DSATUR branch-and-bound for small graphs."""
    n = g.number_of_nodes()
    if n == 0:
        return 0
    nodes = list(g.nodes())
    adj = {v: set(g.neighbors(v)) for v in nodes}

    # Greedy DSATUR upper bound.
    greedy = nx.coloring.greedy_color(g, strategy="saturation_largest_first")
    best = 1 + max(greedy.values(), default=-1)
    colors: dict[int, int] = {}

    def select_vertex() -> int:
        uncolored = [v for v in nodes if v not in colors]
        return max(
            uncolored,
            key=lambda v: (len({colors[w] for w in adj[v] if w in colors}), len(adj[v])),
        )

    def dfs(used: int) -> None:
        nonlocal best
        if len(colors) == n:
            best = min(best, used)
            return
        if used >= best:
            return
        v = select_vertex()
        forbidden = {colors[w] for w in adj[v] if w in colors}
        for c in range(min(used + 1, best)):
            if c in forbidden:
                continue
            new_used = max(used, c + 1)
            if new_used >= best:
                continue
            colors[v] = c
            dfs(new_used)
            del colors[v]

    dfs(0)
    return best


def complete_multipartite(parts: Sequence[int]) -> nx.Graph:
    if any(x < 0 for x in parts):
        raise ValueError("negative part size")
    g = nx.Graph()
    blocks: list[list[int]] = []
    cursor = 0
    for size in parts:
        block = list(range(cursor, cursor + size))
        blocks.append(block)
        g.add_nodes_from(block)
        cursor += size
    for i in range(len(blocks)):
        for j in range(i + 1, len(blocks)):
            g.add_edges_from((u, v) for u in blocks[i] for v in blocks[j])
    return g


def turan_graph(n: int, k: int) -> tuple[nx.Graph, list[list[int]]]:
    if not (1 <= k <= n):
        raise ValueError("require 1 <= k <= n")
    q, r = divmod(n, k)
    parts = [q + 1] * r + [q] * (k - r)
    g = complete_multipartite(parts)
    blocks: list[list[int]] = []
    cursor = 0
    for size in parts:
        blocks.append(list(range(cursor, cursor + size)))
        cursor += size
    return g, blocks


def validate_partition(nodes: Iterable[int], blocks: Sequence[Sequence[int]]) -> None:
    flat = [v for b in blocks for v in b]
    if any(len(b) == 0 for b in blocks):
        raise ValueError("partition blocks must be nonempty")
    if len(flat) != len(set(flat)):
        raise ValueError("partition blocks overlap")
    if set(flat) != set(nodes):
        raise ValueError("partition does not cover exactly the vertex set")
