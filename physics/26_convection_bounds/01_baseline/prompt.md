# PROMPT FOR CLOSING THE RIGOROUS NUSSELT–RAYLEIGH SCALING GAP

## Certified variational bounds on turbulent heat transport in Rayleigh–Bénard convection

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 26 of 50 (Tier 3)
**Source:** top-50 list #40, category F (fluids, plasmas, continuum)
**Modes:** `[bound]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The best rigorous a priori bound on the Nusselt number for three-dimensional, finite-Prandtl-number, no-slip Rayleigh–Bénard convection scales as $\mathrm{Nu}\lesssim \mathrm{Ra}^{1/2}$, while classical Malkus phenomenology and most experiments and simulations are compatible with $\mathrm{Ra}^{1/3}$-type scaling. Closing, narrowing, or rigorously explaining this exponent gap is the sharpest open question in mathematically rigorous turbulence bounds. The problem is exceptionally well matched to current AI-assisted methods because the dominant proof technology - the Doering–Constantin background method and its auxiliary-functional generalizations - is literally an infinite-dimensional convex feasibility problem (a quadratic-form nonnegativity constraint parameterized by a background profile), so both the optimization and its certification reduce to semidefinite programming with interval-arithmetic verification. The complete resolution defined in section 2 (determination of the optimal a priori exponent) is the target; anything less, including every certified prefactor or variant-geometry result produced along the way, must be reported as a partial result under section 3 and never represented as a solution.

## 1. Exact problem statement

### 1.1 Equations, domain, boundary conditions

Work in the nondimensional Boussinesq system on
\[
\Omega=[0,\Gamma_1]\times[0,\Gamma_2]\times[0,1],
\]
periodic in the horizontal variables $x,y$ with fixed aspect ratios $\Gamma_1,\Gamma_2>0$. Unknowns: velocity $u=(u_1,u_2,w):\Omega\times[0,\infty)\to\mathbb R^3$, temperature $T$, pressure $p$. With Prandtl number $\Pr\in(0,\infty)$ and Rayleigh number $\mathrm{Ra}>0$, on the thermal-diffusion time scale:
\[
\partial_t u+u\cdot\nabla u+\nabla p=\Pr\,\Delta u+\Pr\,\mathrm{Ra}\,T\,e_3,
\]
\[
\nabla\cdot u=0,
\qquad
\partial_t T+u\cdot\nabla T=\Delta T .
\]
Boundary conditions (the **primary configuration**):

- no-slip: $u=0$ at $z\in\{0,1\}$;
- fixed temperatures: $T(\cdot,z{=}0)=1$, $T(\cdot,z{=}1)=0$.

Variant configurations must always be labeled explicitly:

- free-slip: $w=\partial_z u_1=\partial_z u_2=0$ at the plates;
- Navier-slip with slip length $\ell$;
- fixed-flux thermal boundary conditions;
- infinite Prandtl number, where the momentum equation degenerates to the Stokes balance $\nabla p=\Delta u+\mathrm{Ra}\,T e_3$.

### 1.2 Solution class and Nusselt number

Fix the solution class $\mathcal S(\mathrm{Ra},\Pr,\Gamma)$: Leray–Hopf-type weak solutions with $T_0\in L^\infty$, $u_0\in L^2_{\mathrm{div}}$, satisfying the standard energy inequalities and the maximum principle $0\le T\le 1$ after transients. Any bound proved under additional regularity hypotheses must declare them. For a solution, define
\[
\mathrm{Nu}:=1+\limsup_{t\to\infty}\frac1t\int_0^t\frac{1}{|\Omega|}\int_\Omega w\,T\,dx\,dt'
\;=\;\limsup_{t\to\infty}\frac1t\int_0^t\frac{1}{|\Omega|}\int_\Omega|\nabla T|^2\,dx\,dt' .
\]
The equality of the two limsup expressions must itself be handled with care in the weak class; state which quantity is bounded. The worst-case transport and the bound exponent are
\[
\overline N(\mathrm{Ra};\Pr,\Gamma):=\sup_{\text{solutions in }\mathcal S}\mathrm{Nu},
\qquad
\beta_*(\Pr):=\limsup_{\mathrm{Ra}\to\infty}\ \sup_{\Gamma}\ \frac{\ln \overline N(\mathrm{Ra};\Pr,\Gamma)}{\ln \mathrm{Ra}} .
\]

### 1.3 The background method as a variational problem

Decompose $T=\tau(z)+\theta$ with $\tau\in H^1(0,1)$, $\tau(0)=1$, $\tau(1)=0$. Averaging the $\theta$-equation against $\theta$ and the momentum equation against $u$ yields the two balances
\[
\langle|\nabla\theta|^2\rangle+\langle \tau'\, w\,\theta\rangle+\langle \tau'\,\partial_z\theta\rangle=0,
\qquad
\langle|\nabla u|^2\rangle=\mathrm{Ra}\,\langle w\,\theta\rangle ,
\]
where $\langle\cdot\rangle$ is the space–time average (horizontal means of $w$ vanish by incompressibility and the boundary conditions). Combining, for any balance parameter $a>0$:
\[
\mathrm{Nu}\;\le\;\int_0^1 \tau'(z)^2\,dz
\quad\text{provided the \emph{spectral constraint} holds:}
\]
\[
\mathcal Q_{\tau,a}(v,\theta):=\frac{a}{\mathrm{Ra}}\int_\Omega|\nabla v|^2
+\int_\Omega|\nabla\theta|^2
+\int_\Omega\bigl(2\tau'(z)-a\bigr)\,v_3\,\theta\;\ge 0
\]
for all horizontally periodic $v\in H^1_{\mathrm{div}}$ and $\theta\in H^1_0$ obeying the velocity boundary conditions. Re-derive this chain in the session; do not trust the prompt's algebra without proof. Define the **background-method value**
\[
B(\mathrm{Ra};\Pr,\Gamma):=\inf\Bigl\{\int_0^1\tau'^2\,dz:\ (\tau,a)\ \text{admissible, }\ \mathcal Q_{\tau,a}\ge0\Bigr\},
\]
and let $\beta_{\mathrm{bg}}$ be its growth exponent. After horizontal Fourier transform, the constraint $\mathcal Q_{\tau,a}\ge0$ decouples into one-dimensional quadratic-form constraints indexed by the horizontal wavenumber $k\ge0$ - this is the structure that makes certified computation tractable.

### 1.4 The open questions

1. **(Upper bound)** Prove $\overline N\le C\,\mathrm{Ra}^{\beta}$ (logarithms allowed) with $\beta<1/2$ for the primary configuration, unconditionally in $\mathcal S$.
2. **(Obstruction)** Prove $B(\mathrm{Ra})\ge c\,\mathrm{Ra}^{1/2}$ for large $\mathrm{Ra}$ - the background method as formulated in 1.3 cannot yield $\beta<1/2$ in the primary configuration - and delimit precisely which augmented constraint sets share this saturation.
3. **(Lower bound)** Exhibit solutions (or admissible fields for stated relaxations, clearly labeled) with $\mathrm{Nu}\ge c\,\mathrm{Ra}^{\beta'}$, with $\beta'$ as large as possible.

## 2. Complete-resolution standard

A complete resolution is the **determination of $\beta_*(\Pr)$ for the primary configuration at some fixed $\Pr\in(0,\infty)$**:

- a proven upper bound $\overline N\le C_\epsilon\,\mathrm{Ra}^{\beta_*+\epsilon}$ for every $\epsilon>0$ (or with explicit logarithmic corrections), valid for all solutions in $\mathcal S$;
- a construction of solutions of the Boussinesq system realizing $\mathrm{Nu}\ge c_\epsilon\,\mathrm{Ra}^{\beta_*-\epsilon}$;
- all constants explicit, every computer-assisted step certified to the standard of section 6.

This plainly requires progress of Navier–Stokes calibre and is **unlikely to be achieved in a session**; the graded targets of section 3 are the realistic goal.

**Not accepted as resolution:**

- Numerically optimized background profiles or auxiliary functionals without interval-verified certificates.
- Certified bounds at finitely many Rayleigh numbers presented as an asymptotic scaling law. A scaling claim requires a certificate valid for all $\mathrm{Ra}\ge \mathrm{Ra}_0$ with symbolic $\mathrm{Ra}$-dependence.
- Two-dimensional, free-slip, Navier-slip, fixed-flux, or $\Pr=\infty$ results presented as the finite-$\Pr$ three-dimensional no-slip theorem.
- Bounds for relaxations - wall-to-wall optimal transport over divergence-free fields, energy-stability classes, truncated dynamics - presented as bounds for Boussinesq solutions.
- Prefactor improvements at exponent $1/2$ presented as exponent progress.
- Heuristic scaling theories (Malkus $1/3$; Kraichnan/Spiegel ultimate regime; Grossmann–Lohse) or agreement with experiment/DNS, in any role other than motivation.
- Bounds valid only under undeclared regularity or initial-data restrictions.

## 3. Graded partial-result targets

- **P1 - Doering–Constantin 1996 reproduced with a certified constant chain.**
  - Deliverable: explicit piecewise-linear $\tau$ with boundary-layer width $\delta(\mathrm{Ra})$, a symbolic proof of the spectral constraint via elementary functional inequalities, and the resulting theorem $\mathrm{Nu}\le c_1\mathrm{Ra}^{1/2}$ for all $\mathrm{Ra}\ge\mathrm{Ra}_0$ with explicit $c_1,\mathrm{Ra}_0$.
  - Certificate: machine-checked inequality chain (SymPy script) with every lemma constant explicit; independent interval re-check. This validates the entire toolchain.
- **P2 - Certified optimal backgrounds at finite Ra.**
  - Deliverable: numerically optimal $(\tau,a)$ at $\mathrm{Ra}\in\{10^5,\dots,10^{10}\}$ (logarithmic grid), each certified by per-wavenumber interval eigenvalue enclosures for the reduced 1D forms, interval coverage of the wavenumber continuum, and an analytic large-$k$ coercivity lemma.
  - Product: a certified curve $B_{\mathrm{cert}}(\mathrm{Ra})$ with two-sided enclosures, compared against the reported numerically optimal prefactor $c\approx0.026$ in $\mathrm{Nu}\le c\,\mathrm{Ra}^{1/2}$ (verify the value and its source before citing).
- **P3 - All-Ra parametric certificate at near-optimal prefactor.**
  - Deliverable: a closed-form family $\tau_{\mathrm{Ra}}$ with symbolic $\mathrm{Ra}$-dependence whose spectral constraint is certified for **all** $\mathrm{Ra}\ge\mathrm{Ra}_0$, with prefactor within a few percent of the P2 optimum.
  - Value: the best fully certified unconditional bound in the literature; the natural publication artifact of the session.
- **P4 - Variant configurations with certified chains.**
  - (a) Free-slip 2D, any $\Pr$: reproduce the Whitehead–Doering bound $\mathrm{Nu}\le C\,\mathrm{Ra}^{5/12}$ (which uses an additional vorticity balance) with certified constants; determine the certified-optimal prefactor within that formulation.
  - (b) $\Pr=\infty$: reproduce the $\mathrm{Ra}^{1/3}$-with-logarithms chains (Constantin–Doering; Doering–Otto–Reznikoff; Otto–Seis) with explicit, optimized constants - these proofs have never been constant-optimized.
  - (c) Navier-slip interpolation between no-slip and free-slip (verify current literature before starting).
- **P5 - Obstruction theorem, certified.**
  - Deliverable: a rigorous lower bound $B(\mathrm{Ra})\ge c\,\mathrm{Ra}^{1/2}$ for the primary configuration, by exhibiting for each large $\mathrm{Ra}$ explicit test fields $(v,\theta)$ that force any admissible $\tau$ to satisfy $\int\tau'^2\gtrsim\mathrm{Ra}^{1/2}$, test-field inequalities verified in interval arithmetic, $\mathrm{Ra}$-dependence symbolic.
  - Warm-up: reproduce the Nobili–Otto $\Pr=\infty$ limitation result (verify its exact exponent, reportedly $\mathrm{Ra}^{5/12}$ up to logarithms).
  - Value: settles internally whether P6 must leave the quadratic background class.
- **P6 - Beyond the background class (strongest short of resolution).**
  - Deliverable: any unconditional certified bound $\overline N\le C\,\mathrm{Ra}^{1/2}(\ln\mathrm{Ra})^{-\mu}$ or $\overline N\le C\,\mathrm{Ra}^{1/2-\delta}$ with $\mu,\delta>0$ for the primary configuration - e.g., via auxiliary functionals of degree $>2$, explicit use of the maximum principle $0\le T\le1$, or new boundary-layer-localized interpolation inequalities.
  - Honest calibration: no such bound exists as of this writing; even a certified logarithmic improvement is a publishable advance.

## 4. Known results and prior art

- Malkus (1954): marginal-boundary-layer phenomenology, $\mathrm{Nu}\sim\mathrm{Ra}^{1/3}$. Kraichnan (1962), Spiegel: ultimate-regime $\mathrm{Ra}^{1/2}$ (with log corrections) phenomenology.
- Howard (1963), Busse (1969): variational bounds under statistical hypotheses; $\mathrm{Nu}\lesssim\mathrm{Ra}^{1/2}$ modulo assumptions.
- Doering–Constantin (1992–1996): the background method; unconditional $\mathrm{Nu}\le c\,\mathrm{Ra}^{1/2}$ for no-slip boundaries (the 1996 convection paper of the energy-dissipation series). Improved prefactors: Nicodemus–Grossmann–Holthaus (1997–98) (verify).
- Optimal-background computations: Plasting–Kerswell (2003) for plane Couette (the exactly solved analogue); for Rayleigh–Bénard, numerically optimal backgrounds by Wen, Chini, and coworkers (~2015) and subsequent Wen–Goluskin–Doering-adjacent work (verify authors, years, and the asymptotic prefactor before citing).
- $\Pr=\infty$: Constantin–Doering (1999), $\mathrm{Ra}^{1/3}(\ln\mathrm{Ra})^{2/3}$; Doering–Otto–Reznikoff (2006), improved logarithm; Otto–Seis (2011), $\mathrm{Ra}^{1/3}(\ln\mathrm{Ra})^{1/3}$-type bound (verify exact log exponents). Finite-but-large $\Pr$: Choffrut–Nobili–Otto (~2016), $\Pr$-dependent interpolation bounds.
- Free-slip: Whitehead–Doering (2011), $\mathrm{Nu}\le0.289\,\mathrm{Ra}^{5/12}$ in 2D at arbitrary $\Pr$; 3D free-slip analogues at $\Pr=\infty$ (Whitehead–Doering ~2012) (verify scope). Note: free-slip is **not** "solved" - $5/12$ is a bound, not a matched exponent. Navier-slip: Drivas–Nguyen–Nobili (~2022) (verify).
- Method limitations: Nobili–Otto (~2017), lower bound on the optimal background value at $\Pr=\infty$. Tobasco–Doering (2017; CPAM ~2019): wall-to-wall optimal transport - divergence-free fields with an enstrophy budget achieve $\mathrm{Ra}^{1/2}$ up to logarithms, so constraint sets blind to the momentum equation beyond the energy balance cannot beat $1/2$.
- Auxiliary-functional framework: Chernyshenko–Goulart–Huang–Papachristodoulou (2014); Fantuzzi–Arslan–Wynn, review of the background method (~2022); Arslan and coworkers, internally heated variants (2021–2024). Software precedent: QUINOPT (Fantuzzi–Wynn) for quadratic integral inequalities via SDP.
- Steady-solution transport: computed steady convection rolls reach $\mathrm{Ra}^{1/3}$-type transport (Wen–Goluskin–Doering ~2020–22) (verify); no solution family is proven to exceed $\mathrm{Ra}^{1/3}$ asymptotically.
- Experiments (context only, never evidence): Chavanne et al. (1997), Niemela et al. (2000), He–Ahlers and successors - the experimental ultimate-regime controversy is itself unresolved.

**Status as of mid-2026 - re-verify against current literature before starting the session.**

## 5. Attack plan

First computations, all sized for a single workstation (≥16 cores, 64 GB):

1. **Wavenumber reduction.** Derive the 1D reduced quadratic forms in $(w_k(z),\theta_k(z))$ - fourth-order in $w_k$ after eliminating horizontal velocity components via incompressibility - with $k$ entering polynomially. Symbolic derivation in SymPy/SageMath, stored as exact rational-coefficient operators.
2. **Exploration solve.** Discretize with Legendre or Chebyshev Galerkin (QUINOPT-style relaxation with rigorous truncation bounds); solve the background SDP with a floating-point solver (Mosek/SCS) to locate optima; re-solve critical certificates in high precision (SDPA-GMP).
3. **Certification pass.** Round Gram matrices to rationals; verify positive semidefiniteness by exact $LDL^{\mathsf T}$ over $\mathbb Q$ (FLINT) or interval Cholesky with directed rounding (Arb). Cover the $k$-continuum by interval subdivision with Lipschitz-in-$k$ coefficient bounds; prove a large-$k$ coercivity lemma once, symbolically. Include the $k=0$ mean mode explicitly - omitting it is a classic silent error.
4. **Parametric certificates (P3, P5).** Keep $\mathrm{Ra}$ symbolic: piecewise-defined $\tau$ with rational-function dependence on the layer width $\delta(\mathrm{Ra})$; reduce the constraint to finitely many polynomial inequalities in $(\delta,k)$; certify by SOS with exact rounding, or by case analysis with interval arithmetic in Arb.
5. **Workstation budget.** One finite-Ra certificate: minutes to hours; the P2 grid: days; the symbolic P3 certificate: mostly human/model time, negligible compute.
6. **Expected failure modes.**
   - SDP ill-conditioning at $\mathrm{Ra}\ge10^9$: boundary layers $\sim\mathrm{Ra}^{-1/2}$ demand mapped bases or piecewise elements; do not brute-force polynomial degree.
   - Interval Cholesky failing exactly at the numerical optimum: retreat to a suboptimal $\tau$ with explicit margin $\eta$.
   - Conflating "certified at sampled Ra" with "certified for all Ra".
   - Weak-solution bookkeeping (time-average limits, attractor regularity) undermining the formal chain: write the functional-analytic wrapper first, at P1.

## 6. Verification and auditability requirements

1. **Exact arithmetic.** Every claimed inequality constant lives in $\mathbb Q$ or in an Arb ball with directed rounding; floating-point SDP output is exploration only. The spectral-constraint verdict for each $(\tau,a,\mathrm{Ra})$ must come from the exact/interval pass, never from solver status codes.
2. **Independent verification.** A standalone checker (C++/Arb, of order a few hundred lines, no dependence on the search code) that takes a certificate file - $\tau$ spline data, $a$, Gram matrices, $k$-subdivision, tail-lemma constants - and outputs a verdict; a second, independently written Python/mpmath checker for every headline certificate.
3. **Reproducibility.** Record solver names and versions, precision settings, basis degrees, $k$-grids, and all seeds; SHA-256 manifest over certificate files, scripts, and the environment lockfile.
4. **Preservation.** All optimization drivers, failed profile families, and the symbolic derivation notebooks are part of the record; any discarded exploration branch is listed, not silently dropped.
5. **Honest reporting.** The final report opens with: complete-resolution standard (section 2) met or not met - expected **not met**. Each result is labeled by its P-target, its configuration (dimension, boundary conditions, $\Pr$), and its validity range in $\mathrm{Ra}$; no scaling claim beyond the certified range.
