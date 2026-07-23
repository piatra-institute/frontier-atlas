# PROMPT FOR DETERMINING THE MINIMUM SIZE OF A KOCHEN–SPECKER SET IN DIMENSION 3

## The minimal vector count for a Kochen–Specker contextuality proof in $\mathbb{C}^3$

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 01 of 50 (Tier 1)
**Source:** top-50 list #6, category A (quantum information and foundations)
**Modes:** `[cert]` `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The Kochen–Specker theorem forbids noncontextual value assignments to quantum observables in dimension $\ge 3$; its minimal witnesses in dimension 3 are finite sets of rays whose orthogonality structure admits no $\{0,1\}$-coloring of the Kochen–Specker type. The record construction has 31 rays (Conway–Kochen); the best certified lower bounds, obtained by SAT-solver and isomorph-free-generation methods, sit in the low-to-mid 20s. The target of this session is the exact minimum. This is the most SAT-shaped problem on our physics list: the search space is a finite family of orthogonality graphs, non-colorability is a propositional statement with DRAT-checkable proofs, and geometric realizability is decidable by exact algebra - the same certified-search machinery as our Ramsey program. The payoff is the minimal experimental footprint for contextuality tests and device-independent protocols. The complete resolution defined in section 2 is the target; anything less must be reported as a partial result, never represented as a solution.

## 1. Exact problem statement

Work in $\mathbb{C}^3$ with the standard Hermitian inner product $\langle\cdot,\cdot\rangle$. A *ray* is a one-dimensional subspace; we identify a ray with any unit vector spanning it, and all counts below count rays (vectors up to global phase and scalar multiple). Two rays $u, v$ are *orthogonal* when $\langle u, v\rangle = 0$.

Let $S$ be a finite set of rays in $\mathbb{C}^3$. A map $f : S \to \{0,1\}$ is a **KS coloring** of $S$ if:

1. **(Exclusivity)** for every pair $u, v \in S$ with $u \perp v$: $f(u)\,f(v) = 0$;
2. **(Completeness)** for every triple $\{u,v,w\} \subseteq S$ of mutually orthogonal rays: $f(u) + f(v) + f(w) \ge 1$ (with exclusivity, exactly one of the three receives 1).

$S$ is a **Kochen–Specker set** (KS set) if no KS coloring of $S$ exists. Define

\[
\mathrm{KS}_{\mathbb{C}}(3) \;=\; \min\{\, |S| : S \subset \mathbb{CP}^2 \text{ is a KS set} \,\},
\]

\[
\mathrm{KS}_{\mathbb{R}}(3) \;=\; \min\{\, |S| : S \subset \mathbb{RP}^2 \text{ is a KS set} \,\}.
\]

**The problem: determine $\mathrm{KS}_{\mathbb{C}}(3)$ exactly.**

Since every real KS set is a complex one,

\[
\mathrm{KS}_{\mathbb{C}}(3) \;\le\; \mathrm{KS}_{\mathbb{R}}(3) \;\le\; 31 .
\]

The two quantities are not known to be equal; every claimed bound must state which variant it certifies. We adopt the complex formulation as primary because $\mathbb{C}^3$ is the physical Hilbert space; the real variant is a named restriction, and resolving both is the ideal outcome.

**Choice of definition.** Several inequivalent notions circulate:

- some authors require $S$ to be a union of complete orthonormal bases ("basis-realizable" or context-covering sets);
- some count *contexts* (bases) rather than rays;
- state-independent-contextuality sets à la Yu–Oh satisfy a strictly weaker operational condition and are **not** KS sets.

We adopt the coloring definition above - the standard one in the lower-bound literature (Arends–Ouaknine–Wampler; Uijlen–Westerbaan; the SAT-based work) - because it makes the problem a pure finite combinatorics-plus-realizability question and matches the record constructions. Results for the other notions are logged separately and never conflated with the target.

**Two-level structure.** For a set of rays $S$, its *orthogonality graph* $G(S)$ has vertex set $S$ and edges exactly the orthogonal pairs. Call a graph $G$ **010-colorable** if there is $f: V(G) \to \{0,1\}$ with no edge having both endpoints valued 1 and every triangle carrying at least one 1. Then:

- if $S$ realizes $G$ faithfully (edges = orthogonal pairs, non-edges = non-orthogonal pairs, distinct vertices = distinct rays), KS colorings of $S$ and 010-colorings of $G$ coincide; in particular non-010-colorability of $G(S)$ makes $S$ a KS set;
- conversely the full orthogonality graph of any KS set is non-010-colorable.

Hence the lower-bound schema: $\mathrm{KS}_{\mathbb{C}}(3) \ge n+1$ follows from a proof that *every non-010-colorable graph on $\le n$ vertices fails to be faithfully realizable as the full orthogonality graph of rays in $\mathbb{C}^3$*. Both halves - combinatorial enumeration and geometric (non-)realizability - must be certified.

## 2. Complete-resolution standard

A complete resolution is the exact value $N = \mathrm{KS}_{\mathbb{C}}(3)$, established by both of:

1. **Upper bound.** An explicit KS set $S^*$ with $|S^*| = N$:
   - exact coordinates in a specified number field $K \subset \mathbb{C}$ (minimal polynomial and embedding given);
   - exact verification of every orthogonality and non-orthogonality;
   - a machine-checked proof of non-010-colorability of $G(S^*)$ - a DRAT/LRAT-certified UNSAT proof checked by an independent verified checker, or a Lean 4 proof.
2. **Lower bound.** A proof that no KS set of size $N-1$ exists in $\mathbb{C}^3$:
   - a complete, isomorph-free enumeration argument over candidate orthogonality graphs on $\le N-1$ vertices, with every pruning rule proved sound;
   - for every candidate surviving to the geometric stage, either (a) an explicit 010-coloring, independently checked, or (b) an exact certificate of non-realizability in $\mathbb{C}^3$ - a Gröbner-basis proof that the realizability ideal contains 1, a Positivstellensatz certificate, or an equally rigorous exact-algebra argument - never a numerically failed optimization.

All certificates must satisfy section 6. The final theorem must be stated over $\mathbb{C}^3$; if only the real case is closed, that is a partial result (a strong one - see P5).

**Not accepted as resolution:**

- A new smallest KS set given only in floating point, or whose non-colorability is asserted by an unverified solver run without a stored, replayable proof.
- A lower bound certified only for $\mathbb{R}^3$ presented as a bound for $\mathrm{KS}_{\mathbb{C}}(3)$.
- A lower bound relying on unpublished or unverifiable prior computations (including published claims whose certificates are not available) without independent re-derivation.
- Minimality of *contexts*, *bases*, or *observables* substituted for minimality of rays.
- State-independent contextuality sets (e.g., the 13-ray Yu–Oh set) or state-dependent arguments presented as KS sets.
- Probabilistic, heuristic, or sampling-based non-existence claims; "no set found after extensive search".
- Conditional results ("assuming realizable graphs have property X") unless the property is itself proved.

## 3. Graded partial-result targets

**P1 - Re-certify the frontier objects.**
*Task:* reproduce the 31-ray Conway–Kochen set and the 33-ray Peres set with exact coordinates; verify all orthogonalities in exact arithmetic; produce DRAT-certified UNSAT proofs of non-010-colorability; stretch goal, a Lean 4 formalization of non-colorability from the adjacency data.
*Certificate:* coordinate files + exact orthogonality checker + CNF + DRAT/LRAT proof + independent checker logs, all hashed.
*Effort:* days; establishes the toolchain.

**P2 - Reproduce the certified lower bound with our own pipeline.**
*Task:* independently re-derive the best published certified bound (Uijlen–Westerbaan's 22; subsequent SAT-plus-CAS pushes to $\ge 23$/$\ge 24$ - verify the current record first). Isomorph-free generation (nauty/Traces or SAT-modulo-symmetries) of candidate graphs; 010-colorability by SAT; realizability filtering by exact algebra; every discarded graph carries a certificate.
*Certificate:* full enumeration manifest with per-graph disposition, spot-checkable by the independent checker.
*Effort:* weeks; the central reproduction milestone.

**P3 - Advance the lower bound by one vertex.**
*Task:* extend P2's pipeline one vertex past the verified record, for the complex case.
*Certificate:* as P2; publishable on its own.
*Note:* expect the realizability stage, not SAT, to be the bottleneck; a clean, reusable exact non-realizability certifier is a deliverable even if the bound does not move.

**P4 - Structured upper-bound search below 31.**
*Task:* search for KS sets with $\le 30$ rays: orbits of finite subgroups of $\mathrm{PU}(3)$; rays with coordinates in small-degree number fields; extensions/reductions of known sets; SAT-guided completion of near-critical graphs followed by exact realization (Gröbner or interval-Newton lift to algebraic coordinates).
*Certificate:* as in P1. Any verified set with $\le 30$ rays is a headline result.

**P5 - Close the real case, or separate the variants.**
*Task:* either determine $\mathrm{KS}_{\mathbb{R}}(3)$ exactly, or exhibit a certified complex KS set smaller than the proven real minimum. A real–complex separation would be a striking foundational result in its own right.
*Certificate:* P2/P3-style lower-bound artifacts restricted to real realizability plus P1-style upper-bound artifacts.

**P6 - Lower bound $\ge 27$ (complex).**
*Task:* a substantial push requiring symmetry-aware enumeration and massive but replayable proof logs.
*Certificate:* as P2; the strongest realistic outcome short of resolution.

**P7 - Full determination of $\mathrm{KS}_{\mathbb{C}}(3)$** per section 2.

Honest calibration: full resolution is plausibly within reach of sustained certified search over a few years, but is *not* expected from one session; P2–P4 are the realistic products.

## 4. Known results and prior art

- Kochen–Specker original proof, 117 rays in $\mathbb{R}^3$ (Kochen–Specker, 1967).
- 33 rays (Peres, 1991); 31 rays (Conway–Kochen, unpublished, reported in Peres's *Quantum Theory: Concepts and Methods*, 1993). Both real. Bub's 33-ray set and Schütte-type sets are nearby variants.
- Dimension 4: 18 rays / 9 contexts (Cabello–Estebaranz–García-Alcaine, 1996); 18 is proven minimal for $d=4$ via exhaustive/SAT-certified methods (Pavičić–Merlet–McKay–Megill exhaustive generation, ~2005; later SAT re-verifications) (verify the exact minimality attribution).
- Lower bounds in $d=3$: no KS set with fewer than 18 rays (Arends–Ouaknine–Wampler, ~2011).
- At least 22 rays (Uijlen–Westerbaan, ~2016; large-scale graph enumeration plus realizability filtering).
- SAT-plus-computer-algebra and SAT-modulo-symmetries pushes to $\ge 23$ and reportedly $\ge 24$ (Li–Bright–Ganesh, ~2022–2024; Kirchweger–Peitl–Szeider, ~2023) (verify the current certified record, and which variant - real or complex - each bound certifies).
- State-independent contextuality with 13 rays (Yu–Oh, 2012), proven optimal for its weaker notion (Cabello–Kleinmann–Portillo, ~2015) (verify) - explicitly *not* a KS set; keep the notions separated in all reporting.
- Methodological neighbors: DRAT-certified SAT results in combinatorics (Heule et al., Pythagorean triples, 2016; Schur number five, 2017); SAT modulo symmetries (Kirchweger–Szeider, ~2021 onward).

**Status as of mid-2026 - re-verify against current literature before starting the session.**

## 5. Attack plan

**SAT layer.**

- Encode 010-colorability per graph: variables = vertices; clauses $\neg u \vee \neg v$ per edge, $u \vee v \vee w$ per orthogonal triangle.
- Solvers: CaDiCaL or kissat with DRAT proof logging; proofs checked with drat-trim and an independently written checker (Python and C++).
- Enumeration: SAT-modulo-symmetries or nauty canonical augmentation, so the graph stream is provably isomorph-free; the generation certificate is stored.

**Graph-side pruning (proved, not assumed).**

- Candidate rules: minimum-degree bounds; every vertex lies in a triangle; no twin vertices; 2-connectivity.
- Each rule carries a lemma-level proof that it preserves at least one minimum KS set; unproved rules are forbidden.

**Realizability layer.**

- Realizability of a graph $G$ in $\mathbb{C}^3$ is a polynomial system: orthogonality equations (Hermitian forms, split into real and imaginary parts over $\mathbb{Q}$) plus inequations (non-orthogonality, distinctness) - an existential real-algebra problem.
- Pipeline: (i) floating-point local search for likely embeddings; (ii) exact lift via interval Newton (Arb/FLINT) plus algebraic reconstruction in SageMath; (iii) for non-realizability, saturation and Gröbner bases in Singular or msolve over $\mathbb{Q}$, producing an ideal-membership certificate ($1 \in I$) that a standalone checker verifies by exact polynomial arithmetic.
- Expect this layer to dominate runtime; cache certificates keyed by canonical graph hash.

**Search for smaller sets (P4).**

- Group-orbit generators in GAP (finite subgroups of $\mathrm{PU}(3)$); number-field coordinate ansätze in SageMath/Pari-GP.
- SAT-guided completion: fix a partial ray set, ask SAT for non-010-colorable graph completions, then attempt exact realization.

**Workstation budget.**

- Enumeration through ~24 vertices with aggressive certified pruning: single workstation, days to weeks.
- 25–27 vertices: likely cluster territory; DRAT logs may reach hundreds of GB - plan streaming verification.

**Expected failure modes.**

- Combinatorial explosion at the graph layer.
- Realizability systems too large for Gröbner: mitigate with triangle-based coordinatization (fix a basis, propagate constraints, case-split).
- Silent unsoundness from unproved pruning rules (forbidden - every rule proved).
- Conflating real and complex realizability (track the two variants separately end-to-end).

## 6. Verification and auditability requirements

1. **Exact arithmetic.** All coordinates in explicit number fields or as interval-certified algebraic numbers; orthogonality checks by exact symbolic evaluation; Gröbner certificates over $\mathbb{Q}$; floating point only for candidate discovery, never certification.
2. **Independent verification.** Standalone checkers, written independently of the search code, for: (a) DRAT/LRAT proofs (an existing verified checker plus our own reimplementation), (b) claimed 010-colorings, (c) orthogonality of coordinate files, (d) ideal-membership certificates. Dual Python and C++ implementations for (b)–(d).
3. **Reproducibility.** Solver versions, flags, seeds, generation orders, and machine specs recorded; SHA-256 manifest over every CNF, proof, coordinate file, certificate, and log; a single driver script re-runs any per-graph claim from the manifest.
4. **Preservation.** All search code, pruning-lemma proofs, and discarded-branch certificates are part of the record; any unpreserved exploratory run is declared as such and carries no evidentiary weight.
5. **Honest reporting.** The final report opens with whether section 2 was met; states the certified value of every bound with its variant ($\mathbb{R}$ vs $\mathbb{C}$); lists which published results were independently re-verified versus assumed; and never presents a heuristic search outcome as a bound.
