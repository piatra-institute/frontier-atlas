# PROMPT FOR REACTION-YIELD AND CONDITION PREDICTION

## Yield, solvent, catalyst, temperature, and additives from reactants - under the missing-negative-data ceiling

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** B - reality-gated (empirical verifier)
**Rank:** B-26 of 29
**Source:** chem/bio top-50 list #29, section D (design)
**Modes:** `[data]` `[func]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Retrosynthesis tells you which bonds to make; yield-and-condition prediction tells you whether the reaction will actually work and under what solvent, catalyst, ligand, base, additive, temperature, and stoichiometry. It is the messier, higher-utility, and far more **data-starved** sibling of route planning: a chemist plans a synthesis in an afternoon but spends weeks optimizing conditions, and a model that reliably ranked conditions would compress that loop. The obstacle is not architecture but the ground truth. High-throughput experimentation (HTE) gives dense, clean, single-scaffold grids; the vast literature corpus (Reaxys, patent-mined USPTO) is enormous but **systematically biased toward reactions that worked** - the failed and low-yield experiments that a predictor most needs are largely unpublished. Models (random forests on HTE descriptors, yield-BERT, graph and fingerprint regressors, condition-recommendation nets) can *advance* the numbers on a fixed scaffold and *rank* plausible conditions, but they cannot *close* the problem: a predicted yield is a hypothesis until the reaction is run. This item is **reality-gated**. The honest deliverable is a certified method contribution, a held-out benchmark result on a leakage-safe split, and a ranked, calibrated set of condition recommendations handed to a wet-lab partner to run - never a claim that yield prediction is "solved."

## 1. Exact problem statement

**Input.** A reaction specified as reactant/reagent structures (SMILES or reaction SMILES), plus a candidate **condition context** drawn from a defined menu: solvent(s), catalyst / metal precursor, ligand, base, additive(s), temperature, concentration, time, and stoichiometric ratios. The prompt fixes, per task, whether conditions are *given* (yield regression) or *to be recommended* (condition prediction). Atom-mapping, when used, is a declared auxiliary input, not ground truth.

**Output.** Two coupled tasks, scored separately:

- **Yield regression / classification.** For a fully specified reaction + condition, a predicted yield $\hat y \in [0,100]\%$ with a **calibrated** predictive interval, or a calibrated probability that yield exceeds a threshold (e.g. $P(y \ge 50\%)$).
- **Condition recommendation.** For reactants and a target product, a *ranked* list of condition sets, each with a calibrated success probability, evaluated by top-$k$ recovery of a known working condition and by prospective wet-lab hit rate.

**Metrics.**

- Regression: root-mean-square error and mean absolute error in yield-percent, coefficient of determination $R^2$.
- Ranking: Spearman rank correlation - ranking, not absolute value, is the decision-relevant signal, since a chemist needs the best conditions ordered, not a calibrated absolute yield.
- Calibration: expected calibration error and predictive-interval coverage on held-out data.
- Condition recommendation: top-$k$ accuracy against recorded working conditions and, prospectively, the fraction of top-ranked suggestions that clear a yield threshold in the lab.

A metric is meaningful only with its population and split attached.

**Population.** Performance is claimed over a **named reaction population**: either a specific reaction class on an HTE grid (e.g. Buchwald–Hartwig C–N coupling, Suzuki–Miyaura C–C coupling), or a defined slice of the literature corpus stratified by reaction class and by substrate novelty. Aggregate numbers pooled across incomparable chemistries are not accepted, because per-class difficulty and data density vary enormously.

**Evaluation regimes.** Three regimes are reported separately and never conflated, because a single number hides which one is claimed:

- **Interpolation** - test reactions inside the training grid/scaffold family; an upper bound on ability, informative but not the goal.
- **Extrapolation** - test reactions on held-out scaffolds / out-of-domain catalysts; the regime that matters for real use.
- **Prospective** - reactions run after the prediction is registered; the only regime the wet-lab gate can confirm.

**Compute-tractable sub-question (in-silico).** Given a frozen, leakage-safe split of an existing HTE or curated corpus, produce a predictor whose held-out RMSE / rank correlation / top-$k$ meets or beats a named SOTA baseline in the **extrapolation** regime, with calibrated uncertainty - *within the domain the data covers*.

**Empirically-gated whole.** Predict the yield, or recommend the winning conditions, for a reaction **not represented in any training corpus** - a new substrate pair, a new scaffold, an out-of-domain catalyst - and have that prediction confirmed by running the reaction. No amount of compute closes this; only the experiment does.

## 2. Verifier and data

**Ground-truth source.**

- **Doyle–Dreher Buchwald–Hartwig HTE set** (Ahneman, Estrada, Lin, Dreher, Doyle, *Science* 2018) - a dense, clean C–N coupling yield grid over aryl halides, ligands, bases, and additives; the canonical HTE yield benchmark.
- **Suzuki–Miyaura HTE / flow-screening set** (Perera et al., *Science* 2018, verify) - nanomole-scale automated Suzuki screening across ligands / bases / solvents.
- **Open Reaction Database (ORD)** (Kearnes et al., ~2021) - a growing open, structured reaction corpus with conditions; the preferred non-proprietary substrate.
- **USPTO reaction corpus** (Lowe patent text-mining) - large, public, but noisy, sparsely conditioned, and success-biased.
- **Reaxys / electronic-lab-notebook (ELN) corpora** (verify; access-gated) - large curated literature reactions with conditions; proprietary and success-biased.
- **Additional pharma/academic HTE releases** (verify) - further single-scaffold grids (e.g. amide coupling, C–H functionalization panels) where publicly available.

**Frozen split (leakage-safe).** The test set is fixed before modeling under a **substrate / scaffold-separation** axis, not a random split: cluster reactions by reactant scaffold (Bemis–Murcko / reaction-center fingerprint) and by reaction class, and hold out **entire clusters** so no test reaction shares a scaffold with training. Where the corpus is time-stamped (patents, ELN), add a **time split** (train on reactions before a committed date, test after). Random splits on HTE grids inflate scores by memorizing one axis of the grid and must be reported only as an interpolation upper bound alongside the scaffold-out split. Split definitions and cluster manifests are committed and hashed before any test number is computed. The **missing-negative-data problem** is documented explicitly: literature corpora contain few genuine failures, so a literature-trained model's apparent accuracy is conditioned on the survivorship bias of what got published.

**Negative and low-yield data.** Because the missing-negative-data problem is central, the corpus is characterized before modeling: what counts as a failure (no product, trace yield, wrong product), how much of it each source contains, and where genuine negatives can be sourced (HTE grids include zeros; ELN corpora sometimes record failures; deliberately run failure plates). A model trained only on published successes has never seen the decision boundary it is asked to predict, and this must be stated wherever such a model is used.

**Wet-lab gate (mandatory).** A predicted yield or a recommended condition set **cannot be established as correct by any computation**. Confirmation requires physically running the reaction and quantifying the product (LC-MS / HPLC / NMR assay). A focused HTE validation plate - tens to a few hundred wells - costs roughly \$5k–\$50k in reagents, instrument time, and analysis depending on scale and substrate cost; a single scale-up validation is cheaper but tests only one point. This gate is not softenable: negative and out-of-domain results, precisely the ones absent from the corpus, can be obtained only by running experiments.

## 3. Standard of a genuine advance

A genuine advance is one of:

1. A **certified method contribution** - a model, representation, or featurization that achieves a *new held-out SOTA* on a frozen, **scaffold-separated** split (better RMSE, rank correlation, and top-$k$ at matched data and compute), with the improvement shown to hold on the hardest stratum (novel scaffolds, out-of-domain catalysts / ligands), and with calibrated uncertainty validated on held-out data.
2. A **calibrated, falsifiable condition-recommendation set** for reactions a wet-lab partner will run: a ranked slate of condition proposals with per-proposal success probabilities and a pre-committed accuracy claim (e.g. "≥ $k$ of top-$n$ suggestions clear 50% yield"), registered before the plate is run.

**Not accepted as resolution:**

- A **leaderboard number treated as a real-world guarantee** - a good HTE-grid RMSE is a claim about interpolation within one scaffold, not about a new substrate.
- **In-silico-only "validation"** - agreement with a DFT descriptor model, a mechanism heuristic, or a consensus of other predictors is not an experimental result.
- A **corpus-overfit or leakage-inflated metric** - high scores driven by random splits on a dense grid, by scaffold leakage, or by exploiting the literature's success bias (predicting "high yield" because failures are absent).
- A model that **implicitly assumes every reaction works** because it never saw a labeled failure, and is presented as generally predictive.
- A **yield-conditional-on-success** predictor (accurate only among reactions already known to proceed) presented as a general go/no-go tool.
- "Solved yield prediction" claimed from any retrospective set.

## 4. Graded targets

**P0 - Data and leakage audit.** Assemble the corpus, characterize each source's negative-data profile, build the scaffold / reaction-center clustering, and commit the frozen splits (scaffold-out, random upper bound, time split) with hashes. *Evidence:* the committed split manifest, a report of per-source success bias, and a demonstration that scaffold clusters do not bleed across the split. This precedes any modeling and is itself a reusable contribution.

**P1 - Reproduce a SOTA baseline on our verified pipeline.** Re-run a published model (random forest on Doyle-style DFT / physical descriptors; yield-BERT / rxnfp fingerprint regressor; a graph-neural yield model) on our frozen scaffold-separated split and reproduce reported RMSE / rank correlation within tolerance. *Evidence:* committed split hashes, an independent scoring script, per-stratum tables. Independently valuable as a leakage-audited baseline. Include the **random-label control** (fit the same pipeline to shuffled yields) to quantify how much apparent skill is dataset artifact.

**P2 - Calibrated uncertainty.** Add and validate a predictive interval / success probability whose coverage and expected calibration error are measured on held-out data, per stratum, with explicit reporting of degraded calibration off-domain. *Evidence:* reliability curves, coverage tables, and an out-of-domain calibration stress test.

**P3 - Certified method contribution.** A modeling change (physically grounded featurization, reaction-center-aware representation, uncertainty-aware active-learning loop, negative-data-aware loss) that yields a *statistically significant, leakage-audited* improvement over P1 on the hard scaffold-out and out-of-domain strata. *Evidence:* paired per-reaction deltas with confidence intervals; ablations; no test-set tuning.

**P4 - New held-out SOTA / cross-domain transfer.** Best-in-class on the committed scaffold- and time-separated split simultaneously across regression, ranking, and condition top-$k$, including demonstrated transfer from HTE grids to literature-scale reactions (or the reverse). *Evidence:* full error distributions, split manifest, independent reproduction from committed code.

**P5 - Wet-lab-ready condition recommendations.** A ranked, calibrated slate of condition proposals for reactions a partner will physically run (or a live HTE campaign), registered before the plate, with a pre-committed falsifiable hit-rate claim. *Evidence:* timestamped registration, post-hoc scoring against measured yields, honest hit/miss accounting including misses and off-domain failures. This is the ceiling the machine can reach; closing the loop is the experiment's job.

## 5. Known results and prior art

- **HTE yield prediction** - Ahneman, Estrada, Lin, Dreher, Doyle (*Science* 2018): random forests on DFT / physical-organic descriptors predict Buchwald–Hartwig yields on a dense grid. The foundational result and benchmark.
- **Random-label critique** - Chuang & Keiser (*Science* 2018, comment): shuffled-label and simplified-feature controls show much apparent skill on the Doyle set reflects dataset structure, not mechanism - the reason a random-label control is mandatory here.
- **Yield from reaction fingerprints** - Schwaller, Vaucher, Laino, Reymond (~2021, *Mach. Learn.: Sci. Technol.*): "yield-BERT," transformer reaction embeddings (rxnfp) regressed to yield; strong on HTE grids, weak out-of-domain.
- **Structure-based reactivity platform** - Sandfort, Strieth-Kalthoff, Glorius et al. (~2020, *Chem*): multiple-fingerprint featurization for reactivity / yield.
- **Condition recommendation** - Gao, Struble, Coley, Jensen et al. (~2018, *ACS Cent. Sci.*): neural recommendation of catalyst / solvent / reagent / temperature from reactant structure; and reaction-class condition models (verify).
- **Reaction representation** - Schwaller et al. (rxnfp / reaction-class embeddings, ~2021, *Nat. Mach. Intell.*); atom-mapping via RXNMapper.
- **Real-world-dataset challenges** - Saebi, Żurański, Doyle, Wiest, Chawla et al. (~2023, *Chem. Sci.*, verify): documents the collapse of HTE-trained models on literature-scale, out-of-domain reactions and the negative-data gap.
- **Data infrastructure** - Open Reaction Database (Kearnes et al., ~2021); USPTO reactions (Lowe); Reaxys (proprietary).

*Status as of mid-2026 - re-verify against current literature before starting any session.* Yield/condition prediction is active; check whether new open HTE releases, negative-data collection efforts, or foundation reaction models have shifted out-of-domain generalization, and re-verify every dataset's access terms and success-bias profile before use.

## 6. Attack plan

**Data.** Pull the Doyle–Dreher C–N and Suzuki HTE grids and the Open Reaction Database; where accessible, ingest a literature / ELN slice. Build the scaffold / reaction-center clustering; commit a **scaffold-out** split (primary) plus a random split (interpolation upper bound) and, on time-stamped corpora, a **time split**. Freeze and hash all splits before modeling. Document the negative-data profile of each source.

**Baselines.** Reproduce the random-forest-on-descriptors model, yield-BERT / rxnfp, and a graph-neural regressor. Run the **random-label control** on each. Score with an independent script separate from training code.

**Model.** Candidate contributions:

- Physically grounded, reaction-center-localized featurization - DFT / steric / electronic descriptors of the varying components, following the Doyle/Sandfort line.
- Uncertainty-aware ensembles or Gaussian-process heads for calibrated intervals and reliable ranking.
- An **active-learning loop** that proposes maximally informative wells for a partner's next HTE plate, directly attacking data scarcity.
- Explicit handling of the missing-negative-data problem - imputing plausible failures, positive-unlabeled learning, or down-weighting survivorship-biased corpora.

**Calibration.** Fit and validate predictive intervals / success probabilities on held-out data (conformal prediction, temperature / isotonic scaling); report coverage and expected calibration error per stratum and, crucially, on an out-of-domain hold-out where calibration is expected to degrade.

**Compute.** Descriptor models, fingerprint transformers, and graph regressors all train and run on one prosumer GPU - compute is not the bottleneck; **data** is. Prefer data-efficient methods and active learning over scaling.

**Failure modes.**

- **Data scarcity** - HTE grids are dense but narrow; a model excellent on one scaffold may be useless on the next.
- **Missing negative data** - literature corpora omit failures, so literature-trained models systematically overpredict success and are miscalibrated toward optimism.
- **Distribution shift** - new substrates, catalysts, and ligands lie outside the training manifold; interpolation scores do not transfer.
- **Leakage** - random splits on dense grids and scaffold leakage silently inflate every number; the scaffold-out split is non-negotiable.
- **Label noise** - literature yields are heterogeneously reported, sometimes crude, and scale-dependent.

## 7. Verification and auditability requirements

1. **Leakage-safe evaluation.** The train/test split is committed and hashed before any evaluation, under documented **scaffold / reaction-center separation** and, where applicable, time separation; random splits are reported only as a labeled interpolation upper bound; there is no test-set tuning; per-reaction-class and per-novelty strata are reported separately.

2. **Random-label and simplified-feature controls.** Every headline model is accompanied by a shuffled-label control and a trivial-baseline comparison, so the fraction of apparent skill attributable to dataset artifact versus chemistry is quantified and reported.

3. **Calibrated uncertainty.** Every prospective prediction carries a calibrated predictive interval or success probability; coverage and expected calibration error are reported on held-out data, per stratum, and explicitly on an out-of-domain hold-out.

4. **Missing-negative-data accounting.** The report states, for each data source, its negative-data profile and success bias, and how the method accounts for it; any claim of general predictivity acknowledges that the model may never have seen a labeled failure.

5. **Independent reproduction.** All metrics (RMSE, MAE, $R^2$, Spearman, top-$k$, calibration) are recomputed by a standalone script separate from training code, from the committed splits and predictions.

6. **Cryptographic manifest and preservation.** A SHA-256 manifest covers split definitions, dataset version hashes, featurization and model code, weights, and every prediction file; training code, descriptors, and data versions are part of the record; anything not preserved is stated explicitly. Prospective recommendation sets (P5) are timestamped and registered before the plate is run and scored afterward including misses.

7. **Honest reporting.** The report states up front that reaction yield/condition prediction is reality-gated and **not resolved**; separates in-silico metrics from any wet-lab result; labels every recommendation a wet-lab-pending hypothesis; foregrounds the missing-negative-data problem and out-of-domain fragility; and never presents an HTE-grid or leaderboard number as a real-world guarantee.
