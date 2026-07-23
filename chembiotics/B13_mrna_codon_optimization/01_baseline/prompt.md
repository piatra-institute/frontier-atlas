# PROMPT FOR JOINT mRNA / CODON OPTIMIZATION: EXPRESSION, STABILITY, AND IMMUNOGENICITY

## Multi-objective sequence design under structure–expression coupling

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** B - reality-gated (empirical verifier)
**Rank:** B13 of 29
**Source:** chem/bio top-50 list #40, section E (genomics)
**Modes:** `[gen]` `[data]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

An mRNA therapeutic or vaccine must be translated well (expression), survive long enough to be translated (stability), and not trip innate immune sensors (low immunogenicity). These objectives trade off - strong secondary structure can stabilize an mRNA while suppressing translation initiation; rare codons and high uridine content interact with both expression and immune sensing - and current tools optimize them mostly one or two at a time. The task is to predict these properties from sequence and to *design* mRNA sequences (codon choice, UTRs, structure) that jointly optimize them, with calibrated uncertainty and an explicit Pareto framing. This is reality-gated: expression and immunogenicity are defined by cell and animal assays and stability partly by in-vitro degradation, so compute can produce a certified predictor, a held-out benchmark result, and a ranked set of falsifiable designs - but a transfection assay, a degradation measurement, and an immunogenicity readout, not the model, confirm a designed mRNA. No resolution is on offer; every designed sequence is a hypothesis pending experimental validation.

## 1. Exact problem statement

**Input.**

- for the design task: a target protein (amino-acid sequence) plus constraints - fixed UTRs or UTR design allowed, nucleoside chemistry, GC/uridine constraints, host cell type;
- for the prediction task: a full mRNA sequence and its context.

**Output.** Two coupled deliverables, each with calibrated confidence:

1. **Property prediction (`[data]`).** For a given mRNA: predicted expression / translation efficiency (e.g. ribosome load or protein yield), stability (mRNA half-life and/or in-vitro degradation rate), and an immunogenicity proxy (innate-immune activation risk from sequence features), each a calibrated estimate.
2. **Multi-objective design (`[gen]`).** A set of candidate mRNA sequences encoding the target protein, presented as a Pareto front over (expression, stability, low-immunogenicity), with per-objective calibrated predictions and the trade-off made explicit.

**Metric.** Fixed before modeling and reported with confidence intervals:

- prediction: Spearman/Pearson against measured expression, half-life, and degradation on held-out sequences; calibration (ECE);
- design: for validated designs, achieved objective values vs predicted (calibration of the design pipeline);
- design: Pareto-front hypervolume vs baselines, and constraint-satisfaction rate;
- because generation is involved, in-silico design quality is scored only as a *predicted* Pareto front until wet-lab tested.

**Population.** mRNAs encoding diverse proteins in the host/context represented by the training assays; report per-objective performance separately and the trade-off explicitly - a single scalar hides the multi-objective structure.

**Compute-tractable sub-question vs empirically-gated whole.**

- *Tractable:* given frozen ribosome-profiling, half-life, and in-vitro-degradation corpora, predict held-out expression/stability/degradation with calibrated uncertainty under a sequence-identity- and gene-holdout split, and generate Pareto-optimal designs against those predictors.
- *Empirically-gated (not claimable on the machine):* that a designed mRNA actually expresses well and is non-immunogenic in cells/animals.

## 2. Verifier and data

**Ground-truth sources.**

- **Ribosome profiling (Ribo-seq)** and polysome-profiling datasets - translation-efficiency labels.
- **5′UTR MPRA / ribosome-load data** - the Optimus 5-Prime training data (Sample et al., ~2019 - verify) and successors, for translation-initiation effects.
- **mRNA-stability / half-life datasets** - transcriptome-wide half-life measurements (metabolic-labeling / SLAM-seq-derived - verify accessions).
- **In-vitro degradation** - the Stanford/Das-lab OpenVaccine mRNA-degradation data (Kaggle 2020 - verify), SHAPE-based per-base degradation/reactivity.
- **Expression measurements** - reporter-expression datasets across codon-variant libraries (verify accessions).
- **Immunogenicity features** - dsRNA content, uridine composition, and known innate-sensor (RIG-I/MDA5/TLR) motif features as proxies; direct immunogenicity labels are scarce - flag this explicitly.

**Frozen, leakage-safe split.** Commit and hash before modeling.

- **Sequence-identity holdout:** cluster mRNAs/UTRs by sequence identity and keep clusters on one side, so near-duplicate sequences do not straddle the split.
- **Gene / protein holdout:** hold out whole encoded proteins so the model cannot memorize a protein's optimal codon pattern.
- **Assay/batch holdout:** where labels come from multiple experiments, guard against batch-effect leakage.
- **Ancestry/host considerations:** codon optimality and tRNA availability are host- and cell-type-dependent; a design optimal for one expression host is not transferable. State host context as part of every claim - this is the analogue of population specificity here.

**Negative controls and label caveats.** Fixed before modeling:

- codon-shuffled and synonymous-randomized sequences as a null for the codon-optimization signal;
- label-shuffled runs to bound leakage/memorization;
- an explicit note that immunogenicity has only proxy labels, so its "predictions" are the weakest-grounded output.

**Wet-lab gate (mandatory).** No expression or immunogenicity claim for a designed mRNA is established without new assays: in-vitro transcription plus transfection and a reporter/protein-quantification assay for expression, a degradation/half-life measurement for stability, and cytokine/innate-immune or animal assays for immunogenicity. Indicative cost: a cell-based expression screen of a design panel runs low-thousands to tens-of-thousands USD; degradation measurement is cheaper (in-vitro); immunogenicity assays (cytokine panels, and especially animal studies) run tens of thousands USD and months. This gate is not optional and must not be softened.

## 3. Standard of a genuine advance

A genuine advance is one or more of:

- a **certified predictor** reproducing a named SOTA expression/stability model (Optimus 5-Prime, CodonBERT, LinearDesign's stability objective) on the frozen, leakage-safe split, independently runnable;
- a **new held-out SOTA** on a pre-registered split for expression, half-life, or degradation prediction, with calibration;
- a **method contribution** on the *joint* problem: a design pipeline whose predicted Pareto front over (expression, stability, immunogenicity) dominates single-objective baselines, with the structure–expression coupling modeled explicitly and calibrated per-objective uncertainty;
- a **ranked, calibrated, falsifiable design set** of mRNA sequences for a target protein, presented as a Pareto front with per-objective hypotheses and the exact assay that would refute each.

**Not accepted as resolution.**

- A single-objective optimization presented as solving the multi-objective problem.
- A design "validated" only in silico or by a folding-energy proxy alone.
- An immunogenicity claim based only on sequence proxies, presented as an established safety property.
- A metric obtained on a split that leaks via near-duplicate sequences or shared proteins.
- A host-specific result presented as host-transferable.

## 4. Graded targets

**P0 - Frozen, hashed corpus and split.** Assemble the ribosome-load, half-life, and degradation label sets and commit the sequence-identity-/gene-holdout split with a provenance manifest before modeling.
*Evidence:* SHA-256 manifest, versioned accessions, written split rationale.

**P1 - Reproduce SOTA predictors on the frozen split.** Rebuild Optimus 5-Prime (ribosome load), a stability/half-life predictor, and the LinearDesign structure objective with our own verified code; match reported metrics on the committed split.
*Evidence:* reproducible metrics, hashed split, side-by-side.

**P2 - Calibrated per-objective prediction.** On held-out sequences, predict expression, half-life, and degradation with calibrated uncertainty; report Spearman per objective and calibration error.
*Evidence:* reliability curves on held-out data; leakage ablation.

**P3 - Certified joint design method.** A design pipeline whose predicted Pareto front over the three objectives dominates single-objective baselines on a pre-registered held-out evaluation, with structure–expression coupling modeled and per-objective calibration.
*Evidence:* hypervolume comparison; benchmark-integrity statement; explicit trade-off reporting.

**P4 - Falsifiable design set for a partner.** For a target protein, a ranked Pareto set of mRNA designs with per-objective hypotheses and the transfection/degradation/immunogenicity assays that would refute each.
*Evidence:* the set, its prior held-out calibration, and a pre-registered success criterion. Every design labeled a wet-lab-pending hypothesis.

## 5. Known results and prior art

- **Optimus 5-Prime** (Sample et al., ~2019) - CNN predicting ribosome load from 5′UTR sequence, trained on MPRA; enables UTR design for translation.
- **CodonBERT** (Sanofi group, ~2023 - verify) - transformer language model over codon sequences for property prediction/design.
- **LinearDesign** (Zhang et al., ~2023) - joint optimization of codon usage and mRNA secondary-structure stability via efficient lattice/dynamic-programming search; a landmark for the stability–codon trade-off.
- **RNA structure / degradation** - the Stanford/Das-lab OpenVaccine mRNA-degradation challenge (Kaggle, ~2020 - verify) established sequence-to-degradation modeling; SHAPE-based reactivity as the readout.
- **Ribosome-load and UTR-design models** and **codon-optimality metrics** (tAI, CAI, and learned successors) as baselines.
- **Open parts:** multi-objective (expression × stability × immunogenicity) trade-offs, the structure–expression coupling, and the scarcity of direct immunogenicity labels - none closed.

**Status as of mid-2026 - re-verify against current literature before starting any session.** Confirm current model names, releases, and dataset accessions (especially the degradation and half-life corpora) before committing.

## 6. Attack plan

Concrete first steps, in order:

1. **Assemble the frozen corpus.** Pull 5′UTR MPRA / ribosome-load data and a transcriptome-wide half-life dataset as the anchor prediction labels; OpenVaccine degradation data (verify) for in-vitro stability; codon-variant expression libraries where available. Assemble sequence-feature-based immunogenicity proxies and flag the label scarcity. Record versions.
2. **Construct the leakage-safe split.** Commit sequence-identity-, gene-, and assay-holdout splits; hash the manifest. Cluster by sequence identity so near-duplicates do not leak; fix and record the expression host/context for every claim.
3. **Reproduce baselines.** Reimplement Optimus 5-Prime and the LinearDesign objective in PyTorch and match reported metrics before attempting any improvement.
4. **Model the contribution.** Build per-objective calibrated predictors (sequence + secondary-structure features via a folding engine such as LinearFold/ViennaRNA) and a multi-objective design/search producing a Pareto front - LinearDesign-style DP, guided generation, or optimization over a generative model `[gen]`.
5. **Calibrate.** Calibrate each predictor on held-out data and report the calibration (reliability curves, ECE).
6. **Negative controls.** Codon-shuffled / synonymous-randomized sequences and label-shuffled runs to bound the trivial and leaked signal.

**One-GPU scope.** The predictors and search fit a single prosumer GPU; RNA secondary-structure computation is CPU-bound and can dominate runtime for long sequences - flag it.

**Failure modes to expect and report:**

- near-duplicate-sequence leakage inflating prediction metrics;
- over-trusting a folding-energy proxy for real stability;
- host-transfer failure of codon optimality to a different expression host;
- treating sequence-proxy immunogenicity as an established safety property;
- Pareto-front instability when the per-objective predictors are miscalibrated.

State each explicitly where it bites, and quantify its impact where the controls allow.

## 7. Verification and auditability requirements

1. **Leakage-safe evaluation.** Sequence-identity-, gene-, and assay-holdout splits committed and hashed before evaluation; near-duplicate clustering documented; no test-set tuning.
2. **Calibrated uncertainty.** Every per-objective prediction and every designed-sequence objective estimate carries calibrated confidence; calibration reported on held-out data with reliability curves and ECE.
3. **Multi-objective and host honesty.** The Pareto trade-off reported explicitly, never collapsed to a single scalar without justification; expression-host/cell-type context stated for every claim; a host-specific result never presented as transferable.
4. **Immunogenicity caution.** Immunogenicity predictions from sequence proxies labeled as hypotheses, never as established safety; the scarcity of direct immunogenicity labels stated up front.
5. **Independent reproduction.** Metrics reproducible from the committed split and code by a separate script; SHA-256 manifest over data version hashes, code, and predictions.
6. **Preservation.** Model weights or weight provenance, design/generation code, and dataset version hashes are part of the record; anything not preserved is stated explicitly.
7. **Honest reporting.** The report states up front that the problem is reality-gated and NOT resolved; separates in-silico predictions from any assay validation; labels every designed mRNA a transfection-/degradation-/immunogenicity-pending hypothesis; and never presents a benchmark number as a real-world guarantee.
