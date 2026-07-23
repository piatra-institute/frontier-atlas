# PROMPT FOR INVERSE MOLECULAR DESIGN UNDER SYNTHESIZABILITY AND ADMET SIMULTANEOUSLY

## Multi-objective generation constrained jointly, not property-by-property, against weak ADMET verifiers

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** B - reality-gated (empirical verifier)
**Rank:** B-24 of 29
**Source:** chem/bio top-50 list #30, section D (design)
**Modes:** `[gen]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Molecular generators can optimize almost any single property. The unsolved task is inverse design under the *full* real constraint set - potency plus the whole ADMET profile plus genuine synthesizability - enforced *simultaneously*, not one property at a time (single-property wins routinely collapse when the other constraints are re-imposed). The distinctive hazard here is that the in-silico verifiers being optimized against - ADMET predictors - are themselves unreliable, so the pipeline chains an unreliable objective to an unreliable generator: in-silico "success" is doubly overstated. This is a **reality-gated** problem: ADMET, PK, and synthesizability are established only by assays (and, for the full PK/tox picture, animal studies), so the honest deliverable is a certified multi-objective/method contribution, an improved held-out ADMET-prediction and synthesizability proxy, and a small ranked calibrated set of falsifiable, synthesizable candidates - never a claimed resolution. The weakness of the ADMET verifier - chained unreliability - is the crux and is foregrounded throughout.

## 1. Exact problem statement

**Design target.** Given a target activity objective (a potency requirement against a stated target, or a property profile) and a *joint* constraint set - synthesizability plus a specified ADMET envelope (e.g. solubility, permeability, metabolic stability, hERG liability, CYP inhibition, plasma protein binding, and basic PK feasibility) - output molecules (with structures and proposed syntheses) that satisfy *all* constraints at once.

**Success metric (the whole problem).**
- **Joint constraint satisfaction under measurement:** the fraction of delivered molecules that, when synthesized and assayed, meet the specified potency *and* the specified ADMET envelope *simultaneously* - not the fraction passing any single axis.
- **Synthesizability realized:** molecules actually made (route executed), not merely scored as accessible.
- **Calibration of the ADMET predictions:** how well predicted ADMET matched measured ADMET on the delivered set.

**Target class.** One target/objective per campaign (a defined activity target plus a defined ADMET envelope suited to a route of administration). Generality across targets is not assumed.

**The in-silico-scorable sub-question (separable).** Independent of the wet lab, one can score: multi-objective Pareto behavior of a generator under joint constraints; validity, novelty, and diversity of output; synthesizability by score and by retrosynthesis; and predicted ADMET across the envelope. These are computable *proxies*. **They are not measured ADMET, PK, or a completed synthesis.** The gap between a molecule that satisfies every predicted constraint and one that survives real assays is wide *and widened further* by the unreliability of the ADMET predictors themselves - the objective is soft, so optimizing it hard invites Goodhart failure.

## 2. Verifier and data

**In-silico oracles and filters (and their known unreliability).**
- **Multi-objective generative models** (REINVENT and RL-based generators, graph/SMILES/fragment models, genetic algorithms). *Unreliable because* they can exploit weaknesses of the reward/predictor (reward hacking), and joint Pareto optimization often produces molecules that satisfy the *scores* rather than the *properties*.
- **Synthesizability scores** - SAscore, SCScore, RAscore. *Unreliable because* they are coarse proxies; a "synthesizable" score does not guarantee a real route, and they penalize novel-but-makeable chemotypes.
- **Retrosynthesis planners** - ASKCOS, AiZynthFinder. *Unreliable because* a proposed route is a prediction; routes fail on selectivity, protecting groups, and reagent availability; template coverage is uneven.
- **ADMET predictors** - ADMET-AI, admetSAR, pkCSM, and Therapeutics-Data-Commons-trained models. **This is the weak verifier and the whole point of the problem.** *Unreliable because* they are trained on limited, assay-heterogeneous, often imbalanced public data; they extrapolate poorly off the training chemotypes; endpoints (hERG, metabolic stability, clearance) have modest predictive ceilings; and different assays for the "same" endpoint disagree. Optimizing a generator against these produces confident predictions on molecules exactly where the predictor is least trustworthy (out of distribution). **Chained unreliability: an unreliable generator optimized against an unreliable objective - in-silico success rates badly overstate real success.**

**Frozen benchmark / precedent set.** Fixed sets committed before modeling: an ADMET-prediction benchmark with proper scaffold/temporal splits (e.g. Therapeutics Data Commons endpoints, verify) to characterize the predictors' *own* reliability; a synthesizability benchmark (retrosynthesis solve-rate on a held-out set); and any published multi-objective-generation precedents with downstream experimental follow-up. Reproducing the predictors' held-out ceilings is the leakage-controlled baseline - and the honest starting point, since those ceilings bound everything built on them.

**Wet-lab gate (mandatory).** ADMET, PK, and synthesizability cannot be established without new physical experiments: actual synthesis, then in-vitro ADME panels (kinetic solubility, Caco-2/PAMPA permeability, microsomal/hepatocyte stability, hERG patch/binding, CYP inhibition, plasma protein binding), and - for the full PK/tox profile - in-vivo studies in animals. Rough cost: synthesis of a single novel compound ranges from hundreds to several thousand dollars (multi-step routes far more, and some fail); an in-vitro ADME panel is on the order of \$1k–\$10k per compound depending on breadth; in-vivo PK is materially more per compound; a full profile across a series is a major, multi-month spend. **This line is not optional and must not be softened: a molecule that passes every ADMET predictor is a hypothesis about a compound, not a measured ADMET/PK profile.**

## 3. Standard of a genuine advance

A genuine advance is one of: (a) a **certified method contribution** - a multi-objective, synthesizability-constrained generator that, under *joint* constraints, produces a higher fraction of valid + genuinely-synthesizable + envelope-satisfying molecules than a named baseline, reproduced independently; (b) an **improved held-out proxy** - a better-calibrated ADMET predictor or synthesizability filter validated on a scaffold/temporal split withheld from construction (raising the trustworthiness of the objective itself, which is the highest-leverage move here); or (c) the top target: a **small, ranked, calibrated, synthesizable, falsifiable candidate set** for one specified objective, each molecule carrying a completed/high-confidence route and calibrated ADMET predictions with uncertainty, handed to a wet-lab partner with pre-registered success criteria.

**Not accepted as resolution.**
- Molecules satisfying every *predicted* constraint, presented as satisfying the constraints. Predicted ADMET is not measured ADMET; only assays decide.
- **Single-axis optimization presented as joint design.** A potency win that ignores (or serially re-optimizes) ADMET/synthesizability is not the problem being solved.
- A "synthesizable" score or a proposed route presented as a made molecule; only an executed synthesis counts as synthesized.
- ADMET predictions reported without their out-of-distribution caveat and without calibration - treating a weak verifier as ground truth.
- Reward-hacked molecules (optimizing predictor artifacts) presented as designs; sanity checks against artifacts are required.
- A single clean profile from an unreported large generated pool presented as a design success rate; the denominator must be stated.

## 4. Graded targets

**P1 - Reproduce generator + ADMET/synthesizability baselines.** Reproduce a published multi-objective generator's reported metrics and re-measure the ADMET predictors' and retrosynthesis planner's held-out performance on frozen benchmarks (report the reliability ceilings). *Certificate:* metrics within noise; committed code and hashes.

**P2 - Certified joint-constraint generation improvement.** Show a generator produces a higher fraction of valid + synthesizable (route-solved) + envelope-satisfying molecules under *simultaneous* constraints than a named baseline, reproduced independently, with reward-hacking checks. *Certificate:* frozen benchmark, frozen outputs, independent recomputation.

**P3 - Improved, better-calibrated held-out ADMET / synthesizability proxy.** Improve the calibration and/or accuracy of an ADMET endpoint predictor or synthesizability filter on a scaffold/temporal split withheld from construction; report the lift and the calibration curve. *Certificate:* held-out split fixed before scoring. (This directly strengthens the weak verifier.)

**P4 - A ranked, calibrated, synthesizable, falsifiable candidate set (top target).** For one specified objective, deliver ≤ 16 molecules, ranked, each with a completed or high-confidence retrosynthetic route, calibrated ADMET predictions *with uncertainty across the envelope*, and a pre-registered joint success criterion (e.g. "≥ 3 of the top 8, when made, meet potency AND ≥ 4 of the specified ADMET endpoints"). *Certificate:* frozen set + routes + calibration model committed before any synthesis/assay; wet-lab partner named.

**P5 - Prospective wet-lab confirmation with honest calibration.** Only with a lab: the P4 set synthesized and run through the ADME panel (and PK where feasible), reporting the realized joint-satisfaction rate against the pre-registered criterion, the predicted-vs-measured ADMET calibration, and the synthesis success rate - including, plainly, if per-molecule real success was low. *Certificate:* raw assay data, the frozen predictions predating them.

## 5. Known results and prior art

- REINVENT - RL for molecular de novo design (Olivecrona et al., 2017; Blaschke et al., 2020, REINVENT 2.0; REINVENT 4, 2024, verify); the standard multi-objective scoring/RL framework.
- Multi-objective / Pareto molecular generation: genetic-algorithm and RL baselines (GraphGA, Jensen 2019; JANUS; MolDQN), and MOO scalarization/Pareto approaches (verify specifics).
- Synthesizability-constrained generation: SynNet and synthesis-aware generation (Gao & Coley, 2021, verify), SyntheMol (Swanson et al., 2024, verify); scores SAscore (Ertl & Schuffenhauer, 2009), SCScore (Coley et al., 2018), RAscore (Thakkar et al., 2021, verify).
- Retrosynthesis planners: ASKCOS (Coley, Jensen and co-workers) and AiZynthFinder (Genheden et al., 2020, verify).
- ADMET predictors and benchmarks: ADMET-AI (Swanson et al., 2024, verify), admetSAR, pkCSM; Therapeutics Data Commons (Huang et al., 2021) as the standard ADMET benchmark suite - with well-documented data-heterogeneity and distribution-shift limits.
- The consistent finding: single-property optimization is easy; *joint* synthesizability + full-ADMET design is not, and the ADMET predictors are the weak link - a model can "solve" the in-silico objective while its predictions are least reliable exactly on the novel molecules it generates.

*Status as of mid-2026 - re-verify against current literature before starting any session.*

## 6. Attack plan

**Datasets/inputs.** Pull the ADMET benchmark (TDC-style, scaffold/temporal splits), a retrosynthesis solve-rate benchmark, and any generation precedents with experimental follow-up. Fix the objective, the ADMET envelope, and a leakage-safe split (any endpoint/scaffold used to build a predictor is held out of its evaluation).

**Pipeline (one prosumer GPU suffices).** REINVENT (or a graph/GA generator) under a joint multi-objective reward; RDKit for validity/descriptors and reward-hacking sanity checks; SAscore/SCScore/RAscore plus ASKCOS/AiZynthFinder for synthesizability, with routes carried forward for deliverables; an ensemble of ADMET predictors (ADMET-AI / TDC-trained) with explicit uncertainty and out-of-distribution flags. Calibrate ADMET and synthesizability predictors on held-out splits and report the calibration - strengthening the verifier is itself a target (P3).

**Failure modes to expect and report.** (i) *Chained unreliability* - the central one: a generator optimizing weak ADMET predictors, most confident where least trustworthy; report predictor OOD flags and calibration alongside every design. (ii) *Reward hacking* - molecules exploiting predictor artifacts; run sanity checks and adversarial filters. (iii) *Synthesizability collapse* - score-passing molecules with no real route; require a route per deliverable. (iv) *Serial re-optimization masquerading as joint design* - enforce constraints simultaneously and report the joint (not per-axis) satisfaction rate. (v) *Denominator hiding* - one clean profile is not a success rate without the tested count.

## 7. Verification and auditability requirements

1. **Leakage-safe evaluation.** Any endpoint/scaffold used to build a predictor is excluded from its evaluation; scaffold/temporal splits and benchmarks are committed (hashed) before scoring; no tuning on the test split. The joint (simultaneous) satisfaction rate is reported, never per-axis wins alone; the denominator is always stated.
2. **Calibrated uncertainty.** Every delivered molecule carries calibrated ADMET predictions *with uncertainty and OOD flags* across the envelope, plus a synthesizability confidence; calibration is reported on held-out data. **Every molecule is a labeled hypothesis, not a measured profile.**
3. **Weak-verifier honesty.** The report foregrounds that ADMET predictors are unreliable, states their held-out ceilings and calibration, and never treats a predicted ADMET pass as ground truth (chained unreliability made explicit).
4. **Synthesizability is part of the deliverable.** Every delivered molecule ships with a retrosynthetic route and its feasibility assessment; score-only "synthesizable" molecules are not counted as designs.
5. **Independent reproduction.** A standalone script recomputes all in-silico metrics from committed inputs, model hashes, and reward configs; SHA-256 manifest over designs, routes, code, scores, and (if any) assay data; reward-hacking sanity checks included.
6. **Preservation.** Generator code, reward configuration, predictor versions, and retrosynthesis outputs are part of the record. Anything not preserved is stated explicitly.
7. **Honest reporting.** The report states up front that the problem is reality-gated and NOT resolved; that *per-molecule real success rates are low*, that ADMET predictors are the weak verifier, and that joint synthesizability + full-ADMET design under measurement remains open. No molecule that merely passes the predictors is presented as satisfying the real constraints.
