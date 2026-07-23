# PROMPT FOR A PREDICTIVE GRAMMAR OF INTRINSICALLY DISORDERED REGION FUNCTION

## Sequence → function for IDRs, where composition and patterning - not fold - encode activity

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** B - reality-gated (empirical verifier)
**Rank:** B-15 of 29
**Source:** chem/bio top-50 list #22, section C (beyond static structure prediction)
**Modes:** `[data]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Intrinsically disordered regions (IDRs) make up a large fraction of eukaryotic proteomes and carry function without a fixed fold. Their activity - conditional binding through short linear motifs, phase-separation driving and modulation, entropic spacers and bristles, allosteric tethering, PTM display - is encoded not in a 3D structure but in a *grammar* of amino-acid composition and sequence patterning (charge patterning, aromatic/proline content, motif placement). This is the "dark proteome" of disorder: structure-prediction tools, by construction, say little about it. Sequence models and biophysically-grounded descriptors (CIDER-lineage patterning parameters, ensemble-dimension predictors) genuinely advance the mapping from sequence to IDR function. But IDR function is defined by biophysical and cellular measurement - NMR/SAXS ensembles, binding thermodynamics, cellular phase behavior - so compute can predict a curated functional class or a measurable biophysical descriptor, not establish the function itself. This is reality-gated. The deliverable is a leakage-safe, composition-controlled method that predicts IDR function *beyond bulk composition*, plus falsifiable biophysical hypotheses for a wet-lab partner.

## 1. Exact problem statement

**Input.** An IDR amino-acid sequence, or a full protein with a delineated disordered region (boundaries from experimental evidence or a stated predictor).

**Output.** Either or both, with calibrated confidence:
- **Functional class** of the IDR - a multi-label assignment over disorder-based function categories (molecular recognition via SLiM/MoRF, phase-separation driver vs modulator, flexible linker/spacer, entropic bristle, conditional/coupled folding, PTM/regulatory display).
- **Quantitative biophysical descriptor** correlated with measurement - e.g. predicted ensemble dimension (radius of gyration Rg or end-to-end Re / scaling exponent ν), or a binding/phase propensity.
- An explicit **abstention** where no class clears the confidence floor - abstention is a first-class output.

**Metric.** For classification: Fmax / AUPRC against DisProt functional annotations, reported per category. For descriptors: Spearman/Pearson and MAE vs experimental values (SAXS-derived Rg, NMR, or reference simulation). For **grammar specifically**: the gain over a composition-only (bag-of-amino-acid) baseline and over sequence-shuffled controls - the quantity that separates a learned *grammar* from mere composition counting.

**Population.** Disordered regions across proteomes, stratified by whether they carry an annotated function and by compositional class (acidic/basic/polar/aromatic-rich, poly-X).

**Scope and boundary conditions.**
- IDR boundaries come from experimental evidence (DisProt regions) where available and otherwise from a stated predictor with its threshold fixed before modeling; predictor-defined boundaries are flagged.
- Function is annotated at the region level, not the whole protein: one protein may carry several functionally distinct IDRs.
- Ordered-domain function is out of scope - the claim is specifically about the non-structural, disorder-encoded grammar.
- Conditional function (partner-, PTM-, concentration-dependent) is flagged where single-sequence input cannot capture it.

**Compute-tractable sub-question vs empirically-gated whole.** Tractable: predict the curated DisProt functional class and biophysical descriptors that correlate with measurements, demonstrably beyond bulk composition. Gated whole: the actual cellular/biophysical function of a given IDR, which requires assays.

## 2. Verifier and data

**Ground-truth source.**
- **DisProt** (Piovesan, Tosatto and colleagues; Aspromonte et al., verify) - the curated database of experimentally characterized disorder with **functional** annotations (the label source that matters here).
- **MobiDB** - disorder consensus and annotation aggregation (note: partly *predictor-derived*, so not experimental ground truth).
- **IDEAL**, **DIBS**, **MFIB** (verify) - disorder-based interactions (disorder-to-order on binding, complexes).
- **ELM** (Eukaryotic Linear Motif resource; Kumar, Gibson et al.) - experimentally validated short linear motifs.
- **PED** (Protein Ensemble Database; Lazar, Vranken et al.) - experimental IDR ensembles (SAXS/NMR) for descriptor ground truth.
- Phase-behavior overlap: **PhaSePro / LLPSDB** for IDRs annotated as phase-separation drivers (see B09).
- Evolutionary-signature datasets of IDR molecular features (Zarin, Moses et al. - verify).

**Frozen split (leakage-safe).** Committed before modeling:
1. **Homology + composition-aware clustering.** Cluster IDRs by sequence identity *and* by compositional/patterning similarity; no test cluster shares a member with train. The composition arm is essential - otherwise a model memorizes compositional bins and reports inflated numbers.
2. **Temporal.** Split by DisProt release date to simulate prospective annotation.
3. **Evidence provenance.** Separate experimentally-grounded disorder/function from predictor-derived labels (MobiDB consensus); the latter never serve as test ground truth.

**Known corpus biases.**
- Many "disorder" labels in aggregators are predictor-derived, not experimental - provenance separation is mandatory.
- DisProt is enriched for well-studied human/model-organism IDRs and for a few function classes (binding, phase separation), leaving others sparse.
- Experimental ensemble data (PED) cover a small, non-random slice of sequence space, so descriptor benchmarks generalize poorly out of composition.
- Function is often conditional (partner, PTM, concentration); single-sequence labels lose that context.

**Additional leakage traps.**
- Paralogous IDRs with near-identical composition bridging train and test below the identity threshold - the composition-clustering arm exists to catch this.
- Descriptor "ground truth" that is itself simulation-derived rather than measured - anchor on PED/SAXS and label simulation-derived targets as such.
- Motif databases (ELM) overlapping with test regions - hold motif-annotated regions out consistently.

**Wet-lab gate (mandatory).** IDR function needs biophysical and cellular assays: NMR/SAXS for ensemble dimensions and conditional folding, ITC/fluorescence/SPR for binding, cell-based assays (optogenetic, recruitment, signaling readout) for phase behavior and regulatory function. Rough cost: an NMR/SAXS ensemble characterization of one IDR runs tens of thousands USD and months (protein production + beamtime/spectrometer); a functional cellular campaign runs more. No descriptor prediction removes this gate.

## 3. Standard of a genuine advance

A genuine advance is one or more of:
- A **leakage-safe, composition-controlled method** predicting DisProt functional class or biophysical descriptors, with a demonstrated gain over composition-only and sequence-shuffle baselines - evidence of a learned *grammar*, not composition counting.
- **New held-out performance** on ensemble-dimension prediction (vs PED/SAXS) or functional classification, exceeding the strongest published descriptor-based and language-model baselines under the frozen split.
- A **ranked, calibrated set of biophysical hypotheses** - e.g. "this IDR is a phase-separation driver via aromatic sticker patterning; predicted Rg X; falsified by assay Y" - for a wet-lab partner.

**Not accepted as resolution.**
- Predicting *disorder itself* and presenting it as predicting function.
- A classifier whose performance is fully explained by bulk amino-acid composition (must beat the bag-of-AA baseline and survive sequence shuffling).
- Recovering CIDER-style descriptors (kappa, FCR, NCPR, SCD) and calling the descriptors "function."
- An in-silico phase diagram or single-chain simulation presented as established cellular function.
- Any prediction without a calibrated confidence, or calibration untested on held-out data.
- A benchmark number represented as a biophysical guarantee.

## 4. Graded targets

**P0 - Data and split integrity.** Confirm the frozen split separates experimental from predictor-derived labels and that homology+composition clustering leaves no bridge between train and test. Certificate: committed split manifest with cluster membership and provenance flags.

**P1 - Reproduce descriptor and disorder-function baselines.** CIDER/localCIDER patterning descriptors, metapredict-style disorder, and a published functional classifier reproduced on the committed split; composition-only and shuffle baselines established as the bar. Independently valuable.

**P2 - Grammar-beyond-composition method.** A sequence model (patterning-aware features and/or ESM-2 embeddings) that beats composition-only and sequence-shuffle controls on DisProt functional classification or PED-referenced dimension prediction, under strict homology+composition splitting. Certificate: ablations vs both null baselines, per-category tables.

**P3 - Calibrated descriptor prediction.** Ensemble-dimension (Rg / scaling exponent) prediction with calibrated uncertainty, validated against held-out SAXS/NMR ensembles. Certificate: reliability diagram, MAE with CIs, out-of-composition generalization.

**P4 - Falsifiable biophysical hypothesis set.** For named IDRs, ranked functional/biophysical hypotheses with calibrated confidence and the single assay (SAXS, ITC, cellular) that would confirm or refute each. Certificate: frozen, hashed prediction registry predating experiment.

**P5 - Prospective confirmation (wet-lab partner).** Tested hypotheses reported as prospective outcomes, hits and misses, with confidence calibration assessed against realized outcomes. Only this target touches true function.

## 5. Known results and prior art

- **DisProt** (Piovesan, Tosatto et al. ~2007–2023) and **MobiDB** - curated disorder and functional annotation.
- **CIDER / localCIDER** (Holehouse, Pappu et al. ~2017) - charge patterning (kappa), FCR/NCPR, the sequence-patterning framework; **metapredict** (Emenecker, Holehouse ~2021) - fast disorder prediction.
- **ALBATROSS** (Lotthammer, Holehouse et al. ~2024, verify) - deep prediction of IDR global dimensions (Rg, Re, ν) from sequence, trained on simulation.
- **Zarin, Moses et al.** (~2019–2021, verify) - evolutionary conservation of *molecular features* of IDR function rather than sequence; a grammar-of-features view.
- **flDPnn** (Hu, Kurgan et al. ~2021) - function-aware disorder prediction with per-residue functional annotations.
- Disorder / disordered-binding predictors: **IUPred2A / ANCHOR2** (Mészáros, Dosztányi ~2018), **SPOT-Disorder**, **AlphaFold pLDDT** as a disorder proxy; **ANCHOR**/MoRF predictors for disorder-based binding regions.
- Motif/interaction: **ELM** resource (Kumar, Gibson et al.).
- **FuzDrop** (Hardenberg, Fuxreiter ~2020) - disorder-driven phase-separation propensity (overlaps B09).
- **PED** (Lazar, Vranken et al.) - experimental IDR ensembles for descriptor benchmarking.
- Stickers-and-spacers framework (Choi, Holehouse, Pappu ~2020) - the physical grammar underlying aromatic/charge patterning effects; **SHEPHARD / sparrow** (Holehouse lab tooling, verify) - large-scale IDR feature analysis.

*Status as of mid-2026 - re-verify against current literature before starting any session.*

## 6. Attack plan

**Data.** Pull DisProt (frozen release) functional annotations, PED ensembles, ELM motifs; build homology+composition clusters; separate experimental from predictor-derived labels.

**Features and baselines.** Compute CIDER/localCIDER patterning descriptors as the interpretable baseline; a bag-of-amino-acid model and a sequence-shuffle control as the null grammar baselines that must be beaten.

**Model.** Patterning-aware sequence encoder (CNN/bi-LSTM in the ALBATROSS spirit) and/or ESM-2 embeddings feeding multi-label functional heads and a regression head for dimensions. Explicitly test whether the model uses order (shuffle test) versus composition.

**Concrete first steps (week 1).**
1. Freeze a DisProt release; extract region-level functional labels with evidence flags.
2. Build homology and composition clusters; commit the split manifest.
3. Compute CIDER descriptors and the bag-of-AA / shuffle null baselines; record their scores.
4. Cache ESM-2 embeddings for all regions.
5. Fix the metric harness (per-category Fmax, descriptor MAE, shuffle-gain) before modeling.

**Ablation and null-model panel.** For every headline result report:
- composition-only (bag-of-AA) baseline;
- sequence-shuffle control (same composition, scrambled order);
- CIDER-descriptor baseline;
- the full model.
A grammar claim must beat all three, and the shuffle gain must be positive and significant.

**Cross-checks.** Compare against ALBATROSS/CIDER descriptor predictions as an orthogonal channel; where the model claims a phase-separation function, cross-reference FuzDrop/PScore; report agreement and disagreement rather than a single blended score.

**One-GPU scope.** Descriptor computation is CPU; ESM-2 embedding + light heads fit one prosumer GPU. Coarse-grained single-chain simulation cross-checks (HPS/Mpipi) for a few sequences are optional and small.

**Failure modes.** (i) Composition memorization - the shuffle and bag-of-AA baselines are the guard. (ii) Predictor-derived labels leaking as ground truth - provenance separation. (iii) Descriptor ground truth being simulation-derived, not experimental - anchor on PED/SAXS. (iv) Context loss - IDR function is often conditional and single-sequence prediction cannot capture it.

## 7. Verification and auditability requirements

1. **Leakage-safe evaluation.** Homology+composition and temporal splits committed before evaluation; clustering parameters and evidence-provenance rules documented; no test-set tuning.
2. **Calibrated uncertainty.** Every functional call and descriptor prediction carries a calibrated confidence/interval; calibration reported on held-out and out-of-composition data.
3. **Grammar-vs-composition controls.** Composition-only and sequence-shuffle null baselines reported for every headline result; any claimed grammar must beat both.
4. **Independent reproduction.** Metrics recomputable from committed splits, predictions, and a separate scoring script; SHA-256 manifest over data-version hashes, code, and predictions.
5. **Preservation.** Feature/model/training code, database version hashes, and split definitions are part of the record. Anything not preserved is stated explicitly.
6. **Prospective prediction registry.** The P4 hypothesis set is timestamped and hashed before any wet-lab test; no post-hoc edits.
7. **Honest reporting.** The report states up front that IDR function is empirically defined and NOT resolved; separates predicted class/descriptor metrics from any assay outcome; labels every functional call a wet-lab-pending hypothesis; and never presents a benchmark number as a biophysical guarantee.
