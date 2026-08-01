# Claim

## Claim

For standard index-1 uniform covering arrays over the alphabet \(\{0,1,2\}\),

\[
\boxed{\mathrm{CAN}(2,8,3)=13}.
\]

Specifically:

1. `array_CA_13_2_8_3.csv` is a \(\mathrm{CA}(13;2,8,3)\).
2. No \(\mathrm{CA}(12;2,8,3)\) exists.

This is an independent certification of a known exact value. It is not claimed as a new covering-array number or a new bound.

## Checker

Run from the package root:

```bash
./verify_all.sh
```

The script:

1. validates `ARTIFACT_MANIFEST.sha256`;
2. checks the 13-row array with a Python set-based scanner;
3. checks the same array with a separately written C++ bitmask scanner;
4. reconstructs all 165 positive \(3\times3\) pair-multiplicity matrices summing to 12;
5. independently reduces them to seven symmetry orbits;
6. independently enumerates all canonical ternary columns of length 12;
7. reconstructs and compares every candidate list and compatibility edge;
8. computes every compatibility graph's clique number by Bron-Kerbosch enumeration and verifies \(\omega<6\).

Pinned load-bearing artifact hashes:

```text
e1b9e381209be503a21463d794fe18447a9d887e0580b0f920bc92026a3cee1f  array_CA_13_2_8_3.csv
b5a26b11d1158562a92e98d71a6536e150ecac3d07abfc19b095e02ae92c1ffd  certificate/lower_bound_summary.json
```

Toolchain versions are recorded in `TOOL_VERSIONS.txt`. The generation environment used Python 3.13.5 and g++ 14.2.0.

## Trust base

Load-bearing components:

- exact integer arithmetic;
- exhaustive finite enumeration;
- standard C++17 and Python 3 language/runtime semantics;
- SHA-256 as implemented by GNU coreutils 9.7;
- the human-auditable normalization argument in `PROOF_NOTE.md`;
- two independently written implementations for the upper certificate;
- two algorithmically different implementations for the lower certificate.

Not load-bearing:

- simulated annealing used to discover the 13-row witness;
- floating-point temperatures in heuristic searches;
- prior literature's classification output;
- the exploratory \(\mathrm{CAN}(3,7,3)\) branch.

No SAT solver, DRAT/LRAT checker, integer-programming oracle, randomized primality test, or floating-point optimization result is trusted for the claim. The lower certificate is a completed exact enumeration, not a DRAT/LRAT trace.

The normalization argument is not formalized in a proof assistant. That small mathematical argument and the source code are the remaining human review surface.

## Encoding fidelity

For any hypothetical \(\mathrm{CA}(12;2,8,3)\), choose two columns. Their ordered-pair frequency matrix is a positive \(3\times3\) integer matrix summing to 12. The generator and independent verifier enumerate all 165 such matrices and quotient them under independent symbol permutations and transposition, obtaining seven canonical cases.

After row-order normalization, every possible additional column is included. Independent symbol relabeling in that column gives a unique first-occurrence, restricted-growth representative. A vertex is retained exactly when it covers all nine pairs with both fixed columns. Two vertices are connected exactly when their columns cover all nine ordered pairs together.

The six remaining columns of a putative eight-column array therefore exist exactly when one of the seven graphs contains \(K_6\). Their independently verified clique numbers are

```text
2, 3, 3, 3, 3, 4, 5
```

so no \(K_6\) exists. `PROOF_NOTE.md` gives the complete equivalence argument and explains why symbol-canonicalization cannot merge two compatible columns.

## Review level

`agent`

No human or community review has yet been recorded.

## Provenance

- The model selected \(\mathrm{CAN}(2,8,3)=13\) as a nontrivial P2 target after checking current table availability and the published exact result.
- The model designed the multiplicity-matrix and compatibility-graph reduction.
- `src/generate_certificate.cpp` generated the seven cases, all candidate and edge files, and the fixed-size clique results.
- `src/verify_lower_bound_independent.py` independently reconstructed the search by decoding all \(3^{12}\) ternary words and used Bron-Kerbosch maximal-clique enumeration.
- `src/search_upper_CA13.py`, seed 123, found the preserved upper witness at restart 1, step 256,894.
- The two coverage checkers independently confirmed all 252 required pair interactions.

The checker confirmed the mathematical artifacts. It did not independently verify the literature-status narrative.

## Cost and attempts

Exact claim computation on the recorded five-core Linux container:

- certificate generation: 0.158580 s;
- independent lower-bound verification: 4.066373 s;
- deterministic upper-witness search reproduction: 1.507911 s;
- two independent upper coverage scans: under 0.1 s each in this environment.

Attempt denominator:

1. one SAT/DRAT route was evaluated and abandoned before a solver run because no certified SAT solver and proof checker were installed and package retrieval was unavailable;
2. one exact symmetry-normalized enumeration route succeeded;
3. one deterministic simulated-annealing upper search succeeded after two restarts, with the solution in restart 1;
4. one neighboring \(N=39,t=3,k=7,v=3\) min-conflicts validation succeeded in 0.607070 s;
5. six recorded \(N=38,t=3,k=7,v=3\) exploratory seeds found no witness; their best states had five uncovered interactions. One run had a 10 s standalone budget and five were parallel time-limited runs. Precise aggregate CPU time for the sandbox-killed parallel jobs was not exposed, so it is not fabricated.

External paid compute: none. Compute beyond a single workstation: none. Total model-token or monetary spend is not exposed to this runtime and is therefore recorded as unavailable.
