# PROMPT FOR POINT-MUTATION ΔΔG AT DEEP-MUTATIONAL-SCAN SCALE

## Predicting the effect of substitutions on protein stability and function, leakage-safe

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** B - reality-gated (empirical verifier)
**Rank:** B-02 of 29
**Source:** chem/bio top-50 list #21, section C (beyond static structure prediction)
**Modes:** `[func]` `[data]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Predicting how a point mutation changes a protein's folding stability (ΔΔG) and its function is of enormous clinical and engineering utility - variant interpretation, protein stabilization, deep-mutational-scan (DMS) design. This is the most hands-on Pack B entry point: the data are public, large, and machine-checkable (ProteinGym, MaveDB, mega-scale folding-stability corpora, FireProtDB, SKEMPI), and a competent baseline runs on one GPU. Sequence models (ESM zero-shot), physics tools (FoldX, Rosetta), and structure-based supervised models genuinely advance it. But novel ΔΔG values are defined by measurement - biophysical denaturation or high-throughput DMS - and the notorious failure mode is **leakage across homologs**: a model that has effectively seen a test protein's family reports inflated accuracy that collapses on a truly unseen fold. This is reality-gated. The deliverable is a leakage-safe, calibrated method whose accuracy survives homology-clean and antisymmetry controls, plus falsifiable ΔΔG predictions for a wet-lab partner - never a claimed general solution to variant effect.

## 1. Exact problem statement

**Input.** A wild-type protein (sequence, optionally experimental or predicted structure) and a substitution (single point mutation, or a defined set/combination).

**Output.** Either or both, with calibrated uncertainty:
- **ΔΔG of folding** in kcal/mol (sign convention fixed and stated; destabilizing vs stabilizing).
- A **functional fitness score** (DMS-style), where the assay measures activity/abundance rather than pure thermodynamic stability.

**Metric.**
- Per-protein/per-assay **Spearman ρ** between predicted and measured scores (the ProteinGym convention), averaged across assays.
- For ΔΔG specifically: **Pearson r and MAE in kcal/mol** vs biophysical values; and the **antisymmetry** check ΔΔG(A→B) ≈ −ΔΔG(B→A) on antisymmetric benchmarks (Ssym).
- Classification of stabilizing / neutral / destabilizing where thresholds are defined.
- **Stability and function reported separately** - they are different assays and must not be blended.

**Population.** Substitutions across diverse proteins/folds. The compute-tractable sub-question is predicting measured DMS/stability scores under leakage-safe evaluation; the empirically-gated whole is generalizing to proteins and folds with *no* measurements, and to clinical pathogenicity, which depends on biology beyond stability.

## 2. Verifier and data

**Ground-truth source.**
- **ProteinGym** (Notin et al. ~2023) - the large DMS + clinical-substitution benchmark suite with standardized splits and zero-shot/supervised leaderboards.
- **MaveDB** (Esposito et al. ~2019) - multiplexed assay of variant effect datasets.
- **Mega-scale folding-stability** data (Tsuboyama, Rocklin et al. ~2023, verify) - proteolysis-based ΔG for hundreds of thousands of variants across many mini-domains: the largest clean thermodynamic corpus.
- **FireProtDB** (Stourac et al. ~2021) and **ThermoMutDB / ProThermDB** (verify) - curated single-variant ΔΔG.
- **SKEMPI 2.0** (Jankauskaitė et al. ~2019) - binding ΔΔG for protein–protein complexes (the binding, not folding, arm).
- **Ssym / S669** (Pancotti et al. and predecessors, verify) - curated antisymmetric ΔΔG benchmarks designed to expose bias.

**Frozen split (leakage-safe).** The heart of this problem. Committed before modeling:
1. **Homology clustering** (MMseqs2 sequence identity, plus structural clustering) so that **no test protein is homologous to any train protein** - the single most abused control in this field.
2. **ProteinGym-style cross-validation schemes** (random / modulo / contiguous position splits) reported, but always alongside the protein-holdout homology-clean scheme, which is the honest one.
3. **Antisymmetry control** via Ssym - a model must not systematically favor destabilizing predictions.
4. **Temporal split for clinical variants** (ClinVar release date) so pathogenicity labels are not circularly inherited.

**Wet-lab gate (mandatory).** A novel ΔΔG needs measurement: biophysical denaturation (thermal/chemical, DSC, CD) for a single variant, or a high-throughput proteolysis/DMS library for scale. Rough cost: a single-variant biophysical ΔΔG runs low thousands USD and weeks; a mega-scale DMS/proteolysis library runs tens to hundreds of thousands USD but returns 10^4–10^5 measurements. Clinical pathogenicity requires clinical/functional evidence beyond any stability number. No score removes this gate.

## 3. Standard of a genuine advance

A genuine advance is one or more of:
- A **certified, leakage-safe pipeline** reproducing ProteinGym zero-shot (ESM-1v/ESM-2 marginals) and a supervised SOTA on the homology-clean protein-holdout scheme, with antisymmetry controlled.
- **New held-out SOTA under homology-clean splitting** - a significant Spearman/ΔΔG-MAE gain over the strongest zero-shot and structure-based baselines that survives on truly unseen folds and passes the antisymmetry check.
- A **ranked, calibrated ΔΔG prediction set** (kcal/mol with intervals) for named proteins/variants, ready for a wet-lab partner, with the stabilizing candidates flagged for biophysical test.

**Not accepted as resolution.**
- A high average Spearman inflated by homologous train/test proteins (the canonical failure).
- A zero-shot or supervised number reported without the antisymmetry (Ssym) and homology controls.
- Conflating **stability** with **function**, or either with **clinical pathogenicity**.
- A "clinically useful variant classifier" claim from ProteinGym clinical AUROC without prospective, biology-grounded validation.
- Any ΔΔG without a calibrated interval, or calibration untested on held-out data.
- A leaderboard rank represented as a real-world ΔΔG guarantee.

## 4. Graded targets

**P1 - Reproduce the ProteinGym frontier.** ESM-1v/ESM-2 zero-shot masked-marginal scores and one supervised baseline (e.g. a structure-based ΔΔG model) reproduced on ProteinGym and on FireProtDB/Ssym, matched to reported Spearman/MAE. Independently valuable as a trusted baseline. **Flagged hands-on entry point: this P1 is achievable on public data with machine-checkable ground truth on one GPU.**

**P2 - Leakage-safe supervised model.** Train on mega-scale stability data with homology-clean protein-holdout CV; report Spearman/MAE on unseen folds and the antisymmetry check. Certificate: split definitions, per-fold tables, Ssym results, ablations.

**P3 - Calibrated ΔΔG in kcal/mol.** Upgrade predictions to calibrated intervals in kcal/mol (conformal or ensemble), validated against held-out biophysical ΔΔG. Certificate: reliability diagram, coverage, MAE with CIs on unseen folds.

**P4 - Falsifiable prediction set.** For named proteins, ranked ΔΔG predictions with calibrated intervals; stabilizing candidates flagged with the biophysical assay that would confirm/refute each. Certificate: frozen, hashed prediction registry predating experiment.

**P5 - Prospective confirmation (wet-lab partner).** Tested predictions reported as prospective outcomes, hits and misses, with interval calibration assessed against realized measurements. Only this touches true ΔΔG.

## 5. Known results and prior art

- **FoldX** (Schymkowitz, Serrano et al. ~2005) and **Rosetta ddG / cartesian_ddg** (Park, DiMaio, Kuhlman et al. ~2016) - physics/statistical ΔΔG standards; fast (FoldX) vs accurate (Rosetta) trade-off.
- **DDGun** (Montanucci, Fariselli, Casadio ~2019) - untrained, antisymmetric baseline; **ACDC-NN** (antisymmetry-enforcing NN).
- **ESM-1v** (Meier, Rives et al. 2021) and **ESM-2** (Lin et al. 2023) - zero-shot variant-effect scores from masked-language-model marginals; **Tranception** (Notin et al. 2022) - retrieval-augmented autoregressive scoring; **EVE** (Frazer, Marks et al. 2021) - evolutionary VAE for clinical variants.
- **ProteinGym** (Notin et al. 2023) - the standardized benchmark and leaderboard.
- **RaSP** (Blaabjerg, Lindorff-Larsen et al. ~2023) - fast Rosetta-trained ΔΔG surrogate; **ThermoMPNN** (Dieckhaus, Kuhlman ~2024, verify) - ProteinMPNN-based supervised ΔΔG; **Stability Oracle** (Diaz et al. ~2024, verify); **PROSTATA** (verify).
- **Tsuboyama, Rocklin et al.** (~2023, verify) - mega-scale folding-stability measurement by proteolysis.
- Benchmark-bias literature (Pancotti et al.; Ssym/S669) - documenting antisymmetry and homology leakage as the field's systematic errors.

*Status as of mid-2026 - re-verify against current literature before starting any session.*

## 6. Attack plan

**Data.** Pull ProteinGym (frozen version), the mega-scale stability corpus, FireProtDB, Ssym/S669, and SKEMPI for the binding arm; cluster all proteins by sequence and structure with MMseqs2/Foldseek; commit the homology-clean protein-holdout split before any training.

**Baselines.** ESM-1v/ESM-2 zero-shot masked-marginal scores (one GPU); DDGun (untrained, antisymmetric); FoldX/Rosetta on a subset. These are the bar.

**Model.** `[func]` A structure-based supervised head (ProteinMPNN/ThermoMPNN-style) and/or an ESM-2 fine-tuned regressor trained on mega-scale stability with homology-clean CV; enforce or test antisymmetry by A→B / B→A augmentation.

**Calibration.** Conformal prediction or deep ensembles for kcal/mol intervals; calibration and coverage measured on held-out unseen folds.

**One-GPU scope.** ESM-2 650M/3B inference and zero-shot scoring, ProteinMPNN, and light supervised heads all fit a single prosumer GPU. Rosetta ddG is CPU and slow - use on a subset only.

**Failure modes.** (i) Homology leakage - the protein-holdout split is the guard; report the naïve random-split number too, to *show* the inflation. (ii) Antisymmetry bias - Ssym is mandatory. (iii) Stability/function/pathogenicity conflation - separate assays, separate metrics. (iv) Assay heterogeneity in DMS (abundance vs activity vs binding) - do not pool incomparable readouts.

## 7. Verification and auditability requirements

1. **Leakage-safe evaluation.** Homology-clean protein-holdout split (sequence + structure clustering) committed before evaluation; ProteinGym CV schemes and the naïve random split reported alongside to expose leakage; no test-set tuning.
2. **Calibrated uncertainty.** Every ΔΔG carries a calibrated interval in kcal/mol; calibration and coverage reported on held-out unseen folds.
3. **Bias controls and baseline parity.** ESM zero-shot, DDGun, and a physics baseline reproduced; the antisymmetry (Ssym) check reported for every model; stability and function scored separately.
4. **Independent reproduction.** Metrics recomputable from committed splits, predictions, and a separate scoring script; SHA-256 manifest over data-version hashes, code, and predictions.
5. **Preservation.** Model/training code, split definitions, database version hashes, and calibration procedure are part of the record. Anything not preserved is stated explicitly.
6. **Prospective prediction registry.** The P4 prediction set (protein, variant, predicted ΔΔG + interval, assay) is timestamped and hashed before any wet-lab test; no post-hoc edits.
7. **Honest reporting.** The report states up front that novel ΔΔG is empirically defined and the problem is NOT resolved; separates in-silico metrics from any measurement; never conflates stability with function or pathogenicity; labels every prediction a wet-lab-pending hypothesis; and never presents a leaderboard number as a real-world ΔΔG guarantee.
