# PROMPT FOR FOLD-SWITCHING (METAMORPHIC) PROTEIN PREDICTION

## Detecting the switch and predicting both folds, where single-structure models fail by construction

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** B - reality-gated (empirical verifier)
**Rank:** B-08 of 29
**Source:** chem/bio top-50 list #17, section C (beyond static structure)
**Modes:** `[struct]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

A small but genuine class of proteins - metamorphic, or fold-switching - adopt two (or more) distinct, well-ordered native folds and interconvert between them in response to temperature, binding, concentration, pH, or redox state. This is a hidden layer of regulation (timing in KaiB, transcriptional antitermination in RfaH, mitotic checkpoint in Mad2), and it is precisely the case AlphaFold2 cannot handle by construction: trained to map a sequence and its evolutionary average to a *single* structure, it returns one fold and hides the other. The task is two-part: **detect** which sequences are fold-switchers, and **predict both folds and the switch region**, ideally with the environmental trigger. MSA-subsampling and cluster-based tricks (AF-Cluster) recover alternate states for known cases but are unreliable and untested on true blind discovery. The class is **reality-gated by two bottlenecks at once**: the ground-truth catalogue of confirmed metamorphic proteins is tiny (extreme data scarcity), and confirming a *new* fold-switch requires experimental structure determination of both states under both conditions. Compute can produce a certified detector, a two-fold predictor benchmarked on the curated set, and a ranked list of candidate fold-switchers for experimental testing; it cannot certify a new metamorph. The honest deliverable is exactly that advance.

## 1. Exact problem statement

**Detection sub-problem.**
- *Input:* a protein sequence $s$ (with MSA), no conformational label.
- *Output:* a calibrated probability that $s$ is fold-switching, and - if positive - the predicted **switch region** (the residues whose secondary structure/topology changes between states).
- *Metric:* precision/recall and AUPRC against the curated metamorphic set vs. a matched single-fold negative population; switch-region localization scored by overlap (IoU) with the experimentally annotated region.

**Two-fold structure sub-problem.**
- *Input:* a sequence known (or predicted) to be metamorphic, optionally with the condition label.
- *Output:* two (or more) ranked full-atom models, one per experimentally known state, each with **calibrated confidence**, plus the switch-region assignment.
- *Metric:* for each known state $X^{(a)}$, the best-of-ensemble TM-score $\mathrm{TM}(\hat X, X^{(a)})$ and lDDT; and a **joint** score requiring *both* states be recovered above threshold by *distinct* models (recovering only the dominant fold, as AF2 does, scores zero on the joint metric),
$$\mathrm{Joint} = \min_a \max_{\hat X \in \text{ensemble}} \mathrm{TM}(\hat X, X^{(a)}).$$
Secondary-structure switch recovery (fraction of switch-region residues assigned the correct SS in each state) is reported.

**Population.** The curated set of experimentally confirmed metamorphic proteins (both states solved), stratified by switch type (order↔order, ligand-induced, oligomerization-coupled) and by whether close homologs appear in training. Because the set is tiny, cross-validation is by protein cluster with leave-family-out folds; aggregate numbers over so few examples are reported with explicit per-protein tables, never as a single headline.

**Compute-tractable sub-question.** On the frozen curated set under leave-family-out separation, (a) detect fold-switchers above a named baseline AUPRC with calibrated probability, and (b) recover both folds on the joint metric above a named baseline.

**Empirically-gated whole.** Discover a *previously unknown* fold-switcher and have both of its folds confirmed experimentally under their respective conditions. No predictor closes this - only structure determination of both states does.

## 2. Verifier and data

**Ground-truth source.**
- **The curated metamorphic / fold-switching database** - the Porter–Looger set and its successors (Porter & Looger; Chakravarty & Porter; verify current name/version, e.g. a "fold-switching proteins" curated list). This is the primary truth for detection.
- **PDB** - the experimental structures of *both* states for each confirmed case (the paired-fold coordinates); e.g. KaiB, RfaH, lymphotactin/XCL1, Mad2, selecase, chemokine cases.
- **Negative population** - single-fold proteins matched for length/family, drawn from the PDB, that have no evidence of fold switching (with the caveat that absence of evidence is weak; the negative set's construction is documented and its noise acknowledged).
- **Conformational-state auxiliaries** - BMRB (NMR ensembles capturing solution states), and any curated alternate-conformation sets. Rfam/UniRef MSAs and metagenomic sequences for the covariation/MSA-subsampling signal.

**Frozen split (leakage-safe).** Because the confirmed set is small and families recur, the split is **leave-cluster-out**: no test protein may share a homolog (above a sequence-identity threshold) or a fold-pair with any training protein, and a **time axis** (structures/annotations deposited after a cutoff) is applied where possible to emulate blind discovery. Split, cluster, and negative-set manifests are committed and hashed before any evaluation. Detection benchmarks are notoriously leaky through homology to known metamorphs; the cluster separation is mandatory.

**Wet-lab gate (mandatory).** Confirming that a candidate is genuinely fold-switching **cannot be done in silico**. It requires experimental determination of *both* folds under their respective conditions - typically solution NMR (well suited to capturing two populated states and exchange), crystallography or cryo-EM of each state, plus biophysical evidence of reversible interconversion (CD, NMR relaxation-dispersion, thermodynamic/kinetic characterization of the switch). This is a full structural-and-biophysical campaign per candidate - many months and, in effort terms, roughly \$100k–\$400k, with a real chance the candidate turns out single-fold. A model's confidence, an MSA-subsampling result, or agreement between predictors is **not** confirmation. This gate is not softenable.

## 3. Standard of a genuine advance

A genuine advance is one of:
1. A **certified detector** - a fold-switch classifier that, under leave-cluster-out separation, beats the strongest baseline (including AF2-confidence-based and MSA-subsampling heuristics) in AUPRC with calibrated probability, and localizes the switch region above a named IoU, on held-out families.
2. A **certified two-fold predictor** - a method that recovers *both* experimental folds on the joint metric for a majority of held-out cases, with distinct models for distinct states and calibrated per-state confidence, demonstrably not a homology lookup.
3. A **falsifiable candidate slate** - a ranked, calibrated list of predicted novel fold-switchers with their two predicted folds and proposed triggering conditions, registered before experimental testing, ready for an NMR/cryo-EM partner.

**Not accepted as resolution:**
- A **leaderboard detection AUPRC or joint-TM treated as a guarantee** that a new candidate is metamorphic - it is a hypothesis until both folds are solved.
- **In-silico "validation"** - recovering both known folds via MSA subsampling, or agreement between AF-Cluster and a second predictor, is not experimental confirmation of a *new* metamorph.
- A **corpus-overfit metric** - detection accuracy driven by homology to the handful of famous metamorphs (KaiB, RfaH); joint-TM inflated by test proteins with training homologs; a negative set so easy that any classifier scores well.
- Recovering only the dominant fold (the AF2 failure mode) and reporting single-state TM as success on a fold-switching target.

## 4. Graded targets

**P1 - Reproduce baselines.** Reproduce AF2 single-fold behavior and the MSA-subsampling / AF-Cluster alternate-state recovery (Wayment-Steele–Kern-style) on the curated set; reproduce a published detector. *Evidence:* committed leave-cluster-out splits, an independent TM/SS scorer, per-protein tables showing where AF2 returns only one fold.

**P2 - Calibrated detection.** A fold-switch classifier with probability calibrated on held-out families; switch-region localization reported. *Evidence:* reliability curves, expected calibration error, IoU distributions, all leave-cluster-out.

**P3 - Certified method contribution.** A modeling idea - conditioning on environmental trigger, energy-landscape / multi-basin modeling, targeted MSA construction, or a two-state generative head - that significantly improves joint two-fold recovery or detection on held-out families over P1. *Evidence:* paired per-protein deltas, ablations, no test-set tuning.

**P4 - New held-out SOTA.** Best-in-class joint two-fold recovery and/or detection AUPRC on the committed leave-cluster-out split, at one-GPU-feasible inference. *Evidence:* per-protein CDFs, split manifests, independent reproduction.

**P5 - Wet-lab-ready candidate slate.** A ranked, calibrated list of predicted novel fold-switchers (two folds + proposed trigger each), registered before experimental testing, with a pre-committed falsifiable claim (e.g. "$\ge k$ of the top $n$ show a second populated fold by NMR"), and honest post-hoc accounting including the single-fold misses. The machine's ceiling; NMR/cryo-EM closes the loop.

## 5. Known results and prior art

- **Porter & Looger** (~2018) - systematic identification and characterization of fold-switching proteins; argued the class is more prevalent than assumed and curated examples.
- **Chakravarty & Porter** (~2022) - demonstrations that AlphaFold2 fails to predict fold switching by construction (returns one fold, high confidence on both-wrong cases); a fold-switch-aware evaluation.
- **Wayment-Steele, Kern et al.** (2023, Nature) - "Predicting multiple conformations via sequence (MSA) clustering and AlphaFold2" (AF-Cluster); recovered alternate states for KaiB, RfaH and others by shallow/clustered MSAs - **verify performance and blind-vs-retrospective scope**; it is retrospective on known metamorphs, not validated blind discovery.
- **Canonical systems** - KaiB (circadian clock; Kern and others), RfaH (autoinhibition/refolding; Rösch, Knauer), lymphotactin/XCL1 (Volkman), Mad2 (Mapelli/Musacchio), selecase, chemokine metamorphs - the paired-fold structural anchors.
- **Ensemble/alternate-conformation prediction** - subsampled-MSA methods (Del Alamo et al. on transporters/GPCRs; verify), and energy-landscape approaches; adjacent to Boltzmann-weighted ensemble prediction.

*Status as of mid-2026 - re-verify against current literature before starting any session.* Check whether any method has demonstrated genuinely *blind* fold-switch discovery confirmed experimentally - as of writing, alternate-state recovery is retrospective on known cases, and the class remains an open, high-interest problem.

## 6. Attack plan

**Data.** Pull the curated metamorphic set and both-state PDB coordinates; build a matched single-fold negative population; cluster by homology and fold-pair; commit leave-cluster-out folds plus a time axis where possible. Assemble MSAs (deep and clustered/shallow variants) for the subsampling signal. Freeze and hash before modeling.

**Baselines.** AF2 (single-fold), AF-Cluster / MSA-subsampling alternate-state recovery, AF3 (as runnable), and a published fold-switch detector. Score both-state recovery with an independent TM/SS scorer.

**Model.** Candidate contributions: (i) a two-state generative / multi-basin structure head that emits *distinct* models for distinct folds; (ii) trigger-conditioned prediction (ligand, oligomeric state, pH/redox as input); (iii) a covariation-based detector exploiting the signal that fold-switchers carry conflicting coevolutionary couplings; (iv) principled MSA construction rather than random subsampling. Rerank ensembles to enforce two-basin coverage.

**Calibration.** Validate per-state confidence against realized TM and detection probability against realized precision, on held-out families; report expected calibration error. Given the tiny sample, report per-protein, not just aggregate.

**Compute.** Inference/fine-tuning of open AF-lineage models and MSA-subsampling are one-GPU feasible. The binding constraint is the number of confirmed examples, not compute.

**Failure modes.** (i) **Extreme data scarcity** - dozens of confirmed cases cap statistical power; overfitting to famous systems is the default failure. (ii) **Negative-set noise** - "single-fold" negatives may include undiscovered switchers, depressing apparent precision. (iii) **Leakage** - homology to KaiB/RfaH inflates everything; cluster separation is mandatory. (iv) **Retrospective illusion** - recovering known alternate states is not blind discovery; only registered prospective predictions count toward P5.

## 7. Verification and auditability requirements

1. **Leakage-safe evaluation.** Leave-cluster-out splits (no homolog or fold-pair shared with training) plus a time axis, committed and hashed before evaluation; the negative-set construction documented; no test-set tuning. Given the small sample, per-protein results are reported alongside aggregates.
2. **Calibrated uncertainty.** Detection probabilities and per-state structural confidences are calibrated and reported on held-out families (reliability curves, expected calibration error).
3. **Independent reproduction.** Joint two-fold TM/lDDT, switch-region IoU, and detection AUPRC are recomputed by a standalone scorer separate from training code, from committed splits and predictions.
4. **Cryptographic manifest.** A SHA-256 manifest covers the curated set version, negative-set definition, splits, code, weights, and every predicted structure and probability.
5. **Preservation.** Training/fine-tuning code, weights, MSA-construction and reranking configuration, and dataset version hashes are part of the record; anything not preserved is stated explicitly.
6. **Prospective-prediction registry.** Any candidate novel fold-switcher (P5) is timestamped and registered - two predicted folds, trigger, confidence, pre-committed claim - before experimental testing, and scored afterward including the single-fold misses.
7. **Honest reporting.** The report states up front that fold-switch discovery is reality-gated and **not resolved**; separates in-silico recovery of *known* alternate states from experimental confirmation of *new* ones; labels every candidate a wet-lab-pending hypothesis; and never presents a detection score or joint-TM as proof that a protein is metamorphic.
