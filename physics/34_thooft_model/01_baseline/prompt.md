# PROMPT FOR A CLOSED-FORM MESON SPECTRUM OF THE 'T HOOFT MODEL

## Exact solution of the 't Hooft integral equation for 2D large-N QCD

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 34 of 50 (Tier 3)
**Source:** top-50 list #46, category G (QFT and mathematical particle theory)
**Modes:** `[sym]` `[proof]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Two-dimensional $SU(N)$ gauge theory with fundamental quarks becomes exactly summable in the 't Hooft limit $N \to \infty$, $\lambda = g^2 N$ fixed: the meson spectrum is the eigenvalue set of a single one-dimensional singular integral equation. Fifty years on, no closed-form solution is known for any quark mass, despite exquisitely developed asymptotics ($\mu_n^2 \sim \pi^2 n$), exact results in limits, and strong recent analytic structure - the Fateev–Lukyanov–Zamolodchikov integral-equation analysis (~2009) and the Ambrosino–Komatsu TQ/Baxter-type reformulation (2023–2024). The problem is matched to current AI methods because the ground truth is machine-generatable to arbitrary precision: certified eigenvalue enclosures, independent verification of the TQ predictions, and PSLQ mining are all concrete, auditable computations, and rigorous spectral theorems about the 't Hooft operator are genuinely provable. The complete resolution defined in section 2 - a proven exact quantization condition - is the target and is frankly unlikely in one session; the graded targets of section 3 are the realistic product, and anything short of section 2 must be reported as partial.

## 1. Exact problem statement

### 1.1 The 't Hooft equation

Fix the 't Hooft limit of 2D $SU(N)$ Yang–Mills with two fundamental Dirac quarks of bare masses $m_1, m_2$, coupling $g$, $\lambda = g^2 N$ fixed. In light-cone gauge the meson light-cone wavefunction $\varphi$ on $x \in (0,1)$ (momentum fraction of quark 1) satisfies the 't Hooft equation

\[
\mu^2\, \varphi(x) \;=\; \left( \frac{\alpha_1}{x} + \frac{\alpha_2}{1-x} \right) \varphi(x)
\;-\; \Xint-_0^1 \frac{\varphi(y)}{(x-y)^2}\, dy ,
\]

with the following normalizations, fixed once and for all:

- $\mu^2$ is the meson mass squared in units of $\lambda/\pi = g^2 N/\pi$;
- $\alpha_i = \pi m_i^2/\lambda - 1$ (the $-1$ is the self-energy shift; $\alpha_i \ge -1$ for real masses);
- $\Xint-$ is the Hadamard finite part (principal value of the double pole).

Define the operator $H$ by the right-hand side. On its form domain in $L^2(0,1)$, $H$ is symmetric and non-negative for $\alpha_i \ge -1$, by the standard quadratic-form identity

\[
\langle \varphi, H\varphi\rangle
= \int_0^1 \left( \frac{\alpha_1}{x} + \frac{\alpha_2}{1-x} \right) |\varphi(x)|^2 dx
+ \frac12 \Xint-_0^1\!\!\Xint-_0^1 \frac{|\varphi(x)-\varphi(y)|^2}{(x-y)^2}\, dx\, dy .
\]

Eigenfunctions vanish at the endpoints as $\varphi \sim x^{\beta_1}$, $\varphi \sim (1-x)^{\beta_2}$, where $\beta_i \in [0,1)$ solves

\[
\pi \beta_i \cot(\pi \beta_i) \;=\; -\alpha_i .
\]

The spectrum is discrete, $0 \le \mu_0^2 < \mu_1^2 < \cdots \to \infty$ (simplicity is expected; its proof status must be audited - see P5), with 't Hooft's asymptotics

\[
\mu_n^2 \;=\; \pi^2 n \;+\; (\alpha_1 + \alpha_2)\ln n \;+\; C(\alpha_1,\alpha_2) \;+\; o(1),
\]

refined by FLZ with explicit constants and oscillatory corrections (verify the exact form). Exact anchor: for $m_1 = m_2 = 0$ (i.e. $\alpha_i = -1$), $\varphi_0 \equiv 1$, $\mu_0^2 = 0$ is an exact eigenpair (the massless "pion").

### 1.2 The open problem

**Determine the spectrum $\{\mu_n^2(\alpha_1, \alpha_2)\}_{n \ge 0}$ in closed form**: produce an explicit function $F$ (built from identified special functions) and prove that the eigenvalues are exactly the solutions of the quantization condition

\[
F(\mu^2; \alpha_1, \alpha_2) \;=\; 0,
\]

for all $\alpha_i \ge -1$. The object of study is the integral equation of section 1.1 itself; the field-theoretic derivation (light-cone quantization, gauge equivalence - Callan–Coote–Gross 1976) is context, not part of the problem. "The model is integrable" or "a TQ equation exists" are not acceptable targets unless accompanied by proofs at the standard of section 2.

## 2. Complete-resolution standard

Complete resolution requires all of:

1. An explicit quantization condition $F(\mu^2; \alpha_1, \alpha_2) = 0$, with $F$ given in closed form (finitely many known special functions; integral representations with explicit kernels admitted), valid for all $\alpha_1, \alpha_2 \ge -1$.
2. A rigorous proof that the solution set of $F = 0$ is exactly the spectrum of $H$ - both directions: completeness and no spurious roots - with $H$ given a precise self-adjoint realization.
3. Consistency proofs against all known exact data: the chiral eigenpair, the 't Hooft/FLZ asymptotics, the heavy-quark asymptotics - derived from $F$, not assumed.
4. Certified numerical confirmation: eigenvalues from $F$ and from the direct spectral problem agree within certified enclosures (section 6 standards).

**Not accepted as resolution:**

- Numerical spectra to any precision, including certified enclosures (these are P1, not the solution).
- Asymptotic expansions (large $n$, chiral, heavy-quark, or in any coupling), however many orders, without exact resummation and proof.
- A TQ/Baxter or Bethe-type equation verified only numerically, or derived formally without operator-level proof.
- PSLQ identifications of individual eigenvalues, however convincing.
- Claims that import integrability or exact solvability from adjacent models without proof for this equation.
- Closed forms valid only at isolated parameter points, presented as the general solution (they are excellent partial results - P4/P6).

## 3. Graded partial-result targets

### P1 - Certified spectrum (frontier reproduction, rigorized)

- Validated eigenvalue enclosures for $\mu_n^2$, $n \le 30$, at benchmarks $(\alpha_1,\alpha_2) \in \{(0,0),\ (-1,-1),\ (\alpha,\alpha) \text{ with heavy } \alpha = 10^3\}$.
- Method: Galerkin discretization in a basis carrying the correct endpoint exponents $\beta_i$; matrix elements enclosed in Arb balls; a posteriori bounds via Kato–Temple / Lehmann–Goerisch, with spectral-gap input bootstrapped from coarse enclosures.
- Precision target: $\ge 50$ certified digits for $n \le 5$ at $(0,0)$.
- Published spectra are floating-point; certified enclosures are already beyond the literature.
- *Certificate:* interval tables plus two independent discretizations (Galerkin vs collocation) with overlapping balls.

### P2 - TQ-equation verification

- Audit the Ambrosino–Komatsu TQ/Baxter reformulation first: exact statement, derivation status, domain of validity (verify).
- Implement it independently from their papers; compare its spectral predictions against P1 enclosures digit-by-digit.
- Document agreement, disagreement, and any reformulation ambiguities.
- *Certificate:* side-by-side tables, independent code, discrepancy log.

### P3 - Limit theorems with proofs

- Chiral limit: prove the leading Gell-Mann–Oakes–Renner-type law $\mu_0^2 = 2 m \sqrt{\pi\lambda/3} + O(m^2)$ (verify the constant against the literature before proving; the proof is rigorous perturbation theory around the exact chiral eigenpair, using relative form-boundedness of the perturbation).
- Heavy-quark limit: prove Airy-type asymptotics for low-lying $\mu_n$ with explicit error bounds (rigorous WKB, Olver-style).
- *Certificate:* theorems, with machine-checked inequality steps where intervals are used.

### P4 - PSLQ mining at distinguished points

- At $(\alpha_1,\alpha_2) = (0,0)$ (the analytically cleanest point, central in FLZ): run PSLQ on $\ge 50$-digit enclosures of low eigenvalues against bases $\{1, \pi, \pi^2, \ln 2, \zeta(3), \text{FLZ constants}\}$ and low-degree products.
- Positive hits reported only with doubled-precision confirmation and decoy-basis controls.
- Certified negatives (exclusion of small-height relations up to stated norm bounds) are the expected, still-valuable outcome.
- *Certificate:* full PSLQ logs, precisions, and norm bounds.

### P5 - Spectral-theory theorems

- Rigorous foundations: self-adjoint realization (Friedrichs extension) of $H$; compact resolvent and discreteness; eigenvalue simplicity; monotonicity and analyticity of $\mu_n^2$ in $\alpha_i$.
- Audit first which of these are already in the literature (a clean published functional-analytic treatment is scarce - verify); prove the gaps.
- *Certificate:* theorems; optionally a Lean 4 formalization of the quadratic-form positivity identity.

### P6 - Proven quantization condition in a regime

- Strongest short of resolution: an exact quantization condition proved on a sub-family - e.g. the asymptotic condition proved to all orders in $1/n$ as a theorem with error bounds, or an exact condition at an isolated $\alpha$ point - cleanly scoped.
- *Certificate:* theorem plus certified numerical cross-check.

### P7 - The windfall

- The full section-2 resolution.

## 4. Known results and prior art

- 't Hooft 1974 ("A two-dimensional model for mesons"), following the planar limit ('t Hooft 1973): the equation, endpoint analysis, linear asymptotics, first numerics.
- Callan–Coote–Gross 1976: covariant-gauge treatment, consistency of the spectrum (context for gauge-independence).
- Brower–Spence–Weis ~1978–1979: spectral and structural studies (verify).
- Zhitnitsky ~1985: chiral-limit relations in 2D QCD (verify the constant used in P3).
- DLCQ and basis numerics: Hornbostel–Brodsky–Pauli ~1988–1990 and successors (verify); standard non-rigorous spectra used as cross-checks.
- Fateev–Lukyanov–Zamolodchikov ~2009: analytic integral-equation machinery for the spectral problem, exact spectral sums, refined asymptotics, conjectured quantization structure (verify exact claims and which are proven).
- Ambrosino–Komatsu 2023–2024: TQ/Baxter-type reformulation of the 't Hooft equation with systematic expansions and high-precision agreement; follow-up generalizations (verify the precise theorems claimed versus physics-level derivations).
- Adjacent modern numerics: lightcone conformal truncation (Fitzpatrick–Katz and collaborators, ~2016–2022, verify) and 2D gauge-model studies (Dempsey–Klebanov–Pufu and collaborators, ~2021–2024, adjacent models) - useful methodology, not results on this exact equation.

Status as of mid-2026 - re-verify against current literature before starting the session.

## 5. Attack plan

1. **Basis construction.**
   - Compute $\beta_i$ from $\pi\beta\cot(\pi\beta) = -\alpha$ as certified Arb roots.
   - Build the 't Hooft basis $\{x^{\beta_1}(1-x)^{\beta_2} P_k(x)\}$ with Jacobi-type $P_k$; assemble the finite-part kernel's matrix elements semi-analytically where hypergeometric closed forms exist, else by rigorous quadrature (python-flint `acb_calc` with explicit endpoint-singularity treatment).
   - $N_{\text{basis}} \approx 200$–$400$ at 100–200 digits fits a single workstation.
2. **Mandatory discretization test.** The exact chiral eigenpair $(\varphi \equiv 1,\ \mu^2 = 0)$ at $\alpha_i = -1$ must be reproduced to full precision; any finite-part discretization error shows up here first.
3. **Certification.**
   - Interval Rayleigh quotients give upper enclosures; Kato–Temple/Lehmann bounds give two-sided enclosures using gap estimates bootstrapped from a coarse certified run.
   - Cross-validate Galerkin against Chebyshev collocation (float, exploratory) and against published spectra.
4. **TQ pipeline.** Independent mpmath implementation of the Ambrosino–Komatsu equations; certified root-finding (Arb) where the equations permit; a written log of exactly which steps of the reformulation are non-rigorous.
5. **Mining.** mpmath PSLQ at twice working precision with decoy-vector controls; inverse-symbolic lookups; every hit re-tested at doubled precision.
6. **Proof work.** The quadratic-form identity of section 1.1 is the foundation for P5; rigorous perturbation theory around the chiral eigenpair for P3(i); rigorous WKB for P3(ii).

Expected failure modes: mismatched endpoint exponents in the basis (algebraic, not spectral, convergence - symptom: eigenvalue drift with $N_{\text{basis}}$); mis-discretized finite part (caught by the chiral test); Kato–Temple failing without gap lower bounds (bootstrap, or fall back to Lehmann–Goerisch); PSLQ false positives from insufficient precision; over-claiming simplicity or completeness of the numerically observed spectrum without proof.

## 6. Verification and auditability requirements

1. **Exact arithmetic.** All certified enclosures in Arb ball arithmetic with directed rounding; matrix elements enclosed, never merely evaluated; floating-point runs labeled exploratory.
2. **Independent verification.** Two independent discretizations (different basis, different code) must yield overlapping enclosures before any digit is reported; a standalone checker re-verifies the Kato–Temple arithmetic from the stored matrices; the TQ implementation shares no code with the spectral solver.
3. **Reproducibility.** Pinned FLINT/Arb, python-flint, mpmath versions; all basis sizes, precisions, and bootstrap sequences recorded; SHA-256 manifest over matrices, enclosure tables, and PSLQ logs.
4. **Preservation.** All code, including failed discretizations and negative PSLQ runs, preserved and indexed; omissions declared.
5. **Honest reporting.** The report opens by stating whether the section-2 standard was met (expected: no); every eigenvalue is labeled (certified enclosure) or (floating point); TQ-derived numbers are labeled by the rigor status of the TQ derivation itself; no numerical identification is reported as a closed form.
