# PROMPT FOR PREDICTING THE TISSUE-SPECIFIC SPLICING CODE AND CRYPTIC-SITE ACTIVATION

## From sequence to splice-site choice, isoform usage, and variant-induced mis-splicing

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** B - reality-gated (empirical verifier)
**Rank:** B03 of 29
**Source:** chem/bio top-50 list #35, section E (genomics)
**Modes:** `[data]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

A large fraction of pathogenic variants act not by changing a protein directly but by disrupting splicing - abolishing a canonical splice site, activating a cryptic one, or shifting isoform balance in a tissue-specific way. SpliceAI made canonical splice-site prediction from sequence startlingly good; the open edge is elsewhere: cryptic-site activation, deep-intronic variants far from annotated junctions, tissue-specific isoform usage, and the quantitative effect of a variant on percent-spliced-in (PSI). The task is to predict, from sequence and tissue context, splice-site location and usage and the effect of a variant on splicing, with calibrated uncertainty and honest handling of the tissue and cryptic-site frontiers. This is reality-gated: correctness is defined by RNA measurement (RNA-seq, minigene, saturation splicing assays), so compute can produce a certified method, a held-out benchmark result, and a ranked set of falsifiable predictions - but a minigene or a patient RNA-seq, not the model, confirms a novel splice effect. No resolution is on offer, and every clinical splice-consequence call is a hypothesis.

## 1. Exact problem statement

**Input.**

- a reference sequence window around a locus (GRCh38; GRCh37 liftover documented, failures reported);
- a tissue or cell-type label;
- for the variant task, `(chrom, pos, ref, alt)` for an SNV or small indel, explicitly including deep-intronic positions.

**Output.** Three separable predictions, each with a calibrated confidence:

1. **Splice-site prediction.** Per-position probability of being a donor, acceptor, or neither, over the window.
2. **Isoform / usage prediction.** Tissue-specific splice-site usage or PSI for annotated and cryptic junctions.
3. **Variant effect (hypothesis-labeled).** Signed change in splice-site probability and in PSI induced by the variant - including cryptic-site *gain* - with an explicit pathogenic-splicing hypothesis where clinically relevant.

**Metric.** Fixed before modeling and reported with confidence intervals:

- splice-site prediction: top-k accuracy and auPRC for donor/acceptor identification on a held-out gene set;
- usage: Spearman/Pearson between predicted and measured PSI, stratified by tissue and by canonical vs cryptic junction;
- variant effect: auPRC for splice-disrupting vs neutral (delta-score) and correlation with measured ΔPSI;
- **cryptic-gain sensitivity** reported separately - the known weak spot that aggregate numbers hide;
- calibration (ECE, reliability curves) for every probabilistic output.

**Population.** Exonic, splice-region, and deep-intronic SNVs and small indels genome-wide; canonical and cryptic sites; across the tissues represented in the atlas. Report cryptic and deep-intronic performance separately.

**Compute-tractable sub-question vs empirically-gated whole.**

- *Tractable:* given a frozen RNA-seq/minigene/saturation-splicing corpus, predict held-out splice-site usage and variant ΔPSI with calibrated uncertainty under a gene-level leakage-safe split.
- *Empirically-gated (not claimable on the machine):* that a novel deep-intronic variant causes disease-relevant mis-splicing *in the patient's tissue*.

## 2. Verifier and data

**Ground-truth sources.**

- **GTEx (v8/v10 - verify latest)** - the primary tissue RNA-seq atlas; junction reads and PSI (via LeafCutter/rMATS-style quantification) and sQTL maps.
- **Splice-site / junction annotations** - GENCODE canonical junctions as reference; observed RNA-seq junctions for cryptic sites.
- **ASCOT** (tissue-specific alternative splicing atlas, Ling et al. ~2020 - verify) and analogous PSI resources.
- **MFASS** - Multiplexed Functional Assay of Splicing via Sort-seq (Cheung et al., ~2019 - verify) - thousands of exonic variants scored for splice disruption; a near-direct causal readout.
- **Vex-seq** (Adamson et al., ~2018 - verify) and minigene/saturation-splicing datasets, including saturation genome editing of splice regions (verify specific accessions).
- **ClinVar** splice-annotated variants and RNA-confirmed splicing outcomes (filter by review status and by presence of RNA evidence).

**Frozen, leakage-safe split.** Commit and hash before modeling.

- **Gene-level and chromosome holdout:** hold out entire genes/chromosomes so no test junction shares local sequence with a training junction.
- **Paralog holdout:** splice motifs are conserved across paralogous genes; cluster paralogs and keep clusters on one side of the split, or metrics leak via sequence similarity.
- **Tissue holdout** for tissue-specific claims: evaluate generalization to a held-out tissue, not only held-out genes within seen tissues.
- **Ancestry considerations:** GTEx and most splicing corpora are European-ancestry-heavy; sQTL effect sizes and rare-variant spectra differ by ancestry. State this as a label-distribution limitation.

**Negative controls and label caveats.** Fixed before modeling:

- neutral variants matched for distance-to-junction, to bound the trivial "near a splice site" signal;
- label-shuffled runs to bound leakage/memorization;
- low-coverage junctions down-weighted or excluded, with the threshold documented.

**Wet-lab gate (mandatory).** No novel splice-altering claim is established without RNA measurement: a minigene / splicing-reporter assay, patient or cell-line RNA-seq, or a saturation-splicing assay for the region. Indicative cost: a single-variant minigene assay runs a few hundred to low-thousands USD and weeks of work; targeted RNA-seq validation of a handful of variants runs low-thousands USD; an MFASS/saturation-splicing library covering thousands of variants runs tens of thousands USD. Deep-intronic and cryptic-gain predictions especially cannot be confirmed in silico. This gate is not optional and must not be softened.

## 3. Standard of a genuine advance

A genuine advance is one or more of:

- a **certified pipeline** reproducing a named SOTA splicing model (SpliceAI, Pangolin) on the frozen, leakage-safe split, independently runnable;
- a **new held-out SOTA** on a pre-registered split for a frontier slice - cryptic-site gain, deep-intronic variants, or tissue-specific PSI - with calibration and tissue stratification;
- a **method contribution** that measurably improves cryptic-site or deep-intronic sensitivity, or that predicts quantitative ΔPSI (not just binary disruption) with calibrated error;
- a **ranked, calibrated, falsifiable prediction set** of candidate splice-altering variants with tissue-specific ΔPSI hypotheses and the minigene/RNA-seq assay that would refute each.

**Not accepted as resolution.**

- A canonical-junction accuracy number presented as covering the cryptic/deep-intronic problem it excludes.
- A variant "validated" only by agreement with another splicing predictor.
- A pathogenic-splicing call issued as a determination rather than a hypothesis.
- A metric obtained on a split that leaks via paralogs or shared genes.
- Tissue-averaged results dressed as tissue-specific prediction.

## 4. Graded targets

**P0 - Frozen, hashed corpus and split.** Assemble the RNA-seq/functional label sets and commit the gene-/paralog-/tissue-holdout split with a provenance manifest before modeling.
*Evidence:* SHA-256 manifest, versioned accessions, written split rationale.

**P1 - Reproduce SOTA on the frozen split.** Rebuild SpliceAI and/or Pangolin inference with our own verified code; match the reported splice-site metric on the committed split.
*Evidence:* reproducible metrics, hashed split, side-by-side with the published number.

**P2 - Calibrated variant ΔPSI.** On held-out MFASS/minigene/sQTL data, predict signed ΔPSI with calibrated uncertainty; report Spearman by canonical vs cryptic and by tissue.
*Evidence:* reliability curves on held-out data; leakage ablation.

**P3 - Certified method / new held-out SOTA on the frontier.** Beat the reproduced baseline on cryptic-gain or deep-intronic prediction, or on held-out-tissue PSI, on a pre-registered split.
*Evidence:* benchmark-integrity statement; tissue and cryptic/canonical stratification.

**P4 - Falsifiable prediction set for a partner.** A ranked, calibrated list of candidate splice-altering variants (emphasizing deep-intronic and cryptic-gain cases) with tissue-specific ΔPSI hypotheses and the exact assay that would refute each.
*Evidence:* the list, its prior held-out calibration, and a pre-registered success criterion. Every entry labeled a wet-lab-pending hypothesis.

## 5. Known results and prior art

- **SpliceAI** (Jaganathan et al., ~2019) - 32-layer dilated residual network predicting donor/acceptor from ~10 kb of sequence; the landmark that made canonical splice-site prediction from sequence highly accurate and remains the standard delta-score for variant effect.
- **Pangolin** (Zeng & Li, ~2022) - extends the approach across multiple tissues and species and predicts splice-site *usage*, improving quantitative and tissue-specific prediction.
- **MMSplice** (Cheng et al., ~2019) - modular neural model composing effects on exon/intron modules for variant splicing prediction.
- **Borzoi** (Linder et al., Calico, ~2023–2024 - verify) - RNA-seq coverage prediction that captures splicing-adjacent signal.
- **Tissue-specific and transformer splicing models** (verify current names) - an active frontier for cryptic and tissue-specific prediction.
- **Functional corpora:** MFASS (Cheung et al., ~2019 - verify), Vex-seq (Adamson et al., ~2018 - verify), ASCOT tissue-splicing atlas (Ling et al., ~2020 - verify); GTEx sQTLs for population-scale splicing effects.

**Status as of mid-2026 - re-verify against current literature before starting any session.** Confirm current model names, releases, and the availability and accessions of the saturation-splicing corpora before committing.

## 6. Attack plan

Concrete first steps, in order:

1. **Assemble the frozen corpus.** Pull GTEx junction/PSI and sQTL data as the anchor label set; MFASS/Vex-seq (verify availability) as the near-causal variant readout; GENCODE for canonical annotation and RNA-seq-derived junctions for cryptic sites; ClinVar RNA-confirmed splice variants as clinical anchors. Record versions.
2. **Construct the leakage-safe split.** Commit gene-, chromosome-, paralog-, and tissue-holdout splits; hash the manifest. Cluster paralogs explicitly so conserved motifs do not leak.
3. **Reproduce a baseline.** Reimplement SpliceAI/Pangolin inference in PyTorch and match the reported splice-site metric before attempting any improvement.
4. **Model the contribution.** Try longer-context or foundation-model sequence encoders with a calibrated tissue-conditioned head aimed specifically at cryptic-gain and deep-intronic sensitivity and at quantitative ΔPSI.
5. **Calibrate.** Fit temperature scaling / isotonic regression on held-out data and report the calibration (reliability curves, ECE), not just point metrics.
6. **Negative controls.** Distance-matched neutral variants and label-shuffled runs to bound the trivial and leaked signal.

**One-GPU scope.** SpliceAI-scale training fits a single prosumer GPU; longer-context or foundation-model backbones may not - flag it and use released weights for those.

**Failure modes to expect and report:**

- paralog leakage inflating splice-site accuracy;
- poor cryptic-gain sensitivity masked by canonical-junction accuracy;
- deep-intronic distribution shift far from annotated junctions;
- tissue-transfer failure to unseen tissues;
- label noise from low-coverage junctions.

State each explicitly where it bites, and quantify its impact where the controls allow.

## 7. Verification and auditability requirements

1. **Leakage-safe evaluation.** Gene-, chromosome-, paralog-, and tissue-holdout splits committed and hashed before evaluation; no test-set tuning; paralog clustering documented.
2. **Calibrated uncertainty.** Every prospective splice-site, PSI, and variant-effect prediction carries a calibrated confidence; calibration reported on held-out data with reliability curves and ECE.
3. **Frontier stratification and fairness.** Cryptic/canonical, deep-intronic, and per-tissue metrics reported separately; ancestry/label-distribution bias of the corpora stated; aggregate numbers never used to hide the frontier.
4. **Causal honesty.** sQTL colocalization never reported as established mechanism; variant splice effects labeled as assay-pending hypotheses.
5. **Independent reproduction.** Metrics reproducible from the committed split and code by a separate script; SHA-256 manifest over data version hashes, code, and predictions.
6. **Preservation.** Model weights or weight provenance, training/inference code, and dataset version hashes are part of the record; anything not preserved is stated explicitly.
7. **Honest reporting.** The report states up front that the problem is reality-gated and NOT resolved; separates in-silico metrics from any RNA validation; labels every splice-consequence call a minigene-/RNA-seq-pending hypothesis; and never presents a benchmark number as a clinical guarantee.
