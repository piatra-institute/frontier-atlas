# PROMPT FOR DETERMINING WHETHER FOUR MUTUALLY UNBIASED BASES EXIST IN DIMENSION 6

## The maximal number of mutually unbiased bases in $\mathbb{C}^6$

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 05 of 50 (Tier 1)
**Source:** top-50 list #1, category A (quantum information and foundations)
**Modes:** `[proof]` `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

For every prime-power dimension $d$, the maximal number $N(d)$ of pairwise mutually unbiased bases (MUBs) of $\mathbb{C}^d$ equals $d+1$. Dimension 6 is the first dimension for which $N(d)$ is unknown: three MUBs are easily constructed, twenty-five years of analytic and numerical work have failed to produce a fourth, and Zauner's conjecture asserts $N(6) = 3$. The problem is tightly coupled to the (also open) classification of $6\times 6$ complex Hadamard matrices, and it is unusually well matched to certified computation: excluding a fourth MUB over a *known, parametrized* Hadamard family is a finite algebraic feasibility question amenable to Gröbner bases, resultants, and interval arithmetic with directed rounding, and each excluded family is a freestanding, certifiable milestone. Payoffs: quantum key distribution, optimal state tomography, and the structural theory of complex Hadamard matrices. The complete resolution defined in section 2 is the target; anything less must be reported as a partial result, never represented as a solution.

## 1. Exact problem statement

Two orthonormal bases $\mathcal{B} = \{|b_1\rangle,\dots,|b_d\rangle\}$ and $\mathcal{B}' = \{|b'_1\rangle,\dots,|b'_d\rangle\}$ of $\mathbb{C}^d$ (standard Hermitian inner product) are **mutually unbiased** if

\[
|\langle b_i | b'_j \rangle|^2 \;=\; \frac{1}{d} \qquad \text{for all } 1 \le i, j \le d.
\]

Let $N(d)$ be the largest $m$ such that there exist $m$ pairwise mutually unbiased orthonormal bases of $\mathbb{C}^d$. Standard facts, to be re-proved in-session as calibration:

- $N(d) \le d+1$ for all $d \ge 2$;
- $N(d) = d+1$ when $d$ is a prime power;
- $N(d) \ge 3$ for all $d \ge 2$;
- $N(mn) \ge \min(N(m), N(n))$, hence $N(6) \ge \min(N(2), N(3)) = 3$.

**The problem: decide whether $N(6) \ge 4$, i.e., whether four pairwise mutually unbiased bases of $\mathbb{C}^6$ exist.** Zauner's conjecture (1999): $N(6) = 3$.

**Normalization and Hadamard form.** Bases are identified up to a single global unitary applied to all bases simultaneously, and each basis up to phases and permutations of its elements; a set of MUBs is an equivalence class under these operations. WLOG the first basis is the standard basis $\mathcal{B}_0$; every other basis is then the column set of $\tfrac{1}{\sqrt6} H$ with $H$ a **complex Hadamard matrix** of order 6:

\[
|H_{jk}| = 1 \ \ \forall j,k, \qquad H H^\dagger = 6\,\mathbb{1}.
\]

Bases $\tfrac{1}{\sqrt6}H_1$ and $\tfrac{1}{\sqrt6}H_2$ are mutually unbiased iff $\tfrac{1}{\sqrt6} H_1^\dagger H_2$ is again complex Hadamard. Hadamard matrices are taken up to the standard equivalence

\[
H \sim D_1 P_1 H P_2 D_2
\]

(diagonal unitaries $D_i$, permutation matrices $P_i$), with dephased normal form (first row and column all 1). Thus:

\[
N(6) \ge 4 \iff \exists\, H_1, H_2, H_3 \text{ complex Hadamard of order 6, pairwise unbiased in the sense above.}
\]

This is the formulation adopted here - it is the standard one in the literature, and it turns the question into constrained algebra over a product of $36$-tori. A **MUB quadruple containing a family $\mathcal{F}$** means a set $\{\mathcal{B}_0, H_1, H_2, H_3\}$ as above with $H_1 \in \mathcal{F}$; exclusion results are always stated relative to a precisely defined $\mathcal{F}$ (section 4).

## 2. Complete-resolution standard

One of the following, with all computational steps certified per section 6:

1. **Nonexistence (expected direction).** A proof that no four pairwise MUBs exist in $\mathbb{C}^6$. If computer-assisted, it must decompose into:
   - a proven, exhaustive parametrization of the search space - e.g., a certified complete classification of order-6 complex Hadamard matrices, or a proven reduction to a finite or compact family; and
   - exact or rigorously interval-certified infeasibility over every branch, with replayable certificates: Gröbner/resultant ideal-triviality certificates over exact fields, or interval-arithmetic covers with directed rounding and stored subdivision trees.
2. **Existence.** An explicit quadruple of MUBs: exact entries in a specified number field (or another exactly checkable closed form), with orthonormality and unbiasedness verified in exact arithmetic by an independent checker. A rigorously validated numerical quadruple (an interval enclosure proving existence of a true solution near the numerical one, via a Krawczyk or interval-Newton existence test) is acceptable only as the constructive core, and must be lifted to a computer-checkable existence certificate.

**Not accepted as resolution:**

- Numerical optimization failing to find a fourth basis (any amount of it), or "overwhelming numerical evidence" of nonexistence.
- Exclusion of a fourth MUB for *particular* Hadamard families - even all currently known ones - presented as $N(6)=3$; the classification of order-6 Hadamards is itself open, so family-wise exclusion cannot close the problem without a completeness theorem.
- Nonexistence of a *complete* set of 7 MUBs presented as resolving the 4-MUB question.
- Results restricted to real Hadamard matrices, Butson-type phase alphabets, or other special ansätze presented as unconditional.
- Asymptotic, average-case, entropic, or dimension-generic bounds specialized informally to $d=6$.
- Any claim relying on unverified external computations that are not independently reproduced.

## 3. Graded partial-result targets

**P1 - Re-certify the $\{\mathcal{B}_0, F_6\}$ pair obstruction.**
*Task:* reproduce Grassl's computation by exact Gröbner-basis methods over the relevant cyclotomic field: determine all vectors unbiased to both the standard basis and the Fourier basis $F_6$ (expect a finite set, 48 vectors), and prove that no MUB quadruple contains the pair $\{\mathcal{B}_0, F_6\}$.
*Certificate:* the ideal, the basis-computation transcript, the finite solution list with exact coordinates, and an independent exact checker for variety membership and exhaustiveness (zero-dimensionality plus degree count).
*Effort:* single workstation, days.

**P2 - Re-certify the Fourier-family exclusion.**
*Task:* reproduce, with an independent toolchain (interval arithmetic in Arb plus exact algebra at degenerate strata), the Jaming–Matolcsi–Móra–Szöllősi–Weiner-type result that no member of the two-parameter Fourier family $F(a,b)$ belongs to a quadruple of MUBs.
*Certificate:* a stored cover of the parameter torus by boxes, each carrying a directed-rounding infeasibility bound; exact treatment of boundary strata; an independent replay checker.
*Effort:* weeks; embarrassingly parallel.

**P3 - New certified exclusion for a previously unexcluded family.**
*Task:* extend the P2 machinery to a precisely defined stratum of known order-6 Hadamards not previously excluded - priority order: Karlsson's $H_2$-reducible three-parameter family, the Szöllősi family, and any case remaining open for the isolated Tao matrix $S_6$ (verify the literature per family first; McNulty–Weigert have partial statements).
*Certificate:* as P2, plus a proof that the parametrization used covers the family as defined.
*Value:* each newly excluded family is an independently publishable milestone - this is the brief's named certifiable target.

**P4 - Unconditional upper bound via certified relaxation.**
*Task:* implement a symmetry-reduced semidefinite/Lasserre or Delsarte-type hierarchy for MUB counting (cf. Gribling–Polak) with exact rational dual certificates. Any unconditional certified bound $N(6) \le 6$ combines with Weiner's theorem ($N(d) \ne d$) to yield $N(6) \le 5$ - a genuinely new theorem.
*Certificate:* rational dual certificate checked by exact PSD verification; reproduction of known small-$d$ values validates the pipeline first.

**P5 - Certified completeness for a Hadamard subclass, with exclusion over it.**
*Task:* prove a completeness theorem for a defined subclass of order-6 Hadamards (e.g., all Butson-type $BH(6,k)$ for $k$ up to a stated bound, or the $H_2$-reducible class per Karlsson, re-verified), then run the P2/P3 exclusion over the entire subclass.
*Value:* the structural template from which a full nonexistence proof would eventually be assembled.

**P6 - Full resolution** per section 2.

Honest calibration: a complete proof of $N(6)=3$ likely requires a completeness theorem for order-6 complex Hadamard matrices that does not yet exist. P1–P3 are the realistic session products; P4 would be a headline.

## 4. Known results and prior art

- $N(d) = d+1$ for primes: Ivanović (1981); for prime powers: Wootters–Fields (1989). Upper bound $N(d) \le d+1$: standard.
- Zauner's conjecture $N(6) = 3$: Zauner (1999, thesis).
- Grassl (~2004): computer-algebra proof that exactly 48 vectors are unbiased to both the identity and Fourier bases; no MUB quadruple contains the pair $\{\mathcal{B}_0, F_6\}$ (verify exact statement).
- Jaming–Matolcsi–Móra–Szöllősi–Weiner (~2009–2010): the Fourier family $F(a,b)$ cannot be extended to four MUBs; related infinite families of MUB triples (verify the precise scope of the rigorous exclusion).
- Brierley–Weigert (~2008–2010): extensive numerical searches; never more than 3 MUBs found; triples constructed throughout the known Hadamard landscape.
- Butterley–Hall (~2007): early numerical evidence for $N(6) = 3$.
- Weiner (~2013): the maximal number of MUBs is never exactly $d$; consequently a proof of $N(6) \le 6$ would immediately give $N(6) \le 5$ (verify statement details).
- McNulty–Weigert (~2012): strong restrictions on which known order-6 Hadamards can appear in MUB triples and quadruples (verify exact per-family statements).
- Order-6 complex Hadamard landscape: Tao's isolated matrix $S_6$ (~2004); the Diță family; Björck's circulant; Beauchamp–Nicoara self-adjoint family (~2006); Szöllősi family (~2010); Karlsson's $H_2$-reducible three-parameter classification (~2011); Tadej–Życzkowski online catalogue (2006 onward). The full classification remains open.
- Matolcsi (~2012): Fourier-analytic/Delsarte approach to MUB bounds.
- Gribling–Polak (~2021–2023): polynomial-optimization and SDP formulations for MUB existence with symmetry reduction (verify current strength at $d=6$).
- Context: the classical 36-officers obstruction (Tarry, ~1900) blocks only Latin-square-type constructions; its *quantum* analogue was solved positively in 2021, a caution against intuition transfer in $d=6$.

**Status as of mid-2026 - re-verify against current literature before starting the session.**

## 5. Attack plan

**Exact algebra (P1).**

- SageMath driving Singular or msolve; variables = entries of a candidate vector $v \in \mathbb{C}^6$ unbiased to $\mathcal{B}_0$ and $F_6$.
- Encode unimodularity as $z_k \bar z_k = 1$ with conjugates as independent variables; work over $\mathbb{Q}(\zeta_6)$, or over $\mathbb{Q}$ after real/imaginary splitting.
- Confirm zero-dimensionality; enumerate solutions exactly; check assembly obstructions by exact linear algebra.
- Failure mode: Gröbner blowup - mitigate with dephased normal forms, equivalence-group symmetry reduction, and msolve's multi-modular engine.

**Interval exclusion over families (P2–P3).**

- Custom C++ (or Arb via Python bindings) branch-and-bound over family parameters: per box, a directed-rounding bound showing the unbiasedness system for a completing pair/triple is infeasible; recurse on failure.
- Measure-zero strata where intervals cannot close are handed to exact algebra (Gröbner at exact parameter values).
- Store the full subdivision tree; it is the certificate.
- Failure modes: clusters of near-solutions stalling subdivision (switch to interval-Newton isolation plus exact local nonexistence proof); mis-parametrized families (prove the parametrization covers the family before excluding over it).

**SDP hierarchy (P4).**

- Model in SageMath/Python; solve with high-precision SDP (SDPA-GMP class); round duals to rational feasible certificates; verify by exact arithmetic (Pari/GP or SageMath).
- Failure mode: rounding destroys feasibility - build margin by strengthening the objective before rounding.

**Workstation budget.**

- P1 and P4: single workstation.
- P2–P3: single workstation for one family (days–weeks); a small cluster for the union of families.

**Search hygiene.**

- All floating-point exploration (gradient searches for a fourth basis) is labeled exploratory.
- A found near-quadruple triggers the validated-numerics existence pipeline - never a headline before the lift.

## 6. Verification and auditability requirements

1. **Exact arithmetic.** Gröbner and resultant certificates over exact fields; interval arithmetic exclusively with directed rounding (Arb/MPFI); no double-precision quantity enters any certified claim.
2. **Independent verification.** Standalone checkers, written independently of the search code, for: ideal-membership and ideal-triviality certificates; the finite solution lists of P1 (exact re-substitution); box-cover infeasibility replays (dual implementations, Python and C++, compared box-by-box); rational SDP certificates (exact PSD checks via $LDL^T$ over $\mathbb{Q}$).
3. **Reproducibility.** Every run records tool versions, parameters, subdivision policies, and seeds; SHA-256 manifest over ideals, bases, covers, certificates, and logs; one driver script per target replays any leaf claim from the manifest.
4. **Preservation.** Family parametrizations with their correctness proofs, all search and exclusion code, and all failed-branch data are preserved; exploratory numerics that informed but do not support claims are archived and labeled as such.
5. **Honest reporting.** The report opens with whether section 2 was met (expected: no); states exactly which families are excluded, under which parametrization and equivalence conventions; and never conflates family-wise exclusion with $N(6) = 3$.
