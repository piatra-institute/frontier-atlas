# PROMPT FOR JOINT PREDICTION OF CRISPR GUIDE EFFICIENCY, OFF-TARGET, AND REPAIR OUTCOME

## One calibrated model of on-target activity, specificity, and edit outcome across cell types

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** B - reality-gated (empirical verifier)
**Rank:** B12 of 29
**Source:** chem/bio top-50 list #39, section E (genomics)
**Modes:** `[data]` `[func]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Therapeutic genome editing is gated by three predictions that are usually made by separate tools: how efficiently a guide cuts (on-target activity), where else it cuts (off-target specificity), and what edit results at the intended site (repair outcome - the indel or precise-edit distribution). Each has a strong single-task model, but the therapeutically decisive quantity is their *joint* behavior in the *target cell type*: a guide that is efficient, specific, and produces the desired repair outcome. The task is to predict all three jointly, with calibrated uncertainty and explicit cell-type conditioning, and to rank guides by a therapeutically meaningful composite. This is reality-gated: correctness is defined by editing screens and sequencing assays, so compute can produce a certified method, a held-out benchmark result, and a ranked set of falsifiable guide predictions - but amplicon sequencing and GUIDE-seq/CIRCLE-seq in the actual target cell type, not the model, confirm a novel editing outcome. No resolution is on offer; every guide recommendation is a hypothesis pending experimental validation.

## 1. Exact problem statement

**Input.**

- a guide/target specification: protospacer + PAM, and target-site genomic context (GRCh38);
- the nuclease/editor (SpCas9, high-fidelity variants, base or prime editor - scope stated);
- a cell-type / DNA-repair context label.

**Output.** Three coupled predictions plus a composite, each with a calibrated confidence:

1. **On-target efficiency.** Predicted editing activity of the guide at its intended site.
2. **Off-target profile.** Ranked candidate off-target sites with predicted cleavage/edit probability, genome-wide.
3. **Repair-outcome distribution.** The predicted distribution over edit outcomes at the target site - indel spectrum for nuclease editing, or precise-edit vs byproduct frequencies for base/prime editing - as a calibrated probability distribution `[func]`.
4. **Joint guide ranking.** A therapeutically meaningful composite (efficiency × specificity × desired-outcome probability) with propagated uncertainty.

**Metric.** Fixed before modeling and reported with confidence intervals:

- on-target: Spearman against measured efficiency;
- off-target: auPRC and top-k recall against experimentally validated off-target sites;
- repair outcome: correlation of predicted vs observed outcome frequencies, KL divergence / earth-mover distance between predicted and observed distributions, and top-outcome accuracy;
- composite: calibrated ranking quality against a held-out therapeutic-relevance criterion;
- calibration (ECE, reliability curves) throughout, including for the distributional output.

**Population.** Guides genome-wide for the stated nuclease/editor, across the cell types represented in the screens. Report per-cell-type performance separately - repair outcomes and off-target activity are cell-type-dependent.

**Compute-tractable sub-question vs empirically-gated whole.**

- *Tractable:* given frozen efficiency screens, off-target assays, and repair-outcome corpora, predict held-out on-target activity, off-target ranking, and outcome distributions with calibrated uncertainty under a guide-/site-/cell-type-holdout split.
- *Empirically-gated (not claimable on the machine):* that a specific guide is safe and effective in a specific therapeutic cell type.

## 2. Verifier and data

**Ground-truth sources.**

- **Guide-efficiency screens** - pooled on-target activity datasets (the Doench/Azimuth training screens and successors; tiling screens - verify accessions).
- **Off-target assays** - GUIDE-seq (Tsai et al., ~2015), CIRCLE-seq (Tsai et al., ~2017), CHANGE-seq (Lazzarotto et al., ~2020 - verify), and validated off-target site sets.
- **Repair-outcome corpora** - the training data behind inDelphi, FORECasT, and Lindel: thousands of target sites with measured indel-outcome distributions (Shen et al.; Allen et al.; Chen et al. - verify accessions).
- **Base/prime-editing outcome data** - BE-Hive (Arbab et al., ~2020 - verify) and prime-editing outcome datasets (PRIDICT / related, ~2023 - verify), if base/prime editing is in scope.

**Frozen, leakage-safe split.** Commit and hash before modeling.

- **Guide/target-site holdout:** hold out whole guides and their genomic neighborhoods; near-duplicate target sites must not straddle the split.
- **Gene / genomic-region holdout:** for off-target evaluation, hold out whole genomic regions so off-target neighborhoods do not leak between train and test.
- **Cell-type holdout:** to test cell-type generalization honestly, evaluate on held-out cell types, not only held-out guides in seen cell types.
- **Ancestry/reference considerations:** off-target profiles depend on the individual genome (SNPs create or destroy off-target sites). Reference-genome-only off-target predictions miss allele-specific off-targets; state this and, where possible, evaluate against personal-genome-aware assays.

**Negative controls and label caveats.** Fixed before modeling:

- non-targeting and mismatched-guide controls to bound the trivial signal in efficiency and off-target scores;
- label-shuffled runs to bound leakage/memorization across near-duplicate guides;
- screen-batch effects checked and reported, since pooled screens carry strong batch structure.

**Wet-lab gate (mandatory).** No novel editing-outcome or safety claim is established without new sequencing in the relevant cell type: targeted amplicon deep sequencing for on-target efficiency and repair outcome, and GUIDE-seq/CIRCLE-seq/CHANGE-seq for genome-wide off-target discovery. Indicative cost: amplicon sequencing of a panel of guides in one cell type runs low-thousands to tens-of-thousands USD depending on scale; a genome-wide off-target assay (GUIDE-seq/CHANGE-seq) runs several thousand USD per guide and weeks of work; therapeutic-cell-type validation (primary cells, iPSC-derived) is costlier still. This gate is not optional and must not be softened.

## 3. Standard of a genuine advance

A genuine advance is one or more of:

- a **certified pipeline** reproducing named SOTA single-task models (Azimuth/Rule Set 2, a GUIDE-seq-trained off-target model, inDelphi/FORECasT/Lindel) on the frozen, leakage-safe split, independently runnable;
- a **new held-out SOTA** on a pre-registered split for one task, or - the distinctive contribution - a **joint model** that predicts efficiency, off-target, and repair outcome coherently and improves the composite guide ranking against a held-out therapeutic criterion;
- a **method contribution** on cell-type dependence: predicting how repair-outcome distributions and off-target activity shift across cell types, with calibrated distributional uncertainty;
- a **ranked, calibrated, falsifiable guide set** for a target locus with joint efficiency/specificity/outcome hypotheses and the exact sequencing assay that would refute each.

**Not accepted as resolution.**

- A single-task leaderboard number presented as a therapeutic-readiness guarantee.
- A guide "validated" only in silico or by another predictor.
- A reference-genome-only off-target prediction presented as a genome-wide safety claim.
- A repair-outcome point estimate reported without its calibrated distribution.
- A metric obtained on a split that leaks via near-duplicate guides or shared genomic regions.
- Aggregate cross-cell-type numbers used to imply cell-type-specific skill.

## 4. Graded targets

**P0 - Frozen, hashed corpus and split.** Assemble the efficiency, off-target, and repair-outcome label sets and commit the guide-/region-/cell-type-holdout split with a provenance manifest before modeling.
*Evidence:* SHA-256 manifest, versioned accessions, written split rationale.

**P1 - Reproduce SOTA single-task models on the frozen split.** Rebuild Azimuth (efficiency), an off-target scorer, and inDelphi/FORECasT/Lindel (repair) with our own verified code; match reported metrics on the committed split.
*Evidence:* reproducible metrics, hashed split, side-by-side with published numbers.

**P2 - Calibrated distributional repair prediction.** On held-out sites, predict the full repair-outcome distribution with calibrated uncertainty; report KL / earth-mover distance and top-outcome accuracy per cell type.
*Evidence:* reliability of distributional predictions on held-out data; leakage ablation.

**P3 - Certified joint model / new held-out SOTA.** A single model predicting efficiency, off-target, and repair jointly that improves the composite ranking against a held-out therapeutic criterion, or a new SOTA on cell-type-transfer repair prediction, on a pre-registered split.
*Evidence:* benchmark-integrity statement; per-cell-type stratification.

**P4 - Falsifiable guide set for a partner.** For a target locus, a ranked, calibrated guide list with joint efficiency/specificity/outcome hypotheses and the amplicon-seq / GUIDE-seq assays that would refute each.
*Evidence:* the list, its prior held-out calibration, and a pre-registered success criterion. Every entry labeled a wet-lab-pending hypothesis.

## 5. Known results and prior art

- **Rule Set 2 / Azimuth** (Doench et al., ~2016) - SpCas9 on-target efficiency; the standard efficiency baseline.
- **DeepCRISPR** (Chuai et al., ~2018) - deep learning for on- and off-target activity.
- **inDelphi** (Shen et al., ~2018 - verify full authorship; Sherwood/Gifford groups) - repair-outcome (indel distribution) prediction.
- **FORECasT** (Allen et al., ~2019) and **Lindel** (Chen et al., ~2019) - repair-outcome prediction; the standard indel-outcome baselines.
- **Off-target assays and models** - GUIDE-seq (Tsai et al., ~2015), CIRCLE-seq (Tsai et al., ~2017), CHANGE-seq (Lazzarotto et al., ~2020 - verify); CFD and deep off-target scorers.
- **Base/prime-editing outcome models** - BE-Hive (Arbab et al., ~2020 - verify); PRIDICT / prime-editing outcome models (~2023 - verify).
- **Open parts:** cell-type dependence of repair and off-target activity, personal-genome-aware off-target prediction, and the *joint* efficiency × specificity × repair framing - none of these is closed.

**Status as of mid-2026 - re-verify against current literature before starting any session.** Confirm current model names, editor variants, and dataset accessions before committing.

## 6. Attack plan

Concrete first steps, in order:

1. **Assemble the frozen corpus.** Pull a guide-efficiency screen, a GUIDE-seq/CHANGE-seq off-target set, and the inDelphi/FORECasT/Lindel repair-outcome corpora as the three anchor label sets (verify accessions); base/prime-editing outcome data if in scope. Record versions.
2. **Construct the leakage-safe split.** Commit guide-, genomic-region-, and cell-type-holdout splits; hash the manifest. De-duplicate near-identical guides across the split.
3. **Reproduce baselines.** Reimplement the single-task baselines in PyTorch and match reported metrics before attempting any improvement.
4. **Model the contribution.** Build a shared-encoder multi-task/joint model with a distributional repair-outcome head (learned outcome distribution `[func]`) and a cell-type-conditioned component; propagate uncertainty into the composite ranking.
5. **Calibrate.** Calibrate each head, including the distributional output, on held-out data and report the calibration (reliability curves, ECE).
6. **Negative controls.** Non-targeting / mismatched-guide controls and label-shuffled runs to bound trivial and leaked signal; evaluate off-target ranking against validated sites, not just reference candidates.

**One-GPU scope.** These models fit a single prosumer GPU; genome-wide off-target *candidate enumeration* is the compute-heavy step and is CPU/IO-bound - flag it.

**Failure modes to expect and report:**

- near-duplicate-guide leakage inflating efficiency and off-target metrics;
- reference-only off-target blind spots (allele-specific off-targets);
- cell-type-transfer failure in repair distributions;
- miscalibrated distributional outputs;
- screen-specific batch effects masquerading as signal.

State each explicitly where it bites, and quantify its impact where the controls allow.

## 7. Verification and auditability requirements

1. **Leakage-safe evaluation.** Guide-, genomic-region-, and cell-type-holdout splits committed and hashed before evaluation; near-duplicate guides de-duplicated across the split; no test-set tuning.
2. **Calibrated uncertainty.** Every prospective efficiency, off-target, and repair-outcome prediction carries calibrated confidence - including the full repair-outcome distribution; calibration reported on held-out data with reliability curves and ECE.
3. **Cell-type and genome-context fairness.** Per-cell-type metrics reported separately; reference-genome-only off-target limitations and allele-/ancestry-specific off-target risk stated; aggregate numbers never used to imply cell-type-specific skill.
4. **Joint-vs-single honesty.** The composite ranking's uncertainty is propagated from all three components; single-task wins never reported as therapeutic-readiness.
5. **Independent reproduction.** Metrics reproducible from the committed split and code by a separate script; SHA-256 manifest over data version hashes, code, and predictions.
6. **Preservation.** Model weights or weight provenance, training/inference code, and dataset version hashes are part of the record; anything not preserved is stated explicitly.
7. **Honest reporting.** The report states up front that the problem is reality-gated and NOT resolved; separates in-silico metrics from any sequencing validation; labels every guide recommendation an amplicon-seq-/GUIDE-seq-pending hypothesis; and never presents a benchmark number as a therapeutic guarantee.
