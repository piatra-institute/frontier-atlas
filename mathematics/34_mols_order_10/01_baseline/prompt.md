# PROMPT FOR DETERMINING WHETHER THREE MOLS OF ORDER 10 EXIST

## The maximum number of mutually orthogonal Latin squares of order ten, \(N(10)\)

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 34 of 50  
**Area:** designs & codes  
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Two orthogonal Latin squares of order 10 exist - Bose, Shrikhande and Parker disproved Euler's conjecture in 1959 - but whether **three** mutually orthogonal Latin squares of order 10 exist has been open for more than sixty years. This is the flagship small case of the MOLS problem and a sibling of the projective-plane-of-order-12 problem (04): a projective plane of order \(n\) is equivalent to a complete set of \(n-1\) MOLS\((n)\).

The question is a crisp, finite, machine-checkable decision problem - a triple can be verified exactly in milliseconds, and constructive or symmetry-restricted nonexistence searches are exactly the certified/SAT and exact-enumeration work this program targets. The resolution standard in section 2 is the goal; anything short of it - a symmetry-restricted nonexistence, a reproduced pair, an incomplete search - is reported as a partial result and never represented as settling the trichotomy \(N(10)=2\) versus \(N(10)\ge 3\).

## 1. Exact problem statement

A **Latin square** of order \(n\) is an \(n\times n\) array \(L=(L_{ij})\), with \(i,j\in[n]:=\{0,\dots,n-1\}\) and entries in a symbol set \(S\), \(|S|=n\), such that every symbol occurs exactly once in each row and exactly once in each column. Fix \(S=[n]\).

