# Degree-57 Moore graph: verified research package

This package records exact reductions and finite exclusions for the hypothetical Moore graph
with parameters `(3250,57,0,1)`. It does **not** claim a complete existence or nonexistence
proof.

## Strongest verified result

The rooted matching permutations generate a primitive group on 56 labels. The complete
primitive-group classification reduces that group to seven actions after the representation
test, and an exact-cover computation then excludes the base `PSL(3,4)` action. The six
remaining possible generated groups are:

```text
PSL(3,4).2_3, PSL(3,4).2_1, PSL(3,4).2_2,
PSL(3,4).2^2, Alt(56), Sym(56).
```

## Main contents

- `REPORT.md` - full mathematical derivation and exact remaining gap.
- `Moore57_verified_report.pdf` - typeset version of the report.
- `verify_known_moore.py` - exact regression checks on degrees 2, 3, and 7.
- `derive_constraints.py` - exact spectra, character multiplicities, and primitivity arithmetic.
- `primgrp_degree56_excerpt.g` - official PrimGrp 4.0.2 degree-56 data excerpt.
- `group_tools.py` - exact permutation parser and enumerator.
- `classify_primitive_groups.py` - verifies all nine primitive degree-56 actions and eliminates
  the `Alt(8)` and `Sym(8)` actions.
- `psl_sharp_exact_cover.py` - derives the `PSL(3,4)` class constraints, generates the two
  exhaustive branches, and proves both unsatisfiable with a Python bitset solver.
- `psl_exactcover_branch_0.txt`, `psl_exactcover_branch_1.txt` - canonical finite instances.
- `dlx_exact_cover.cpp` - independent C++ dancing-links verifier.
- `regular_group_obstruction.md` - standalone proof excluding every semiregular group cover.
- `RESULTS.json` - machine-readable summary.
- `MANIFEST.sha256` - package hashes.

## Reproduce

```bash
python3 -m pip install numpy networkx
python3 verify_known_moore.py
python3 derive_constraints.py
python3 classify_primitive_groups.py
python3 psl_sharp_exact_cover.py --write-inputs .

g++ -O3 -std=c++17 dlx_exact_cover.cpp -o dlx_exact_cover
./dlx_exact_cover psl_exactcover_branch_0.txt
./dlx_exact_cover psl_exactcover_branch_1.txt

sha256sum -c MANIFEST.sha256
```

All defining identities and search decisions are exact. Floating-point eigenvalue routines in
the known-graph regression script are used only for redundant printed diagnostics after exact
integer identities pass.
