# PROMPT FOR PARKER'S CURRENT-SHEET CONJECTURE

## Must generic line-tied magnetic fields form tangential discontinuities instead of smooth equilibria?

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 42 of 50 (Tier 4)
**Source:** top-50 list #42, category F (fluids, plasmas, continuum)
**Modes:** `[proof]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Parker conjectured in 1972 that a generic smooth magnetic field anchored ("line-tied") between two plates cannot relax, while preserving its field-line topology, to a smooth force-free equilibrium: current sheets - tangential discontinuities of the field - necessarily form. The conjecture is the leading candidate mechanism for coronal heating, and it has resisted proof for five decades partly because its statement has genuinely inequivalent weak and strong readings, which the literature routinely conflates. It suits current AI methods because its most tractable faces are exact-statement engineering (a formulation dossier with a proved implication lattice) and reduced-model rigor: 2.5D line-tied models in which smooth-equilibrium non-existence, or rigorous current-layer growth, is provable with computer-assisted certificates (interval FEM energy bounds, CAPD-style rigorous integration). Tier 4 calibration: the complete resolution defined in section 2 - a genericity theorem in full 3D line-tied ideal MHD, or its refutation - is unlikely in a session; the graded targets in section 3 are the goal, and neither thinning-current-layer numerics nor formal arguments may ever be represented as a solution.

## 1. Exact problem statement

### 1.1 Line-tied geometry and admissible fields

Primary domain: the slab
\[
M=\mathbb T^2\times[0,1]
\]
(variant: $D^2\times[0,1]$; declare which in every claim). Admissible fields:
\[
B\in C^\infty(M;\mathbb R^3),\qquad \nabla\cdot B=0,\qquad B_z>0\ \text{throughout},
\]
so there are no magnetic nulls and every field line runs from the bottom plate to the top. The plates are perfect conductors with prescribed $B\cdot n$; footpoints are frozen.

### 1.2 Topological data and equilibria

**Topological equivalence.** $B\sim B'$ iff $B'=\phi_*B$ for a volume-preserving diffeomorphism $\phi$ of $M$, isotopic to the identity, restricting to the identity on both plates. For $B_z>0$ fields this equivalence is faithfully encoded by the field-line map
\[
F_B:\ \mathbb T^2\times\{0\}\ \to\ \mathbb T^2\times\{1\}
\]
together with the isotopy (braiding and winding) data of the field-line family; the session must fix this encoding precisely. This is part of target P1, and sloppiness here is the historic source of the entire controversy.

**Equilibrium.** A force-free equilibrium is $B$ with
\[
(\nabla\times B)\times B=0 ;
\]
more generally magnetohydrostatic $(\nabla\times B)\times B=\nabla p$. Declare which; Parker's coronal setting is force-free, the adopted primary target.

**Current sheet (adopted meaning).** A limit object with bounded $B$ whose tangential component jumps across a set of positive $\mathcal H^2$-measure - a tangential discontinuity. Large-but-bounded current is *never* a current sheet in this prompt.

### 1.3 The two readings (both tracked; PW is adopted)

- **(PW) Weak / existence reading - adopted target.** For a *generic* smooth equivalence class $[B_0]$ - topology: $C^\infty$ Whitney on representative data; genericity: residual set, or complement of a finite-codimension set, declared in P1 - there is **no** force-free equilibrium $B_\ast\in C^1(M)$ with $B_\ast\in[B_0]$. Consequently any topology-preserving relaxed state fails to be $C^1$ and exhibits tangential discontinuities.
- **(PS) Strong / dynamic reading.** Ideal topology-preserving relaxation dynamics - e.g., magneto-frictional flow $\partial_t B=\nabla\times(v\times B)$ with $v=(\nabla\times B)\times B$ - started from generic smooth data develops unbounded current density, $\|\nabla\times B(t)\|_{L^\infty}\to\infty$ in finite or infinite time, with weak-$*$ limits containing tangential discontinuities.

PW does not imply PS, and PS for one relaxation dynamic does not imply PW; the dossier (P1) must prove exactly which implications hold. The counter-position (van Ballegooijen 1985) holds that smooth equilibria exist for all data near the uniform field - so PW is genuinely contested, and either verdict for a precise class is progress.

### 1.4 Energy and relaxation

The magnetic energy is
\[
\mathcal E(B)=\frac12\int_M|B|^2\,dx .
\]
Within a fixed topological class $[B_0]$, $\mathcal E$ is bounded below by a positive class invariant (the relaxed energy), and force-free fields are exactly the smooth critical points of $\mathcal E$ under topology-preserving variations. The Parker question is whether the infimum of $\mathcal E$ over $[B_0]$ is *attained by a smooth field* for generic $[B_0]$: PW says no. Any relaxation dynamics used in-session must state which quantities it conserves (topology, helicity variants, footpoint data) and which it dissipates - Taylor relaxation, which conserves only total helicity, sits outside the conjecture.

### 1.5 Reduced models in scope

1. The Hahm–Kulsrud–Taylor (HKT) problem and its line-tied variants: 2.5D fields $B=\nabla A\times e_z+B_z e_z$ with boundary shear.
2. Reduced MHD in the strong-guide-field limit.
3. Discrete braided flux-tube classes (pigtail-braid data, in the Parker 1994 tradition).

Results in these models are P-targets, never the 3D theorem.

## 2. Complete-resolution standard

A complete resolution is **either**:

1. A proof of (PW) with an explicit genericity notion: the set of smooth classes admitting a $C^1$ topology-equivalent force-free equilibrium in $M=\mathbb T^2\times[0,1]$ is meager (or has an explicitly characterized complement), together with the current-sheet corollary for relaxed limits; every computer-assisted step certified per section 6; **or**
2. Its refutation: a proof that every class in an open $C^\infty$-neighborhood of the uniform field (or another explicit open set of data) contains a smooth force-free equilibrium - a rigorous van Ballegooijen theorem.

**Not accepted as resolution:**

- Numerical demonstrations of current-layer thinning at any resolution: exponentially thin but smooth layers are consistent with both verdicts, so no simulation - including the extensive corpus reviewed by Pontin–Hornig - decides PW.
- Formal asymptotics or optimization arguments without certified error control.
- Taylor-relaxation results (helicity-only constraints), or any relaxation that abandons topology preservation, presented as Parker-relevant equilibria.
- Reduced-model theorems (2.5D, RMHD, discrete braids) presented as the 3D slab statement; they are graded targets and must be labeled as such.
- "Current sheet" claims where the current is large but provably bounded, or where the discontinuity set has zero $\mathcal H^2$-measure, unless the claim states exactly that.
- Genericity claims without a declared topology on data; statements about $D^2\times[0,1]$ and $\mathbb T^2\times[0,1]$ interchanged silently.
- Weak-solution existence results for relaxed states without a proof that the field-line topology of the data is preserved in the limit.

## 3. Graded partial-result targets

- **P1 - Precise-statement dossier (a contribution in itself).**
  - Deliverable: the PW/PS lattice fully articulated - encodings of topological data for $B_z>0$ slab fields (field-line map plus braiding; winding data on $\mathbb T^2$); at least four precise statements (PW-residual, PW-codimension, PS-finite-time, PS-infinite-time); proved implications and explicit non-implications; the principal literature claims (Parker 1972/1994; van Ballegooijen 1985; Low's analyses; Ng–Bhattacharjee 1998; Craig–Sneyd; line-tied HKT numerics) each mapped to a statement with exact hypotheses.
  - Certificate: the dossier itself, with each implication proved.
- **P2 - Certified verdicts in reduced models (the machine-checkable core).**
  - Deliverable: for the line-tied HKT class with explicit boundary shear data, either a certified proof that no smooth equilibrium exists in a declared function class (interval-arithmetic infeasibility of the equilibrium equations over a compact truncated family, plus a priori tail bounds), or a certified existence proof (radii-polynomial / Newton–Kantorovich in Fourier–Chebyshev bases).
  - Either verdict, certified for explicit data, is new-grade. The current numerical consensus - smooth ramps, no finite-time singularity in the line-tied smooth case (verify against Zhou–Huang–Qin–Bhattacharjee-type studies) - makes certified *existence* the likelier outcome; report whichever is proved.
- **P3 - Topology-forced discontinuity theorems for explicit classes.**
  - Deliverable: for an explicit discrete braided class (e.g., pigtail-braid flux-tube data), a proof that every topology-preserving force-free (or MHS) state has current concentration bounded below - a quantified obstruction.
  - Method: certified magnetic-energy comparisons - interval FEM lower bounds for the constrained minimization against upper bounds from explicit smooth competitors, with the incompatibility explicit.
  - Shape of the theorem: "a smooth equilibrium in this class requires energy $\ge E_1$, but ideal relaxation from the data cannot exceed $E_0<E_1$", or a direct jump-formation bound; all constants certified.
  - Independent value: even a single explicit class with a certified obstruction upgrades Low-type qualitative arguments to quantitative theorems.
- **P4 - Certified relaxation dynamics in a reduced PDE.**
  - Deliverable: rigorous integration (CAPD-style, or a dissipative-truncation-plus-tail framework in the Zgliczyński tradition) of a magneto-frictional line-tied reduced model from explicit data - certified growth of $\|\nabla\times B\|_{L^\infty}$ by an explicit factor with certified topology preservation.
  - Stretch goal, high risk: a computer-assisted self-similar blowup or infinite-time sheet-formation certificate in the Chen–Hou methodological line. Even certified finite-factor growth is a first for this problem.
- **P5 - Parker theorem in finite codimension (strongest short of resolution).**
  - Deliverable: a genericity theorem inside an explicit infinite family - for a $d$-parameter Fourier-polynomial family of boundary shear data, prove that outside an explicit measure-zero (or codimension-$\ge1$ algebraic) subset, no smooth force-free equilibrium with the prescribed topology exists in the declared class; the exceptional set computed by elimination, the non-existence certified with P2 machinery.
  - This is "PW restricted to an explicit slice" - the honest maximal session outcome.

## 4. Known results and prior art

- Parker (1972), "Topological dissipation and the small-scale fields in turbulent gases"; Parker (1994), *Spontaneous Current Sheets in Magnetic Fields* - the conjecture and its coronal-heating (nanoflare) program.
- Contra: van Ballegooijen (1985) - perturbative construction of smooth equilibria near the uniform field; the ensuing dispute (Antiochos, Low, and others) is precisely a formulation dispute - dossier material.
- Model problems: Hahm–Kulsrud–Taylor (1985) - boundary-driven current-sheet formation at a resonant surface; Ng–Bhattacharjee (1998) - non-existence arguments for smooth 3D equilibria in reduced settings (verify exact scope); Longcope–Strauss (1994); Craig–Sneyd (2005); Zhou–Huang–Qin–Bhattacharjee (~2018–19) - line-tied HKT numerics indicating thinning without finite-time singularity (verify).
- Zweibel–Li (1987) - early rigorous-flavored analysis of current-sheet formation conditions in line-tied fields (verify exact claims).
- Topological analyses: B. C. Low (~2006–2015) - optical analogy and compression arguments for tangential discontinuities (verify individual claims; several are contested); Janse–Low (2009) and its critiques; Aly and Amari on force-free existence theory.
- Numerical corpus and reviews: Pontin–Hornig, "The Parker problem: existence of smooth force-free fields and coronal heating", Living Reviews in Solar Physics (~2020) (verify year) - the canonical survey of the strong numerical evidence and its limits.
- Rigorous adjacent results: Enciso–Peralta-Salas (~2016, ARMA) - Beltrami fields with nonconstant proportionality factor are rare (an overdetermination result; qualitative support for the scarcity of smooth force-free states); magnetic-relaxation PDE analysis: Moffatt (1985) program; Brenier (~2014) - topology-preserving relaxation formulations (verify); Beekie–Friedlander–Vicol (~2022–23) - analysis of Moffatt's magnetic relaxation equations (verify exact statements); Constantin–Pasqualotto (~2023) - force-free limits via Voigt-type regularization (verify). None of these decides PW or PS; each must be mapped onto the P1 lattice.
- Computer-assisted PDE methodology (imported): Zgliczyński's rigorous dissipative-PDE integration; van den Berg–Lessard radii polynomials; Chen–Hou certified self-similar blowup (~2022) - the methodological template for P4.
- Braided-field phenomenology (context for P3 class selection): Wilmot-Smith–Hornig–Pontin (~2009–2011) braiding experiments and topological-entropy measures of footpoint mappings (verify).

**Status as of mid-2026 - re-verify against current literature before starting the session.**

## 5. Attack plan

Single-workstation program; statement-first discipline throughout:

1. **Dossier first (P1).** No computation before the encodings are fixed: field-line map plus braiding data for $B_z>0$ slab fields, written as definitions with well-definedness and invariance lemmas. Worked examples in SymPy notebooks, in increasing order of topological content:
   - the uniform field ($F_B=\mathrm{id}$, trivial braiding) - the null test every encoding must pass;
   - a single shear layer (nontrivial $F_B$, trivial braiding);
   - HKT boundary data (resonant-surface topology);
   - a three-tube pigtail braid (trivial $F_B$ on the tube cores, nontrivial braiding) - the example that separates the field-line map from the braiding data and shows why both are needed.
   This is where the session earns the right to compute.
2. **Reduced-model certificates (P2, P5).**
   - Fourier–Chebyshev discretization of the 2.5D force-free system with explicit rational data.
   - Float Newton solves (SciPy) to locate candidate equilibria; then Arb-based radii-polynomial verification for existence, or interval infeasibility over compact truncated families with symbolic tail bounds for non-existence.
   - Elimination for the P5 exceptional sets: Gröbner bases (Singular/Macaulay2) on polynomial truncations, then certified transfer to the PDE statement.
   - The classic failure: an infeasibility certificate for a *truncated* system is not non-existence for the PDE without the tail lemma - the tail lemma is the theorem.
3. **Energy-bound machinery (P3).** Interval FEM lower bounds: conforming elements with certified quadrature (Arb) for constrained energy minimization over the braided class; explicit smooth competitors integrated symbolically for the upper bounds; braiding constraints imposed via certified winding-number functionals. Failure mode: the constraint set is the hard part - an unconstrained or under-constrained minimization proves nothing about Parker; every constraint's enforcement must be part of the certificate.
4. **Rigorous relaxation runs (P4).** Start with 1.5D/2.5D magneto-frictional truncations in the dissipative-tail framework; certified integration over moderate horizons; measure certified current growth. Budget: days per run on a single workstation; expect step-size collapse as layers thin - report the certified horizon honestly rather than extrapolating.
5. **Workstation sizing overall.** P1–P3 are symbol- and proof-heavy with negligible compute; P2 verification runs are minutes-to-hours per data point; only P4 consumes multi-day compute.
6. **Cross-cutting failure modes.**
   - Exponential thinning misread as singularity: never claim discontinuity from any finite-time computation without a blowup certificate.
   - Topology leakage in discretized relaxation: numerical reconnection destroys the very constraint the problem is about - certified topology preservation must be checked, not assumed.
   - Slab-vs-cylinder and periodic-vs-disk mismatches between cited results and session claims.
   - Overclaiming reduced-model verdicts as 3D statements.
   - Force-free vs. MHS drift: a theorem proved with $\nabla p\neq0$ available is a different theorem; keep the two tracks separate from the dossier onward.

## 6. Verification and auditability requirements

1. **Exact arithmetic.** All boundary data and family parameters rational; all certificates (radii polynomials, infeasibility bounds, FEM energy bounds, integration enclosures) in interval arithmetic with directed rounding (Arb/CAPD); floating-point PDE solves are exploration only and never enter a certificate.
2. **Independent verification.** Every existence or non-existence certificate is a self-contained file (basis, coefficients, bounds) consumed by a standalone checker written independently of the search code; dual implementations (Python/mpmath and C++/Arb) for the headline P2 and P3 artifacts; rigorous integrations cross-checked by a second run with different order and step parameters.
3. **Reproducibility.** All truncation orders, mesh and basis parameters, tolerance settings, CAS and library versions, and seeds recorded; SHA-256 manifest over the dossier, certificates, code, and environment lockfile.
4. **Preservation.** The dossier's rejected formulations, all failed certificate attempts (with the truncation at which they failed), and all relaxation trajectories are part of the record; contested literature claims are quoted with page-level pointers in the session notes, or marked unverified.
5. **Honest reporting.** The report opens with: section 2 standard met or not met - expected **not met**. Every result is tagged with its reading (PW/PS or reduced model), geometry, function class, and genericity notion; the words "current sheets form" may be used only for claims meeting the tangential-discontinuity definition of 1.2, and never for thinning numerics.
