# PROMPT FOR CERTIFYING OPTIMAL KOBON TRIANGLE ARRANGEMENTS

## The Kobon triangle problem: certified constructions and matching upper bounds for \(K(n)\)

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 49 of 50
**Area:** order theory & extremal set systems (combinatorial geometry)
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

An arrangement of \(n\) lines in the plane cuts out a number of triangular cells; the Kobon triangle problem asks for the maximum, \(K(n)\), over all arrangements. It is a finite combinatorial-geometry problem with machine-checkable ground truth: a lower bound is an explicit arrangement whose triangle count can be recomputed exactly, and an upper bound is a combinatorial exhaustion over pseudoline arrangements decidable by SAT.

Exact values are known only for small \(n\); the standard upper bound is Tamura's \(\lfloor n(n-2)/3\rfloor\), refined by Clément–Bader for \(n\equiv0,2\ (\mathrm{mod}\ 6)\), and "perfect" arrangements attaining the bound exist for a sparse set of \(n\). The problem is live: in 2025 Savchuk resolved \(n=11\) and set records at \(n=23,27\) with a SAT-solver method over a compact table encoding of pseudoline arrangements.

The target is a **certified optimal arrangement for an open \(n\)** - a lower construction with exact-arithmetic triangle count plus a matching certified upper bound - or a new record arrangement. Anything less (a picture, a floating count, a lower bound without a matching upper bound) is reported as a partial result.

## 1. Exact problem statement

Consider \(n\) distinct lines in the real projective/affine plane, forming an **arrangement** \(\mathcal A\). The arrangement partitions the plane into vertices (pairwise intersections), edges, and faces.

A **Kobon triangle** is a bounded face of \(\mathcal A\) that is a triangle: a cell whose boundary consists of exactly three edges lying on three distinct lines of \(\mathcal A\), with no line of \(\mathcal A\) passing through its interior. Distinct triangular cells have disjoint interiors, so the triangles are automatically non-overlapping. Let \(T(\mathcal A)\) be the number of triangular cells and
\[
K(n)\;=\;\max_{\mathcal A:\ |\mathcal A|=n}\ T(\mathcal A).
\]
Both simple arrangements (no two lines parallel, no three concurrent) and non-simple ones (parallels, multiple points) are allowed; the maximum is what is sought.

**Combinatorial counts.** For a *simple* arrangement (no two parallel, no three concurrent) the numbers of vertices, edges, and faces are
\[
V=\binom n2,\qquad E=n^2,\qquad F=\binom n2+n+1\ \ (\text{Euler, unbounded faces included}),
\]
with \(\binom{n}{2}-n+1\) of the faces bounded. Non-simple arrangements only reduce the vertex/edge counts.

**Upper bound (Tamura).**
\[
K(n)\ \le\ \Bigl\lfloor \tfrac{n(n-2)}{3}\Bigr\rfloor .
\]
The bound comes from a double count: each triangle is bounded by three edges, each edge borders at most two faces, and along each of the \(n\) lines the incident triangles are constrained by the \(n-1\) crossing points, yielding \(3\,T(\mathcal A)\le n(n-2)\) after the boundary accounting.

**Refinement (Clément–Bader 2007).** For \(n\equiv0\) or \(2\ (\mathrm{mod}\ 6)\) the Tamura bound is not attained; a strictly smaller upper bound holds (verify the exact refined value). The Tamura value is an integer exactly when \(n\equiv0,2\pmod3\); "perfect" arrangements can exist only when the parity/congruence conditions permit.

An arrangement is **perfect** if it attains \(\lfloor n(n-2)/3\rfloor\). The pseudoline / oriented-matroid relaxation replaces straight lines by pseudolines; a pseudoline arrangement realizing a triangle count is a valid **upper-bound witness** but is a genuine straight-line construction only if it is **stretchable**.

**Convention.** Triangles are *bounded* cells; the count is taken in the affine plane, and lines through the common point at infinity (parallels) contribute no crossing there. The maximum is unchanged under the projective closure provided the count of bounded triangular faces is what is recorded. All targets below use this bounded-triangle convention.

No informal target is admissible: a claimed value of \(K(n)\) requires an exact triangle count for a specific arrangement and a matching certified bound.

## 2. Resolution standard

For a target \(n\), a complete resolution is the exact determination of \(K(n)\), certified in two matching parts:

- **Lower bound (construction).** An explicit arrangement of \(n\) lines - exact rational (or algebraic) coordinates - with a machine-verified triangle count \(T(\mathcal A)=m\). Intersections and cell incidences are computed in exact rational arithmetic or, for algebraic coordinates, with interval arithmetic and directed rounding that certifies the combinatorial type. A pseudoline construction is admissible only with an accompanying **stretchability certificate** (a rational realization, or an oriented-matroid realizability proof).
- **Upper bound.** A proof that no arrangement of \(n\) lines has more than \(m\) triangles: either the Tamura / Clément–Bader bound when it equals \(m\), or an exhaustive **SAT / oriented-matroid enumeration** over pseudoline arrangements with a **DRAT/LRAT** UNSAT proof that "\(T\ge m+1\)" is infeasible.

