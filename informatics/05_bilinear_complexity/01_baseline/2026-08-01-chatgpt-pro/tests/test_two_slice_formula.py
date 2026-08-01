#!/usr/bin/env python3
"""Exhaustively validate the F2 two-slice rank formula on all 2x2x2 tensors."""
from collections import deque


def matrix_rank_2x2(m: int) -> int:
    rows = [m & 3, (m >> 2) & 3]
    if rows == [0, 0]:
        return 0
    if rows[0] == 0 or rows[1] == 0 or rows[0] == rows[1]:
        return 1
    return 2


def outer2(u: int, v: int) -> int:
    return (v if u & 1 else 0) | ((v if u & 2 else 0) << 2)


terms = set()
for a in (1, 2, 3):
    for u in (1, 2, 3):
        for v in (1, 2, 3):
            m = outer2(u, v)
            state = (m if a & 1 else 0) | ((m if a & 2 else 0) << 4)
            terms.add(state)

# Exact tensor ranks by BFS in the additive group F2^8.
distance = [-1] * 256
distance[0] = 0
queue = deque([0])
while queue:
    state = queue.popleft()
    for term in terms:
        nxt = state ^ term
        if distance[nxt] < 0:
            distance[nxt] = distance[state] + 1
            queue.append(nxt)

assert all(d >= 0 for d in distance)
for state in range(256):
    m0, m1 = state & 15, state >> 4
    formula = min(
        matrix_rank_2x2(z)
        + matrix_rank_2x2(m0 ^ z)
        + matrix_rank_2x2(m1 ^ z)
        for z in range(16)
    )
    assert formula == distance[state], (state, formula, distance[state])

print(f"FORMULA TEST OK: all 256 tensors; {len(terms)} nonzero rank-one generators")
