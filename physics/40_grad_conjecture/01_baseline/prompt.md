# PROMPT FOR GRAD'S CONJECTURE ON NON-SYMMETRIC MHD EQUILIBRIA

## Do smooth 3D magnetohydrostatic equilibria with nested toroidal flux surfaces require a symmetry?

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 40 of 50 (Tier 4)
**Source:** top-50 list #41, category F (fluids, plasmas, continuum)
**Modes:** `[proof]` `[bound]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Grad conjectured in 1967 that smooth, non-symmetric three-dimensional magnetohydrostatic (MHS) equilibria with continuously nested toroidal flux surfaces "essentially" do not exist: force balance $\nabla p=J\times B$ with a genuinely three-dimensional field is expected to force either a continuous symmetry, singular current structures, or the destruction of nested surfaces. The conjecture underpins stellarator physics - quasisymmetric configurations found numerically to machine precision (Landreman–Paul 2022) sit exactly on its edge - yet it has never been given a single agreed precise statement, let alone a proof. It is matched to current AI methods because its sharpest partial evidence is computational-symbolic: near-axis and near-surface expansions whose order-by-order solvability is a chain of exact linear-algebra and small-divisor computations that can be certified in exact arithmetic. This is a Tier 4 problem: pinning down THE statement is itself a graded target; the complete resolution defined in section 2 is unlikely in a session, and no formal expansion, numerical equilibrium, or restricted-class theorem may be represented as a solution.

## 1. Exact problem statement

### 1.1 The MHS system

Let $\Omega\subset\mathbb R^3$ be a bounded toroidal domain (diffeomorphic to a solid torus) with smooth boundary. The unknowns are the magnetic field $B$ and the pressure $p$:
\[
(\nabla\times B)\times B=\nabla p,
\qquad
\nabla\cdot B=0\ \ \text{in }\Omega,
\qquad
B\cdot n=0\ \ \text{on }\partial\Omega .
\]
Write $J=\nabla\times B$ for the current. Taking scalar products with $B$ and $J$ gives
\[
B\cdot\nabla p=0,
\qquad
J\cdot\nabla p=0 :
\]
pressure is constant along field lines and current lines.

**Nested-surface configuration.** A solution is *nested* on $\Omega$ if there is a smooth flux label $\psi$ with $\nabla\psi\neq0$ on $\Omega\setminus\gamma_0$ for a single closed curve $\gamma_0$ (the magnetic axis), whose level sets are tori shrinking to $\gamma_0$, with
\[
B\cdot\nabla\psi=0,\qquad p=P(\psi).
\]

**Symmetry.** A continuous **Euclidean symmetry** is a one-parameter isometry group (axial, translational, or helical) preserving $(B,p,\Omega)$. **Quasisymmetry** is the weaker, non-isometric field symmetry: in Boozer-type coordinates $|B|$ depends only on $\psi$ and a single helicity angle $M\theta-N\varphi$; adopt the Burby–Kallinikos–MacKay coordinate-free definition in-session and prove any equivalences used.

### 1.2 Inequivalent formulations (all must be tracked; G1 is adopted)

- **(G1) Analytic rigidity - adopted target.** If $(B,p)$ is a real-analytic nested MHS solution on $\Omega$ with $P'(\psi)\neq0$ on a dense open set of flux surfaces, then $(B,p,\Omega)$ admits a continuous Euclidean symmetry.
- **(G2) Smooth rigidity.** The same statement with $C^\infty$ replacing real-analytic. Expected harder, and possibly false as stated (flat spots, localized constructions).
- **(G3) Generic non-existence.** In a declared topology on boundary shapes (or external coil fields), the set admitting nested, nonconstant-pressure MHS solutions without symmetry is meager or null.
- **(G4) Quasisymmetric variant.** Exact quasisymmetric MHS solutions with nested surfaces and nonconstant pressure are exhausted by the known symmetric families - a precise "Grad conjecture for quasisymmetry".

Grad's own hedge "essentially" (his 1967 paper admits exceptional cases) is part of the problem: the formulation dossier (target P1) must state what exceptional set each formulation tolerates. Rotational-transform hypotheses may be added, but must be declared as hypotheses, never smuggled in.

**Rotational transform and small divisors.** On each flux surface $\{\psi=c\}$ the field-line flow has a well-defined rotational transform $\iota(\psi)$ (average poloidal turns per toroidal turn). Perturbative constructions and rigidity arguments meet divisors of the form
\[
m\,\iota(\psi)-n,\qquad (m,n)\in\mathbb Z^2\setminus\{0\},
\]
which vanish on rational surfaces; Diophantine conditions on $\iota$ ($|m\iota-n|\ge\gamma m^{-\sigma}$) are the standard taming hypothesis. Whether the conjecture's truth is sensitive to the $\iota$-profile (shear vs. constant, rational vs. Diophantine) is itself an open structural question the dossier must address.

### 1.3 What is *not* in question

- Axisymmetric and helically symmetric solutions exist in abundance (Grad–Shafranov theory).
- Vacuum and force-free Beltrami fields with chaotic or partially nested structure exist.
- Stepped-pressure weak solutions (pressure piecewise constant, current sheets at interfaces) exist (Bruno–Laurence).

The open question is **smooth, nonconstant pressure, nested, non-symmetric - all four simultaneously**.

### 1.4 Benchmark objects

Every computational target must anchor to explicit data:

- axisymmetric baseline: a Solov'ev-type Grad–Shafranov equilibrium with rational profile coefficients (exact closed form - the linearization point for P3/P6);
- non-symmetric probe: a rotating-ellipse boundary family with two shape parameters (the minimal genuinely 3D deformation);
- quasisymmetric probe: the Landreman–Paul precise-QA configuration, used strictly as an exploration benchmark for the near-axis ledger, never as evidence.

## 2. Complete-resolution standard

A complete resolution is **either**:

1. A proof of (G1), with all hypotheses - analyticity, nondegeneracy of $P$, rotational-transform conditions, axis regularity - stated exactly, and every computer-assisted step certified per section 6; **or**
2. A counterexample: a real-analytic (or $C^\infty$, thereby resolving G2 negatively) nested MHS solution with $P'\neq0$ on a dense open set and provably **no** continuous Euclidean symmetry - existence established by rigorous functional analysis or a certified computer-assisted proof (radii-polynomial/Newton–Kantorovich with interval bounds), not by numerics.

**Not accepted as resolution:**

- Numerical equilibria (VMEC, SPEC, DESC, GVEC output) at any precision - including quasisymmetry-to-$10^{-12}$ configurations - presented as existence or non-existence proofs.
- Formal near-axis or near-surface expansions without certified error control, presented as either construction or obstruction.
- Stepped-pressure or weak solutions (current sheets, pressure jumps) presented as smooth counterexamples; devil's-staircase pressure constructions presented as satisfying the $P'\neq0$ hypothesis.
- Theorems about a formulation other than the one claimed; the G1–G4 lattice must be respected in every claim.
- Rigidity theorems with undeclared smallness or perturbative hypotheses presented as global.
- Confinement phenomenology or stellarator-engineering arguments in any evidentiary role.

## 3. Graded partial-result targets

- **P1 - Formulation dossier (a contribution in itself).**
  - Deliverable: the precise statement lattice G1–G4 plus variants (with/without Diophantine transform conditions, with/without boundary, local vs. global), with proven implications and separations, and every major literature claim (Grad 1967; Bruno–Laurence; Constantin–Drivas–Ginsberg; Enciso–Luque–Peralta-Salas; Burby–Kallinikos–MacKay; Landreman–Paul) mapped onto the lattice with exact hypotheses quoted.
  - Certificate: the dossier itself, each implication proved, machine-checked where formalizable.
- **P2 - Certified near-axis obstruction ledger.**
  - Deliverable: the MHS near-axis expansion (Mercier/Garren–Boozer framework) implemented in exact arithmetic - at each order $r^k$ in distance from the axis, the linear system for the unknown Fourier coefficients, its rank, kernel, and solvability conditions computed over $\mathbb Q$ with a symbolic axis curve.
  - Milestone (a): reproduce, in certified form, the Garren–Boozer result that exact quasisymmetry generically over-determines at third order.
  - Milestone (b): the analogous certified order-by-order ledger for the *general* (non-quasisymmetric) nested-MHS expansion, identifying exactly where non-symmetric solvability fails or survives, resonance denominators included.
  - Certificate: exact-arithmetic notebooks plus independent rank re-computation.
- **P3 - Quantitative rigidity in perturbative regimes.**
  - Deliverable: a Constantin–Drivas–Ginsberg-type near-symmetry rigidity theorem reproduced with every constant explicit, then extended - a certified statement of the form "any nested analytic MHS solution within $\epsilon_0$ (explicit) of a nondegenerate axisymmetric one in a declared norm, with $P'\neq0$, is axisymmetric or satisfies explicit constraints", with $\epsilon_0$ certified via interval-verified spectral bounds on the linearized operator.
- **P4 - Certified non-existence in restricted classes.**
  - Deliverable: a theorem of the form "within an explicit finite-parameter or finite-Fourier class of candidate non-symmetric nested equilibria (declared truncation, exact coefficients), no solutions exist", proved by Gröbner-basis elimination or interval exhaustion over the compact parameter domain.
  - Quasisymmetric case (G4 restricted): extend Burby–Kallinikos–MacKay-style overdetermination into a certified elimination result for low mode numbers $(M,N)$.
- **P5 - Rigorous existence on the flexibility side.**
  - Deliverable: a certified computer-assisted existence proof (radii polynomials in Fourier–Chebyshev bases, interval coefficients) for a non-symmetric MHS object *adjacent* to the conjecture - a stepped-pressure Bruno–Laurence equilibrium with explicit bounds, or a non-symmetric vacuum/Beltrami field with certified nested surfaces (the KAM step certified).
  - Value: either outcome sharpens where the conjectured obstruction actually lives - in the pressure gradient, not in mere three-dimensionality.
- **P6 - Local Grad theorem (strongest short of resolution).**
  - Deliverable: a proof of G1 in a perturbative neighborhood - every analytic nested MHS solution with $P'\neq0$ and Diophantine rotational transform sufficiently close (explicit norm and radius) to *some* symmetric solution **is** symmetric - upgrading P3 from "constraints" to a genuine local dichotomy, with the closeness radius certified.

## 4. Known results and prior art

- Grad (1967), "Toroidal containment of a plasma" - the conjecture, with the "essentially" hedge. Grad–Rubin (1958) - equilibrium boundary-value formulations.
- Symmetric theory: the Grad–Shafranov equation (Grad–Rubin 1958; Shafranov 1958); Lortz (1970) - existence with reflection-type symmetry (verify exact scope); Mercier (1964) - near-axis expansions.
- 3D existence with singular structures: Bruno–Laurence (1996) - weak equilibria with stepped pressure near axisymmetry, current sheets at rational surfaces.
- Modern rigidity/flexibility: Constantin–Drivas–Ginsberg (~2021) - near-symmetry rigidity and flexibility-with-adapted-forces theorems (verify the exact statements of the two papers); Enciso–Luque–Peralta-Salas (~2023) - MHS equilibria with nonconstant (devil's-staircase-like) pressure in toroidal domains (verify precisely what pressure regularity and nondegeneracy are achieved - this is the closest existence result and must be mapped onto the G-lattice with care).
- Quasisymmetry: Boozer (1981) - coordinates; Garren–Boozer (1991) - near-axis overdetermination of exact quasisymmetry at third order; Burby–Kallinikos–MacKay (~2020) - coordinate-free characterization; Landreman–Sengupta (~2018–19) - near-axis construction machinery; Landreman–Paul (2022) - numerical quasisymmetry to machine precision; Rodríguez–Bhattacharjee (~2021) - weak quasisymmetry and anisotropic-pressure reformulations; Cardona–Duignan–Perrella and related geometric results (~2023–2025) (verify).
- Reviews: Helander (2014), "Theory of plasma confinement in non-axisymmetric magnetic fields"; recent stellarator-mathematics surveys (verify the current best).
- Numerical infrastructure (exploration only, never evidence): VMEC (Hirshman–Whitson 1983); SPEC stepped-pressure equilibria (Hudson and coworkers, ~2012); DESC (Dudt–Kolemen ~2020); near-axis codes in the Landreman school.
- Adjacent rigorous tools: KAM theory for divergence-free fields; Arnold's structure theorem for steady Euler flows - the hydrodynamic twin of nested MHS; Sengupta–Weitzner-type near-surface expansions (verify).

**Status as of mid-2026 - re-verify against current literature before starting the session.**

## 5. Attack plan

Single-workstation program; the problem is symbol-heavy, not flop-heavy:

1. **Exact near-axis engine (P2).** SageMath/SymPy implementation of the near-axis expansion in exact rational arithmetic:
   - axis curve with symbolic curvature and torsion Fourier coefficients;
   - per-order unknowns stored as sparse exact linear systems;
   - ranks and solvability conditions by fraction-free elimination (FLINT);
   - cross-checks of low orders against published Garren–Boozer and Landreman–Sengupta expansions (float comparison as sanity only);
   - a second, independent implementation of at least orders 1–3 (different coordinate convention) to catch convention errors - the near-axis literature has at least three incompatible sign/angle conventions in circulation.
   Cost: minutes per order through order ~4; combinatorial coefficient growth beyond order 6 - prune by truncating axis Fourier content and document the truncation.
2. **Elimination layer (P4).** Translate truncated equilibrium conditions into polynomial systems over $\mathbb Q$; Gröbner bases in Singular/Macaulay2 (grevlex, then elimination orders); where degrees explode, switch to interval exhaustion (Arb) over compact parameter boxes with certified infeasibility per box. Workstation budget: Gröbner runs are memory-bound - cap at 32 GB per run and record every abort.
3. **Exploration layer (never certification).** DESC/VMEC-style equilibrium solves and near-axis codes (pyQSC-type) may be used to locate promising parameter regions and to sanity-check the exact ledger - their output is quarantined from all certificates.
4. **Functional-analytic certificates (P3, P5, P6).** Radii-polynomial/Newton–Kantorovich arguments in Fourier–Chebyshev spaces with interval coefficients (Arb; CAPD only if an ODE reduction appears): bound the inverse of the linearized operator at an approximate solution and certify contraction - or certify non-contraction plus a degree-theoretic exclusion for non-existence. Small divisors from the rotational transform enter the norms explicitly; Diophantine hypotheses must appear in the certificate, not just the prose.
5. **Expected failure modes.**
   - Gauge and parametrization redundancy (coordinate re-labeling) producing spurious kernels: quotient by the symmetry/gauge tangent space before any rank claim - this is the classic error in expansion-based "proofs".
   - Claiming an obstruction from a truncated expansion: a solvability failure at order $k$ under truncation is a statement about the truncated system only; the certificate must say so.
   - Axis coordinate singularities: use regularized near-axis variables.
   - Conflating quasisymmetry with isometry anywhere in the chain.
   - Literature drift: the 2021–2026 rigidity papers have easily misquoted hypotheses; re-verify every statement against the source before building on it.

## 6. Verification and auditability requirements

1. **Exact arithmetic.** All expansion coefficients, ranks, kernels, and solvability conditions over $\mathbb Q$ (or explicit algebraic extensions) - never floating point; all functional-analytic constants as Arb balls with directed rounding. Numerical equilibria run for intuition are exploration only and never enter certificates.
2. **Independent verification.** Each order-$k$ ledger entry re-verified by an independently written rank/solvability checker (a second CAS, or fraction-free elimination in C++/FLINT); each radii-polynomial certificate re-checked by a standalone interval verifier consuming only the certificate file.
3. **Reproducibility.** CAS versions, variable orderings, Gröbner options, truncation parameters, and all symbolic notebooks recorded; SHA-256 manifest over ledgers, certificates, and environment.
4. **Preservation.** The full formulation dossier including rejected formulations, all failed elimination runs, and truncation-dependence studies are part of the record; every claim carries its truncation order on its face.
5. **Honest reporting.** The report opens with: section 2 standard met or not met - expected **not met**. Every result is tagged with its formulation (G1–G4 or declared variant), category (analytic/smooth), regime (global/perturbative/truncated), and whether it is an obstruction, a rigidity, or an existence statement. The phrase "Grad's conjecture is proved/refuted" may appear only if section 2 is met.
