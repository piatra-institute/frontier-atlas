# PROMPT FOR CALIBRATED EFFECT PREDICTION OF NON-CODING AND STRUCTURAL VARIANTS

## Ranking the regulatory and structural genome by functional and clinical consequence

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** B - reality-gated (empirical verifier)
**Rank:** B01 of 29
**Source:** chem/bio top-50 list #36, section E (genomics)
**Modes:** `[data]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

> **Audit note (July 2026 - see `../../STATUS_AUDIT_2026-07.md`):** SOTA moved decisively in 2025. **AlphaGenome** (DeepMind; Nature 2025), a unified 1-Mb DNA→function model, reports SOTA on 25/26 variant-effect tasks and is now the baseline to beat for the non-coding fraction. The problem is not resolved - causal effect stays wet-gated (MPRA/reporter), and calibrated non-coding pathogenicity is unsolved - but reproduce/benchmark against AlphaGenome in P1 rather than the older scorers.

### Abstract

Most of the human genome is non-coding, and most variants of uncertain significance (VUS) that reach a clinic fall outside protein-coding exons or are structural (CNVs, inversions, mobile-element insertions). Coding missense interpretation has advanced sharply (the AlphaMissense lineage), but the non-coding and structural fraction - larger, and where regulatory logic hides - remains the harder, more clinically consequential problem. The task is to predict, from reference sequence and genomic context, the functional and clinical effect of a non-coding or structural variant, with calibrated uncertainty, and to separate what is *correlational* (a variant tags a signal via linkage) from what is *causal* (the variant itself drives a molecular phenotype). This is reality-gated: the ground truth is empirical - reporter assays, eQTL maps, patient outcomes - so compute can produce a certified method, a held-out benchmark result, and a ranked set of falsifiable predictions, but the loop is closed by a wet lab or a clinic, never by the model. No claimed resolution is on offer, and no clinical claim is anything but a hypothesis pending experimental and clinical validation.

## 1. Exact problem statement

**Input.** A variant defined against a fixed reference build:

- for a small variant, `(chrom, pos, ref, alt)` on GRCh38 primary assembly, with any GRCh37 liftover documented and the liftover failures reported;
- for a structural variant, a typed interval - deletion, duplication, insertion, inversion, or translocation breakpoint - with coordinates and, where available, breakpoint-resolved sequence;
- optional context: a tissue or cell type, and a candidate target gene or regulatory element.

**Output.** Three separable predictions, each with a calibrated confidence:

1. **Molecular effect (regression).** A signed, magnitude-bearing effect on a defined molecular phenotype - allelic effect on expression (log fold-change), chromatin accessibility, transcription-factor binding, or reporter activity - for a named cell type or tissue.
2. **Functional classification.** Probability that the variant is functional/regulatory versus neutral in a defined context.
3. **Clinical pathogenicity (hypothesis-labeled).** Probability of pathogenicity for a stated condition, explicitly framed as a computational hypothesis, never a determination.

**Metric.** Fixed before modeling and reported with confidence intervals from a committed resampling scheme:

- molecular effect: Spearman and Pearson correlation against measured effect sizes, plus sign-concordance, stratified by element class (promoter, enhancer, splice-adjacent, UTR, intergenic);
- classification/pathogenicity: area under precision–recall (auPRC - primary, because pathogenic non-coding variants are rare) and auROC;
- calibration: expected calibration error (ECE) and reliability curves for every probabilistic output;
- a **causal-controlled** variant of the molecular metric, evaluated only on fine-mapped credible-set variants, reported separately from the LD-tagging-permissive metric.

**Population.** Non-coding single-nucleotide variants and small indels genome-wide; structural variants by type; reported per ancestry group where cohort labels permit, because effect sizes and allele frequencies are ancestry-dependent.

**Compute-tractable sub-question vs empirically-gated whole.**

- *Tractable:* given a frozen molecular-assay corpus (MPRA, eQTL, saturation mutagenesis), predict held-out allelic molecular effects with calibrated uncertainty under a leakage-safe split.
- *Empirically-gated (not claimable on the machine):* that a given non-coding or structural variant *causes* a specific clinical phenotype in a real patient.

## 2. Verifier and data

**Ground-truth sources.**

- **ClinVar** - clinically asserted variant significance; non-coding subset is small and review-status-heterogeneous. Filter by review status (star rating); treat single-submitter assertions as weak labels.
- **gnomAD (v4)** - population allele frequencies and non-coding constraint metrics (genome-wide constraint / "Gnocchi"-type scores, Chen et al. - verify current release); SV catalog for structural variants.
- **GTEx (v8/v10 - verify latest)** - tissue eQTL/sQTL effect sizes and fine-mapped credible sets; the primary correlational causal-QTL resource.
- **GWAS Catalog** and **Open Targets Genetics** (verify) - trait associations and locus-to-gene evidence.
- **MPRA and saturation-mutagenesis corpora** - massively parallel reporter assays and saturation mutagenesis of regulatory elements (Kircher et al. saturation-mutagenesis MPRA, ~2019; enhancer MPRA atlases - verify specific accessions). The closest thing to a direct causal readout of regulatory variant effect.
- **MaveDB / MAVE** - multiplex assays of variant effect, mostly coding but with regulatory entries growing (verify non-coding coverage).
- **ENCODE / Roadmap** epigenome tracks - used as feature context, never as labels for effect.

**Frozen, leakage-safe split.** Commit before any modeling and hash the manifest.

- **Chromosome holdout** for genome-wide claims: hold out entire chromosomes (e.g. chr8, chr9, chrX) so no test locus shares local sequence with training.
- **LD-block / locus holdout** for eQTL and GWAS labels: variants in linkage disequilibrium share signal, so splitting by variant leaks - hold out whole LD blocks or fine-mapped loci.
- **Element holdout** for MPRA: hold out entire regulatory elements, not positions within an element, so saturation-mutagenesis neighbors do not straddle the split.
- **Ancestry considerations:** report performance separately for each ancestry group present; do not average away a portability gap. ClinVar and most reporter libraries are European-ancestry-biased - state this as a property of the label distribution, not of the biology.

**Negative controls and label caveats.** Fixed before modeling:

- allele-frequency-matched neutral (putatively benign) variants as a null class, so enrichment is measured against a realistic background rather than random positions;
- label-shuffled and position-shuffled runs to bound the score achievable by leakage or memorization;
- an orthogonal-predictor agreement report kept strictly separate from the empirical metric (agreement with another model is not evidence of correctness).

**Wet-lab gate (mandatory).** No causal molecular-effect claim for a novel variant is established without a new physical experiment: an MPRA / episomal or genomic reporter assay for regulatory activity, base-editing or prime-editing to install the variant in its native locus, or CRISPRi/a perturbation to test the target-gene link. Indicative cost: a targeted MPRA library covering a few thousand variants runs roughly tens of thousands of USD in reagents and sequencing; saturation mutagenesis of a single regulatory element roughly USD 10k–50k; per-variant base-editing validation in the relevant cell type runs a few thousand USD each and weeks of work. Clinical pathogenicity requires segregation, case–control, or functional-in-patient evidence that no assay alone supplies. This gate is not optional and must not be softened in any report.

## 3. Standard of a genuine advance

A genuine advance is one or more of:

- a **certified pipeline** that reproduces a named SOTA non-coding variant-effect result on the frozen, leakage-safe split, with the leakage protocol documented and independently runnable;
- a **new held-out SOTA** on a pre-registered split for a defined element class or variant type (enhancer-effect regression, splice-adjacent non-coding, structural-variant dosage effect), reported with calibration, ancestry stratification, and a benchmark-integrity statement;
- a **method contribution** that measurably narrows the correlational-vs-causal gap - predictions that hold under fine-mapping / LD-controlled evaluation rather than tagging LD structure - or that closes part of the *enhancer-effect gap* (models predict chromatin/binding tracks well but predict allelic expression change poorly);
- a **ranked, calibrated, falsifiable prediction set** of candidate causal non-coding/structural variants with molecular-effect hypotheses, formatted for a wet-lab or clinical partner to test.

**Not accepted as resolution.**

- A leaderboard number presented as a real-world or clinical guarantee.
- A variant "validated" only in silico, or by agreement with another predictor.
- A pathogenicity call issued as a determination rather than a hypothesis.
- A correlational eQTL/GWAS colocalization reported as an established causal mechanism.
- Any metric obtained on a split that leaks via LD, shared elements, or homologous sequence.
- A model that predicts epigenomic tracks accurately but is silently scored as if that established variant *effect* on expression.

## 4. Graded targets

**P0 - Frozen, hashed corpus and split.** Assemble the anchor label sets and commit the leakage-safe split with a documented provenance manifest before any model touches the data.
*Evidence:* SHA-256 manifest, versioned accessions, a written split rationale.

**P1 - Reproduce SOTA on the frozen split.** Rebuild a public non-coding scorer (an Enformer/Borzoi-derived variant-effect pipeline, CADD, or a genomic foundation-model scorer) with our own verified code and match its reported metric on the committed leakage-safe split.
*Evidence:* reproducible metrics, hashed split, side-by-side with the published number.

**P2 - Calibrated molecular-effect regression.** On held-out MPRA/eQTL, predict allelic molecular effects with calibrated uncertainty; report Spearman by element class and calibration error.
*Evidence:* reliability curves on held-out data; ablation showing the split is not leaking.

**P3 - Certified method / new held-out SOTA.** Beat the reproduced baseline on a pre-registered split for at least one element class or the structural-variant case, with a documented LD/fine-mapping-controlled evaluation that addresses the causal-vs-correlational confound.
*Evidence:* full benchmark-integrity statement; ancestry-stratified results; causal-controlled metric reported alongside the permissive one.

**P4 - Falsifiable prediction set for a partner.** A ranked, calibrated list of candidate causal non-coding/structural variants with explicit molecular-effect hypotheses and the specific assay that would refute each.
*Evidence:* the list, its calibration on prior held-out data, and a pre-registered success criterion. Every entry labeled a wet-lab-pending hypothesis.

## 5. Known results and prior art

- **Enformer** (Avsec et al., ~2021) - sequence-to-function transformer, ~200 kb receptive field, predicts CAGE/DNase/ChIP; widely used for variant-effect scoring by contrasting ref vs alt predictions.
- **Borzoi** (Linder et al., Calico, ~2023–2024 - verify) - extends the Enformer approach to RNA-seq coverage, improving expression- and splicing-adjacent effect prediction.
- **AlphaMissense** (Cheng et al., ~2023) - coding missense pathogenicity; lineage marker for how far *coding* interpretation has moved, and the contrast that defines this problem.
- **CADD** (Kircher et al., ~2014; Rentzsch et al. updates) - integrative deleteriousness annotation across coding and non-coding.
- **DeepSEA / Sei** (Zhou & Troyanskaya ~2015; Chen et al. ~2022) - chromatin-effect prediction from sequence; Sei adds sequence-class organization.
- **Genomic foundation models** - GPN and GPN-MSA (Benegas et al., ~2023–2024) for variant effect from unsupervised sequence modeling; DNABERT / Nucleotide Transformer families; Evo (verify) for long-range genomic modeling. Names and capabilities move fast - verify each.
- **Saturation-mutagenesis MPRA** (Kircher et al., ~2019 - verify accession) as a near-causal regulatory readout; gnomAD non-coding constraint (Chen et al. - verify) as a population-level orthogonal signal.
- **Fine-mapping** - SuSiE, DAP-G, FINEMAP - the standard tools for separating causal from LD-tagging QTL variants; essential to any honest causal claim here.

**Status as of mid-2026 - re-verify against current literature before starting any session.** This subfield reframes "solved" quickly; confirm current model names, releases, and benchmark splits before committing.

## 6. Attack plan

Concrete first steps, in order:

1. **Assemble the frozen corpus.** Pull GTEx fine-mapped eQTL credible sets and a saturation-mutagenesis MPRA corpus as the two anchor label sets; ClinVar (filtered by review status) and gnomAD SV as clinical/structural labels; ENCODE tracks as feature context only. Record every version and accession.
2. **Construct the leakage-safe split.** Commit chromosome-, LD-block-, and element-level holdouts before modeling; hash the split manifest. Build an explicit LD/fine-mapping-controlled evaluation so a "win" cannot be LD tagging.
3. **Reproduce a baseline.** Reimplement an Enformer/Borzoi-derived ref-vs-alt scorer in PyTorch and reproduce its reported metric on the committed split before attempting any improvement.
4. **Model the contribution.** Try a foundation-model embedding plus a calibrated head, or a fine-tuned track model - always scored on molecular *effect*, not track reconstruction, and always stratified by ancestry and element class.
5. **Calibrate.** Fit temperature scaling / isotonic regression on held-out data and report the calibration itself (reliability curves, ECE), not just point metrics.
6. **Negative controls.** Include allele-frequency-matched neutral variants, label-shuffled runs, and a "predict track then score effect" ablation to expose the enhancer-effect gap.

**One-GPU scope.** Enformer/Borzoi-class *training* exceeds a single prosumer GPU - flag this: use released weights for inference/embedding and restrict on-GPU work to head training, fine-tuning, and evaluation.

**Failure modes to expect and report:**

- LD leakage inflating eQTL metrics when the split cuts by variant rather than by locus;
- the enhancer-effect gap - good epigenomic-track prediction, poor allelic expression-effect prediction;
- label noise in single-submitter ClinVar entries and in low-power eQTL calls;
- ancestry distribution shift between training labels and the target population;
- structural-variant sparsity and breakpoint imprecision, which starve the SV models;
- silent scoring of track reconstruction as if it were variant effect.

State each explicitly where it bites, and quantify its impact where the negative controls allow.

## 7. Verification and auditability requirements

1. **Leakage-safe evaluation.** Chromosome-, LD-block-, and element-level holdouts committed and hashed before any evaluation; no test-set tuning; the LD/fine-mapping control documented so no metric can be inflated by tagging.
2. **Calibrated uncertainty.** Every prospective molecular-effect and pathogenicity prediction carries a calibrated confidence; calibration reported on held-out data with reliability curves and ECE.
3. **Ancestry and population fairness.** All metrics stratified by ancestry group; portability gaps reported, never averaged away; label-distribution bias (European-ancestry-heavy ClinVar/MPRA) stated as a limitation.
4. **Causal-vs-correlational honesty.** Every causal molecular-effect claim marked as fine-mapping-controlled or explicitly flagged as correlational; colocalization never reported as established mechanism.
5. **Independent reproduction.** Metrics reproducible from the committed split and code by a separate script; SHA-256 manifest over data version hashes, code, and predictions.
6. **Preservation.** Model weights or weight provenance, training/inference code, and dataset version hashes are part of the record; anything not preserved is stated explicitly.
7. **Honest reporting.** The report states up front that the problem is reality-gated and NOT resolved; separates in-silico metrics from any experimental validation; labels every variant call a wet-lab- or clinic-pending hypothesis; and never presents a benchmark number as a clinical or real-world guarantee.
