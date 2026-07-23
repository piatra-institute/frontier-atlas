# Exact verification package: a 604-point code in dimension 11

## Result status

This package **does not determine the exact 11-dimensional kissing number**. It verifies the exact lower bound `tau_11 >= 604` and proves a stronger local theorem about that particular construction:

> Let `C` be the reconstructed antipodal 604-point code, written with vectors of squared norm 4. Its polar at kissing threshold 2 is
> `P(C) = { y in R^11 : |<v,y>| <= 2 for every v in C }`.
> Then `max_{y in P(C)} ||y||^2 = 3`.

Consequently, no vector of squared norm 4 can be adjoined to `C`. The code is geometrically saturated, with an exact squared-norm gap of `4 - 3 = 1`.

Saturation of one fixed code is not a universal upper bound: a different 605-point code need not contain this 604-point code.

## One-command verification

```bash
./verify_all.sh
```

The proof checkers use only Python's standard library. They do not use floating-point arithmetic for mathematical checks.

## Main files

- `construction_604.json`: exact coordinates in `Q(sqrt(2))`.
- `generate_604.py`: deterministic generator for the construction.
- `verify_604.py`: exact norms, all 182,106 pairwise inequalities, distinctness, antipodality, frame operator, and rank.
- `certificates/*.json`: five exact Handelman certificates covering all chamber orbits.
- `verify_saturation_604.py`: independent exact expansion and chamber-cover verifier.
- `verification_604.json`: construction audit report.
- `verification_saturation_604.json`: saturation audit report.
- `RESULT.md`: human-readable derivation and exact remaining gap.
- `MANIFEST.sha256`: hashes for every immutable package file.

## Coordinate convention

Each stored coordinate `[a,b]` means

`(a + b*sqrt(2))/3`.

Every constructed vector has squared norm 4. Dividing every vector by 2 produces unit vectors with pairwise inner products at most `1/2`.
