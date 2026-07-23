# Research report: exact Ramsey number $R(5,5)$

**Session date:** 20 July 2026  
**Input prompt:** `01_ramsey_R5_5(1).pdf`  
**Outcome:** No exact value was proved. The strongest completed results are certified finite reductions around the known 42-vertex catalogue and the strongest published 43-vertex near-misses.

## 1. Status and scope

The target is to determine the unique integer in

$$
43 \le R(5,5) \le 46.
$$

A graph is a $(5,5)$-Ramsey graph when it has neither a clique of size five nor an independent set of size five. A complete resolution requires both a lower-bound witness and an exhaustive upper-bound proof. This session did not produce either missing global component, so it does **not** determine $R(5,5)$.

The work concentrated on three exact, independently auditable questions:

1. Can any of the 656 known 42-vertex Ramsey graphs be extended by one vertex to a 43-vertex Ramsey graph?
2. Can any known 42-vertex graph be extended to a 43-vertex coloring with zero or one monochromatic $K_5$, and which ones attain two?
3. How far, in edge-flip Hamming distance, is the strongest published 43-vertex near-miss from any possible 43-vertex Ramsey graph?

All headline negative answers below have proof traces and independent replay checkers.

## 2. One-vertex extension formulation

Let $G$ be a 42-vertex $(5,5)$-Ramsey graph. Add a new vertex $x$, and introduce a Boolean variable $y_v$ for every $v\in V(G)$:

$$
y_v=1 \quad\Longleftrightarrow\quad xv\in E.
$$

Every forbidden five-set in the extension must contain $x$, because $G$ itself has no forbidden five-set. Therefore:

- for every $K_4$, $Q\subseteq G$, add
  $$
  \bigvee_{v\in Q}\neg y_v;
  $$
- for every independent four-set, $Q\subseteq G$, add
  $$
  \bigvee_{v\in Q}y_v.
  $$

This monotone 4-SAT formula is satisfiable if and only if $G$ has a valid one-vertex Ramsey extension.

### Certified result A

The supplied official data file contains 328 representatives. Their complements give 656 known graphs. For every representative:

- the graph6 record was independently decoded;
- the graph was verified to have neither $K_5$ nor an independent five-set;
- its exact extension CNF was generated;
- Glucose 4 returned UNSAT and emitted a DRUP proof;
- a separate standard-library Python checker regenerated the CNF and replayed every RUP addition.

**Result:** none of the 328 representatives extends to order 43. Complement symmetry gives the same conclusion for all 656 known graphs.

Numerical audit:

| Quantity | Value |
|---|---:|
| Representatives checked | 328 |
| Known graphs including complements | 656 |
| Valid one-vertex extensions | 0 |
| Extension DRUP additions replayed | 37,713 |
| Input graph6 SHA-256 | Recorded immediately below |
| DPLL nodes in independent custom search | 441,990 |
| Unit propagations in custom search | 2,464,913 |

Input graph6 SHA-256, split across two display lines and concatenated without whitespace:

```text
067902e853d87b49bcef0d1d4c0e3bba
dd238ee18bc65341b079a3ca4780eccb
```

This does not prove that no 43-vertex Ramsey graph exists, because the 656-graph collection is explicitly a collection of known examples, not a complete catalogue.

A useful corollary is exact:

> If a 43-vertex Ramsey graph exists, none of its 42-vertex vertex-deleted subgraphs is isomorphic to any of the 656 known graphs.

Indeed, deleting any vertex from a 43-vertex Ramsey graph gives a 42-vertex Ramsey graph. If one deletion belonged to the known collection, the original graph would be an extension that has just been certified impossible.

## 3. Zero-, one-, and two-violation extensions

Relax each extension clause with a fresh Boolean variable. A violated extension clause corresponds bijectively to one monochromatic $K_5$ containing the new vertex. An at-most-one sequential counter therefore asks whether the extension can have zero or one forbidden five-set.

### Certified result B

For all 328 representatives, the at-most-one formula is UNSAT.

- 328 Glucose DRUP traces were generated.
- A separate C++ checker independently decoded graph6, independently generated all four-set clauses and the sequential counter, and replayed the proofs.
- Deletion lines were conservatively ignored. Retaining previously derived clauses yields a monotone sound proof sequence.

