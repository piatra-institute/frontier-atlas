# PROMPT FOR PREDICTING BIOMOLECULAR CONDENSATE PROPENSITY FROM SEQUENCE

## Phase-separation driver vs client prediction, grounded in curated LLPS corpora and saturation concentrations

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** B - reality-gated (empirical verifier)
**Rank:** B-09 of 29
**Source:** chem/bio top-50 list #43, section F (cells / structures / images)
**Modes:** `[data]` `[struct]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Biomolecular condensates formed by liquid–liquid phase separation (LLPS) organize much of cell biology, and predicting phase-separation propensity from sequence is a young, crisp, high-interest problem. The physics is increasingly clear - multivalent "stickers" (aromatics, charges) spaced by flexible "spacers" drive condensation, captured by descriptors like pi-pi contact propensity and charge patterning, and by coarse-grained models that compute saturation concentrations. Sequence models and these biophysical scores genuinely advance driver prediction. But phase behavior is defined by measurement - in-vitro saturation concentration, turbidity, microscopy, and condition-dependent cellular assays - and the curated corpora are small and heavily biased. Compute can predict curated-database membership and, where measured, an in-vitro saturation concentration; it cannot establish that a protein forms condensates in a cell, nor distinguish a driver from a passively recruited client without careful design. This is reality-gated. The deliverable is a leakage-safe, negative-set-honest method that separates **driver** prediction from **client recruitment**, plus falsifiable in-vitro/cellular hypotheses for a wet-lab partner.

## 1. Exact problem statement

**Input.** A protein sequence (optionally its RNA/protein partners and a concentration/condition context).

**Output.** Either or both, with calibrated confidence:
- **Phase-separation class** - driver/scaffold vs client vs non-LLPS (self-assembly under physiological-range conditions vs partitioning only in a pre-formed condensate vs neither), with a calibrated propensity.
- **Quantitative descriptor** - a predicted in-vitro saturation concentration c_sat (or a coexistence/phase-boundary summary) where measurements exist.
- An explicit **abstention** where no class clears the confidence floor.

**Metric.** Classification: AUPRC and AUROC on curated positives vs *matched* negatives (matched for length, disorder fraction, and expression), stratified by driver vs client. Quantitative: Spearman/Pearson and MAE (in log c_sat units) vs in-vitro measurements. The dataset-bias caveat (§2) is reported alongside every number.

**Population.** Proteins and their regions; the honest population must confront positive-unlabeled structure - confirmed positives are few, confirmed negatives are fewer, and most of the proteome is *untested*, not negative.

**Scope and boundary conditions.**
- "Driver" means a region sufficient to phase-separate under near-physiological conditions in vitro; "client" means partitioning only into a pre-formed condensate; "non-LLPS" means tested and negative.
- Conditions (salt, crowder, temperature, RNA presence) are part of the label and travel with every measurement.
- RNA-only and RNA-driven condensates are flagged as a distinct regime, not pooled with protein drivers.
- Single-sequence prediction cannot capture concentration- and partner-dependence; those cases are flagged as scope limits.

**Compute-tractable sub-question vs empirically-gated whole.** Tractable: predict curated-corpus membership and measured in-vitro c_sat under leakage-safe, bias-controlled evaluation. Gated whole: whether a protein forms a functional condensate in a living cell under a given condition, which needs assays.

## 2. Verifier and data

**Ground-truth source.**
- **PhaSePro** (Mészáros et al. ~2020) - curated, manually annotated LLPS drivers with region-level detail.
- **LLPSDB** (Li, Liu et al. ~2020) - in-vitro LLPS with conditions and, in many entries, concentration data.
- **DrLLPS** (Ning et al. ~2020) - drivers/regulators/clients classification (its own driver-vs-client labels are directly relevant).
- **PhaSepDB** and **CD-CODE** (community condensate database, ~2023 - verify) - broader condensate/component sets.
- **In-vitro saturation-concentration** measurements (turbidity, microscopy titration) from primary literature as the quantitative ground truth.

**Frozen split (leakage-safe).** Committed before modeling:
1. **Homology clustering** (MMseqs2) - no test cluster shares a member with train.
2. **Driver/client and organism stratification** - report driver and client performance separately; do not let one abundant class inflate the other.
3. **Temporal** - split by database release to simulate prospective prediction.
4. **Negative-set protocol** - negatives matched to positives for length, disorder fraction, and expression level; the positive-unlabeled bias documented explicitly, and a "random-negative" run reported only as a cautionary upper bound.

**Known corpus biases.**
- The dominant bias is positive-unlabeled: confirmed positives are few, confirmed negatives far fewer, and the proteome is untested rather than negative.
- Corpora over-represent a handful of studied systems (FUS/hnRNP/DDX-family, nucleolar and stress-granule proteins).
- In-vitro c_sat values are collected under heterogeneous conditions and are not directly comparable without metadata.
- Driver and client labels are unevenly curated across databases and sometimes conflict.

**Additional leakage traps.**
- Homologous or repeat-rich sequences (e.g. related RGG/low-complexity domains) bridging train and test - cluster on low-complexity content, not only global identity.
- A "negative" that is simply untested being counted as a true non-LLPS - only tested negatives count as negatives.
- c_sat measurements from the same study/construct appearing in both train and test - split by source study, not just by sequence.

**Wet-lab gate (mandatory).** Phase behavior needs in-vitro turbidity/microscopy (purified protein ± crowder, c_sat titration, salt/temperature sweeps) and cellular assays (optoDroplet/Corelet optogenetics, stress-granule or nucleolus recruitment, live imaging). Rough cost: an in-vitro c_sat/phase-diagram measurement for one construct runs thousands to low tens of thousands USD including protein production; a cellular condensate campaign runs more. No score removes this gate.

## 3. Standard of a genuine advance

A genuine advance is one or more of:
- A **leakage-safe, matched-negative method** predicting curated LLPS membership, with driver and client scored separately and gains shown not to be trivial disorder/composition separation.
- **New held-out performance** on in-vitro c_sat prediction (vs measured values) or on driver classification, exceeding catGRANULE/PScore/FuzDrop-lineage baselines under the frozen split.
- A **ranked, calibrated hypothesis set** - proteins predicted to be drivers with a predicted c_sat regime and the in-vitro/cellular assay that would falsify each - for a wet-lab partner.

**Not accepted as resolution.**
- AUROC on a positives-vs-random-negatives split (trivially separable by disorder/composition), presented as predicting phase separation.
- Calling a **client** a **driver**, or reporting a single blended metric that hides the driver/client distinction.
- A predicted phase diagram or coarse-grained c_sat with no experimental anchor, presented as established.
- Ignoring that the vast majority of "negatives" are untested, not confirmed non-LLPS.
- Any prediction without a calibrated propensity, or calibration untested on held-out data.
- A leaderboard number represented as a guarantee of cellular condensate formation.

## 4. Graded targets

**P0 - Data and split integrity.** Confirm matched negatives, study-level separation of c_sat measurements, and non-empty driver/client strata. Certificate: committed split manifest with negative-set construction and per-stratum counts.

**P1 - Reproduce biophysical and ML baselines.** catGRANULE, PScore (pi-pi), FuzDrop, and a composition/disorder logistic baseline reproduced on the committed matched-negative split; per-class (driver/client) tables established. Independently valuable.

**P2 - Bias-controlled classifier.** A sequence/biophysical model beating the baselines on driver classification under matched negatives and homology separation, with the gain shown to survive disorder/length/composition matching. Certificate: ablations, per-stratum tables, positive-unlabeled caveat quantified.

**P3 - Quantitative c_sat prediction.** Predict in-vitro saturation concentration with calibrated intervals, validated against held-out measurements; optionally cross-checked with a coarse-grained (HPS/Mpipi-style) single-sequence simulation. Certificate: MAE in log c_sat with CIs, reliability diagram, out-of-family generalization.

**P4 - Falsifiable hypothesis set.** For named proteins, ranked driver hypotheses with predicted c_sat regime, calibrated confidence, and the single in-vitro or cellular assay that would confirm/refute each. Certificate: frozen, hashed prediction registry predating experiment.

**P5 - Prospective confirmation (wet-lab partner).** Tested hypotheses reported as prospective outcomes, hits and misses, with confidence calibration assessed against realized phase behavior. Only this touches true condensate biology.

## 5. Known results and prior art

- **catGRANULE** (Bolognesi, Tartaglia et al. ~2016; catGRANULE 2.0 later, verify) - sequence-propensity predictor of RNA-granule/condensate association.
- **PScore** (Vernon, Forman-Kay et al. ~2018) - planar pi-pi contact propensity as an LLPS driver score.
- **FuzDrop** (Hardenberg, Fuxreiter et al. ~2020) - droplet-promoting probability from disorder and binding entropy.
- **PLAAC** (Lancaster, King et al. ~2014) - prion-like amino-acid composition, an early sequence driver score.
- **Stickers-and-spacers** theory (Choi, Holehouse, Pappu ~2020; Wang, Hyman et al. 2018 on FUS) - the physical framework separating drivers by valence/patterning; enables mechanistic c_sat prediction.
- **DeePhase** (Saar, Knowles et al. ~2021, verify), **PSAP**, **PhaSePred** (Chu, Liu et al. ~2022, verify) - ML predictors integrating sequence and biophysical features.
- Coarse-grained physics: **HPS** model (Dignon, Mittal et al. ~2018) and **Mpipi** (Joseph, Collepardo-Guevara et al. ~2021) - residue-resolution simulations that compute coexistence and c_sat.
- Databases: **PhaSePro**, **LLPSDB**, **DrLLPS**, **PhaSepDB**, **CD-CODE** (as above); reviews of LLPS-prediction dataset bias and benchmarking pitfalls (verify).

*Status as of mid-2026 - re-verify against current literature before starting any session.*

## 6. Attack plan

**Data.** Pull PhaSePro/LLPSDB/DrLLPS at frozen releases; build matched negatives (length, disorder, expression); cluster with MMseqs2; extract in-vitro c_sat values where present, keeping condition metadata.

**Features and baselines.** Composition/patterning (aromatic sticker counts, SCD, kappa), PScore pi-pi, disorder fraction, as interpretable features; reproduce catGRANULE/PScore/FuzDrop as the bar.

**Model.** A sequence model (biophysical features and/or ESM-2 embeddings) with separate driver and client heads; for c_sat, a regression head. `[struct]`: a residue-resolution HPS/Mpipi coarse-grained simulation channel to compute single-sequence coexistence as a physics cross-check for a subset.

**Concrete first steps (week 1).**
1. Freeze PhaSePro/LLPSDB/DrLLPS releases; harmonize driver/client labels; record conflicts.
2. Build matched negatives and MMseqs2 clusters; commit the split manifest.
3. Reproduce catGRANULE/PScore/FuzDrop; record per-class AUPRC on matched negatives.
4. Reproduce one published c_sat/phase diagram with the coarse-grained channel to validate it before use.
5. Fix the metric harness (per-class AUPRC, log-c_sat MAE) before modeling.

**Ablation and null-model panel.** Report, per class:
- composition/disorder logistic baseline;
- PScore (pi-pi) alone;
- FuzDrop alone;
- ESM-2 embedding head alone;
- the full model.
The headline must beat every single-channel ablation and survive length/disorder/composition matching.

**Cross-checks.** Where a coarse-grained c_sat is computed, compare its rank-ordering against the data-driven propensity; disagreement between physics and data channels is informative and reported, not hidden.

**One-GPU scope.** Feature/embedding + heads fit a single prosumer GPU. Small coarse-grained slab simulations (HOOMD-blue/LAMMPS/OpenMM) for a handful of sequences fit one GPU; a proteome-wide simulation sweep does not.

**Failure modes.** (i) The positive-unlabeled negative problem inflating easy separations - matched negatives and the caveat are the guard. (ii) Driver/client conflation - separate heads and tables. (iii) Corpus bias toward a few FUS/hnRNP-like sequences - organism/family stratification. (iv) c_sat measured under heterogeneous conditions - condition metadata must travel with the label.

## 7. Verification and auditability requirements

1. **Leakage-safe evaluation.** Homology, driver/client, organism, temporal, and matched-negative splits committed before evaluation; negative-set and study-level-separation protocols documented; no test-set tuning. The positive-unlabeled caveat accompanies every metric.
2. **Calibrated uncertainty.** Every propensity and c_sat prediction carries a calibrated confidence/interval; calibration reported on held-out and out-of-family data.
3. **Baseline parity and bias controls.** catGRANULE/PScore/FuzDrop reproduced; disorder/length/composition matching applied; ablations show any gain is not trivial separation.
4. **Independent reproduction.** Metrics recomputable from committed splits, predictions, and a separate scoring script; SHA-256 manifest over data-version hashes, code, simulation configs, and predictions.
5. **Preservation.** Feature/model/training code, coarse-grained simulation configurations, database version hashes, and split definitions are part of the record. Anything not preserved is stated explicitly.
6. **Prospective prediction registry.** The P4 hypothesis set (protein, driver/client, predicted c_sat regime, falsifying assay) is timestamped and hashed before any wet-lab test; no post-hoc edits.
7. **Honest reporting.** The report states up front that phase behavior is empirically defined and NOT resolved; separates in-silico metrics (including coarse-grained c_sat) from any in-vitro/cellular outcome; labels every driver call a wet-lab-pending hypothesis; and never presents a benchmark number as a guarantee of cellular condensate formation.