Two Latin squares \(L,L'\) of order \(n\) are **orthogonal** if the map
\[
[n]\times[n]\ \longrightarrow\ [n]\times[n],\qquad (i,j)\ \longmapsto\ \bigl(L_{ij},\,L'_{ij}\bigr)
\]
is a bijection; equivalently the \(n^2\) ordered pairs \((L_{ij},L'_{ij})\) are pairwise distinct and hence exhaust \([n]\times[n]\).

A set \(\{L^{(1)},\dots,L^{(k)}\}\) of Latin squares of order \(n\), pairwise orthogonal, is a set of \(k\) **mutually orthogonal Latin squares** (MOLS). Write
\[
N(n)=\max\{k:\ \text{a set of } k \text{ MOLS of order } n \text{ exists}\}.
\]

Always \(N(n)\le n-1\), with equality iff a projective plane (equivalently an affine plane, equivalently a complete set of MOLS) of order \(n\) exists.

**Equivalent objects.** These reformulations are used freely and each gives a distinct search handle:

- A set of \(k\) MOLS\((n)\) is equivalent to a **transversal design** \(\mathrm{TD}(k+2,n)\).

- It is equivalent to an **orthogonal array** \(\mathrm{OA}(n^2,k+2,n,2)\) of index 1.

- It is equivalent to a **\((k+2)\)-net** of order \(n\); net-completion theory (Bruck) bounds how large \(k\) can be before a plane is forced.

- It is equivalent to a set of \(k\) pairwise **disjoint common transversals** structure on a single square; for the triple case, a common orthogonal mate must decompose two squares' transversals simultaneously.

The paratopism group acting on a MOLS set of order \(n\) with \(k\) squares has order \((n!)^{3}\cdot 2\cdot k!\) at most (before quotienting by stabilisers), so isomorph rejection is essential to keep any enumeration finite in practice.

**The open question.** Is \(N(10)\ge 3\)? Equivalently, do there exist three Latin squares of order 10 that are pairwise orthogonal? A `yes` is witnessed by an explicit triple; a `no` asserts \(N(10)=2\).

**Conventions fixed so the problem starts from the prompt alone.**

- *Equivalence.* MOLS sets are considered up to the **paratopism / main-class** action: row permutations, column permutations, and symbol permutations applied independently to each square, permutation of the three coordinate roles, and permutation of the \(k\) squares among themselves. Orthogonality is invariant under all of these, so any reported nonexistence must state the group it quotients by.

- *Normalisation.* A single square may be reduced (first row and first column in natural order) without loss, but the normalisation and its effect on the search must be declared and accounted for.

## 2. Resolution standard

A **complete resolution** is one of:

- **(A) Existence.** An explicit triple \(\{L^{(1)},L^{(2)},L^{(3)}\}\) of order-10 Latin squares, given as three \(10\times10\) integer arrays, together with an independent checker verifying in exact integer arithmetic that (i) each array is Latin and (ii) each of the three pairs is orthogonal (all 100 ordered pairs distinct). This proves \(N(10)\ge 3\) and settles the headline question.

- **(B) Nonexistence.** A proof that no three MOLS of order 10 exist (hence \(N(10)=2\)), either by a complete isomorph-free exhaustive search carrying a machine-checkable completeness certificate, or by a mathematical argument reducible to independently verifiable finite computations.

Determining \(N(10)\) *exactly* additionally fixes the upper side; but the headline open problem is precisely the trichotomy \(N(10)=2\) versus \(N(10)\ge3\).

**Named certified forms accepted.**

- Exhaustive isomorph-free enumeration via orderly generation or `nauty`/`Traces` canonical forms, with a replay checker that re-derives the same canonical set.

- SAT/CP encodings whose **UNSAT** claims carry DRAT/LRAT proofs for symmetry-restricted nonexistence.

- Exact finite arithmetic for every Latin and orthogonality check.

**Not accepted as resolution.**

- A pair of MOLS(10) (already known since 1959).

- A triple whose orthogonality was checked only in floating point, or by the same code that produced it, without an independent exact re-check.

- A "near-orthogonal" triple in which some pair repeats a few ordered pairs.

- A nonexistence result restricted to triples with a prescribed autotopism / autoparatopism group, or to triples extending one prescribed square, when represented as full nonexistence.

- An incomplete backtracking or heuristic search that "found no triple," absent a completeness certificate over a precisely delimited class.

- Any claim resting on unverified reuse of a historical dataset without independent regeneration.

## 3. Graded partial-result targets

Ordered milestones; each names the artifact that proves it and how it is independently checked.

- **P1 - Reproduce the known frontier.** Regenerate an explicit pair of MOLS(10) (e.g. a Parker-type pair) and verify it with an independently written exact checker. *Certificate:* two arrays + checker output; SHA-256 of both.

- **P2 - Verified orthogonal-mate machinery.** For a fixed order-10 Latin square species representative, exhaustively find all its orthogonal mates by exact search and verify the count against the literature where available. *Certificate:* isomorph-free mate list + replay; documented species representative.

- **P3 - Symmetry-restricted nonexistence.** For a prescribed nontrivial autoparatopism group \(G\), prove by exhaustive/SAT search that no triple of MOLS(10) admits \(G\). *Certificate:* DRAT/LRAT for the SAT encoding, or an isomorph-free enumeration with completeness proof; explicit statement of \(G\) and its action.

- **P4 - Extend the symmetry sweep.** Cover a family of prescribed groups (e.g. all groups of a given order acting in a fixed way, or all triples containing a square with a prescribed nontrivial autotopism), documenting the exact union of classes ruled out. *Certificate:* per-class certificates + a coverage table.

- **P5 - Conditional structural theorem.** Prove no triple exists in which two of the three squares form one enumerated main-class of 2-MOLS(10), over a completely enumerated set of such pairs. *Certificate:* the enumerated pair catalogue (canonical hashes) + per-pair third-square nonexistence certificate.

- **P6 - Full resolution (windfall).** Either exhibit a triple (case A) or complete an exhaustive nonexistence with a global completeness certificate. Report honestly that unrestricted exhaustion is astronomically large; P6 is a windfall, not the planned product.

## 4. Known results and prior art

- **Euler (1782)** posed the 36-officers problem and conjectured \(N(n)=1\) for all \(n\equiv 2\pmod 4\).

- **Tarry (1900)** verified by exhaustion that \(N(6)=1\), confirming Euler for \(n=6\).

- **MacNeish (1922)** gave multiplicative lower bounds \(N(mn)\ge\min(N(m),N(n))\) and conjectured these were tight (later false).

- **Bose, Shrikhande, Parker (1959–1960)** disproved Euler's conjecture: \(N(n)\ge 2\) for all \(n\notin\{2,6\}\); in particular \(N(10)\ge 2\). Parker exhibited explicit pairs of MOLS(10).

- **Lam, Thiel, Świercz (1989)** proved no projective plane of order 10 exists, whence \(N(10)\le 8\).

- The commonly cited sharper bound is \(N(10)\le 6\), via net-completion / Bruck-type arguments combined with the order-10 plane nonexistence. **Re-verify the exact upper bound and its provenance** - the value and attribution are stated here from memory and marked **(verify)**.

- Extensive computational searches for three MOLS(10) have all failed; the problem is regarded as one of the hardest small design questions.

- Enumeration of Latin squares of order 10 and of small MOLS sets is due to **McKay–Meynert–Myrvold**, **Myrvold**, and **Egan–Wanless** ("Enumeration of MOLS of small order," *Math. Comp.*, c. 2016 - **verify**). The number of main classes of Latin squares of order 10 is astronomically large.

- Recent work has enumerated **pairs** of MOLS(10) satisfying nontrivial algebraic relations and shown none of the enumerated pairs extends to a triple (c. 2022, **verify** authorship and scope) - a relation-restricted result, not full nonexistence.

**Status as of mid-2026 - re-verify against the current literature before starting any session.** Bounds, enumeration counts, and the exact upper bound on \(N(10)\) drift; several nearby design problems have moved recently. Confirm the best current lower bound (still 2), the upper bound and its proof, and which symmetry-restricted nonexistence results are already published before committing search effort.

## 5. Attack plan

`[search]` The unrestricted space is far beyond exhaustion on one workstation, so the plan is: exact tooling first, then symmetry-restricted decision problems, then constructive attempts.

- **Exact verification core.** A small independent checker (Python + exact integers, or C++ with `int8`) validates the Latin property and pairwise orthogonality. Every artifact passes through it. `SageMath` (`LatinSquare`, `designs`) and `GAP` cross-check.

- **Canonical forms and enumeration.** `nauty`/`Traces` canonically label the associated coloured graph or the orthogonal-array / net incidence structure for isomorph rejection; orderly generation yields species representatives. Replay every enumeration with an independently seeded canonicaliser.

- **Symmetry-restricted SAT/CP.** Encode "three MOLS(10) with prescribed autoparatopism group \(G\)" as SAT (one Boolean per cell–symbol–square with Latin and orthogonality clauses) or CP (all-different), fixing the \(G\)-orbit structure to shrink the model, and require **DRAT/LRAT** for every UNSAT. Solvers: `kissat`, `CaDiCaL`, `CryptoMiniSat`; CP via OR-Tools for exploration, re-certified by SAT.

- **Constructive search.** Fix one square as a species representative, compute all orthogonal mates, then search for a common third orthogonal to a chosen pair; drive with backtracking that prunes on partial ordered-pair collisions. Autotopisms, prolongation, and transversal structure reduce the branching.

- **One-workstation scope.** P1–P4 are feasible: pair reproduction and mate enumeration are cheap; single prescribed-group decisions are seconds-to-hours with good symmetry breaking. Full unrestricted nonexistence is **not** feasible and must not be attempted as the deliverable.

- **Failure modes.** Weak symmetry breaking causing redundant search and inflated runtimes; canonicalisation bugs that under- or over-count species; off-by-one in symbol/coordinate roles; treating a floating-point orthogonality check as authoritative; representing a group-restricted `UNSAT` as full nonexistence.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Every Latin and orthogonality check runs in exact integer arithmetic; every symmetry-restricted nonexistence carries a DRAT/LRAT proof or a replayable isomorph-free enumeration. Floating point and heuristic solvers are for exploration only, never certification.

2. **Independent verification.** For each certificate, a standalone checker written separately from the search: a DRAT checker (`drat-trim` / `cake_lpr`) for SAT `UNSAT`; an enumeration replay under an independently implemented canonical form; a second CAS (`SageMath` vs `GAP`) for any constructed triple or pair.

3. **Reproducibility.** All square representatives, group specifications, encodings, solver versions, and seeds recorded; a SHA-256 manifest over every array, proof file, and script; the exact group action and normalisation stated so a third party can regenerate the model.

4. **Preservation.** All search and enumeration source code is part of the record - the Hadamard-668 lost-source lesson applies. Anything not preserved is stated explicitly rather than obscured; a `NEXT_STEPS.md` records the exact frontier group/class reached when pausing.

5. **Honest reporting.** The report states up front whether the resolution standard (a verified triple, or a certified full nonexistence) was met. A symmetry-restricted nonexistence, a reproduced pair, or an incomplete search is labelled as such and never represented as establishing \(N(10)\ge 3\) or \(N(10)=2\).
