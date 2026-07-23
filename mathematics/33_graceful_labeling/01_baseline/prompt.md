# PROMPT FOR THE GRACEFUL TREE CONJECTURE

## Extending certified verification, or proving gracefulness for a new tree class

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 33 of 50  
**Area:** graph theory  
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The graceful tree conjecture (Ringel–Kotzig, ~1964) asserts that every tree admits a graceful labeling: a vertex labeling by distinct integers in \(\{0,\dots,m\}\), where \(m\) is the number of edges, inducing all edge labels \(\{1,\dots,m\}\) exactly once. It is verified by computer for all trees up to roughly 35 vertices and proven for several structured tree families (paths, caterpillars, and more), yet open in general. This is an unusually clean finite-search problem: a graceful labeling is a single object checked in linear time, and "all trees on \(n\) vertices are graceful" is an exhaustive statement over the isomorph-free list of free trees (generated completely by nauty's `gentreeg`). It is well matched to current AI methods - per-tree constraint/SAT search for the labeling, plus certified-complete tree generation. The resolution standard in section 2 is the target: either extend the certified verification to more vertices with a replayable exhaustive certificate, or prove gracefulness for a genuinely new tree class. A large sample of graceful trees, or an un-replayable search, is reported only as a partial result.

## 1. Exact problem statement

A **tree** is a connected acyclic finite simple graph. Let \(T\) be a tree with vertex set \(V\), \(|V|=m+1\), and edge set \(E\), \(|E|=m\). A **graceful labeling** of \(T\) is an injective map
\[
f:V\to\{0,1,\dots,m\}
\]
such that the induced edge labels
\[
\{\,|f(u)-f(v)| : uv\in E\,\}=\{1,2,\dots,m\}
\]
(all \(m\) edge labels are distinct, hence a bijection onto \(\{1,\dots,m\}\)). Since \(|V|=m+1\) and \(f\) is injective into a set of size \(m+1\), \(f\) is a bijection onto \(\{0,\dots,m\}\); gracefulness is the additional requirement that the edge differences hit every value \(1,\dots,m\). A tree is **graceful** if it has a graceful labeling.

A strengthening used throughout the theory: an **\(\alpha\)-labeling** (Rosa) is a graceful labeling with a boundary value \(k\) such that every edge \(uv\) has \(\min(f(u),f(v))\le k<\max(f(u),f(v))\); \(\alpha\)-labelings are bipartite-respecting and yield cyclic decompositions.

**Graceful Tree Conjecture (GTC).** Every tree is graceful.

**Task.** Choose one:
- **(Verification extension)** Prove, by exhaustive isomorph-free search, that every tree on \(n\) vertices is graceful, for an \(n\) beyond the current certified record.
- **(New class)** Prove that every tree in a structurally defined family not previously settled is graceful (e.g. lobsters, or a specified subclass thereof; caterpillars are already done).

Related labelings (harmonious, \(\alpha\)-, and the Kotzig–Ringel decomposition consequence) are context, not the target, unless used as a tool.

## 2. Resolution standard

**Verification-extension resolution.** For a specific \(n\) beyond the current record, a proof that **every** tree on \(n\) vertices is graceful, certified by:
- a **complete isomorph-free enumeration** of all free trees on \(n\) vertices (nauty `gentreeg`, whose output is certified complete and non-isomorphic), the count matching the known number of trees on \(n\) vertices (OEIS A000055); and
- for **each** such tree, an explicit graceful labeling, independently verified (injectivity into \(\{0,\dots,m\}\) and edge-label bijection onto \(\{1,\dots,m\}\)), the collection stored and replayable.

Equivalently, per-tree gracefulness may be certified by a SAT/CP model whose satisfying assignment is the labeling (with a DRAT proof only needed if a tree were claimed **non**-graceful - which would refute GTC and demands the strongest certificate).

**New-class resolution.** A complete mathematical proof that every tree in the specified family is graceful - a general labeling construction with a correctness proof covering all members - ideally with the construction formalized or at least validated exhaustively on all small members via the enumeration above.

**Named certified form.** Verification extension: nauty `gentreeg` complete enumeration replay (count matched to A000055) plus a per-tree graceful-labeling checker. New class: a written (ideally formalized) constructive proof plus exhaustive validation on all small members.

**Not accepted as resolution.**
- A large **sample** of graceful trees (random or heuristic) presented as verifying an order - the enumeration must be provably complete for that \(n\).
- A verification whose tree list is not certified complete/isomorph-free, or whose labelings are not independently re-checked.
- A near-graceful or "graceful except one edge" labeling counted as graceful.
- A construction for a class that covers only "most" members or omits boundary cases.
- Reproducing the known record \(n\) without extending it, presented as new.
- Any claim of a non-graceful tree (a refutation of GTC) without an exhaustive, DRAT-certified nonexistence proof for that specific tree - this is an extraordinary claim requiring the strongest certificate.

## 3. Graded partial-result targets

**P1 - Reproduce the verification frontier.** Independently re-verify that all trees on \(\le n_0\) vertices are graceful, where \(n_0\) is the current certified record, with your own complete `gentreeg` enumeration (count matched to A000055) and an independent labeling checker. *Certificate:* the enumeration replay plus stored per-tree labelings; SHA-256 manifest. This confirms the toolchain before pushing further.

**P2 - Certified per-tree solver.** Build and validate a graceful-labeling search (backtracking with difference-set pruning, or a SAT/CP model) that finds a labeling for any tree quickly, validated on all trees up to \(n_0\). *Certificate:* round-trip on the settled range with independent labeling verification.

**P3 - Extend the verification by one or more \(n\).** Prove every tree on \(n_0+1\) (and, compute permitting, further) vertices is graceful, via complete enumeration plus per-tree labeling. *Certificate:* verification-extension resolution above. *This is the flagship finite product.* (The number of trees grows fast - A000055 roughly multiplies by ~2.5 per vertex - so each additional \(n\) is a substantial, publishable step.)

**P4 - New structured class, small validation.** Give a candidate graceful-labeling construction for a new class (a lobster subfamily, a spider/olive-tree variant, symmetric trees, or bounded-degree caterpillar generalizations) and validate it exhaustively on all members up to some order. *Certificate:* the construction plus exhaustive small-order validation with independent checking.

**P5 - New class, full proof.** Prove gracefulness for a genuinely new tree family with a general construction and correctness proof (e.g. a settled subclass of lobsters). *Certificate:* a written proof, formalized where practical, plus exhaustive validation on small members. (Full resolution for that class.)

**P6 - α-labeling strengthening.** For a class where gracefulness is known, prove the stronger \(\alpha\)-labeling (which yields cyclic decompositions and feeds the Ringel/Kotzig–Ringel program), or extend the \(\alpha\)-labeling frontier. *Certificate:* construction plus proof, with small-order validation.

## 4. Known results and prior art

- **Origin.** Ringel (1963) and Kotzig posed the conjecture; Rosa (1967) introduced graceful labelings under the name **\(\beta\)-valuations**, along with \(\alpha\)-, \(\sigma\)-, and \(\rho\)-labelings and the connection to cyclic decompositions of complete graphs. Golomb coined the term "graceful". The **Kotzig–Ringel** consequence: if every tree with \(m\) edges is graceful, then \(K_{2m+1}\) decomposes into \(2m+1\) copies of that tree (verify statement).
- **Settled classes.** Paths, stars, caterpillars (Rosa), symmetrical trees, complete binary trees, spiders/olive trees, and many others are proven graceful; **lobsters** (trees whose removal of leaves yields a caterpillar) are conjectured graceful (Bermond) and open in general, with numerous subclasses settled (verify which). Gallian's **Dynamic Survey of Graph Labeling** (Electronic Journal of Combinatorics, updated regularly) is the authoritative running catalogue of settled classes and records.
- **Computer verification.** Aldred and McKay (~1998) verified GTC (and harmonious labelings) exhaustively for all trees up to around 26–27 vertices using nauty-based tree generation; Horton and others extended the range; W. Fang (~2010) reported verification of all trees up to about 35 vertices via a hybrid deterministic/randomized search (verify the exact record and whether the largest orders are exhaustive or sampled - this distinction is central to the resolution standard here).
- **Adjacent notions.** Harmonious labelings (Graham–Sloane) and the general labeling zoo are surveyed by Gallian; the Ringel decomposition conjecture (recently resolved asymptotically by Montgomery, Pokrovskiy, Sudakov for large \(n\)) is related but distinct (verify).

**Status as of mid-2026 - re-verify against the current literature and Gallian's survey before starting any session.** The verification record and the list of settled classes move; confirm the current exhaustively-verified \(n\) (distinguishing exhaustive from sampled), the state of the lobster conjecture, and which subclasses remain open before committing compute.

## 5. Attack plan

**Complete tree generation (`[search]`).** Generate all free trees on \(n\) vertices with nauty's `gentreeg` (certified complete and isomorph-free); confirm the count against OEIS A000055 as an integrity check. This is the backbone of any verification-extension claim - the completeness of the list, not the search, is what makes the result a proof.

**Per-tree gracefulness search.** For each tree, find a graceful labeling by backtracking with strong pruning: assign labels to vertices while maintaining the set of used differences, prune on parity/difference-multiset feasibility, exploit the forced endpoints (some vertex gets 0, some gets \(m\), and the edge of difference \(m\) joins them). Alternatively a SAT/CP model with an all-different constraint on vertex labels and on edge differences. The labeling is a linear-time-checkable witness, so search cost dominates and completeness of the tree list dominates correctness.

**New-class constructions.** For a target family (a lobster subclass, spiders, symmetric trees), develop a parameterized labeling scheme (often a "transfer" or "component-shifting" construction, or an \(\alpha\)-labeling glued along a spine) and prove it graceful in general; validate exhaustively on all small members from `gentreeg` filtered to the class.

**One-workstation scope and failure modes.** A single workstation can: regenerate and re-verify the known frontier; extend the exhaustive verification by one or a few \(n\) (bounded by the A000055 growth - the tree count roughly multiplies by ~2.5 each step, so the compute wall arrives fast); and prove/validate new-class constructions. It **cannot** verify very large \(n\) exhaustively, and it cannot prove GTC in general. Expect: a small number of "hard" trees per order whose labeling search is slow (invest in pruning and, if needed, a per-tree SAT fallback); the exhaustive-vs-sampled distinction being the crux of whether a record is a proof; and new-class constructions that work on all tested members but resist a clean general proof at the boundary. Report the exhaustively-verified \(n\) precisely and never conflate it with a sampled range.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Tree lists generated by a certified-complete isomorph-free generator (`gentreeg`), counts matched to A000055; every graceful labeling verified by exact integer checks (injectivity and edge-label bijection). Any non-graceful claim requires a DRAT-certified exhaustive nonexistence proof for that tree.
2. **Independent verification.** A standalone labeling checker, written separately from the search, re-verifies every stored labeling; the tree enumeration is replayed independently and its count re-matched to A000055; new-class constructions are validated exhaustively on small members by the independent checker.
3. **Reproducibility.** All generation commands, search parameters/seeds, solver/CAS versions, and environment recorded; SHA-256 manifest over the tree lists, the stored labelings, and logs.
4. **Preservation.** Generation and search source code, and all stored labelings, are part of the record; if any order's verification used sampling rather than full enumeration, that is stated explicitly and the order is **not** claimed as exhaustively verified - the Hadamard-668 lost-source lesson and the exhaustive-vs-sampled honesty requirement together.
5. **Honest reporting.** The report states up front the exact \(n\) up to which every tree is **exhaustively** verified graceful, distinguishes it from any sampled range, names any new class proved graceful, and never represents a sample or a near-graceful labeling as resolving an order or the conjecture.
