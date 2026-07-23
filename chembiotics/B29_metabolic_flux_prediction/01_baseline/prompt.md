# PROMPT FOR METABOLIC-FLUX PREDICTION WITHOUT EXHAUSTIVE KINETICS

## Learned constraints that predict the realized intracellular flux distribution - validated against 13C-MFA, not internal consistency

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** B - reality-gated (empirical verifier)
**Rank:** B-29 of 29
**Source:** chem/bio top-50 list #45, section F (cells)
**Modes:** `[algo]` `[func]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Flux balance analysis (FBA) predicts the *feasible space* of steady-state metabolic flux distributions from a stoichiometric network and an assumed objective - but a cell realizes **one** distribution, and FBA generally does not tell you which. Kinetic models can in principle predict the realized flux, but they demand thousands of rate constants that are unmeasured and non-identifiable, so they do not scale. The open problem is to predict the realized intracellular flux distribution **without** exhaustive kinetics: by learning additional constraints - thermodynamic, enzyme-capacity, regulatory, or data-driven - that narrow the feasible space toward the true operating point, and by validating those constraints against **measured** fluxes rather than against the model's own consistency. This matters because flux is the quantitative phenotype metabolic engineering acts on. Enzyme-constrained models (GECKO-lineage), parsimonious FBA, and ML-augmented constraint methods can *advance* this - narrow the space, improve agreement with observed growth and secretion - but they cannot *close* it: the only ground truth for intracellular flux is an isotope-labeling experiment, and a predicted flux is a hypothesis until so measured. This item is **reality-gated**. The honest deliverable is a certified constraint-learning method, a held-out benchmark against 13C-MFA fluxes under a leakage-safe split, and a ranked, calibrated set of falsifiable flux predictions for an experimental partner - never a claim that flux prediction is "solved."

## 1. Exact problem statement

**Input.** A genome-scale (or core) metabolic-network reconstruction (stoichiometry, reversibility, gene–protein–reaction rules), a defined growth condition (medium, uptake bounds, aerobic/anaerobic), and optionally auxiliary data (enzyme abundances/proteomics, thermodynamic parameters, measured exchange rates). The prompt fixes, per task, which auxiliary data are provided.

**Output.** A predicted **realized flux distribution** $v \in \mathbb{R}^{n}$ over network reactions (or a named subset - central carbon metabolism, split ratios at key branch points), each flux carrying a **calibrated** predictive interval, together with the learned constraints that produced it stated explicitly.

**Metrics.** Against measured fluxes: MAE / RMSE on flux values (normalized to substrate uptake), Spearman rank correlation across reactions, and - for the decision-relevant quantities - error on **branch-point split ratios** (e.g. the glycolysis/pentose-phosphate split, the TCA/glyoxylate split) and on secretion fluxes. Calibration: expected calibration error and predictive-interval coverage on held-out conditions. Reporting must separate reactions that 13C-MFA actually resolves from those it does not; unresolvable fluxes are not scored as if measured. A metric is meaningful only with its population and split attached.

**Population.** Performance is claimed over a named organism and condition population - e.g. *E. coli* central carbon metabolism across carbon sources and growth rates, or a yeast panel - stratified by condition and by novelty relative to training conditions. Aggregate errors pooled across incomparable networks/conditions are not accepted.

**Compute-tractable sub-question (in-silico).** Given a frozen, leakage-safe split of measured (13C-MFA) fluxes, produce learned constraints whose predicted flux distribution meets or beats a named baseline (FBA, pFBA, enzyme-constrained FBA) on held-out conditions in flux MAE / split-ratio error, with calibrated uncertainty - *within the conditions the data covers*.

**Empirically-gated whole.** Predict the realized flux distribution of a **novel** condition or strain - an unseen carbon source, an engineered knockout, a new organism - and have it confirmed by a 13C-MFA experiment. No amount of compute closes this; FBA feasibility and internal consistency are not evidence about the realized flux, and only isotope-labeling measurement decides.

## 2. Verifier and data

**Ground-truth source.**
- **13C-metabolic-flux-analysis (13C-MFA) datasets** - intracellular fluxes inferred from isotope-labeling experiments; the *only* direct ground truth for realized intracellular flux. Compilations of central-carbon fluxes across conditions (e.g. Gerosa, Sauer et al., ~2015 *E. coli* conditions; and aggregated flux databases, verify) are the primary corpus.
- **Central-carbon flux databases** (verify) - curated repositories of published 13C-MFA flux maps (e.g. CeCaFDB-style compilations, verify); heterogeneous in organism, network, and reporting convention.
- **Exometabolomics / exchange fluxes** - measured uptake and secretion rates (glucose, oxygen, acetate, ethanol, etc.); directly measurable boundary fluxes that any prediction must match.
- **Growth rates** - measured biomass production across conditions; a weak but measurable global constraint.
- **Proteomics / enzyme-abundance data** (verify) - for enzyme-constrained and capacity models (inputs, not flux ground truth).
- **Network reconstructions** - BiGG Models, EcoCyc/MetaCyc, organism-specific genome-scale reconstructions (structure/priors, **not** flux truth).

**Frozen split (leakage-safe).** The test set is fixed before modeling under **condition/strain and study separation**: hold out entire growth conditions, strains, and - wherever possible - entire studies, so a test flux map is not a replicate or batch-twin of a training one. Add a **novelty** axis (test conditions distinct in carbon source / growth regime from training). Because 13C-MFA maps are reported under different network scopes and conventions, all fluxes are harmonized to a common network and normalization **before** splitting, and the harmonization is documented. Reactions that the labeling design does not resolve are marked non-scored. Split and harmonization manifests are committed and hashed before any test number.

**Wet-lab gate (mandatory).** A predicted intracellular flux distribution **cannot be established by any computation**. Confirmation requires a physical **isotope-labeling experiment**: culturing on ¹³C-labeled substrate, quenching, measuring mass-isotopomer distributions by MS/NMR, and inferring fluxes by 13C-MFA - plus exchange-rate and growth measurement. A single condition's 13C-MFA campaign costs roughly \$15k–\$100k and weeks to months (labeled substrate, quench/extraction, MS, flux inference); multiple conditions and strains multiply this. This gate is not softenable: FBA and internal consistency say nothing about which feasible flux the cell realizes; only the labeling experiment does.

## 3. Standard of a genuine advance

A genuine advance is one of:
1. A **certified method contribution** - a constraint-learning method (thermodynamic, enzyme-capacity, regulatory, or data-driven) that achieves a *new held-out result against measured 13C-MFA fluxes* under a condition/strain-separated split (better flux MAE, split-ratio error, and rank correlation than FBA / pFBA / enzyme-constrained baselines), with the improvement holding on novel conditions and calibrated uncertainty validated on held-out data.
2. A **calibrated, falsifiable flux-prediction set** for conditions/strains an experimental partner will assay by 13C-MFA: ranked predicted flux distributions with per-flux calibrated intervals, registered before the experiment, with a pre-committed accuracy claim (e.g. "branch-point split ratios within $\pm x$ on ≥ $k$ of $n$ conditions").

**Not accepted as resolution:**
- **FBA feasibility or internal consistency treated as a flux prediction** - a feasible or self-consistent flux distribution is not evidence about the realized flux; the feasible space is not the operating point.
- **Learned constraints validated only against themselves** - narrowing the space, matching only growth/exchange, or agreeing with another model is not validation against measured intracellular flux.
- **In-silico-only "validation"** - reproducing a flux map used to fit the constraints, or matching a different predictor, is not experimental confirmation.
- A method whose apparent skill comes from **leakage** (replicate/batch twins across the split) or from scoring reactions the labeling design cannot resolve.
- "Solved flux prediction" claimed from any FBA variant or refit.

## 4. Graded targets

**P1 - Reproduce baselines on our verified pipeline.** Re-run FBA, parsimonious FBA (pFBA), and an enzyme-constrained model (GECKO-style) on our harmonized, condition-separated split and reproduce their agreement with measured 13C-MFA fluxes within tolerance. *Evidence:* committed split/harmonization hashes, an independent scoring script, per-condition and per-branch-point tables. Independently valuable as a leakage-audited baseline that quantifies how far FBA feasibility is from realized flux.

**P2 - Calibrated uncertainty.** Attach and validate per-flux predictive intervals whose coverage and expected calibration error are measured on held-out conditions, per condition and per novelty stratum, with explicit reporting of degraded calibration on novel conditions and on poorly resolved reactions. *Evidence:* reliability curves, coverage tables, resolved/non-resolved reaction annotation.

**P3 - Certified method contribution.** A learned-constraint method - thermodynamic (e.g. max-min driving force), enzyme-capacity, regulatory, or ML-augmented - that yields a *statistically significant, leakage-audited* improvement over P1 on measured fluxes on the hard novel-condition stratum. *Evidence:* paired per-flux/per-condition deltas with confidence intervals, ablations isolating each constraint's contribution, no test-set tuning.

**P4 - New held-out SOTA / cross-condition transfer.** Best-in-class on the committed condition- and study-separated split across flux MAE, split-ratio error, and rank correlation simultaneously, with demonstrated transfer to a genuinely novel condition or strain. *Evidence:* full error distributions over resolved reactions, split/harmonization manifest, independent reproduction from committed code.

**P5 - Wet-lab-ready flux predictions.** A ranked, calibrated slate of predicted flux distributions for conditions/strains a partner will assay by 13C-MFA, registered before the experiment, with a pre-committed falsifiable claim on branch-point split ratios and secretion fluxes. *Evidence:* timestamped registration, post-hoc scoring against inferred fluxes, honest hit/miss accounting including mispredicted branch points. This is the ceiling the machine reaches; closing the loop is the labeling experiment's job.

## 5. Known results and prior art

- **Flux balance analysis / COBRA** - Palsson lab and the COBRA ecosystem; Orth, Thiele, Palsson (~2010, *Nat. Biotechnol.*, "What is flux balance analysis?"); COBRApy (Ebrahim et al., ~2013). The feasible-space baseline this item must beat against measurement.
- **Parsimonious FBA (pFBA)** - Lewis et al. (~2010): minimal-total-flux selection within the FBA optimum; a standard point-selection heuristic.
- **Enzyme-constrained models** - GECKO (Sánchez, Nielsen et al., ~2017) and GECKO 2.0/3.0 (Domenzain et al., ~2022); MOMENT and ecModel approaches: proteome-capacity constraints narrowing the flux space.
- **Thermodynamic constraints** - max-min driving force / thermodynamic FBA (Noor, Milo et al., ~2014, verify): thermodynamic feasibility as an additional constraint.
- **13C-MFA methodology and tooling** - Wiechert, Antoniewicz, Young et al.; INCA / 13CFLUX2 flux-inference software; the measurement standard for intracellular flux.
- **Reference flux datasets** - Gerosa, Sauer et al. (~2015): *E. coli* fluxes across conditions; aggregated central-carbon flux compilations (CeCaFDB-style, verify).
- **ML-augmented and kinetic-learning approaches** - machine-learning prediction of flux / pathway dynamics (e.g. Costello & Martin, ~2018, *npj Syst. Biol. Appl.*, verify); ensemble/kinetic-model learning (K-FIT and ensemble modeling, verify) as components; data-driven constraint learning.

*Status as of mid-2026 - re-verify against current literature before starting any session.* Constraint-based and ML-augmented flux modeling are active; re-verify whether new enzyme-constrained methods, ML constraint learners, or larger 13C-MFA compilations have improved held-out flux prediction, and confirm the network scope, normalization convention, and resolvability of every flux dataset before use.

## 6. Attack plan

**Data.** Pull a 13C-MFA flux compilation (e.g. *E. coli* central-carbon across conditions), exchange-rate and growth data, and the matching genome-scale reconstruction (BiGG). Harmonize all flux maps to a common network and normalization; annotate resolved vs. non-resolved reactions. Build condition/strain/study clustering; commit a **condition-separated** split plus a labeled within-study upper bound. Freeze and hash before modeling.

**Baselines.** Reproduce FBA, pFBA, and an enzyme-constrained (GECKO-style) model; measure each against 13C-MFA fluxes with an independent scoring script separate from the modeling code, per condition and per branch point.

**Model.** Candidate contributions: (i) thermodynamic constraints (max-min driving force) added to the feasible space; (ii) enzyme-capacity constraints from proteomics; (iii) an **ML-learned constraint** (e.g. a model mapping condition/omics to flux priors or to bounds) trained to narrow the space toward measured operating points; (iv) hybrid schemes that combine mechanistic constraints with a data-driven residual - always validated against held-out 13C-MFA, never against internal consistency.

**Calibration.** Fit and validate per-flux predictive intervals on held-out conditions (conformal / ensemble methods); report coverage and expected calibration error per condition and per novelty stratum, and separately for well- vs. poorly resolved reactions.

**Compute.** FBA/pFBA/enzyme-constrained optimization and ML constraint learners all run comfortably on one prosumer GPU / CPU workstation - compute is not the bottleneck; **measured 13C-MFA flux data** is scarce and heterogeneous. Prefer data-efficient, mechanistically grounded constraint learning over scale.

**Failure modes.** (i) **Feasible-space ≠ operating point** - the core conceptual trap; FBA narrows possibilities but does not identify the realized flux, and a self-consistent solution is not a validated one. (ii) **Validation against internal consistency** - learned constraints that are only checked against the model, or against growth/exchange alone, are not validated against intracellular flux. (iii) **Data scarcity and heterogeneity** - 13C-MFA maps are few, reported under different network scopes and conventions, and unevenly resolved; harmonization errors propagate silently. (iv) **Non-resolvable reactions** - scoring fluxes the labeling design cannot resolve inflates apparent accuracy. (v) **Leakage and distribution shift** - replicate/batch twins across the split, and novel conditions outside the training manifold, both mislead.

## 7. Verification and auditability requirements

1. **Leakage-safe evaluation.** The train/test split is committed and hashed before any evaluation, under documented **condition/strain and study separation** plus a novelty axis; within-study scores are reported only as a labeled upper bound; all fluxes are harmonized to a common network/normalization before splitting, with the harmonization documented; there is no test-set tuning.
2. **Validation against measured flux, not consistency.** Every constraint-learning claim is validated against **measured 13C-MFA** intracellular fluxes; agreement with growth/exchange only, or with the model's own feasible space, is explicitly labeled insufficient and never presented as flux validation.
3. **Feasible-space honesty.** The report states explicitly that FBA predicts a feasible space, not the realized flux, and quantifies how far each baseline's chosen point is from measurement; no feasible or self-consistent distribution is presented as a validated prediction.
4. **Resolvability accounting.** Reactions that the labeling design does not resolve are marked and excluded from scored metrics; split-ratio and secretion-flux errors (the resolvable, decision-relevant quantities) are reported explicitly.
5. **Calibrated uncertainty.** Every prospective flux carries a calibrated predictive interval; coverage and expected calibration error are reported on held-out conditions, per novelty stratum and per resolvability class, with degradation on novel conditions foregrounded.
6. **Cryptographic manifest, preservation, and registry.** A SHA-256 manifest covers split and harmonization definitions, dataset and reconstruction version hashes, model/constraint code, and every prediction file; network scope, normalization convention, and constraint configurations are part of the record; anything not preserved is stated explicitly. Wet-lab-ready predictions (P5) are timestamped and registered before the 13C-MFA experiment and scored afterward including mispredictions.
7. **Honest reporting.** The report states up front that metabolic-flux prediction is reality-gated and **not resolved**; separates in-silico feasibility/consistency from any 13C-MFA result; foregrounds that the feasible space is not the realized flux and that learned constraints must be validated against measurement; labels every prediction a wet-lab-pending hypothesis; and never presents an FBA variant or internal-consistency metric as a real-world guarantee.
