# PROMPT FOR IMPROVING A CAGE ORDER

## A smaller construction or a certified nonexistence bound for an open \((r,g)\)-cage number

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 29 of 50  
**Area:** graph theory  
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

An \((r,g)\)-cage is a smallest \(r\)-regular graph of girth \(g\); its order \(n(r,g)\) is the **cage number**. The Moore bound gives a clean lower bound, and cages meeting it are exceptional (they coincide with the Moore graphs and generalized polygons). For most parameter pairs the exact cage number is unknown, trapped between the best explicit construction (an upper bound) and the best nonexistence argument (a lower bound), with a gap that has resisted closure for decades - the \((3,13)\)-cage and the \((7,6)\)-cage are standing examples. This is a finite, certifiable problem: an upper bound is a single explicit graph (regularity and girth checked in low-degree polynomial time), and a lower bound of the form "no \(r\)-regular graph of girth \(g\) has fewer than \(N\) vertices" is an exhaustive or SAT-certified nonexistence statement over a fully specified finite space. It is well matched to AI methods for exactly that reason. The resolution standard in section 2 - a strict improvement of an open cage number in either direction, with a machine-checkable certificate - is the target; heuristic near-record constructions and un-replayable searches are reported as partial results.

## 1. Exact problem statement

Let \(r\ge 3\) and \(g\ge 3\) be integers. A graph is **\(r\)-regular** if every vertex has degree exactly \(r\), and has **girth \(g\)** if its shortest cycle has length exactly \(g\). An **\((r,g)\)-graph** is any \(r\)-regular graph of girth \(g\); an **\((r,g)\)-cage** is an \((r,g)\)-graph of minimum order, and that minimum order is the **cage number** \(n(r,g)\). Cages exist for all \(r\ge 2, g\ge 3\) (Erdős–Sachs).

The **Moore bound** \(n_0(r,g)\) is
\[
n_0(r,g)=
\begin{cases}
1+r\displaystyle\sum_{i=0}^{d-1}(r-1)^i, & g=2d+1 \text{ (odd)},\\[2mm]
2\displaystyle\sum_{i=0}^{d-1}(r-1)^i, & g=2d \text{ (even)},
\end{cases}
\]
and \(n(r,g)\ge n_0(r,g)\). Equality holds only in rare cases: for odd \(g\), equality forces a **Moore graph** (girth 5 exists only for \(r\in\{2,3,7,57?\}\), the last open - problem 07); for even \(g\), equality forces the incidence graph of a **generalized polygon**, which exists only for \(g\in\{4,6,8,12\}\) and specific \(r\) (e.g. \(g=6\) needs a projective plane of order \(r-1\), which requires a prime-power order - no plane of order 6, so \(n(7,6)>n_0(7,6)=86\)).

Concrete Moore bounds relevant below:
\[
n_0(3,13)=1+3(1+2+4+8+16+32)=190,
\]
\[
n_0(7,6)=2(1+6+36)=86,
\]
\[
n_0(4,7)=1+4(1+3+9)=53,
\]
\[
n_0(5,6)=2(1+4+16)=42.
\]
For \((7,6)\), because no projective plane of order 6 exists, no graph attains 86; the true cage number therefore satisfies \(n(7,6)>86\), and the exact value is pinned only between the best excess-based lower bound and the best explicit construction (verify the current interval in the survey). This is the archetype of a "geometry-missing" open cage.

The Moore bound counts the vertices of a breadth-first tree of depth \(d=\lfloor(g-1)/2\rfloor\) rooted at a vertex (odd girth) or an edge (even girth): distinct up to depth \(d\) is exactly the girth condition, so any \((r,g)\)-graph has at least \(n_0(r,g)\) vertices. For girth 6 specifically, meeting the bound is equivalent to the existence of a projective plane of order \(r-1\); since planes are known only for prime-power orders (and are ruled out for order 6 and, conjecturally, several others), the family \(\{(r,6): r-1 \text{ not a prime power}\}\) is a systematic source of open cases - \((7,6)\) is the smallest.