The lower-bound count is a purely combinatorial predicate on exact coordinates: with \(p_{ab}=\ell_a\cap\ell_b\) the exact intersection of lines \(a,b\), a triple \(\{a,b,c\}\) bounds a Kobon triangle iff the three points \(p_{ab},p_{ac},p_{bc}\) are distinct and no fourth line \(\ell_d\) meets the interior of their triangle, all decidable by exact sign-of-determinant tests. Hence
\[
T(\mathcal A)=\#\bigl\{\{a,b,c\}:\ p_{ab},p_{ac},p_{bc}\ \text{form an empty triangular cell}\bigr\}
\]
is exactly computable.

A **certified optimal Kobon arrangement** for \(n\) is a matching lower construction and upper bound with \(m=K(n)\).

**Not accepted as resolution.**

- A drawing or floating-point arrangement whose triangle count is not recomputed in exact/interval arithmetic.
- A lower-bound construction with no matching certified upper bound, presented as "optimal".
- A pseudoline arrangement not shown stretchable, presented as a straight-line arrangement.
- A single \(n\) value used to claim the general problem "solved" - \(K(n)\) is per-\(n\) and open across an infinite set.
- An upper bound from a solver run with no independently checkable UNSAT proof.
- A count that silently relies on a degenerate coincidence (three lines through a point, or two parallels) not permitted by the intended realization, or that double-counts a cell touched by a fourth line.

## 3. Graded partial-result targets

- **P1 - reproduce the known frontier.**
  For small \(n\) (through \(n\le10\)), reconstruct arrangements attaining the documented \(K(n)\), with exact coordinates and an independent exact triangle count, and reproduce the matching certified upper bounds.
  *Certificate:* rational coordinate files, an exact-arithmetic face-enumeration recount, and the upper-bound argument replayed.

- **P2 - reproduce Savchuk's 2025 results independently.**
  Re-derive the \(n=11\) resolution and the \(n=23,27\) record arrangements with an **independent SAT encoding** and DRAT verification, validating the table-notation method against a from-scratch implementation.
  *Certificate:* independent CNF, DRAT trace checked by `drat-trim`, and exact-coordinate (or stretchability) verification of the constructions.

- **P3 - certify optimality for one open \(n\).**
  For a currently open order, a matching construction (exact coordinates + verified count) and upper bound (SAT / oriented-matroid exhaustion with DRAT), fixing \(K(n)\).
  *Certificate:* both parts, independently checked.

- **P4 - a new record lower bound.**
  For an open \(n\), an arrangement with strictly more triangles than previously documented, exact coordinates and verified count, even without a matching upper bound.
  *Certificate:* coordinate file + exact recount + comparison to the prior record with citation.

- **P5 - a certified upper-bound improvement.**
  Prove the Tamura / Clément–Bader bound unreachable for a specific new \(n\) (a Savchuk-style tightening), via SAT / oriented-matroid exhaustion with a DRAT UNSAT proof.
  *Certificate:* the encoding and verified UNSAT trace, with a soundness argument linking the encoding to genuine arrangements.

- **P6 - stretchability resolution.**
  For a record pseudoline arrangement, decide realizability by straight lines: a rational realization (interval-certified) proving stretchable, or a non-realizability certificate (Bokowski–Sturmfels final polynomial / a Positivstellensatz witness).
  *Certificate:* the realization with interval bounds, or the algebraic non-realizability proof.

## 4. Known results and prior art

- **Origin.** Posed by Kobon Fujimura; popularized by Martin Gardner. OEIS **A006066** tracks best-known \(K(n)\); it records lower bounds (constructions) that are not all proven optimal, so "A006066 value" and "certified \(K(n)\)" must be distinguished in every claim.
- **Small exact values.** Against the Tamura bound \(B(n)=\lfloor n(n-2)/3\rfloor\):
\[
\begin{array}{c|ccccccc}
n & 3 & 4 & 5 & 6 & 7 & 8 & 9\\\hline
K(n) & 1 & 2 & 5 & 7 & 11 & 15 & 21\\
B(n) & 1 & 2 & 5 & 8 & 11 & 16 & 21
\end{array}
\]
so \(n=5,7,9\) are perfect while \(n=6,8\) fall short of \(B(n)\) (consistent with Clément–Bader). Verify the tail of the table and each optimality claim against A006066.
- **Upper bounds.** Tamura's \(\lfloor n(n-2)/3\rfloor\); Clément–Bader (2007) proved it unattainable for \(n\equiv0,2\ (\mathrm{mod}\ 6)\) (verify the refined value).
- **Perfect arrangements.** Straight-line arrangements attaining the Tamura bound are documented for
\[
n\in\{3,4,5,6,7,8,9,13,15,17\}\ (\text{verify}),
\]
and Savchuk (2025) added optimal arrangements at \(n=23,27\). The exact \(K(n)\) is not settled for many intermediate and larger \(n\); the smallest genuinely open order must be re-confirmed against A006066 before a target is chosen.
- **Savchuk (2025, arXiv 2507.07951).** A SAT-solver method (KISSAT) over a compact **table notation** for pseudoline arrangements: resolved the long-open \(n=11\) case (proving the previously suspected upper bound), and found new optimal/record arrangements at \(n=23\) and \(n=27\). Confirm the precise claims and any successor results.
- **Background.** Grünbaum's *Arrangements and Spreads*; oriented-matroid and pseudoline-arrangement theory (Björner–Las Vergnas–Sturmfels–White–Ziegler); Bokowski–Sturmfels on realizability.

