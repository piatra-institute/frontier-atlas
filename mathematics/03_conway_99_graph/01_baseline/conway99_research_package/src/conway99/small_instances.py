"""Small generalized instances used to audit the reduction and encoding."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
from math import isqrt
from typing import Iterator

import numpy as np
from numpy.typing import NDArray

from .model import build_model
from .verify import verify_B

IntMatrix = NDArray[np.int64]


def brute_force_reduced_solutions(m: int) -> Iterator[IntMatrix]:
    """Brute-force all reduced B matrices for tiny m.

    The routine refuses instances with more than 24 binary variables.  It is
    intended as an independent audit, not as a Conway-99 search engine.
    """

    model = build_model(m)
    q = model.second_layer_count
    pairs = list(combinations(range(q), 2))
    if len(pairs) > 24:
        raise ValueError(
            f"brute-force guard: m={m} needs {len(pairs)} variables (>24)"
        )

    for bits in product((0, 1), repeat=len(pairs)):
        B = np.zeros((q, q), dtype=np.int64)
        for bit, (i, j) in zip(bits, pairs):
            B[i, j] = bit
            B[j, i] = bit
        if verify_B(B, m=m, verify_full=True).valid:
            yield B


def m2_unique_solution() -> IntMatrix:
    """Return the unique labeled reduced solution for m=2."""

    solutions = list(brute_force_reduced_solutions(2))
    if len(solutions) != 1:
        raise AssertionError(f"expected one labeled m=2 solution, found {len(solutions)}")
    return solutions[0]


def spectral_feasibility(m: int) -> dict[str, object]:
    """Check the elementary eigenvalue-multiplicity feasibility condition.

    For parameters (1+2m^2, 2m, 1, 2), the two restricted eigenvalues solve
    x^2+x+2-2m=0.  This routine reports exact rational multiplicities when the
    discriminant is a square and detects the conjugate-multiplicity obstruction
    otherwise.
    """

    if m < 2:
        raise ValueError("m must be at least 2")
    v = 1 + 2 * m * m
    k = 2 * m
    discriminant = 8 * m - 7
    root = isqrt(discriminant)
    if root * root == discriminant:
        r = Fraction(-1 + root, 2)
        s = Fraction(-1 - root, 2)
        f = Fraction(-k - (v - 1) * s, r - s)
        g = (v - 1) - f
        feasible = f.denominator == 1 and g.denominator == 1 and f >= 0 and g >= 0
        return {
            "m": m,
            "parameters": [v, k, 1, 2],
            "discriminant": discriminant,
            "eigenvalues": [str(r), str(s)],
            "multiplicities": [str(f), str(g)],
            "feasible": bool(feasible),
            "reason": "integral multiplicities" if feasible else "nonintegral multiplicities",
        }

    # With irrational conjugate roots, an integer characteristic polynomial
    # forces equal multiplicities.  The trace would then be k-(v-1)/2.
    equal_multiplicity = (v - 1) // 2
    trace_if_equal = k - equal_multiplicity
    feasible = trace_if_equal == 0
    return {
        "m": m,
        "parameters": [v, k, 1, 2],
        "discriminant": discriminant,
        "eigenvalues": [f"(-1+sqrt({discriminant}))/2", f"(-1-sqrt({discriminant}))/2"],
        "forced_equal_multiplicity": equal_multiplicity,
        "trace_if_equal": trace_if_equal,
        "feasible": feasible,
        "reason": (
            "irrational conjugates can have equal multiplicity with zero trace"
            if feasible
            else "irrational conjugates force equal multiplicity, contradicting trace zero"
        ),
    }
