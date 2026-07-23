# PROMPT FOR THE SPACETIME PENROSE INEQUALITY

## Mass–area inequalities for asymptotically flat initial data with apparent horizons

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 43 of 50 (Tier 4)
**Source:** top-50 list #49, category H (classical gravitation)
**Modes:** `[proof]` `[bound]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The Penrose inequality asserts that asymptotically flat initial data containing an apparent horizon of area $A$ has ADM mass $m \ge \sqrt{A/16\pi}$ - a quantitative strengthening of the positive mass theorem and a consistency test of weak cosmic censorship. The Riemannian (time-symmetric) case is proven (Huisken–Ilmanen 2001 via inverse mean curvature flow; Bray 2001 via conformal flow), but the full spacetime case is open, with a genuine zoo of inequivalent formulations, counterexample-shaped warnings for the wrong horizon notions (Carrasco–Mars), and a long-running generalized-Jang program (Bray–Khuri). This is a Tier 4 problem: a full proof is far beyond a session, and the assignment is explicitly the graded ladder - a rigorous dossier of formulations, machine-verified model-case proofs, certified ODE/PDE analysis in symmetry classes, small new special-class theorems, and Lean infrastructure for the Riemannian argument. The complete resolution defined in section 2 is stated for the record; every session output will be a partial result and must be reported as such.

## 1. Exact problem statement

### 1.1 Initial data and mass

An initial data set is $(M^3, g, k)$: complete Riemannian 3-manifold $(M, g)$ with symmetric 2-tensor $k$, satisfying the constraint equations

\[
16\pi \mu = R_g + (\mathrm{tr}_g k)^2 - |k|_g^2, \qquad
8\pi J = \mathrm{div}_g \bigl( k - (\mathrm{tr}_g k)\, g \bigr),
\]

with the dominant energy condition (DEC) $\mu \ge |J|_g$. Asymptotic flatness (one end, standard decay: $g_{ij} = \delta_{ij} + O_2(|x|^{-1})$, $k_{ij} = O_1(|x|^{-2})$, with $\mu, J$ integrable) defines the ADM mass $m$.

### 1.2 Horizons

For a closed embedded surface $\Sigma \subset M$ with outward unit normal $\nu$ and mean curvature $H$ (convention: $H > 0$ for round spheres in flat space with outward $\nu$), the null expansions are

\[
\theta^\pm \;=\; H \pm \bigl( \mathrm{tr}_g k - k(\nu,\nu) \bigr).
\]

$\Sigma$ is a marginally outer trapped surface (MOTS) if $\theta^+ = 0$. An apparent horizon is an outermost MOTS. For time-symmetric data ($k = 0$), MOTS are minimal surfaces.

### 1.3 Adopted formulation and the version zoo

**Conjecture (spacetime Penrose inequality - minimal-area-enclosure form, adopted here).** Let $(M, g, k)$ be asymptotically flat initial data satisfying the DEC, with outermost MOTS $\mathcal{S}$, and let $A_{\min}(\mathcal{S})$ be the minimal area required to enclose $\mathcal{S}$. Then

\[
m \;\ge\; \sqrt{\frac{A_{\min}(\mathcal{S})}{16\pi}},
\]

with equality only for data embeddable in Schwarzschild.

Inequivalent circulating versions - the session must keep them separated at all times:

1. with $A(\mathcal{S})$ itself in place of $A_{\min}$ (delicate; failure modes known in spherically symmetric examples - Ben-Dov 2004 (verify exact content));
2. with "generalized apparent horizons" (proposed by Bray–Khuri; refuted by Carrasco–Mars ~2010 (verify));
3. Penrose's original null-shell version (1973);
4. the Riemannian case ($k = 0$, $\mathcal{S}$ outermost minimal): proven.

The open problem is the adopted formulation (and close DEC variants). No informal "mass is at least horizon size" phrasing is an acceptable target.

## 2. Complete-resolution standard

Complete resolution is one of:

1. A proof of the adopted formulation for all asymptotically flat, DEC initial data in dimension 3 (one end; multiple horizon components treated, or the single-component restriction stated in the theorem), at publication standard, with the equality case characterized or explicitly deferred.
2. A counterexample to the adopted formulation meeting the same standard of rigor: explicit data, DEC verified, horizon and $A_{\min}$ controlled, mass computed - with certified numerics wherever numbers are used.

**Not accepted as resolution:**

- Proofs of the Riemannian case, however streamlined (calibration only, cf. P2/P6).
- Spherically symmetric or other symmetry-restricted proofs presented as the general case.
- Perturbative statements (data near Schwarzschild) without uniform, explicit smallness control - and even with it, these are P4, not resolution.
- Jang-program conditional results ("the inequality holds if the coupled system admits a solution with properties X") presented as unconditional.
- The refuted generalized-horizon version, or any version-swapping between $A$ and $A_{\min}$ mid-argument.
- Numerical evidence of any kind as proof.

## 3. Graded partial-result targets

### P1 - Formulations dossier (the map of the battlefield)

- Precise statements of all circulating versions 1–4 of section 1.3, plus charged and higher-dimensional variants.
- A proved implication/independence diagram between the versions.
- The counterexample-shaped warnings (Carrasco–Mars; Ben-Dov) restated with verified hypotheses and an exact account of which versions they kill.
- *Certificate:* referee-grade document; every implication either proved in-line or cited to a specific verified statement; disagreements with the literature flagged.

### P2 - Model-case proofs, machine-verified

- Spherical symmetry: full proof of the spacetime inequality (Misner–Sharp mass monotonicity, Hayward-style argument), with all tensor computations machine-checked in SageManifolds/xAct and the key monotonicity reproduced symbolically.
- Riemannian case: verified symbolic reproduction of the Geroch monotonicity computation (Hawking mass under smooth IMCF); Bray and Huisken–Ilmanen statements documented at dossier level.
- Certified numerical stress tests: families of spherically symmetric data (explicit $\mu$, $J$ profiles) integrated with rigorous ODE methods (CAPD/Arb), confirming the adopted inequality with certified margins and exhibiting certified violations of the *wrong* versions from P1 - a machine-checkable artifact the literature lacks.
- *Certificate:* symbolic notebooks plus interval-ODE ledgers.

### P3 - Jang program in symmetry classes

- The Bray–Khuri generalized Jang system reduced under spherical symmetry (ODEs): rigorous existence/blow-up analysis with certified integration.
- Document exactly where the general-case coupling obstruction manifests in the reduced system.
- Extend to a wider cohomogeneity-one class if the reduction closes; modest new rigorous results are plausible here.
- *Certificate:* theorems plus validated phase-plane/ODE artifacts.

### P4 - Perturbative special class

- A certified proof for an explicit neighborhood of Schwarzschild data: quantitative implicit-function-theorem argument with all constants explicit and interval-verified.
- Statement shape: "for all data with $\|(g - g_{\mathrm{Schw}}, k)\|_{X} < \varepsilon_0$ (explicit $\varepsilon_0$, explicit norm $X$), the adopted inequality holds."
- Relation to null-case results near Schwarzschild (Alexakis ~2014 (verify)) documented.
- *Certificate:* theorem with explicit constants; interval ledger for the constants.

### P5 - New special-class theorem

- One genuinely new, fully proved class beyond the literature. Candidates: cohomogeneity-one data beyond spherical symmetry; graph-type spacetime data (spacetime analogues of Lam's Riemannian graph proof ~2010 (verify what exists)); axisymmetric maximal data with extra structure.
- Small is fine; complete is mandatory.
- *Certificate:* the theorem, plus machine-checked identities where the proof uses computation.

### P6 - Lean 4 infrastructure

- Statement-level formalization of asymptotically flat data, ADM mass (axiomatized interface), and Hawking mass.
- A complete formal proof of Geroch monotonicity in the rotationally symmetric (1D-reduced) case.
- A structured blueprint (named leaf lemmas plus their mathlib gaps) for the Huisken–Ilmanen weak-flow argument; the weak flow itself is far beyond current mathlib - the artifact must say so.
- *Certificate:* Lean sources checked by the kernel, with an axiom audit.

### P7 - Strongest short of resolution

- Any unconditional theorem strictly extending the known special-class frontier of the adopted formulation.

## 4. Known results and prior art

- Penrose 1973: the original heuristic and null-shell version; Geroch ~1973 and Jang–Wald 1977: Hawking-mass monotonicity under IMCF and the reduction idea.
- Huisken–Ilmanen 2001: Riemannian case via weak IMCF (largest horizon component); Bray 2001: full Riemannian case via conformal flow; Bray–Lee 2009: dimensions up to 7.
- Recent Riemannian re-proofs via potential theory: Agostiniani–Mazzieri–Oronzio and collaborators, ~2022 (p-harmonic and Green's-function methods) (verify).
- Spherical symmetry (spacetime case): Malec–Ó Murchadha 1994; Hayward 1996 (verify attributions for the definitive statement).
- Bray–Khuri ~2010–2011: generalized Jang equation program reducing the spacetime case to a coupled system; existence for the coupled system open; Han–Khuri on Jang-equation existence and blow-up (verify).
- Carrasco–Mars ~2010: counterexample to the generalized-apparent-horizon version (verify exact statement); Ben-Dov 2004: spherically symmetric warnings on horizon-area versions (verify).
- Null case: Ludvigsen–Vickers 1983 (argument with a known gap); later analyses (Sauter ~2008 (verify)); Alexakis ~2014: null-shell inequality near Schwarzschild (verify scope).
- Alaee–Khuri–Yau ~2019–2023: spacetime Penrose-type inequalities under additional hypotheses and quasi-local variants (verify exact statements and hypotheses - the most likely recently-moved frontier).
- Surveys and foundations: Mars 2009, "Present status of the Penrose inequality"; Dan Lee, *Geometric Relativity* (2019) for complete Riemannian-case proofs; MOTS theory: Andersson–Mars–Simon ~2005–2008.

Status as of mid-2026 - re-verify against current literature before starting the session.

## 5. Attack plan

Modes `[proof]` `[bound]`: the deliverables are theorems and certified inequalities; computation serves the proofs.

1. **Dossier first (P1).** Build the implication diagram as a structured document: each node a formal statement in section-1 notation; every arrow an in-line proof or a checked citation. Highest value per hour; de-risks everything downstream.
2. **Symbolic verification layer (P2).**
   - SageManifolds (Python) and xAct (Mathematica) in parallel for: the Misner–Sharp mass and its monotonicity in spherical symmetry; Geroch monotonicity $\frac{d}{dt} m_H \ge 0$ under smooth IMCF, with the full second-fundamental-form terms.
   - Two independent systems because sign conventions in $k$, $H$, $\theta^\pm$ are the dominant error source in this literature.
3. **Certified ODE layer (P2/P3).**
   - Spherically symmetric data families: the constraints become ODEs in $r$; integrate with CAPD (C++) or Taylor models over Arb.
   - Verify DEC pointwise in intervals; locate the outermost MOTS with certified root enclosures; compute $m$, $A$, and $A_{\min}$ with intervals; produce certified margins for the adopted inequality and certified violations for refuted versions.
   - Workstation-trivial per family; the value is the rigor.
4. **Jang reduction (P3).** Derive the spherically symmetric generalized-Jang ODE system symbolically (machine-checked); rigorous phase-plane analysis - equilibria, blow-up asymptotics at the MOTS (cylindrical blow-up expected; verify against Han–Khuri) - and certified shooting with CAPD.
5. **Lean 4 (P6).** Target mathlib honestly: Hawking mass on spheres of a rotationally symmetric metric as a 1D object; the reduced Geroch monotonicity as the formal centerpiece; maintain a gap ledger of missing mathlib prerequisites (second-fundamental-form API, Gauss–Bonnet on surfaces - check current state) rather than faking generality.

Expected failure modes: version confusion (name the formulation in every lemma); sign-convention drift in $\theta^\pm$ across sources (the dual-CAS layer exists to catch this); the Jang reduction mishandled at the horizon (it is singular exactly where it matters); Lean scope creep (the weak flow is out of reach and the blueprint must say so); overclaiming perturbative results without explicit norms and constants.

## 6. Verification and auditability requirements

1. **Exact arithmetic.** All certified numerical claims (data families, MOTS locations, masses, areas, margins) in interval/ball arithmetic with directed rounding (CAPD/Arb); symbolic claims reduced to CAS-verifiable identities; floating point exploratory only.
2. **Independent verification.** Every symbolic identity derived in two independent CAS (SageManifolds and xAct) from independently written notebooks; every interval-ODE result re-checked by a standalone checker reading stored enclosure data; Lean artifacts checked by the kernel and axiom-audited, with all axiomatized interfaces listed.
3. **Reproducibility.** All data-family parameters, integration tolerances, and CAS versions pinned and recorded; SHA-256 manifest over notebooks, enclosure ledgers, Lean sources, and the dossier.
4. **Preservation.** Abandoned proof attempts and failed reductions preserved with notes - in a Tier 4 problem the failure map is a primary deliverable; anything not preserved is declared.
5. **Honest reporting.** The report states up front that the spacetime Penrose inequality remains open (unless section 2 was genuinely met), classifies every result as dossier / reproduction / symmetry-class / perturbative / formalization, and never lets a special-class or conditional result masquerade as the conjecture.
