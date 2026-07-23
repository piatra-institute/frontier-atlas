# PROMPT FOR DECIDING THE EXISTENCE OF NPT BOUND ENTANGLEMENT

## Undistillability of negative-partial-transpose Werner states, beginning with two copies

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 10 of 50 (Tier 1)
**Source:** top-50 list #3, category A (quantum information and foundations)
**Modes:** `[proof]` `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Whether every entangled state with negative partial transpose (NPT) can be distilled into pure entanglement is the oldest structural open problem of entanglement theory, open since about 2000. By known symmetrization arguments it reduces to the conjectured undistillability of a one-parameter family of Werner states, and its first genuinely open rung - 2-copy undistillability of the critical Werner states - is a *concrete, finite-dimensional* polynomial feasibility problem: a Hermitian quartic form must be shown nonnegative over the manifold of Schmidt-rank-2 vectors. That shape - heavily symmetric polynomial optimization, SDP relaxations, exact rational certificates - sits squarely within current certified-computation methods, even though 25 years of attempts warn that the final inequality is delicate. Payoff: the existence or impossibility of NPT bound entanglement fixes the axiomatic structure of entanglement distillation and the fate of several reversibility conjectures. The complete resolution defined in section 2 is the target; anything less must be reported as a partial result, never represented as a solution.

## 1. Exact problem statement

Work on $\mathbb{C}^d \otimes \mathbb{C}^d$. Let $F = \sum_{i,j}|ij\rangle\langle ji|$ be the swap operator and $T_B$ the partial transpose on the second tensor factor in the computational basis. A bipartite state $\rho$ is **NPT** if $\rho^{T_B}$ has a negative eigenvalue.

For $n \ge 1$, $\rho$ is **$n$-distillable** if there exists a vector $|\psi\rangle \in (\mathbb{C}^{d})^{\otimes n} \otimes (\mathbb{C}^{d})^{\otimes n}$ (bipartition $A^n : B^n$) of Schmidt rank at most 2 across $A^n : B^n$ such that

\[
\langle\psi|\,\big(\rho^{\otimes n}\big)^{T_{B^n}}\,|\psi\rangle \;<\; 0 .
\]

$\rho$ is **distillable** iff it is $n$-distillable for some $n$. This Schmidt-rank-2 characterization (the Horodecki criterion) is adopted as the definition here: it is the formulation every computational attack uses, and its equivalence to the operational LOCC definition is a known theorem to be cited, not re-proved.

**Werner family (adopted normalization).** For $\alpha \in [-1, 1]$ define on $\mathbb{C}^d\otimes\mathbb{C}^d$

\[
\rho_\alpha \;=\; \frac{\mathbb{1} - \alpha F}{d^2 - d\alpha} .
\]

Calibration facts, to be re-derived exactly in-session:

- $F^{T_B} = d\,|\phi^+\rangle\langle\phi^+|$ with $|\phi^+\rangle = \tfrac{1}{\sqrt d}\sum_i |ii\rangle$; hence $\rho_\alpha$ is NPT iff $\alpha > 1/d$;
- $\rho_\alpha$ is separable iff $\alpha \le 1/d$;
- $\rho_\alpha$ is 1-distillable iff $\alpha > 1/2$;
- the open region is therefore $\alpha \in (1/d,\, 1/2]$, $d \ge 3$.

**The problem.** Do there exist NPT states that are not distillable? By the known reduction (twirling plus local filtering), it suffices to decide the Werner family: the conjecture (DiVincenzo–Shor–Smolin–Terhal; Dür–Cirac–Lewenstein–Bruß, ~2000) is that for $d \ge 3$ every $\rho_\alpha$ with $\alpha \in (1/d, 1/2]$ is undistillable - i.e., NPT bound entanglement exists.

**Primary concrete target adopted here: $d = 3$; prove or refute 2-undistillability of $\rho_{1/2}$** (then of the range $\alpha \in (1/3, 1/2]$): decide whether

\[
M_2(\alpha) \;=\; \min_{\substack{|\psi\rangle,\ \||\psi\rangle\|=1 \\ \operatorname{SR}_{A^2:B^2}(\psi) \le 2}} \langle\psi|\big(\rho_\alpha^{\otimes 2}\big)^{T_{B^2}}|\psi\rangle \;\ge\; 0 \quad\text{at } \alpha = \tfrac12 .
\]

Writing $|\psi\rangle = |x_1\rangle|y_1\rangle + |x_2\rangle|y_2\rangle$ with $x_i \in \mathbb{C}^9$ (the $A$ side) and $y_i \in \mathbb{C}^9$ (the $B$ side), $M_2$ is the minimum of a Hermitian quartic form in $(x_1, x_2, y_1, y_2)$ - real polynomial optimization in 72 real variables, with a large symmetry group: $\rho_\alpha^{\otimes 2}$ is invariant under collective $U \otimes U$ actions on each copy, so the walled Brauer algebra controls the invariant structure and must be exploited.

## 2. Complete-resolution standard

One of:

1. **NPT bound entanglement exists.** A proof that some explicit NPT state - e.g., $\rho_\alpha$ at $d = 3$ and a stated $\alpha \in (1/3, 1/2]$ - is $n$-undistillable for *every* $n$. Computer-assisted ingredients (per-$n$ certificates, inductive structure) must be exact and independently checkable, and the induction over $n$ must be a proof, not extrapolation from small $n$.
2. **No NPT bound entanglement.** A proof that every NPT state is distillable - e.g., for each $\alpha > 1/d$ an $n(\alpha)$ and an explicit Schmidt-rank-2 witness with exactly certified negative expectation, together with an argument covering the full parameter range (not a sample of points).

**Not accepted as resolution:**

- 2-copy (or any fixed-$n$) undistillability presented as the full conjecture; these are milestones (P3–P5), not the resolution.
- Numerical SDP values without exact dual certificates; local optimization over Schmidt-rank-2 vectors reporting "no negative value found".
- Results about twirled/symmetric relaxations, or about PPT-assisted protocols, presented as LOCC (un)distillability - the protocol class of every claim must be stated.
- Claims certified at sampled $\alpha$ values presented as covering an interval; interval coverage requires parametric certificates or exact continuity arguments.
- Rank-restricted results (e.g., distillability of low-rank NPT states) presented as general.
- Heuristic "evidence" of any kind represented as more than evidence.

## 3. Graded partial-result targets

**P1 - Exact re-derivation of the classical thresholds.**
*Task:* separability, NPT, and 1-distillability boundaries of the Werner family for general $d$, in exact arithmetic, including the closed form of $M_1(\alpha)$; plus a written replication (with citations) of the reduction chain: twirling, sufficiency of the Werner family, sufficiency of Schmidt rank 2.
*Certificate:* symbolic derivations (SymPy/SageMath) with a numerical cross-check harness.
*Effort:* days; calibrates every convention downstream.
*Note:* also verify $\operatorname{Tr}\rho_\alpha = 1$ and the spectrum of $\rho_\alpha^{T_B}$ symbolically as unit tests for the convention module.

**P2 - Symmetry-reduced exact reformulation of $M_2(\alpha)$.**
*Task:* carry out the walled-Brauer/isotypic decomposition of $(\rho_\alpha^{\otimes 2})^{T_{B^2}}$ and of the Schmidt-rank-2 constraint's orbit structure, producing an equivalent minimization over a drastically smaller explicit semialgebraic set, with machine-checked equivalence (exact rational projectors; idempotency, orthogonality, and completeness identities verified in GAP/SageMath).
*Certificate:* the projector identities plus a proof memo; reusable artifact.
*Note:* historically this is where errors creep in - certify the reformulation itself.

**P3 - Certified bounds on $M_2(1/2)$ at $d = 3$.**
*Task:* run the Lasserre/SOS hierarchy (symmetry-reduced) on the P2 reformulation at increasing levels with high-precision SDP; round to exact rational certificates. Ranked outcomes:
  (a) exact certificate $M_2(1/2) \ge 0$ - *proves 2-copy undistillability at the critical point*, a 25-year milestone;
  (b) certified $M_2(1/2) \ge -\varepsilon$ for tiny rational $\varepsilon$, plus the best certified upper bound - report both honestly;
  (c) a Schmidt-rank-2 witness with exactly certified negative value - refuting 2-copy undistillability at $\alpha = 1/2$, a major result in the other direction.
*Certificate:* rational SOS/moment certificates verified by exact PSD checks, or an exact algebraic witness vector evaluated exactly.
*Effort:* the core weeks-long computation of the session; escalate hierarchy levels as memory allows.

**P4 - Parametric 2-copy result on a subinterval.**
*Task:* extend P3 from the point $\alpha = 1/2$ to certified statements over intervals: SOS certificates with polynomial dependence on $\alpha$, or interval subdivision with directed rounding. Even 2-undistillability for $\alpha \in (1/3, 1/3 + \delta]$ with certified $\delta > 0$ would, if new, be publishable - but verify first which fixed-$n$ statements near the separable boundary were already proved rigorously (~2000 literature is ambiguous between "proved" and "numerically supported"; pin it down).
*Certificate:* parametric certificates plus the literature audit.
*Effort:* incremental over P3 once the point certificates exist.

**P5 - Three copies, or structural leverage.**
*Task:* either push the machinery to $M_3$ (expect severe scaling; certified statements about *why* the hierarchy fails to scale are themselves worth recording), or prove a new structural theorem - e.g., a clean matrix-inequality equivalent of the 2-copy question sharpening the Pankowski–Piani–Horodecki–Horodecki-style reformulations, with machine-verified steps.
*Certificate:* proofs plus replayable computations.
*Effort:* speculative; time-box it after P3–P4 are secured.

**P6 - Full resolution** per section 2.

Honest calibration: full resolution is unlikely. P3(a) is the flagship realistic-but-hard target this problem was selected for; P1–P3 are the expected session products.

## 4. Known results and prior art

- Distillation protocols: Bennett et al. (~1996). PPT states are undistillable; PPT entangled ("bound entangled") states exist: Horodecki–Horodecki–Horodecki (~1997–1998).
- Schmidt-rank-2 characterization of distillability: Horodecki et al. (~1998).
- The NPT conjecture and the Werner-family reduction: DiVincenzo–Shor–Smolin–Terhal (with Thapliyal) (~2000); Dür–Cirac–Lewenstein–Bruß (~2000). Both give evidence that critical Werner states are undistillable; verify exactly which fixed-$n$ claims were rigorously proved versus numerically supported before relying on any of them.
- Many copies can be necessary: Watrous (~2004) - states that are $n$-distillable only for large $n$; cautionary against fixed-$n$ intuition.
- Reformulations and partial progress: Pankowski–Piani–Horodecki–Horodecki (~2007–2010), equivalent formulations of 2-copy undistillability; Chen–Đoković (~2010s), distillability of low-rank NPT states (rank $\le 4$-type statements) (verify exact rank hypotheses); SDP hierarchies bounding distillable entanglement (Wang–Duan line, ~2016 onward) (verify).
- Rains bounds and PPT-assisted distillation (~1999–2001): context for what survives relaxation of LOCC to PPT operations; the standard question is LOCC.
- Representation-theoretic toolkit for $U \otimes U$-invariant problems: Eggeling–Werner (~2001) for Werner-symmetry decompositions; walled Brauer algebra literature.

**Status as of mid-2026 - re-verify against current literature before starting the session; search specifically for post-2020 claims on 2-copy undistillability.**

## 5. Attack plan

**Exact symbolic layer (P1–P2).**

- SageMath/SymPy for operators on $(\mathbb{C}^3)^{\otimes 4}$; the ambient dimension (81 per side) is only notation - the twirled invariant algebra is tiny.
- GAP/SageMath for the walled-Brauer isotypic decomposition, with exact rational projectors verified by idempotency and completeness identities.
- Failure mode: bookkeeping errors in tensor-factor ordering and partial-transpose conventions - freeze all conventions in one module with unit tests against the known thresholds of P1.

**SOS/moment layer (P3–P4).**

- Two cross-checking encodings: (i) direct polynomial optimization in $(x_1, x_2, y_1, y_2)$ with normalization constraints; (ii) optimization over rank-$\le 2$ operator variables with PSD/trace constraints (SDP-representable outer shell plus rank cuts).
- Solvers: SDPA-GMP or equivalent high-precision SDP; symmetry-reduce first (block-diagonalization by the invariance group; expect orders-of-magnitude shrinkage).
- Rational rounding: project the numerical dual onto the exactly feasible cone with margin; verify by exact $LDL^T$ over $\mathbb{Q}$.
- Failure modes: required hierarchy level exceeds memory (mitigate via symmetry, sparsity, and the P2 reduction); numerically-tight-but-negative bounds tempting over-claim (forbidden: report the certified interval only).

**Witness search (refutation direction).**

- Aggressive nonconvex search for $M_2 < 0$: manifold optimization over Schmidt-rank-2 vectors, simulated annealing, many restarts, in C++; sweep $\alpha$ across $(1/3, 1/2]$.
- Any hit goes to exact lift: rational approximation of the witness plus exact evaluation of the exact quartic form (the form is exact, so certification is direct evaluation).
- Cheap to run continuously; history says automate it well.

**Cross-validation.**

- Every certified bound from the reduced formulation is recomputed from the unreduced formulation at low precision, as a sanity check that symmetry reduction preserved the problem.

**Workstation budget.**

- P1–P2: trivial to light.
- P3 at low hierarchy levels: single workstation (symmetry-reduced blocks expected in the hundreds of dimensions); higher levels may need 256 GB+ memory - record the wall honestly.
- $M_3$: likely out of reach without new reductions; if hit, say so and document the scaling data.

## 6. Verification and auditability requirements

1. **Exact arithmetic.** All final certificates rational or algebraic: SOS Gram matrices verified positive semidefinite by exact $LDL^T$ over $\mathbb{Q}$; witness values by exact evaluation of the exact quartic; interval arithmetic (Arb) with directed rounding for parametric-in-$\alpha$ covers.
2. **Independent verification.** Standalone checkers, independent of the modeling code, for: SOS certificates (exact-arithmetic Python and C++ implementations, cross-compared); the isotypic-projector identities of P2; witness evaluations. The P2 equivalence is written up mathematically and its computational steps replayed by the checker.
3. **Reproducibility.** SDP solver versions, precisions, and schedules; search seeds and restart logs; SHA-256 manifest over models, duals, certificates, projectors, and code; a driver re-verifies any claim from stored artifacts alone.
4. **Preservation.** All modeling and search code, failed hierarchy levels with their numerical duals, and near-witnesses preserved; the convention-freezing module is part of the record; anything unpreserved is declared.
5. **Honest reporting.** The report opens with whether section 2 was met (expected: no) and which of P1–P5 were achieved; every bound appears with its certified sign and margin; fixed-$n$ and fixed-$\alpha$ results are never extrapolated in summary language, and protocol classes (LOCC vs. PPT) are named wherever a distillability claim appears.
