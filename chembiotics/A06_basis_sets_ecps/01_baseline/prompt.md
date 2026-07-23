# PROMPT FOR OPTIMAL COMPACT GAUSSIAN BASIS SETS AND EFFECTIVE CORE POTENTIALS

## Systematic search-discovered basis sets and ECPs with certified energy/property accuracy per element

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** A - closed-loop (on-machine verifier)
**Rank:** A-06 of 21
**Source:** chem/bio top-50 list #7, section A (electronic structure)
**Modes:** `[gen]` `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Every molecular quantum-chemistry calculation begins by choosing a Gaussian basis set (and, for heavy elements, an effective core potential / pseudopotential). The community standard sets - Dunning's correlation-consistent cc-pVXZ, the Karlsruhe def2 family, the Pople sets - were built by decades of careful hand-optimization.

The question is whether *systematic search and optimization* can discover more compact bases (fewer primitives/contractions) that match a target accuracy for a target element set, or trace a better accuracy-vs-size Pareto front. This is the cleanest generative-search problem in Pack A: the objective is a **directly computable total energy or property error** against a near-exact reference (PySCF/Psi4 run on-machine), with exact ground truth and immediate downstream utility.

The **on-machine verifier** is the electronic-structure code itself - total energies, atomic/molecular properties, and their errors versus a fixed high-accuracy reference are computed exactly and deterministically. Anything short of the section-2 standard is reported as a partial result, never as a solution.

## 1. Exact problem statement

**Objects to optimize.**

- A **Gaussian basis set** for element $Z$: a set of primitive Gaussian exponents $\{\alpha_{i}\}$ (per angular momentum $\ell$) and contraction coefficients $\{c_{ij}\}$ grouping primitives into contracted basis functions, with a stated number of functions per shell (the "size").
- An **effective core potential (ECP)** for element $Z$: a number of removed core electrons $N_{\text{core}}$, a semilocal radial potential

\[
U_\ell(r) = \sum_k d_{k\ell}\, r^{\,n_{k\ell}}\, e^{-\zeta_{k\ell} r^2}
\]

per angular channel, and a matched valence basis; optionally spin–orbit ECP terms.

**Reference method (ground truth).** For each element/property the target is a fixed near-exact reference, one of:

- *Atomic total energies:* numerical (grid-based, basis-set-limit) Hartree–Fock or a named correlated method (e.g. a finite-element / numerical atomic solver), giving the complete-basis-set limit to which a Gaussian basis is compared.
- *Molecular energies/properties:* a very large reference basis (e.g. aug-cc-pV5Z or a decontracted even-tempered near-CBS set) at a fixed correlated level (CCSD(T) or MP2), computed on-machine as the reference.
- *Heavy elements:* for all-electron references, a documented relativistic Hamiltonian (X2C/DKH); ECP-derived results are compared to the matched all-electron relativistic reference.

**Property panel.** Total energy (Hartree), plus a stated property panel per use case - atomization energy, ionization potential, dipole moment/polarizability, equilibrium bond length, harmonic frequency - each with its own numeric tolerance and unit.

**Admissible class.** Contracted Gaussian bases of a stated size (contracted functions per $\ell$, and primitive count); real spherical-harmonic Gaussians; energy-consistent or shape-consistent ECPs of the standard semilocal form. Optimization variables: exponents, contraction coefficients, ECP parameters, and core size.

**Accuracy threshold (numeric, per target).** A target is "matched" only when written numerically, e.g.:

- Absolute atomic total-energy error $\le E_{\text{tol}}$ Hartree (state the number, e.g. $1\,\mathrm{mHartree}$).
- Relative energy (atomization, reaction) error $\le 1\,\mathrm{kcal/mol}$ vs the near-CBS reference.
- Property errors: bond length $\le 0.005\,\text{\AA}$, harmonic frequency $\le 10\,\mathrm{cm^{-1}}$, etc. - each stated.

"As accurate as cc-pVTZ" is admissible only as a *measured* per-target error distribution against the same reference, not as a label.

## 2. Resolution standard

The deliverable is a **discovered basis set and/or ECP**, given as an explicit parameter table, that meets a stated accuracy threshold for a stated element set and property panel *at a smaller size than the incumbent standard set*, with all errors certified by on-machine reference calculations, verified on a **held-out molecular test set** the basis was not optimized against.

For a Pareto claim, the deliverable is a set of bases tracing a front strictly dominating the incumbent sets in the (size, error) plane on the held-out set.

**Not accepted as resolution:**

- A basis that beats the incumbent only on the *atoms/molecules it was optimized on* (over-fitting to the training molecules) - transferability to a held-out molecular set is mandatory.
- Lower total energy alone presented as "better", ignoring the property panel (a basis can be variationally lower yet worse for properties).
- A smaller basis matching the reference on energies but silently worse on forces/geometries/polarizabilities not in the reported panel.
- An ECP that reproduces valence energetics for the fitting states but fails for other charge/spin states or in molecular environments (transferability across states is required).
- "Compact" claimed by counting contracted functions while the primitive count or integral cost is actually higher.

**Benchmark-integrity clause.** The verifier (a QM code computing energies against a fixed reference) is deterministic and clean but has named biases.

- *Variational bias.* Total energy is minimized by construction, so an optimizer can drive energy down while degrading properties. Guard: a mandatory property panel including at least one non-energy observable and one held-out molecule per element.
- *Molecule-selection bias.* Bases optimized on a narrow training molecule set transfer poorly. Guard: a frozen held-out molecular test set (different bonding environments) fixed before optimization, on which the final errors are reported.
- *Reference-method bias.* The "near-exact" reference is itself basis-truncated/method-limited; its own error (vs a still-larger basis, or vs numerical CBS for atoms) must be quantified and be smaller than the claimed tolerance.

## 3. Graded partial-result targets

**P1 - Reproduce a standard basis's accuracy with our pipeline.** Take cc-pVXZ / def2-XZVP for a set of elements and reproduce its published errors (atomic energies, a small molecular panel) against our own near-CBS reference, confirming the reference and toolchain. *Certificate:* our recomputed errors matching the standard set's known behavior; reference verified against numerical CBS for atoms.

**P2 - Match a target accuracy at smaller size for a target element set.** By systematic optimization, discover a basis with *fewer* contracted functions (or primitives, or lower integral cost - state which) than the incumbent that meets a stated tolerance on a held-out molecular panel for a named element set (e.g. first-row main group). *Certificate:* explicit basis table; held-out error distribution meeting tolerance; size/cost comparison to incumbent computed exactly.

**P3 - Pareto front of accuracy vs size.** Produce a family of bases tracing the (size, error) trade-off for a target element set and property, and show it strictly dominates the standard hierarchy on the held-out set. *Certificate:* the Pareto set with per-point held-out errors; dominance verified numerically.

**P4 - Transferable contraction schemes / ECPs.** Discover a general contraction rule (or an ECP + matched valence basis) that transfers across a row/block or across charge/spin states with certified accuracy on a held-out set spanning those states. *Certificate:* the scheme/ECP table; held-out errors across the transfer axis; ECP tested on states not used in the fit.

**P5 - Property-targeted or method-targeted bases.** Discover a compact basis optimized for a specific property (polarizability, NMR shielding) or a specific correlated method (explicitly-correlated F12, or a specific DFT functional), matching a much larger general basis's property accuracy at reduced cost, verified on held-out systems. *Certificate:* property-specific held-out error meeting tolerance vs the large-basis reference.

## 4. Known results and prior art

- Dunning (1989) - correlation-consistent cc-pVXZ basis sets; Woon & Dunning - augmented and core-valence variants.
- Weigend & Ahlrichs (2005) - Karlsruhe def2 basis sets (def2-SVP/TZVP/QZVP). Hehre, Pople et al. - the Pople 6-31G* family.
- Jensen (2001–) - polarization-consistent pc-$n$ basis sets optimized for DFT.
- Peterson and co-workers - cc-pVXZ-F12 basis sets for explicitly correlated methods.
- ECPs / pseudopotentials: Hay & Wadt (LANL); the Stuttgart/Cologne energy-consistent ECPs (Dolg, Stoll, Preuss; Peterson, Figgen, Dolg - small-core relativistic ECPs with matched cc-pVXZ-PP bases); shape-consistent ECPs (Christiansen; Ermler); correlation-consistent pseudopotentials (Burkatzki, Filippi, Dolg) for QMC.
- The Basis Set Exchange (Pritchard et al., 2019, and the earlier EMSL BSE) - the canonical repository of standard sets to compare against.
- Even-tempered and well-tempered basis generation (Raffenetti; Huzinaga) - systematic geometric-series exponent schemes, an early "search" precedent.
- Recent ML/optimization approaches to basis generation (verify): differentiable/gradient-based exponent optimization and ML-designed compact bases have appeared but are not yet standard - treat all specific recent claims as (verify).

*Status as of mid-2026 - re-verify against current literature before starting any session.*

## 5. Attack plan

**Reference/verifier layer.** Build atomic near-CBS references with a numerical atomic HF/DFT solver (or a Slater/finite-element atomic code) and molecular references with a very large Gaussian basis (aug-cc-pV5Z-class, decontracted even-tempered) at a fixed method in **PySCF** or **Psi4**. For heavy elements, use X2C or DKH relativistic all-electron references as the ECP ground truth. Quantify the reference's own truncation error first.

**Search/optimization layer `[gen]` `[search]`.** Two complementary engines:

- *Gradient-based* - implement basis energy/property as a differentiable function of exponents/coefficients (PySCF exposes integrals; analytic or autodiff exponent gradients) and optimize with L-BFGS.
- *Global search* - CMA-ES / Bayesian optimization / genetic search over exponent seeds and contraction patterns to escape local minima, since the basis landscape is highly non-convex.

Encode size as a hard constraint (fixed number of contracted functions per $\ell$). For ECPs, fit $U_\ell(r)$ parameters to reproduce reference valence orbital energies/shapes (energy-consistent objective) across multiple reference states simultaneously.

**Evaluation layer.** Every candidate is scored by an on-machine QM run: total energy and the full property panel on the *held-out* molecule set, not the fitting set. Multi-objective scoring (energy + properties + size) is handled by explicit Pareto tracking.

**Workstation scope.** Atomic and small-molecule references and thousands of candidate-basis evaluations run on one workstation; the bottleneck is the number of QM evaluations, not any single one. One prosumer GPU accelerates PySCF's GPU4PySCF integrals/SCF for the larger held-out molecules.

**Expected failure modes.**

- Linear dependence / near-redundant exponents making SCF ill-conditioned - enforce minimum exponent ratios.
- Variational over-fitting: energy improves, properties degrade - caught only by the property panel.
- ECP transferability collapse across states - fit and test on multiple states.
- Reference truncation error exceeding the claimed tolerance - quantify it first.
- A basis "smaller in contracted count but larger in primitive/integral cost" - report the actual cost metric.

## 6. Verification and auditability requirements

1. **Exact or certified numerics.** Every accuracy claim is a computed energy/property error against a fixed reference whose own truncation error is quantified and smaller than the claimed tolerance; SCF/correlation convergence thresholds are tightened and recorded so the error is not convergence noise. Sizes and integral costs are counted exactly.
2. **Independent verification.** A standalone script - separate from the optimizer - reads the discovered basis/ECP table, runs the held-out panel in a *second* code (PySCF vs Psi4), and reproduces every reported error; ECPs are re-tested on held-out states.
3. **Reproducibility.** The reference recipe, the held-out molecular test set (frozen before optimization), optimizer seeds/hyperparameters, code versions, and all convergence thresholds are recorded; SHA-256 manifest over the basis tables and results; the held-out split is committed before evaluation.
4. **Preservation.** Search/optimization code, candidate-evaluation logs, and reference-generation inputs are part of the record. Anything not preserved is stated explicitly.
5. **Honest reporting.** The report states up front whether a discovered basis/ECP beats the incumbent at smaller size on the *held-out* set, reports the full property panel (not just energy), states the actual size/cost metric used, and never presents fitting-set performance or a variational energy win as the result.