The Moore bound is almost never met for \(g\ge 6\) other than in the generalized-polygon cases, and for odd \(g\ge 7\) it is essentially never met. When it is not met, better lower bounds come from **excess** and **parity** arguments (a graph exceeding the Moore bound by a small amount forces local structure that can be counted) and from exhaustive small-order search; better upper bounds come from explicit algebraic constructions. The cubic frontier illustrates the pattern (orders are the established cage numbers):

| \((3,g)\) | \(g=7\) | \(g=8\) | \(g=9\) | \(g=10\) | \(g=11\) | \(g=12\) | \(g=13\) |
|---|---|---|---|---|---|---|---|
| \(n(3,g)\) | 24 | 30 | 58 | 70 | 112 | 126 | open |
| Moore bound | 22 | 30 | 46 | 62 | 94 | 126 | 190 |

The pattern (Moore bound met only at \(g=8,12\), the generalized-polygon cases) makes plain why \(g=13\) is hard: the gap between the Moore bound and the truth widens with girth.

**Task.** Choose one **open** cage number \(n(r,g)\) - a pair for which the best known lower and upper bounds differ - and strictly improve one side of the interval with a certificate. Candidate open cases (re-verify current records against the Exoo–Jajcay dynamic cage survey before committing):

- \(n(3,13)\): the first open cubic cage (all \(n(3,g)\) are known for \(g\le 12\)); Moore bound 190, improved lower bound and best construction both above it (verify current values, roughly low-200s lower / high-200s upper);
- \(n(7,6)\): open because no projective plane of order 6 exists, so the Moore bound 86 is unattainable (verify current interval);
- \(n(4,7)\), and other \((r,g)\) with a known gap (verify each is still open - some "small" pairs are already settled).

Conventions fixed here: graphs are finite, simple, undirected, and \(r\)-regular with \(r\ge 3\); "girth exactly \(g\)" means the shortest cycle has length \(g\) (a graph of girth \(>g\) does **not** count as an \((r,g)\)-graph). Bipartite incidence graphs of geometries are allowed constructions when they meet the degree and girth conditions.

## 2. Resolution standard

Fix the chosen open pair \((r,g)\) with current best bounds \(L \le n(r,g) \le U\), \(L<U\).

**Upper-bound resolution (smaller construction).** An explicit \(r\)-regular graph of girth exactly \(g\) on \(m\) vertices with \(m<U\), given as a graph6 string or adjacency list, together with an independent verification that (i) every degree equals \(r\) and (ii) the girth is exactly \(g\) (no cycle of length \(<g\); a cycle of length \(g\) exists). This improves the upper bound to \(m\). If \(m=L\) the cage number is determined exactly.

**Lower-bound resolution (nonexistence at an order).** A proof that **no** \(r\)-regular graph of girth \(g\) exists on fewer than \(N\) vertices, for some \(N>L\), in a certified form:
- an **exhaustive isomorph-free enumeration** (canonical augmentation with nauty/Traces, or a girth-aware orderly generation) showing the class of \((r,g)\)-graphs on each order \(<N\) is empty; the generation tree and canonicity tests independently replayable; or
- a **DRAT/LRAT-certified UNSAT** proof of a Boolean encoding whose models are exactly the \((r,g)\)-graphs on a fixed order, with all symmetry-breaking justified.

**Named certified form.** Upper bound: graph6 witness plus an independent regularity-and-girth checker. Lower bound: a nauty-canonical isomorph-free enumeration replay, or a DRAT/LRAT UNSAT certificate checked by an independent verifier (`drat-trim` / `cake_lpr`).

**Not accepted as resolution.**
- A construction whose girth is not verified to be exactly \(g\) (a shorter cycle, or girth larger than \(g\), both disqualify).
- A record-tying construction (same order as the current best) presented as an improvement.
- A heuristic search (tabu, simulated annealing, genetic) that finds no smaller graph - absence of a find is not a nonexistence proof.
- A lower bound argument that is only asymptotic, or that assumes vertex-transitivity / a prescribed automorphism group, unless that assumption is itself proven necessary.
- Floating-point or unverified girth computations; any claimed girth must be checked exactly.
- A construction that is \(r\)-regular but not connected, or has a vertex of the wrong degree, presented as an \((r,g)\)-graph.
- A lower bound proved only for a restricted subclass (e.g. bipartite, or Cayley) presented as a bound on all \((r,g)\)-graphs.
- Improving a cage number that turns out to already be settled.

