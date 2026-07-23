# PROMPT FOR CONFORMATIONAL ENSEMBLES WITH CORRECT BOLTZMANN WEIGHTS

## Predicting the distribution, not the structure - certified against reference MD, cross-checked against experiment

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Pack:** A - closed-loop (on-machine verifier)  
**Rank:** A-13 of 21  
**Source:** chem/bio top-50 list #16, section C (beyond static structure prediction)  
**Modes:** `[struct]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

AlphaFold and its lineage largely solved single-domain static structure. The explicitly named next grand challenge is the **conformational ensemble**: the set of structures a flexible protein, loop, or disordered region visits *and the Boltzmann weight of each*. A structure predictor answers "the fold"; an ensemble predictor must answer "the distribution," which is a strictly harder object - averages, populations, and observables all depend on the weights, not just the members. This prompt keeps the on-machine verifier where it is exact: for a fixed Hamiltonian, **reference molecular dynamics defines the target ensemble and its Boltzmann-weighted observables**, and a generative ensemble predictor is judged by reproducing those ensemble averages. Experimental observables - NMR $J$-couplings and residual dipolar couplings (RDCs), NOEs, chemical shifts, SAXS profiles - are used as external cross-checks, but they are *partly reality-gated*: they confound predictor error with force-field error and with the forward-model (Karplus, CRYSOL) error, and are flagged as such throughout. The core sampling verifier is MD. The honesty spine: this is distribution prediction, sharply distinct from static structure prediction, and "correct weights" means correct for the chosen Hamiltonian, not automatically correct in reality. Anything short of section 2 is a partial result.

## 1. Exact problem statement

**System class.** Flexible and multi-state systems where a single structure is the wrong object: multi-basin folded proteins, flexible loops, and intrinsically disordered regions (IDRs) / disordered peptides short enough that a converged reference is attainable. Declared per run.

**Distinction from static structure prediction (mandatory).** The deliverable is not a coordinate set (or a top-$k$ list) but a *weighted ensemble*: a distribution $\rho(x)$ over configurations, or equivalently samples $\{x_i\}$ with weights $\{w_i\}$, such that ensemble averages $\langle O\rangle = \sum_i w_i O(x_i)$ are the predicted quantities. A method that outputs several plausible structures without calibrated weights does not address this problem.

**Hamiltonian and target (fixed and named).** A stated force field and (if explicit) water model - for disordered/flexible systems, an ensemble-appropriate force field such as a99SB-disp or CHARMM36m - define $U(x)$ and the target Boltzmann ensemble
$$
\rho(x) = Z^{-1} e^{-\beta U(x)}.
$$
The **reference ensemble** is a converged MD (or enhanced-sampling-reweighted) trajectory sampling $\rho$. Its Boltzmann-weighted observables $\langle O\rangle_\rho$ are the on-machine ground truth. Convergence of the reference (independent replicas agreeing, block-averaged errors) is a certified precondition.

**Observables.**
- *On-machine (MD-native):* per-residue secondary-structure populations, dihedral distributions, radius of gyration $R_g$ distribution, contact-map probabilities, macrostate populations, tertiary-contact free energies.
- *Experimental cross-checks (reality-gated, flagged):* scalar $J$-couplings via a stated Karplus relation, RDCs via an alignment model, NOE-derived distances, chemical shifts via a stated predictor (e.g. SPARTA+/ShiftX-type), SAXS $I(q)$ via a stated forward model (CRYSOL/FoXS). Each carries forward-model error that must be reported alongside.

**Generator (the object to be built).** A model producing an ensemble with usable weights: a flow / flow-matching / diffusion model over conformations, an MSA-subsampled structure-prediction ensemble, or a learned emulator of equilibrium ensembles - provided it yields either tractable densities for reweighting or a defensible weight assignment.

**Accuracy thresholds (numeric).**
- *Ensemble-average agreement (resolution metric).* Predicted Boltzmann-weighted observables match the converged reference within combined statistical error ($\le 2\sigma$) for on-machine observables; for scalar free energies (e.g. a helix–coil population free energy) within $0.5$ kcal/mol.
- *Weight-calibration.* The predicted weights, when used to compute a *held-out* observable not used in any fitting, reproduce the reference within error. Uncalibrated weights are a failure regardless of how good the member structures are.
- *Experimental cross-check (secondary, flagged).* Agreement with experimental observables is reported with the forward-model uncertainty propagated, and is never the sole basis of a resolution claim.

## 2. Resolution standard

A resolution, for a stated system and fixed Hamiltonian, consists of:

1. A generated **weighted ensemble** whose Boltzmann-weighted on-machine observables reproduce the converged reference within $2\sigma$ (and scalar free energies within $0.5$ kcal/mol), with reference convergence certified.
2. A passed **weight-correctness test**: held-out observables computed from the predicted weights agree with the reference within error; and, where the generator admits a density, an exact-reweighting check (as in the free-energy-sampling problem) reduces residual weight error.
3. Validation on a **held-out** system the generator was not trained on.
4. Experimental cross-checks reported for at least one system, with forward-model error propagated and labeled reality-gated.

**Not accepted as resolution:**

- An ensemble of plausible-looking structures with no weights, or with weights that fail the held-out observable test (the structures may be right and the *distribution* still wrong - this is the whole point).
- A method that reproduces the reference's *most populated* state (i.e. re-solves static structure) but not the minor-state populations and averages.
- Matching *experimental* observables while skipping the reference-MD comparison, or while hiding the forward-model error inside the fit.
- A single-system success presented as general ensemble prediction.
- Reweighting-to-experiment (BME / maximum-entropy) presented as *prediction* - bias-correcting an ensemble to fit data is a refinement, not a de novo prediction, and must be labeled as such.

**Benchmark-integrity clause.** Two verifiers, both flagged. (i) *Reference MD is exact for the Hamiltonian but only as good as its convergence*: disordered and multi-state systems are exactly those where MD converges slowly, so independent-replica agreement is mandatory before the reference is trusted, and the honest scope is systems small/fast enough to converge on a workstation. (ii) *Experimental observables are reality but triple-confounded* - predictor error, force-field error, and forward-model (Karplus/alignment/CRYSOL) error all enter the same number. A predictor "validated" against experiment through a compensating force-field error is confident-but-wrong on the next system. The guard: report the on-machine (reference-MD) metric as the resolution metric; report the experimental cross-check separately with forward-model uncertainty; use a frozen, hash-committed held-out system split; and never let experiment-fitting (reweighting to data) masquerade as prediction.

## 3. Graded partial-result targets

- **P1 - Reproduce an MD ensemble's observables with a generator.** On a small flexible peptide, train a conformational generator and reproduce the converged reference-MD dihedral and $R_g$ distributions with calibrated weights, within $2\sigma$. *Certificate:* the weighted ensemble, observable-by-observable comparison with error bars, reference-convergence evidence.
- **P2 - Certified ensemble-average agreement.** For a multi-basin system, reproduce macrostate populations and a scalar population free energy to $\le 0.5$ kcal/mol against a converged reference. *Certificate:* replica-agreement for the reference, predicted populations with bootstrap errors.
- **P3 - Boltzmann-weight correctness test.** Demonstrate that the predicted weights pass a held-out observable test and, where a density is available, an exact-reweighting reduction of residual error (link to the free-energy-sampling reweighting machinery). *Certificate:* held-out observable agreement, ESS if reweighted, and the weight-vs-uniform ablation showing the weights matter.
- **P4 - Ensemble prediction on a held-out target with calibrated weights.** Predict the weighted ensemble for a system the generator never saw; certify against that system's converged reference. *Certificate:* frozen split hash, held-out weighted observables within error.
- **P5 - Experimental cross-check with propagated forward-model error.** For at least one system, compare the predicted ensemble's $J$-couplings / RDCs / SAXS to experiment with the Karplus/alignment/CRYSOL uncertainty propagated, reported *separately* from the on-machine metric and labeled reality-gated. *Certificate:* forward-model definitions, error propagation, and the experiment-vs-prediction table with the force-field caveat stated.
- **P6 - Disordered-region ensemble.** Strongest short of resolution: a calibrated-weight ensemble for a genuine IDR where MD is barely converged, with an explicit statement of the convergence limit and which observables are trustworthy. *Certificate:* convergence diagnostics, weighted observables, honest scope.

## 4. Known results and prior art

- Beyond-AlphaFold ensemble generators: AlphaFlow / ESMFlow (Jing, Berger, Jaakkola 2024) - flow-matching on top of structure predictors. Distributional Graphormer (DiG, Zheng et al, Microsoft ~2023–2024). BioEmu (Microsoft ~2024–2025, equilibrium-ensemble emulation - verify). Str2Str (~2024, verify).
- MSA-subsampling for AF2 conformational ensembles: Del Alamo, Sala, Mchaourab, Meiler ~2022; Wayment-Steele, Kern ~2023 (fold-switching via MSA clustering, verify).
- IDR-specific generative ensembles: idpGAN (Janson, Feig ~2023); learned coarse ensemble models for disordered proteins.
- Ensemble force fields: a99SB-disp (Robustelli, Piana, Shaw 2018); CHARMM36m (Huang, MacKerell ~2017); Amber ff99SB-ILDN.
- Experiment-directed ensemble refinement: Bayesian/maximum-entropy reweighting (BME; Bottaro, Lindorff-Larsen ~2020); ensemble-averaged restrained MD; the metainference method (Bonomi, Vendruscolo ~2016). These are *refinement*, distinct from prediction.
- Forward models: Karplus relations for $J$-couplings; CRYSOL (Svergun) and FoXS (Sali) for SAXS; SPARTA+/ShiftX2 for chemical shifts (verify current standards).

**Status as of mid-2026 - re-verify against current literature before starting any session.**

## 5. Attack plan

`[struct]` mode; one workstation, one GPU.

1. **Converged reference ensemble.** OpenMM/GROMACS long MD or replica-exchange (for disordered/multi-state systems) with an ensemble-appropriate force field; convergence certified by independent-replica agreement on populations and observables. This is the verifier.
2. **Generator.** A conformational flow / flow-matching / diffusion model (PyTorch), or an MSA-subsampled AF-lineage ensemble, producing samples with a defensible weight assignment; where a density exists, enable exact reweighting.
3. **Weight calibration and testing.** Held-out observable tests; where possible, exact-reweighting against $U$ to sharpen weights and report ESS. Failure mode: uncalibrated or degenerate weights - the held-out observable test is the gate.
4. **Experimental forward models (cross-check).** PLUMED / dedicated tools for $J$-couplings, RDCs, SAXS; propagate forward-model error; report separately. Failure mode: burying forward-model error inside the comparison - keep it explicit and propagated.
5. **Sampling-limit honesty.** For IDRs, reference convergence is the binding constraint; state the limit and restrict claims to converged observables. Distinguish sharply, in every report, from static structure prediction.

## 6. Verification and auditability requirements

1. **Certified numerics.** Reference ensemble averages carry block-averaged errors and independent-replica agreement; predicted weighted observables carry bootstrap errors; ESS reported wherever reweighting is used. An unconverged reference is not a verifier and is reported as such.
2. **Independent verification.** The observable-computation and weighting code is separate from the generator-training code; a standalone checker recomputes headline weighted observables from stored samples and weights; a second implementation reproduces at least one comparison.
3. **Reproducibility.** Force field, water model, sampling protocol, seeds, generator hyperparameters, forward-model definitions, and the frozen held-out split are recorded with a SHA-256 manifest; splits committed before evaluation.
4. **Preservation.** Generator-training code, failed weight schemes, and non-converged references (with reasons) are part of the record.
5. **Honest reporting.** The report states up front whether the section-2 tolerance was met against the *converged reference ensemble* (the resolution metric), reports experimental cross-checks separately with propagated forward-model error and a force-field caveat, never presents an unweighted structure set or a most-populated-state hit as ensemble prediction, and never presents experiment-reweighting as de novo prediction.
