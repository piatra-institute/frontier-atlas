# Prioritized next steps

## 1. Independent encoding audit

Implement a second generator in another language or proof assistant and compare normalized instance hashes after canonical variable renaming. The critical obligations are:

- block reduction equivalence;
- all 11 orbit cases cover the full point-star matching space;
- case-fixing clauses are equisatisfiable;
- common-neighbor constraints implement the exact quadratic equation.

## 2. Proof-producing baseline runs

Generate each of the 11 OPB cases and use a solver that emits independently checkable pseudo-Boolean proofs. Solver termination without a certificate is not a theorem.

Suggested artifact layout:

```text
certificates/
  case_01/
    model.opb
    proof.pbp
    checker.txt
    SHA256SUMS
  ...
  case_11/
```

## 3. Benchmark alternative encodings

Compare at least three exact formulations on reduced or partially fixed instances:

1. adjacency plus common-neighbor conjunction variables;
2. point-star matchings plus 140 triangle-selection variables;
3. integral `+15` lift variables for the projector matrix `G`.

Measure propagation, learned constraints, proof size, and symmetry reduction. Raw variable count alone is not sufficient.

## 4. Canonical augmentation

Build the 14 point-star perfect matchings incrementally. At every stage:

- canonicalize under the surviving subgroup of `S2 wr S7`;
- reject duplicate partial structures;
- enforce upper bounds on common neighbors;
- enforce residual degree feasibility;
- enforce residual triangle-incidence feasibility;
- apply exact modular-rank and principal-minor tests.

## 5. Structural target: the forced 2-factor

Classify possible cycle decompositions of the 84-edge 2-factor `H` under the 140-triangle constraints. Useful subtargets include:

- rule out short cycles or specific combinations of cycle lengths;
- derive intersection restrictions between `B[S_u]` and `B[S_v]`;
- determine whether the triangle incidence matrix has a forced Gram matrix;
- identify an integral or modular contradiction attached to a cycle type.

A lemma eliminating one normalized orbit or one family of 2-factor cycle types would constitute genuine progress.

## 6. Positive search remains necessary

Do not assume nonexistence. In parallel with proof-oriented exclusion, search structured construction families such as voltage graphs, lifts, block-circulant matrices, and algebraically generated projector subspaces. Every candidate must pass `verify_B` and the reconstructed `verify_A` exactly.