**Result:** no known 42-vertex Ramsey graph has a 43-vertex extension with at most one monochromatic $K_5$.

Certificate audit:

| Quantity | Value |
|---|---:|
| Proofs | 328 |
| RUP additions independently replayed | 554,611 |
| Solver proof lines, including deletions | 1,047,253 |
| Failed replay steps | 0 |

Consequently, any 43-vertex coloring with exactly one monochromatic $K_5$ would have five Ramsey vertex deletions, one for each vertex of that $K_5$, and all five deletion graphs would have to lie outside the known collection.

### Certified exact two-violation enumeration

An at-most-two search was run for every representative using an explicit sequential-counter encoding. Indices 41 and 255 are satisfiable and were retained as direct witnesses. The other 326 instances emitted DRUP traces, all of which passed the independent C++ replay checker.

Certificate audit:

| Quantity | Value |
|---|---:|
| UNSAT proofs | 326 |
| Satisfiable representatives | 2 |
| RUP additions independently replayed | 1,684,031 |
| Deletion lines conservatively ignored | 1,730,537 |
| Failed replay steps | 0 |

**Only indices 41 and 255 are satisfiable.** Each admits two projected neighbor-set assignments in the chosen labeling. Exhaustive model blocking and graph-isomorphism testing reduce the four labeled extensions to exactly two unlabeled 43-vertex graphs.

Those two isomorphism classes are precisely the two published 43-vertex near-miss graphs with two monochromatic $K_5$'s.

| Extension class | Edges | Violation color | Base types |
|---|---:|---|---|
| Class 0 | 448 | two independent five-sets | 41 and 255 |
| Class 1 | 449 | two clique five-sets | 41 and 255 |

This is an exhaustive statement only relative to the 328 representatives and their complements.

## 4. Structure of the two 43-vertex near-misses

The two published adjacency matrices were independently parsed and checked.

### Graph 1

- 43 vertices, 448 edges;
- degree counts: 20 vertices of degree 20, 10 of degree 21, 13 of degree 22;
- exactly two forbidden sets, both independent:
  $$
  \{0,2,28,29,38\},\qquad \{0,11,28,29,38\}.
  $$

### Graph 2

- 43 vertices, 449 edges;
- degree counts: 19 vertices of degree 20, 10 of degree 21, 14 of degree 22;
- exactly two forbidden sets, both cliques:
  $$
  \{0,15,22,28,39\},\qquad \{0,15,24,28,39\}.
  $$

The matrices differ by exactly one edge, $\{0,28\}$. Flipping this edge trades two independent violations for two clique violations.

### Deletion-intersection lemma

For any coloring $F$, let $\mathcal B(F)$ be the family of monochromatic five-sets. Then

$$
F-v\text{ is Ramsey}\quad\Longleftrightarrow\quad v\in\bigcap_{B\in\mathcal B(F)}B.
$$

The proof is immediate: deletion removes every forbidden set exactly when the deleted vertex belongs to every forbidden set.

Each near-miss has two bad five-sets sharing a four-set, so each has exactly four Ramsey vertex deletions. Exact isomorphism checks give:

- Graph 1 deletion types: index 255 twice, index 41 twice;
- Graph 2 deletion types: index 255 twice, index 41 twice.

This explains why precisely those two catalogue representatives appear in the at-most-two extension search.

## 5. Certified Hamming ball around the strongest near-miss

Let one Boolean variable represent the decision to flip each of the $\binom{43}{2}=903$ edges/nonedges of Graph 1. For a five-set containing $t$ base edges:

- it can become independent within radius $r$ only when $t\le r$;
- it can become a clique within radius $r$ only when $10-t\le r$.

Only these potentially endangered five-sets need clauses. An explicit sequential counter enforces at most $r$ flips.

DRUP certificates were generated and independently replayed for $r=1,2,3,4,5$.

| Radius | Variables | Clauses | RUP additions | Result |
|---:|---:|---:|---:|---|
| 1 | 1,805 | 16,478 | 21 | UNSAT |
| 2 | 2,707 | 85,576 | 257 | UNSAT |
| 3 | 3,609 | 299,290 | 1,210 | UNSAT |
| 4 | 4,511 | 715,454 | 8,039 | UNSAT |
| 5 | 5,413 | 1,227,766 | 30,366 | UNSAT |

