# PROMPT FOR DIRECT PREDICTION OF EXCITED-STATE SURFACES AND CONICAL INTERSECTIONS

## Learned excited-state potentials with certified topology at nonadiabatic seams

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** A - closed-loop (on-machine verifier)
**Rank:** A-10 of 21
**Source:** chem/bio top-50 list #8, section A (electronic structure)
**Modes:** `[func]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Photochemistry - vision, photosynthesis, photovoltaics, photocatalysis, DNA photodamage - is governed by what happens when electronic states meet: excited-state potential energy surfaces, the nonadiabatic couplings between them, and the conical intersections (CIs) where surfaces touch and population transfers on femtosecond timescales. This is ground-state quantum chemistry's blind spot: the reference methods are expensive multireference calculations, and the geometry near a CI is genuinely hard (double-cone topology, a singular derivative coupling, and a geometric/Berry phase that flips wavefunction sign around the seam). Machine-learned excited-state potentials exist (SchNarc; Westermayr–Marquetand) and can fit surfaces, but faithfully capturing the *topology* of the intersection - not just interpolating energies - is unsolved in general. The **on-machine verifier** is the multireference reference method (CASSCF, CASPT2/XMS-CASPT2, MRCI) that the session itself runs to label geometries and to check predicted surfaces, couplings, and seam geometries. A crucial honesty note runs through this prompt: **the reference data is itself expensive and imperfect** - active-space choice, state averaging, and dynamic-correlation treatment all inject reference error that must be quantified, not assumed away. Anything short of the section-2 standard is reported as a partial result, never as a solution.

## 1. Exact problem statement

**Reference method (ground truth), with declared uncertainty.** For a molecule and a set of electronic states $\{|\Psi_I\rangle\}$, the reference is a fixed, documented multireference protocol:
- State-averaged CASSCF(n,m) with a *named, fixed* active space $(n\text{ electrons}, m\text{ orbitals})$ and state-averaging weights, followed by
- A dynamic-correlation correction: XMS-CASPT2 (or MS-CASPT2 / MRCI / NEVPT2), with a stated basis and, for CASPT2, a stated IPEA/level shift.
The reference yields, at geometry $R$: adiabatic energies $E_I(R)$, nonadiabatic derivative couplings $\mathbf{d}_{IJ}(R) = \langle \Psi_I | \nabla_R \Psi_J\rangle$, and (where used) diabatic states. The reference's *own* uncertainty - active-space sensitivity, basis, dynamic-correlation method - is measured by a documented convergence study and reported as a band, not ignored.

**Objects to learn.** A model $\{E_I^\theta(R), \mathbf{d}_{IJ}^\theta(R)\}$ (or an equivalent smooth diabatic Hamiltonian $\mathbf{H}^{\text{dia}}_\theta(R)$ whose eigenvalues/eigenvectors reproduce the adiabatic quantities). The diabatic formulation is preferred because it makes the surfaces and couplings smooth *through* the seam and encodes the double-cone and geometric phase automatically.

**Admissible class.** Smooth, symmetry-respecting models of the molecular geometry (equivariant descriptors), predicting either adiabatic energies+couplings or a diabatic potential matrix; permutationally invariant; defined over a stated configuration domain (a molecule or a reaction/relaxation region including the CI seam).

**Accuracy thresholds (numeric).**
- **Excited-state energies:** MAE $\le 0.1\,\mathrm{eV}$ (state to aim for; $\approx 2.3\,\mathrm{kcal/mol}$) on held-out geometries vs the reference, with the *energy gap* $E_J - E_I$ near the seam within $0.05\,\mathrm{eV}$.
- **Nonadiabatic couplings:** direction (unit vector) within a stated angular tolerance and magnitude within a stated relative error away from the singular region; the singularity at the seam is represented, not fit as a finite bump.
- **Conical-intersection geometry:** minimum-energy CI (MECI) geometry located within a stated RMSD (e.g. $0.05\,\text{\AA}$) of the reference MECI, with the correct branching-space vectors ($\mathbf{g}$ gradient-difference and $\mathbf{h}$ derivative-coupling) and the correct linear (not avoided) topology.
- **Geometric phase:** the wavefunction/diabatic model must reproduce the sign change (Berry phase $\pi$) around any loop enclosing the seam - a topological, binary check.

## 2. Resolution standard

Full resolution is a learned excited-state model for a stated molecular domain that meets *all* section-1 thresholds on a held-out geometry set including the CI seam region, reproduces the correct double-cone topology and geometric phase, and drives nonadiabatic dynamics (surface hopping or Ehrenfest) whose observables (excited-state lifetime, branching ratios, product quantum yields) match reference-based dynamics within a stated tolerance. The deliverable is the model, the reference calculations run, the seam-region held-out test, the topology/phase certificates, and the dynamics benchmark.

**Not accepted as resolution:**
- A model with low energy MAE *away* from the seam that fits the CI region as a smooth avoided crossing (wrong topology) - the double cone must be reproduced.
- Correct energies but a nonadiabatic coupling that misses the seam singularity or the geometric phase.
- A model validated on interpolated geometries near training points but not on a genuinely held-out region of the seam.
- Dynamics agreement in one observable (e.g. lifetime) while branching ratios or product yields disagree.
- Matching a *single-reference* excited-state method (TD-DFT, ADC(2), EOM-CCSD) near a CI and calling it validated - single-reference methods are themselves qualitatively wrong at many CIs (the reference must be multireference where multireference character is present).
- A claim of generality from one molecule.

**Benchmark-integrity clause.** The multireference verifier is *both* the strength and the weakest link. Named biases: (i) *Active-space dependence* - CASSCF/CASPT2 energies and even CI *existence/location* can shift with active-space choice and state-averaging weights; a model can match a *badly chosen* reference and be wrong. Guard: the reference active space is fixed and documented, its sensitivity quantified by a convergence study, and the reported model error is stated *relative to the reference band*, never as absolute truth. (ii) *IPEA/level-shift and basis dependence* of CASPT2. (iii) *Held-out leakage near the seam* - because seam geometries are rare and expensive, it is tempting to train and test on the same narrow seam sampling. Guard: a prospective held-out seam region (a portion of the seam, or a nearby reaction channel) whose reference labels are computed after the model is frozen. A model that matches its own imperfect reference is reported as "consistent with the reference (uncertainty band X)", never as "correct".

## 3. Graded partial-result targets

**P1 - Reproduce reference excited-state energies with a verified pipeline.** For a benchmark molecule (e.g. the CH$_2$NH$_2^+$ / methaniminium, or ethylene, or a small chromophore with a documented CI), reproduce state-averaged CASSCF and XMS-CASPT2 vertical excitations and a surface scan against published values, and quantify the active-space sensitivity band. *Certificate:* matching energies within the reference band; documented convergence study.

**P2 - Learned surfaces with certified error, including the seam region.** Fit $\{E_I^\theta, \mathbf d_{IJ}^\theta\}$ (or a diabatic $\mathbf H^{\text{dia}}_\theta$) and certify energy/coupling error on a held-out set *that includes seam-adjacent geometries*, reporting error as a function of distance to the seam. *Certificate:* held-out error CDF binned by seam distance; couplings compared to reference.

**P3 - Correct topology and geometric phase.** Demonstrate the model reproduces the linear double-cone topology at the MECI (correct $\mathbf g$/$\mathbf h$ branching vectors), locates the MECI within the RMSD tolerance, and yields Berry phase $\pi$ around the seam. *Certificate:* MECI RMSD to reference; branching-space vector overlaps; the binary geometric-phase loop integral.

**P4 - Nonadiabatic dynamics benchmark.** Run trajectory surface hopping (or Ehrenfest) on the learned surfaces and reproduce reference-based dynamics observables - excited-state population decay/lifetime, branching ratios, key product yields - within a stated tolerance, with statistical error bars from enough trajectories. *Certificate:* dynamics observables vs reference dynamics with matched initial conditions and converged trajectory counts.

**P5 - Transfer across a chemical family.** Extend a validated single-molecule model to a family (substituted chromophores, or a reaction series) with the thresholds still met on held-out members including their seams - explicitly short of universal photochemistry. *Certificate:* held-out family errors and topology checks.

## 4. Known results and prior art

- Yarkony (1996–) - theory of conical intersections, derivative couplings, and the geometric phase in molecular systems; branching-space ($\mathbf g$,$\mathbf h$) formalism.
- Domcke, Yarkony, Köppel (eds.) - *Conical Intersections* volumes; the diabatization and topology background.
- Levine & Martínez; Ben-Nun & Martínez - ab initio multiple spawning and CI-driven photochemistry.
- Westermayr & Marquetand (2019–2021) - machine learning for excited states; reviews and the SchNarc model (SchNet + nonadiabatic couplings). Westermayr, Gastegger, Marquetand - phase-corrected coupling learning.
- Dral and co-workers - ML potentials for excited states and nonadiabatic dynamics (MLatom, verify).
- Guan, Zhang, Guo, Yarkony (2019–) - neural-network diabatic potential matrices guaranteeing correct topology by construction; permutationally invariant diabatization.
- Shen, Yang and co-workers; Wang; and others on diabatic ML Hamiltonians (verify specific attributions).
- Reference methods/software: OpenMolcas (CASSCF/CASPT2/XMS-CASPT2, RASSCF), BAGEL (XMS-CASPT2 and analytic CI optimization, Shiozaki), Molpro (MRCI, CASPT2), COLUMBUS (MRCI, analytic couplings), PySCF (CASSCF, and interfaces). Surface-hopping/dynamics: SHARC (Marquetand, González), Newton-X, PyRAI2MD (verify).

*Status as of mid-2026 - re-verify against current literature before starting any session.*

## 5. Attack plan

**Reference/verifier layer.** Generate labels with **OpenMolcas** or **BAGEL** (state-averaged CASSCF then XMS-CASPT2), computing energies, analytic nonadiabatic couplings, and - with BAGEL - optimizing the reference MECI and branching-space vectors directly. Fix and document the active space and state-averaging; run the active-space/basis sensitivity study up front to establish the reference band. A single workstation handles small chromophores (active spaces up to $\sim (10,10)$–$(12,12)$) though CASPT2 gradients are the cost bottleneck.

**Model layer `[func]`.** Prefer a **diabatic** neural potential matrix $\mathbf H^{\text{dia}}_\theta(R)$ (symmetric, smooth) whose eigen-decomposition yields adiabatic energies and couplings - this builds in the double-cone and geometric phase by construction (Guan–Yarkony-style). Use an equivariant/invariant descriptor (SchNet-class or MACE-class backbone in PyTorch, one prosumer GPU). Train to energies *and* couplings (or to diabatic matrix elements from a reference diabatization), with phase-consistency handling for the sign ambiguity of adiabatic couplings.

**Topology/phase layer.** After training, locate the model's MECI by constrained optimization, extract $\mathbf g$/$\mathbf h$, and compute the loop integral of the derivative coupling (or the diabatic-eigenvector sign) around a small circuit enclosing the seam to check Berry phase $\pi$.

**Dynamics layer.** Drive **SHARC** or a surface-hopping implementation with the learned surfaces; match initial conditions (Wigner sampling) to reference dynamics; converge trajectory count for the reported observables.

**Expected failure modes.** (i) The reference itself moves the CI when the active space changes - mistaken for model error. (ii) Adiabatic coupling sign/phase inconsistency across geometries corrupts training - diabatic formulation avoids it. (iii) Smoothing over the cusp: a naive energy-MAE loss rewards fitting the CI as an avoided crossing. (iv) Sparse seam sampling → good interpolation, wrong extrapolation onto held-out seam. (v) CASPT2 gradient cost limiting data volume; active learning near the seam is essential.

## 6. Verification and auditability requirements

1. **Exact or certified numerics.** Reference energies/couplings are converged (documented thresholds) with a quantified active-space/basis uncertainty band; model errors are held-out and reported relative to that band. Topology (double cone) and geometric phase ($\pi$) are checked as explicit computed quantities, not asserted. Dynamics observables carry trajectory-count error bars.
2. **Independent verification.** A standalone evaluator - separate from training - recomputes energy/coupling errors, re-locates the MECI, and re-evaluates the geometric-phase loop; a subset of reference points is recomputed with a second multireference code (OpenMolcas vs BAGEL vs Molpro) to bound reference error.
3. **Reproducibility.** Active space, state-averaging weights, basis, IPEA/level shift, geometry sampling, held-out seam split (frozen before evaluation), model version/hash, and dynamics initial conditions are recorded; SHA-256 manifest over all artifacts.
4. **Preservation.** Training code, reference inputs, MECI-optimization and phase-check scripts, and dynamics setups are part of the record. Anything not preserved is stated explicitly.
5. **Honest reporting.** The report states up front whether the topology/phase and dynamics standards were met, reports the reference uncertainty band alongside every model error, distinguishes "consistent with the (imperfect) reference" from "correct", reports held-out seam-region performance separately, and never presents smooth-region energy accuracy as capturing the intersection.
