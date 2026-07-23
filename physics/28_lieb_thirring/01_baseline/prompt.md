# PROMPT FOR DETERMINING THE SHARP LIEB–THIRRING CONSTANT AT γ = 1

## The optimal constant in the Lieb–Thirring inequality governing stability of matter

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 28 of 50 (Tier 3)
**Source:** top-50 list #18, category B (rigorous many-body and condensed matter)
**Modes:** `[bound]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The Lieb–Thirring inequality bounds Riesz means of the negative eigenvalues of a Schrödinger operator $-\Delta+V$ by a semiclassical phase-space integral of the potential.
At the physically decisive exponent $\gamma=1$ - the case dual to the kinetic-energy inequality underlying the Lieb–Thirring proof of stability of matter and all density-functional lower bounds - the sharp constant $L_{1,d}$ is unknown in every dimension.
The proven constant sits at $1.456$ times the semiclassical value (Frank–Hundertmark–Jex–Nam 2021), while the conjectured sharp values are $2/\sqrt{3}\approx 1.1547$ times semiclassical in $d=1$ and (after Frank–Gontier–Lewin 2021 refuted the one-bound-state branch of the 1976 conjecture in the relevant range) exactly semiclassical in $d\ge 2$ (verify).
The gap between $1.456$ and the conjectured values is a genuine optimization problem over proof structures with machine-checkable ground truth, which is why this problem is matched to current AI methods in `[bound]` mode.
The complete resolution defined in section 2 - the exact sharp constant with proof - is the target; anything less must be reported as a partial result, never represented as a solution.

## 1. Exact problem statement

Work on $L^2(\mathbb{R}^d)$, $d\ge 1$, with the Schrödinger operator $H_V=-\Delta+V$, defined as the Friedrichs extension of the quadratic form $\int |\nabla u|^2 + V|u|^2$ on $C_c^\infty(\mathbb{R}^d)$. Write $V_\pm=\max(\pm V,0)$. For $\gamma\ge 0$ define the Riesz mean

\[
\operatorname{Tr}\,(H_V)_-^{\gamma} \;=\; \sum_{j} |E_j|^{\gamma},
\]

the sum over all negative eigenvalues $E_1\le E_2\le\cdots<0$ of $H_V$ (counted with multiplicity).
The Lieb–Thirring inequality states: there is a finite constant $L_{\gamma,d}$ such that for all $V$ with $V_-\in L^{\gamma+d/2}(\mathbb{R}^d)$,

\[
\operatorname{Tr}\,(H_V)_-^{\gamma}\;\le\; L_{\gamma,d}\int_{\mathbb{R}^d} V_-(x)^{\gamma+d/2}\,dx .
\]

It holds iff $\gamma\ge 1/2$ ($d=1$), $\gamma>0$ ($d=2$), $\gamma\ge 0$ ($d\ge 3$; $\gamma=0$ is Cwikel–Lieb–Rozenblum).
Here $L_{\gamma,d}$ denotes the *smallest* admissible constant - the sharp constant. The semiclassical constant is

\[
L^{\mathrm{cl}}_{\gamma,d}
=\;(2\pi)^{-d}\int_{\mathbb{R}^d}\big(|p|^2-1\big)_-^{\gamma}\,dp
\;=\;\frac{\Gamma(\gamma+1)}{(4\pi)^{d/2}\,\Gamma(\gamma+d/2+1)},
\]

e.g. $L^{\mathrm{cl}}_{1,1}=\tfrac{2}{3\pi}$ and $L^{\mathrm{cl}}_{1,3}=\tfrac{1}{15\pi^2}$.
Weyl asymptotics give $L_{\gamma,d}\ge L^{\mathrm{cl}}_{\gamma,d}$ always.
Define the finite-rank constants $L^{(N)}_{\gamma,d}$ as the sharp constants when $\operatorname{Tr}(H_V)_-^\gamma$ is replaced by $\sum_{j\le N}|E_j|^\gamma$; $L^{(1)}_{\gamma,d}$ is the one-bound-state constant, computable from a Gagliardo–Nirenberg-type variational problem (Keller 1961 in $d=1$; in particular $L^{(1)}_{1,1}=\tfrac{2}{\sqrt3}\,L^{\mathrm{cl}}_{1,1}$).

**The problem.** Determine the sharp constant $L_{1,d}$ - primarily for $d=3$ (stability of matter) and $d=1$ (the cleanest conjectural picture) - with proof. Equivalently, determine the ratio $R_{1,d}=L_{1,d}/L^{\mathrm{cl}}_{1,d}$.

**Conjecture landscape (state precisely; do not conflate).**

- Laptev–Weidl 2000: $L_{\gamma,d}=L^{\mathrm{cl}}_{\gamma,d}$ for all $\gamma\ge 3/2$, all $d$. Sharp and closed.
- Hundertmark–Lieb–Thomas 1998: $L_{1/2,1}=\tfrac12=2L^{\mathrm{cl}}_{1/2,1}$, sharp, saturated in a rank-one (delta-potential) limit.
- The 1976 Lieb–Thirring conjecture asserted $L_{\gamma,d}=\max\{L^{\mathrm{cl}}_{\gamma,d},\,L^{(1)}_{\gamma,d}\}$.
  Frank–Gontier–Lewin 2021 proved that for $\gamma>\max(0,2-d/2)$ the one-bound-state constant is not optimal (rank-one trial potentials are beaten), refuting the $L^{(1)}$ branch at $\gamma=1$ for $d\ge 2$ (verify the exact range) and leading to the revised conjecture $L_{1,d}=L^{\mathrm{cl}}_{1,d}$ for $d\ge 2$ (verify).
- In $d=1$, $\gamma=1<3/2=2-d/2$: the classical conjecture $L_{1,1}=L^{(1)}_{1,1}=\tfrac{2}{\sqrt3}L^{\mathrm{cl}}_{1,1}$ still stands.
- Best proven bound at $\gamma=1$, all $d$: $R_{1,d}\le 1.456$ (Frank–Hundertmark–Jex–Nam 2021).

**Duality with the kinetic inequality.** For $L^2$-orthonormal $u_1,\dots,u_N\in H^1(\mathbb{R}^d)$ and $\rho=\sum_i|u_i|^2$,

\[
\sum_{i=1}^N\int_{\mathbb{R}^d}|\nabla u_i|^2\,dx\;\ge\;K_d\int_{\mathbb{R}^d}\rho^{1+2/d}\,dx,
\qquad
K_d=\frac{d}{d+2}\Big(\frac{2}{(d+2)\,L_{1,d}}\Big)^{2/d},
\]

by Legendre duality; sharp $L_{1,d}$ and sharp $K_d$ are equivalent data.
Any claimed constant must state which normalization ($\hbar=1$, mass $=1/2$ as above) it uses; mismatched normalizations are a standing source of published-constant confusion.

## 2. Complete-resolution standard

A complete resolution, for a stated dimension $d\in\{1,2,3\}$, consists of:

1. An exact closed-form (or algorithmically exactly computable) value of $L_{1,d}$.
2. A complete proof of the upper bound $\operatorname{Tr}(H_V)_-\le L_{1,d}\int V_-^{1+d/2}$ for *all* admissible $V$, at the claimed value - not for a restricted class.
3. A matching optimality statement: either an explicit optimizing potential/sequence saturating the constant, or a proof that the semiclassical Weyl bound is the supremum (when $L_{1,d}=L^{\mathrm{cl}}_{1,d}$, item 3 is automatic).
4. If any step relies on computation (an optimization, an eigenvalue enclosure, a definite integral), that step must be certified in exact or interval arithmetic with an independent checker, per section 6.

Disproof branches also count as complete resolution of the corresponding conjecture: a certified trial potential proving $L_{1,d}>L^{\mathrm{cl}}_{1,d}$ for some $d\ge2$, or $L_{1,1}>L^{(1)}_{1,1}$, would resolve the respective conjecture negatively and is a fully acceptable outcome.

**Not accepted as resolution:**

- Any improvement of $1.456$ that does not reach the sharp value (this is target P3, a partial result).
- Sharpness proven only within a restricted class: radial potentials, one-dimensional-reducible potentials, finite-rank Riesz means $L^{(N)}$, or potentials with prescribed sign/shape.
- Numerical evidence (floating-point optimization of trial potentials, non-certified eigenvalue computations) that the conjectured value is sharp.
- Semiclassical or formal expansions without uniform remainder control.
- Sharp constants for $\gamma\neq 1$ presented as if they settle $\gamma=1$ (Aizenman–Lieb monotonicity transfers bounds only in one direction and degrades constants).
- The dual kinetic inequality with a constant claimed sharp but derived from a non-sharp $L_{1,d}$.

## 3. Graded partial-result targets

Full resolution is unlikely in a session; the graded targets below are the goal. Each carries its own certificate standard.

- **P1 - Certified reproduction of the FHJN 1.456 bound.**
  Re-derive the Frank–Hundertmark–Jex–Nam proof to the point where the constant is an explicit finite-dimensional optimization (their argument, via Rumin's momentum decomposition, ends in a numerically optimized expression).
  Certify, with interval arithmetic (Arb), that the optimized expression is $\le 1.456$ (and compute the enclosure of their optimum to $\ge 10$ digits).
  *Certificate:* a standalone interval-arithmetic checker evaluating the closed-form objective at the certified parameter point, plus a human-readable derivation that the objective rigorously dominates $R_{1,d}$.
  This reproduces the known frontier with our own verified toolchain.
- **P2 - Certified one-bound-state constants.**
  Compute certified enclosures of $L^{(1)}_{1,d}$ for $d=1,2,3$ by solving the associated Euler–Lagrange ODE (radial Lane–Emden-type equation) with validated integration, including a proof of optimizer existence/uniqueness in the radial class or citation-plus-verification of the known one.
  In $d=1$ verify the exact value $\tfrac{2}{\sqrt3}L^{\mathrm{cl}}_{1,1}$ symbolically.
  *Certificate:* interval enclosures with two independent ODE-enclosure implementations agreeing.
- **P3 - Improve the constant $1.456$.** The genuine `[bound]` target.
  Search over extensions of the FHJN/Rumin proof structure - richer momentum decompositions, additional free functions/parameters in the trial decomposition, interpolation with the Laptev–Weidl operator-valued lifting - for a certified constant $<1.456$ at $\gamma=1$.
  Every candidate improvement reduces to a finite-dimensional or low-dimensional functional optimization whose validity is machine-checkable.
  *Certificate:* the new inequality chain written out in full, with every numerical constant enclosed in interval arithmetic and an independent checker for the final evaluation.
  Even a $1.44$ would be a publishable frontier move.
- **P4 - Map the finite-rank landscape in $d=1$.**
  Certified enclosures of $L^{(N)}_{\gamma,1}$ for $N=1,2,3$ and $\gamma\in\{0.6,0.8,1.0,1.2,1.4\}$, testing the Frank–Gontier–Lewin monotonicity picture and locating where (if anywhere) $L^{(2)}>L^{(1)}$ in $d=1$ - direct evidence for or against the surviving $d=1$ conjecture.
  *Certificate:* validated multi-bound-state variational computations with rigorous truncation bounds; upper bounds are rigorous by evaluation, lower bounds require certified optimality gaps and must be labeled as such.
- **P5 - Lean 4 formalization of the core chain.**
  Formalize: (a) the Birman–Schwinger principle for $-\Delta+V$ in $d=1$; (b) Aizenman–Lieb monotonicity of $L_{\gamma,d}/L^{\mathrm{cl}}_{\gamma,d}$ in $\gamma$; (c) target of opportunity - the Hundertmark–Lieb–Thomas $\gamma=1/2$, $d=1$ sharp proof.
  Scope honestly: mathlib's unbounded-operator spectral theory is thin; (a)–(b) are realistic, (c) is stretch.
  *Certificate:* compiling Lean artifacts with `#print axioms` clean.
