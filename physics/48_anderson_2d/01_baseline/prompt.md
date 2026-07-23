# PROMPT FOR TWO-DIMENSIONAL ANDERSON LOCALIZATION AT WEAK DISORDER

## Complete localization in $d = 2$ for arbitrarily small disorder: the scaling-theory gap

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 48 of 50 (Tier 4)
**Source:** top-50 list #13, category B (rigorous many-body and condensed matter)
**Modes:** `[proof]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The single-parameter scaling theory of Abrahams–Anderson–Licciardello–Ramakrishnan (1979) predicts that in two dimensions all eigenstates of the Anderson model localize at any nonzero disorder strength. Rigorously, localization is proved only at large disorder or at extreme energies (Fröhlich–Spencer multiscale analysis 1983; Aizenman–Molchanov fractional moments 1993), and nothing is known at small disorder in the band bulk - the outstanding gap between physical consensus and theorem in random operator theory. This is a Tier 4, opportunistic-only prompt: no credible path to the full statement exists, and the session's value lies in certified reproductions and quantitative pushes. The match to current methods is the finite-volume structure of the theory: the Aizenman–Schenker–Friedrich–Hundertmark finite-volume fractional-moment criteria reduce localization in an energy window to a strict inequality about a finite-box quantity - a disorder expectation of a fractional power of a Green function - certifiable by interval arithmetic plus certified quadrature. Pushing the certified disorder threshold down, and certifying quasi-1D Lyapunov bounds on strips, produces machine-checked ground truth where the field currently has folklore. The complete resolution defined in section 2 is the target, and anything less must be reported as a partial result, never represented as a solution.

## 1. Exact problem statement

On $\ell^2(\mathbb{Z}^2)$ define the Anderson Hamiltonian

\[
(H_\omega \psi)(x) \;=\; \sum_{|y - x|_1 = 1} \psi(y) \;+\; \lambda\, \omega_x\, \psi(x),
\]

with $\{\omega_x\}_{x \in \mathbb{Z}^2}$ i.i.d. with common distribution $\mu$; the reference choice is $\mu = \mathrm{Unif}[-1, 1]$ (fix $\mu$ in every artifact; other bounded densities are variants, Bernoulli $\mu$ is a different and much harder problem). Disorder strength $\lambda > 0$. The almost-sure spectrum is $\Sigma = [-4, 4] + \lambda\,\mathrm{supp}\,\mu$.

Localization notions - fix precisely; they are not interchangeable:

- **Spectral localization in an interval $I$:** almost surely, $H_\omega$ has pure point spectrum in $I$ with exponentially decaying eigenfunctions.
- **Dynamical localization in $I$:** $\displaystyle \mathbb{E}\Big[\sup_{t \in \mathbb{R}} \big|\langle \delta_x |\, e^{-itH_\omega} P_I(H_\omega)\, |\delta_y\rangle\big|\Big] \le C\, e^{-|x-y|/\xi}$.
- **Fractional-moment condition in $I$:** for some $s \in (0, 1)$ and $C, \xi > 0$,

\[
\mathbb{E}\big[\, |G_\omega(x, y;\, E + i\epsilon)|^s \,\big] \;\le\; C\, e^{-|x-y|/\xi}
\quad \text{uniformly for } E \in I,\ \epsilon > 0,
\]

where $G_\omega(z) = (H_\omega - z)^{-1}$. For regular $\mu$ this implies the other two (Aizenman et al.).

**Target theorem (2D complete localization).** For every $\lambda > 0$: almost surely $H_\omega$ has pure point spectrum on all of $\mathbb{R}$ with exponentially decaying eigenfunctions, and dynamical localization holds on every compact interval. The decisive case is small $\lambda$ at band-bulk energies (e.g. $E = 0$); large $\lambda$ and spectral edges are known.

Quasi-1D restriction used by the graded targets: the strip $\mathbb{Z} \times \{1, \dots, M\}$ with the same Hamiltonian. Writing $\psi_n \in \mathbb{C}^M$ for the wavefunction on column $n$ and $V_n$ for the diagonal disorder of column $n$ plus the intra-column hopping matrix, the transfer matrices

\[
T_n(E) \;=\; \begin{pmatrix} E\,\mathbb{1}_M - \lambda V_n - A_M & -\mathbb{1}_M \\ \mathbb{1}_M & 0 \end{pmatrix} \in \mathrm{Sp}(2M, \mathbb{R})
\]

(with $A_M$ the width-$M$ discrete Laplacian; fix boundary conditions across the strip) propagate $(\psi_{n+1}, \psi_n)$. Lyapunov exponents $\gamma_1 \ge \dots \ge \gamma_M \ge 0$ of the random product exist by Oseledets; strip localization is governed by positivity of the smallest exponent $\gamma_M$ (Goldsheid–Margulis; Klein–Lacroix–Speis). The 2D question is the $M \to \infty$ limit with quantitative control of $\gamma_M(M, \lambda, E)$ - the precise mathematical form of the scaling-theory gap.

Conventions to fix and hold: the lattice Laplacian is the pure hopping sum above (no diagonal $4$ shift - state if shifted); $\lambda$ multiplies $\omega_x$ with $\omega_x \sim \mathrm{Unif}[-1,1]$, so published thresholds with other conventions (density on $[0,1]$, hopping $1/2$, shifted Laplacian) must be converted before any comparison - conversion errors are a known source of fake "improvements".

Two a priori facts anchor all certified work (both to be re-proved in-session): the Aizenman–Molchanov a priori bound

\[
\mathbb{E}\big[\, |G_\omega(x, x;\, E + i\epsilon)|^s \,\big] \;\le\; \frac{C_s}{\lambda^s}
\qquad (0 < s < 1),
\]

with $C_s$ explicit for $\mathrm{Unif}[-1,1]$ (certify it tightly - the generic constant is wasteful), and the deterministic bound $\|G(z)\| \le 1/\mathrm{dist}(z, \sigma(H_\omega))$ for off-spectrum control.

## 2. Complete-resolution standard

A complete resolution is a proof of the Target theorem - complete localization for all $\lambda > 0$ for the stated model - or a disproof: a proof that some spectral region carries absolutely continuous or otherwise delocalized spectrum at small $\lambda$, overturning scaling theory; either counts. All analytic steps fully proved; all computational inputs (finite-volume criteria, quadrature over disorder) certified with independent checkers.

**Not accepted as resolution:**

- Large-$\lambda$ or band-edge localization proofs (known since 1983/1993), however polished, presented as bearing on the weak-disorder bulk.
- Numerical transfer-matrix or finite-size-scaling studies (MacKinnon–Kramer tradition), at any lattice size, including data collapses.
- Field-theoretic derivations (nonlinear sigma model, SUSY) without rigorous control.
- Localization for modified models - special chiral/symplectic symmetry classes, quasi-periodic potentials, Landau-level projections, trees or expanders - passed off as the orthogonal-class 2D Anderson model above.
- Strip results at fixed finite $M$ presented as 2D statements (they are P-targets, not the theorem).
- Certified finite-volume criteria verified at specific $(\lambda, E)$ described as more than exactly that.
- Threshold "improvements" that are artifacts of convention conversion between papers (see the normalization ledger in section 1) rather than genuine gains.

## 3. Graded partial-result targets

Ordered from most accessible to strongest short of resolution; each is independently valuable and certifiable. Expected Tier 4 session product: P1–P2 complete, P3 partial, P4 stated.

**P1 - Certified finite-volume fractional-moment criterion, reproduced from scratch.**
- Task: re-derive the ASFH (Aizenman–Schenker–Friedrich–Hundertmark 2001) finite-volume criterion for the 2D model with all constants explicit: an inequality "if the finite-box quantity $B_L(\lambda, E, s)$ - a specified disorder expectation of fractional Green-function moments on an $L$-box with specified boundary decorations - satisfies $B_L < b^*$, then the fractional-moment condition, hence spectral and dynamical localization, holds in a neighborhood of $E$". Then certify $B_L < b^*$ at large $\lambda$: exact rational resolvent solves per disorder sample (FLINT) or interval LU with directed rounding; certified quadrature over the disorder variables using the criterion's own factorization structure.
- Certificate: the re-derivation document with explicit constants; the certified inequality with dual-implementation checkers; expect $L \le 4$ at first.
- Value: a certified statement "for $\lambda \ge \lambda_0^{\mathrm{cert}}$, localization holds near $E_0$" under our own toolchain, with $\lambda_0^{\mathrm{cert}}$ compared honestly to published thresholds - the verified frontier reproduction.

**P2 - Pushing the certified threshold down.**
- Task: optimize P1 along every axis: the fractional exponent $s$; box size $L$ (criterion strength grows with $L$, certification cost grows fast - quantify the curve); distribution-specific decoupling constants for $\mathrm{Unif}[-1,1]$ certified tightly with Arb instead of generic bounds; energy dependence (band center vs. edge).
- Stretch: compare against the Germinet–Klein bootstrap-MSA finite-volume condition on the same boxes - whichever criterion certifies a lower $\lambda_0$ becomes the program's workhorse; the comparison itself is a finding.
- Certificate: the certified phase-boundary table $\lambda_0^{\mathrm{cert}}(E, L)$ with full manifests; extrapolations labeled non-rigorous.
- Value: every strict certified improvement over the published localization region is a standalone result; the saturation curve documents exactly where the fractional-moment method dies.

**P3 - Certified strip Lyapunov bounds.**
- Task: for strips of width $M = 1, 2, 3, \dots$: certified lower bounds $\gamma_M(\lambda, E) \ge g_M > 0$ via computer-assisted invariant-cone / projective-contraction arguments - interval arithmetic on the symplectic cocycle, certified contraction of a Birkhoff-type metric on the Lagrangian Grassmannian, worst-case over the compactly supported disorder where possible and measure-quantified where not (adapting the rigorous-Lyapunov tradition of Pollicott-style algorithms and Jurga–Morris-type certified estimates).
- Certificate: per-$(M, \lambda, E)$ certificates with an independent cone-condition verifier; benchmark points must include weak $\lambda$.
- Value: machine-checked ground truth for the quasi-1D route; to our knowledge never done with certificates (verify); expect $M \le 8$–$16$.

**P4 - The scaling-gap theorem.**
- Task: turn the folklore "the obstruction is uniformity in $M$" into precise mathematics: prove the sharpest available conditional theorem "if $\gamma_M(\lambda, E) \ge f(M)$ for all $M$, with an explicit condition on $f$ (the expected truth is $\gamma_M \sim e^{-cM}$ at weak disorder - reconcile with the band-matrix literature), then 2D localization holds at $(\lambda, E)$" - or prove that no such implication is available by known routes, identifying exactly what supplementary input (e.g. a finite-volume criterion seeded by strip data) closes the loop.
- Certificate: theorem-grade statement of the gap with the win-condition inequality explicit.
- Value: the citable formulation of why the problem is hard; the map for every future session.

**P5 - Weak-disorder asymptotics of certified quantities.**
- Task: certified two-sided bounds on $\gamma_M(\lambda, E)$ or $B_L(\lambda, E, s)$ as functions of small $\lambda$ at fixed small $M, L$: certified validation of the perturbative $\gamma_1 \sim c\,\lambda^2$ law at $M = 1$ (Figotin–Pastur-type formulas), including the band-center anomaly at $E = 0$ - a known trap; certify it correctly rather than around it.
- Certificate: interval enclosures of the certified quantities across a $\lambda$-grid with proofs of monotone interpolation where claimed.
- Value: rigorous anchor points for the scaling picture; a stress test of whether certified methods can enter the weak-disorder regime at all. Expected to be the hardest certification; partial $\lambda$-ranges acceptable.

**P6 - Conditional 2D statements from certified seeds.**
- Task: strongest short of resolution - a proved theorem "certified finite computation $X$ (explicit box or strip quantity at explicit $(\lambda, E)$, feasible or near-feasible) implies localization at $(\lambda, E)$" with $\lambda$ strictly below all published thresholds, plus the certified computation itself if within reach.
- Certificate: the theorem plus, if achieved, the full certificate chain.
- Value: any unconditional certified extension of the known localization region, however small, is the flagship outcome available to this prompt.

## 4. Known results and prior art

- Abrahams–Anderson–Licciardello–Ramakrishnan (1979): scaling theory; the $\beta$-function argument for complete 2D localization. Not rigorous; the target's origin.
- Fröhlich–Spencer (1983): multiscale analysis; localization at large disorder or extreme energies.
- Fröhlich–Martinelli–Scoppola–Spencer (1985): completion of the multiscale route to pure point spectrum with exponentially decaying eigenfunctions.
- von Dreifus–Klein (1989): the streamlined multiscale scheme most later work builds on.
- Aizenman–Molchanov (1993): fractional-moment method; simpler proofs, dynamical localization, explicit large-$\lambda$ thresholds.
- Aizenman–Schenker–Friedrich–Hundertmark (2001): finite-volume fractional-moment criteria - the machine-checkable reduction this prompt is built on (verify exact constants and boundary decorations).
- Germinet–Klein (2001+): bootstrap multiscale analysis - the alternative finite-volume pipeline; compare which criterion certifies better in practice.
- Kunz–Souillard (1980); Carmona–Klein–Martinelli (1987): complete localization in $d = 1$, including singular distributions.
- Goldsheid–Margulis (1989): Furstenberg-type positivity of all Lyapunov exponents for symplectic random products.
- Klein–Lacroix–Speis (c. 1990): localization on strips of arbitrary fixed width (verify hypotheses on $\mu$).
- Furstenberg (1963); Bougerol–Lacroix (1985 book): the random-matrix-product foundations behind every strip statement.
- Ding–Smart (c. 2019, Inventiones): 2D Anderson–Bernoulli localization near the spectral edge via quantitative unique continuation; Li–Zhang (c. 2022): 3D analogues (verify) - different disorder class and edge-only, but the modern techniques to know.
- Random band matrices / quasi-1D (Schenker; subsequent width-scaling improvements - verify the current record): the strongest counter-pressure on naive uniformity hopes in $M$; any P4 statement must be consistent with this literature.
- Bourgain (2000s): weak-disorder results on $\mathbb{Z}^2$ for related quantities (density of states, localization-length bounds - verify carefully what exists and for which models).
- Simon–Wolff (1986): spectral-averaging criterion - an alternative route from Green-function bounds to point spectrum; useful for the P1 write-up.
- Wegner (1981): density-of-states bound - enters every finite-volume criterion; certify its constant for $\mathrm{Unif}[-1,1]$.
- Numerics: MacKinnon–Kramer (1981+); Slevin–Ohtsuki high-precision scaling - non-rigorous calibration only.
- Reviews: Aizenman–Warzel, *Random Operators* (2015) - the canonical modern source for the fractional-moment formalism; use its statements as the baseline to re-derive against.

Status as of mid-2026 - re-verify against current literature before starting the session.

## 5. Attack plan

Mode `[proof]`, with heavy certified computation in service of proofs. Single-workstation first computations.

1. **Green-function certification core (C++/Julia).** For an $L \times L$ box, rational disorder sample $\omega$, rational $E$: compute $G(x, y; E)$ exactly over $\mathbb{Q}$ (FLINT sparse rational solves; feasible to $L \approx 12$) or in Arb interval arithmetic for larger $L$. Checker: independent re-solve with a different elimination order plus exact residual verification.
2. **Disorder integration.** The ASFH quantity is an expectation over $L^2$ i.i.d. variables; direct certified cubature is exponential and must not be attempted. Re-derive, before coding, which integrals the criterion actually needs - the fractional-moment decoupling structure reduces the requirement to low-dimensional conditional integrals over single-site variables. Certify the $\mathrm{Unif}[-1,1]$ decoupling constant tightly with Arb. Expected failure mode: misreading which quantity the criterion needs; the paper half of P1 gates the code half.
3. **Strip cocycles (P3).** Interval transfer matrices in $\mathrm{Sp}(2M, \mathbb{R})$; certified cone-field contraction on the Lagrangian Grassmannian; rigorous $\gamma_M$ lower bounds from certified contraction ratios accumulated over verified windows, uniform over the compact disorder support where the cone survives. Expected failure mode: cone arguments fail at weak disorder where rotation dominates contraction - map the failure boundary precisely; it feeds P4 and P5 as data, not as an excuse.
4. **Comparison ledger.** A table of certified thresholds versus every published explicit constant (AM 1993 and successors) - establishing the certified state of the art is itself a deliverable, and the literature's explicit thresholds are scattered and convention-dependent (lattice normalization of $-\Delta$, definition of $\lambda$): normalize all of them once, in writing.
5. **Tier 4 discipline.** No multiscale-analysis reimplementation marathon; no new delocalization theory; opportunistic certified gains only. Timebox the P3 cone experiments - if $M = 4$ certification fails at moderate $\lambda$, report the failure mode and stop that line.
6. **Calibration firewall.** Floating-point transfer-matrix runs (MacKinnon–Kramer style) may be used to choose parameters worth certifying; they never appear in any claim.
7. **Expected failure modes, global.** (a) The certified quadrature constants at $L = 3, 4$ produce a $\lambda_0^{\mathrm{cert}}$ *worse* than the analytic AM bound - possible, and reportable as a finding about criterion sharpness, not hidden. (b) Interval blowup in long transfer products - mitigate with periodic QR-type interval renormalization of the frame, each step verified. (c) The $E = 0$ band-center anomaly contaminating $M = 1$ validation - use off-center $E$ for validation first, then treat $E = 0$ as its own certified case.
8. **Honest calibration.** Nothing in this plan approaches the $\lambda \to 0$ conjecture; the plan's ceiling is a strictly larger certified localization region and a theorem-grade statement of the gap. A session delivering P1 + P2 + the P4 statement has met the bar.

## 6. Verification and auditability requirements

1. **Exact arithmetic.** Rational Green-function solves where feasible; Arb directed-rounding intervals otherwise; all quadrature with certified remainders; every criterion inequality evaluated as a directed interval comparison. Floating point only for exploration, clearly firewalled.
2. **Independent verification.** Dual Green-function implementations (rational vs. interval, different elimination orders); a standalone checker re-verifying each final inequality chain from stored enclosures; strip certificates re-checked by an independent cone-condition verifier (Python).
3. **Reproducibility.** Disorder distribution, $s$, box size, boundary decorations, precision, exploratory seeds, and library versions recorded; SHA-256 manifest over all certificates, samples, and ledgers.
4. **Preservation.** The ASFH re-derivation notes (constants differ across the literature; our re-derivation becomes the reference), failed cone constructions, and the threshold-vs-$L$ ledger preserved; anything unpreserved declared explicitly rather than obscured.
5. **Honest reporting.** The report opens by stating that 2D weak-disorder localization was not proved (barring a shock in either direction), then gives: the certified localization region achieved as explicit $(\lambda, E)$ sets; its comparison to published thresholds; the certified strip table; and the P4 statement of the remaining gap. Finite-parameter certifications are never described as progress on the $\lambda \to 0$ conjecture beyond exactly what they are.
