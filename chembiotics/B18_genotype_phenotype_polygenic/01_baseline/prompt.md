# PROMPT FOR GENOTYPE-TO-PHENOTYPE PREDICTION OF COMPLEX POLYGENIC TRAITS

## Calibrated, ancestry-aware polygenic risk estimation - and the limits of it

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** B - reality-gated (empirical verifier)
**Rank:** B18 of 29
**Source:** chem/bio top-50 list #37, section E (genomics)
**Modes:** `[data]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Most medically relevant human traits are polygenic: thousands of variants each contribute a little, heritability is substantial but incompletely captured ("missing heritability"), and effects interact with genetic background (epistasis) and environment (gene×environment). Polygenic risk scores predict such traits with real but limited accuracy, and - critically - that accuracy does not transfer across ancestries, so naive deployment can widen health disparities. The task is to predict complex-trait phenotypes from genotype with calibrated uncertainty and honest, mandatory ancestry stratification, and to distinguish predictive from causal signal. This is reality-gated in an unusual way: the phenotype label is *observational* (biobank records, not a designed experiment), and causal mechanism requires functional perturbation the model cannot perform. Compute can produce a certified method, a held-out benchmark result, and calibrated risk estimates - but a risk estimate is never a determination, a predictive score is never a proven mechanism, and no clinical use is implied. No resolution is on offer, and every output is a probabilistic hypothesis, not a fact about a person.

## 1. Exact problem statement

**Input.** An individual's genotype (array or sequence-derived, imputed to a reference panel; build documented), optionally with environmental/covariate context and self-reported or genetically-inferred ancestry.

**Output.** For a defined trait, a calibrated phenotype prediction:
- for a **quantitative** trait, a predicted value with a calibrated interval;
- for a **binary/disease** trait, a calibrated probability (risk estimate), explicitly framed as a population-relative risk, never a determination.
Each output carries an ancestry label and an explicit statement of transferability limits.

**Metric.** Quantitative: incremental R² (variance explained beyond covariates), reported *per ancestry group*. Binary: AUC, odds ratio per standard deviation, and - primary - calibration (calibration slope/intercept, reliability curves) per ancestry. A **transferability ratio** (accuracy in a non-discovery ancestry relative to the discovery ancestry) is mandatory. Confidence intervals from a fixed resampling scheme.

**Population.** Individuals across the ancestry groups represented in the biobank(s); performance reported separately per group with sample sizes. Aggregate accuracy that hides an ancestry gap is not acceptable.

**Compute-tractable sub-question vs empirically-gated whole.** Tractable: *given a frozen, access-controlled biobank split, predict held-out phenotypes with calibrated, ancestry-stratified accuracy under an individual- and cohort-holdout protocol.* Empirically- and observationally-gated: the *causal* genetic architecture - which variants cause the trait, how they interact (epistasis), and how they combine with environment (GxE) - cannot be established from observational genotype–phenotype correlation and requires functional experiments outside the model's reach.

## 2. Verifier and data

**Ground-truth sources.**
- **UK Biobank** (~500k participants, access-controlled) - the primary genotype–phenotype resource; **All of Us** (ancestry-diverse, access-controlled) - essential for cross-ancestry evaluation; **FinnGen**, **Biobank Japan**, and similar cohorts (verify current access terms). Note the access barrier explicitly: these require approved applications, and All of Us / diverse cohorts are the only way to evaluate transferability honestly.
- **GWAS Catalog** - curated trait associations and summary statistics.
- **PGS Catalog** - published polygenic scores and their reported performance; the standard external benchmark.

**Frozen, leakage-safe split.** Commit and hash before modeling.
- **Individual holdout with relatedness control:** hold out whole individuals *and* remove cryptic relatives across the split (kinship-based pruning) - related individuals leak phenotype signal.
- **Cohort holdout:** train on one biobank, evaluate on another, to expose overfitting to cohort-specific structure.
- **Ancestry holdout / stratification:** evaluate on ancestry groups distinct from the GWAS-discovery ancestry; this is where PRS accuracy collapses and must be measured, not assumed away.
- **Summary-statistic overlap control:** ensure the GWAS discovery sample does not overlap the PRS test individuals - sample overlap is a classic, silent leak that inflates PRS accuracy.

**Wet-lab / functional gate (mandatory).** The phenotype is observational; a predictive association is not a causal mechanism. Establishing that a variant *causes* a trait - as opposed to tagging causal variation via LD or confounding - requires functional or perturbation experiments (MPRA, CRISPR perturbation, model-organism or cellular assays) that no biobank analysis supplies. Fine-mapping narrows candidates but does not close this. Indicative cost: functional follow-up of a candidate locus (reporter/perturbation assays) runs low-tens-of-thousands USD and months per locus; establishing GxE mechanism is costlier still and often intractable observationally. This gate is not optional and must not be softened. Additionally, the biobank access barrier is itself a real-world gate on even the predictive half.

## 3. Standard of a genuine advance

A genuine advance is one or more of:
- A **certified pipeline** reproducing a named SOTA PRS method (LDpred2, PRS-CS/PRS-CSx) on the frozen, access-controlled split, with ancestry-stratified metrics independently runnable.
- A **new held-out SOTA** in predictive accuracy *or* - more valuable here - in **cross-ancestry transferability** or **calibration**, on a pre-registered split, reported per ancestry.
- A **method contribution** that captures signal beyond additive PRS (epistasis, GxE, rare-variant burden) with a demonstrated, leakage-controlled improvement, or that improves risk-estimate calibration across ancestries.
- A **calibrated, ancestry-stratified risk-estimate set** explicitly framed for research use, with transferability limits stated, ready for a clinical/epidemiological partner to evaluate - never for direct clinical action.

**Not accepted as resolution.**
- An aggregate accuracy number that hides an ancestry transferability gap.
- A predictive PRS presented as a causal or mechanistic result.
- A risk estimate presented as a determination of an individual's outcome.
- Any output framed for direct clinical or reproductive decision-making.
- A metric inflated by relatedness leakage or GWAS-sample overlap.
- An "epistasis captured" claim not controlled for additive-model leakage and overfitting.

## 4. Graded targets

**P1 - Reproduce SOTA PRS on the frozen split.** Rebuild LDpred2 and PRS-CS(x) with our own verified code; match reported per-ancestry accuracy on the committed individual-/cohort-holdout split. Evidence: reproducible metrics, hashed split, side-by-side with PGS Catalog numbers.

**P2 - Calibrated, ancestry-stratified risk.** Predict held-out phenotypes with calibrated risk estimates; report calibration and transferability ratio per ancestry. Evidence: reliability curves per group; relatedness- and overlap-leakage ablations.

**P3 - Certified method: transferability, calibration, or beyond-additive signal.** Improve cross-ancestry transferability, calibration, or capture leakage-controlled non-additive (epistasis/GxE) or rare-variant signal, on a pre-registered split. Evidence: benchmark-integrity statement; explicit demonstration that the gain is not additive-model leakage.

**P4 - Calibrated risk-estimate set for a research partner.** An ancestry-stratified, calibrated risk-estimate set with transferability limits and a mechanism-vs-prediction disclaimer, framed for research/epidemiological evaluation only, with a pre-registered success criterion. Every output labeled a probabilistic hypothesis, never a determination.

## 5. Known results and prior art

- **LDpred / LDpred2** (Vilhjálmsson et al., ~2015; Privé et al., ~2020) - Bayesian PRS accounting for LD; a standard baseline.
- **PRS-CS** (Ge et al., ~2019) and **PRS-CSx** (cross-ancestry, ~2022 - verify) - continuous-shrinkage priors; PRS-CSx targets multi-ancestry integration.
- **lassosum, SBayesR, MegaPRS** (verify) - additional strong PRS methods.
- **Deep-learning genotype models on biobanks** - various (verify current results); note that deep models have often *not* decisively beaten well-tuned additive PRS for common traits - report this honestly.
- **Transferability work** - Martin et al. (~2019) showed PRS accuracy is far lower in non-European ancestries and that naive clinical use may exacerbate disparities; this framing is central and non-negotiable here.
- **Resources** - UK Biobank, All of Us, FinnGen, Biobank Japan; GWAS Catalog; PGS Catalog.
- **Open parts:** missing heritability, epistasis, gene×environment, and cross-ancestry portability - none closed; these are why the problem is a portfolio item, not a solvable target.

**Status as of mid-2026 - re-verify against current literature before starting any session.** Confirm current methods, cohort access terms, and PGS Catalog benchmarks before committing.

## 6. Attack plan

**First dataset pull.** Apply for UK Biobank and, for transferability, All of Us access (note the multi-week/month approval barrier); pull GWAS summary statistics and PGS Catalog scores as external baselines. Do not begin modeling before access and the split are in place.

**Leakage-safe protocol.** Commit individual-holdout (with kinship pruning), cohort-holdout, and ancestry-stratified splits before modeling; verify no GWAS-discovery/PRS-test sample overlap; hash the manifest. Report every metric per ancestry with sample sizes.

**Baseline and model.** Reproduce LDpred2 and PRS-CS(x) as baselines. For a contribution, target transferability (cross-ancestry priors, functionally-informed weighting), calibration, or leakage-controlled non-additive signal - and treat any epistasis/GxE claim with an explicit overfitting/additive-leakage control. Calibrate risk estimates on held-out data per ancestry and report the calibration.

**One-GPU scope and failure modes.** Additive PRS fitting is CPU/memory-bound (large genotype matrices) rather than GPU-bound; deep models fit a single prosumer GPU but rarely beat tuned PRS - flag both. Failure modes to expect and report: relatedness and sample-overlap leakage inflating accuracy; ancestry transferability collapse; spurious epistasis from overfitting; confounding (population structure, assortative mating, environment) masquerading as genetic effect; and the ever-present risk of over-interpreting a risk estimate as a determination. State each where it bites.

## 7. Verification and auditability requirements

1. **Leakage-safe evaluation.** Individual-holdout with kinship pruning, cohort-holdout, and ancestry-stratified splits committed and hashed before evaluation; GWAS-sample-overlap explicitly ruled out; no test-set tuning.
2. **Calibrated uncertainty.** Every risk estimate carries a calibrated confidence; calibration reported on held-out data per ancestry with reliability curves - a risk estimate without calibration is not reportable here.
3. **Ancestry and population fairness (mandatory, foregrounded).** All metrics stratified by ancestry with sample sizes; the transferability ratio reported; the disparity risk of naive deployment stated up front; aggregate numbers never used to hide an ancestry gap.
4. **Causal-vs-predictive honesty.** Every association labeled predictive unless functionally established; PRS never presented as mechanism; epistasis/GxE claims carry additive-leakage and overfitting controls.
5. **Independent reproduction.** Metrics reproducible from the committed split and code by a separate script; SHA-256 manifest over data version hashes, code, and predictions (respecting biobank data-governance - hashes and code, not raw individual data).
6. **Preservation and governance.** Model weights or provenance, code, and dataset version hashes are part of the record; individual-level data handling complies with the biobank's governance; anything not preserved is stated explicitly.
7. **Honest reporting.** The report states up front that the problem is reality-gated and NOT resolved; separates predictive accuracy from any causal claim; labels every output a probabilistic, research-only hypothesis and never a clinical or reproductive determination; and never presents a benchmark number as a real-world guarantee about any individual.