- **P6 - Sharpness in a new regime.** Strongest short of resolution: extend the set of $(\gamma,d)$ with known sharp constant - e.g. prove $L_{\gamma,1}=L^{(1)}_{\gamma,1}$ for some $\gamma\in(1/2,3/2)$, or prove $R_{1,d}\to 1$ as $d\to\infty$ with explicit rate (verify what is known about dimensional asymptotics first).
  *Certificate:* complete proof, with any computational lemmas certified per section 6.

## 4. Known results and prior art

- Lieb–Thirring 1975–1976: the inequality, the kinetic dual, and stability of matter; original conjecture $L_{\gamma,d}=\max\{L^{\mathrm{cl}},L^{(1)}\}$.
- Keller 1961: sharp one-eigenvalue bound in $d=1$ (closed form for $L^{(1)}_{\gamma,1}$).
- Aizenman–Lieb 1978: monotonicity of $\gamma\mapsto L_{\gamma,d}/L^{\mathrm{cl}}_{\gamma,d}$.
- Cwikel 1977, Lieb 1976, Rozenblum 1972: $\gamma=0$, $d\ge3$ (CLR bound).
- Hundertmark–Lieb–Thomas 1998: sharp $L_{1/2,1}=1/2$.
- Laptev–Weidl 2000: sharp semiclassical constant for $\gamma\ge 3/2$, all $d$, via operator-valued inequalities; Hundertmark–Laptev–Weidl 2000: factor-2 bound for $\gamma\ge1/2$ (verify exact range).
- Eden–Foias 1991 ($d=1$) and Dolbeault–Laptev–Loss 2008 (lifting to all $d$): $R_{1,d}\le \pi/\sqrt3\approx 1.814$ for $\gamma\ge1$.
- Frank–Hundertmark–Jex–Nam 2021 (J. Eur. Math. Soc., "The Lieb–Thirring inequality revisited"): $R_{1,d}\le 1.456$ for all $d$, $\gamma\ge1$; proof contains an explicitly optimizable component.
- Frank–Gontier–Lewin 2021 (Comm. Math. Phys.): finite-rank optimizers are never optimal for $\gamma>\max(0,2-d/2)$; reshapes the conjecture at $\gamma=1$, $d\ge2$ toward $L^{\mathrm{cl}}$ (verify precise statements before relying on them).
- Frank–Laptev–Weidl 2022 (book, CUP): current-state survey of the whole field - the canonical reference for exact constants and normalizations.
- Levitt ~2014: careful floating-point numerics on best constants (verify); useful as non-certified ground truth for P2/P4.

