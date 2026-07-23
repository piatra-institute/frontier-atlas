# PROMPT FOR CERTIFYING SMALL-ORDER LATIN-SQUARE TRANSVERSALS AND MAPPING THE RESIDUAL GAP

## The Ryser–Brualdi–Stein transversal conjecture after Montgomery's large-\(n\) theorem

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 47 of 50
**Area:** order theory & extremal set systems
**Modes:** `[search]` `[proof]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Every Latin square of order \(n\) is conjectured to contain a partial transversal of size \(n-1\), and a full transversal of size \(n\) when \(n\) is odd. This is a finite, machine-checkable statement per instance - for any given square a transversal is an exact-cover certificate - but a universal one over all \(n\).

The status changed materially in 2023: Montgomery proved the size-\((n-1)\) bound for all *sufficiently large even* \(n\). That result is asymptotic; it leaves the small and moderate orders, the odd-order full-transversal (Ryser) claim, and the fully general all-\(n\) statement outside its reach, and its "sufficiently large" threshold is far beyond any explicit computation.

**The mandatory first step of any session is a literature gate** (section 3, P0) that re-establishes exactly what Montgomery and successors proved before any target is pursued. This prompt is scoped to certified small-order ground truth and a precise map of the residual gap - never to a claim on the asymptotic part, which is not this program's to re-earn.

## 1. Exact problem statement

A **Latin square** of order \(n\) is an \(n\times n\) array \(L=(L_{ij})_{i,j\in[n]}\) with entries in \([n]=\{1,\dots,n\}\) such that
\[
\{L_{i1},\dots,L_{in}\}=[n]\ \ \text{for each row }i,
\qquad
\{L_{1j},\dots,L_{nj}\}=[n]\ \ \text{for each column }j.
\]

A **partial transversal of size \(k\)** is a set of \(k\) cells \(\{(i_1,j_1),\dots,(i_k,j_k)\}\) with
\[
i_s\ \text{pairwise distinct},\qquad j_s\ \text{pairwise distinct},\qquad L_{i_s j_s}\ \text{pairwise distinct}.
\]
A **full transversal** is a partial transversal of size \(n\); equivalently it is a permutation \(\sigma\in S_n\) with
\[
\bigl\{\,L_{i,\sigma(i)}:i\in[n]\,\bigr\}=[n],
\]
one cell per row and column carrying each symbol once. Write \(t(L)\) for the maximum size of a partial transversal of \(L\).

**Conjecture (Ryser–Brualdi–Stein).**
\[
\textbf{(Brualdi–Stein)}\quad t(L)\ \ge\ n-1\ \ \text{for every Latin square }L;
\qquad
\textbf{(Ryser)}\quad t(L)=n\ \ \text{when }n\ \text{is odd}.
\]

Oddness is necessary in Ryser's part. For the Cayley table \(L_{ij}=i+j\pmod n\) of \(\mathbb Z_n\), a full transversal is a permutation \(\sigma\) with \(\{i+\sigma(i)\}=\mathbb Z_n\); summing over \(i\),
\[
\sum_{i\in\mathbb Z_n}\bigl(i+\sigma(i)\bigr)=2\sum_{i}i,
\qquad
\sum_{i}\bigl(i+\sigma(i)\bigr)\equiv\sum_{r\in\mathbb Z_n} r=\tfrac{n(n-1)}{2}\pmod n,
\]
and \(2\sum_i i=n(n-1)\equiv0\), so a transversal forces \(\tfrac{n(n-1)}{2}\equiv0\pmod n\), which **fails for even \(n\)**. Hence \(n-1\) is best possible for even orders.

**Computational reformulation.** Encode \(L\) as the set of triples \(\mathcal T=\{(i,j,L_{ij})\}\subset[n]^3\). A partial transversal of size \(k\) is a subset of \(\mathcal T\) of size \(k\) with all first, all second, and all third coordinates distinct - i.e. a matching of size \(k\) in the \(3\)-partite \(3\)-uniform hypergraph on rows, columns, symbols. Thus
\[
t(L)=\nu_3(\mathcal T)\quad(\text{maximum }3\text{-dimensional matching}),
\]
and deciding \(t(L)\ge s\) is an exact-cover / matching decision, well suited to DLX and SAT.

Stein's original conjecture is the stronger *array* statement - any \(n\times n\) array using \(n\) symbols each exactly \(n\) times has a partial transversal of size \(n-1\) - which is now known to be **false** in that general form (verify the disproving reference); the Latin-square case (Brualdi–Stein) is the surviving conjecture and the object here.

Compactly, the conjecture is
\[
t(L)\ \ge\ n-1\ \ \text{for all }L,
\qquad
t(L)=n\ \ \text{for all }L\text{ of odd order},
\]
with the even-order Cayley tables showing \(t(L)=n-1\) is attained.

No informal reading is admissible: a claimed transversal is the explicit list of cells, and \(t(L)\ge n-1\) for a fixed \(L\) is decided exactly by an exact-cover / maximum-matching computation.

## 2. Resolution standard

The full conjecture, as a theorem for **all** \(n\), remains open (Montgomery's theorem is asymptotic and even-order). Two things count as resolving what remains:

- **(Affirmative, all \(n\))** a proof valid for every \(n\) of both parts - closing the gap between "sufficiently large" and small/moderate \(n\), and settling odd-order full transversals for all \(n\). The residual is infinite, so this is a **proof** (Lean-formalizable), not a search.
- **(Negative)** an explicit Latin square \(L_0\) with \(t(L_0)\le n-2\), or an odd-order square with no full transversal - a finite object with an exact-cover **non-existence certificate** (a DRAT/LRAT UNSAT proof that no partial transversal of the target size exists).

**Certified form.** For the search targets the accepted artifact is a **certified transversal audit** for a fixed order \(n\):

- an explicit size-\((n-1)\) partial transversal (and, for odd \(n\), a full transversal) for a specific hard square, cells listed and machine-verified; or
- an **exhaustive isomorph-free certificate** that every Latin square of order \(n\) satisfies the conjecture, replayable over a canonical set of species/main-class representatives, with a DRAT UNSAT proof discharging each "no transversal of size \(s\)" subproblem.

**Not accepted as resolution.**

- Citing Montgomery (2023) as "the conjecture is solved". It is not: the theorem is large-even-\(n\), size \(n-1\) only.
- An asymptotic or "almost all Latin squares" result represented as the all-\(n\) statement.
- A floating-point / heuristic transversal search without an explicit verified cell set, or an existence claim without a certificate.
- Verifying one square, or one order, and calling the conjecture confirmed.
- Any target that re-derives or restates the asymptotic theorem and presents it as new institute work.

## 3. Graded partial-result targets

- **P0 - literature gate (mandatory, first action).**
  Before any computation, establish in writing, with citations: (i) the exact statement of Montgomery (2023, arXiv 2310.19779) - large even \(n\), transversal of size \(n-1\); (ii) the current status of the **odd-\(n\) full-transversal** (Ryser) part for large \(n\), who proved it and under what threshold (verify); (iii) any post-2023 work lowering thresholds or covering new orders.
  *Certificate:* a dated status memo naming references and marking each sub-claim proved / open. No later target proceeds until P0 is fixed.

- **P1 - reproduce small-order ground truth.**
  Certified exhaustive verification that every Latin square of order \(n\le8\) has \(t(L)\ge n-1\), and a full transversal for odd \(n\le7\), by isomorph-free enumeration of main-class (species) representatives and exact transversal search.
  *Certificate:* replay log per representative with a witnessed size-\((n-1)\) transversal (cells), plus the species count matching McKay–Wanless data as a completeness check.

- **P2 - extend the certified frontier.**
  Push the exhaustive certified verification to \(n=9\) (and toward \(n=10,11\) as far as species enumeration allows) using canonical representatives and SAT/ILP transversal existence with **DRAT proofs** for each decision.
  *Certificate:* isomorph-free representative set with completeness argument, DRAT traces, and independent replay of a sample.

- **P3 - transversal-free catalogue (even orders).**
  Enumerate small even-order Latin squares with **no** full transversal, verifying tightness of the \(n-1\) bound and characterizing the transversal-free families beyond the Cayley table of \(\mathbb Z_n\).
  *Certificate:* exact list of representatives with DRAT UNSAT proofs of "no full transversal" and verified size-\((n-1)\) transversals.

- **P4 - residual-gap map.**
  A precise, citable delineation of exactly what is open after Montgomery: the small/moderate \(n\) not covered, the odd-order full-transversal status per \(n\), and the all-\(n\) statement - each entry marked *certified-closed here*, *closed in literature*, or *open*.
  *Certificate:* a table backed by P1–P3 certificates and P0 citations.

- **P5 - certified structural lemma or record.**
  A machine-checked statement useful to a small-\(n\) attack: a reduction lemma (Lean-formalizable) narrowing which squares can fail, or a certified extremal/near-extremal family attaining exactly \(n-1\).
  *Certificate:* Lean proof term or exact enumeration with completeness.

- **P6 - formalize a settled small case in Lean.**
  A kernel-checked proof of the conjecture for a fixed small odd \(n\) (full transversal) or the \(n-1\) bound for a fixed \(n\).
  *Certificate:* the Lean development.

## 4. Known results and prior art

- **Origins.** Ryser (1967, odd-order full transversal); Brualdi (the \(n-1\) conjecture, in Brualdi–Ryser 1991); Stein (1975, the general-array form).
- **Lower bounds on \(t(L)\).** \(n-O(\sqrt n)\) (Woolbright 1978; Brouwer–de Vries–Wieringa 1978); \(n-O(\log^2 n)\) (Shor 1982; corrected Hatami–Shor 2008); \(n-O(\log n/\log\log n)\) (Keevash–Pokrovskiy–Sudakov–Yepremyan, approx. 2020–2022, verify).
- **Montgomery (2023, arXiv 2310.19779).** For all sufficiently large **even** \(n\), every Latin square of order \(n\) has a partial transversal of size \(n-1\). The **odd-\(n\) full-transversal** part and all small/moderate \(n\) are not settled by this paper (verify whether a companion or later result covers large odd \(n\)).
- **Stein's general array conjecture** was disproved by constructions of arrays with no near-transversal (verify the reference, approx. Pokrovskiy–Sudakov / Montgomery–Pokrovskiy–Sudakov). The Latin-square case is unaffected.
- **Small-order data.** Counts of Latin squares, isotopy classes, and main classes are tabulated to \(n=11\) (McKay–Wanless); these are the completeness anchors for exhaustive verification. The number of main classes (species) grows as
\[
n=7:\ 147,\quad n=8:\ 283{,}657,\quad n=9:\ \approx1.9\times10^{7},\quad n=10:\ \approx3.4\times10^{10}\ (\text{verify}),
\]
which fixes the exhaustive-verification horizon at roughly \(n=9\) on a workstation.
- **Adjacent.** Alon–Tarsi (#43) and Rota's basis conjecture (#44) sit in the same Latin-square / transversal neighborhood.

**Status as of mid-2026 - re-verify against the current literature before starting any session.** This is the problem in the set most changed by recent work; P0 exists precisely because the asymptotic frontier moved in 2023 and may have moved again. Confirm Montgomery's exact statement, the odd-order status, and any threshold reductions before scoping targets.

## 5. Attack plan

- **`[search]` enumeration.** Obtain or generate main-class / isotopy-class representatives (McKay–Wanless tables; or generate with `nauty`-backed canonical forms under the paratopy group). SageMath / GAP for Latin-square manipulation.
- **Transversal search as exact cover.** A full transversal is an exact-3-cover (rows, columns, symbols); solve existence with Knuth's DLX or a SAT encoding. Maximum partial transversal is a 3-dimensional matching optimization; decide \(t(L)\ge s\) by SAT/ILP. For non-existence (tightness, or a hypothetical counterexample) emit a **DRAT/LRAT** proof of UNSAT.
- **`[proof]` formalization.** Lean 4 + mathlib for P5/P6 reduction lemmas and small fixed-\(n\) cases; combinatorial-design support in mathlib is limited (failure mode).
- **One-workstation scope.** Exhaustive over main classes is comfortable through \(n=8\) (\(283{,}657\) species) and feasible at \(n=9\) (\(\approx1.9\times10^{7}\) species); \(n=10\) (billions of main classes) is **not** exhaustively feasible on a workstation, so \(n\ge10\) work is restricted to structured subfamilies (group tables, known hard squares) and random hard instances, stated as such.
- **Failure modes.** Enumeration explosion past \(n=9\); SAT scaling for the maximum-transversal optimization; canonical-form correctness (a bug voids completeness); mistaking a subfamily result for an exhaustive one.

## 6. Verification and auditability requirements

1. **Exact/certified computation.** Transversal existence and non-existence are decided by exact combinatorial search; every non-existence claim carries a DRAT/LRAT proof, every existence claim an explicit verified cell set. No floating point enters a certificate.
2. **Independent verification.** A standalone checker, independent of the search, validates each listed transversal (distinct rows, columns, symbols) and runs a DRAT checker (e.g. `drat-trim`) on every UNSAT proof; species counts are cross-checked against published tables.
3. **Reproducibility.** Representative sets, canonical-form definitions, encodings, solver versions, and seeds recorded; SHA-256 manifest over every representative file, certificate, and proof trace.
4. **Preservation.** Enumeration and encoding source is part of the record (the Hadamard-668 lost-source lesson). Any order left only partially covered (e.g. \(n=10\) subfamilies) is stated explicitly, not implied complete.
5. **Honest reporting.** The report leads with the P0 status memo and states plainly that Montgomery's theorem is asymptotic and even-order; institute results are certified small-order verifications and a residual-gap map, never a claim on the general or asymptotic statement.

### Honest calibration

Montgomery closed the headline for large even \(n\); this program cannot and should not try to re-earn or extend the asymptotic result in a session. The honest deliverable is trustworthy small-order ground truth (P1–P3) and a precise, well-cited map of what remains open (P4) - modest, exact, and durable. P5–P6 are stretch goals; the all-\(n\) proof is not on the table here.
