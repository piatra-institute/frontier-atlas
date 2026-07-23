# PROMPT FOR PREDICTING ENHANCER ACTIVITY AND 3D CHROMATIN CONTACTS FROM SEQUENCE

## The regulatory / non-coding genome code: cell-type-specific activity and long-range architecture

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** B - reality-gated (empirical verifier)
**Rank:** B04 of 29
**Source:** chem/bio top-50 list #34, section E (genomics)
**Modes:** `[data]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

> **Audit note (July 2026 - see `../../STATUS_AUDIT_2026-07.md`):** SOTA moved decisively in 2025. **AlphaGenome** (DeepMind; Nature 2025) is a unified 1-Mb DNA→function model reporting SOTA on 22/24 genome-track tasks and 25/26 variant-effect tasks - it supersedes the Enformer/Borzoi framing used below as the baseline to beat. The problem is not resolved (enhancer causality is wet-gated; unseen-enhancer accuracy is unsolved), but re-baseline P1 against AlphaGenome before claiming any contribution.

### Abstract

The regulatory genome - enhancers, promoters, insulators, and the 3D folding that brings them together - encodes when and where each gene is expressed. Enformer-class models predict epigenomic tracks from sequence well and 3D contact maps (Akita, Orca) with real skill, yet two things remain hard and important: cell-type-specific enhancer *activity* (as opposed to averaged chromatin state) and long-range enhancer–gene effects, where sequence models are known to underperform. The task is to predict, from sequence, enhancer activity and 3D chromatin contacts with cell-type resolution and calibrated uncertainty, and to connect predicted regulatory activity to a causal enhancer–gene effect. This is reality-gated: correctness is defined by ENCODE/Roadmap assays, Hi-C/Micro-C maps, MPRA, and CRISPRi perturbations, so compute can produce a certified method, a held-out benchmark result, and a ranked set of falsifiable predictions - but an MPRA or a CRISPRi screen, not the model, confirms that a sequence is a functional enhancer. No resolution is on offer; every enhancer-function claim is a hypothesis.

## 1. Exact problem statement

**Input.**

- a reference sequence window (GRCh38); long-range tasks require tens to hundreds of kb of context, and multiscale 3D tasks require up to whole-chromosome context;
- a cell-type / tissue label.

**Output.** Three separable predictions, each with a calibrated confidence:

1. **Epigenomic / activity tracks.** Per-cell-type profiles - DNase/ATAC accessibility, histone marks, TF binding, CAGE, and RNA-seq coverage - at the model's resolution.
2. **3D contact prediction.** Predicted Hi-C / Micro-C contact maps (or contact-frequency features) for the locus and cell type.
3. **Enhancer activity and enhancer–gene effect (hypothesis-labeled).** Predicted MPRA-style enhancer activity for a candidate element, and a predicted causal effect of the enhancer on a target gene, framed as a computational hypothesis.

**Metric.** Fixed before modeling and reported with confidence intervals:

- tracks: Pearson correlation across the genome and, separately, *across cell types at fixed loci* - the harder cell-type-specificity test;
- 3D contacts: stratum-adjusted correlation (SCC) and distance-stratified Pearson on held-out loci;
- enhancer activity: Spearman against measured MPRA activity;
- enhancer–gene links: auPRC for CRISPRi-validated links;
- calibration (ECE, reliability curves) for every probabilistic output.

**Population.** Regulatory elements genome-wide across the cell types/tissues in the epigenome atlases; report long-range (distal enhancer) and cell-type-specificity performance *separately* - these are the frontier and aggregate numbers hide them.

**Compute-tractable sub-question vs empirically-gated whole.**

- *Tractable:* given frozen ENCODE/Hi-C/MPRA corpora, predict held-out tracks, contact maps, and MPRA activity with calibrated uncertainty under a chromosome- and cell-type-holdout split.
- *Empirically-gated (not claimable on the machine):* that a specific sequence is a functional enhancer for a specific gene in a specific cell type.

## 2. Verifier and data

**Ground-truth sources.**

- **ENCODE** and **Roadmap Epigenomics** - DNase/ATAC, histone ChIP, TF ChIP across many cell types; the primary track label source.
- **Hi-C / Micro-C** contact maps (ENCODE, 4D Nucleome - verify current releases) - 3D architecture labels.
- **MPRA enhancer-activity atlases** - massively parallel reporter assays of enhancer activity (including lentiMPRA / STARR-seq datasets - verify accessions); the near-causal activity readout.
- **CAGE (FANTOM5)** - promoter/enhancer transcription initiation; enhancer RNA as an activity proxy.
- **CRISPRi enhancer-screen data** (genome-wide / locus CRISPRi enhancer–gene mapping - verify specific datasets) - the closest thing to a causal enhancer–gene link.
- **ABC-model** enhancer–gene predictions and their validation data as an orthogonal baseline (verify).

**Frozen, leakage-safe split.** Commit and hash before modeling.

- **Chromosome holdout:** hold out entire chromosomes so no test locus shares local sequence with training; standard for this class of model.
- **Cell-type holdout:** to test cell-type specificity honestly, evaluate on held-out cell types, not only held-out loci in seen cell types.
- **Element holdout** for MPRA: hold out whole elements, not positions within an element.
- **Ancestry considerations:** epigenome atlases derive largely from a limited set of (often European-ancestry) cell lines and donors; regulatory activity can be donor- and ancestry-context-dependent. State this as a label-distribution limitation.

**Negative controls and label caveats.** Fixed before modeling:

- GC- and accessibility-matched inactive sequences as a null class for enhancer-activity calls;
- distance-matched non-interacting locus pairs as the null for enhancer–gene links;
- label-shuffled runs to bound leakage/memorization, and a batch-effect check across assay labs.

**Wet-lab gate (mandatory).** No enhancer-function or enhancer–gene claim for a novel element is established without a new physical experiment: an MPRA / STARR-seq or episomal reporter assay for activity, or CRISPRi/CRISPRa perturbation to test the causal effect on the target gene in the relevant cell type. Indicative cost: an MPRA library covering thousands of candidate elements runs roughly tens of thousands of USD in reagents and sequencing; a locus-scale CRISPRi enhancer screen runs tens of thousands USD and months of work; single-element reporter validation runs low-thousands USD each. This gate is not optional and must not be softened.

## 3. Standard of a genuine advance

A genuine advance is one or more of:

- a **certified pipeline** reproducing a named SOTA sequence-to-function or sequence-to-contact model (Enformer, Borzoi, Akita, Orca) on the frozen, leakage-safe split, independently runnable;
- a **new held-out SOTA** on a pre-registered split for a frontier slice - cross-cell-type track prediction, distal-enhancer effect, or held-out-cell-type contact prediction - with calibration and cell-type stratification;
- a **method contribution** that measurably improves long-range enhancer–gene prediction or cell-type specificity, addressing the known weakness that current models underuse distal enhancers;
- a **ranked, calibrated, falsifiable prediction set** of candidate enhancers and enhancer–gene links with activity hypotheses and the MPRA/CRISPRi assay that would refute each.

**Not accepted as resolution.**

- A genome-wide track-correlation number presented as demonstrating cell-type-specific enhancer prediction it does not test.
- An enhancer "validated" only by another predictor or by chromatin state alone.
- A predicted enhancer–gene link reported as an established causal mechanism.
- A metric obtained on a split that leaks via shared loci or homologous sequence.
- Distance-inflated contact-map correlations reported without distance stratification.

## 4. Graded targets

**P0 - Frozen, hashed corpus and split.** Assemble the track/contact/MPRA/CRISPRi label sets and commit the chromosome-/cell-type-holdout split with a provenance manifest before modeling.
*Evidence:* SHA-256 manifest, versioned accessions, written split rationale.

**P1 - Reproduce SOTA on the frozen split.** Rebuild inference for Enformer/Borzoi (tracks) and Akita/Orca (contacts) with our own verified code; match reported metrics on the committed chromosome-holdout split.
*Evidence:* reproducible metrics, hashed split, side-by-side with published numbers.

**P2 - Calibrated cell-type-specific prediction.** On held-out cell types, predict tracks and MPRA activity with calibrated uncertainty; report cross-cell-type Pearson and Spearman.
*Evidence:* reliability curves on held-out data; leakage ablation.

**P3 - Certified method / new held-out SOTA on the frontier.** Beat the reproduced baseline on distal-enhancer effect, cross-cell-type prediction, or held-out-cell-type contacts, on a pre-registered split.
*Evidence:* benchmark-integrity statement; cell-type and distance stratification.

**P4 - Falsifiable prediction set for a partner.** A ranked, calibrated list of candidate enhancers and enhancer–gene links with activity hypotheses and the exact MPRA/CRISPRi assay that would refute each.
*Evidence:* the list, its prior held-out calibration, and a pre-registered success criterion. Every entry labeled a wet-lab-pending hypothesis.

## 5. Known results and prior art

- **Enformer** (Avsec et al., ~2021) - transformer with ~200 kb receptive field predicting thousands of epigenomic and CAGE tracks from sequence; the reference sequence-to-function model.
- **Borzoi** (Linder et al., Calico, ~2023–2024 - verify) - extends the approach to RNA-seq coverage / expression.
- **Akita** (Fudenberg et al., ~2020) - predicts Hi-C/Micro-C contact maps from ~1 Mb of sequence.
- **Orca** (Zhou, ~2022) - multiscale 3D genome contact prediction from sequence, up to chromosome scale.
- **Sei** (Chen et al., ~2022) - sequence-class framework organizing regulatory activity; **Basenji/Basenji2** (Kelley et al.) - Enformer predecessors; **BPNet/ChromBPNet** (Avsec et al., ~2021) - base-resolution TF-binding and accessibility.
- **ABC model** (Fulco/Engreitz et al., ~2019 - verify) - activity-by-contact enhancer–gene prediction, a strong non-deep-learning baseline.
- **Known frontier limitation:** studies (Karollus et al., ~2023; Sasse et al., ~2023 - verify) show current sequence models struggle to predict the effect of distal enhancers and inter-individual expression variation - the defining open problem here.

**Status as of mid-2026 - re-verify against current literature before starting any session.** Confirm current model names, releases, and the availability of MPRA/CRISPRi and 4D Nucleome datasets before committing.

## 6. Attack plan

Concrete first steps, in order:

1. **Assemble the frozen corpus.** Pull ENCODE tracks and Hi-C/Micro-C maps as the anchor label sets; an MPRA enhancer-activity atlas and a CRISPRi enhancer-screen dataset (verify accessions) as the near-causal readouts; FANTOM5 CAGE as an activity proxy; ABC-model outputs as an orthogonal baseline. Record versions.
2. **Construct the leakage-safe split.** Commit chromosome-, cell-type-, and element-holdout splits; hash the manifest. Fix a distance-stratification scheme for all contact-map metrics up front.
3. **Reproduce baselines.** Reimplement Enformer/Borzoi and Akita/Orca inference in PyTorch and match reported metrics before attempting any improvement.
4. **Model the contribution.** Target the distal-enhancer and cell-type-specificity weakness - longer effective context, explicit contact-conditioned activity heads, or foundation-model encoders - always scored on held-out cell types and CRISPRi-validated links, not on averaged chromatin state.
5. **Calibrate.** Fit calibration on held-out data and report it (reliability curves, ECE), not just point metrics.
6. **Negative controls.** GC/accessibility-matched inactive sequences, distance-matched non-interacting pairs, and label-shuffled runs to bound trivial and leaked signal.

**One-GPU scope.** Enformer/Borzoi/Orca-class *training* exceeds a single prosumer GPU - flag this: use released weights for inference/embedding and restrict on-GPU work to head training, fine-tuning, and evaluation.

**Failure modes to expect and report:**

- locus leakage inflating track correlations;
- distance inflation of contact-map correlations when not distance-stratified;
- distal-enhancer underuse - the model ignoring far elements;
- cell-type-transfer failure to unseen cell types;
- cell-line-limited, ancestry-narrow label distributions.

State each explicitly where it bites, and quantify its impact where the controls allow.

## 7. Verification and auditability requirements

1. **Leakage-safe evaluation.** Chromosome-, cell-type-, and element-holdout splits committed and hashed before evaluation; no test-set tuning; contact-map metrics distance-stratified.
2. **Calibrated uncertainty.** Every prospective track, contact, and enhancer-activity prediction carries a calibrated confidence; calibration reported on held-out data with reliability curves and ECE.
3. **Cell-type-specificity and fairness.** Cross-cell-type and distal-enhancer metrics reported separately; cell-line/ancestry limitations of the atlases stated; averaged-chromatin numbers never used to imply cell-type-specific skill.
4. **Causal honesty.** Predicted enhancer–gene links never reported as established mechanism; enhancer-function claims labeled as MPRA/CRISPRi-pending hypotheses.
5. **Independent reproduction.** Metrics reproducible from the committed split and code by a separate script; SHA-256 manifest over data version hashes, code, and predictions.
6. **Preservation.** Model weights or weight provenance, training/inference code, and dataset version hashes are part of the record; anything not preserved is stated explicitly.
7. **Honest reporting.** The report states up front that the problem is reality-gated and NOT resolved; separates in-silico metrics from any experimental validation; labels every enhancer call a wet-lab-pending hypothesis; and never presents a benchmark number as a real-world guarantee.