**Status as of mid-2026 - re-verify against current literature before starting the session.**

## 5. Attack plan

`[bound]` mode; single-workstation scale throughout.

1. **FHJN objective extraction (week-1 computation).**
   Transcribe the FHJN proof into an explicit objective $F(\text{params})\ge R_{1,d}$; implement in Arb (via python-flint or C) with directed rounding; certify their optimum.
   Expected effort: the transcription, not the computation.
   Failure mode: the published argument may leave minor normalization choices implicit - resolve them against the Frank–Laptev–Weidl book before certifying.
2. **One-bound-state ODE enclosures.** Validated integration of the radial Euler–Lagrange equation (interval Taylor methods in Arb; independent check with a second method, e.g. rigorous Chebyshev spectral enclosure).
   Shooting parameter enclosed by interval bisection with sign-change certificates.
   Failure mode: near-degenerate shooting sensitivity - mitigate with high precision (Arb makes this cheap).
3. **Proof-structure search for P3.** Parameterize Rumin-type decompositions by a small number of free functions discretized on coarse grids; optimize in floating point for exploration; *only* certified re-evaluation in interval arithmetic counts.
   Keep a strict wall between exploration (float) and certification (Arb).
   Failure mode: optimization landscape flatness near 1.456 - treat plateaus as evidence the proof family is exhausted, and report that as a finding.
