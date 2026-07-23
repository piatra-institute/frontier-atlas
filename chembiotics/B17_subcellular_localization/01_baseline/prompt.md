# PROMPT FOR AB INITIO SUBCELLULAR LOCALIZATION AND TRAFFICKING-SIGNAL PREDICTION

## Beyond N-terminal targeting peptides - multi-localization and condition-dependent trafficking

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** B - reality-gated (empirical verifier)
**Rank:** B-17 of 29
**Source:** chem/bio top-50 list #42, section F (cells / structures / images)
**Modes:** `[data]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Where a protein goes in the cell, and by what signals, is a determinant of its function and a target for engineering. The classical cases - N-terminal signal peptides, mitochondrial transit peptides - are largely solved by mature tools (SignalP, TargetP), and localization classifiers (DeepLoc-lineage) reach strong accuracy on single-localized proteins. The open edge is elsewhere: **non-canonical and internal targeting signals, multi-localization** (proteins with several compartments), and **condition- or cell-type-dependent trafficking**. Sequence and structure models advance ab-initio prediction here, but localization is defined by microscopy and fractionation, the imaging ground truth is itself partial and reliability-graded, and much trafficking is context-dependent in ways a single sequence cannot encode. Compute can predict curated/imaging localization labels; it cannot establish where a given protein resides in a given cell state. This is reality-gated. The deliverable is a leakage-safe method that improves specifically on **multi-localized and non-canonically-targeted** proteins, plus falsifiable localization hypotheses for a microscopy partner.

## 1. Exact problem statement

**Input.** A protein amino-acid sequence, optionally its structure and a cell-type/condition context.

**Output.**
- A **multi-label** distribution over subcellular compartments (nucleus, cytoplasm, mitochondrion, ER, Golgi, plasma membrane, extracellular/secreted, peroxisome, lysosome/vacuole, plastid where relevant), each with a calibrated probability.
- Identified **trafficking signals**: signal peptide and cleavage site, mitochondrial/chloroplast transit peptide, NLS/NES, GPI-anchor, and transmembrane topology.

**Metric.** Multi-label: macro- and micro-F1, per-compartment AUPRC, and Jaccard on the compartment set; reported with a **multi-localization subset** broken out. Signal peptides: cleavage-site accuracy and Matthews correlation (the SignalP benchmark). Topology: per-residue and per-protein accuracy.

**Population.** Proteins across organisms (human/eukaryote focus), stratified by single vs multi-localization and by canonical vs non-canonical targeting.

**Compute-tractable sub-question vs empirically-gated whole.** Tractable: predict UniProt/HPA localization labels and signal-peptide benchmarks under leakage-safe evaluation, with real gains on the multi-localization stratum. Gated whole: the actual localization of a protein in a specific cell type and condition, which needs imaging/fractionation.

## 2. Verifier and data

**Ground-truth source.**
- **UniProtKB** curated subcellular-location annotations (evidence-coded) - the sequence-side ground truth.
- **Human Protein Atlas (HPA)** immunofluorescence imaging with reliability scores (Thul, Lundberg, Uhlén et al. ~2017) - the imaging-side, multi-localization-rich ground truth.
- **DeepLoc** datasets (Almagro Armenteros, Winther et al. ~2017; DeepLoc 2.0, Thumuluri et al. ~2022) - homology-partitioned localization benchmarks.
- **SignalP 6.0** benchmark (Teufel et al. ~2022) and **TargetP 2.0** (Almagro Armenteros et al. ~2019) - signal/transit-peptide ground truth with cleavage sites.
- **DeepTMHMM / TMHMM** (verify) for transmembrane topology reference.

**Frozen split (leakage-safe).** Committed before modeling:
1. **Homology partitioning** (the DeepLoc protocol) - no test protein homologous to any train protein (sequence-identity cluster separation).
2. **Temporal** - split by UniProt/HPA release to simulate prospective annotation.
3. **Label-provenance separation** - imaging-derived (HPA) and sequence-curated (UniProt) labels kept distinct so a model is not trained on one and "validated" circularly on the same evidence stream.
4. **Multi-localization held-out subset** fixed in advance - the stratum the headline claim rests on.

**Wet-lab gate (mandatory).** Localization needs microscopy (immunofluorescence, fluorescent-protein fusion, live-cell imaging) and/or subcellular fractionation with mass spectrometry; a predicted NLS/NES needs a relocalization assay (mutate the signal, image the shift). Rough cost: validating one protein's localization with a tagged-construct microscopy experiment runs low thousands USD and weeks; a proteome-scale imaging effort (HPA-style) is a major multi-year, multi-antibody undertaking. No score removes this gate.

## 3. Standard of a genuine advance

A genuine advance is one or more of:
- A **certified, leakage-safe pipeline** reproducing SignalP 6.0 / DeepLoc 2.0 baselines on their homology-partitioned splits.
- **New held-out performance on the multi-localization and non-canonical-targeting strata specifically** - a significant macro-F1/AUPRC gain over the strongest embedding-based baselines where the field is weak.
- A **ranked, calibrated hypothesis set** - proteins with predicted (multi-)localization and the specific microscopy/relocalization assay that would confirm/refute each - for a microscopy partner.

**Not accepted as resolution.**
- A single-label predictor scored only on single-localized proteins, presented as general localization.
- Strong N-terminal signal-peptide performance presented as solving localization (the internal/non-canonical signals are the open edge).
- A blended metric that hides multi-localization performance.
- A predicted NLS/NES with no relocalization test, presented as established.
- Any prediction without a calibrated probability, or calibration untested on held-out data.
- A leaderboard number represented as a guarantee of where the protein resides in a live cell.

## 4. Graded targets

**P1 - Reproduce SignalP / TargetP / DeepLoc baselines.** SignalP 6.0 cleavage-site MCC, TargetP class accuracy, DeepLoc 2.0 multi-label F1 reproduced on their homology-partitioned splits within tolerance. Independently valuable as a trusted baseline.

**P2 - Embedding-based multi-label model.** ProtT5/ESM-2 embeddings with a light-attention or multi-label head, matched or improved on the DeepLoc 2.0 split under strict homology partitioning. Certificate: per-compartment tables, multi-localization subset broken out.

**P3 - Multi-localization / non-canonical SOTA with calibration.** A significant gain on the multi-localization and non-canonical-targeting strata, with calibrated per-compartment probabilities (reliability diagrams, ECE). Certificate: per-stratum bootstrap CIs, calibration report.

**P4 - Falsifiable localization hypothesis set.** For named proteins, ranked (multi-)localization hypotheses and, for signal-driven cases, the mutate-and-image relocalization experiment that would confirm/refute each. Certificate: frozen, hashed prediction registry predating experiment.

**P5 - Prospective confirmation (microscopy partner).** Tested hypotheses reported as prospective outcomes, hits and misses, with confidence calibration assessed against realized imaging. Only this touches true localization.

## 5. Known results and prior art

- **SignalP** (Nielsen, Brunak et al.; SignalP 6.0, Teufel et al. 2022) - transformer-based signal-peptide and cleavage-site prediction across signal-peptide types.
- **TargetP 2.0** (Almagro Armenteros et al. ~2019) - N-terminal targeting-peptide classification.
- **DeepLoc / DeepLoc 2.0** (Almagro Armenteros, Winther ~2017; Thumuluri et al. 2022) - multi-label subcellular localization from sequence, homology-partitioned.
- **Light Attention** (Stärk, Rost et al. ~2021) - ProtT5-embedding localization with attention pooling.
- **Human Protein Atlas** (Thul, Lundberg, Uhlén et al. ~2017) - imaging-based subcellular map with reliability scoring; basis of image-classification challenges.
- **MULocDeep** (Jiang et al. ~2021, verify) - multi-localization with sub-organelle resolution.
- **DeepTMHMM** (Hallgren, Nielsen et al. ~2022, verify) - transmembrane topology.
- Protein language models: **ProtT5** (Elnaggar, Rost et al. ~2021), **ESM-2** (Lin et al. 2023) as the embedding backbone.

*Status as of mid-2026 - re-verify against current literature before starting any session.*

## 6. Attack plan

**Data.** Pull UniProt localization annotations and HPA imaging labels at frozen releases, plus SignalP/TargetP benchmark sets; build homology-partitioned and multi-localization splits; keep imaging vs sequence provenance separate.

**Baselines.** Reproduce SignalP 6.0, TargetP 2.0, DeepLoc 2.0, and a WoLF-PSORT-style feature baseline as the bar.

**Model.** ProtT5/ESM-2 embeddings feeding a light-attention multi-label head for compartments, plus a CRF/sequence-labeling head for signal-peptide cleavage sites and a topology head. Structure features (from AlphaFold DB) optional for membrane/topology cases.

**Calibration.** Per-compartment temperature scaling or conformal prediction; calibration measured on held-out data and separately on the multi-localization stratum.

**One-GPU scope.** Embedding extraction plus light heads fit one prosumer GPU; full language-model fine-tuning does not - cache embeddings.

**Failure modes.** (i) Homology leakage inflating everything - homology partitioning is the guard. (ii) Single-localization dominance masking multi-localization weakness - the broken-out stratum. (iii) Circular validation on the same evidence stream - provenance separation. (iv) Context-dependence - condition/cell-type-specific trafficking is outside single-sequence reach and must be flagged as a scope limit.

## 7. Verification and auditability requirements

1. **Leakage-safe evaluation.** Homology-partitioned and temporal splits committed before evaluation; imaging-vs-sequence provenance separated; multi-localization subset fixed in advance; no test-set tuning.
2. **Calibrated uncertainty.** Every compartment probability carries a calibrated confidence; calibration (reliability diagram, ECE) reported on held-out data and separately on the multi-localization stratum.
3. **Baseline parity and stratified reporting.** SignalP/TargetP/DeepLoc baselines reproduced; every headline metric reported with the single-vs-multi and canonical-vs-non-canonical strata broken out.
4. **Independent reproduction.** Metrics recomputable from committed splits, predictions, and a separate scoring script; SHA-256 manifest over data-version hashes, code, embeddings, and predictions.
5. **Preservation.** Model/training code, embedding pipeline, database/imaging version hashes, and split definitions are part of the record. Anything not preserved is stated explicitly.
6. **Prospective prediction registry.** The P4 hypothesis set (protein, predicted localization, relocalization/imaging assay) is timestamped and hashed before any wet-lab test; no post-hoc edits.
7. **Honest reporting.** The report states up front that localization is empirically defined and NOT resolved; separates predicted-label metrics from any imaging/fractionation outcome; labels every localization call a wet-lab-pending hypothesis; and never presents a benchmark number as a guarantee of a protein's location in a live cell.
