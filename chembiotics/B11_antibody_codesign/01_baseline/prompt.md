# PROMPT FOR ANTIBODY STRUCTURE, DEVELOPABILITY, AND AFFINITY CO-PREDICTION

## The CDR-H3 loop and the multi-objective antibody gap in the AlphaFold3 era

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** B - reality-gated (empirical verifier)
**Rank:** B-11 of 29
**Source:** chem/bio top-50 list #46, section G (higher-order / adjacent)
**Modes:** `[struct]` `[gen]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Antibodies are the workhorse of modern therapeutics, and their design is a distinctive prediction problem that general structure models handle only partly. The variable-domain framework is easy; the antigen-binding paratope is dominated by the **CDR-H3 loop**, which is hypervariable in length and sequence, has no germline template, and adopts diverse conformations that AlphaFold-Multimer and even AlphaFold3 still model unreliably. Worse, a usable therapeutic must satisfy *three coupled objectives at once* - correct **structure** (paratope geometry), sufficient **affinity** for the target, and acceptable **developability** (expression, thermostability, low aggregation/self-association, low viscosity, absence of PTM/polyspecificity liabilities). Optimizing one often degrades another. This is **reality-gated**: affinity is defined by an SPR/BLI measurement and developability by expression and biophysical assays, and those measurements - not any predictor - are ground truth. Structure models (IgFold, ImmuneBuilder, AF-Multimer) and biophysical profilers (TAP) advance the in-silico numbers; they cannot certify that a designed antibody will bind and behave. The honest deliverable is a certified method on the CDR-H3 and multi-objective tasks, a held-out benchmark on a leakage-safe split, and a ranked, calibrated design/prediction slate for a wet-lab partner to express and assay.

## 1. Exact problem statement

**Structure sub-problem.**
- *Input:* antibody VH/VL sequences (optionally the antigen sequence/structure for the complex).
- *Output:* a full-atom Fv (or Fab) model with **calibrated per-region confidence**, and - where antigen is given - a docked complex with paratope/epitope.
- *Metric:* **CDR-H3 backbone RMSD** (the headline), framework and other-CDR RMSD, VH–VL orientation error (OCD, orientational coordinate distance), and - for complexes - DockQ / paratope accuracy. Report the CDR-H3 RMSD *distribution*, not just the mean, stratified by loop length.

**Affinity sub-problem.**
- *Input:* antibody (and mutational variants) against a fixed antigen.
- *Output:* predicted binding affinity / ranking, with calibrated uncertainty.
- *Metric:* Spearman/Pearson correlation with measured $K_D$ (or $\Delta\Delta G$ of binding) on mutational and cross-clone series; ranking quality (NDCG) for affinity maturation.

**Developability sub-problem.**
- *Input:* antibody sequence/structure.
- *Output:* predicted developability readouts / flags (thermostability $T_m$, aggregation/self-association, viscosity, expression titer, PTM and polyspecificity liabilities), with calibrated uncertainty.
- *Metric:* correlation/AUROC against measured assay readouts (HIC retention, AC-SINS, DSF $T_m$, SEC aggregation, titer).

**Co-prediction (the actual target).** A single model or coupled pipeline producing all three, with a **joint** evaluation: on a Pareto-style panel, does the method identify variants that are simultaneously high-affinity, well-folded, and developable - the property that isolated single-objective scores miss?

**Population.** Non-redundant antibodies clustered by CDR-H3, stratified by loop length and by therapeutic vs. natural origin; affinity/developability panels named explicitly.

**Compute-tractable sub-question.** On frozen, CDR-H3-clustered, time-separated splits: beat a named baseline on CDR-H3 RMSD, on affinity-ranking correlation, and on developability AUROC, each with calibrated uncertainty.

**Empirically-gated whole.** A designed or selected antibody's *actual* affinity and developability - established only by expression and SPR/BLI/aggregation assays, never by any score.

## 2. Verifier and data

**Ground-truth source.**
- **SAbDab** (Structural Antibody Database; Dunbar, Deane et al.) and **Thera-SAbDab** - antibody/nanobody structures and therapeutic antibodies; the structural truth and CDR-H3 source.
- **OAS** (Observed Antibody Space; Kovaltsuk, Deane et al.) - massive natural antibody *sequence* repertoire (context/pretraining, not 3D truth).
- **Affinity:** **AB-Bind** (Sirin, Klein et al., ~2016) - antibody–antigen binding mutants with measured $\Delta\Delta G$; the antibody subset of **SKEMPI** (Moal & Fernández-Recio); and per-campaign SPR/BLI datasets (verify curated public sets; many are proprietary).
- **Developability:** curated therapeutic-antibody developability panels (e.g. the Jain et al. ~2017 biophysical panel of clinical-stage antibodies; verify) and the **TAP** (Therapeutic Antibody Profiler; Raybould, Deane ~2019) reference flags. Most developability assay data is proprietary - a named public panel is required and its limits stated.

**Frozen split (leakage-safe).** Structure test set fixed before modeling by **CDR-H3 clustering** (no test antibody sharing a CDR-H3 cluster - by length and sequence identity - with training) intersected with a **time split** (deposition/approval-date cutoff). Affinity and developability panels are split by antibody/target cluster so no test clone is homologous to a training clone; mutational series are split by *parent* antibody, not by individual mutant, to prevent trivial leakage. All cluster, split, and panel manifests are committed and hashed before any test number. Antibody benchmarks leak severely through germline and CDR-H3 similarity; the clustering is mandatory.

**Wet-lab gate (mandatory).** Affinity and developability **cannot be established in silico**. Affinity requires surface plasmon resonance (SPR) or bio-layer interferometry (BLI) - and first, expression of the antibody. Developability requires expression titer measurement, DSF/nanoDSF for $T_m$, SEC/DLS for aggregation, HIC and AC-SINS for hydrophobicity/self-association, and polyspecificity/PTM assays. A realistic per-panel campaign (express and profile tens to low-hundreds of variants) is many weeks to months and, in effort terms, roughly \$50k–\$300k, before any binding is confirmed. A model's predicted $K_D$, TAP flags, or structure confidence is a hypothesis, not a measurement. This gate is not softenable.

## 3. Standard of a genuine advance

A genuine advance is one of:
1. A **certified method contribution** - a new held-out SOTA on CDR-H3 RMSD (especially long loops), and/or on affinity-ranking correlation, and/or on developability AUROC, at matched compute, with calibrated uncertainty validated on held-out data; ideally a **joint** improvement that surfaces simultaneously-good variants a single-objective method misses.
2. A **falsifiable, ranked design/prediction slate** - designed or selected antibody variants with predicted structure, affinity rank, and developability profile, each with calibrated confidence, registered before expression and assay, ready for a wet-lab partner.

**Not accepted as resolution:**
- A **leaderboard CDR-H3 RMSD or affinity correlation treated as a guarantee** that a designed antibody will bind or be developable.
- **In-silico "validation"** - low predicted energy, good TAP flags, agreement between structure predictors, or docking scores are hypotheses, not confirmation.
- A **corpus-overfit metric** - accuracy driven by germline/CDR-H3 memorization; affinity correlation inflated by mutant-level leakage within a parent series; developability AUROC on a panel too small or too homogeneous to generalize.
- Optimizing one objective while silently degrading another - a high-affinity design that will not express, or a developable antibody that does not bind, is not a co-prediction success.

## 4. Graded targets

**P1 - Reproduce baselines.** Run IgFold / ImmuneBuilder (ABodyBuilder2) / AF-Multimer for structure, a TAP-style developability profiler, and an affinity baseline on the frozen splits; reproduce reported CDR-H3 RMSD, affinity correlation, and developability metrics within tolerance. *Evidence:* committed split/cluster hashes, independent scorers, CDR-H3-length-stratified tables.

**P2 - Calibrated uncertainty.** Validate structure confidence as a predictor of realized CDR-H3 RMSD, and affinity/developability uncertainty against realized error, on held-out data. *Evidence:* reliability curves, expected calibration error, per stratum.

**P3 - Certified method contribution.** A modeling change - CDR-H3-specific loop modeling/refinement, an antibody language-model prior, a coupled multi-objective head - that significantly improves CDR-H3 RMSD, affinity ranking, or developability on held-out clusters over P1. *Evidence:* paired per-antibody deltas with confidence intervals, ablations, no test-set tuning.

**P4 - New held-out SOTA / multi-objective.** Best-in-class on the committed splits, with a demonstrated **joint** benefit (Pareto front of affinity × developability × structure quality better than single-objective baselines), at one-GPU-feasible inference. *Evidence:* full CDFs, Pareto analyses, split manifests, independent reproduction.

**P5 - Wet-lab-ready design/prediction slate.** A ranked, calibrated set of antibody variants (predicted structure + affinity rank + developability profile), registered before expression/assay, with pre-committed falsifiable claims (e.g. "$\ge k$ of top $n$ bind at $K_D <$ threshold and pass developability flags"), and honest post-hoc accounting including the failures. The machine's ceiling; SPR/BLI and the aggregation assays close the loop.

## 5. Known results and prior art

- **IgFold** - Ruffolo & Gray (2023, Nat. Commun.) - fast antibody structure prediction with an antibody language model; strong framework, CDR-H3 still the hard region.
- **DeepAb / ABlooper / ImmuneBuilder (ABodyBuilder2)** - Ruffolo & Gray (~2022); Abanades, Deane et al. (~2022–2023) - antibody structure and CDR-loop modeling with per-residue uncertainty; CDR-H3 remains the accuracy bottleneck.
- **AlphaFold-Multimer / AlphaFold3** - Evans et al. (~2022); Abramson et al. (2024) - antibody–antigen complexes; CDR-H3 and epitope specificity remain unreliable - **re-verify on our CDR-H3-clustered split.**
- **SAbDab / Thera-SAbDab / OAS** - Dunbar, Kovaltsuk, Deane et al. (from ~2014) - the structural and repertoire data foundation.
- **TAP (Therapeutic Antibody Profiler)** - Raybould, Deane et al. (~2019) - structure-based developability flags; the developability baseline.
- **AB-Bind** - Sirin, Klein et al. (~2016) - antibody–antigen $\Delta\Delta G$ mutational data; the affinity anchor (with SKEMPI's antibody subset).
- **Developability panels** - Jain et al. (~2017) biophysical profiling of clinical-stage antibodies (verify) - a rare public multi-assay reference.
- **Generative antibody design** - diffusion/inverse-folding for CDRs (e.g. antibody-specific RFdiffusion/ProteinMPNN adaptations, dyMEAN, and related; verify) - the `[gen]` side, whose outputs are hypotheses pending expression and assay.

*Status as of mid-2026 - re-verify against current literature before starting any session.* Check whether any model reliably predicts CDR-H3 conformation on a leakage-safe split, and whether joint affinity+developability co-prediction has a validated public benchmark; both remain open.

## 6. Attack plan

**Data.** Pull antibody structures from SAbDab; cluster by CDR-H3 (length + identity); commit a CDR-H3-cluster ∩ time split. Assemble AB-Bind/SKEMPI affinity series (split by parent) and a named public developability panel (split by clone). Use OAS for antibody-LM pretraining only. Freeze and hash before modeling.

**Baselines.** IgFold, ImmuneBuilder, AF-Multimer/AF3 (structure); TAP (developability); a sequence/structure affinity baseline. Score CDR-H3 RMSD, OCD, DockQ, affinity correlation, developability AUROC with independent scorers.

**Model.** Candidate contributions: (i) **CDR-H3-focused** loop generation + physics refinement with calibrated per-residue uncertainty; (ii) an **antibody language-model** prior conditioning structure and property heads; (iii) a **coupled multi-objective** model sharing a representation across structure, affinity, and developability so the Pareto trade-off is explicit; (iv) `[gen]` CDR design (inverse folding / diffusion) filtered by the co-predictor. Rank designs by a calibrated multi-objective acquisition score.

**Calibration.** Validate structure confidence vs. realized CDR-H3 RMSD and property uncertainty vs. realized error on held-out clusters; report expected calibration error per stratum.

**Compute.** IgFold/ImmuneBuilder-class inference, antibody-LM fine-tuning, and property heads are one-prosumer-GPU feasible; AF3-scale complex prediction is the heavier step. The bottleneck is measured affinity/developability data, not compute.

**Failure modes.** (i) **CDR-H3 hardness** - no template, high variability; the persistent structural gap. (ii) **Data scarcity + proprietary data** - most affinity/developability data is private; public panels are small. (iii) **Leakage** - germline/CDR-H3 and mutant-level leakage inflate every number; cluster and parent-level splits are mandatory. (iv) **Objective conflict** - improving affinity can worsen developability; single-objective wins mislead. (v) **Distribution shift** - designed antibodies leave the natural distribution the model was trained on.

## 7. Verification and auditability requirements

1. **Leakage-safe evaluation.** CDR-H3 clustering plus time separation for structure; antibody/target-cluster and parent-level separation for affinity/developability; all committed and hashed before evaluation; no test-set tuning; CDR-H3-length and origin strata reported.
2. **Calibrated uncertainty.** Every structure, affinity, and developability prediction carries calibrated uncertainty; calibration (reliability curves, expected calibration error) is reported on held-out clusters.
3. **Independent reproduction.** CDR-H3 RMSD, OCD, DockQ, affinity correlation, and developability AUROC are recomputed by standalone scorers separate from training code, from committed splits and predictions.
4. **Cryptographic manifest.** A SHA-256 manifest covers split/cluster definitions, affinity/developability panel versions, data hashes, model code, weights, and every predicted structure, affinity, and profile.
5. **Preservation.** Training/fine-tuning and design code, weights, refinement and acquisition configuration, and dataset version hashes are part of the record; anything not preserved is stated explicitly.
6. **Prospective-prediction registry.** Any design/prediction slate (P5) is timestamped and registered - structure, affinity rank, developability profile, confidence, pre-committed claims - before expression and assay, and scored afterward including the failures.
7. **Honest reporting.** The report states up front that antibody affinity and developability are reality-gated and **not resolved**; separates in-silico metrics (CDR-H3 RMSD, TAP flags, predicted $K_D$) from measured affinity/developability; labels every designed or predicted antibody a wet-lab-pending hypothesis; flags any objective improved at another's expense; and never presents a benchmark number as a guarantee that an antibody will bind or be developable.