4. **Finite-rank variational computations (P4).**
   Trial potentials as splines/sums of exponentials with rational parameters; eigenvalues of $-\tfrac{d^2}{dx^2}+V$ enclosed via validated Prüfer/oscillation counting (machine-checkable eigenvalue counts) plus interval eigenvalue bounds.
   Upper bounds on $L^{(N)}$ ratios are rigorous by construction.
5. **Lean 4 (P5).** Begin from mathlib's `Mathlib.Analysis.InnerProductSpace.Spectrum` and current unbounded-operator files; formalize Birman–Schwinger in the compact-resolvent setting first.
   Failure mode: formalization scope explosion - timebox and report the exact frontier reached.

## 6. Verification and auditability requirements

Instantiating the five template requirements for this problem:

1. **Exact arithmetic.** All constants ($L^{\mathrm{cl}}$ values, FHJN objective, ODE enclosures) in Arb interval arithmetic with directed rounding or exact rationals/algebraics; floating point only in the exploration phase of P3/P4 and never cited in a claim.
2. **Independent verification.** For each certified constant: a standalone checker ($\le$ 200 lines, reads the parameter point and re-evaluates the enclosure) written independently of the search code; dual implementations (python-flint and C/Arb) for the P1 and P3 final evaluations.
3. **Reproducibility.** Every claim ships with: exact parameter values (rationals), Arb precision settings, library versions, and a SHA-256 manifest over all scripts, certificates, and Lean sources.
4. **Preservation.** The exploration code (float optimizers, failed proof-family parameterizations) is part of the record - negative results about exhausted proof families are findings and must be preserved, not discarded.
5. **Honest reporting.** The final report opens with a single sentence stating whether the sharp constant $L_{1,d}$ was determined (expected answer: no) and lists exactly which of P1–P6 were achieved, with the certified numerical ratio frontier stated to its enclosure width.
   Any bound valid only for a restricted potential class must carry the restriction in its headline statement.