**Status as of mid-2026 - re-verify against the current literature before starting any session.** This problem moved in 2025 (Savchuk); confirm the current A006066 table, which \(n\) are certified optimal versus best-known, and the smallest genuinely open \(n\) before choosing a target. No fabricated arXiv IDs, DOIs, or page numbers are to be introduced.

## 5. Attack plan

- **`[search]` pseudoline / oriented-matroid enumeration.** Represent arrangements by wiring diagrams / allowable sequences (equivalently rank-\(3\) oriented matroids). The number of simple arrangements of \(n\) pseudolines grows superexponentially,
\[
2^{\Theta(n^2)},
\]
so full combinatorial enumeration is confined to modest \(n\); this is the wall Savchuk's SAT encoding sidesteps by searching for a high-triangle arrangement directly. Encode "an arrangement of \(n\) lines with \(\ge m\) triangles" as CNF à la Savchuk (table notation → clauses), solve with **kissat/CaDiCaL**, and emit **DRAT** for UNSAT upper bounds.
- **Exact triangle counting.** Given rational line coordinates, compute all \(\binom n2\) intersections exactly, build the arrangement, and count triangular bounded faces in exact rational arithmetic. Incidence and side-of-line tests reduce to exact sign evaluations
\[
\operatorname{sign}\det\!\begin{pmatrix} x-x_0 & y-y_0\\ u & v\end{pmatrix}\in\{-,0,+\},
\]
computed with CGAL exact predicates or a custom GMP kernel. Never count from floating coordinates.
- **Realizability / stretchability.** From an oriented matroid, decide stretchability with Bokowski–Sturmfels final polynomials, or solve the realization space with exact algebra (Gröbner bases / cylindrical algebraic decomposition in SageMath / QEPCAD), using interval arithmetic to certify a rational realization.
- **One-workstation scope.** Exact-coordinate verification of a given arrangement is cheap (\(O(n^3)\) exact sign tests for the full triangle count). SAT-based upper bounds are feasible into the low teens of \(n\) (Savchuk reached \(n=11\)); full combinatorial exhaustion beyond \(\sim n=11\text{–}13\) is infeasible. Stretchability is \(\exists\mathbb R\)-complete in general and tractable only for structured small instances.
- **Failure modes.** SAT instances blow up with \(n\); stretchability is intractable for large arrangements; floating-point intersection counting silently miscounts near-degenerate cells (must be exact); an unstretchable pseudoline "construction" is not a valid line arrangement.

## 6. Verification and auditability requirements

1. **Exact/certified computation.** Triangle counts come from exact rational (or interval-certified algebraic) arithmetic; upper bounds carry DRAT/LRAT UNSAT proofs; floating point is exploration only.
2. **Independent verification.** A standalone checker, independent of the search, recomputes the triangle count from the coordinates and runs `drat-trim` on every UNSAT proof; stretchability realizations are re-verified by interval evaluation of the sign conditions.
3. **Reproducibility.** Coordinates, encodings, solver versions, seeds, and the table-notation definitions recorded; SHA-256 manifest over every arrangement, certificate, and proof trace.
4. **Preservation.** Construction and search source (the SAT encoder, the exact counter, the realizability code) is part of the record - the Hadamard-668 lost-source lesson. A lower bound without a matching upper bound is stated as a record, not as \(K(n)\).
5. **Honest reporting.** The report states which \(n\) were certified optimal, which are records, and which upper bounds are proved versus assumed; a pseudoline construction is never reported as a line arrangement without a stretchability certificate.

### Honest calibration

This is a finite problem with clean machine-checkable ground truth, and 2025 showed SAT methods can crack individual open orders. The scoreboard for a session is a single certified row,
\[
n\ \longmapsto\ \bigl(\text{lower bound }m,\ \text{upper bound }M,\ m\overset{?}{=}M\bigr),
\]
and a realistic product is a certified \(K(n)\) for one open \(n\) (\(m=M\)), an independent replay of Savchuk's results, or a new record lower bound with an exact count. Certifying a large open \(n\), or resolving stretchability for a big pseudoline arrangement, is hard and should be scoped modestly.
