"""Lossless 11-case normalization for the matching in one point-star.

Fix base vertex 0.  The 12 second-layer vertices containing 0 are labeled by
2,...,13.  Their B-induced graph is a perfect matching.  Relative to the
fixed mate matching Q={(2,3),(4,5),...,(12,13)}, its orbit under C2 wr S6 is
classified by the alternating-cycle half-lengths, hence by a partition of 6.
"""

from __future__ import annotations

from collections import Counter
from itertools import permutations, product
from typing import Iterable, Iterator, Sequence

Matching = tuple[tuple[int, int], ...]


def canonical_pair(a: int, b: int) -> tuple[int, int]:
    if a == b:
        raise ValueError("matching edge endpoints must be distinct")
    return (a, b) if a < b else (b, a)


def canonical_matching(edges: Iterable[tuple[int, int]]) -> Matching:
    result = tuple(sorted(canonical_pair(a, b) for a, b in edges))
    flat = [vertex for edge in result for vertex in edge]
    if len(flat) != len(set(flat)):
        raise ValueError("edges do not form a matching")
    return result


def integer_partitions(n: int, maximum: int | None = None) -> Iterator[tuple[int, ...]]:
    """Yield partitions of n in reverse lexicographic order."""

    if n < 0:
        return
    if n == 0:
        yield ()
        return
    cap = n if maximum is None else min(n, maximum)
    for first in range(cap, 0, -1):
        for rest in integer_partitions(n - first, first):
            yield (first,) + rest


def fixed_q_matching(m: int = 7, fixed_base_vertex: int = 0) -> Matching:
    """Return the mate matching after deleting the pair containing the fixed point."""

    if m < 2:
        raise ValueError("m must be at least 2")
    pair_index = fixed_base_vertex // 2
    edges = []
    for p in range(m):
        if p == pair_index:
            continue
        edges.append((2 * p, 2 * p + 1))
    return canonical_matching(edges)


def matching_representative(
    partition: Sequence[int],
    m: int = 7,
    fixed_base_vertex: int = 0,
) -> Matching:
    """Construct a canonical perfect-matching representative for a partition.

    A part r uses r consecutive Q-edges and joins their endpoints in one
    alternating cycle of length 2r.  A part 1 is a matching edge shared with Q.
    """

    partition_tuple = tuple(int(x) for x in partition)
    if any(x <= 0 for x in partition_tuple):
        raise ValueError("partition parts must be positive")
    if sum(partition_tuple) != m - 1:
        raise ValueError(f"partition must sum to {m - 1}")

    q_edges = list(fixed_q_matching(m=m, fixed_base_vertex=fixed_base_vertex))
    result: list[tuple[int, int]] = []
    cursor = 0
    for size in partition_tuple:
        block = q_edges[cursor : cursor + size]
        if len(block) != size:
            raise AssertionError("partition overran the Q matching")
        # If block[i]=(a_i,b_i), add F-edges (b_i,a_{i+1}) cyclically.
        for i, (_, b_i) in enumerate(block):
            a_next, _ = block[(i + 1) % size]
            result.append(canonical_pair(b_i, a_next))
        cursor += size
    return canonical_matching(result)


def _involution(matching: Matching) -> dict[int, int]:
    mapping: dict[int, int] = {}
    for a, b in matching:
        if a in mapping or b in mapping:
            raise ValueError("not a matching")
        mapping[a] = b
        mapping[b] = a
    return mapping


def alternating_signature(matching: Matching, q_matching: Matching) -> tuple[int, ...]:
    """Return alternating-cycle half-lengths of matching union Q."""

    f = _involution(canonical_matching(matching))
    q = _involution(canonical_matching(q_matching))
    if set(f) != set(q):
        raise ValueError("the two matchings must use the same vertex set")

    unvisited = set(f)
    parts: list[int] = []
    while unvisited:
        start = min(unvisited)
        current = start
        component_vertices: set[int] = set()
        f_steps = 0
        while True:
            component_vertices.add(current)
            current = f[current]
            component_vertices.add(current)
            f_steps += 1
            current = q[current]
            if current == start:
                break
            if f_steps > len(f):
                raise RuntimeError("alternating traversal failed to close")
        unvisited.difference_update(component_vertices)
        parts.append(f_steps)
    return tuple(sorted(parts, reverse=True))


def enumerate_perfect_matchings(vertices: Sequence[int]) -> Iterator[Matching]:
    """Enumerate all perfect matchings of a small even vertex set."""

    remaining = tuple(vertices)
    if len(remaining) % 2:
        raise ValueError("vertex count must be even")
    if not remaining:
        yield ()
        return

    first = remaining[0]
    for i in range(1, len(remaining)):
        second = remaining[i]
        tail = remaining[1:i] + remaining[i + 1 :]
        for rest in enumerate_perfect_matchings(tail):
            yield canonical_matching(((first, second),) + rest)


def signature_counts(m: int = 7, fixed_base_vertex: int = 0) -> Counter[tuple[int, ...]]:
    """Count all perfect matchings by their alternating signature."""

    q = fixed_q_matching(m=m, fixed_base_vertex=fixed_base_vertex)
    vertices = sorted(vertex for edge in q for vertex in edge)
    return Counter(alternating_signature(f, q) for f in enumerate_perfect_matchings(vertices))


def wreath_group_permutations(m: int = 7, fixed_base_vertex: int = 0) -> Iterator[dict[int, int]]:
    """Generate C2 wr S_(m-1), acting on the surviving fixed pairs.

    This is intended for independent orbit audits.  For m=7 it yields 46,080
    permutations.
    """

    q_edges = list(fixed_q_matching(m=m, fixed_base_vertex=fixed_base_vertex))
    r = len(q_edges)
    for pair_permutation in permutations(range(r)):
        for flips in product((0, 1), repeat=r):
            mapping: dict[int, int] = {}
            for source_index, target_index in enumerate(pair_permutation):
                source = q_edges[source_index]
                target = q_edges[target_index]
                if flips[source_index]:
                    target = (target[1], target[0])
                mapping[source[0]] = target[0]
                mapping[source[1]] = target[1]
            yield mapping


def transform_matching(matching: Matching, permutation: dict[int, int]) -> Matching:
    """Apply a vertex permutation to a matching."""

    return canonical_matching((permutation[a], permutation[b]) for a, b in matching)


def orbit_of_representative(
    representative: Matching,
    m: int = 7,
    fixed_base_vertex: int = 0,
) -> set[Matching]:
    """Enumerate the full C2 wr S_(m-1) orbit of a representative."""

    return {
        transform_matching(representative, permutation)
        for permutation in wreath_group_permutations(m=m, fixed_base_vertex=fixed_base_vertex)
    }


def build_case_records(m: int = 7, fixed_base_vertex: int = 0) -> list[dict[str, object]]:
    """Build deterministic metadata for every normalized matching case."""

    counts = signature_counts(m=m, fixed_base_vertex=fixed_base_vertex)
    records: list[dict[str, object]] = []
    for number, partition in enumerate(integer_partitions(m - 1), start=1):
        representative = matching_representative(
            partition, m=m, fixed_base_vertex=fixed_base_vertex
        )
        signature = alternating_signature(
            representative,
            fixed_q_matching(m=m, fixed_base_vertex=fixed_base_vertex),
        )
        if signature != partition:
            raise AssertionError((partition, signature))
        records.append(
            {
                "case": number,
                "partition": list(partition),
                "representative_matching": [list(edge) for edge in representative],
                "orbit_size": counts[partition],
            }
        )
    return records
