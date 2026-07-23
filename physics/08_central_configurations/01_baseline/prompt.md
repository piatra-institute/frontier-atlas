# PROMPT FOR THE FINITENESS OF PLANAR CENTRAL CONFIGURATIONS OF THE NEWTONIAN $n$-BODY PROBLEM

## Smale's sixth problem - relative equilibria for $n \ge 5$, with Saari's conjecture and point-vortex companions

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 08 of 50 (Tier 1)
**Source:** top-50 list #35, category E (dynamical systems and classical mechanics)
**Modes:** `[cert]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Smale's sixth problem for the twenty-first century asks whether, for every choice of positive masses, the Newtonian $n$-body problem has only finitely many relative equilibria - equivalently, finitely many similarity classes of planar central configurations. The question is classical (Chazy 1918, Wintner 1941), controls the bifurcation structure of the full $n$-body flow, and is settled only for $n \le 4$ in full and $n = 5$ generically. It is matched to current AI methods because the entire modern attack is certifiable computational algebra: BKK/mixed-volume bounds, Gröbner and resultant elimination, and interval (Krawczyk) certificates over configuration and mass space - exactly the `[cert]` mode. The complete resolution defined in section 2 is the target. Full resolution for all $n$ is not a realistic single-session outcome; the graded targets of section 3 are the intended product, and anything short of the section 2 standard must be reported as a partial result, never represented as a solution.

## 1. Exact problem statement

### 1.1 Central configurations

Fix $n \ge 3$, masses $m = (m_1,\dots,m_n) \in \mathbb{R}_{>0}^n$, total mass $M = \sum_i m_i$, and positions $q = (q_1,\dots,q_n) \in (\mathbb{R}^2)^n$ with $q_i \ne q_j$ for $i \ne j$. Write $r_{ij} = |q_i - q_j|$, center of mass $c = M^{-1}\sum_i m_i q_i$, and

\[
U(q) = \sum_{1 \le i < j \le n} \frac{m_i m_j}{r_{ij}}, \qquad
I(q) = \sum_{i=1}^n m_i\,|q_i - c|^2 .
\]

A configuration $q$ is a **planar central configuration (CC)** for $m$ if there exists $\lambda \in \mathbb{R}$ (necessarily $\lambda = U/I > 0$) such that

\[
\sum_{j \ne i} \frac{m_j\,(q_j - q_i)}{r_{ij}^3} \;+\; \lambda\,(q_i - c) \;=\; 0, \qquad i = 1,\dots,n .
\]

Equivalently, $q$ is a critical point of $U$ restricted to the sphere $\{I = 1\}$, modulo isometries. Each planar CC generates a **relative equilibrium**: the rigid solution $q(t) = R(\omega t)\,q(0)$, $R$ a rotation with $\omega^2 = \lambda$; conversely every relative equilibrium of the planar problem arises this way. "Relative equilibrium" and "planar central configuration" are used interchangeably below.

### 1.2 Equivalence and counting

Two CCs are **equivalent** if they differ by a composition of translation, rotation, reflection, and dilation of $\mathbb{R}^2$. Relabelings are *not* quotiented: a labeled count is adopted, so mass-symmetric statements stay unambiguous. Let

\[
\mathrm{cc}(m) \;\in\; \mathbb{N} \cup \{\infty\}
\]

denote the number of equivalence classes of planar CCs for the mass vector $m$.

### 1.3 The adopted question

**Smale's sixth problem (adopted formulation).** *Is $\mathrm{cc}(m)$ finite for every $n \ge 3$ and every $m \in \mathbb{R}_{>0}^n$?*

Current status of the exact question:

- $n = 3$: yes; exactly five classes (three Euler collinear, two Lagrange equilateral) for all positive masses.
- $n = 4$: yes, for all positive masses (Hampton–Moeckel 2006), with $32 \le \mathrm{cc}(m) \le 8472$.
- $n = 5$: yes for all masses outside an explicitly defined codimension-two subvariety of mass space (Albouy–Kaloshin 2012); open on that variety.
- $n \ge 6$: completely open, for every mass vector.
- Positivity of masses is essential: with one negative mass, a continuum of five-body CCs exists (Roberts 1999).

No informal surrogate ("essentially finite", "finite for physical masses", "finitely many observed") is an acceptable target.

### 1.4 Reduced algebraic formulations

Work in mutual-distance variables. With $s_{ij} = r_{ij}^2$, $S_{ij} = r_{ij}^{-3} + \lambda$ (normalize $\lambda = 1$ by dilation), $s_{ii} = 0$, $S_{ii} = 0$, the Albouy–Chenciner equations (1998) are

\[
f_{ij} \;=\; \sum_{k=1}^{n} m_k \Big[\, S_{ik}\,(s_{jk} - s_{ik} - s_{ij}) \;+\; S_{jk}\,(s_{ik} - s_{jk} - s_{ij}) \,\Big] \;=\; 0,
\qquad 1 \le i < j \le n,
\]

which characterize CCs in $\mathbb{R}^{n-1}$. Planarity for $n \ge 4$ is imposed by the vanishing of all $4$-point Cayley–Menger determinants:

\[
\mathrm{CM}(i,j,k,l) \;=\;
\det \begin{pmatrix}
0 & 1 & 1 & 1 & 1 \\
1 & 0 & s_{ij} & s_{ik} & s_{il} \\
1 & s_{ij} & 0 & s_{jk} & s_{jl} \\
1 & s_{ik} & s_{jk} & 0 & s_{kl} \\
1 & s_{il} & s_{jl} & s_{kl} & 0
\end{pmatrix} = 0 .
\]

After clearing denominators (auxiliary variables $t_{ij}$ with $t_{ij}^2 s_{ij}^3 = 1$, or the Hampton–Moeckel polynomialization), one obtains a polynomial system with the masses as parameters. Dziobek's equations give the classical $n = 4$ reduction. Any inequivalent formulation used in a session must be proved equivalent to 1.1–1.3 before results are claimed in its terms.

### 1.5 Companion problems (in scope as graded targets, not as substitutes)

**Saari's conjecture.** A solution $q(t)$ of the planar $n$-body problem with $I(q(t))$ constant in $t$ is a relative equilibrium. Proven for $n = 3$ and all positive masses (Moeckel 2005, computer-assisted, BKK + interval arithmetic); open in general for $n \ge 4$.

**Point-vortex analog.** For vorticities $\Gamma_i \ne 0$, the relative equilibria of the planar point-vortex system (interaction $\propto r_{ij}^{-1}$ in the velocity field; logarithmic Hamiltonian) satisfy an analogous algebraic system. Hampton–Moeckel (2009) proved finiteness for four vortices, with explicit exceptional vorticity conditions - verify the exact hypotheses before citing.

## 2. Complete-resolution standard

A complete resolution of this prompt's problem is one of the following, with full proof:

1. **Finiteness theorem.** For every $n \ge 3$ and every $m \in \mathbb{R}_{>0}^n$, $\mathrm{cc}(m) < \infty$. A proof for a fixed new $n$ (all positive masses) is the complete resolution *at that $n$*; the first open instances are $n = 5$ on the Albouy–Kaloshin exceptional variety, and $n = 6$ in full.
2. **Counterexample.** An explicit $n$, an explicit $m \in \mathbb{R}_{>0}^n$, and a proof that the set of equivalence classes of planar CCs for $m$ contains a continuum.

Required form: theorem-level mathematics; every computational step carried by exact or interval certificates per section 6; if computer-assisted, the certificate chain must be independently checkable without rerunning the search.

**Not accepted as resolution**

- Finiteness for *generic* masses only (this is the Albouy–Kaloshin grain at $n = 5$; at $n \ge 6$ it would be a landmark partial result - still not the resolution).
- Finiteness restricted to a symmetry class (collinear, reflection-symmetric, stacked, nested rings) represented as the full planar statement.
- BKK, Bézout, or homotopy root counts alone: these bound *isolated* solutions and prove nothing until positive-dimensional components are excluded for the actual parameter values.
- Floating-point enumerations of CCs, however exhaustive-looking, without interval or algebraic certificates.
- Upper bounds on $\mathrm{cc}(m)$ *conditional on* finiteness.
- Results for vortices, charges, quasihomogeneous potentials, or the spatial ($\mathbb{R}^3$) problem represented as the planar Newtonian statement.
- "Finiteness holds for all masses we sampled."

## 3. Graded partial-result targets

Ordered from most accessible to strongest short of resolution. Each is independently valuable and must ship with its own certificate.

- **P1 - Reproduce the $n = 4$ finiteness certificates with our own toolchain.**
  - *Task:* from our own encoding of the Albouy–Chenciner/Dziobek system, recompute (a) the Newton polytopes and mixed volumes in exact integer arithmetic; (b) the exclusion of every relevant face system - no zeros in $(\mathbb{C}^*)^N$ compatible with positive masses - each face closed by a Gröbner/ideal-membership certificate over $\mathbb{Q}$ or an interval infeasibility certificate.
  - *Certificate:* per-face artifact files (basis cofactors or interval exclusion trees) plus an independent checker that re-verifies each exclusion without the search code.
  - *Value:* reproduces Hampton–Moeckel (2006) on our own stack; toolchain gate for everything below.
- **P2 - Reproduce one companion computer-assisted theorem.**
  - *Task:* Moeckel's Saari proof for $n = 3$ (all positive masses) or Hampton–Moeckel four-vortex finiteness, on the P1 pipeline.
  - *Certificate:* same standard as P1.
  - *Value:* demonstrates the pipeline generalizes across the problem family rather than being tuned to one system.
- **P3 - Certified complete solution lists at explicit masses.**
  - *Task:* reproduce the Moczurad–Zgliczyński equal-mass planar counts for $n = 5, 6$ (and $7$ if resources allow) with an independent interval-Krawczyk search over the compact normalized domain; then produce *new* certified complete CC lists for explicit non-equal rational mass vectors at $n = 5$, and first instances at $n = 6$.
  - *Certificate:* the full bisection tree; per-box Krawczyk contraction or exclusion data; a standalone checker verifying every box; explicit collision/infinity boundary exclusion inequalities.
  - *Value:* each new mass vector is a new certified data point on the finiteness landscape and feeds P4.
- **P4 - Certified exclusion/constancy regions in mass space.**
  - *Task:* explicit product boxes $B \subset \mathbb{R}_{>0}^n$ (mass space; $n = 5$, then $6$) with a parametric interval certificate that for every $m \in B$ all CCs are nondegenerate and $\mathrm{cc}(m)$ is finite and constant on $B$.
  - *Certificate:* parametric Krawczyk enclosures (masses as interval parameters) covering the configuration domain; box list with per-box contraction constants.
  - *Value:* converts finiteness from a point statement into an open-set statement with a machine-checkable proof - the concrete "exclusion regions in mass space" deliverable.
- **P5 - $n = 6$ finiteness in an explicit symmetry class, all positive masses.**
  - *Task:* for a declared class (e.g., reflection symmetry pairing equal masses; stacked/kite reductions), run the full BKK + face-exclusion program of P1 on the reduced system with symbolic mass parameters.
  - *Certificate:* exact mixed volumes plus face-exclusion certificates valid for all positive masses in the class.
  - *Value:* first finiteness theorems touching $n = 6$; the reduced systems are the proving ground for the general attack.
- **P6 - Frontier theorem.**
  - *Task:* either (a) finiteness for $n = 5$ on (part of) the Albouy–Kaloshin exceptional variety, shrinking or closing it, or (b) generic-mass finiteness for $n = 6$ in the Albouy–Kaloshin style.
  - *Certificate:* complete proof; any computational steps to the P1 standard.
  - *Value:* major publication; the strongest realistic result short of the section 2 standard.

## 4. Known results and prior art

- Euler (1767), Lagrange (1772): the five three-body classes. Moulton (1910): exactly $n!/2$ collinear CCs for any positive masses.
- Chazy (1918) and Wintner (1941): the finiteness question. Smale (1998): problem 6 of the eighteen problems for the twenty-first century.
- Palmore (1970s): counts and degenerate examples. Simó (1978): numerical census for $n = 4$; the count varies with the masses (verify the reported range before quoting numbers).
- Albouy–Chenciner (1998): the mutual-distance equations used by all later finiteness work. Albouy (1995–96): complete classification for four equal masses.
- Hampton–Moeckel (2006, Inventiones): finiteness for $n = 4$, all positive masses, via BKK theory over the Albouy–Chenciner system; count between 32 and 8472.
- Albouy–Kaloshin (2012, Annals): finiteness for $n = 5$ for all positive masses outside an explicit codimension-two variety of mass space; new proof for $n = 4$. Check for post-2012 reductions of the exceptional variety - status uncertain (verify).
- Roberts (1999): continuum of five-body CCs with one negative mass - positivity is sharp.
- Saari's conjecture: Moeckel (2005), computer-assisted proof for the planar three-body problem, all positive masses (BKK + interval); McCord (~2004) for three equal masses; Diacu–Pérez-Chavela–Santoprete (~2005) for the collinear case (verify exact scopes).
- Hampton–Moeckel (2009): finiteness of stationary configurations of the four-vortex problem (verify exceptional vorticity hypotheses).
- Moczurad–Zgliczyński (2019, with follow-ups ~2020): rigorous interval-arithmetic complete lists of planar CCs for equal masses, $n = 5, 6, 7$, and related spatial results - the direct methodological ancestor of P3/P4.
- Certification tooling: alphaCertified (Hauenstein–Sottile, ~2012); interval certification in HomotopyContinuation.jl (Breiding–Rose–Timme, ~2020).

Status as of mid-2026 - re-verify against current literature before starting the session.

## 5. Attack plan

All modes here are `[cert]`.

1. **Encode.** Write the Albouy–Chenciner system with Cayley–Menger planarity constraints as an explicit polynomial system over $\mathbb{Q}(m_1,\dots,m_n)$, with the $\lambda = 1$ normalization and a rotation-pinning gauge. Validate by recovering the five three-body classes symbolically (Singular or Macaulay2, rational masses - minutes).
2. **Mixed volumes / BKK.** Newton polytopes and mixed volumes via polymake or Gfan (exact integer arithmetic), cross-checked against the mixed-cell counts reported by PHCpack. Reproduce the Hampton–Moeckel $n = 4$ numbers before anything new is attempted.
3. **Face exclusions.** For each face of the relevant subdivision: attempt a Gröbner/ideal-membership proof that the face system has no admissible zero (Singular, Macaulay2, or msolve over $\mathbb{Q}$, mass parameters symbolic where feasible); where symbolic elimination blows up, fall back to interval exclusion at interval mass parameters (custom C++ with directed rounding, or the kv library; CAPD-style wrappers acceptable).
4. **Krawczyk census.** For explicit rational masses: complete bisection + Krawczyk search over the compact normalized mutual-distance domain, collision and infinity boundaries excluded by explicit inequalities. Exploratory roots via HomotopyContinuation.jl or Bertini/PHCpack first; then certify every found root and certify emptiness of the remainder.
5. **Parametric boxes (P4).** Rerun the census with masses as intervals; where Krawczyk contraction holds uniformly, record constancy of the count; bisect mass boxes adaptively and stop at proximity to the bifurcation set.

**Workstation feasibility.**

- $n = 4$: everything above in hours.
- $n = 5$ equal-mass reproduction: days (Moczurad–Zgliczyński scale).
- $n = 6$: symmetric subclasses and single-mass-vector censuses at the edge (weeks, aggressive pruning).
- Fully parametric $n = 6$ face exclusion: beyond one workstation; must be sharded and budgeted across sessions.

**Expected failure modes.**

- Solutions at infinity/collision faces dominate the BKK count; each face needs its own exclusion argument - this is the bulk of the work, not a corner case.
- Krawczyk fails to contract near degenerate or clustered CCs, driving bisection-depth explosion; mitigate with higher precision (MPFI) and normal-form preconditioning.
- Parametric certificates necessarily fail across bifurcation masses where $\mathrm{cc}(m)$ jumps; boxes must be split to avoid the bifurcation set, and no box may straddle it.
- Gröbner bases with fully symbolic masses blow up at $n \ge 5$; a specialization at sample masses proves nothing for nearby masses without an explicit parametric certificate - do not silently substitute one for the other.
- Gauge-fixing errors (rotation pinning, labeling) silently double-count or drop classes; the checker must recount equivalence classes from raw solution data.

## 6. Verification and auditability requirements

1. **Exact arithmetic.** Masses are exact rationals, or interval parameters with rational endpoints. Polytope and mixed-volume computations in exact integer arithmetic. Every exclusion and contraction claim in interval arithmetic with directed rounding, or in Gröbner/ideal-membership form over $\mathbb{Q}$. Floating-point homotopy runs are exploratory only and certify nothing.
2. **Independent verification.** A standalone checker, written independently of the search code, that (a) re-evaluates Albouy–Chenciner residuals and Krawczyk inclusions from the stored box data, and (b) verifies Gröbner certificates by cofactor re-multiplication (ideal membership), not by re-running the basis computation. Dual implementations - Python/rational and C++/MPFI - for the box checker, run on the full certificate set.
3. **Reproducibility.** Record exact mass vectors, gauge and normalization choices, bisection trees, tool versions (Singular, Macaulay2, msolve, polymake, HomotopyContinuation.jl, Bertini/PHCpack), homotopy seeds, and a SHA-256 manifest over every certificate artifact.
4. **Preservation.** All search code, face-case logs, and discarded branches (failed contractions, inconclusive boxes) are part of the record; anything not preserved is stated explicitly rather than obscured.
5. **Honest reporting.** The final report opens by stating that Smale's sixth problem is not resolved (unless section 2 is actually met), and labels every claim with its exact scope: which $n$, which mass set (point, box, generic, symmetry class), planar vs spatial, Newtonian vs vortex.
