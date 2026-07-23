# PROMPT FOR THE KELVIN PROBLEM: THE OPTIMAL UNIT-VOLUME PARTITION OF SPACE

## Minimal average interface area in equal-volume foams, building on the institute's 2026 Kelvin audit

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 37 of 50 (Tier 3)
**Source:** top-50 list #44, category F (fluids, plasmas, continuum)
**Modes:** `[search]` `[bound]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The Kelvin problem asks for the partition of $\mathbb R^3$ into unit-volume cells minimizing average interface area. Kelvin's 1887 tetrakaidecahedral foam stood until Weaire–Phelan (1994) beat it by about $0.3\%$; no better partition has been found since, and no nontrivial global lower bound certifies how close Weaire–Phelan is to optimal. The problem combines a machine-drivable search space (periodic candidate topologies, relaxable in Surface Evolver) with a certifiable bounding program (exact polyhedral competitors, quantitative isoperimetry, calibration duals) - hence the `[search]` and `[bound]` modes. **This prompt builds directly on institute prior art**: the 21 July 2026 audit dossier at `research/frontier-atlas/mathematics/11_kelvin_weaire_phelan_optimizer/01_baseline/kelvin_audit_artifacts/` (frustration-gap theorem, exact flat-A15 competitor, calibration no-go theorem, finite-defect invariance), whose conclusions are the adopted starting frontier below. The complete resolution defined in section 2 is the target; every lesser product - including any new record partition - is a partial result under section 3 and must never be represented as a solution.

## 1. Exact problem statement

### 1.1 Admissible class and functional (institute normalization)

An **admissible partition** $E=(E_i)_{i\in\mathbb N}$ is a locally finite Caccioppoli partition of $\mathbb R^3$ into cells of volume exactly $1$:
\[
|E_i|=1,\qquad |E_i\cap E_j|=0\ (i\ne j),\qquad \Bigl|\mathbb R^3\setminus\bigcup_i E_i\Bigr|=0,
\]
with locally finite perimeter. Let $J_E$ denote the interface (the union of the reduced boundaries) and $Q_R=[-R/2,R/2]^3$. Define the **mean interface density** and the Kelvin constant
\[
\mathcal A(E):=\limsup_{R\to\infty}\frac{2\,\mathcal H^2(J_E\cap Q_R)}{R^3},
\qquad
\kappa_3:=\inf_E\ \mathcal A(E).
\]
The factor $2$ counts the full boundary contribution of each cell (each interface separates two cells), matching the audit dossier and, after conversion, the Kusner–Sullivan convention. In this normalization a single unit ball has cost
\[
(36\pi)^{1/3}=4.835975862049408\ldots
\]

**Finite-defect invariance (dossier, §6).** $\mathcal A$ is unchanged by any bounded-region modification, so $\mathcal A$-optimality alone implies neither local minimality nor Plateau regularity. Structural claims therefore use the **ground-state condition (GS)**: no compactly supported volume-preserving perturbation strictly lowers the (unnormalized) perimeter.

**The problem adopted here:** determine $\kappa_3$, and identify a GS partition attaining it.

### 1.2 Adopted starting frontier (institute prior art - to be independently re-verified, not assumed)

From `kelvin_partial_resolution_dossier.md`:

1. **Frustration gap:** there exists $\varepsilon_3>0$ with
   \[
   \kappa_3\ \ge\ (36\pi)^{1/3}+\varepsilon_3
   \]
   (proof via sharp quantitative isoperimetry plus the Kepler theorem; no numerical value of $\varepsilon_3$ extracted).
2. **Exact flat A15 competitor:** the equal-volume periodic Laguerre A15 partition has exact cost
   \[
   \mathcal A_{\mathrm{A15,flat}}=\frac32+\frac{3\sqrt6}{2}+\frac{6\sqrt5-4\sqrt6-3}{2\sqrt[3]{16}}=5.296950417263704\ldots,
   \]
   and it is non-stationary at its triple edges, whence the strict bound $\kappa_3<5.296950417263705$.
3. **Calibration no-go:** on a closed flat torus with only prescribed phase volumes, every ordinary convex paired-calibration dual has value $\le0$; a positive global lower certificate must exclude the uniform fractional mixture (block boundary traces, integrality/topology constraints, or reduction to a finite integral class).
4. **Certified bracket:**
   \[
   4.835975862\ldots\ <\ \kappa_3\ <\ 5.296950417263705,
   \]
   the lower margin qualitative, not numerical.

Classical reference values (mostly **uncertified**):

- flat Kelvin (truncated octahedron, planar faces), exact: $(6+12\sqrt3)\,(8\sqrt2)^{-2/3}=5.31474\ldots$;
- relaxed (curved) Kelvin $\approx5.306$ and relaxed Weaire–Phelan $\approx5.288$, per Surface Evolver computations (Kusner–Sullivan 1996; Brakke) - floating-point values, not enclosures.

### 1.3 Open questions

- (Q1) Determine $\kappa_3$.
- (Q2) Is the relaxed Weaire–Phelan foam a GS optimizer?
- (Q3) Produce any certified lower bound numerically above $(36\pi)^{1/3}$, and any certified upper bound at or below the flat-A15 value.

## 2. Complete-resolution standard

A complete resolution consists of **all** of the following (this is the dossier's five-item remaining-gap list, adopted verbatim as the standard):

1. A rigorous existence/definition theorem for the candidate optimizer (e.g., the relaxed Weaire–Phelan foam as a GS periodic partition) in the admissible class of 1.1.
2. A certified two-sided enclosure of its cost $\mathcal A(E^\ast)$, including lattice, volume-constraint, curvature, Plateau-angle, topology, and discretization error control.
3. A matching universal lower bound $\kappa_3\ge\mathcal A(E^\ast)$ valid for the full admissible class - necessarily integrality-sensitive, per the no-go theorem.
4. A theorem connecting finite-torus or block certificates to the unrestricted functional $\mathcal A$ (thermodynamic-limit link).
5. An equality analysis compatible with finite-defect invariance (uniqueness modulo zero-density defects, or the appropriate GS classification).

**Not accepted as resolution:**

- Surface Evolver (or any floating-point) area values, including the classical $5.288$ decimal, presented as certified.
- Optimality within a fixed combinatorial type, within Laguerre/polyhedral classes, or among a finite candidate list, presented as global optimality.
- Torus-periodic optimality without the limit theorem of item 4.
- The 1994 Weaire–Phelan comparison itself (an upper-bound improvement, not a resolution), or any new record partition without a matching lower bound.
- Restatements of the sphere bound $(36\pi)^{1/3}$, or of the dossier's qualitative gap, without new quantitative content.
- Structural claims (Plateau angles, uniqueness, regularity) derived from $\mathcal A$-optimality alone, in violation of finite-defect invariance.

## 3. Graded partial-result targets

- **P1 - Frontier reproduction with our own verified toolchain.**
  - (a) Independently re-derive and re-run the dossier's exact flat-A15 certificate (`verify_flat_a15.py`, `flat_a15_candidate.json`); the re-derivation must be an independent implementation, not a re-execution.
  - (b) Produce the analogous exact symbolic certificate for flat Kelvin ($5.31474\ldots$) and for at least one further flat TCP competitor (e.g., C15).
  - (c) Reproduce uncertified Evolver relaxations of Kelvin ($\approx5.306$) and Weaire–Phelan ($\approx5.288$) with a scripted, hash-logged pipeline and Richardson-extrapolation error estimates, labeled non-rigorous.
  - Certificate: SymPy/Sage exact scripts plus an independent checker; Evolver runs reproducible bit-for-bit in inputs.
- **P2 - Certified upper bound strictly below flat A15.**
  - Make the dossier's strict-descent argument quantitative: an explicit finite-dimensional perturbation family of the flat A15 partition (piecewise-polynomial interface patches near the non-Plateau triple edges, volume errors cancelled by the dossier's face-patch variations), with the area decrease and exact volume restoration certified by symbolic/interval computation.
  - Product: $\kappa_3\le5.296950417263705-\delta$ with explicit $\delta>0$.
  - Stronger version: a certified enclosure for a curved WP-type competitor via interval-arithmetic area quadrature on an explicit spline foam with exactly constrained volumes. An upper bound needs only an admissible competitor - that is what makes it certifiable. Target $\kappa_3\le5.29$; stretch target $\le5.289$.
- **P3 - Systematic candidate search (machine-enumerable).**
  - Enumerate periodic weighted-point (Laguerre) seeds: all TCP/Frank–Kasper types with $\le16$ cells per fundamental domain (A15, C14, C15, Z, $\sigma$, $\mu$, H, and hybrids), plus randomized weighted-Delaunay seeds and Gabbrielli-type PDE-generated seeds (verify literature).
  - Relax each in Surface Evolver under identical protocols; rank by extrapolated cost with error bars.
  - Certificate: the full pipeline plus manifest; any structure numerically beating Weaire–Phelan is a headline result, to be promoted immediately to P2-style certification.
- **P4 - Explicit frustration-gap constant.**
  - Chase constants through the dossier's gap proof: an explicit quantitative-isoperimetry constant $C_3$ (Fusco–Maggi–Pratelli 2008 is non-explicit; the mass-transport route of Figalli–Maggi–Pratelli 2010 admits explicit constants - verify the best available explicit $C_3$), the fragment-to-packing conversion, and Hales' Kepler density $\pi/\sqrt{18}$.
  - Product: a certified numerical $\varepsilon_3>0$ in $\kappa_3\ge(36\pi)^{1/3}+\varepsilon_3$.
  - Honest calibration: the first explicit $\varepsilon_3$ may be minuscule ($10^{-10}$ or smaller); it is still the first numerical improvement over the sphere bound and directly discharges the dossier's stated limitation.
- **P5 - Boundary-conditioned block certificate (the dossier's named highest-value experiment).**
  - Construct a paired calibration on a cube with fixed phase traces compatible with A15/WP, certified by SOS/interval verification of the pointwise constraints; prove a quantitative penalty for incompatible traces; tile or average to a lower bound for $\kappa_3$.
  - Any certified lower bound $\ge4.9$ would dwarf P4; intermediate values are still valuable and reportable.
- **P6 - Strongest short of resolution.**
  - Certified GS local minimality of the relaxed Weaire–Phelan foam within its combinatorial type (second-variation eigenvalue enclosures on the relaxed foam), combined with a P5 lower bound within $1\%$ of the P2 upper bound.
  - This would bracket $\kappa_3$ tightly and make Q2 precise without resolving Q1; it must be reported exactly so.

## 4. Known results and prior art

- W. Thomson (Kelvin) (1887): tetrakaidecahedral foam. Weaire–Phelan (1994): A15-based foam, $\approx0.3\%$ better. Kusner–Sullivan (1996): careful comparison and exact polyhedral values. Brakke (1992): Surface Evolver.
- J. Taylor (1976): classification of soap-film singularities (Plateau borders, tetrahedral corners) for area-minimizing sets - the regularity backdrop for curved candidates.
- Hales (2001): 2D honeycomb theorem - the methodological template for any 3D lower-bound program. Hales (1998/2005; Flyspeck 2017): Kepler conjecture, an input to the dossier's gap theorem.
- Quantitative isoperimetry: Fusco–Maggi–Pratelli (2008); Figalli–Maggi–Pratelli (2010) - the explicit-constant route (verify best current explicit $C_3$).
- Lower bounds for related problems: Choe (1989) on minimal fundamental domains (verify exact scope; its applicability to $\kappa_3$ is limited). No numerical lower bound above $(36\pi)^{1/3}$ is published for $\kappa_3$ itself (verify).
- Calibration methods: Lawlor–Morgan (1994), paired calibrations; Fischer–Hensel–Laux–Simon (arXiv:2212.11840), local paired calibrations for interface functionals; Cesaroni–Novaga (~2022–2024), minimal periodic foams with equal cells and with fixed inradius.
- Candidate sources: Frank–Kasper phases (1958–59) as the TCP catalogue; Gabbrielli (~2009), counterexample-generation via a Swift–Hohenberg-type PDE (verify); foam numerics by Cox, Graner, and coworkers; Sullivan's surveys on bubbles and foams (~1998).
- **Institute prior art (adopted frontier):** Piatra Kelvin audit, 21 July 2026 - `research/frontier-atlas/mathematics/11_kelvin_weaire_phelan_optimizer/01_baseline/kelvin_audit_artifacts/` containing `kelvin_partial_resolution_dossier.md`, `verify_flat_a15.py`, `flat_a15_candidate.json`, `README_kelvin_audit.md`: the frustration gap, exact flat A15, calibration no-go, finite-defect invariance, and the five-item remaining-gap list reproduced as section 2.

**Status as of mid-2026 - re-verify against current literature before starting the session.**

## 5. Attack plan

Single-workstation program:

1. **`[search]` Evolver pipeline (P1c, P3).** Surface Evolver with scripted refinement schedules (quadratic model, conjugate gradient plus Hessian steps, mesh grooming), identical protocols across candidates; per-cell volumes constrained exactly; cost extrapolated in mesh size with error estimates. Seeds from CGAL periodic weighted-Delaunay/Laguerre tessellations; TCP site data from crystallographic tables. Each candidate: minutes to hours; the full $\le16$-cell TCP sweep: days.
2. **`[bound]` Exact polyhedral layer (P1a, P1b).** SymPy/SageMath exact radical arithmetic for flat competitors: cell volumes and face areas as symbolic polyhedral integrals; equal-volume weight equations solved exactly (the dossier's A15 cubic $64\delta^3-240\delta^2+300\delta+3=0$ is the model case). Independent numerical reconstruction (NumPy) as a cross-check only.
3. **Certified curved upper bound (P2).** Interfaces as piecewise-quadratic/cubic patches with exact rational control data; areas by degree-adaptive interval quadrature (Arb, directed rounding); volumes by exact divergence-theorem sums plus an interval-certified correction cell; triple-line neighborhoods handled by explicit local cone constructions with monotone area comparisons (excision lemmas proved symbolically).
4. **Explicit-gap constant chase (P4).** A literate constant-tracking document: every inequality's constant in $\mathbb Q$, machine-checked (SymPy plus Arb); output $\varepsilon_3$ as a single certified rational lower bound.
5. **Block calibration (P5).** Ansatz: polynomial vector fields on a cube, degree $\le8$; constraints $|\xi_i-\xi_j|\le1$ and divergence conditions imposed via SOS with exact rational rounding (SDPA-GMP exploration, FLINT verification); the trace-penalty lemma proved symbolically.
6. **Expected failure modes.**
   - Evolver converging to non-minimal critical points: perturb and re-anneal; report all basins.
   - Volume drift accumulating in long relaxations: re-project and log every projection.
   - Naive interval quadrature blowing up near curvature concentrations and triple lines: excise and bound; do not refine indefinitely.
   - Topology changes during relaxation invalidating a fixed combinatorial certificate: freeze and verify the combinatorial type at certification time.
   - The calibration no-go reappearing in disguise: any proposed global lower certificate must state explicitly which of the dossier's escape routes (§5 consequence list) it uses.

## 6. Verification and auditability requirements

1. **Exact arithmetic.** All flat-competitor values in exact radicals; all curved-competitor enclosures in Arb balls with directed rounding; all SOS/calibration certificates rounded to $\mathbb Q$ and re-verified exactly. Evolver floats are exploration only and must be labeled so in every table.
2. **Independent verification.** Each certificate (flat value, curved enclosure, gap constant, block calibration) re-checked by a standalone verifier written independently of the construction code; dual implementations (Python/SymPy and C++/Arb or FLINT) for the headline P2 and P5 artifacts. The institute's `verify_flat_a15.py` must be re-implemented, not merely re-run, for P1a.
3. **Reproducibility.** Evolver version, all `.fe` files, refinement scripts, seeds, and extrapolation code recorded; SHA-256 manifest over every artifact, including the inherited dossier files, so provenance from the 2026 audit is explicit.
4. **Preservation.** All candidate seeds and relaxation logs - including candidates that lost - are part of the record; the ranked table must list every structure attempted, not only the leaders.
5. **Honest reporting.** The report opens with: section 2 standard met or not met - expected **not met**. Results are labeled P1–P6; upper bounds, lower bounds, and uncertified numerics are kept in visibly separate tables; any structural claim states whether it assumes the GS condition.