### Certified result C

> No 43-vertex Ramsey graph lies within five edge flips of Graph 1.

Equivalently, any hypothetical solution at order 43 has edge-Hamming distance at least six from this near-miss.

Since Graph 2 is one flip from Graph 1, the same triangle-inequality argument excludes radius four around Graph 2.

The one-flip landscape was also enumerated directly. Graph 1 has two flips that preserve the minimum of two violations, $\{0,28\}$ and $\{29,38\}$; every other single flip produces at least three violations. Graph 2 likewise has only two minimum-preserving flips, $\{0,28\}$ and $\{15,39\}$.

## 6. Aggregate structural relaxation, and why it failed

An integer program was built from:

- exact minimum and maximum edge counts in $R(4,5,d)$ for every relevant $d\in\{17,\ldots,24\}$;
- degree-class counts;
- neighborhood and antineighborhood triangle counts;
- Goodman's monochromatic-triangle identity;
- common-neighbor upper bounds from $R(3,5)=14$;
- inclusion-exclusion lower bounds on codegrees.

The relaxation remains feasible for every order 42 through 46, including unrealistic regular endpoint solutions. It therefore does not improve the interval.

This negative result is informative: aggregate degree, edge, and triangle statistics are too coarse. A successful route must retain compatibility information between particular neighborhoods, common-neighbor subgraphs, or graph-isomorphism classes. This agrees with the architecture of the published $R(5,5)\le46$ proof, which combines linear inequalities with large finite gluing computations.

## 7. Exact remaining gap

The completed computations establish a strong conditional frontier, but not the global theorem.

To prove $R(5,5)=43$, one still needs an exhaustive reason that every hypothetical 43-vertex Ramsey graph has a 42-vertex deletion in a certified finite class, followed by nonextendibility of that class. The present 656 known graphs are not complete, so the implication stops there.

To prove a larger value, one needs an explicit 43-, 44-, or 45-vertex Ramsey graph with exact verification. No such graph was found here.

The most focused next target suggested by these results is:

> Prove that every 43-vertex $(5,5)$-Ramsey graph has at least one vertex-deleted subgraph in a rigorously complete, computationally manageable subclass of $R(5,5,42)$.

A plausible subclass should be defined by local neighborhood types, degree sequence, edge count, or a bounded gluing interface. Merely assuming that the 656 known examples are exhaustive is invalid.

## 8. Reproduction

From `src/`:

```bash
# Recheck all 328 exact one-vertex extension proofs.
python check_extension_proofs.py \
  --graphs ../data/r55_42some.g6 \
  --proof-dir ../proofs

# Compile and replay the 328 at-most-one proofs.
g++ -O3 -std=c++17 -o check_one_bad_drup check_one_bad_drup.cpp
./check_one_bad_drup ../data/r55_42some.g6 ../proofs/one_bad 0 328

# Compile and replay the 326 at-most-two UNSAT proofs.
g++ -O3 -std=c++17 -o check_two_bad_drup check_two_bad_drup.cpp
./check_two_bad_drup ../data/r55_42some.g6 ../proofs/two_bad 0 328

# Compile and replay Hamming-radius proofs 1 through 5.
g++ -O3 -std=c++17 -o check_near_radius_drup check_near_radius_drup.cpp
./check_near_radius_drup \
  ../data/near43_graph1.matrix \
  ../proofs/near_radius_seq 5
```

The final radius-5 proof can also be replayed in ranges using the optional proof-start and proof-end arguments. This is useful in environments with a short process limit.

## 9. Trust boundary

The following statements are fully supported by the included finite data, source, proof traces, and independent replay:

- all 328 supplied records are valid 42-vertex Ramsey graphs;
- none has a valid one-vertex Ramsey extension;
- none has an extension with at most one monochromatic $K_5$;
- exactly representatives 41 and 255 have an extension with at most two;
- their two-violation extensions form exactly two unlabeled classes, matching the two supplied near-miss matrices;
- no Ramsey graph is within five edge flips of near-miss Graph 1.

The package does **not** certify that the 328 representatives, or their 328 complements, exhaust all 42-vertex Ramsey graphs. Consequently, it does not certify the exact value of $R(5,5)$.
