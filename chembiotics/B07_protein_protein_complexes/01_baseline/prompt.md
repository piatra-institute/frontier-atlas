# PROMPT FOR PROTEIN–PROTEIN COMPLEX AND INTERACTION-NETWORK PREDICTION

## Complex structure and the interactome at proteome scale, including the weak and transient

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** B - reality-gated (empirical verifier)
**Rank:** B-07 of 29
**Source:** chem/bio top-50 list #19, section C (beyond static structure)
**Modes:** `[struct]` `[data]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Cells run on protein–protein interactions, most of which have no solved complex structure and many of which are weak, transient, or condition-dependent. The task has two coupled faces: (i) **structural** - given two (or more) chains that do interact, predict the bound complex geometry; and (ii) **network** - given a proteome, predict *which* pairs interact at all, including low-affinity and transient encounters that stable co-crystallization misses. AlphaFold-Multimer and AlphaFold3 transformed the first face for stable, evolutionarily coupled heterodimers, yet they degrade on antibody–antigen, weak/transient, and folding-upon-binding interfaces, and they do not by themselves answer the binary yes/no of the interactome. Both faces are **reality-gated**: the ground truth is an experimental complex structure (crystallography, cryo-EM) or an experimentally measured interaction (co-IP, crosslinking-MS, two-hybrid, affinity assay), and both corpora are sparse, biased toward the stable, and expensive to extend. Compute can produce a certified method and a ranked, calibrated interaction/complex hypothesis set; it cannot certify that two proteins interact in a living cell. The honest deliverable is a held-out SOTA on a leakage-safe structural split, calibrated interactome predictions, and a falsifiable slate for a wet-lab partner - never a claim that the interactome is "mapped."

## 1. Exact problem statement

**Structural sub-problem.**
- *Input:* the sequences (and optionally MSAs / paired MSAs) of $k\ge 2$ chains known to form a complex; stoichiometry may be given or inferred.
- *Output:* a ranked set of full-atom complex models with per-interface and per-residue **calibrated confidence** (interface-PAE / ipTM analogues).
- *Metric:* **DockQ** $\in[0,1]$ combining native-contact recovery $f_\mathrm{nat}$, interface RMSD, and ligand RMSD,
$$\mathrm{DockQ} = \tfrac{1}{3}\big(f_\mathrm{nat} + \tfrac{1}{1+(\mathrm{iRMSD}/1.5)^2} + \tfrac{1}{1+(\mathrm{lRMSD}/8.5)^2}\big),$$
mapped to the **CAPRI** tiers (incorrect / acceptable / medium / high). Report the fraction of targets at $\ge$ acceptable and $\ge$ medium.

**Network sub-problem.**
- *Input:* a set of candidate protein pairs from a proteome (with sequences, and optional context: co-expression, localization, homology to known interfaces).
- *Output:* a calibrated probability $p_{ij}$ that pair $(i,j)$ physically interacts, and - where predicted positive - a complex model with confidence.
- *Metric:* precision–recall / AUPRC against a held-out set of experimentally supported interactions and, critically, against a **matched negative set** (the hardest and most abused part: random pairs are trivially separable; the meaningful negatives are co-localized, co-expressed non-interactors). Report AUPRC at fixed recall on the hard-negative population.

**Population.** Structural performance is claimed over non-redundant heteromeric complexes, stratified by:
- **interface novelty** - test interfaces absent from vs. present in training;
- **interface type** - obligate / transient / antibody–antigen / peptide-motif, which behave very differently;
- **coupling depth** - paired-MSA availability, the strongest predictor of success.

Network performance is claimed over a named proteome (e.g. human) with an explicitly defined, non-trivial negative population; the negative construction is part of the specification, not an afterthought.

**Compute-tractable sub-question.** On a frozen, homology- and time-separated structural split, meet or beat a named SOTA DockQ CDF with calibrated interface confidence; and on a frozen interactome split, beat a sequence/co-evolution baseline in AUPRC against hard negatives.

**Empirically-gated whole.** Establish that two proteins *actually* interact in the cell, in what geometry, and with what affinity/lifetime - provable only by new physical experiment, not by any predictor's score.

## 2. Verifier and data

**Ground-truth source.**
- **PDB** - experimentally determined complexes (crystallography, cryo-EM); the structural truth.
- **Docking Benchmark 5 / 5.5 (DB5.5)** (Vreven, Weng et al.; verify version) - the standard bound/unbound docking benchmark with difficulty tiers (rigid / medium / difficult).
- **CAPRI** (Critical Assessment of PRedicted Interactions; Janin, Wodak, Lensink et al.) - blind community assessment; the leakage-free structural gold standard.
- **Interactome corpora:** **HuRI** (Human Reference Interactome, Luck et al. 2020, Y2H binary), **IntAct**, **BioGRID**, **STRING** (mixed evidence/inferred - use only direct-experimental subsets as truth), **CORUM** (curated complexes), **hu.MAP** (AP-MS complexes; verify).
- **Integrative / crosslinking-MS restraints** - XL-MS datasets and the PDB-Dev / PDB-IHM archive of integrative structures (Sali, Rappsilber and collaborators; verify archive name).
- **Affinity:** **SKEMPI** (mutational $\Delta\Delta G$ of binding; Moal & Fernández-Recio) and **PDBbind** protein–protein subset (verify) for the quantitative face.

**Frozen split (leakage-safe).** Structural test set fixed before modeling under **interface/fold clustering** (no test complex sharing an interface homolog - chain pairs clustered by sequence identity and by SCOP/ECOD fold of both partners) **and** a **time split** (deposition-date cutoff, CAPRI-style). Paired-MSA availability is a stratum, not a hidden confound. For the network task, negatives are drawn from the co-localized/co-expressed hard-negative population and the split is by protein *cluster* (no test protein homologous to a training protein), because interactome benchmarks leak badly through paralogs and through degree bias (hub proteins). All split, cluster, and negative-set manifests are committed and hashed before any test number.

**Corpus biases and leakage traps to guard against:**
- **Stable-complex bias** - the PDB is dominated by obligate, crystallizable complexes; transient and weak interactions, the open frontier, are under-represented in the truth set.
- **Interface-homolog leakage** - a test complex whose interface has a training homolog is a memorized answer; cluster on the interface and on both partners' folds, not just sequence.
- **Paralog leakage (network)** - interactome benchmarks leak badly through paralogs sharing an interaction; split by protein cluster.
- **Degree/hub bias (network)** - a classifier can score well by memorizing hub proteins; report performance controlling for node degree.
- **Easy-negative inflation** - random protein pairs are trivially separable; only co-localized, co-expressed non-interactors are a meaningful negative population.
- **Evidence-channel confusion** - STRING/inferred edges are predictions, not measurements; use only direct-experimental interactions as truth.

**Wet-lab gate (mandatory).** No computation can establish that two proteins physically interact, in what geometry, or with what strength. Binary interaction requires co-immunoprecipitation, yeast/mammalian two-hybrid, affinity-purification MS, or proximity labeling; **geometry** requires crosslinking-MS restraints plus integrative modeling, cryo-EM, or crystallography of the complex; **affinity/kinetics** require SPR, BLI, or ITC. Weak and transient interactions are the expensive frontier: they resist co-crystallization and stable pulldown by their nature, needing crosslinking-MS, NMR, or fast-kinetics assays. Order-of-magnitude effort: a solved complex structure is months and \$50k–\$300k and frequently fails; a systematic binary interactome screen is a multi-year, multi-assay program. This gate is not softenable.

## 3. Standard of a genuine advance

A genuine advance is one of:
1. A **certified method contribution** - a new held-out SOTA on the frozen structural split (higher fraction at $\ge$ medium DockQ, at matched compute), demonstrably driven by a real modeling idea and holding on the hard strata (transient, antibody–antigen, shallow-MSA), with calibrated interface confidence validated on held-out data.
2. A **calibrated interactome contribution** - beating strong baselines in AUPRC against a hard-negative population, with probabilities calibrated on held-out data, and a demonstration that gains are not artifacts of degree/paralog leakage.
3. A **falsifiable, ranked prediction set** - complex models and/or novel interaction calls, registered before experimental testing, with pre-committed confidence and a stated accuracy claim, ready for a crosslinking-MS / cryo-EM / co-IP partner.

**Not accepted as resolution:**
- A **leaderboard DockQ or AUPRC treated as a guarantee** that a predicted interaction is real - a retrospective number is a hypothesis about prospective truth.
- **In-silico "validation"** - self-consistency of ipTM/PAE, agreement across predictors, or a docking-score consensus is not experimental confirmation.
- A **corpus-overfit metric** - high interactome AUPRC that collapses when negatives are hard, or high DockQ concentrated on obligate homolog-rich interfaces; hub-degree memorization; STRING's inferred edges scored as if experimental.
- Confident complex geometry for a pair that does not actually interact - a plausible model of a non-interaction is a false positive, not a success.

## 4. Graded targets

**P1 - Reproduce a SOTA baseline.** Run AlphaFold-Multimer and (where feasible) AlphaFold3 on the frozen structural split; reproduce reported DockQ/CAPRI-tier statistics within tolerance. Reproduce a co-evolution / sequence baseline on the frozen interactome split. *Evidence:* committed split + negative-set hashes, an independent DockQ scorer, per-stratum tables.

**P2 - Calibrated confidence.** Validate interface-confidence (ipTM/PAE-analogue) as a predictor of realized DockQ, and interactome probabilities against realized precision, on held-out data. *Evidence:* reliability curves and expected calibration error per stratum, including hard negatives.

**P3 - Certified method contribution.** A modeling change - paired-MSA construction, transient-interface-aware training, integration of XL-MS restraints, or a hard-negative-aware interactome model - that yields a significant, leakage-audited improvement on the hard strata. *Evidence:* paired per-target deltas with confidence intervals, ablations, no test-set tuning.

**P4 - New held-out SOTA.** Best-in-class fraction at $\ge$ medium DockQ on the committed structural split *including* transient/antibody/shallow-MSA strata, and/or best AUPRC-at-hard-negatives on the interactome split, at one-GPU-feasible inference. *Evidence:* full CDFs / PR curves, split manifests, independent reproduction.

**P5 - Wet-lab-ready prediction set.** A ranked, calibrated slate of (a) complex models for interactions under active structural determination and/or (b) novel binary-interaction calls for co-IP/XL-MS testing, registered before results, with a pre-committed falsifiable accuracy claim and honest post-hoc scoring including misses. The machine's ceiling; the assay closes the loop.

## 5. Known results and prior art

- **AlphaFold-Multimer** - Evans, Jumper et al. (~2021–2022), extension of AlphaFold2 to complexes; strong on stable heterodimers, weaker on transient/antibody interfaces.
- **AlphaFold3** - Abramson, Jumper et al. (2024, Nature), unified biomolecular complexes; improved but with residual weakness on antibody–antigen and weak interfaces - **re-verify on our leakage-safe split**.
- **DockQ** - Basu & Wallner (2016), the standard single-number complex-quality metric; **CAPRI** - Janin, Wodak, Lensink et al. (long-running), the blind assessment.
- **Docking Benchmark 5 / 5.5** - Vreven, Weng et al. (~2015), bound/unbound docking benchmark with difficulty tiers.
- **HuRI** - Luck, Vidal et al. (2020, Nature), systematic human binary interactome by Y2H; the network-scale reference and a lesson in coverage limits.
- **Integrative / crosslinking-MS modeling** - Sali and collaborators (Integrative Modeling Platform, IMP) and Rappsilber (XL-MS); PDB-IHM/PDB-Dev archive of integrative structures (verify).
- **SKEMPI** - Moal & Fernández-Recio (~2012, updated), mutational binding-affinity changes; the quantitative-affinity anchor.
- **Classical docking** - ClusPro (Vajda/Kozakov), HADDOCK (Bonvin, data-driven/restraint docking), ZDOCK/pyDock - baselines and restraint-integration frameworks.
- **Weak/transient interactions** - remain an open, actively studied hard case; encounter complexes and fuzzy/condition-dependent binding are poorly captured by single-structure predictors.

*Status as of mid-2026 - re-verify against current literature before starting any session.* Check whether AlphaFold3-class models have closed the transient/antibody gap on a genuinely leakage-safe split, and the current state of interactome-scale structural screens.

## 6. Attack plan

**Data.** Assemble complexes from the PDB; cluster by interface and by fold of both partners; commit an interface-cluster ∩ time split. Build the interactome task from HuRI/IntAct/CORUM direct-experimental edges with a **hard-negative** population (co-localized, co-expressed non-interactors) and a protein-cluster split. Freeze and hash everything before modeling.

**Baselines.** AlphaFold-Multimer, AlphaFold3 (as runnable), ClusPro/HADDOCK for restraint docking, and a co-evolution/paired-MSA interactome baseline. Score DockQ with an independent scorer; score the network with a standalone PR/AUPRC script.

**Model.** Candidate contributions:
- improved **paired-MSA / species-pairing** to strengthen the co-evolution signal for both structure and network tasks;
- **transient- and antibody-interface-aware** fine-tuning targeting the strata general models fail on;
- **XL-MS-restraint integration** into a deep predictor (integrative deep modeling), coupling sparse experimental restraints to learned priors;
- a **hard-negative-aware interactome classifier** that consumes structural-model confidence (ipTM/PAE) as a feature.

Generate ensembles and rerank with interface-confidence plus restraint satisfaction.

**Calibration.** Validate ipTM/PAE-analogues against realized DockQ and interactome probabilities against realized precision; temperature/isotonic scaling per stratum; report expected calibration error.

**Compute.** Inference and fine-tuning of open Multimer-class models are one-GPU feasible; large paired-MSA generation is the heavier step. The bottleneck is data and negatives, not FLOPs.

**Failure modes.** (i) **Data scarcity / bias** - the corpus is dominated by stable, crystallizable complexes; transient interactions are under-sampled. (ii) **Distribution shift** - prospective proteome pairs differ from the crystallized mass. (iii) **Leakage** - paralog and hub-degree leakage inflate interactome AUPRC; interface-homolog leakage inflates DockQ; strict clustering is mandatory. (iv) **Negative-set gaming** - easy negatives make any model look good; the hard-negative population is the real test. (v) **Ensemble/condition dependence** - some interactions exist only under specific PTM/condition states a single model cannot represent.

## 7. Verification and auditability requirements

1. **Leakage-safe evaluation.** Structural split committed and hashed before evaluation under interface/fold clustering **and** time separation; interactome split by protein cluster with a committed hard-negative population; paired-MSA availability reported as a stratum; no test-set tuning.
2. **Calibrated uncertainty.** Every complex model carries a calibrated interface confidence and every interaction call a calibrated probability; calibration (reliability curves, expected calibration error) is reported on held-out data, per stratum and against hard negatives.
3. **Independent reproduction.** DockQ/CAPRI tiers and AUPRC/PR are recomputed by standalone scorers separate from training code, from committed splits, negatives, and predictions.
4. **Cryptographic manifest.** A SHA-256 manifest covers split definitions, the hard-negative set, data version hashes, model code, weights, and every predicted structure and probability.
5. **Preservation.** Training/fine-tuning code, weights, MSA-pairing pipeline, restraint-integration configuration, and dataset version hashes are part of the record; anything not preserved is stated explicitly.
6. **Prospective-prediction registry.** Any blind complex model or novel interaction call (P5) is timestamped and registered with its ranking, confidence, and pre-committed accuracy claim before experimental results, and scored afterward including misses.
7. **Honest reporting.** The report states up front that complex and interactome prediction are reality-gated and **not resolved**; separates in-silico metrics from experimental confirmation; labels every predicted complex and interaction a wet-lab-pending hypothesis; and never presents a DockQ or AUPRC as a guarantee that an interaction is real.
