#!/usr/bin/env python3
"""Exact arithmetic checks for the degree-57 Moore graph reductions."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class Spectrum:
    eigenvalue: int
    multiplicity: int


def solve_two_eigenvalue_multiplicities(
    dimension: int, trace: int, positive: int, negative: int
) -> tuple[Fraction, Fraction]:
    """Solve a+b=dimension and positive*a+negative*b=trace exactly."""
    a = Fraction(trace - negative * dimension, positive - negative)
    b = Fraction(positive * dimension - trace, positive - negative)
    return a, b


def full_graph() -> list[Spectrum]:
    # A has eigenvalues 57 on the all-one vector and roots 7,-8 elsewhere.
    a, b = solve_two_eigenvalue_multiplicities(3249, -57, 7, -8)
    assert a.denominator == b.denominator == 1
    return [Spectrum(57, 1), Spectrum(7, int(a)), Spectrum(-8, int(b))]


def rooted_cover() -> list[Spectrum]:
    # On fibre-constant vectors: 56^1 and (-1)^56.
    # On the 3135-dimensional fibre-sum-zero space: roots 7,-8, trace 56.
    # The trace of C is zero, so the residual trace after 56 + 56*(-1) is zero.
    a, b = solve_two_eigenvalue_multiplicities(3135, 0, 7, -8)
    assert a.denominator == b.denominator == 1
    return [Spectrum(56, 1), Spectrum(7, int(a)), Spectrum(-1, 56), Spectrum(-8, int(b))]


def compressed_matrix() -> list[Spectrum]:
    # B has order 56^2. The all-one eigenvalue is 56; two quotient spaces give
    # zero with total multiplicity 110. The remaining 3025-dimensional space has
    # eigenvalues 8,-7 and trace 3136-56=3080.
    a, b = solve_two_eigenvalue_multiplicities(3025, 3080, 8, -7)
    assert a.denominator == b.denominator == 1
    return [Spectrum(56, 1), Spectrum(8, int(a)), Spectrum(0, 110), Spectrum(-7, int(b))]


def regular_group_character_test(character_degree: int = 1) -> tuple[Fraction, Fraction]:
    # A nontrivial irreducible character of degree d yields a 57d-dimensional block
    # with roots 7,-8 and trace zero.
    return solve_two_eigenvalue_multiplicities(57 * character_degree, 0, 7, -8)


def main() -> None:
    print("Full graph spectrum:", full_graph())
    print("Rooted distance-two graph spectrum:", rooted_cover())
    print("Compressed B spectrum:", compressed_matrix())

    a, b = regular_group_character_test(1)
    print("Linear-character multiplicities:", a, b)
    assert a.denominator != 1 or b.denominator != 1
    print("Contradiction: a one-dimensional nontrivial character is impossible.")

    print("\nGeneral constituent divisibility test (degrees 1..60):")
    allowed = []
    for d in range(1, 61):
        x, y = regular_group_character_test(d)
        if x.denominator == y.denominator == 1:
            allowed.append(d)
    print("Allowed degrees:", allowed)
    assert allowed == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
    print("Therefore every nontrivial constituent of the 56-point permutation module must have degree divisible by 5.")

    proper_block_counts = [2, 4, 7, 8, 14, 28]
    block_module_dimensions = [m - 1 for m in proper_block_counts]
    print("\nPossible proper block counts in degree 56:", proper_block_counts)
    print("Block-constant zero-sum dimensions:", block_module_dimensions)
    assert all(d % 5 != 0 for d in block_module_dimensions)
    print("Therefore the generated transitive matching group must be primitive.")


if __name__ == "__main__":
    main()
