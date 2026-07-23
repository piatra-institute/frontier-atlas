# PROMPT FOR DESIGNING STEREOSELECTIVE ORGANOCATALYSTS AND CHIRAL LIGANDS

## Designing for enantioselectivity via the ΔΔG‡ of competing diastereomeric transition states

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** B - reality-gated (empirical verifier)
**Rank:** B-25 of 29
**Source:** chem/bio top-50 list #31, section D (design)
**Modes:** `[gen]` `[func]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Designing an organocatalyst or chiral ligand that delivers high enantioselectivity for a chosen asymmetric transformation is the **most compute-informed design problem in Pack B**, because the physical origin of selectivity - the free-energy difference \(\Delta\Delta G^{\ddagger}\) between the competing diastereomeric transition states - is directly computable by quantum chemistry (this half is Pack-A-like: an on-machine TS calculation). Yet the real deliverable, enantiomeric excess (ee), is a wet-lab measurement: synthesize the catalyst and substrate, run the reaction, and analyze by chiral chromatography. The problem is therefore reality-gated despite an unusually strong in-silico signal - a signal whose reliability is nonetheless capped by DFT functional/dispersion/solvation error and TS conformational sampling, where a ~1 kcal/mol error swings predicted ee across a wide range. The honest deliverable is a certified TS-modeling/descriptor method contribution, an improved held-out ee-prediction proxy, and a small ranked calibrated set of falsifiable catalyst designs - never a claimed resolution.

## 1. Exact problem statement

**Design target.** Given a specified asymmetric transformation (substrate class, bond formed, desired configuration) and a catalyst family (e.g. a chiral phosphoric acid, a bifunctional thiourea/squaramide organocatalyst, an amine catalyst, or a chiral metal–ligand complex), output catalyst structures predicted to deliver high ee for the target configuration.

**Success metric (the whole problem).**
- **Enantiomeric excess** \(\mathrm{ee}\) (target: high, e.g. \(\ge 90\%\), often \(\ge 95\%\)) for the intended enantiomer, measured by chiral HPLC/SFC/GC.
- The thermodynamic target behind it: \(\Delta\Delta G^{\ddagger}\) between the major- and minor-enantiomer-forming transition states, related (single dominant pathway, Curtin–Hammett) by

\[
\mathrm{ee} \approx \tanh\!\left(\frac{\Delta\Delta G^{\ddagger}}{2RT}\right),
\qquad \Delta\Delta G^{\ddagger}\gtrsim 2\text{–}3\ \mathrm{kcal/mol}\ \text{for}\ \ge 95\%\ \mathrm{ee}.
\]

- Plus yield/conversion, scope, and catalyst synthetic accessibility.

**Target class.** One transformation + one catalyst family per campaign. The claim is per-reaction; generality is not assumed.

**The in-silico-scorable sub-question (the strong half).** \(\Delta\Delta G^{\ddagger}\) is computable: locate the competing diastereomeric TSs (DFT, with conformer sampling), take the Boltzmann-weighted energy gap, and predict ee. Complementarily, multivariate descriptor / linear-free-energy-relationship (LFER) models (Sterimol sterics, NBO/electronic parameters, vibrational frequencies) predict ee within a scaffold from measured training data. **This is a genuinely strong in-silico signal - far stronger than docking is for binders - but it is not ee.** Its reliability is bounded by: DFT error on relative TS energies (functional, dispersion, implicit-solvent, and basis) that easily reaches or exceeds the ~1 kcal/mol separating 90% from 99% ee; incomplete TS conformational sampling; and, for descriptor models, interpolation only within the trained scaffold. The design-versus-measurement gap is therefore narrower here than elsewhere in Pack B, but real.

## 2. Verifier and data

**In-silico oracles and filters (and their known unreliability).**
- **DFT transition-state modeling of diastereomeric TSs** - the primary oracle. *Unreliable because* relative TS energies carry functional/dispersion/solvation error near or above the kcal/mol that separates good from excellent ee; predicted ee is exponentially sensitive to \(\Delta\Delta G^{\ddagger}\); TS conformer ensembles are often under-sampled; and the assumed mechanism/rate-determining step may be wrong. High-level single points (e.g. DLPNO-CCSD(T)) tighten but do not eliminate the error.
- **Multivariate descriptor / LFER models (Sigman-style)** - Sterimol, charges, IR frequencies regressed against measured ee. *Unreliable because* they interpolate within a scaffold and training range and extrapolate poorly to new catalyst cores or substrates; they encode, not explain, and inherit training-data noise.
- **ML on catalyst descriptors** (including learned representations, ligand descriptor libraries). *Unreliable because* data are scarce and scaffold-clustered; distribution shift to novel catalysts is severe.
- **Generative catalyst design.** *Unreliable because* generated catalysts must still be synthesizable and their ee must still be computed/measured - generation does not supply selectivity.

**Frozen benchmark / precedent set.** Fixed sets committed before modeling: datasets of catalysts/substrates with *measured* ee for the target reaction family (e.g. published chiral-phosphoric-acid or thiourea selectivity datasets, verify), and a set with both measured ee and published DFT \(\Delta\Delta G^{\ddagger}\) to calibrate the TS method's own error. Reproducing the correlation between computed \(\Delta\Delta G^{\ddagger}\) (and descriptor-model predictions) and measured ee is the leakage-controlled baseline. Scaffold-based splits are essential - random splits leak within a scaffold and flatter the models.

**Wet-lab gate (mandatory).** ee cannot be established without new physical experiments: synthesis of the catalyst (often multi-step and enantiopure) and substrate, running the reaction under specified conditions, and chiral analysis (chiral HPLC/SFC/GC), with conversion/yield controls. Rough cost: synthesizing a novel chiral catalyst can be a multi-step campaign costing thousands of dollars and weeks per catalyst (some routes fail); reaction screening + chiral analysis per catalyst/substrate pair is a further defined cost. **This line is not optional and must not be softened: a computed \(\Delta\Delta G^{\ddagger}\), however careful, is a hypothesis about ee, not a measured ee.**

## 3. Standard of a genuine advance

A genuine advance is one of: (a) a **certified method contribution** - a TS-modeling or descriptor/ML pipeline that predicts measured ee on the frozen set better than a named baseline under a proper scaffold split, reproduced independently, with its error honestly bounded; (b) an **improved held-out ee-prediction proxy** - a model that predicts ee for catalysts/substrates outside its training scaffold better than prior work, validated on a scaffold-held-out split; or (c) the top target: a **small, ranked, calibrated, synthesizable, falsifiable catalyst design set** for one specified transformation, each catalyst carrying a computed \(\Delta\Delta G^{\ddagger}\) with an error bound, a calibrated predicted-ee interval, and a synthetic route, handed to a wet-lab partner with pre-registered success criteria.

**Not accepted as resolution.**
- A computed \(\Delta\Delta G^{\ddagger}\) or predicted ee presented as the reaction's ee. Computed selectivity is a hypothesis; only chiral analysis of the real reaction decides.
- A descriptor/ML ee prediction validated only under a **random split** (within-scaffold leakage) presented as predictive for new catalysts; scaffold-held-out validation is required.
- A predicted ee reported without an error bound that reflects the exponential sensitivity to \(\Delta\Delta G^{\ddagger}\) (a ±1 kcal/mol uncertainty spans a wide ee range and must be shown).
- A design whose catalyst has no credible synthesis, presented as a deliverable.
- A single successful catalyst from an unreported computational pool presented as a design success rate; the denominator must be stated.
- The strong in-silico signal treated as closing the loop - the TS calculation is Pack-A-like but the ee is still wet-gated.

## 4. Graded targets

**P1 - Reproduce a TS-modeling / descriptor pipeline's in-silico metrics.** Reproduce a published \(\Delta\Delta G^{\ddagger}\)-to-ee workflow (or a Sigman-style LFER model) on its reported dataset, matching the reported correlation and the TS energetics. *Certificate:* metrics within noise; committed code, geometries, and hashes.

**P2 - Certified ee prediction on the frozen set under a scaffold split.** Predict measured ee across the frozen precedent set better than a named baseline under a scaffold-held-out split, with an honestly bounded error (propagating the DFT/sampling uncertainty into the predicted ee). *Certificate:* frozen set, scaffold split fixed before scoring, independent recomputation.

**P3 - Improved held-out ee proxy for new catalysts/substrates.** Build a model predicting ee outside its training scaffold and validate on a scaffold withheld from construction; report the lift and calibration of the predicted-ee intervals. *Certificate:* held-out scaffold split fixed before scoring.

**P4 - A ranked, calibrated, synthesizable, falsifiable catalyst set (top target).** For one specified transformation, deliver ≤ 12 catalysts, ranked, each with a computed \(\Delta\Delta G^{\ddagger}\) and error bound, a calibrated predicted-ee interval, a synthetic route, and a pre-registered success criterion (e.g. "≥ 2 of the top 6, when made, give \(\ge 90\%\) ee of the predicted configuration"). *Certificate:* frozen design set + TS geometries + calibration model committed before any synthesis/assay; wet-lab partner named.

**P5 - Prospective wet-lab confirmation with honest calibration.** Only with a lab: the P4 set synthesized and run, reporting realized ee against the pre-registered criterion, the predicted-vs-measured ee calibration, and the sign accuracy (did the predicted major enantiomer match) - including, plainly, if per-catalyst real success was low. *Certificate:* raw chiral-analysis chromatograms, the frozen predictions predating them.

## 5. Known results and prior art

- Sigman multivariate LFER / parameterization: steric (Sterimol) and electronic descriptors regressed to predict ee (Sigman and co-workers, 2011–; Harper & Sigman; Reid & Sigman, 2019, Nature, ee prediction and extrapolation - verify).
- Denmark's ML for selectivity: chiral-phosphoric-acid-catalyzed reactions with a large descriptor set and ML (Denmark et al., 2019, Science - verify).
- TS-based selectivity prediction: Houk and Paton group DFT transition-state models rationalizing and predicting stereoselectivity; Q2MM quantum-guided molecular mechanics for TS force fields (Norrby and co-workers - verify).
- Ligand descriptor libraries: Kraken and related phosphine/ligand descriptor sets (Sigman, Sunoj, Aspuru-Guzik and co-workers, ~2022 - verify).
- The consistent finding: TS energetics give a genuinely predictive (Pack-A-like) signal for ee that is unusual in molecular design, but it is bounded by DFT/sampling error and is scaffold-local for descriptor models; general, prospective *design* of a new stereoselective catalyst that hits a target ee without empirical iteration remains open, and ee itself is only established in the lab.

*Status as of mid-2026 - re-verify against current literature before starting any session.*

## 6. Attack plan

**Datasets/inputs.** Pull the frozen ee dataset(s) for the target reaction family and a subset with published DFT \(\Delta\Delta G^{\ddagger}\) for method calibration. Fix a scaffold-based leakage-safe split (never random).

**TS-modeling layer `[func]` (the strong half).** DFT (a documented functional + dispersion + implicit solvent, with a validated basis) via ORCA / Gaussian / Psi4 to locate the competing diastereomeric TSs, with systematic conformer sampling (e.g. CREST/ORCA-based) and Boltzmann weighting; optional DLPNO-CCSD(T) single points on the shortlist to tighten \(\Delta\Delta G^{\ddagger}\). Propagate the method's calibrated error into a *predicted-ee interval*, not a point estimate. A single workstation handles organocatalyst-sized TSs; metal complexes stretch it and require care.

**Descriptor/ML layer `[func]` `[gen]`.** Compute Sterimol/electronic/vibrational descriptors (Morfeus, RDKit, DFT); fit and cross-validate LFER/ML ee models under scaffold splits; use a generator over the catalyst family for P4, gated by the TS/descriptor predictions and by synthesizability. RDKit + a retrosynthesis check for routes on deliverables.

**Failure modes to expect and report.** (i) *DFT error amplified by ee's exponential sensitivity* - a modest \(\Delta\Delta G^{\ddagger}\) error is a large ee error; always report the interval. (ii) *TS under-sampling / wrong mechanism* - missing conformers or the wrong rate-determining step invalidate the gap. (iii) *Scaffold-split leakage* - random splits inflate descriptor-model performance; enforce scaffold splits. (iv) *Synthesizability* - a computationally excellent catalyst that cannot be made is not a deliverable. (v) *Sign errors* - predicting the wrong major enantiomer; report sign accuracy explicitly.

## 7. Verification and auditability requirements

1. **Leakage-safe evaluation.** Scaffold-based splits (never random) are committed (hashed) before scoring; no tuning on the test scaffold. The denominator (catalysts computed, ranked, made, tested) is always reported.
2. **Calibrated uncertainty.** Every delivered catalyst carries a computed \(\Delta\Delta G^{\ddagger}\) with a method-calibrated error bound and a calibrated predicted-**ee interval** (reflecting the exponential sensitivity), plus a predicted major configuration; calibration is reported on held-out data. **Every design is a labeled hypothesis, not a measured ee.**
3. **Separation of in-silico from real validation.** Computed \(\Delta\Delta G^{\ddagger}\), descriptor predictions, and predicted-ee intervals are kept physically separate from any measured ee; no computed selectivity is presented as a measured ee - the strong in-silico signal does not close the loop.
4. **TS-method transparency.** The DFT recipe (functional, dispersion, solvent, basis, high-level corrections), the conformer-sampling protocol, and the calibrated method error are documented; the assumed mechanism/rate-determining step is stated and justified.
5. **Independent reproduction.** A standalone script recomputes all predictions from committed geometries, energies, descriptors, and model hashes; SHA-256 manifest over designs, TS structures, code, and (if any) assay data.
6. **Preservation.** TS geometries and energies, descriptor computations, model code, generator settings, and retrosynthesis outputs are part of the record. Anything not preserved is stated explicitly.
7. **Honest reporting.** The report states up front that the problem is reality-gated and NOT resolved despite an unusually strong (Pack-A-like) in-silico signal; that *per-catalyst real success rates are low* for prospective design; that predicted ee carries a wide interval from DFT/sampling error; and it never presents a computed \(\Delta\Delta G^{\ddagger}\) as a measured ee, nor a random-split model score as predictive for new catalysts.
