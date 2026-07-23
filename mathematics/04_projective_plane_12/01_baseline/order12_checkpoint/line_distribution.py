#!/usr/bin/env python3
"""Exact line-type feasibility for ternary dual words of weights 15 and 18.

For a word with a plus-points and b minus-points, n[i,j] is the number of
ambient lines containing i plus-points and j minus-points. Orthogonality to
every line imposes i-j = 0 mod 3. The remaining equations count lines,
point-line incidences, and same/opposite-sign pairs.
"""
from __future__ import annotations

from math import comb
from z3 import Int, Or, Solver, Sum, sat


def distributions(weight: int) -> list[tuple[int, int, dict[tuple[int, int], int]]]:
    out: list[tuple[int, int, dict[tuple[int, int], int]]] = []
    for a in range(weight + 1):
        b = weight - a
        types = [
            (i, j)
            for i in range(a + 1)
            for j in range(b + 1)
            if i + j <= 13 and (i - j) % 3 == 0
        ]
        variables = {t: Int(f"n_{weight}_{a}_{t[0]}_{t[1]}") for t in types}
        s = Solver()
        s.add(*(x >= 0 for x in variables.values()))
        s.add(Sum(list(variables.values())) == 157)
        s.add(Sum(i * variables[i, j] for i, j in types) == 13 * a)
        s.add(Sum(j * variables[i, j] for i, j in types) == 13 * b)
        s.add(Sum(comb(i, 2) * variables[i, j] for i, j in types) == comb(a, 2))
        s.add(Sum(comb(j, 2) * variables[i, j] for i, j in types) == comb(b, 2))
        s.add(Sum(i * j * variables[i, j] for i, j in types) == a * b)
        while s.check() == sat:
            model = s.model()
            values = {t: model.eval(variables[t]).as_long() for t in types}
            out.append((a, b, {t: x for t, x in values.items() if x}))
            s.add(Or(*(variables[t] != values[t] for t in types)))
    return out


def weight18_parallel_class_refinement() -> tuple[int, ...]:
    # Let t be the number of concurrent parallel classes in either embedded
    # STS(9)=AG(2,3). If m=4-t nonconcurrent classes remain, each must pair
    # its three pair-intersection points with three distinct classes on the
    # opposite side. Hence either m=0 or m>=3.
    return tuple(t for t in range(5) if (4 - t == 0 or 4 - t >= 3))


w15 = distributions(15)
w18 = distributions(18)
assert w15 == []
assert w18 == [(9, 9, {(0, 0): 52, (0, 3): 12, (1, 1): 81, (3, 0): 12})]
assert weight18_parallel_class_refinement() == (0, 1, 4)

print("PASS")
print("weight 15: no integer line-type distribution")
print("weight 18: unique distribution")
print(w18[0])
print("Each sign class is an STS(9), uniquely AG(2,3).")
print("Refined number t of concurrent parallel classes: t in {0,1,4}.")
