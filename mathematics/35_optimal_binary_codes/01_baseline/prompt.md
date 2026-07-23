# PROMPT FOR CLOSING A SPECIFIC OPEN VALUE OF \(A(n,d)\)

## Optimal binary codes: the maximum size of a length-\(n\), minimum-distance-\(d\) binary code

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 35 of 50  
**Area:** designs & codes  
**Modes:** `[search]` `[opt]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

For binary codes, \(A(n,d)\) - the maximum number of length-\(n\) binary words with pairwise Hamming distance at least \(d\) - is one of the most-studied functions in combinatorial coding theory, and many small values remain open, trapped between the best-known construction (lower bound) and the Delsarte linear-programming / Schrijver semidefinite bound (upper bound).

Each open cell of Brouwer's table is a self-contained, machine-checkable target: a construction is verified by exact distance enumeration, and an upper bound becomes a *proof* only when the linear or semidefinite dual is given in exact rational arithmetic with certified rounding. This is precisely the `[search]`+`[opt]` regime, adjacent to the Hadamard problem (02) and covering codes (36). The resolution standard in section 2 - determining a specific open \(A(n,d)\) exactly, both sides certified - is the goal; a one-sided improvement is a genuine partial result and is reported as such, never as "the value is now known."

## 1. Exact problem statement

Work over \(\mathbb{F}_2^n\) with the Hamming metric \(d_H(x,y)=|\{i:x_i\neq y_i\}|\).

A **binary code** of length \(n\) is any subset \(C\subseteq\mathbb{F}_2^n\); its **minimum distance** is
\[
d(C)=\min\{d_H(x,y):x\neq y\in C\}.
\]

Define
\[
A(n,d)=\max\{\,|C|:\ C\subseteq\mathbb{F}_2^n,\ d(C)\ge d\,\}.
\]

No linearity is assumed: \(C\) is an arbitrary (unrestricted) code. Standard reductions hold and are used freely:

- \(A(n,d)\) is invariant under the automorphism group of the Hamming scheme (coordinate permutations and complementations).

- For odd \(d\), \(A(n,2e-1)=A(n+1,2e)\); it therefore suffices to treat even \(d\), and each odd-distance cell is bracketed by an even-distance one.

- The Singleton, Hamming (sphere-packing), Plotkin, Elias–Bassalygo, and Griesmer bounds give quick sanity limits but are dominated by the LP/SDP bounds in the open range.

**Distance distribution (the LP variable).** For a code \(C\) with \(|C|=M\), its inner distribution is
\[
B_i=\frac{1}{M}\bigl|\{(x,y)\in C^2:d_H(x,y)=i\}\bigr|,\qquad i=0,\dots,n,
\]
with \(B_0=1\), \(B_i=0\) for \(1\le i<d\), and \(\sum_i B_i=M\). The MacWilliams transform via the Krawtchouk polynomials \(K_k(i)=\sum_{j}(-1)^j\binom{i}{j}\binom{n-i}{k-j}\) gives the dual nonnegativity constraints
\[
\sum_{i=0}^{n} B_i\,K_k(i)\ \ge\ 0,\qquad k=0,\dots,n,
\]
and maximising \(\sum_i B_i\) subject to these (plus \(B_i\ge0\), \(B_i=0\) below \(d\)) is exactly the **Delsarte LP** whose optimum upper-bounds \(A(n,d)\). The exact rational dual to this LP is the certificate targeted in section 2.

**The open question, made specific.** Fix one currently open cell \((n,d)\) from Brouwer's table and determine \(A(n,d)\) exactly.

A concrete flagship, to be **re-verified** at session start: \(A(17,4)\), equivalently \(A(16,3)\), for which the best known construction gives \(\ge 2720\) and the linear-programming bound gives \(\le 3276\) (both values **verify**). The chosen \((n,d)\) and its current bracket must be quoted from the live table, not from this prompt.

## 2. Resolution standard

A **complete resolution** for a chosen open \((n,d)\) is a matched pair.

- **Lower side.** An explicit code \(C\) with \(|C|=M\) and a proof, by exhaustive pairwise exact distance computation (or a certified structural argument), that \(d(C)\ge d\).

- **Upper side.** A proof that \(A(n,d)\le M\), given as an **exact rational** feasible dual: for the Delsarte LP, a Krawtchouk-expansion multiplier vector \(y\ge 0\) whose objective, evaluated in exact arithmetic and correctly rounded down to an integer, equals \(M\); or, for a semidefinite (Schrijver three-point / Gijswijt) relaxation, a dual solution certified positive semidefinite by an exact factorisation and rounded soundly.

Together these give \(A(n,d)=M\).

**Named certified forms accepted.**

- Exhaustive or clique/SAT search with a completeness certificate for the lower side of small cases (DRAT/LRAT for SAT `UNSAT` of "does a code of size \(M{+}1\) exist?").

- Exact-rational Delsarte LP dual with directed rounding.

- Exact-rounded SDP dual (Terwilliger-algebra block-diagonalised) verified by rational PSD certificates.

**Not accepted as resolution.**

- A floating-point LP/SDP bound with no exact rational dual - rounding can flip the last integer.

- A construction whose minimum distance was only sampled or spot-checked rather than exhaustively verified.

- Improving one side only (a better code, or a better bound) and reporting the value as "determined."

- Reproducing a table entry with the same software that generated it, without independent re-verification.

- Asymptotic, probabilistic, or heuristic estimates presented as exact values.

## 3. Graded partial-result targets

- **P1 - Certified reproduction, both sides.** Pick a cell where \(A(n,d)\) is *known* and reproduce it end to end: an exact code plus an exact-rational Delsarte LP dual meeting it. *Certificate:* code file + LP dual with exact arithmetic transcript.

- **P2 - Exact Delsarte engine.** Implement the Delsarte LP in exact rational arithmetic (Krawtchouk polynomials \(K_k(x)\) exact, MacWilliams-type constraints), reproducing published bounds for a range of \((n,d)\). *Certificate:* dual vectors + a verifier recomputing the objective in exact arithmetic.

- **P3 - Rounding-doubt removal.** For a target open \((n,d)\) whose table upper bound is a floating-point LP value, produce the **exact** rational dual attaining the same integer, removing any rounding doubt about the published bound. *Certificate:* exact dual + independent recomputation.

- **P4 - SDP three-point bound, exactly.** Implement the Schrijver/Gijswijt SDP with block-diagonalisation and reproduce a literature SDP bound with certified rational rounding for a small case. *Certificate:* block dual + exact PSD certificate.

- **P5 - Lower-bound improvement.** Improve the best-known \(A(n,d)\) for a specific open cell by a new construction found via SAT/clique/ILP search and verified exactly. *Certificate:* the code + exhaustive distance check + provenance of the search.

- **P6 - Upper-bound improvement.** Tighten the best-known upper bound for a specific open cell via a stronger exact SDP (higher-order / four-point) certificate. *Certificate:* exact-rounded dual + independent PSD check.

- **P7 - Close a gap (windfall).** Determine \(A(n,d)\) exactly for a genuinely open cell - both sides certified and equal.

## 4. Known results and prior art

- **Delsarte (1973)** introduced the linear-programming bound from the Hamming association scheme; the foundational modern upper-bound method.

- **Best, Brouwer, MacWilliams, Odlyzko, Sloane (1978)**, "Bounds for binary codes of length less than 25" (*IEEE Trans. IT*), consolidated small-code bounds; **Best (1978)** gave the nonlinear \((10,40,4)\) code, so \(A(10,4)=40\).

- **McEliece, Rodemich, Rumsey, Welch (1977)** proved the asymptotic second LP (MRRW) bound.

- **Schrijver (2005)** strengthened the LP bound to a semidefinite (three-point) bound via the Terwilliger algebra, improving several small \(A(n,d)\).

- **Gijswijt, Mittelmann, Schrijver (2012)** added block-diagonalisation; **Litjens, Polak, Schrijver** and others extended the hierarchy (**verify** scope and dates).

- **Brouwer's online tables** of \(A(n,d)\) (and constant-weight \(A(n,d,w)\)) are the living reference for current best lower and upper bounds; **consult the live table** for the current open cells and brackets. Constant-weight lower bounds continue to improve (recent 2024–2026 entries; **verify**).

- Construction toolkit: shortening / puncturing / extending, the \((u\mid u+v)\) construction, Best-type nonlinear codes, algebraic-geometry and Goppa codes, and computer search (clique, SAT, ILP) for small optimal codes.

**Status as of mid-2026 - re-verify against the current literature before starting any session.** The table moves: lower bounds improve by new constructions and upper bounds by new SDP hierarchies. Do not trust the specific bracket for \(A(17,4)\) quoted above without checking the current table; confirm the chosen cell is still open and record the exact bracket at session start.

## 5. Attack plan

`[opt]` for certified bounds, `[search]` for constructions; both must terminate in exact certificates.

- **Exact LP (Delsarte).** Build the LP over the distance distribution with exact Krawtchouk coefficients; solve for the dual with an exact/rational LP solver - `QSopt_ex`, `SoPlex` in exact/iterative-refinement mode, or `SageMath`'s exact backend - and verify the dual objective and feasibility in exact rational arithmetic, rounding down soundly. Only the exact dual is a proof; the primal LP guides but does not certify.

- **Exact SDP (Schrijver/Gijswijt).** Symmetry-reduce via the Terwilliger algebra to small blocks; solve numerically at high precision (`SDPA-GMP`), then round the dual to rationals and certify positive semidefiniteness with an exact \(LDL^\top\) / rational spectral argument. A numerically PSD matrix is not a proof.

- **Construction search.** Model "code of size \(\ge M{+}1\) with \(d(C)\ge d\)" as SAT (with DRAT), as a maximum-clique instance in the graph on \(\mathbb{F}_2^n\) with edges for distance \(\ge d\) (`Cliquer`, `MoMC`), or as ILP (`Gurobi`/`SCIP` for exploration, exact re-check afterward). Exploit prescribed automorphism groups (`nauty`, `GAP`) to shrink the search.

- **Exact distance verification.** A standalone checker enumerates all \(\binom{|C|}{2}\) pairs (or uses the weight distribution for linear codes) in exact integer arithmetic.

- **One-workstation scope.** Exact LP is cheap for the \(n\lesssim 30\) range; exact SDP is feasible after symmetry reduction but conditioning-sensitive; clique/SAT constructions are feasible for small \(M\) and modest \(n\). Larger \(n\) or high-order SDP hierarchies exceed one workstation and are out of scope for certification.

- **Failure modes.**

  - Floating-point rounding silently invalidating a "proof."

  - Ill-conditioned SDP blocks that resist exact rational rounding.

  - Clique / ILP solvers timing out without a completeness certificate.

  - Conflating best-known *linear*-code bounds with the unrestricted \(A(n,d)\).

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Every upper bound rests on an exact rational dual (LP) or exactly-rounded PSD dual (SDP); every lower bound on an exact distance verification or a DRAT-backed SAT `UNSAT`. Floating point is exploratory only.

2. **Independent verification.** A separate checker recomputes each LP/SDP dual objective and feasibility in exact arithmetic; a DRAT checker validates SAT `UNSAT`; a second solver or CAS re-derives any constructed code's minimum distance.

3. **Reproducibility.** All codes, dual vectors, Krawtchouk/Terwilliger data, solver versions, precisions, and seeds recorded; SHA-256 manifest over every artifact; the exact \((n,d)\) and its bracket at session start quoted from the live table with an access date.

4. **Preservation.** Search and bound-computation source is part of the record (the Hadamard-668 lost-source lesson); a `NEXT_STEPS.md` records the cell attacked and the remaining gap when pausing.

5. **Honest reporting.** The report states up front whether a full determination (both sides certified and equal) was achieved. A one-sided improvement, a reproduced value, or a floating-only bound is labelled as such and never represented as determining \(A(n,d)\).
