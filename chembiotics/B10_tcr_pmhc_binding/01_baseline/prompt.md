# PROMPT FOR TCR:pMHC BINDING AND IMMUNOGENICITY PREDICTION

## Generalizing to unseen epitopes, where data are scarce and biased toward a few well-studied peptides

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** B - reality-gated (empirical verifier)
**Rank:** B-10 of 29
**Source:** chem/bio top-50 list #47, section G (higher-order / adjacent)
**Modes:** `[data]` `[struct]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Predicting whether a T-cell receptor (TCR) binds a peptide-MHC (pMHC) complex, and whether that pMHC is immunogenic, is central to personalized cancer vaccines and immunotherapy. It is also notoriously data-limited and biased: public binding data are dominated by a handful of well-studied epitopes, so models that look strong on random splits collapse on **unseen epitopes** - the case that actually matters for neoantigen design. Sequence models advance the pMHC-binding side (NetMHCpan is mature) and the TCR side (NetTCR, ERGO, TCRdist), and structure predictors are beginning to model the ternary complex. But binding and immunogenicity are defined by tetramer/multimer staining and functional T-cell assays, and generalization to new epitopes is unproven. Compute can predict binding-database membership under honest splits; it cannot establish that a TCR recognizes a new epitope, still less that it is immunogenic in a patient. This is reality-gated. The deliverable is a method whose performance is reported under a strict **unseen-epitope split**, with realistic negatives and calibrated confidence, plus falsifiable predictions for a wet-lab partner - never a claimed general solution.

## 1. Exact problem statement

**Input.** A TCR (CDR3β, optionally CDR3α, with V/J gene usage), a peptide, and an MHC allele (class I focus initially; class II is harder and noted as scope).

**Output.** Either or both, with calibrated confidence:
- **Binding probability** for the TCR–pMHC pair.
- **Immunogenicity** of the pMHC (its likelihood of eliciting a T-cell response), where that label exists.
- Optionally a **structural model** of the ternary complex (`[struct]`) with a confidence score.

**Metric.** AUROC and AUPRC for binding, but reported **separately for seen and unseen epitopes** - the unseen-epitope AUPRC is the headline. Per-epitope breakdown (to expose the few-epitope dominance). For structure: DockQ / interface-RMSD against known complexes. Immunogenicity: AUPRC on held-out epitopes.

**Population.** TCR–pMHC pairs, dominated in public data by a few epitopes (e.g. common viral peptides). The honest population weights performance toward epitopes and MHC alleles *not* seen in training.

**Compute-tractable sub-question vs empirically-gated whole.** Tractable: predict binding-database membership under an unseen-epitope split with realistic negatives. Gated whole: whether a TCR functionally recognizes a new epitope and drives an immune response, which needs tetramer and functional assays.

## 2. Verifier and data

**Ground-truth source.**
- **VDJdb** (Shugay et al. ~2018), **IEDB** (Vita et al.), **McPAS-TCR** (Tickotsky et al. ~2017) - curated TCR–pMHC binding pairs with confidence scores.
- **10x Genomics dextramer** single-cell datasets and **ImmuneCODE / TChard** (verify) - larger, noisier binding readouts.
- **STCRDab** (Leem et al. ~2018) / **TCR3d** - structural TCR–pMHC complexes for the `[struct]` arm.
- **NetMHCpan** training data (Nielsen and colleagues) - pMHC binding/presentation, the upstream filter.

**Frozen split (leakage-safe).** The crux. Committed before modeling:
1. **Unseen-epitope split** - entire epitopes (peptides) held out of training; the primary, headline evaluation. Seen-epitope performance is reported only as a contrast.
2. **TCR-cluster split** (TCRdist-based) - avoid near-duplicate TCRs bridging train and test.
3. **MHC-allele stratification** - report generalization across alleles, not just the dominant HLA-A*02:01.
4. **Negative-set protocol** - the known confound: random TCR–peptide pairings are trivially separable and inflate scores. Use true experimentally-determined non-binders where available; where synthetic negatives are unavoidable, report their construction and treat the result as an upper bound.

**Wet-lab gate (mandatory).** Binding and immunogenicity need tetramer/multimer staining and functional T-cell assays (activation markers, cytokine secretion, cytotoxicity), typically with HLA-matched primary cells. Rough cost: tetramer validation of a handful of TCR–epitope pairs runs thousands to tens of thousands USD; a functional immunogenicity screen with primary cells and HLA matching runs substantially more and takes months. No score removes this gate.

## 3. Standard of a genuine advance

A genuine advance is one or more of:
- A **leakage-safe pipeline** reproducing NetTCR/ERGO/TCRdist baselines under both seen- and unseen-epitope splits with realistic negatives.
- **New held-out performance on the unseen-epitope split specifically** - a significant AUPRC gain over the strongest baselines on epitopes and alleles absent from training, with negatives honestly constructed.
- A **ranked, calibrated prediction set** - TCR–neoantigen pairs predicted to bind, with calibrated confidence and the tetramer/functional assay that would confirm/refute each - for a wet-lab partner.

**Not accepted as resolution.**
- AUROC on a seen-epitope (or random) split, presented as predicting TCR recognition - this memorizes a few epitopes.
- Scores inflated by shuffled/random negatives without disclosure.
- Predicting **binding** but claiming **immunogenicity** (binding is necessary, not sufficient).
- A structural complex model with no experimental validation, presented as established.
- A neoantigen ranking presented as validated without T-cell assays.
- Any prediction without a calibrated confidence, or calibration untested on unseen epitopes.
- A leaderboard number represented as a guarantee of patient immunogenicity.

## 4. Graded targets

**P1 - Reproduce the baselines under honest splits.** NetTCR-2.0, ERGO-II, and TCRdist reproduced on VDJdb/IEDB with both seen- and unseen-epitope splits and a documented negative-set protocol; the seen-vs-unseen gap quantified. Independently valuable as a trusted, sobering baseline.

**P2 - Unseen-epitope method.** A model (TCR + peptide + MHC-pseudosequence encoders, possibly ESM-based) that improves unseen-epitope AUPRC over the baselines with realistic negatives and TCR-cluster separation. Certificate: per-epitope and per-allele tables, negative-set ablation.

**P3 - Calibrated confidence.** Calibrated per-epitope binding confidences (reliability diagrams on unseen epitopes), acknowledging that calibration on never-seen epitopes is the hard and honest test. Certificate: ECE on unseen epitopes, coverage.

**P4 - Falsifiable prediction set.** For named neoantigens/TCRs, ranked binding (and where possible immunogenicity) predictions with calibrated confidence and the tetramer/functional assay that would confirm/refute each. Optionally a structural model per pair with its confidence. Certificate: frozen, hashed prediction registry predating experiment.

**P5 - Prospective confirmation (wet-lab partner).** Tested predictions reported as prospective outcomes, hits and misses, with confidence calibration assessed against realized tetramer/functional results. Only this touches true recognition and immunogenicity.

## 5. Known results and prior art

- **NetTCR / NetTCR-2.0** (Montemurro, Nielsen et al. ~2021) - CNN for TCR–pMHC binding.
- **ERGO / ERGO-II** (Springer, Louzoun et al. ~2020–2021) - LSTM/autoencoder TCR–peptide binding.
- **TCRdist / tcrdist3** (Dash et al. 2017; Mayer-Blackwell et al. 2021) - biochemical TCR distance metric and repertoire clustering.
- **pMTnet** (Lu et al. 2021) - explicitly targets unseen-epitope generalization for TCR–pMHC.
- pMHC presentation: **NetMHCpan-4.1** (Reynisson, Nielsen et al. 2020) and **MHCflurry** (O'Donnell, Hammerbacher et al.) - mature upstream binding/presentation predictors.
- Structure: **AlphaFold-Multimer** applied to TCR–pMHC and **TCRdock** (Bradley ~2023, verify) - ternary-complex modeling with variable success.
- Immunogenicity: **PRIME** (Schmidt, Gfeller et al.), **DeepImmuno** (verify).
- Benchmarking caution: Moris et al. (~2021) and Grazioli et al. - documenting that TCR–pMHC models **fail to generalize to unseen epitopes**, the defining open problem here.

*Status as of mid-2026 - re-verify against current literature before starting any session.*

## 6. Attack plan

**Data.** Pull VDJdb/IEDB/McPAS-TCR at frozen releases with confidence filtering; STCRDab for structures; commit the unseen-epitope and TCR-cluster splits before training; fix the negative-set protocol (true non-binders where available).

**Baselines.** Reproduce NetTCR-2.0, ERGO-II, TCRdist nearest-neighbor, under both split regimes - the seen-vs-unseen gap is the reality check.

**Model.** Encoders for CDR3β(/α) with V/J context, peptide, and MHC pseudosequence; ESM-2 embeddings for peptide/TCR sequences; a binding head trained under strict unseen-epitope CV. `[struct]`: AlphaFold-Multimer / TCRdock for a subset as a structural cross-check for high-confidence predictions.

**Calibration.** Per-epitope temperature scaling or conformal prediction; calibration measured on unseen epitopes - the only honest calibration test here.

**One-GPU scope.** Sequence encoders, ESM embeddings, and binding heads fit a single prosumer GPU. AlphaFold-Multimer/TCRdock inference for a handful of complexes fits one GPU; a large structural sweep does not.

**Failure modes.** (i) Few-epitope dominance and seen-epitope leakage - the unseen-epitope split and per-epitope tables are the guard. (ii) Negative-set artifacts - realistic negatives and disclosure. (iii) Binding≠immunogenicity - keep the two labels and claims separate. (iv) Class II and rare alleles - data are even scarcer; flag as scope limits, do not extrapolate silently.

## 7. Verification and auditability requirements

1. **Leakage-safe evaluation.** Unseen-epitope and TCR-cluster splits committed before evaluation; MHC-allele stratification and negative-set protocol documented; seen-epitope performance reported only as a contrast; no test-set tuning.
2. **Calibrated uncertainty.** Every binding/immunogenicity prediction carries a calibrated confidence; calibration (reliability diagram, ECE) reported specifically on unseen epitopes.
3. **Baseline parity and negative-set controls.** NetTCR/ERGO/TCRdist reproduced under both split regimes; negative-set construction ablated and disclosed; the seen-vs-unseen gap reported.
4. **Independent reproduction.** Metrics recomputable from committed splits, predictions, and a separate scoring script; SHA-256 manifest over data-version hashes, code, and predictions.
5. **Preservation.** Model/training code, split and negative-set definitions, database version hashes, and calibration procedure are part of the record. Anything not preserved is stated explicitly.
6. **Prospective prediction registry.** The P4 prediction set (TCR, peptide, MHC, predicted binding/immunogenicity + confidence, assay) is timestamped and hashed before any wet-lab test; no post-hoc edits.
7. **Honest reporting.** The report states up front that binding and immunogenicity are empirically defined and the problem is NOT resolved; separates in-silico metrics from any tetramer/functional outcome; never presents binding as immunogenicity; labels every prediction a wet-lab-pending hypothesis; and never presents a benchmark number as a guarantee of patient immunogenicity.
