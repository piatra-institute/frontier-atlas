# PROMPT FOR FUNCTION ANNOTATION OF THE DARK PROTEOME

## Calibrated GO / EC assignment for proteins with no characterized function

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** B - reality-gated (empirical verifier)
**Rank:** B-06 of 29
**Source:** chem/bio top-50 list #38, section E (genomics / sequence / systems)
**Modes:** `[data]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

A large and growing share of sequenced proteins carries no confident functional annotation. The UniProt/TrEMBL universe is dominated by proteins whose function is inferred, absent, or wrong, and a hard core - the *dark proteome* - has neither experimental annotation nor detectable homology to anything characterized. Predicting function from sequence (Gene Ontology terms, EC numbers, free-text function) is the central task, and modern sequence models (ESM-2-lineage embeddings, structure transfer via AlphaFold DB + Foldseek) genuinely advance it. But the ground truth of *function* is biochemical: an enzyme's reaction, a binder's partner, a knockout's phenotype. Compute can predict the label a future curator or a blind CAFA assessment will assign; it cannot establish that the protein actually does the thing. This is reality-gated. The deliverable is a certified, leakage-safe method that improves function prediction **specifically on the dark, remote-homology subset**, plus a ranked, calibrated set of falsifiable function hypotheses for a wet-lab partner - never a claim that the dark proteome has been "annotated."

## 1. Exact problem statement

**Input.** A protein amino-acid sequence, optionally with its predicted structure (AlphaFold DB or locally folded), genomic/operonic context, and taxonomy.

**Output.** A set of function labels, each with a **calibrated** confidence in [0,1]:
- **GO terms** across the three ontologies - Molecular Function (MFO), Biological Process (BPO), Cellular Component (CCO) - propagated consistently up the GO DAG (true-path rule).
- **EC numbers** (four-level hierarchy) for putative enzymes.
- Optionally a controlled free-text function statement.
- An explicit **abstention** ("unknown / novel function") when no term clears the calibrated confidence floor - abstention is a first-class output, not a forced guess.

**Metric.** CAFA-style protein-centric **Fmax** (threshold-swept F1 over the propagated GO DAG), term-centric **AUPRC** and semantic-distance **S-min** (information-content-weighted), reported **per ontology**. For EC, hierarchical accuracy at each level and full-EC exact match. All metrics reported **twice**: over the full test set and - the number that matters - over the **dark subset** defined in §2.

**Population.** Proteins with no experimental GO/EC annotation whose closest experimentally-annotated relative falls below a fixed remote-homology threshold. Performance on easy homologs is reported only as a sanity baseline, never as the headline.

**Scope and boundary conditions.**
- The remote-homology threshold is fixed as a number before modeling: no train relative above 25–30% sequence identity (MMseqs2) **and** no Foldseek structural hit above a set TM-score / below a set E-value.
- "No confident function" is operational: no experimental GO leaf term and no InterPro/Pfam family carrying a specific molecular-function assignment.
- Multi-domain proteins are annotated per domain where boundaries are defined; whole-chain-only annotation is stated as such.
- Prediction is over a closed GO/EC label space fixed at a frozen release; genuinely novel functions (no existing term) are out of scope and flagged, not forced into the nearest term.

**Compute-tractable sub-question vs empirically-gated whole.** The tractable target is to predict the annotation a blind curator / CAFA assessment will assign given the standard evidence codes - i.e. reproduce and extend the curated labelling process. The gated whole is the *true* molecular and cellular function, which only assays establish.

## 2. Verifier and data

**Ground-truth source.**
- **UniProtKB/Swiss-Prot** manually reviewed annotations, restricted to experimental evidence codes (EXP, IDA, IPI, IMP, IGI, IEP and descendants) - the only labels that count as ground truth.
- **Gene Ontology** DAG (for propagation and semantic distance) and the **GOA** annotation set.
- **EC / ENZYME** nomenclature; **BRENDA** for enzyme-reaction cross-reference (verify).
- **CAFA** blind community assessment (Radivojac, Friedberg and colleagues) as the gold external protocol - its temporal, curator-driven design is the reference standard.
- Structure-transfer resources: **AlphaFold DB** and **Foldseek** for remote structural homology; **InterPro/Pfam** for domain baselines.

**Frozen split (leakage-safe).** Two separations, both committed before modeling:
1. **Temporal (CAFA protocol).** Train on annotations existing at time t0; test only on proteins that acquire their *first* experimental annotation after t0. This is the honest simulation of prospective annotation.
2. **Homology + structure.** Cluster all sequences with MMseqs2 at a fixed low identity (e.g. 30% and a stricter 25% arm) and by Foldseek structural similarity; no test cluster may share a member with any train cluster. The **dark subset** is the test partition whose nearest train relative is below the remote-homology threshold in *both* sequence and structure.

**Known corpus biases.**
- Annotation is concentrated in a few model organisms; the dark subset skews toward non-model taxa where even training signal is sparse.
- Electronic (IEA) annotations vastly outnumber experimental ones and must never enter the ground truth.
- GO is open-world and incomplete: absence of a term is not evidence of absent function, so negatives are unknowns, not confirmed negatives.
- The GO DAG's information content is uneven, so raw Fmax rewards shallow, high-frequency terms - S-min and IC-weighting are the corrective.

**Additional leakage traps.**
- A test protein annotated by curators *using* homology to a training protein - filter test labels to direct experimental evidence only.
- Shared MSA/profile membership bridging train and test even below the identity threshold - check profile overlap, not just pairwise identity.
- Structure leakage: a deposited experimental structure of a test protein present at train time - hold structures out consistently with sequences.

**Wet-lab gate (mandatory).** A predicted function is a hypothesis until a biochemical assay confirms it: an enzyme-activity assay for a predicted EC, a binding/pull-down for a predicted interaction, a knockout/knockdown phenotype for a predicted process. Rough cost: a targeted activity assay on a soluble, expressible protein runs a few thousand USD and weeks; full functional characterization of a genuinely novel-fold, unknown-biochemistry dark protein runs $50k–$500k+ and multiple years, and may fail because the assay itself is unknown. No in-silico score removes this gate.

## 3. Standard of a genuine advance

A genuine advance is one or more of:
- A **certified, leakage-safe pipeline** reproducing the CAFA baselines (naïve frequency, DIAMOND/BLAST homology transfer) and a published SOTA method on the frozen temporal split, matched to reported Fmax/S-min per ontology.
- **New held-out SOTA on the dark subset specifically** - a statistically significant Fmax/AUPRC gain over the strongest homology-transfer and language-model baselines on remote-homology proteins, with the gain shown *not* to come from easy homologs.
- A **ranked, calibrated hypothesis set** for named dark-proteome proteins: predicted MFO/EC labels with calibrated confidences and the specific assay that would falsify each, ready to hand to a wet-lab partner.

**Not accepted as resolution.**
- A high full-set Fmax driven by easy homologous proteins, presented as annotating the dark proteome.
- Gains that vanish when the dark, remote-homology stratum is scored separately.
- Fmax inflated by aggressive up-propagation of shallow, high-information-content-poor GO terms.
- Any label emitted without a calibrated confidence, or with confidences that fail calibration on held-out data.
- Agreement between a predicted label and a structure-model active-site motif presented as *established* function rather than as a hypothesis.
- A CAFA/Kaggle leaderboard rank represented as a real-world guarantee of biological function.
- A free-text or ProtNLM-style name presented as a validated function without an evidence-coded term and calibrated confidence behind it.
- Reporting only easy-organism performance while the dark subset (non-model taxa) is silently dropped for being too hard.

## 4. Graded targets

**P0 - Data and split integrity.** Before any modeling, verify the frozen split has no experimental-evidence leakage between train and test and that the dark subset is non-empty and hard for homology transfer. Certificate: the committed split manifest with cluster membership and the DIAMOND-transfer dark-subset score.

**P1 - Reproduce the CAFA frozen-split baselines.** Naïve and DIAMOND/BLAST-transfer baselines plus one published SOTA (e.g. a DeepGO-lineage or ProteInfer-lineage model), reproduced on the committed temporal split; Fmax/S-min per ontology matched to literature within tolerance. Independently valuable as a trusted baseline.

**P2 - Language-model + structure-transfer method.** Combine ESM-2 embeddings with Foldseek/AlphaFold-DB structural transfer under strict homology separation; report full-set and dark-subset metrics. Certificate: frozen splits, per-stratum tables, ablations isolating the source of any gain.

**P3 - Calibrated dark-subset SOTA.** Demonstrate a significant improvement over the strongest baseline **on the dark subset**, with calibrated confidences (reliability diagram / ECE on held-out data). Certificate: per-stratum bootstrap CIs, calibration report.

**P4 - Falsifiable hypothesis set.** For a fixed list of dark-proteome proteins, emit ranked MFO/EC hypotheses with calibrated confidence and, for each, the single assay that would confirm or refute it. Certificate: a frozen prediction registry (hashes, timestamps) predating any experiment.

**P5 - Prospective confirmation (wet-lab partner).** Any experimentally tested hypothesis is reported as a prospective outcome - hits *and* misses - with the calibration of the confidence assessed against the realized hit rate. This is the only target that touches the true function.

## 5. Known results and prior art

- **CAFA** community assessments: CAFA1 (Radivojac et al. ~2013), CAFA2 (Jiang et al. ~2016), CAFA3 (Zhou et al. ~2019); CAFA5 ran as a public competition ~2023 (verify). The recurring lesson: homology transfer is a stubbornly strong baseline and gains concentrate on well-studied proteins.
- **DeepGO / DeepGOPlus / DeepGOZero** (Kulmanov, Hoehndorf ~2018–2022) - CNN/embedding + GO-DAG-aware prediction.
- **NetGO / NetGO 2.0** (Yao, Zhu et al. ~2019–2021, verify) - learning-to-rank integration of many evidence sources; **GOLabeler** (You, Zhu et al. ~2018) - the ranking ensemble it descends from.
- **TALE** (Cao, Shen ~2021) - transformer with GO-hierarchy-aware loss.
- **ProteInfer** (Sanderson et al. ~2023) - sequence CNN for EC and GO. **CLEAN** (Yu, Zhao et al. ~2023) - contrastive learning for EC-number prediction with confidence.
- **ProtCNN / ProtENN** (Bileschi et al. ~2022) - deep Pfam family classification extending annotation coverage.
- **ProtNLM** (UniProt/Google ~2022, verify) - language-model-generated protein names for uncharacterized entries.
- **DeepFRI** (Gligorijević et al. ~2021) - structure-based graph CNN for function.
- **ESM-1b / ESM-2** (Rives et al. 2021; Lin et al. 2023) embeddings as function features; **Foldseek** (van Kempen, Steinegger et al. ~2023) enabling structure-based remote-homology transfer at scale against **AlphaFold DB** (Varadi, Tunyasuvunakool et al. ~2021–2022); **InterPro2GO** - the domain-to-GO mapping behind most electronic annotation.
- Dark-proteome characterization: Perdigão et al. (~2015) and follow-ups quantifying the unannotated / structurally-dark fraction.

*Status as of mid-2026 - re-verify against current literature before starting any session.*

## 6. Attack plan

**Data.** Pull Swiss-Prot experimental annotations at a frozen release, the GO DAG, and the CAFA temporal target set; build the dark subset with MMseqs2 + Foldseek clustering against AlphaFold DB. Fold any test proteins lacking a deposited structure locally.

**Baselines.** DIAMOND/BLAST k-nearest homology transfer and the naïve frequency model first - they are the bar the dark-subset gain must clear.

**Model.** ESM-2 (650M on one GPU; larger via embedding caching) sequence embeddings feeding GO-DAG-consistent multi-label heads (or a hierarchical/contrastive head à la CLEAN for EC), fused with a Foldseek structural-transfer channel. Enforce the true-path rule in the loss and at inference.

**Calibration.** Temperature scaling or conformal prediction per ontology; calibration measured on a held-out stratum, reported as reliability diagrams and ECE, **separately** for the dark subset where calibration is hardest and most consequential.

**Concrete first steps (week 1).**
1. Freeze a Swiss-Prot release and the GO/EC vocabularies; record version hashes.
2. Build MMseqs2 sequence clusters and Foldseek structural clusters; define and freeze the dark subset.
3. Reproduce the naïve and DIAMOND-transfer baselines; record per-ontology Fmax/S-min on full set and dark subset.
4. Cache ESM-2 embeddings for train/test to disk (one pass) so later heads train cheaply.
5. Commit the split manifest and baseline numbers before any model tuning.

**Cross-checks.** Confirm the dark subset is genuinely hard (DIAMOND transfer near-random on it); use InterPro/Pfam domain hits as an orthogonal evidence channel and report where the model agrees or disagrees with domain-based calls.

**Ablation and null-model panel.** On the dark subset, report:
- label-frequency prior alone;
- DIAMOND homology transfer alone;
- ESM-2 embedding head alone;
- Foldseek structural transfer alone;
- the full fusion.
Any headline claim must show the fusion beats every single-channel ablation on the dark subset, not only on the full set.

**One-GPU scope.** Embedding extraction and MLP/hierarchical heads fit a single prosumer GPU; Foldseek runs on CPU. Full protein language-model fine-tuning does not - cache embeddings.

**Failure modes.** (i) Homology leakage silently inflating everything - the dark-subset table is the guard. (ii) GO-DAG propagation gaming Fmax - report S-min and IC-weighted metrics. (iii) Label noise and open-world negatives (absence of annotation ≠ absence of function) - treat negatives as unknown. (iv) Distribution shift to non-model organisms where even the training annotations are sparse.

## 7. Verification and auditability requirements

1. **Leakage-safe evaluation.** Temporal and homology+structure splits committed before any evaluation; MMseqs2/Foldseek clustering parameters and the dark-subset definition documented; no test-set tuning. Every headline metric reported for the full set *and* the dark subset.
2. **Calibrated uncertainty.** Every emitted label carries a calibrated confidence; calibration (reliability diagram, ECE) is reported on held-out data and separately on the dark subset.
3. **Baseline parity and ablation.** Naïve and homology-transfer baselines reproduced and reported alongside; ablations isolate the source of any gain (language model vs structure transfer vs propagation).
4. **Independent reproduction.** Metrics recomputable from committed splits, predictions, and a separate scoring script; a SHA-256 manifest covers data-version hashes, code, embeddings, and predictions.
5. **Preservation.** Model/training code, embedding pipeline, database version hashes, and split definitions are part of the record. Anything not preserved is stated explicitly.
6. **Prospective prediction registry.** The P4 hypothesis set (protein, predicted label, calibrated confidence, falsifying assay) is timestamped and hashed before any wet-lab test; nothing is added or edited post hoc.
7. **Honest reporting.** The report states up front that function is empirically defined and the problem is NOT resolved; separates predicted-annotation metrics from any assay outcome; labels every function call a wet-lab-pending hypothesis; and never presents a CAFA/leaderboard number as a real-world guarantee of biological function.