## 3. Graded partial-result targets

Ordered from reproducing the known frontier to a strict record improvement and, at the top, exact determination. Each target fixes a single \((r,g)\) and states its current interval before the run.

**P1 - Reproduce the frontier.** Independently reconstruct the known cages bracketing the target (e.g. verify \(n(3,12)=126\) via the generalized hexagon incidence graph, and the current record graphs for the chosen open pair) with your own regularity/girth checker, matching the survey's orders. *Certificate:* graph6 files plus an independent checker; SHA-256 manifest.

**P2 - Certified search model.** Build and validate a girth-constrained isomorph-rejection generator and/or a SAT encoding of "\(r\)-regular, girth \(\ge g\), order \(m\)", validated by reproducing a *known* small cage exactly (right order, empty below it). *Certificate:* round-trip on a solved pair with independent replay.

**P3 - Improve the lower bound by a small margin.** Certify nonexistence of an \((r,g)\)-graph at one order above the current proven lower bound (raise \(L\) by at least 1). *Certificate:* exhaustive enumeration or DRAT UNSAT at that order, independently replayable. Even a single-order gain on a geometry-missing pair is a genuine contribution.

**P4 - Structured construction near the record.** Produce an explicit \((r,g)\)-graph at or just above the current best order using an algebraic or voltage-graph / lift construction (Cayley graphs, biaffine planes, Sachs-type amalgams), with full girth verification. *Certificate:* graph6 witness plus independent checker. (A tie is a partial result; a strict improvement is P5.)

**P5 - Strict upper-bound improvement.** An explicit \((r,g)\)-graph on fewer vertices than the current record. *Certificate:* upper-bound resolution form above. (This improves the world record for the pair.)

**P6 - Exact determination.** Close the interval completely: a construction at order \(m\) plus a certified nonexistence proof below \(m\), giving \(n(r,g)=m\). *Certificate:* both forms above with independent replay. (Full resolution; expected only for the more tractable pairs.)

Each target must state, before the run, the current best interval \([L,U]\) it is attacking and the exact quantity it aims to change; a result that leaves \([L,U]\) unchanged (a tie, a re-derivation, a null search) is reported at its true grade, not promoted.

## 4. Known results and prior art

