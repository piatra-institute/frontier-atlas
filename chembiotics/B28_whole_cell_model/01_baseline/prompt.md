# PROMPT FOR A PREDICTIVE WHOLE-CELL MODEL

## A Karr-model successor whose kinetics predict unseen perturbations rather than refit known phenotypes

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** B - reality-gated (empirical verifier)
**Rank:** B-28 of 29
**Source:** chem/bio top-50 list #44, section F (cells)
**Modes:** `[algo]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

A whole-cell model simulates every molecule and process of a single cell - replication, transcription, translation, metabolism, division - as one integrated dynamical system, mapping genotype to phenotype. The 2012 *Mycoplasma genitalium* model showed it is possible; the open problem is making such a model **predictive rather than fitted**. A model with thousands of parameters can be tuned to reproduce the very datasets used to build it and still have no forecasting power; the scientific value lies entirely in predicting phenotypes it was **not** trained on - a novel gene knockout's essentiality, a growth rate under an unseen medium, a perturbation response - with the parameters constrained, not fit post hoc. This is an enormous integrative and identifiability challenge: many parameters are unmeasured, heterogeneous datasets must be reconciled, and vastly different parameter sets can fit the same training data (non-identifiability), so "reproduces the data" is nearly vacuous as evidence. Mechanistic frameworks (Karr-lineage, E. coli whole-cell efforts), hybrid mechanistic-ML models, and data-driven foundation cell models can *advance* this - integrate more biology, learn unmeasured rates, extend coverage - but they cannot *close* it: a predicted novel phenotype is a hypothesis until measured. This item is **reality-gated**. The honest deliverable is a certified modeling contribution, a held-out benchmark on **withheld perturbations**, and a ranked, calibrated set of falsifiable phenotype predictions for an experimental partner - never a claim that whole-cell modeling is "solved."

## 1. Exact problem statement

**Input.** A genotype and condition specification: the organism's genome/annotation, a defined growth medium/environment, and a **perturbation** (gene knockout/knockdown, gene addition, medium change, expression change). The model's mechanistic content (reaction network, rate laws) and its parameters are fixed *before* seeing the test perturbation.

**Output.** A predicted **phenotype** for the perturbed cell, each element carrying a **calibrated** uncertainty: viability/essentiality (binary or graded), growth rate / doubling time, and - where measured - molecular observables (mRNA/protein/metabolite levels, fluxes, cell-cycle timing).

**Metrics.** Essentiality: balanced accuracy, precision/recall, and area under precision-recall on **held-out** genes. Growth: MAE / RMSE on doubling time or growth rate across held-out conditions and Spearman rank across perturbations. Molecular observables: MAE / rank correlation per observable class. Calibration: expected calibration error and predictive-interval coverage on held-out perturbations. The **decisive** figure of merit is performance on perturbations *absent from parameterization*, reported separately from any fit-quality metric. A metric is meaningful only with its population and split attached.

**Population.** Performance is claimed over a named organism and a named perturbation population - e.g. single-gene knockouts of *M. genitalium* or *E. coli*, or defined-medium growth conditions - stratified by perturbation type and by novelty relative to any data used in parameterization. Aggregate fit statistics without a held-out-perturbation stratum are not accepted.

**Compute-tractable sub-question (in-silico).** Given a model whose structure and parameters are frozen against a committed parameterization corpus, predict a **withheld** set of perturbation phenotypes and meet or beat a named baseline on held-out essentiality / growth, with calibrated uncertainty. This is compute-tractable *only* as prediction on data never used to fit.

**Empirically-gated whole.** Predict the phenotype of a **novel** perturbation - a knockout or condition with no existing measurement - and have it confirmed by experiment. No amount of compute closes this; a self-consistent simulation that refits its own training data is not evidence, and only a new measurement decides.

## 2. Verifier and data

**Ground-truth source.**
- **Gene-essentiality datasets** - genome-wide knockout/transposon-mutagenesis (Tn-seq) essentiality calls; for *E. coli* the Keio single-gene-knockout collection (Baba et al., ~2006) and Tn-seq essentiality; for *M. genitalium* / minimal cells the essentiality data underlying JCVI-syn3.0 (Hutchison et al., ~2016). The primary held-out target.
- **Growth phenotypes** - doubling times / growth rates across defined media and single-carbon-source panels (e.g. Biolog-style and chemostat data, verify).
- **Single-cell and omics measurements** - transcriptome/proteome/metabolome abundances and, where available, single-cell distributions and cell-cycle timing, for molecular-observable validation.
- **Model / knowledge bases** - WholeCellKB (Karr et al., ~2013) and the *M. genitalium* whole-cell model outputs; the *E. coli* whole-cell model (Covert lab, wcEcoli) knowledge base; BiGG/EcoCyc for network structure (parameterization inputs, **not** held-out truth).
- **Foundation cell models** (verify) - data-driven single-cell models (e.g. Geneformer, scGPT-lineage) as *baselines/priors*; they predict expression patterns, not mechanistic perturbation phenotypes, and are explicitly not mechanistic ground truth.

**Frozen split (leakage-safe).** Because the failure mode is refitting, the split is a **parameterization/prediction separation**: a committed corpus of datasets is designated for building and parameterizing the model, and a disjoint set of **perturbations** (specific genes, specific conditions) is withheld and *never touched* during parameterization, structure choice, or hyperparameter selection. The withheld perturbations are chosen to be mechanistically non-trivial (not trivially predictable from the training set) and are committed and hashed before any prediction. Any parameter fit to a dataset that overlaps a test perturbation voids the split. A **leave-whole-perturbation-out** protocol (and, where feasible, leave-one-gene-out cross-validation over essentiality) is documented. This split, and the discipline of not tuning on it, is the entire scientific content of the item.

**Wet-lab gate (mandatory).** A predicted novel-perturbation phenotype **cannot be established by any computation**. Confirmation requires physical experiment: constructing the knockout/knockdown or growth condition and measuring viability, growth rate, and molecular observables (strain construction, culturing, sequencing/omics). A focused campaign - tens of engineered perturbations with growth and omics readout - costs roughly \$50k–\$300k and months; single-cell and cell-cycle phenotyping add cost. This gate is not softenable: the whole point is prediction of the unmeasured, obtainable only by measuring it.

## 3. Standard of a genuine advance

A genuine advance is one of:
1. A **certified modeling contribution** - a whole-cell (or whole-cell-scale) model, a hybrid mechanistic-ML architecture, or a parameterization method that achieves a *new held-out result on withheld perturbations* (better held-out essentiality / growth / observable prediction than a named baseline), with the improvement demonstrably **not** a product of refitting, with parameter identifiability analyzed, and with calibrated uncertainty validated on held-out perturbations.
2. A **calibrated, falsifiable phenotype-prediction set** for perturbations an experimental partner will construct: ranked essentiality/growth/observable predictions with per-perturbation calibrated uncertainties, registered before construction, with a pre-committed accuracy claim (e.g. "correct essentiality call on ≥ $k$ of $n$ withheld genes").

**Not accepted as resolution:**
- A **fit-quality metric treated as predictive power** - reproducing the datasets used to build the model is nearly vacuous; only performance on withheld perturbations counts.
- **Non-identifiable parameterization presented as mechanism** - if many different parameter sets fit the training data equally, no claim about a specific mechanism or parameter value is warranted; identifiability must be analyzed and reported.
- **In-silico-only "validation"** - self-consistency of the simulation, or agreement with another model, is not experimental confirmation.
- A model tuned on the "held-out" perturbations (directly or through structure/hyperparameter choices), which voids the split.
- "Solved whole-cell modeling" claimed from any refit.

## 4. Graded targets

**P1 - Reproduce a baseline whole-cell model on our verified pipeline.** Rebuild/rerun an existing model (the *M. genitalium* whole-cell model, or the *E. coli* wcEcoli model) and reproduce its reported behavior on its own corpus within tolerance, under a committed parameterization/prediction separation. *Evidence:* committed corpus and split hashes, independent scoring, documented parameter provenance. Independently valuable as a leakage-audited, identifiability-annotated baseline.

**P2 - Held-out perturbation prediction with calibration.** Predict a committed set of **withheld** perturbations (genes/conditions never used in parameterization) and report calibrated essentiality/growth predictions with coverage and expected calibration error. *Evidence:* leave-perturbation-out results, reliability curves, explicit statement of what was and was not used to fit.

**P3 - Certified modeling contribution.** A method - better mechanistic coverage, learned unmeasured rates constrained by data, a hybrid mechanistic-ML model, or a principled parameterization with identifiability analysis - that yields a *statistically significant, split-audited* improvement over P1/P2 on withheld perturbations. *Evidence:* paired per-perturbation deltas with confidence intervals, ablations, an identifiability analysis distinguishing constrained from unconstrained parameters, no test-set tuning.

**P4 - New held-out SOTA on unseen perturbations.** Best-in-class on the committed withheld-perturbation set across essentiality, growth, and molecular observables, with demonstrated transfer to a genuinely novel perturbation class. *Evidence:* full held-out distributions, split and provenance manifest, independent reproduction from committed code.

**P5 - Wet-lab-ready phenotype predictions.** A ranked, calibrated slate of novel-perturbation phenotype predictions for perturbations a partner will construct, registered before construction, with a pre-committed falsifiable claim. *Evidence:* timestamped registration, post-hoc scoring against constructed-strain phenotypes, honest hit/miss accounting including surprising phenotypes. This is the ceiling the machine reaches; closing the loop is the experiment's job.

## 5. Known results and prior art

- **Karr whole-cell model** - Karr, Sanghvi, Macklin, Covert et al. (*Cell* 2012): the first whole-cell computational model, *M. genitalium*, integrating 28 submodels and predicting phenotype from genotype; the founding result and the model this item seeks to succeed with predictive kinetics.
- **WholeCellKB** - Karr et al. (~2013): the structured knowledge base underlying whole-cell models.
- **E. coli whole-cell model (wcEcoli)** - Covert lab (Macklin, Ahn-Horst, Sun et al., ~2020, *Science*): mechanistic simulation cross-evaluating heterogeneous *E. coli* datasets; the largest-organism whole-cell effort.
- **Minimal-cell whole-cell simulation** - Thornburg, Luthey-Schulten et al. (~2022, *Cell*): spatially resolved whole-cell simulation of the minimal cell JCVI-syn3A; Hutchison et al. (~2016, *Science*) for the minimal-genome essentiality data.
- **Vivarium** - Agmon, Spangler, Covert et al. (~2022): a multi-scale, composable simulation framework for integrating cell models.
- **Hybrid mechanistic-ML / scientific ML** - universal-differential-equation and neural-ODE approaches to learning unmeasured kinetics (Rackauckas et al., verify); enzyme-constrained and kinetic-learning methods as components.
- **Foundation cell models** (verify) - Geneformer (Theodoris et al., ~2023, *Nature*), scGPT (Cui et al., ~2024): data-driven single-cell models; predictive of expression patterns, **not** mechanistic perturbation phenotypes - included as baselines and a cautionary contrast to fitted mechanism.

*Status as of mid-2026 - re-verify against current literature before starting any session.* Whole-cell and foundation-cell modeling are active; re-verify whether new organism models, hybrid mechanistic-ML methods, or perturbation-prediction benchmarks have shifted the predictive-vs-fitted frontier, and confirm the provenance and independence of every essentiality/growth dataset before use.

## 6. Attack plan

**Data.** Assemble the parameterization corpus (network structure, measured rates, expression/omics) and a **disjoint** withheld-perturbation set (specific essentiality genes and growth conditions), committing and hashing the parameterization/prediction separation before any prediction. Document, per parameter, whether it is measured, fit, or unconstrained.

**Baselines.** Rebuild/rerun the *M. genitalium* and/or *E. coli* whole-cell models; run leave-perturbation-out prediction; include a data-driven foundation-model baseline for contrast. Score essentiality/growth with an independent script separate from the simulation code.

**Model.** Candidate contributions: (i) hybrid mechanistic-ML models that learn unmeasured rate laws under mechanistic constraints; (ii) principled parameterization (Bayesian / ensemble) that yields **parameter posteriors** and exposes non-identifiability rather than hiding it in a point fit; (iii) improved integrative coverage of a subsystem (e.g. metabolism–expression coupling) evaluated by held-out prediction; (iv) active-learning selection of maximally informative perturbations for a partner.

**Calibration and identifiability.** Report parameter posteriors / profile-likelihoods to distinguish constrained from unconstrained parameters (structural and practical identifiability). Fit and validate predictive-interval calibration on held-out perturbations; report coverage and expected calibration error.

**Compute.** A whole-cell simulation and moderate hybrid-ML training are feasible on one prosumer GPU / CPU workstation for small organisms; ensemble parameterization and larger organisms are heavier and may bound scope. Compute enables prediction and identifiability analysis, not closure.

**Failure modes.** (i) **Refitting masquerading as prediction** - the dominant risk; a model tuned to its training data reports fit quality as if it were forecasting power. (ii) **Parameter non-identifiability** - many parameter sets fit equally, so mechanistic and parameter-value claims are unwarranted without identifiability analysis. (iii) **Data heterogeneity** - reconciling datasets from different labs/conditions introduces silent inconsistencies. (iv) **Distribution shift** - a novel perturbation class lies outside anything the parameterization constrained. (v) **Leakage** - any tuning on the held-out perturbations (including via structure/hyperparameters) voids the entire claim.

## 7. Verification and auditability requirements

1. **Parameterization/prediction separation.** A committed, hashed split designates which datasets parameterize the model and which **perturbations** are withheld; the withheld set is never touched during parameterization, structure choice, or hyperparameter selection; leave-perturbation-out (and leave-one-gene-out where feasible) protocols are documented; there is no test-set tuning. This is the item's central requirement.
2. **Predictive-vs-fitted separation in reporting.** Fit-quality metrics on the parameterization corpus and **held-out-perturbation** metrics are reported separately and never conflated; the decisive claim is held-out performance.
3. **Parameter identifiability.** Every headline mechanistic/parameter claim is accompanied by an identifiability analysis (posteriors / profile-likelihoods) distinguishing constrained from unconstrained parameters; non-identifiable parameters are flagged and no point-value mechanism is claimed for them.
4. **Calibrated uncertainty.** Every prospective phenotype prediction carries a calibrated uncertainty; coverage and expected calibration error are reported on held-out perturbations, per perturbation type, with degradation on novel classes foregrounded.
5. **Independent reproduction.** All held-out metrics are recomputed by a standalone script separate from the simulation/training code, from the committed splits and predictions; parameter provenance (measured / fit / unconstrained) is part of the record.
6. **Cryptographic manifest, preservation, and registry.** A SHA-256 manifest covers the parameterization/prediction split, dataset and knowledge-base version hashes, model and parameterization code, parameter values/posteriors, and every prediction file; anything not preserved is stated explicitly. Wet-lab-ready predictions (P5) are timestamped and registered before strain construction and scored afterward including surprises.
7. **Honest reporting.** The report states up front that predictive whole-cell modeling is reality-gated and **not resolved**; separates in-silico fit from any experimental phenotype; foregrounds the predictive-vs-fitted distinction and parameter non-identifiability as the core standard; labels every novel-perturbation prediction a wet-lab-pending hypothesis; and never presents a refit or a self-consistent simulation as a real-world guarantee.
