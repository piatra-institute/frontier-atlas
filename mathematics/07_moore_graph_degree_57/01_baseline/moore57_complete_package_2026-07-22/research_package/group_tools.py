#!/usr/bin/env python3
"""Small exact permutation-group utilities for the bundled degree-56 PrimGrp data."""

from __future__ import annotations

from collections import deque
from pathlib import Path
import re
from typing import Iterable

N = 56
DEFAULT_DATA = Path(__file__).with_name("primgrp_degree56_excerpt.g")
Permutation = tuple[int, ...]


def split_top(text: str) -> list[str]:
    out: list[str] = []
    bracket_depth = 0
    paren_depth = 0
    in_string = False
    start = 0
    for i, ch in enumerate(text):
        if in_string:
            if ch == '"':
                in_string = False
            continue
        if ch == '"':
            in_string = True
        elif ch == '[':
            bracket_depth += 1
        elif ch == ']':
            bracket_depth -= 1
        elif ch == '(':
            paren_depth += 1
        elif ch == ')':
            paren_depth -= 1
        elif ch == ',' and bracket_depth == 0 and paren_depth == 0:
            out.append(text[start:i].strip())
            start = i + 1
    out.append(text[start:].strip())
    return out


def load_entries(path: Path | str = DEFAULT_DATA) -> list[str]:
    text = Path(path).read_text(encoding="utf-8")
    marker = "PRIMGRP[56]:="
    if marker not in text:
        raise ValueError(f"Missing {marker} in {path}")
    block = text[text.index(marker) :]
    outer = block[block.index('[') : block.rfind(';')]
    entries: list[str] = []
    depth = 0
    start: int | None = None
    in_string = False
    escaped = False
    for i, ch in enumerate(outer):
        if in_string:
            if escaped:
                escaped = False
            elif ch == '\\':
                escaped = True
            elif ch == '"':
                in_string = False
            continue
        if ch == '"':
            in_string = True
        elif ch == '[':
            depth += 1
            if depth == 2:
                start = i
        elif ch == ']':
            if depth == 2 and start is not None:
                entries.append(outer[start : i + 1])
                start = None
            depth -= 1
    if len(entries) != 9:
        raise AssertionError(f"Expected 9 primitive groups of degree 56, found {len(entries)}")
    return entries


def metadata(path: Path | str = DEFAULT_DATA) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for entry in load_entries(path):
        fields = split_top(entry[1:-1])
        order_expr = fields[1]
        order = int(order_expr) if order_expr.isdigit() else order_expr
        subdegrees = [(int(a), int(b)) for a, b in re.findall(r'\[\s*(\d+)\s*,\s*(\d+)\s*\]', fields[4])]
        rows.append(
            {
                "index": int(fields[0]),
                "order": order,
                "subdegrees": subdegrees,
                "description": fields[6].strip('"'),
                "raw_fields": fields,
            }
        )
    return rows


def parse_perm(cycle_text: str, n: int = N) -> Permutation:
    p = list(range(n))
    for cycle in re.findall(r'\(([^()]*)\)', cycle_text):
        points = [int(x) - 1 for x in re.findall(r'\d+', cycle)]
        if len(points) >= 2:
            for x, y in zip(points, points[1:] + points[:1]):
                p[x] = y
    return tuple(p)


def inverse(p: Permutation) -> Permutation:
    q = [0] * len(p)
    for i, image in enumerate(p):
        q[image] = i
    return tuple(q)


def compose(p: Permutation, q: Permutation) -> Permutation:
    """Return p after q."""
    return tuple(p[q[i]] for i in range(len(p)))


def enumerate_group(generators: Iterable[Permutation], expected_order: int | None = None) -> list[Permutation]:
    moves: list[Permutation] = []
    for g in generators:
        moves.extend((g, inverse(g)))
    identity = tuple(range(N))
    seen = {identity}
    queue: deque[Permutation] = deque([identity])
    while queue:
        x = queue.popleft()
        for g in moves:
            y = compose(g, x)
            if y not in seen:
                seen.add(y)
                queue.append(y)
                if expected_order is not None and len(seen) > expected_order:
                    raise AssertionError("Generated group exceeded expected order")
    if expected_order is not None and len(seen) != expected_order:
        raise AssertionError(f"Expected order {expected_order}, obtained {len(seen)}")
    return sorted(seen)


def load_group(index: int, path: Path | str = DEFAULT_DATA) -> tuple[dict[str, object], list[Permutation], list[Permutation]]:
    rows = metadata(path)
    row = rows[index - 1]
    fields = row["raw_fields"]
    assert isinstance(fields, list)
    order = row["order"]
    if not isinstance(order, int):
        raise ValueError(f"Group {index} is represented symbolically and cannot be enumerated here")
    generator_field = fields[-1]
    generator_texts = split_top(generator_field[1:-1])
    generators = [parse_perm(text) for text in generator_texts]
    group = enumerate_group(generators, order)
    return row, generators, group


def fixed_points(p: Permutation) -> int:
    return sum(i == image for i, image in enumerate(p))


def is_derangement(p: Permutation) -> bool:
    return fixed_points(p) == 0


def cycle_type(p: Permutation) -> tuple[int, ...]:
    seen = [False] * len(p)
    lengths: list[int] = []
    for i in range(len(p)):
        if seen[i]:
            continue
        j = i
        length = 0
        while not seen[j]:
            seen[j] = True
            length += 1
            j = p[j]
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def conjugacy_classes(group: Iterable[Permutation], generators: Iterable[Permutation]) -> list[list[Permutation]]:
    moves: list[Permutation] = []
    for g in generators:
        moves.extend((g, inverse(g)))
    unseen = set(group)
    classes: list[list[Permutation]] = []
    while unseen:
        x = min(unseen)
        orbit = {x}
        queue: deque[Permutation] = deque([x])
        while queue:
            y = queue.popleft()
            for s in moves:
                z = compose(compose(s, y), inverse(s))
                if z not in orbit:
                    orbit.add(z)
                    queue.append(z)
        unseen.difference_update(orbit)
        classes.append(sorted(orbit))
    classes.sort(key=lambda cls: cls[0])
    return classes


def point_suborbits(group: Iterable[Permutation], point: int = 0) -> list[list[int]]:
    stabilizer = [g for g in group if g[point] == point]
    unseen = set(range(N))
    orbits: list[list[int]] = []
    while unseen:
        y = min(unseen)
        orbit = {h[y] for h in stabilizer}
        unseen.difference_update(orbit)
        orbits.append(sorted(orbit))
    orbits.sort(key=lambda x: (len(x), x))
    return orbits
