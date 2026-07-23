# PROMPT FOR MICROBIOME COMMUNITY-FUNCTION PREDICTION

## The emergent metabolic output of a microbial community from its metagenome - not the sum of single-organism functions

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** B - reality-gated (empirical verifier)
**Rank:** B-19 of 29
**Source:** chem/bio top-50 list #48, section G (higher-order)
**Modes:** `[data]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

A microbial community's useful output - which metabolites it produces and consumes, whether it makes butyrate or hydrogen sulfide, how it responds to a dietary or drug perturbation - is an **emergent** property, not a lookup of its members' genomes. The same species carries different gene content strain to strain; cross-feeding, competition, and higher-order interactions mean the community is not the sum of its parts; and function is heavily **context-dependent** on nutrients, pH, oxygen, and host. Metagenomes are now cheap and abundant, but they enumerate *genetic potential*, not *realized metabolic output*; the paired measurements that would ground a function predictor - metagenome plus metabolome, defined-community assays, gnotobiotic phenotypes - are comparatively scarce, heterogeneous, and confounded. Gene-content predictors (PICRUSt-lineage) and community metabolic models (community FBA, MICOM) can *advance* this - impute pathway abundance, propose flux distributions, rank likely outputs - but they cannot *close* it: emergence, strain variation, and context dependence mean a predicted community function is a hypothesis until measured. This item is **reality-gated**. The honest deliverable is a certified prediction method, a held-out benchmark on paired multi-omics under a leakage-safe split, and a ranked, calibrated set of falsifiable community-function predictions for an experimental partner - never a claim that microbiome function is "solved."

## 1. Exact problem statement

**Input.** A community description at a declared resolution: a **metagenome** (assembled genes / MAGs / taxonomic + functional-gene profiles), optionally 16S amplicon profiles, optionally strain-resolved genomes, together with a specified **environmental context** (nutrient medium / diet, pH, oxygen, host state). The prompt fixes, per task, the input resolution and whether context is given.

**Output.** A predicted **community metabolic phenotype**: the production/consumption of a named panel of metabolites (e.g. short-chain fatty acids - butyrate, propionate, acetate; H₂S; secondary bile acids; specified drug metabolites), each with a **calibrated** predictive interval, and/or classification of a community's functional state. Where a mechanistic model is used, the output includes a community flux distribution with the same calibration requirement.

**Metrics.** For each metabolite: MAE / RMSE on measured concentration or flux (in the assay's units), Spearman rank correlation across communities, and - where the decision is directional - classification accuracy of production vs. non-production. Calibration: expected calibration error and predictive-interval coverage on held-out communities. For multi-metabolite panels, per-metabolite reporting is mandatory; a single pooled score hides which functions are actually predictable. A metric is meaningful only with its population and split attached.

**Population.** Performance is claimed over a named population - e.g. human gut communities on a defined multi-omics cohort, or a panel of synthetic/defined communities in a specified medium - stratified by cohort/study and by community novelty (test communities compositionally distinct from training). Cross-study aggregation without stratification is not accepted, because batch and protocol effects dominate.

**Compute-tractable sub-question (in-silico).** Given a frozen, leakage-safe split of paired metagenome+metabolome (or defined-community) data, produce a predictor whose held-out per-metabolite MAE / rank correlation meets or beats a named baseline, with calibrated uncertainty - *within the contexts and community types the data covers*.

**Empirically-gated whole.** Predict the metabolic output of a community that is **novel** (a new composition, a new context, an unseen strain configuration) and have that prediction confirmed by culturing/metabolomics or a gnotobiotic experiment. No amount of compute closes this; emergence and context dependence mean only the measurement decides.

## 2. Verifier and data

**Ground-truth source.**
- **Paired metagenome + metabolome cohorts** - e.g. the HMP2 / iHMP IBD multi-omics resource (Lloyd-Price et al., ~2019) and the associated stool metabolomics (Franzosa et al., ~2019, verify); the primary observational ground truth for realized function.
- **Defined / synthetic-community assays** - designed communities with measured metabolite outputs in controlled media (Venturelli-lab-style synthetic human gut communities, e.g. butyrate-production designs, ~2021, verify); the cleanest causal ground truth because composition and context are controlled.
- **Gnotobiotic experiments** (verify) - defined communities in germ-free hosts with measured metabolic/physiological readouts; expensive but causally strong.
- **Genome-scale reconstruction resources** - AGORA / AGORA2 (Thiele lab, ~2017 / ~2023) curated gut-microbe metabolic reconstructions, used by community models (inputs/priors, not ground truth).
- **Metagenome-function reference data** - for training/evaluating gene-content predictors (KEGG/MetaCyc pathway annotations); genetic potential, explicitly **not** realized output.
- **Public repositories** - MGnify / curatedMetagenomicData (verify) for metagenomes; MetaboLights / Metabolomics Workbench for metabolomics.

**Frozen split (leakage-safe).** The test set is fixed before modeling under **community/subject and study separation**: hold out entire subjects (never split a subject's timepoints across train and test) and, wherever possible, entire studies/cohorts, so a test community is not a batch-twin of a training community. Add a **compositional-novelty** axis (test communities with low overlap in strain/MAG content to training). For synthetic-community data, hold out entire community compositions, not individual replicates. Batch/protocol confounders are documented, and cross-study evaluation is reported separately from within-study. Split manifests are committed and hashed before any test number.

**Wet-lab gate (mandatory).** A predicted community function **cannot be established by any computation**. Confirmation requires physical measurement: anaerobic culturing of the community (or a defined reconstruction of it) followed by targeted/untargeted **metabolomics** (LC-MS/GC-MS), or a **gnotobiotic** experiment for host-context function. A defined-community + metabolomics campaign costs roughly \$20k–\$150k and weeks to months (anaerobic culture, strain sourcing, MS analysis); gnotobiotic mouse experiments are substantially more (animal facility, months). This gate is not softenable: emergence, strain variation, and context dependence are exactly the properties that observational metagenomes cannot resolve.

## 3. Standard of a genuine advance

A genuine advance is one of:
1. A **certified method contribution** - a predictor (ML on paired multi-omics, an improved community metabolic model, or a hybrid) that achieves a *new held-out result* on measured community metabolite output under a subject/study-separated split (better per-metabolite MAE / rank correlation than PICRUSt-style gene-content baselines and community-FBA baselines), with the improvement holding on compositionally novel communities and calibrated uncertainty validated on held-out data.
2. A **calibrated, falsifiable community-function prediction set** for communities an experimental partner will assay: ranked predictions of the target metabolite panel with per-community calibrated intervals, registered before the assay, with a pre-committed accuracy claim (e.g. "correct production/non-production call on ≥ $k$ of $n$ communities for butyrate").

**Not accepted as resolution:**
- A **gene-content or pathway-abundance number treated as realized function** - PICRUSt-style genetic potential is not measured metabolic output; conflating them is the field's core error.
- **In-silico-only "validation"** - internal consistency of a community FBA model, or agreement between two models, is not experimental confirmation.
- A **leakage-inflated metric** - scores driven by splitting a subject's timepoints across train/test, by batch/study twins, or by pooling correlated cohorts.
- A predictor that works only when the test community is a near-copy of a training community, presented as generally predictive of **emergent** function.
- "Solved microbiome function" claimed from any observational correlation.

## 4. Graded targets

**P1 - Reproduce baselines on our verified pipeline.** Re-run (a) a gene-content function predictor (PICRUSt2) and (b) a community metabolic model (MICOM / community FBA over AGORA reconstructions) on our frozen subject/study-separated split, and reproduce reported behavior for the target metabolite panel within tolerance. *Evidence:* committed split hashes, independent scoring, per-metabolite and per-cohort tables. Independently valuable as a leakage-audited baseline.

**P2 - Calibrated uncertainty.** Attach and validate per-metabolite predictive intervals whose coverage and expected calibration error are measured on held-out communities, per cohort and per novelty stratum, with explicit reporting of degraded calibration on compositionally novel communities. *Evidence:* reliability curves, coverage tables.

**P3 - Certified method contribution.** A method that beats P1 on measured output on the hard strata - e.g. an ML model on paired multi-omics that captures cross-feeding/context, a community model with learned interaction or uptake constraints, or a hybrid mechanistic-ML predictor - with a *statistically significant, leakage-audited* improvement. *Evidence:* paired per-community deltas with confidence intervals, ablations, no test-set tuning.

**P4 - New held-out SOTA / cross-context transfer.** Best-in-class on the committed split across the metabolite panel, including demonstrated transfer across cohorts or from defined communities to observational communities (or the reverse), and correct handling of context change. *Evidence:* full error distributions, split manifest, independent reproduction from committed code.

**P5 - Wet-lab-ready function predictions.** A ranked, calibrated slate of community-function predictions for communities a partner will culture/assay (defined communities or a gnotobiotic panel), registered before the assay, with a pre-committed falsifiable claim. *Evidence:* timestamped registration, post-hoc scoring against metabolomics, honest hit/miss accounting including emergent-behavior misses. This is the ceiling the machine reaches; closing the loop is the experiment's job.

## 5. Known results and prior art

- **PICRUSt / PICRUSt2** - Langille et al. (~2013); Douglas et al. (~2020, *Nat. Biotechnol.*): predict functional-gene abundance from marker/metagenome data - genetic potential, the standard (and standardly misused) baseline.
- **Metabolome-from-metagenome ML** - MelonnPan (Mallick, Huttenhower et al., ~2019, *Nat. Commun.*): predictive metabolomic profiling from amplicon/metagenomic features; the reference ML approach and its documented limits.
- **Community metabolic modeling** - MICOM (Diener, Gibbons, Resendis-Antonio, ~2020, *mSystems*): community-scale FBA with tradeoff regularization; SteadyCom (Chan, Maranas, ~2017); SMETANA (Zelezniak, Patil et al., ~2015); COMETS (Segrè lab, dynamic/spatial community FBA, ~2021).
- **Genome-scale reconstruction resources** - AGORA (Magnúsdóttir, Thiele et al., ~2017) and AGORA2 (Heinken et al., ~2023): curated gut-microbe reconstructions underpinning community models.
- **Synthetic / defined communities** - Venturelli-lab designs of human gut communities predicting assembly and butyrate production (Clark et al., ~2021, *Nat. Commun.*, verify); higher-order-interaction and ecological-model work.
- **Paired multi-omics resources** - HMP2 / iHMP IBD study (Lloyd-Price et al., ~2019, *Nature*); stool metabolomics (Franzosa et al., ~2019, *Nat. Microbiol.*, verify).

*Status as of mid-2026 - re-verify against current literature before starting any session.* Multi-omics microbiome ML is active; re-verify whether larger paired cohorts, strain-resolved reconstructions, or foundation microbiome models have improved emergent-function prediction, and confirm access terms and batch-confounder structure of every dataset before use.

## 6. Attack plan

**Data.** Pull a paired metagenome+metabolome cohort (HMP2/iHMP + stool metabolomics) and, where accessible, a defined-community dataset with measured outputs. Build subject/study clustering and a compositional-novelty axis; commit a **subject- and study-separated** split (never splitting a subject's timepoints), plus a labeled within-study split as an upper bound. Freeze and hash before modeling. Document batch confounders.

**Baselines.** Reproduce PICRUSt2 (gene content), MelonnPan-style ML (metabolome from features), and MICOM/community-FBA over AGORA. Score with an independent script separate from any training code, per metabolite and per cohort.

**Model.** Candidate contributions: (i) ML on paired multi-omics with cross-feeding-aware / interaction features and explicit context inputs; (ii) community metabolic models with **learned** uptake or interaction constraints fit on measured output (not just internal consistency); (iii) hybrid mechanistic-ML predictors; (iv) strain-resolved inputs to test whether strain-level gene content improves emergent-function calls.

**Calibration.** Fit and validate per-metabolite predictive intervals on held-out communities (conformal / quantile methods); report coverage and expected calibration error per cohort and per novelty stratum, foregrounding degradation on novel communities and changed contexts.

**Compute.** ML predictors and community-FBA over hundreds of reconstructions run comfortably on one prosumer GPU / CPU workstation; compute is not the bottleneck - **paired, causally clean, strain-resolved data** is. Prefer data-efficient and mechanistically informed models over scale.

**Failure modes.** (i) **Emergence** - community function is not the sum of member functions; additive gene-content models miss cross-feeding and higher-order interactions. (ii) **Strain-level variation** - species-level input hides functionally decisive strain gene-content differences. (iii) **Context dependence** - the same community produces different outputs under different nutrients/pH/oxygen/host; a context-blind model fails on context change. (iv) **Data scarcity and confounding** - paired multi-omics is scarce, cross-study batch effects are severe, and observational cohorts confound composition with host/diet. (v) **Leakage** - splitting a subject's timepoints or pooling correlated cohorts silently inflates every number.

## 7. Verification and auditability requirements

1. **Leakage-safe evaluation.** The train/test split is committed and hashed before any evaluation, under documented **subject and study separation** (no subject's timepoints split across train/test) plus a compositional-novelty axis; within-study scores are reported only as a labeled upper bound; per-metabolite and per-cohort strata are reported separately; there is no test-set tuning.
2. **Potential-vs-realized honesty.** The report explicitly distinguishes predicted **genetic potential** (gene/pathway abundance) from **realized metabolic output** (measured metabolites) and never presents the former as the latter.
3. **Calibrated uncertainty.** Every prospective prediction carries a calibrated per-metabolite interval; coverage and expected calibration error are reported on held-out communities, per cohort and per novelty stratum, with degradation on novel communities and changed contexts foregrounded.
4. **Emergence and strain accounting.** The report states, for each target function, whether an additive gene-content baseline already explains it, and quantifies the incremental value of interaction-aware, strain-resolved, or context-aware modeling - so that claims about **emergent** function are earned, not assumed.
5. **Independent reproduction.** All metrics are recomputed by a standalone script separate from training and community-model code, from the committed splits and predictions; community-model configurations (reconstructions, media, objectives) are part of the record.
6. **Cryptographic manifest, preservation, and registry.** A SHA-256 manifest covers split definitions, dataset and reconstruction version hashes, model/model-config code, and every prediction file; anything not preserved is stated explicitly. Wet-lab-ready predictions (P5) are timestamped and registered before the assay and scored afterward including misses.
7. **Honest reporting.** The report states up front that microbiome community function is reality-gated and **not resolved**; separates in-silico metrics from any culturing/metabolomics/gnotobiotic result; foregrounds emergence, strain variation, and context dependence; labels every prediction a wet-lab-pending hypothesis; and never presents an observational correlation or model-internal consistency as a real-world guarantee.