- **Foundations.** Cages were introduced by Tutte (1947); Erdős and Sachs (1963) proved existence for all \(r,g\) and gave general upper bounds (roughly, a graph of girth \(g\) exists on \(O(r^{g-2})\)-ish order), so every \(n(r,g)\) is finite and bracketed. Sachs and later authors gave amalgam constructions; the monotonicity lemma (the minimum order for girth \(\ge g\) is attained at girth exactly \(g\)) justifies working with the "girth \(\ge g\)" relaxation in searches.
- **Monotonicity and bipartite variants.** Bipartite \((r,g)\)-graphs (relevant for even \(g\)) and vertex-transitive cages are studied separately; a smaller bipartite or transitive example is an upper bound on the general cage number, but a lower bound proved only for such a subclass is not a general lower bound.
- **Cubic cages.** All \(n(3,g)\) are known for \(g\le 12\): \(n(3,3)=4, n(3,4)=6, n(3,5)=10\) (Petersen), \(n(3,6)=14\) (Heawood), \(n(3,7)=24\) (McGee), \(n(3,8)=30\) (Tutte–Coxeter), \(n(3,9)=58\) (Brinkmann–McKay–Saager, ~1995), \(n(3,10)=70\) (O'Keefe–Wong, ~1980), \(n(3,11)=112\) (Balaban construction, minimality by McKay–Myrvold–Nadon, ~1998), \(n(3,12)=126\) (Benson generalized hexagon, ~1966) (verify attributions/years). \(n(3,13)\) is **open**, the first open cubic case.
- **Generalized polygons.** For even girth, incidence graphs of projective planes (\(g=6\)), generalized quadrangles (\(g=8\)) and hexagons (\(g=12\)) give Moore-bound-meeting cages when the underlying geometry exists (prime-power orders). The absence of a projective plane of order 6 (Tarry / Bruck–Ryser) forces \(n(7,6)>86\), making \((7,6)\) open.
- **Records and lower bounds.** The **Exoo–Jajcay dynamic cage survey** (Electronic Journal of Combinatorics, dynamic survey DS16, periodically updated) is the authoritative running table of best-known constructions and lower bounds for all open \((r,g)\). Exoo, McKay, Myrvold, Nadon, Jajcay and others hold or held numerous records; lower bounds beyond the Moore bound come from parity/counting arguments and exhaustive small-order searches (verify all current numeric records against the live survey).
- **Lower-bound methods.** Beyond the Moore bound, the strongest general lower bounds come from **excess** arguments (a graph exceeding the Moore bound by \(t\) vertices forces a spectral/combinatorial deficiency in the distance partition) and from spectral and counting refinements (Biggs; and later authors). For specific pairs, exhaustive computer search establishes exact nonexistence at a given order (the mechanism behind proven cage numbers such as \(n(3,11)=112\)).
- **Construction methods.** Record upper bounds are built from Cayley graphs, graph lifts / voltage graphs, and incidence structures of generalized polygons and their truncations; Exoo has produced many record graphs via computer-assisted algebraic search over small groups. The best-known \((3,13)\)-graph and other records are catalogued (with their orders) in the Exoo–Jajcay survey.
- **Adjacent problem.** The girth-5 Moore-bound-meeting case is exactly the missing degree-57 Moore graph (problem 07); the two problems share the Moore-bound / generalized-polygon machinery.

**Status as of mid-2026 - re-verify against the current literature and the Exoo–Jajcay survey before starting any session.** Cage records drift: constructions and lower bounds in this area have improved repeatedly over the last two decades. Confirm the exact current interval for the chosen pair, and confirm it is still open, before committing compute.

## 5. Attack plan

First fix the target pair \((r,g)\) and record, with its survey source, the current best interval \([L,U]\). Then split into an upper-bound (construction) and a lower-bound (nonexistence) workstream; a session may pursue either or both.

**Construction side (`[search]`).** Target algebraic and lift constructions on one workstation: Cayley graphs over small groups with girth screened algebraically; voltage graphs / regular covers of small base graphs (McKay–Myrvold-style), where girth is controlled by the voltage assignment; biaffine and incidence-geometry amalgams. Generate candidates with SageMath/GAP, screen girth with an exact BFS-per-vertex girth routine, and keep only exact-\(g\) graphs. For a strict record attempt, exhaust a parameterized family rather than sampling.

**Excess and spectral pruning.** Before a raw search, apply the excess/parity bound for the chosen \((r,g)\): compute the exact deficiency a hypothetical graph at order \(m\) would carry relative to the Moore tree, and use it to forbid orders outright or to force local structure (a fixed number of extra vertices at each distance level) that seeds the isomorph-rejection tree. This is often the difference between a hopeless and a feasible lower-bound search.

**Isomorph rejection discipline.** In the enumeration, every partial graph is reduced to a canonical form (nauty/Traces) so that isomorphic partials are generated once; the canonical labelling and the augmentation rule together give a proof-carrying search tree whose completeness is auditable. A pruning step is admissible only if its reason is local and independently checkable (a short cycle present, a degree overflow, an excess violation) - never a heuristic score.

**SAT vs enumeration tradeoff.** For the smallest orders a direct isomorph-free enumeration is both fastest and easiest to audit; as the order grows, a SAT encoding with cube-and-conquer splitting and DRAT output may reach further but at the cost of a larger, harder-to-read certificate. Choose per order and record the choice; where feasible, corroborate a SAT UNSAT with a partial enumeration on the same sub-space.

**Nonexistence side (`[search]`).** Girth-constrained isomorph-free generation with nauty/Traces via canonical augmentation: grow the graph vertex-by-vertex, rejecting any partial graph that already contains a cycle shorter than \(g\) or cannot be completed to \(r\)-regular within the order budget. Alternatively, a SAT encoding with adjacency Booleans, degree cardinality constraints, and short-cycle-forbidding clauses (all length-\(<g\) closed walks excluded); run CaDiCaL / kissat / CryptoMiniSat, emit DRAT, convert to LRAT, and check independently. Symmetry-breaking must be sound and justified.

**Construction search in practice.** For an upper-bound attempt, fix a small group \(H\) and search connection sets (Cayley) or voltage assignments (lifts of a small base graph) so that the shortest relation has length \(\ge g\); this reduces a large graph search to a search over algebraic data of modest size, tractable on one workstation. Screen each candidate's girth exactly and keep only girth-\(g\) graphs strictly below the current record order.

**Smaller solved analogues.** Validate the entire pipeline on a *known* cage before the open target: reproduce, say, \(n(3,11)=112\) (both the record graph and the certified nonexistence below 112, if attempting a lower bound) end to end. A generator that cannot re-derive a settled cage number is not trusted at the open pair, and a construction search that cannot rediscover a known record graph is not trusted to beat it.

**Girth computation at scale.** The dominant cost in both directions is the exact girth check. Use a per-vertex truncated BFS to depth \(\lfloor g/2\rfloor+1\) with early termination on the first short cycle; batch over vertices with bitset adjacency. Correctness of this routine is load-bearing (a bug produces false records or false nonexistence), so it is one of the two independently re-implemented checkers.

**One-workstation scope and failure modes.** A single workstation can: verify record graphs; run construction families of moderate size; and certify nonexistence at small orders (the \((3,13)\) lower-bound frontier is near the edge of feasibility and any gain is significant). It **cannot** exhaustively enumerate \((3,13)\)-graphs across the whole open interval - the space is enormous - so lower-bound progress will be incremental (one order at a time) and upper-bound progress will come from structured constructions, not blind search. Expect: girth routines that are correct but slow at scale (optimize the short-cycle check); SAT encodings that blow up without good symmetry-breaking; and construction families that plateau at the current record. Report ties and null searches as partial results, not as improvements.

The most compute-efficient targets on one workstation are the geometry-missing girth-6 cases (e.g. \((7,6)\)), where the excess argument gives strong local structure and the search space, while large, is far smaller than the odd-girth cages; and construction attempts for any pair with a promising small-group Cayley/lift landscape. The odd-girth cubic frontier \((3,13)\) is the most storied but among the least tractable for a full determination.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Regularity and girth verified by exact integer BFS/adjacency computation; nonexistence claims backed by isomorph-free enumeration replay or DRAT/LRAT. No floating point in any certified claim.
2. **Independent verification.** A standalone regularity-and-girth checker, written separately from the generator, validates every construction. Nonexistence enumerations are re-run with a fresh nauty invocation to reproduce canonical-form counts; SAT UNSAT proofs are checked by an independent verifier.
3. **Reproducibility.** All construction parameters (groups, voltages, generators), generator flags, solver versions, seeds, and environment recorded; SHA-256 manifest over every graph6 file, encoding, proof trace, and log. The current best interval \([L,U]\) claimed as the baseline is recorded with its survey source and access date.
4. **Preservation.** Construction and search source code is part of the record. Any assumption used to prune (vertex-transitivity, prescribed symmetry, fixed subgraph) is stated explicitly as a scope limit - the Hadamard-668 lost-source lesson.
5. **Honest reporting.** The report states up front whether an open cage number was strictly improved (which side, by how much) or only tied/reproduced. A record-tying graph or a failed nonexistence search is reported as a partial result and never represented as improving the cage number.

### Calibration

Exact determination of an open cage number (P6) is rare and hard; the realistic session product is a **single-side improvement** - a construction one or more vertices below the record (P5), or a lower bound raised by at least one order (P3) - each of which is a genuine, publishable contribution to the Exoo–Jajcay survey. A record *tie* or a failed search is not an improvement and is reported as such. Pick the pair to match the mode: lower-bound work favours pairs whose current interval sits near the feasibility edge of exhaustive search (small \(r\), moderate \(g\)); upper-bound work favours pairs with a rich algebraic construction landscape.
