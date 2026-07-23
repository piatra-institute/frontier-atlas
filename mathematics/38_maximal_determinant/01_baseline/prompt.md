# PROMPT FOR DETERMINING THE MAXIMAL \(\pm1\) DETERMINANT AT A SPECIFIC OPEN ORDER

## The Hadamard maximal-determinant problem for orders \(n\not\equiv 0\pmod 4\)

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 38 of 50  
**Area:** designs & codes  
**Modes:** `[search]` `[opt]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

\(D(n)\) is the largest possible absolute value of the determinant of an \(n\times n\) matrix with entries in \(\{+1,-1\}\). For \(n\equiv 0\pmod 4\) the Hadamard bound \(n^{n/2}\) is attained exactly when a Hadamard matrix exists; for \(n\equiv 1,2,3\pmod 4\) the maximum is governed by the Barba, Ehlich–Wojtas, and Ehlich bounds, attained only for special \(n\), and the exact value is unknown for many orders.

Each open order is a finite, exactly-checkable target: a construction is verified by an exact integer determinant, and an upper bound becomes a proof only through exact arithmetic - a number-theoretic argument or a complete Gram-matrix enumeration. This is the `[search]`+`[opt]` regime of the program, a sibling of the order-668 Hadamard existence problem (02). The resolution standard in section 2 - determining \(D(n)\) exactly at a specific open order, both sides certified - is the goal; a construction alone, or a bound alone, is a partial result and never reported as the value.

## 1. Exact problem statement

Let \(\mathcal M_n=\{-1,+1\}^{n\times n}\). Define
\[
D(n)=\max_{M\in\mathcal M_n}\ |\det M|.
\]

Determinants of \(\pm1\) matrices are integers, so \(D(n)\in\mathbb Z_{\ge0}\); optimal matrices are considered up to Hadamard equivalence (row/column permutations and sign changes, plus transposition), which preserves \(|\det|\).

A convenient reformulation uses the **Gram matrix** \(G=M^\top M\): a positive-semidefinite integer matrix with diagonal \(n\), with \(\det M=\pm\sqrt{\det G}\). Bounding \(\det G\) over admissible \(G\) bounds \(D(n)\), and the off-diagonal residue constraints on \(G\) drive the finite enumeration on the upper side.

The residue structure is the key finiteness lever. Every off-diagonal entry \(G_{ij}=\langle M_{\cdot i},M_{\cdot j}\rangle\) is a sum of \(n\) terms in \(\{\pm1\}\), so \(G_{ij}\equiv n\pmod 2\) and in fact \(G_{ij}\equiv n\pmod 4\) after the standard row-normalisation; the extremal Gram matrices for each residue class \(n\bmod 4\) have a known near-block form (a small number of diagonal blocks \(J+cI\)), which is precisely why the analytic bounds take their stated shapes and why the upper side reduces to a finite candidate enumeration.

The problem is equivalent to finding **D-optimal designs** (maximising \(\det(X^\top X)\) over \(\pm1\) design matrices) and is adjacent to weighing-matrix and conference-matrix existence.

**The analytic bounds.**

- **Hadamard:** \(|\det M|\le n^{n/2}\), with equality iff \(M\) is a Hadamard matrix (possible only for \(n=1,2\) or \(n\equiv0\pmod4\)).

- **Barba (1933), \(n\equiv1\pmod4\):** \(|\det M|\le\sqrt{2n-1}\,(n-1)^{(n-1)/2}\); attainable requires \(2n-1\) to be a perfect square.

- **Ehlich–Wojtas (1964), \(n\equiv2\pmod4\):** \(|\det M|\le(2n-2)\,(n-2)^{(n-2)/2}\); attainable requires \(2n-2\) to be a sum of two squares.

- **Ehlich (1964), \(n\equiv3\pmod4\):** a block-based bound, attained only under stringent number-theoretic conditions.

**The open question, made specific.** Fix one currently open order \(n\not\equiv0\pmod4\) and determine \(D(n)\) exactly.

A concrete flagship, to be **re-verified**: \(n=29\) (\(\equiv1\pmod4\)), where \(2n-1=57\) is not a perfect square, so the Barba bound is not attained and the exact maximum is open. The chosen order and its current bracket must be quoted from the live maximal-determinant record, not from this prompt.

## 2. Resolution standard

A **complete resolution** for a chosen open order \(n\) is a matched pair.

- **Lower side.** An explicit matrix \(M\in\mathcal M_n\) with \(|\det M|=V\), where \(\det M\) is computed in **exact** arithmetic (multi-modular / Bareiss), so \(V\) is certified as an attained value.

- **Upper side.** A proof that \(D(n)\le V\), by exact arithmetic: a reduction of the maximisation of \(\det G\) to a finite, completely enumerated set of admissible Gram matrices (with isomorph rejection); or a number-theoretic tightening of the Barba / Ehlich–Wojtas / Ehlich bound carried out exactly; or a DRAT-backed `UNSAT` for "does a \(\pm1\) matrix of \(|\det|>V\) exist?" over a faithful finite encoding.

Together these give \(D(n)=V\).

**Named certified forms accepted.**

- Exact integer determinant (multi-modular CRT / Bareiss) for every candidate matrix.

- Exhaustive isomorph-free enumeration of candidate Gram matrices via `nauty`, with a completeness argument.

- Exact-rounded LP / number-theoretic upper bounds.

- DRAT/LRAT for SAT-encoded nonexistence.

**Not accepted as resolution.**

- A determinant computed in floating point (rounding / overflow can corrupt the integer).

- A construction attaining \(V\) with no matching upper-bound proof (a lower bound only).

- An analytic bound that is not attained, quoted as \(D(n)\) (off the special orders the bound is only an upper bound).

- Matching a conjectured or record value without an independent exact upper certificate.

- A Gram-matrix enumeration that is not proved complete, or that omits isomorph rejection and double-counts.

## 3. Graded partial-result targets

- **P1 - Certified reproduction.** For an order where \(D(n)\) is *known*, reproduce it end to end: an exact-determinant construction plus the matching certified upper bound (analytic-attained or enumerated). *Certificate:* matrix + exact determinant transcript + bound argument.

- **P2 - Exact bound formulas.** Implement the Barba, Ehlich–Wojtas, and Ehlich bounds symbolically and evaluate them exactly at the target orders, recording the number-theoretic attainability conditions (square / sum-of-two-squares tests). *Certificate:* exact evaluations + attainability verdicts.

- **P3 - Strong lower bound.** For a specific open order (e.g. \(n=29\)), search for a high-\(|\det|\) matrix (simulated annealing / local search / structured families) and certify its determinant exactly. *Certificate:* matrix + exact determinant + search provenance.

- **P4 - Finite Gram reduction.** For the target order, reduce the upper side to a finite set of admissible Gram matrices (diagonal \(n\); off-diagonals constrained mod 4 and by PSD), and prune it exactly with isomorph rejection. *Certificate:* the enumerated candidate set + rejection log.

- **P5 - Determine \(D(n)\) (windfall).** Close a specific open order - lower and upper certified and equal.

- **P6 - Second order / family.** Extend a settled technique to a second open order or a residue-class family, with the same certificate standard.

## 4. Known results and prior art

- **Hadamard (1893)** gave the determinant bound and the \(n\equiv0\pmod4\) attainment condition (Hadamard matrices).

- **Barba (1933)** for \(n\equiv1\), **Ehlich (1964)** for \(n\equiv3\), and **Ehlich (1964)** and **Wojtas (1964)** for \(n\equiv2\) established the residue-class bounds; **Williamson** and later authors supplied constructions.

- The **D-optimal designs** literature (**Kounias, Chadjipantelis, Moyssiadis** and others) determined many exact values and equivalence-class counts for small \(n\).

- Recent determinations include order **15** (**Orrick**, c. 2005), orders **19 and 37** (**Brent, Orrick, Osborn, Zimmermann**, c. 2012), order **21**, and order **22** (**Chasiotis, Kounias, Farmakis**) (**verify** attributions and dates).

- For \(n\equiv3\pmod4\) the Ehlich bound involves a block decomposition and is the hardest residue class; several such orders remain open, and constructions relate to conference matrices and skew-Hadamard families.

- The survey **"A Survey of the Hadamard Maximal Determinant Problem"** (Brent, Osborn, Orrick, Solomon; arXiv, c. 2021 - **verify**) and **Orrick's maximal-determinant website** are the living references for current records and open orders.

- Per the survey, the open orders with \(n\equiv1\pmod4\) and \(n\le50\) are **29, 33, 45, 49** (**verify**); many \(n\equiv2,3\pmod4\) orders are also open.

**Status as of mid-2026 - re-verify against the current literature before starting any session.** Records at specific orders fall periodically; confirm from Orrick's site (or its current successor) that the chosen order is still open, and record the current best lower bound and the governing analytic upper bound with an access date. Do not trust the open-order list above without checking.

## 5. Attack plan

`[search]` for constructions, `[opt]` for certified upper bounds; both terminate in exact certificates. Fix the target value \(V\) from the exact analytic ceiling first, then attack the lower and upper sides toward it.

- **Exact determinant core.** Multi-modular (CRT over several primes) and Bareiss fraction-free elimination in `FLINT`/`NTL`/`SageMath`; never a floating determinant. Every candidate matrix is scored exactly, and results are cross-checked between the CRT and Bareiss routines to catch implementation error.

- **Lower-bound search (metaheuristic).** Simulated annealing, tabu, and local search over \(\mathcal M_n\), each hit re-scored by the exact determinant core.

- **Lower-bound search (structured).** Circulant cores, two-circulant, block / Williamson-type, conference-matrix and D-optimal design templates via `GAP`/`SageMath`; structure both accelerates the search and yields matrices whose determinants factor transparently.

- **Upper-bound reduction.** Enumerate admissible Gram matrices with fixed diagonal \(n\), off-diagonals constrained by residue conditions (mod 4) and positive-semidefiniteness; use `nauty` for isomorph rejection and exact PSD / determinant tests; combine with exact number-theoretic tightenings of the Barba / Ehlich bounds. For narrow ranges, SAT-encode "\(|\det|>V\)?" and require **DRAT** for `UNSAT`.

- **Exact PSD and determinant of \(G\).** Positive-semidefiniteness of a candidate Gram matrix is certified by an exact rational \(LDL^\top\) factorisation (never a numerical eigenvalue check), and \(\det G\) is computed by the same exact routines used for \(\det M\).

- **Number-theoretic pre-filter.** Before searching, evaluate the attainability tests exactly (is \(2n-1\) a square? is \(2n-2\) a sum of two squares?) and compute the exact analytic ceiling; this fixes the target value \(V\) the search aims at and tells whether the analytic bound can possibly be tight.

- **Bootstrapping from smaller orders.** Optimal or near-optimal matrices at \(n-1\) and \(n-2\) seed constructions at \(n\) (bordering, row/column extension); each extension is re-scored exactly rather than assumed to inherit optimality.

- **One-workstation scope.** Lower-bound search is feasible at \(n\approx29\); exact-determinant scoring is cheap. The exact upper side is the hard part: full Gram enumeration is feasible only when the residue / PSD constraints cut the candidate set to a tractable size - for many orders it will not, and the honest deliverable is then a strong certified lower bound plus a partial upper argument.

- **Failure modes.**

  - Floating-determinant overflow or rounding corrupting the integer value (values reach hundreds of digits).

  - Incomplete Gram enumeration silently missing candidate blocks.

  - Isomorph-rejection bugs that double-count or over-prune.

  - Quoting an unattained analytic bound as \(D(n)\) when the attainability conditions fail.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Every determinant is exact integer arithmetic (multi-modular / Bareiss); every upper bound rests on an exact finite enumeration, an exact number-theoretic argument, or a DRAT-backed `UNSAT`. Floating point is exploratory only.

2. **Independent verification.** A standalone exact-determinant routine (separate from the search) re-scores every claimed matrix; a second implementation replays any Gram enumeration and isomorph rejection; a DRAT checker validates SAT `UNSAT`.

3. **Reproducibility.** All matrices, Gram candidate sets, bound derivations, solver / CAS versions, and seeds recorded; SHA-256 manifest over every artifact; the chosen order and its bracket quoted from the live record with an access date.

4. **Preservation.** Search and enumeration source is part of the record - the Hadamard-668 lost-source lesson is directly on point for this sibling problem. A `NEXT_STEPS.md` records the order attacked, the best exact lower bound, and the state of the upper-side reduction when pausing.

5. **Honest reporting.** The report states up front whether \(D(n)\) was determined exactly at the target order. A record-setting construction, a bound evaluation, or a partial Gram reduction is labelled as such and never represented as determining \(D(n)\).
