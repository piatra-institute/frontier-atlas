# PROMPT FOR AN ANALYTIC DERIVATION OF THE CHOPTUIK CRITICAL-COLLAPSE CONSTANTS

## The echoing period Δ and mass-scaling exponent γ of critical gravitational collapse

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 36 of 50 (Tier 3)
**Source:** top-50 list #50, category H (classical gravitation)
**Modes:** `[sym]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Spherically symmetric collapse of a massless scalar field exhibits universal critical behavior at the black-hole formation threshold (Choptuik 1993): the black-hole mass scales as $M \propto (p - p^*)^\gamma$ with $\gamma \approx 0.374$, and the critical solution is discretely self-similar (DSS) with echoing period $\Delta \approx 3.4453$. Both constants are eigenvalues of a well-posed self-similarity boundary-value problem - precise mathematical objects, computed numerically to many digits (Gundlach; Martín-García–Gundlach) but never derived analytically. A computer-assisted existence proof of the critical spacetime was announced by Reiterer–Trubowitz (~2012, published ~2019 - the assignment sheet's "rigorous existence unproven" must be re-audited against this). The problem is matched to current AI methods because the entire pipeline is certifiable: validated-numerics existence proofs, certified eigenvalue enclosures for $\Delta$ and $\gamma$, and PSLQ mining against transcendental bases are concrete machine-checkable deliverables that the numerical-relativity literature has almost never produced. Full analytic derivation - the complete resolution of section 2 - is unlikely; the graded targets of section 3 are the goal, and any lesser outcome must be reported as partial.

## 1. Exact problem statement

### 1.1 Field equations

Einstein–massless-scalar system, $G = c = 1$, action

\[
S = \int \Bigl( \tfrac{R}{16\pi} - \tfrac12 (\nabla\phi)^2 \Bigr) \sqrt{-g}\; d^4x ,
\]

so $G_{ab} = 8\pi \bigl( \nabla_a\phi \nabla_b\phi - \tfrac12 g_{ab} (\nabla\phi)^2 \bigr)$ and $\Box \phi = 0$. Spherical symmetry in polar-areal gauge:

\[
ds^2 = -\alpha^2(t,r)\, dt^2 + a^2(t,r)\, dr^2 + r^2 d\Omega^2 .
\]

With $\Phi = \partial_r \phi$ and $\Pi = (a/\alpha)\, \partial_t \phi$:

\[
\partial_t \Phi = \partial_r \Bigl( \frac{\alpha}{a} \Pi \Bigr), \qquad
\partial_t \Pi = \frac{1}{r^2}\, \partial_r \Bigl( r^2 \frac{\alpha}{a} \Phi \Bigr),
\]
\[
\frac{\partial_r a}{a} = \frac{1 - a^2}{2r} + \kappa\, r\, (\Phi^2 + \Pi^2), \qquad
\frac{\partial_r \alpha}{\alpha} = \frac{\partial_r a}{a} + \frac{a^2 - 1}{r},
\]

with $\kappa = 4\pi$ in the normalization above (Choptuik's papers use a rescaled field with $\kappa = 2\pi$; the session must fix and audit the convention - a wrong $\kappa$ changes nothing physical here but corrupts cross-checks). Regularity at the center: $a(t,0) = 1$, $\Phi(t,0) = 0$.

### 1.2 The critical solution and the constants

**DSS critical solution.** In adapted coordinates $T = -\ln\bigl((t_* - t)/\ell\bigr)$, $x = r/(t_* - t)$ (accumulation point $t_*$, arbitrary scale $\ell$), the critical solution $Z_* = (a, \alpha, \phi)$ is invariant under $T \to T + \Delta$ for a specific $\Delta > 0$:

\[
a_*(x, T + \Delta) = a_*(x, T), \qquad \alpha_*(x, T + \Delta) = \alpha_*(x, T), \qquad \phi_*(x, T + \Delta) = \pm\, \phi_*(x, T)
\]

(the scalar may return with a sign; conventions differ - the session must state which period is quoted; the standard value refers to the metric period (verify)). The critical solution is the DSS solution that is analytic, regular at the center $x = 0$, and regular on the past self-similarity horizon (the backward characteristic cone of the accumulation point), with $\Delta$ determined as a nonlinear eigenvalue by these two-point regularity conditions (Gundlach's formulation).

**The exponent $\gamma$.** Linear perturbations about $Z_*$ of the form $\delta Z \sim e^{\lambda T} \zeta(x, T)$, with $\zeta$ periodic in $T$ of period $\Delta$, admit (numerically) exactly one growing mode, with real eigenvalue $\lambda_0 > 0$; then $\gamma = 1/\lambda_0$.

**Reference values:** $\Delta = 3.445452402(3)$ (Gundlach ~1997; verify current best digits, including recent recomputations by Baumgarte and collaborators) and $\gamma \approx 0.374$, $\lambda_0 \approx 2.674$ (Gundlach; Martín-García–Gundlach; verify).

### 1.3 The open problem

**Derive $\Delta$ and $\gamma$ analytically:** produce closed forms in known constants, or a proven exact characterization sharper than "eigenvalue of the BVP of section 1.2" (e.g. an explicit transcendental equation from monodromy/Stokes data of an associated linear problem), together with rigorous existence of the DSS solution and of the single growing mode, and certified numerical agreement. Subsidiary precise questions: is $\lambda_0$ real and simple (numerically yes - prove it)? Is the DSS solution locally unique up to the symmetry group? No informal phrasing ("explain the value 3.44") is an acceptable target.

## 2. Complete-resolution standard

Complete resolution requires all of:

1. An analytic characterization of $\Delta$ - closed form, or an explicit proven equation in identified special functions or monodromy data whose solution set provably contains the physical $\Delta$ and provably selects it - plus the same for $\lambda_0$, hence $\gamma$.
2. Rigorous existence of the DSS critical solution with the section-1.2 regularity, and rigorous existence, realness, and uniqueness of the growing mode.
3. Certified numerical confirmation: the analytic characterization reproduces $\Delta$ and $\gamma$ within certified enclosures matching the section-3 artifacts.

**Not accepted as resolution:**

- Numerical values of $\Delta$, $\gamma$ to any precision, certified or not (those are P2–P4).
- Formal series or perturbative constructions without validated error control.
- PSLQ or inverse-symbolic identifications, however striking, without proof.
- Existence claims from truncated Galerkin/Fourier systems without a posteriori validation.
- Assuming, rather than proving, the single-growing-mode property in any derivation of $\gamma$.
- Results for surrogate systems (continuously self-similar matter, perfect fluids, lower-dimensional models) presented as results for the massless-scalar DSS problem - they are context (cf. P5).

## 3. Graded partial-result targets

### P1 - Independent reproduction (exploratory tier)

- Re-derive the section-1.1 system symbolically (SageManifolds or xAct - machine-checked tensor algebra, catching the $\kappa$ convention).
- Implement a Fourier-in-$T$ × Chebyshev-in-$x$ pseudospectral solver for the DSS BVP and the linearized mode problem.
- Reproduce $\Delta$ and $\gamma$ to $\ge 8$ digits against the literature, with convergence tables.
- *Certificate:* code, convergence data, manifest - explicitly labeled non-rigorous.

### P2 - Certified existence and Δ enclosure (the headline realistic target)

- A validated-numerics existence proof: Newton–Kantorovich / radii-polynomial argument around the P1 solution in a Fourier–Chebyshev Banach algebra, all bounds in Arb ball arithmetic (or CAPD), with the singular past-horizon regularity conditions built into the unknowns.
- Theorem: a DSS solution exists with $\Delta \in [\underline\Delta, \overline\Delta]$, explicit interval.
- Positioning: audit Reiterer–Trubowitz first (verify their exact statement, method, and published status). The deliverable is an *independent, quantitatively sharp* proof with an explicit $\Delta$ enclosure; if their theorem does not cover the standard formulation or gives no tight enclosure, this target is a genuine new theorem either way.
- *Certificate:* proof document plus machine-verifiable bound ledger.

### P3 - Certified γ

- Enclosure of the growing eigenvalue $\lambda_0$ of the linearization about the validated solution: certified eigenpair via the same functional-analytic machinery.
- Realness and simplicity certified within an explicit spectral region; an honest statement of exactly which region is swept (a certified global count of unstable modes is the hard part - scope it explicitly).
- Theorem: $\gamma = 1/\lambda_0 \in [\underline\gamma, \overline\gamma]$.
- *Certificate:* bound ledger plus contour/argument-principle data with certified quadrature.

### P4 - High precision and PSLQ mining

- Push P2/P3 enclosures to $\ge 30$–$50$ certified digits (Newton in ball arithmetic on larger truncations).
- PSLQ and inverse-symbolic searches for $\Delta$, $\lambda_0$, $\gamma$, and simple combinations ($e^{\Delta}$, $\Delta/\pi$, $2\pi/\Delta$, $\gamma\Delta$, ...) against bases $\{\pi, e, \ln 2, \ln 3, \gamma_E, \zeta(3), \Gamma(1/3), \Gamma(1/4)\}$ and low-height products.
- Certified negative results (no small-height relation below stated norms) are the expected outcome and are the first such calibration in this literature.
- *Certificate:* PSLQ logs with precisions, norms, and decoy controls.

### P5 - Structure of the echoing equation

- Reformulate the $\Delta$-eigenvalue condition as a connection/monodromy problem in the complexified similarity coordinate (Stokes data at $x = 0$ and at the past horizon).
- Prove a reduction theorem of the form "$\Delta$ solves $\mathcal{M}(\Delta) = 0$" with $\mathcal{M}$ built from monodromy/path-ordered data of an explicit linear system - the plausible route toward an analytic derivation.
- Contrast with continuously self-similar analogues where criticality constants come from ODE eigenvalue problems (perfect fluids, Koike–Hara–Adachi 1995; the Roberts family) to isolate what is genuinely DSS-hard.
- *Certificate:* theorem-level reduction, plus certified numerics consistency.

### P6 - Windfall

- Closed forms for $\Delta$ or $\gamma$ meeting the section-2 standard.

## 4. Known results and prior art

- Choptuik 1993: discovery - universality, mass scaling $\gamma \approx 0.37$, echoing $\Delta \approx 3.44$.
- Gundlach 1995–1997: the DSS critical solution as a nonlinear eigenvalue problem; high-precision $\Delta$; perturbation spectrum and $\gamma$ from the growing mode.
- Hod–Piran 1997: fine structure (periodic wiggle of period $\Delta/(2\gamma)$ superposed on the scaling law).
- Martín-García–Gundlach ~1999–2003: nonspherical perturbations (all decaying); global structure of the critical spacetime (verify).
- Gundlach–Martín-García 2007: Living Reviews survey - canonical reference for definitions and values (verify latest revision).
- Reiterer–Trubowitz, "Choptuik's critical spacetime exists" (~2012 preprint; published in Communications in Mathematical Physics ~2019 - verify): computer-assisted existence proof of a DSS solution with period near the numerical $\Delta$; audit its exact formulation, stated enclosure, and community acceptance before framing P2.
- Recent numerics: Baumgarte and collaborators ~2018–2024 (spherical and aspherical critical collapse, improved codes); the Gundlach–Baumgarte–Hilditch program on critical collapse beyond spherical symmetry (verify current values and digits).
- Analogues with semi-analytic constants: Koike–Hara–Adachi 1995 (perfect fluid, CSS, exponents from ODE eigenvalue problems); Neilsen–Choptuik 2000 (fluid collapse); Roberts 1989 (CSS scalar solution - not the critical one).
- Validated-numerics methodology: the radii-polynomial / rigorous-computing school (van den Berg–Lessard and collaborators, ~2010s) - technology base for P2/P3, not results on this problem.

Status as of mid-2026 - re-verify against current literature before starting the session; in particular, resolve the Reiterer–Trubowitz status first, since it determines whether P2 is "first proof with sharp enclosure" or "independent second proof".

## 5. Attack plan

1. **Symbolic layer.**
   - SageManifolds (or xAct) derivation of the polar-areal system and the DSS-coordinate residual equations, machine-checked; export as explicit polynomial-in-fields expressions for the spectral solver.
   - Cross-check against a second, independently written derivation; this layer exists to kill sign and convention errors.
2. **Exploratory solver (P1).**
   - Fourier ($T$) × Chebyshev ($x$) collocation on $x \in [0, x_{\mathrm{hor}}(T)]$ with the horizon location among the unknowns (or a horizon-adapted compactification).
   - Newton iteration with phase conditions removing the $T$-translation and scaling zero-modes; $\Delta$ enters as an unknown with one normalization condition.
   - Julia or Python; truncations $40 \times 40$ to $80 \times 80$; workstation-scale.
3. **Validation (P2).**
   - Radii-polynomial argument around the Newton solution: bound the approximate inverse Jacobian and truncation tails in a weighted $\ell^1$ Fourier–Chebyshev algebra, all constants in Arb (python-flint) with directed rounding; CAPD Taylor-model integration along characteristics as an alternative route for the horizon-regularity map.
   - The past horizon is a singular characteristic: expand in the regular-singular basis there and certify the truncation of that expansion.
4. **Eigenvalue tier (P3).** Certified eigenpair for the Floquet-type linearization; argument-principle mode counting in an explicit region with certified contour quadrature.
5. **Mining (P4).** mpmath PSLQ with doubled-precision confirmation and decoy-basis controls; log everything, including negatives.

Expected failure modes: gauge/normalization drift between codes ($\kappa$, slicing conventions) - mitigated by the machine-checked symbolic layer; the singular past horizon destroying naive spectral convergence (regularity must be built in analytically); the zero-modes making Newton singular (phase conditions are mandatory); eigenvalue crowding near $\lambda_0$ defeating crude enclosures; underestimating P2 - validated PDE proofs with two singular boundaries are heavy, and a completed P2 alone is a strong session outcome.

## 6. Verification and auditability requirements

1. **Exact arithmetic.** Every certified bound in ball/interval arithmetic with directed rounding (Arb or CAPD); floating-point results confined to P1 and labeled non-rigorous.
2. **Independent verification.** The radii-polynomial ledger (finite bounds, tail bounds, radii) re-checked by a standalone checker reading stored coefficients; the DSS field equations verified by two independent symbolic derivations; $\Delta$ and $\gamma$ cross-checked between independent discretizations (collocation vs Galerkin) before certification.
3. **Reproducibility.** Truncation sizes, weights, precisions, phase conditions, and continuation paths recorded; SHA-256 manifest over solution coefficients, bound ledgers, and PSLQ logs; pinned versions of Arb/python-flint, CAPD, SageMath.
4. **Preservation.** Failed validation attempts (radii that did not close) are data - preserved with their parameters; discarded branches listed.
5. **Honest reporting.** The report opens with the outcome of the Reiterer–Trubowitz audit and states whether the section-2 standard was met (expected: no); every value of $\Delta$ and $\gamma$ is labeled (literature), (our floating point), or (certified enclosure); no PSLQ hit is reported as a derivation.
