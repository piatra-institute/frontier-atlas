# Degree-57 Moore graph: complete artifact bundle

Bundle date: 22 July 2026

This archive collects every artifact produced in the current research run on the hypothetical
strongly regular graph with parameters `(3250,57,0,1)`. It does **not** claim a complete
existence or nonexistence proof.

## Contents

- `original_prompt/` — the research prompt that defined the complete-resolution standard.
- `research_package/` — mathematical report, PDF report, source code, outputs, exact-cover
  instances for the base `PSL(3,4)` action, environment record, and checksums.
- `extension_instances/` — all 12 generated exact-cover instances for the four surviving
  `PSL(3,4)` extensions, plus original and portable metadata.
- `NEXT_STEPS.md` — prioritized continuation plan and exact remaining proof obligations.
- `scripts/verify_bundle.sh` — verifies all bundle hashes and the extension-instance hashes.
- `scripts/run_extension_branches.sh` — compiles the existing DLX solver and runs the 12
  extension instances, recording logs. This solver is exploratory: it does not yet emit a
  formal UNSAT certificate or a SAT witness row list.
- `MANIFEST.sha256` — SHA-256 digest of every file in the bundle except this manifest itself.
- `PACKAGE_INVENTORY.txt` — file names, byte sizes, and file types.

## Integrity note

The research directory arrived with an older `MANIFEST.sha256` whose hashes no longer matched
five files that had subsequently been revised. It is preserved as
`research_package/MANIFEST.prebundle.sha256`. A fresh, passing
`research_package/MANIFEST.sha256` and a bundle-wide `MANIFEST.sha256` were generated for this
archive.

## Verify

From the bundle root:

```bash
bash scripts/verify_bundle.sh
```

Or directly:

```bash
sha256sum -c MANIFEST.sha256
cd research_package && sha256sum -c MANIFEST.sha256
```

## Reproduce the verified base computations

```bash
cd research_package
python3 -m pip install numpy networkx
python3 verify_known_moore.py
python3 derive_constraints.py
python3 classify_primitive_groups.py
python3 psl_sharp_exact_cover.py --write-inputs .

g++ -O3 -std=c++17 dlx_exact_cover.cpp -o dlx_exact_cover
./dlx_exact_cover psl_exactcover_branch_0.txt
./dlx_exact_cover psl_exactcover_branch_1.txt
```

Expected base-branch results:

```text
branch 0: satisfiable=false nodes=2416 max_depth=8
branch 1: satisfiable=false nodes=2526 max_depth=11
```
