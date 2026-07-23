# Conway-99 fixed-vertex research package

This repository reconstructs the rigorous mathematical and computational artifacts retained from the investigation of the existence of a strongly regular graph

\[
\operatorname{srg}(99,14,1,2).
\]

## Status

**UNRESOLVED.** The repository contains neither:

1. a verified `99 x 99` adjacency matrix, nor
2. a complete, independently checked nonexistence certificate.

It therefore does not solve Conway's 99-graph problem. See [`STATUS.md`](STATUS.md).

The package does contain:

- a lossless reduction to a binary symmetric `84 x 84` matrix `B`;
- independent exact verifiers for `B` and the reconstructed `99 x 99` matrix `A`;
- a complete audit of the 11 normalized point-star matching cases;
- a dependency-free exact pseudo-Boolean (`.opb`) generator;
- a small `m=2` instance solved completely by brute force, used to validate the reduction and encoding;
- the integral-projector reformulation `G^2 = 105 G`;
- deterministic tests, audit output, case manifests, and hashes;
- the original research prompt.

## Provenance warning

These files were **reconstructed after the exploratory runtime ended** from the derivations preserved in the conversation. They are not a byte-for-byte recovery of the temporary scripts used during the earlier run. The exact provenance is documented in [`docs/artifact_provenance.md`](docs/artifact_provenance.md).

## Mathematical core

Fix a vertex `x`. Its 14 neighbors induce `7K2`. Label those neighbors `0,...,13`, paired by

```text
(0,1), (2,3), ..., (12,13).
```

The 84 vertices at distance two from `x` are canonically indexed by the edges of

\[
C=K_{14}-7K_2=K_{2,2,2,2,2,2,2}.
\]

Let:

- `L` be the adjacency matrix of `7K2`;
- `T = J - I - L`, the adjacency matrix of `C`;
- `M` be the unsigned `84 x 14` edge-vertex incidence matrix of `C`;
- `B` be the unknown adjacency matrix on the 84 distance-two vertices.

Then

\[
A=
\begin{pmatrix}
0 & \mathbf 1^T & 0\\
\mathbf 1 & L & M^T\\
0 & M & B
\end{pmatrix}
\]

is an `srg(99,14,1,2)` exactly when `B` is binary, symmetric, zero-diagonal, and

\[
BM=MT,
\]

\[
B^2=12I-B-MM^T+2J.
\]

See [`docs/reduction.md`](docs/reduction.md) for the complete derivation.

## Installation

Python 3.11 or later is recommended.

```bash
cd conway99_research_package
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
```

Only NumPy is required for the core package.

## Run the full audit

```bash
python -m unittest discover -s tests -v
python scripts/generate_cases.py
python scripts/generate_examples.py
python scripts/run_audit.py
python scripts/hash_tree.py
```

Or:

```bash
make audit
```

Expected high-level results:

```text
UNRESOLVED
84 second-layer vertices
11 normalized matching cases
10,395 labeled point-star perfect matchings covered
m=2 reduced and full exact checks: PASS
projector baseline cross-check: PASS
full normalized OPB size: 289,338 variables, 862,284 constraints
```

## Verify a candidate

Reduced matrix `B`:

```bash
python scripts/verify_candidate.py B candidate_B.csv
```

Full adjacency matrix `A`:

```bash
python scripts/verify_candidate.py A candidate_A.csv
```

Integral-projector matrix `G`:

```bash
python scripts/verify_candidate.py G candidate_G.csv
```

The verifier checks exact integer equations, not floating-point spectra.

## Generate a normalized Conway case

The 11 case signatures are the partitions of 6. For example:

```bash
python -m conway99 generate-opb generated/case_3_2_1.opb \
  --partition 3+2+1 \
  --metadata generated/case_3_2_1.metadata.json
```

The full file is large. One normalized case contains:

| Item | Count |
|---|---:|
| `x` adjacency variables | 3,486 |
| `y` conjunction variables | 285,852 |
| Total variables | 289,338 |
| Incidence equalities | 1,176 |
| AND linearization constraints | 857,556 |
| Common-neighbor equalities | 3,486 |
| Case-fixing constraints | 66 |
| Total constraints | 862,284 |

The included `examples/m2_case_1.opb` is a small complete audit instance.

## Directory map

```text
prompt/       original uploaded research prompt
docs/         derivations, projector viewpoint, next steps, provenance
src/          reusable Python package
scripts/      deterministic generators, verifiers, audit and hashing
cases/        all 11 normalized case records and manifest
tests/        unit and exhaustive small-instance audits
examples/     completely solved m=2 analogue and OPB example
results/      audit reports and SHA-256 manifest
```

## What remains

A solution requires one of the following:

- find a binary `B` satisfying both exact reduced equations, then publish `B`, reconstructed `A`, hashes, and at least two independent verifiers;
- prove all 11 normalized cases unsatisfiable using proof-producing solvers or a complete structural theorem, then independently validate every proof and the case cover.

The most promising research direction retained here is the integral-projector formulation described in [`docs/projector_formulation.md`](docs/projector_formulation.md).
