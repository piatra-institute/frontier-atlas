# Projective plane of order 12: rigorous research checkpoint

## Status

**This package does not resolve existence or nonexistence.** No 157 x 157 incidence matrix was constructed, and no complete nonexistence certificate was obtained. The order-12 problem remains open in the literature checked through 21 July 2026.

The package preserves the strongest exact deductions reached in this run, together with executable checkers. Its main contribution is a universal ternary-code reduction that applies even when a hypothetical plane has trivial automorphism group.

## Exact conditional theorem

Assume a projective plane of order 12 exists, with incidence matrix `N`.

1. `|det N| = 13*12^78`, `N^{-1}=(13N^T-J)/156`, and every Smith invariant divides 156.
2. `rank_F3(N)=79` and `rank_F13(N)=156`.
3. Let `C` be the ternary row code and `D=C^perp`. Then:
   - `C` has parameters `[157,79,13]_3`;
   - `D` has parameters `[157,78,d]_3` with `d >= 18`;
   - the only weight-13 words of `C` are the 314 signed line vectors.
4. The plane induces a ternary Type-III self-dual `[160,80]` code with exactly:
   - 2 words of weight 3;
   - 0 words of weights 6, 9, and 12;
   - 942 words of weight 15.
5. If `D` has a word of weight 18, its plus/minus supports each have 9 points and the line distribution is uniquely
   `52*(0,0) + 12*(3,0) + 81*(1,1) + 12*(0,3)`.
   Each sign support is an embedded `STS(9)`, hence an affine plane `AG(2,3)`. The number of concurrent parallel classes on either side is restricted to `0`, `1`, or `4`.

The report gives proofs. `line_distribution.py`, `verify_gleason.py`, and `verify_macwilliams_rational.py` independently check the exact finite calculations.

## Reproduce

```bash
python -m venv .venv
. .venv/bin/activate              # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python run_all.py
```

`run_all.py` first generates known planes `PG(2,3)` and `PG(2,5)` and validates them with two independent incidence verifiers. It then runs all order-12 conditional checks.

To test a proposed order-12 matrix:

```bash
python verify_incidence.py candidate.json --order 12
python verify_incidence_independent.py candidate.json --order 12
```

JSON may be a raw matrix or an object with a `matrix` field. CSV is also accepted.

## Important negative checks

Two tempting contradiction claims failed exact audit:

- Ordinary one-variable Gleason constraints are compatible with the forced self-dual-code coefficients. `verify_gleason.py` constructs a formal nonnegative enumerator. This is not a code construction.
- The rational MacWilliams linear program for `D` and `C=D^perp` is exactly feasible. A floating-point infeasibility report would therefore be spurious. The exact rational certificate is in `certificates/`.

## Files

- `REPORT.md`: mathematical derivations and the exact unresolved gap.
- `verify_incidence.py`, `verify_incidence_independent.py`: candidate-plane validators.
- `generate_pg2_prime.py`: known-prime-order test generator.
- `verify_algebra.py`: determinant, inverse, rank, and Smith constraints.
- `line_distribution.py`: exact Z3 enumeration for weights 15 and 18.
- `verify_gleason.py`: formal Type-III Hamming enumerator check.
- `verify_macwilliams_rational.py`: exact Fraction-based certificate checker.
- `source/`: the supplied prompt.
