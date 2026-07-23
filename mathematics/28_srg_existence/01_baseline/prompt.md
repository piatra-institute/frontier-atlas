# PROMPT FOR SETTLING AN OPEN STRONGLY REGULAR GRAPH PARAMETER SET

## Existence or nonexistence of a strongly regular graph at a feasible open parameter tuple

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 28 of 50  
**Area:** graph theory  
**Modes:** `[search]` `[enum]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

A strongly regular graph \( \mathrm{srg}(v,k,\lambda,\mu) \) is a highly symmetric combinatorial object whose parameters are tightly constrained by linear algebra, yet whose existence is, for many parameter tuples, genuinely undecided. Andries Brouwer's parameter tables list dozens of tuples that satisfy every known feasibility condition - integrality of eigenvalue multiplicities, the Krein conditions, the absolute bound, and more - for which no graph has been constructed and no nonexistence proof is known. This prompt fixes one such open tuple and asks for a definitive settlement: either an explicit construction with a machine-checkable certificate, or an exhaustive isomorph-free nonexistence proof. The task is matched to current AI methods because it is finite and certifiable: a construction is a single adjacency matrix that any checker validates in milliseconds, and a nonexistence proof is an isomorph-rejection search or a DRAT-certified SAT run over a fully specified finite space. The resolution standard in section 2 is the target; every partial catalogue, prescribed-automorphism sub-search, or feasibility-refinement result is reported as a partial result and never represented as settling the tuple.

## 1. Exact problem statement

Conventions fixed here: graphs are finite, simple, undirected; \( 0<k<v-1 \) (excluding complete and empty graphs); the primitive case \( 0<\mu<k \) is assumed (imprimitive SRGs are disjoint unions of complete graphs or their complements and are not the object). Parameters are ordered \( (v,k,\lambda,\mu) \) throughout.

A **strongly regular graph** with parameters \( (v,k,\lambda,\mu) \), written \( \mathrm{srg}(v,k,\lambda,\mu) \), is a finite simple undirected graph \( G \) on \( v \) vertices that is neither complete nor empty and satisfies:

1. \( G \) is \( k \)-regular: every vertex has exactly \( k \) neighbours;
2. every pair of adjacent vertices has exactly \( \lambda \) common neighbours;
3. every pair of non-adjacent vertices has exactly \( \mu \) common neighbours.

Equivalently, the adjacency matrix \( A \in \{0,1\}^{v\times v} \) satisfies
\[
A^2 = kI + \lambda A + \mu (J - I - A), \qquad AJ = kJ,
\]
where \( J \) is the all-ones matrix. The parameters obey the identity \( k(k-\lambda-1) = (v-k-1)\mu \). The eigenvalues of \( A \) are \( k \) and
\[
r,s \;=\; \frac{(\lambda-\mu)\pm\sqrt{(\lambda-\mu)^2+4(k-\mu)}}{2},
\qquad r>0>s,
\]
with integer multiplicities
\[
f,g \;=\; \frac{1}{2}\!\left[(v-1)\mp\frac{2k+(v-1)(\lambda-\mu)}{\sqrt{(\lambda-\mu)^2+4(k-\mu)}}\right].
\]

A parameter tuple is **feasible** if it passes all standard necessary conditions: integrality and non-negativity of \( f,g \); the handshake identity above; the Krein conditions
\[
(r+1)(k+r+2rs)\le (k+r)(s+1)^2,\qquad (s+1)(k+s+2rs)\le (k+s)(r+1)^2;
\]
and the absolute bound \( v \le \tfrac{1}{2}f(f+3) \) and \( v \le \tfrac{1}{2}g(g+3) \) (and their equality refinements). **Feasible does not imply existent.**

Two structural facts fix the scope. First, the **complement** \( \overline{G} \) of an \( \mathrm{srg}(v,k,\lambda,\mu) \) is an \( \mathrm{srg}(v,\,v-k-1,\,v-2k+\mu-2,\,v-2k+\lambda) \); a construction or nonexistence proof therefore settles the complementary tuple simultaneously, and searches may work on whichever side is smaller. Second, tuples split into the **conference type** (\( v=4t+1,\ k=2t,\ \lambda=t-1,\ \mu=t \), where the discriminant \( (\lambda-\mu)^2+4(k-\mu)=v \) is not a perfect square, forcing irrational eigenvalues \( (-1\pm\sqrt v)/2 \) with equal multiplicities \( (v-1)/2 \)) and the **integral type** (perfect-square discriminant, integer \( r,s \)). Conference graphs are equivalent to symmetric conference matrices and their existence is governed by additional number-theoretic constraints.

Worked feasibility check for \( \mathrm{srg}(76,21,2,7) \): here \( \lambda-\mu=-5 \), \( k-\mu=14 \), discriminant \( 25+56=81 \), so \( r=2, s=-7 \). The multiplicity formula gives
\[
2k+(v-1)(\lambda-\mu)=42+75\cdot(-5)=-333,\qquad
f,g=\tfrac{1}{2}\!\left[75\mp\tfrac{-333}{9}\right]=\tfrac{1}{2}[75\pm 37],
\]
so \( \{f,g\}=\{56,19\} \), both positive integers; Krein and the absolute bound are also satisfied. Every necessary condition passes, yet no \( \mathrm{srg}(76,21,2,7) \) is known to exist or proven not to - the exact situation this prompt targets.

**Task.** Fix one feasible tuple whose existence is currently open on Brouwer's tables and settle it: construct an \( \mathrm{srg} \) with those parameters, or prove no such graph exists. Concrete long-standing candidates (re-verify each is still open before committing):

- \( \mathrm{srg}(65,32,15,16) \) - a conference-graph parameter tuple (\( v=4t+1, k=2t, \lambda=t-1, \mu=t \) with \( t=16 \); irrational eigenvalues \( (-1\pm\sqrt{65})/2 \), equal multiplicities \( 32 \)) (verify open);
- \( \mathrm{srg}(76,21,2,7) \) - integral eigenvalues \( r=2, s=-7 \), multiplicities \( f=56, g=19 \); a famous smallest-open case (verify open);
- \( \mathrm{srg}(85,20,3,5) \) and other tuples in the \( v\le 120 \) open range (verify parameters and status).

Reference spectra for the candidates (recompute and re-verify open status before use):

| tuple | \( r,s \) | \( f,g \) | type |
|---|---|---|---|
| \( (65,32,15,16) \) | \( (-1\pm\sqrt{65})/2 \) | \( 32,32 \) | conference |
| \( (76,21,2,7) \) | \( 2,-7 \) | \( 56,19 \) | integral |
| \( (85,20,3,5) \) | \( 3,-5 \) | \( 34,50 \) | integral (verify) |

The adjacent parameter tuples \( \mathrm{srg}(99,14,1,2) \) (Conway's 99-graph, problem 03) and \( \mathrm{srg}(3250,57,0,1) \) (Moore graph of degree 57, problem 07) are reserved to their own prompts and are **out of scope** here; choose a tuple distinct from those two. Borsuk-type geometric representations (problem 23) may inform lower bounds but are not the object.

## 2. Resolution standard

A complete resolution of the chosen tuple \( (v,k,\lambda,\mu) \) is one of:

**(A) Existence.** An explicit adjacency matrix (or graph6 string) of a graph on \( v \) vertices, together with an independently checkable verification that it is \( k \)-regular and that the common-neighbour counts are exactly \( \lambda \) on every edge and \( \mu \) on every non-edge - equivalently that \( A^2 - \lambda A - \mu(J-I-A) - kI = 0 \) over the integers. This certificate is a single object and is checked in \( O(v^3) \) exact integer arithmetic.

**(B) Nonexistence.** A proof that no graph with those parameters exists, in one of the following certified forms:
- an **exhaustive isomorph-free enumeration** (canonical augmentation / orderly generation) of all candidate graphs consistent with the parameters, terminating with the empty set, with the generation tree and canonicity test independently replayable (nauty/Traces canonical forms);
- a **DRAT/LRAT-certified UNSAT** proof of a Boolean encoding whose satisfying assignments are exactly the \( \mathrm{srg}(v,k,\lambda,\mu) \) adjacency matrices (with all symmetry-breaking clauses justified);
- a rigorous **combinatorial or algebraic nonexistence argument** (e.g. via triple intersection numbers, local eigenvalue / interlacing obstructions, or a Euclidean-representation / semidefinite argument reduced to exact rational arithmetic), machine-verified where it depends on computation.

**Named certified form.** For existence: a graph6 witness plus an exact-arithmetic regularity/common-neighbour checker. For nonexistence: either a nauty-canonical isomorph-free enumeration replay, or a DRAT/LRAT UNSAT certificate checked by an independent verifier (e.g. `drat-trim` / `cake_lpr`).

**Not accepted as resolution.**
- Passing additional feasibility conditions (refined Krein, quadruple counting, more absolute-bound variants) without settling existence.
- A construction attempt that yields a graph with the right spectrum but wrong \( \lambda \) or \( \mu \) on some pair.
- A prescribed-automorphism search that finds nothing, unless it is a proof that **no** graph exists (not merely none with the assumed group).
- A partial enumeration that exhausts only a sub-case (fixed subgraph, fixed degree partition) without covering the whole space.
- Floating-point spectral or SDP output presented as a proof; it is exploratory until converted to exact certificates.
- A construction of a merely *regular* graph with the right eigenvalues that fails the exact common-neighbour conditions on some pair (co-spectral is not strongly regular).
- Settling a *different* (e.g. already-decided) tuple and presenting it as the open one.

## 3. Graded partial-result targets

**P1 - Reproduce the feasibility frontier.** Independently recompute, in exact arithmetic, the feasibility status (multiplicities, Krein, absolute bound) of every open tuple with \( v \le 120 \), and reproduce the known small-order SRG catalogue (e.g. all \( \mathrm{srg} \) on \( v \le 40 \)) with matching counts. *Certificate:* exact-arithmetic feasibility table plus canonical-form counts agreeing with published enumerations; SHA-256 manifest.

**P2 - Certified constraint model.** Produce a fully specified isomorph-rejection generator and/or SAT encoding for the chosen tuple, validated on a *solved* nearby parameter set (a tuple where an SRG is known, or where nonexistence is proved) by reproducing the correct answer end to end. *Certificate:* the model plus a passing round-trip on a known case with an independent checker.

**P3 - Prescribed-automorphism sub-search.** Exhaustively settle existence of an SRG with the chosen parameters **admitting a nontrivial automorphism** of a fixed prime order (orbit/quotient method à la Behbahani–Lam). *Certificate:* isomorph-free enumeration over the assumed symmetry, with the group action and orbit structure recorded and replayable. (This is a genuine partial result: it rules out or exhibits symmetric solutions only.)

**P4 - Local / substructure obstruction.** Derive and machine-verify a new necessary condition specific to the tuple (triple-intersection-number infeasibility, local eigenvalue obstruction, forbidden neighbourhood configuration), narrowing the search. *Certificate:* exact derivation plus an independent recomputation of the intersection arrays.

**P5 - Constructive existence.** Exhibit an explicit graph with the chosen parameters. *Certificate:* form (A) above - graph6 witness plus exact checker. (This fully resolves the tuple in the existence direction and is the strongest constructive outcome.)

**P6 - Exhaustive nonexistence.** A complete isomorph-free or DRAT-certified nonexistence proof for the chosen tuple. *Certificate:* form (B) above with independent replay. (This is full resolution in the nonexistence direction.)

Targets P1–P4 are realistic session products; P5/P6 are full resolutions and are expected only for the more tractable open tuples.

## 4. Known results and prior art

- **Feasibility theory.** Integrality of multiplicities and the absolute bound go back to the foundational work of Delsarte, Goethals and Seidel (1977, absolute bound) and Scott / Krein (Krein conditions, early 1970s) (verify). The standard reference is Brouwer, Cohen and Neumaier, *Distance-Regular Graphs* (1989), and the modern monograph Brouwer and Van Maldeghem, *Strongly Regular Graphs* (2022, Cambridge) (verify edition/year).
- **Parameter tables.** A. E. Brouwer maintains online tables of strongly regular graph parameters with existence status (exists / does not exist / open) for \( v \) into the thousands; these are the authoritative "open list" for this prompt (verify current contents - the tables are updated as results land).
- **Nonexistence results (examples, verify each).** Azarija and Marc proved there is no \( \mathrm{srg}(75,32,10,16) \) and no \( \mathrm{srg}(95,40,12,20) \) (mid-2010s) by combining eigenvalue arguments with computation. Makhnev, Gavrilyuk and collaborators have ruled out many tuples via triple-intersection-number and local-eigenvalue methods. Bondarenko, Prymak, Radchenko and collaborators ruled out putative sets using Euclidean-representation / semidefinite arguments (verify specific parameters and years).
- **Constructive / enumerative work.** Behbahani and Lam (~2011) searched for SRGs with nontrivial automorphisms; Coolsaet, Degraer and Spence produced computer classifications of SRGs for specific small parameter sets (verify). SageMath ships a `strongly_regular_graph` constructor and a feasibility database derived from Brouwer's tables.
- **Classical constructions.** Many SRGs arise from combinatorial geometry and algebra: Paley graphs (conference type, prime-power \( v\equiv 1\bmod 4 \)), Latin-square and block-graph constructions, rank-3 permutation groups, two-weight codes, and regular two-graphs. A target tuple that resists all such families is precisely one where existence is genuinely in doubt; the absence of an algebraic construction is evidence but not proof of nonexistence.
- **The open landscape.** Beyond the named candidates, Brouwer's tables carry a running list of open feasible tuples across the small-\( v \) range (many below \( v=200 \)); the more tractable ones - smaller \( v \), integral spectrum, or a plausible prescribed automorphism - are the sensible session targets, while the largest are effectively out of reach on one workstation.
- **Status of the named candidates.** \( \mathrm{srg}(65,32,15,16) \), \( \mathrm{srg}(76,21,2,7) \), and \( \mathrm{srg}(85,20,3,5) \) have all been listed as open for many years (verify none has been settled recently). Adjacent SRG problems in this program: \( \mathrm{srg}(99,14,1,2) \) (problem 03) and \( \mathrm{srg}(3250,57,0,1) \) (problem 07).

**Status as of mid-2026 - re-verify against the current literature and Brouwer's tables before starting any session.** Existence status in these tables drifts as constructions and nonexistence proofs appear; several nearby SRG parameter sets were settled in 2015–2024. Confirm the chosen tuple is still open before committing compute.

## 5. Attack plan

**Feasibility and bookkeeping (`[enum]`).** In SageMath or a small exact-arithmetic script, recompute multiplicities, Krein parameters, and absolute bounds over \( \mathbb{Q} \) / algebraic numbers; cross-check against Brouwer's tables. Enumerate the open window (say \( v\le 120 \)) and pick the most tractable target - smaller \( v \), integral eigenvalues, and small automorphism-agnostic search space are favourable.

**Isomorph-free enumeration (`[search]`).** Use canonical augmentation with nauty/Traces (`geng`-style orderly generation is too weak alone at these orders; a bespoke SRG-aware generator that fixes a vertex neighbourhood and grows the local structure with interlacing pruning is needed). Every pruning rule must have a locally checkable reason (degree, common-neighbour count on a completed pair, interlacing on a completed principal submatrix). Record the generation tree for replay.

**Prescribed-automorphism method.** Assume an automorphism of fixed prime order \( p \), reduce to an orbit matrix / quotient problem, and enumerate solutions of the smaller integer system (the Behbahani–Lam approach). This makes symmetric cases tractable on one workstation even when the full space is not. Sweep a set of candidate prime orders and record, for each, whether a symmetric SRG exists; a full sweep of admissible orders that finds nothing is a genuine partial result (no vertex-symmetric solution) but not a nonexistence proof.

**Complement duality in practice.** For each candidate work on whichever of \( G \) or \( \overline{G} \) has the smaller degree, since the two are settled together; the smaller-degree side usually has cheaper cardinality constraints and a shallower search tree.

**SAT encoding (`[search]`).** Encode the adjacency Booleans \( a_{ij} \) with regularity as cardinality constraints and common-neighbour counts as exact cardinality constraints over each pair; add lexicographic symmetry-breaking with a justification. Run CaDiCaL / kissat / CryptoMiniSat and emit DRAT; convert to LRAT and check with `drat-trim` / `cake_lpr`. Feasible only for the smaller open tuples or heavily symmetry-reduced sub-cases.

**Local subconstituent structure.** In an \( \mathrm{srg}(v,k,\lambda,\mu) \) the neighbourhood of any vertex induces a \( \lambda \)-regular graph on \( k \) vertices, and the non-neighbourhood induces a \( \mu \)-avoiding structure with its own regularity; the local eigenvalues are constrained by interlacing. Enumerate the admissible neighbourhood graphs first (a much smaller problem: for \( \mathrm{srg}(76,21,2,7) \) the neighbourhood is a \( 2 \)-regular graph on 21 vertices, i.e. a disjoint union of cycles totalling 21 vertices), then attempt to glue globally consistent completions. A contradiction at the local-gluing stage can yield nonexistence without a full global search.

**Algebraic obstructions.** Compute triple and quadruple intersection numbers exactly; test local eigenvalue conditions and interlacing on hypothetical neighbourhood subgraphs (SageMath / GAP with GRAPE and nauty). Any SDP/Euclidean-representation bound must be rationalized to an exact certificate before it counts.

**Smaller exact analogues.** Before committing compute at the target tuple, run the entire pipeline (generator, SAT model, obstruction checks) on a nearby *solved* tuple - one where an SRG is known and one where nonexistence is proven - and confirm it returns the correct verdict end to end. A method that cannot rediscover a settled nearby case is not trusted at the open one.

**One-workstation scope and failure modes.** A single modern workstation can: fully enumerate small SRG parameter sets, run prescribed-automorphism searches for many groups, and DRAT-certify small encodings. It **cannot** brute-force the unconstrained space at \( v=65 \) or \( v=76 \) - these have astronomically many candidate matrices; progress there requires strong structural reduction or symmetry assumptions (which yield only partial results unless combined with a coverage argument). Expect: search spaces that look tractable but blow up after a fixed neighbourhood is chosen; SAT encodings whose symmetry-breaking is unsound if not carefully justified; and SDP outputs that are numerically suggestive but resist exact certification. Report these honestly rather than as near-misses.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** All feasibility arithmetic in exact rationals/algebraic numbers; all common-neighbour and regularity checks in exact integer arithmetic; all SAT nonexistence claims backed by DRAT/LRAT. Floating-point spectra and SDP values are exploratory only and never certify a claim.
2. **Independent verification.** For a constructed graph, a standalone checker (written separately from the generator) validates \( A^2 = kI+\lambda A+\mu(J-I-A) \) and, independently, that every edge has exactly \( \lambda \) and every non-edge exactly \( \mu \) common neighbours by direct enumeration. For a nonexistence proof, an independent enumeration replay (recompute canonical forms with a fresh nauty invocation) or an independent DRAT/LRAT checker. Dual implementations for the intersection-number derivations.
3. **Reproducibility.** All parameter choices, generator flags, symmetry assumptions, solver versions, seeds, and environment recorded; a SHA-256 manifest over every artifact (encodings, proof traces, graph6 files, logs).
4. **Preservation.** Generator and encoder source code is part of the record. If any search was pruned by an assumption (prescribed automorphism, fixed subgraph), that assumption is stated explicitly as a scope limit, not obscured - the lesson of the Hadamard-668 lost-source episode in this program.
5. **Honest reporting.** The report states up front whether the chosen tuple was settled (existence or nonexistence) or not. A prescribed-automorphism null result, a feasibility refinement, or a sub-case enumeration is reported as a partial result and never represented as resolving the tuple.

### Calibration

Full resolution of an open SRG tuple is a hard, genuinely open problem; a single session is far more likely to deliver P1–P4 (reproduced frontier, validated model, a prescribed-automorphism verdict, or a new local obstruction) than P5–P6. The realistic high-value outcome is a *certified* narrowing - a machine-checkable partial result that a later session or a specialist can build on - not a claimed existence/nonexistence unless the tuple is one of the more tractable ones. Choose the target tuple with that in mind: prefer the smallest \( v \), integral spectrum, and a plausible symmetry over the most famous but least tractable cases.
