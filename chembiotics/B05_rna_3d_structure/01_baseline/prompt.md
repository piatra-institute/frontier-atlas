# PROMPT FOR DE NOVO RNA 3D STRUCTURE PREDICTION

## Native tertiary folds of RNA from sequence, under the data-scarcity ceiling

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** B - reality-gated (empirical verifier)
**Rank:** B-05 of 29
**Source:** chem/bio top-50 list #18, section C (beyond static structure)
**Modes:** `[struct]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Protein structure prediction crossed the usefulness threshold when the PDB grew dense enough to act as a verifier; RNA has not. RNA folds into tertiary architectures stabilized by non-canonical base pairs, coaxial stacking, kissing loops, pseudoknots, and a shell of ordered Mg²⁺ ions and water - and the experimental record that would train and test a predictor is roughly two orders of magnitude smaller than the protein PDB, dominated by a handful of families (tRNA, rRNA fragments, riboswitches, ribozymes). De novo RNA 3D structure prediction is the clearest candidate for the "next AlphaFold," and its central obstacle is not architecture but **data scarcity**: there is not enough independent, non-redundant experimental structure to either train a large model or to certify one without leakage. Deep methods (RoseTTAFoldNA, DeepFoldRNA, RhoFold, trRosettaRNA, AlphaFold3's nucleic-acid channel) advance the number; at CASP15 human expert and physics-based pipelines were still competitive with, and often ahead of, end-to-end learning. This problem is **reality-gated**: the ground truth is an experimental structure that must be physically determined (crystallography, cryo-EM, NMR). The honest deliverable is a certified method contribution, a held-out benchmark result on a leakage-safe split, and a ranked, calibrated set of blind predictions handed to a structural-biology partner - never a claim that RNA structure is "solved."

## 1. Exact problem statement

**Input.** An RNA sequence $s \in \{A,C,G,U\}^{L}$ of length $L$, optionally accompanied by (i) a multiple sequence alignment (homologous sequences from Rfam/RNAcentral), (ii) a predicted or experimentally probed secondary structure, and (iii) declared ionic conditions. The prompt fixes which auxiliary inputs a given target may use; MSA-free and MSA-provided tracks are scored separately because covariation is the single strongest signal and its availability is itself family-dependent.

**Output.** A ranked ensemble of full-atom (or at minimum P, C4′, N1/N9 backbone-plus-glycosidic) 3D coordinate models, each carrying a per-residue and per-interaction **calibrated confidence**, plus an explicit list of predicted tertiary contacts (base pairs, stacks, pseudoknot partners).

**Metrics.** For a predicted model $\hat{X}$ against native $X$:

- Root-mean-square deviation after optimal superposition,
$$\mathrm{RMSD}(\hat X, X) = \min_{R,t}\sqrt{\tfrac{1}{N}\sum_{i=1}^N \lVert R\hat x_i + t - x_i\rVert^2}.$$
- RNA-adapted TM-score with length-dependent $d_0$,
$$\mathrm{TM} = \frac{1}{N}\sum_{i=1}^N \frac{1}{1+(d_i/d_0(L))^2},\qquad d_0(L)=0.6\,(L-0.5)^{1/2}-2.5 \ \text{(verify constant)}.$$
- lDDT (superposition-free local distance difference test) over backbone atoms.
- **Interaction Network Fidelity** (INF): the Matthews correlation coefficient over the predicted vs. native set of base-pair and base-stacking interactions,
$$\mathrm{INF}=\frac{\mathrm{TP}\cdot\mathrm{TN}-\mathrm{FP}\cdot\mathrm{FN}}{\sqrt{(\mathrm{TP}+\mathrm{FP})(\mathrm{TP}+\mathrm{FN})(\mathrm{TN}+\mathrm{FP})(\mathrm{TN}+\mathrm{FN})}},$$
and the **deformation index** $\mathrm{DI}=\mathrm{RMSD}/\mathrm{INF}$.

Secondary metrics, reported alongside but never in place of the above:
- **clash score** (physical validity of the model);
- **Mg²⁺- / ion-site recovery** (fraction of resolved ordered ions placed near their native positions);
- **P-value** (RNA-Puzzles convention: probability that the achieved RMSD arises by chance for the given length), guarding against trivially good scores on short chains.

**Population.** Performance is claimed over a named, non-redundant population of natural RNA structural domains, stratified by:
- **size class** - $<50$, $50$–$120$, $>120$ nt;
- **family novelty** - test families absent from vs. present in training;
- **MSA depth** - covariation-rich vs. orphan RNAs;
- **motif content** - presence of pseudoknots, kissing loops, and multi-helix junctions, which carry the hardest tertiary signal.

A metric is meaningful only with its population and stratification attached; a single headline number is not.

**Compute-tractable sub-question (in-silico).** Given a frozen, homology- and time-separated training corpus, produce a predictor whose median backbone RMSD / TM / INF on the frozen held-out split meets or beats a named SOTA baseline, with calibrated confidence. This is bounded above by the corpus: the model can only be as good as the sparse, biased structures allow, and its held-out number is an estimate of retrospective skill, not of prospective correctness on a novel fold.

**Empirically-gated whole.** Predict the native tertiary fold of an RNA whose structure has *never* been experimentally determined, and have that prediction confirmed by a newly determined structure. No amount of compute closes this; only a new physical experiment does.

## 2. Verifier and data

**Ground-truth source.**
- **PDB** - all RNA-containing entries; the primary corpus of atomic-resolution truth.
- **RNAsolo** (verify) and **NAKB / Nucleic Acid Database (NDB)** - curated, cleaned RNA-only extractions of PDB with redundancy annotation.
- **RNA-Puzzles** - the community blind-prediction target set and its released natives (Cruz, Westhof, Das, Dokholyan and collaborators).
- **CASP15 / CASP16 RNA category** - blindly assessed targets and released coordinates; the gold standard for leakage-free evaluation because predictions are registered before the structure is public.
- **Rfam** - family alignments / covariation (MSA input, family labels for splitting).
- **BMRB** (NMR restraints/ensembles) and **EMDB** (cryo-EM maps) for non-crystallographic truth and ensemble targets.
- **bpRNA / RNAcentral** - secondary structure and sequence context (auxiliary input only, not 3D truth).

**Frozen split (leakage-safe).** The test set is fixed before modeling under a **two-axis separation**: (i) **time split** - train only on structures deposited on or before a committed cutoff date, test on later depositions, mirroring CASP blind conditions; and (ii) **family/structure clustering** - remove any test chain sharing an Rfam family, exceeding a sequence-identity threshold, or falling below a structural-distance threshold (US-align / RMSD clustering) to any training chain. Both filters are documented; the cluster and date manifests are committed with hashes before a single test-set number is computed. Because natural RNA is dominated by a few families, the split must report per-family and MSA-availability strata separately - an aggregate number is dominated by rRNA/tRNA and overstates de novo ability.

**Corpus biases and leakage traps to guard against:**
- **Family concentration** - a handful of families (rRNA fragments, tRNA, riboswitches, group I/II introns) dominate the PDB; an aggregate score is largely their score, not de novo ability.
- **Redundancy** - the same construct in multiple crystal forms, point mutants, and bound/unbound states inflate apparent test size; cluster before splitting.
- **Homology leakage** - a test chain with a training homolog is a memorized answer; sequence identity alone is insufficient, so cluster on structure (US-align) as well.
- **MSA leakage** - a deep Rfam alignment can carry the fold for a family seen in training; the MSA-free track is what exposes this.
- **Size/quality bias** - small hairpins and duplexes score well and mask failure on large multi-junction tertiary folds; filter by resolution and validation metrics and stratify by length.

**Wet-lab gate (mandatory).** A predicted structure for an RNA not already in the PDB **cannot be established as correct by any computation**. Confirmation requires new physical experiment: X-ray crystallography (needs a crystallizable construct - frequently unattainable for flexible or non-globular RNA; typically months of effort and a high failure rate, roughly \$50k–\$200k of effort per solved structure), single-particle cryo-EM (difficult below ~50–60 kDa, i.e. most single RNAs, and needs specialized fiducials/scaffolds), or solution NMR (practically limited to $\lesssim 50$ nt, weeks of instrument time). Chemical probing (SHAPE / DMS-MaPseq) and crosslinking constrain **secondary structure and accessibility only**, not the full tertiary coordinate set, and cannot serve as 3D ground truth. This gate is not softenable: the corpus is the bottleneck, and every prospective prediction is a hypothesis until a structure is solved.

## 3. Standard of a genuine advance

A genuine advance is one of:
1. A **certified method contribution** - a model or algorithm that achieves a *new held-out SOTA* on the frozen, family- and time-separated split (better median/CDF on TM, INF, and DI at matched compute), with the improvement shown to hold on the hardest stratum (novel families, MSA-poor, $>120$ nt), and with calibrated confidence that is itself validated on held-out data.
2. A **calibrated, falsifiable blind prediction set**: for a slate of RNAs whose structures are being determined by a partner (or the live CASP/RNA-Puzzles round), a ranked list of models with per-target confidence and explicit tertiary-contact calls, registered before the natives are released, with a pre-committed accuracy claim (e.g. "TM $\ge$ 0.45 on $\ge k$ of $n$ targets").

**Not accepted as resolution:**
- A **leaderboard or benchmark number treated as a real-world guarantee** - a good median TM on a retrospective split is a hypothesis about prospective performance, not proof of it.
- **In-silico-only "validation"** - agreement with a force field, a folding simulation, or a consensus of other predictors is not experimental confirmation and must never be labeled as such.
- A **corpus-overfit metric** - high scores driven by tRNA/rRNA/riboswitch redundancy, by MSA memorization of a family seen in training, or by test chains homologous to training chains under a lax split.
- A single lucky target, or cherry-picked best-of-ensemble numbers reported without the pre-committed ranking.
- A **backbone-only** or global-RMSD success reported while the base-pair/stacking network (INF) is wrong - the interaction network, not just the trace, is what makes an RNA model useful.
- "Solved RNA folding" claimed from any retrospective set - the field's cautionary tale is exactly the premature "solved" reframing.

A benchmark win here is a hypothesis about the next unsolved fold, not a result. It becomes a result only when a structure is determined and matches.

## 4. Graded targets

**P1 - Reproduce a SOTA baseline on our verified pipeline.** Re-run a published open model (RhoFold / DeepFoldRNA / RoseTTAFoldNA, and AlphaFold3's RNA channel where accessible) on our frozen, homology+time-separated split and reproduce reported TM/INF/DI within tolerance. *Evidence:* committed split hashes, an independent scoring script (US-align / RNA-Puzzles toolkit), per-stratum tables. Independently valuable as a trusted, leakage-audited baseline.

**P2 - Calibrated confidence.** Add and validate a per-residue / per-interaction confidence whose reliability curve is measured on held-out data (predicted confidence vs. realized lDDT/INF). *Evidence:* calibration plots and expected-calibration-error on the frozen split, per stratum.

**P3 - Certified method contribution.** A modeling change (physics-informed loss, ion/hydration modeling, MSA-free covariation surrogate, ensemble reranking) that yields a *statistically significant, leakage-audited* improvement over P1 on the hard strata. *Evidence:* paired per-target deltas with confidence intervals; ablation isolating the contribution; no test-set tuning.

**P4 - New held-out SOTA.** Best-in-class on the committed split across TM, INF, and DI simultaneously, including the MSA-poor and novel-family strata, at one-GPU-feasible inference. *Evidence:* full CDFs, the split manifest, an independent reproduction from committed code.

**P5 - Blind, wet-lab-ready prediction set.** A ranked, calibrated slate of models for RNAs under active experimental determination (partner targets or a live CASP16+/RNA-Puzzles round), registered before native release, with a pre-committed falsifiable accuracy claim and explicit contact predictions. *Evidence:* timestamped registration, post-hoc scoring against released natives, honest hit/miss accounting including the misses. This is the ceiling the machine can reach; closing the loop is the experiment's job.

**Cross-cutting evidence standard.** Every target above carries the same non-negotiables: metrics recomputed by an *independent* scorer from committed splits; results reported *per stratum* (size, family novelty, MSA depth, motif content), never as a single mean; calibrated confidence reported on held-out data; and, for any prospective claim, a timestamped registration predating native release. A number that cannot be reproduced from the committed manifest does not count.

## 5. Known results and prior art

- **RNA-Puzzles** - Cruz, Westhof, Das, Dokholyan et al. (from ~2012), the community blind-assessment consortium; established RMSD/INF/DI as the RNA metric vocabulary.
- **CASP15 RNA category** (2022 season, assessed 2023) - first inclusion of RNA in CASP; Das, Westhof, Kryshtafovych and the RNA assessors reported that human/physics pipelines (e.g. the Das lab's fragment-assembly and the Chen lab's methods) remained competitive with or ahead of deep-learning entries, underscoring the data ceiling.
- **RoseTTAFoldNA** - Baek, Baker et al. (~2023), joint protein–nucleic-acid modeling.
- **DeepFoldRNA** - Pearce, Zhang et al. (~2022–2023), end-to-end RNA structure from sequence/MSA.
- **RhoFold / RhoFold+** - Shen, Tao, Li and collaborators (~2022–2024), language-model-based RNA structure prediction.
- **trRosettaRNA** - Wang, Yang et al. (~2023), inter-residue geometry + Rosetta folding.
- **DRfold** - Li, Zhang et al. (verify), end-to-end differentiable RNA folding.
- **AlphaFold3** - Abramson, Jumper et al. (2024, Nature), a unified biomolecular model with a nucleic-acid channel; RNA accuracy is present but reported as modest relative to proteins, and is **to be independently re-verified on our leakage-safe split** before any comparison is trusted.
- **Physics / secondary-structure foundations** - FARFAR/FARFAR2 (Das lab), SimRNA (Bujnicki lab), Vfold (Chen lab), and covariation/secondary-structure tools (Rfam, R-scape, ViennaRNA) as inputs and baselines.

*Status as of mid-2026 - re-verify against current literature before starting any session.* RNA structure prediction is moving fast; check whether AlphaFold3-class models have measurably closed the gap on a genuinely leakage-safe split, and whether a new CASP round has shifted the frontier.

## 6. Attack plan

**Data.** Pull the RNA-only PDB via RNAsolo/NAKB; build the redundancy graph (sequence identity + structural clustering with US-align); commit a **time-split** (deposition-date cutoff) intersected with **family/cluster separation** (Rfam, identity, structure). Fetch Rfam alignments for the MSA track and hold an explicit MSA-free track. Freeze and hash all splits before modeling.

**Leakage-safe split protocol.** (1) Cluster all chains by structural similarity (US-align TM threshold) and by Rfam family; (2) assign whole clusters - never individual chains - to train or test; (3) additionally enforce a deposition-date cutoff so the test set post-dates all training; (4) record, for every test chain, its nearest training neighbour's identity and TM, and publish that leakage audit alongside results. Any test chain whose nearest training neighbour exceeds the identity/TM thresholds is dropped, not down-weighted.

**Baselines.** Reproduce RhoFold / DeepFoldRNA / RoseTTAFoldNA and, where runnable on one GPU, AlphaFold3's RNA channel. Score with the RNA-Puzzles toolkit + US-align in an **independent** script separate from any training code.

**Model.** Start from an open architecture (RhoFold-style RNA-LM + geometry head, or RoseTTAFoldNA-style track). Candidate contributions:
- explicit **Mg²⁺ / hydration** and ionic-condition conditioning, since ions make or break tertiary contacts;
- **non-canonical base-pair and pseudoknot/kissing-loop-aware losses** targeting the tertiary signal generic losses wash out;
- **MSA-free covariation surrogates** for orphan RNAs, where deep alignments do not exist;
- **ensemble generation + physics-based reranking** (FARFAR2 / SimRNA relaxation) to exploit the small-data regime where a learned prior plus a physical refiner beats either alone.

**Calibration.** Fit and validate confidence on held-out data (temperature scaling / isotonic on predicted-vs-realized lDDT and INF); report expected calibration error per stratum. Every prospective model carries calibrated per-interaction confidence.

**Compute.** Inference and moderate fine-tuning of an open RNA model are one-prosumer-GPU feasible; training a large model from scratch is not the point and is not the bottleneck - data is. Prefer fine-tuning + physics refinement over scaling.

**Failure modes.**
- **Data scarcity** - the dominant risk; too few independent families to train or certify, so improvements may not generalize.
- **Distribution shift** - natural test RNAs differ in size/family from the redundant training mass.
- **Leakage** - a test chain homologous to training under a lax split silently inflates every number; the two-axis split is non-negotiable.
- **Ensemble/flexibility** - many functional RNAs are conformationally heterogeneous; a single-structure metric misscores a correct ensemble, connecting this item to Boltzmann-weighted ensemble prediction.
- **Ion/water dependence** - Mg²⁺ and ordered water stabilize tertiary contacts a sequence-only model cannot see; ionic conditions must be an explicit input, not an averaged-away nuisance.
- **Metric gaming** - optimizing global RMSD/TM while getting the base-pair/stacking network (INF) wrong yields a plausible-looking, functionally meaningless model; report INF/DI alongside TM always.

## 7. Verification and auditability requirements

1. **Leakage-safe evaluation.** The train/test split is committed and hashed before any evaluation, under documented family-cluster **and** time separation; MSA-free and MSA-provided tracks are scored separately; there is no test-set tuning. The dominance of a few RNA families makes per-stratum reporting mandatory, not optional.
2. **Calibrated uncertainty.** Every prospective prediction carries a per-residue and per-interaction calibrated confidence; calibration (reliability curve, expected calibration error) is itself reported on held-out data and per stratum.
3. **Independent reproduction.** All metrics (TM, RMSD, lDDT, INF, DI, clash) are recomputed by a standalone scoring script - using the community RNA-Puzzles toolkit and US-align - separate from training code, from the committed splits and predictions.
4. **Cryptographic manifest.** A SHA-256 manifest covers the split definitions, data version hashes, model code, weights, and every predicted coordinate file, so no number can be silently regenerated after the fact.
5. **Preservation.** Training/fine-tuning code, weights, the physics-refinement configuration, and dataset version hashes are part of the record; anything not preserved is stated explicitly.
6. **Prospective-prediction registry.** Any blind prediction (P5) is timestamped and registered - with its ranking, confidence, and pre-committed accuracy claim - before the native structure is released, and is scored afterward including the misses.
7. **Honest reporting.** The report states up front that RNA 3D structure is reality-gated and **not resolved**; separates in-silico metrics from any experimental confirmation; labels every prospective model a wet-lab-pending hypothesis; and never presents a benchmark or leaderboard number as a real-world guarantee.
