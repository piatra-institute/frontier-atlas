# PROMPT FOR PROGRAMMABLE SMALL-MOLECULE BINDERS AND SENSORS

## Generative co-design of pocket and ligand for arbitrary small-molecule targets

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** B - reality-gated (empirical verifier)
**Rank:** B-22 of 29
**Source:** chem/bio top-50 list #26, section D (design)
**Modes:** `[gen]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The goal is a *programmable* capability: for an arbitrary small-molecule target, generatively co-design a protein pocket and (where the small molecule itself is to be designed) the ligand, so as to produce a specific binder - and, for a sensor, a binder whose ligand-bound state produces a measurable conformational readout. Structure-based generative models can now propose ligands inside a given pocket and, conversely, design pockets around a given ligand, but the field's central weakness is that the in-silico scorer of "does it bind" - molecular docking - is unreliable, and self-consistency of a designed pocket is not affinity. This is a **reality-gated** problem: binding and sensing are biophysical measurements on a synthesized ligand and an expressed protein, so the honest deliverable is a certified method contribution, an improved (synthesizable, dockable, testable) design proxy on a held-out target, and a small ranked calibrated design set - never a claimed resolution. Docking-score unreliability and the synthesizability constraint are treated as first-class obstacles; sensors add a conformational-readout requirement the binding score does not address.

## 1. Exact problem statement

**Design target.** Two coupled sub-problems.
- **Binder:** given a target - either a small molecule to be *bound by a protein* (design/redesign a protein pocket, e.g. via LigandMPNN / RFdiffusionAA) or a protein pocket to be *filled by a designed small molecule* (structure-based ligand generation) - output binder designs (protein sequences and/or ligand structures) predicted to form a specific complex.
- **Sensor:** in addition, the ligand-bound state must couple to a measurable readout - a conformational change reported by FRET, a fluorescence change, a split-reporter reconstitution, or induced binding to a partner. Binding alone is not a sensor; the readout is a separate design objective.

**Success metric (the whole problem).**
- **Binding:** \(K_D\) (or ITC \(\Delta H, K_a\)) for the intended target, and specificity against near-analog decoys.
- **Sensing:** dynamic range (signal fold-change on saturation), limit of detection, and response specificity.
- Plus, for any designed small molecule, **synthetic accessibility confirmed by actual synthesis**, and for any protein, expression/solubility.

**Target class.** One target per campaign (a metabolite, drug, toxin, or biomarker for a sensor; a defined pocket for de novo ligand generation). Generality across arbitrary targets is the aspiration, not an assumption.

**The in-silico-scorable sub-question (separable).** Independent of the wet lab, one can score: pose plausibility (docking), pocket self-consistency (does the designed sequence re-predict the pocket around the ligand), estimated binding free energy (FEP/MM-GBSA re-scoring), ligand validity and synthesizability (RDKit sanity + retrosynthesis). These are computable *filters*. **They are not binding, and none of them is sensing.** The gap between a top-docked, self-consistent, synthesizable design and a measured, specific, signal-producing binder is where this problem lives.

## 2. Verifier and data

**In-silico oracles and filters (and their known unreliability).**
- **Structure-based generative models** - Pocket2Mol, DiffSBDD, TargetDiff, and relatives generate ligands conditioned on a pocket. *Unreliable because* they routinely emit strained, invalid, or synthetically inaccessible molecules, and "fits the pocket" in the model is not measured affinity.
- **Pocket design** - LigandMPNN / RFdiffusionAA design a protein around a ligand/functional site. *Unreliable because* pocket self-consistency (re-prediction agreement) measures foldability around a pose, not binding energy or selectivity.
- **Molecular docking (AutoDock Vina, Gnina, and score functions generally).** *Unreliable because* docking has decent *pose* prediction but poor *scoring/affinity* power; scores rank-order weakly and are biased by decoy composition (DUD-E-style artifacts), protein flexibility, and solvation. **A good docking score is not a good binder.** This is the central failure to foreground.
- **FEP / MM-GBSA re-scoring** - physically better than docking on a congeneric series with a good pose. *Unreliable because* it needs a correct pose and force field, is expensive, and degrades on novel chemotypes and flexible pockets.
- **Synthesizability scores + retrosynthesis** (SA/SC-score, ASKCOS/AiZynthFinder). *Unreliable because* a "feasible" retrosynthetic route is a prediction, not a completed synthesis; routes fail in practice.
- **Conformational-readout prediction (for sensors).** Essentially unsolved in silico - coupling ligand binding to a defined signal is a multistate/allosteric property (cf. B23) that no single-structure score captures.

**Frozen benchmark / precedent set.** Fixed sets committed before modeling: a docking/affinity benchmark (e.g. a re-docking + affinity set such as PDBbind/CASF-style, verify) to characterize docking's own reliability; a set of *published* de novo small-molecule binders and biosensors with reported affinities/dynamic ranges (see §5). Reproducing docking's known scoring-power ceiling and the precedent affinities is the leakage-controlled baseline.

**Wet-lab gate (mandatory).** Binding and sensing cannot be established without new physical experiments: synthesis of any designed small molecule, expression/purification of any designed protein, and biophysical assays - ITC/SPR/fluorescence for binding, and a functional readout assay for a sensor. Rough cost: custom small-molecule synthesis ranges from a few hundred to several thousand dollars per compound (and multi-step routes can fail or cost far more); protein expression + a binding assay panel is on the order of \$1k–\$5k per design; a sensor's functional characterization (dynamic range, LOD, specificity) is a further defined cost. **This line is not optional and must not be softened: a top-docked, synthesizable-on-paper design is a hypothesis, not a measured binder or sensor.**

## 3. Standard of a genuine advance

A genuine advance is one of: (a) a **certified method contribution** - a co-design/scoring pipeline that improves on a named baseline for a well-posed in-silico task (e.g. pose+affinity ranking, or synthesizable-and-valid generation rate) reproduced independently; (b) an **improved design proxy on a held-out target** - a filter combining docking/FEP + synthesizability + pocket self-consistency that raises the confirmed-binder fraction, validated on a target withheld from construction; or (c) the top target: a **small, ranked, calibrated, synthesizable, falsifiable design set** for one specified target (binder, or binder+readout for a sensor), each design carrying a calibrated binding probability, a completed or high-confidence synthetic route, and a predicted affinity/dynamic-range class, handed to a wet-lab partner with pre-registered success criteria.

**Not accepted as resolution.**
- A top-docked pose or a low predicted \(\Delta G\) presented as a binder. Docking rank is not affinity; only ITC/SPR/fluorescence makes it a binder.
- **Pocket self-consistency reported as function.** Foldability around a pose is not binding or selectivity.
- A generated ligand with a good score but no credible synthesis, presented as a design; unsynthesizable molecules are non-deliverables.
- A binder claim doubling as a sensor claim with no conformational readout demonstrated; sensing is a separate, unmet objective until a signal is measured.
- FEP numbers on a novel chemotype/flexible pocket presented with the reliability they earn only on congeneric series with a validated pose.
- A single ITC hit from an unreported large screened set presented as a programmable success rate; the denominator must be stated.

## 4. Graded targets

**P1 - Reproduce docking/generative baselines and characterize docking reliability.** Reproduce a published structure-based generative model's validity/novelty/docking-score metrics and re-measure docking's own scoring power on a frozen affinity benchmark (report the ceiling, not just the pose success). *Certificate:* metrics within noise; committed code and hashes.

**P2 - Certified in-silico improvement.** Improve on a named baseline for a well-posed in-silico task - e.g. synthesizable-and-valid generation rate at matched docking score, or pose+affinity ranking with FEP re-scoring - reproduced independently. *Certificate:* frozen benchmark, frozen scores, independent recomputation.

**P3 - Improved confirmed-binder proxy on a held-out target.** Build a combined filter (docking/FEP + synthesizability + self-consistency) that raises the confirmed-binder fraction and validate it on a target withheld from construction; report the lift and calibration. *Certificate:* held-out split fixed before scoring.

**P4 - A ranked, calibrated, synthesizable, falsifiable design set (top target).** For one specified target, deliver ≤ 16 designs, ranked, each with a calibrated binding probability, a completed or high-confidence retrosynthetic route (or an expressible protein), a predicted affinity class, and - for a sensor - a predicted readout mechanism and dynamic-range class, plus a pre-registered success criterion. *Certificate:* frozen design set + routes + calibration model committed before any synthesis/assay; wet-lab partner named.

**P5 - Prospective wet-lab confirmation with honest calibration.** Only with a lab: the P4 set synthesized/expressed and assayed for binding (and, for sensors, readout), reporting the realized hit rate against the pre-registered criterion, the affinity/dynamic-range distribution, and the calibration error - including, plainly, if per-design real success was low. *Certificate:* raw assay data, the frozen predictions predating them.

## 5. Known results and prior art

- Structure-based generative models: Pocket2Mol (Peng et al., 2022), TargetDiff (Guan et al., 2023), DiffSBDD (Schneuing et al., 2022–2024, verify), and relatives (ResGen, Lingo3DMol - verify) - strong at pocket-conditioned generation but with well-documented validity/synthesizability and docking-score caveats.
- Docking and its limits: AutoDock Vina (Trott & Olson, 2010), Gnina (McNutt et al., 2021, verify); the docking-power vs scoring-power distinction and CASF/PDBbind evaluations (Su et al., verify); DUD-E decoy-bias findings on ML scoring (Chen et al., 2019, verify).
- Free-energy methods: FEP+ and modern relative-FEP (Wang et al., 2015, and later), reliable mainly on congeneric series with a validated pose.
- De novo small-molecule-binding proteins: the COMBS / van-der-Mer approach (Polizzi & DeGrado, 2020, verify) and Baker-lab designed small-molecule binders (Lu et al. / An et al., 2023–2024, verify) - including LigandMPNN and RFdiffusionAA for ligand-aware design.
- Designed protein biosensors: lucCage/LOCKR-style switchable sensors (Quijano-Rubio et al., 2021, verify) - precedent that binding can be coupled to readout, but per-target de novo sensor design is not routine.
- The consistent finding: generation is easy, *validated specific binding* is not, docking scoring is the weak verifier, synthesizability is a hard constraint, and de novo **sensing** (conformational readout) is markedly harder than binding.

*Status as of mid-2026 - re-verify against current literature before starting any session.*

## 6. Attack plan

**Datasets/inputs.** Pull the frozen affinity/docking benchmark and the precedent binder/sensor set; fix targets and a leakage-safe split (any target used to build a filter is held out). For ligand generation, fix the pocket structure; for pocket design, fix the ligand.

**Pipeline (one prosumer GPU suffices for the neural stages).** Structure-based generators (Pocket2Mol/TargetDiff/DiffSBDD) and/or LigandMPNN + RFdiffusionAA for pocket design; RDKit for validity/sanitization and descriptor computation; AutoDock Vina / Gnina for docking; optional FEP/MM-GBSA for shortlist re-scoring; ASKCOS or AiZynthFinder for retrosynthesis feasibility, with routes carried forward for any deliverable small molecule. For sensors, add a multistate/allostery analysis (cf. B23) to reason about readout coupling. Calibrate a binding-probability model and report calibration on held-out targets.

**Failure modes to expect and report.** (i) *Docking-score unreliability* - the single most important; report the scoring-power ceiling and never present a docking rank as affinity. (ii) *Synthesizability collapse* - generated molecules that score well but cannot be made; a route must accompany any deliverable. (iii) *Pocket self-consistency inflation* - re-prediction agreement that does not survive binding assays. (iv) *Sensor readout gap* - a binder that produces no measurable signal; readout is an unmet objective until demonstrated. (v) *Denominator hiding* - a good hit rate is meaningless without the number synthesized/tested.

## 7. Verification and auditability requirements

1. **Leakage-safe evaluation.** Any target/pocket used to build a filter is excluded from its evaluation; frozen benchmarks and splits are committed (hashed) before scoring; no tuning on the test target. The denominator (generated, filtered, synthesized, tested) is always reported.
2. **Calibrated uncertainty.** Every delivered design carries a calibrated binding probability (and, for sensors, a readout-plausibility estimate); calibration is reported on held-out targets. **Every design is a labeled hypothesis, not a claimed binder or sensor.**
3. **Separation of in-silico filters from real validation.** Docking scores, FEP numbers, and self-consistency metrics are kept physically separate from any measured affinity/readout; no in-silico score is presented as \(K_D\) or as a working sensor.
4. **Synthesizability is part of the deliverable.** Any designed small molecule ships with a retrosynthetic route and its feasibility assessment; molecules with no credible route are not counted as designs.
5. **Independent reproduction.** A standalone script recomputes all in-silico metrics from committed inputs, model hashes, and docking configs; SHA-256 manifest over designs, routes, code, scores, and (if any) assay data.
6. **Preservation.** Generation/design code, model versions, docking/FEP configs, and retrosynthesis outputs are part of the record. Anything not preserved is stated explicitly.
7. **Honest reporting.** The report states up front that the problem is reality-gated and NOT resolved; that *per-design real success rates are low*, that docking scoring is an unreliable verifier, and that de novo sensing is harder than binding. No top-docked, self-consistent, synthesizable-on-paper design is presented as a measured binder or sensor.
