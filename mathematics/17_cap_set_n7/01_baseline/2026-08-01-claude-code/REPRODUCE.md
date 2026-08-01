# Reproduce

Toolchain: Python 3.12.4, scipy 1.14.1 (HiGHS LP). The `caps` target additionally
needs OR-tools CP-SAT (`pip install ortools`); `verify-fast` and `lower` do not.

```bash
make verify-fast      # independent staircase reproduction, self-checking (< 1 s)
make lower            # honest lower-bound search, ~25 s, seed 20260801
make caps             # CP-SAT: proves a(4) <= 20 (~7 s); a(5), a(6) not closed in budget
make sat              # certified a(4) <= 20 with a drat-trim VERIFIED proof (~17 s)
make check-manifest   # verify every file against SHA256SUMS
```

The `sat` target needs `cadical` on PATH (`brew install cadical`) and builds
`tools/drat-trim` from source (`tools/drat-trim.c`, MIT, from Marijn Heule's
drat-trim). It writes DRAT proofs under `proofs/`; the `.drat` files are large and
git-ignored (regenerable), while the `.cnf` inputs and the drat-trim VERIFIED
verdict in `certificates/sat_bounds.json` are the tracked evidence.

`verify-fast` regenerates `certificates/staircase_{291,290,289,288}.json` and
asserts every claimed number: the moment identities (1093/364/121), the forced
exceptional profile sets, the aggregate slacks, the minimum forced-direction
counts, and an exact-integer LP separator that is independent of the published
coefficients.

## Layout
```
src/verify_staircase.py     independent staircase reducer + LP separator search
src/lower_bound_search.py   randomized greedy + local repair lower-bound attempt
certificates/staircase_*.json   regenerated per-size reduction certificates
data/cf236.csv              the 236-cap (copied from the sibling chatgpt-pro run)
logs/                       captured run output
report.md  CLAIM.md         findings and the audit surface
```

## Scope
This run verifies and reduces; it does not prove a new bound. See `report.md`.
Determining a(7), or beating 236 (lower) or 288 (upper), needs an exact solver
and the profile-elimination SAT runs described in the report's next steps.
