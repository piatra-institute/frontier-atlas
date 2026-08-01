# Exact certificate for \(\mathrm{CAN}(2,8,3)=13\)

## Result

The artifacts certify both halves:

1. `array_CA_13_2_8_3.csv` is a \(\mathrm{CA}(13;2,8,3)\).
2. No \(\mathrm{CA}(12;2,8,3)\) exists.

Therefore

\[
\boxed{\mathrm{CAN}(2,8,3)=13}.
\]

This is an independent reproduction of a known exact value, not a new table entry.

## Upper bound

For each of the \(\binom{8}{2}=28\) column pairs, both independent coverage scanners verify that all nine ordered pairs in \(\{0,1,2\}^2\) occur. The 252 pair-tuple obligations have multiplicities between 1 and 3 in the supplied 13-row array.

The array was originally found by deterministic simulated annealing with seed 123. The search found the preserved witness at restart 1, step 256,894. Search is provenance only; coverage verification is the proof.

## Lower bound normalization

Assume a \(\mathrm{CA}(12;2,8,3)\) exists and distinguish any two columns, called \(c_0,c_1\).

### 1. Multiplicity matrix

Let \(M=(m_{ij})\) count rows with \((c_0,c_1)=(i,j)\). Pair coverage implies

\[
m_{ij}\ge 1,\qquad \sum_{i,j=0}^{2}m_{ij}=12.
\]

Thus \(M\) is the all-one \(3\times3\) matrix plus three distributed units. There are

\[
\binom{3+9-1}{9-1}=\binom{11}{8}=165
\]

labelled matrices. Independent symbol permutations in \(c_0,c_1\), together with swapping the two columns, reduce them to exactly seven canonical orbits:

| ID | Canonical matrix, row-major | Orbit size |
|---:|---|---:|
| 0 | `1 1 1 / 1 1 1 / 1 1 4` | 9 |
| 1 | `1 1 1 / 1 1 1 / 1 2 3` | 36 |
| 2 | `1 1 1 / 1 1 1 / 2 2 2` | 6 |
| 3 | `1 1 1 / 1 1 2 / 1 2 2` | 36 |
| 4 | `1 1 1 / 1 1 2 / 1 3 1` | 36 |
| 5 | `1 1 1 / 1 1 2 / 2 2 1` | 36 |
| 6 | `1 1 2 / 1 2 1 / 2 1 1` | 6 |

The orbit sizes sum to 165.

Rows are then ordered in lexicographic \((c_0,c_1)\)-blocks. Repeated rows inside a block may be put in any order; every possible assignment to those positions is still enumerated below.

### 2. Candidate additional columns

An additional column \(x\in\{0,1,2\}^{12}\) is admissible only when both pairs \((c_0,x)\) and \((c_1,x)\) cover all nine ordered symbol pairs.

Each added column has its own independent symbol symmetry. We choose the unique restricted-growth representative: the first symbol seen is renamed 0, the next new symbol 1, and the third new symbol 2. There are exactly 86,526 length-12 restricted-growth words using all three symbols. Filtering them against the two base columns gives the candidate counts below.

### 3. Compatibility graphs

For each multiplicity pattern, form a graph whose vertices are admissible added columns. Two vertices are adjacent exactly when their two columns cover all nine ordered pairs.

A hypothetical \(\mathrm{CA}(12;2,8,3)\) needs six additional columns beyond \(c_0,c_1\). Those six columns must be pairwise compatible, so they would form a \(K_6\). Conversely, every \(K_6\) gives such an array. Symbol-canonicalization cannot merge two columns of a valid clique: columns equivalent by a symbol permutation realize only three ordered pairs with one another and therefore are not adjacent.

The exact graph data and exhaustive clique results are:

| Pattern | Vertices | Edges | Maximum clique \(\omega\) | Number of maximum cliques |
|---:|---:|---:|---:|---:|
| 0 | 180 | 2,513 | 2 | 2,513 |
| 1 | 288 | 5,357 | 3 | 444 |
| 2 | 408 | 9,597 | 3 | 3,392 |
| 3 | 508 | 14,473 | 3 | 9,160 |
| 4 | 552 | 15,497 | 3 | 11,832 |
| 5 | 792 | 32,589 | 4 | 160 |
| 6 | 1,280 | 84,017 | 5 | 336 |

Every graph is \(K_6\)-free. Hence no \(\mathrm{CA}(12;2,8,3)\) exists, so

\[
\mathrm{CAN}(2,8,3)\ge 13.
\]

Together with the 13-row witness, equality follows.

## Independent verification

The certificate generator and checker use different algorithms:

- C++ generator: recursive restricted-growth generation, bitset compatibility graphs, fixed-size clique enumeration.
- Python verifier: integer decoding of all \(3^{12}=531,441\) ternary words, first-occurrence canonicalization, set graphs, and Bron-Kerbosch maximal-clique enumeration.
- Upper checker 1: Python tuple-set scan.
- Upper checker 2: standalone C++ 9-bit mask scan.

No floating-point arithmetic is load-bearing. Floating point appears only in the heuristic construction search, which is not used to establish coverage or optimality.

## Certificate type and limitation

The lower half is a completed, symmetry-normalized exhaustive enumeration with preserved candidate and edge lists and an independent replay. It is not a DRAT/LRAT proof and it is not a global classification of all isomorphism classes. Duplicate partial representations would only enlarge the search; they cannot create a false nonexistence conclusion. Completeness follows from enumerating all 165 multiplicity matrices, all canonical added columns, and all cliques in every resulting graph.
