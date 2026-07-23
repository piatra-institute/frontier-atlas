# PROMPT FOR DESIGNING A TARGET CONFORMATIONAL ENSEMBLE AND ALLOSTERY

## Multistate design for a specified ensemble and a switch, not a single rigid structure

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** B - reality-gated (empirical verifier)
**Rank:** B-23 of 29
**Source:** chem/bio top-50 list #25, section D (design)
**Modes:** `[gen]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Almost all successful protein design targets a *single* rigid structure. Function, however, often lives in an *ensemble*: two or more conformational states, a defined population ratio, and a switch that shifts that ratio in response to a stimulus (a ligand, a partner, pH, phosphorylation) - i.e. allostery. Designing for the ensemble is hard precisely because the dominant generators (RFdiffusion, AlphaFold) are single-structure engines; the objective here is a free-energy landscape with specified populations and a specified coupling, not one backbone. This is a **reality-gated** problem: state populations and allosteric coupling are functional/biophysical measurements (smFRET, NMR, HDX, activity assays), so the honest deliverable is a certified multistate-design/method contribution, an improved in-silico switching proxy on a held-out design, and a small ranked calibrated set of falsifiable switch designs - never a claimed resolution. The ensemble-objective gap versus single-structure design is the crux, and it connects directly to the Pack A conformational-ensemble work (A13).

## 1. Exact problem statement

**Design target.** Output a protein sequence (and the intended state models) that populates a *specified conformational ensemble*: two (or more) defined states \(S_1, S_2, \dots\) with a target population ratio (target \(\Delta G_{S_1\to S_2}\)), and - for an allosteric switch - a specified stimulus that shifts the populations by a target amount (target \(\Delta\Delta G\) of switching upon ligand/partner binding or condition change).

**Success metric (the whole problem).**
- **Two-state existence and population:** experimental evidence that both intended states are populated (smFRET distance distributions, NMR/relaxation-dispersion, HDX-MS, or a state-specific reporter), with the measured population ratio compared to the target.
- **Switching:** the measured change in population / activity upon the specified stimulus (target-referenced \(\Delta\Delta G\) or fold-change), and its specificity to that stimulus.
- Plus expression/solubility and, ideally, structures of both states.

**Target class.** One designed switch per campaign, drawn from: a two-state conformational toggle, a ligand-induced hinge/rigid-body motion, or a designed allosteric coupling between an effector site and a functional site. Generality is not assumed.

**The in-silico-scorable sub-question (separable).** Independent of the wet lab, one can score: does a single sequence satisfy *both* target backbones (multistate self-consistency - re-prediction of each intended state, and a designed-in energy gap); does an ensemble generator sample both states with roughly the target populations; does MD show interconversion with a plausible barrier and no collapse to one state. These are computable *proxies*. **They are not measured populations or switching.** The gap between a sequence that "looks bistable" in silico and one whose ensemble and coupling are experimentally correct is the heart of the problem - worsened because in-silico state populations rest on force-field and sampling accuracy that is itself unresolved (cf. A13).

## 2. Verifier and data

**In-silico oracles and filters (and their known unreliability).**
- **Multistate design (Rosetta-style)** - design one sequence for stability in multiple fixed backbones with a target energy gap. *Unreliable because* a designed gap in a score function is not a measured \(\Delta G\); score functions are not calibrated free energies, and the two backbones may not be the ensemble's actual metastable states.
- **Ensemble generators** - AF2 with subsampled/clustered MSAs, AlphaFlow/ESMFlow, and Boltzmann-style generators to sample alternative states. *Unreliable because* the sampled "states" and their apparent populations are not validated Boltzmann weights; MSA-subsampling tricks reveal alternative conformers without giving correct thermodynamics.
- **MD validation of switching** - does the designed sequence interconvert with a plausible barrier and target populations. *Unreliable because* force-field error and timescale limits make populations and barriers quantitatively untrustworthy; enhanced sampling helps but does not close the gap (this is exactly A13's open problem).
- **Single-structure re-prediction (AF3/AF2, ipTM/pLDDT).** *Unreliable and mis-targeted here* - high confidence in one structure says nothing about the second state or the coupling; a confident single-state prediction can be actively misleading for an ensemble objective.
- **Allosteric-network analysis** (SCA, perturbation/normal-mode methods) - proposes coupling pathways. *Unreliable because* predicted pathways are hypotheses about coupling, not measured \(\Delta\Delta G\).

**Frozen benchmark / precedent set.** A fixed set committed before modeling: *published* designed conformational switches and multistate designs with reported state populations / switching (see §5), plus natural allosteric proteins with measured two-state thermodynamics as a calibration reference. Reproducing their in-silico multistate metrics and rank-ordering known switch magnitudes is the leakage-controlled baseline.

**Wet-lab gate (mandatory).** Ensemble populations and allosteric function cannot be established without new physical experiments: expression/purification, then state-resolving biophysics - smFRET (labeling + single-molecule instrument), NMR (isotope labeling + spectrometer time, including relaxation-dispersion for minor states), HDX-MS, and/or a functional switch assay - plus stimulus titrations. Rough cost: expression + a functional switch readout is on the order of \$1k–\$5k per design; state-resolving biophysics (smFRET or NMR) is labor- and instrument-heavy and materially more expensive, often \$10k+ and weeks per construct; two-state structural confirmation (two crystal forms or cryo-EM states) is a further major cost. **This line is not optional and must not be softened: a design that looks bistable in silico is a hypothesis about an ensemble, not a measured one.**

## 3. Standard of a genuine advance

A genuine advance is one of: (a) a **certified method contribution** - a multistate/ensemble design or scoring method that, on the frozen precedent set, predicts measured state populations or switch magnitudes better than a named baseline, reproduced independently; (b) an **improved in-silico switching proxy on a held-out design** - a metric that better predicts realized two-state behavior, validated on a design withheld from construction; or (c) the top target: a **small, ranked, calibrated, expressible, falsifiable switch design set** for one specified ensemble/allostery objective, each design carrying calibrated predictions of population ratio and switch magnitude, handed to a wet-lab partner with pre-registered success criteria.

**Not accepted as resolution.**
- A design that re-predicts one target state confidently, presented as an ensemble/switch. A single confident structure is not a bistable protein.
- **Single-structure self-consistency (AF3/AF2 agreement) reported as ensemble function.** It measures one state, not populations or coupling.
- A designed energy gap in a score function presented as a measured \(\Delta G\); score-function gaps are not calibrated free energies.
- MD populations or barriers presented with the reliability they do not have, given unresolved force-field/sampling error (see A13).
- A predicted allosteric pathway (SCA/normal modes) presented as a demonstrated coupling.
- A single working switch from an unreported pool presented as a general capability; the denominator must be stated.

## 4. Graded targets

**P1 - Reproduce a multistate-design pipeline's in-silico metrics.** Rebuild a multistate design and/or ensemble-generation pipeline and reproduce reported multistate self-consistency / sampled-population metrics on a published switch. *Certificate:* metrics within noise; committed code and hashes.

**P2 - Certified retrospective discrimination on the frozen set.** Show the pipeline predicts measured state populations / switch magnitudes across the frozen precedent set better than a named baseline, with an honest correlation and confidence interval. *Certificate:* frozen set, frozen scores, independent recomputation.

**P3 - Improved switching proxy on a held-out design.** Build a metric predicting realized two-state behavior and validate it on a design withheld from construction; report the lift and calibration. *Certificate:* held-out split fixed before scoring.

**P4 - A ranked, calibrated, falsifiable switch design set (top target).** For one specified ensemble/allostery objective, deliver ≤ 16 designs, ranked, each with a calibrated predicted population ratio, a predicted switch magnitude/direction, the stimulus, and a pre-registered success criterion (e.g. "≥ 2 of the top 8 show a stimulus-dependent state shift of the target sign and ≥ 2-fold"). *Certificate:* frozen design set + calibration model committed before any assay; wet-lab partner named.

**P5 - Prospective wet-lab confirmation with honest calibration.** Only with a lab: the P4 set expressed and probed by state-resolving biophysics + a switch assay, reporting realized population ratios and switch magnitudes against the pre-registered criterion and the calibration error - including, plainly, if per-design real success was low. *Certificate:* raw smFRET/NMR/HDX/activity data, the frozen predictions predating them.

## 5. Known results and prior art

- Multistate / multispecificity design in Rosetta (Havranek & Harbury; Leaver-Fay, Kuhlman, and co-workers) - the framework for designing one sequence toward multiple states/specificities. (verify authors/years)
- Designed conformational switches and hinges: LOCKR / switchable de novo systems (Langan et al., 2019; Praetorius et al., 2023 designed hinges - verify), pH-responsive and ligand-induced switches from the Baker lab.
- Ensemble generators and their thermodynamic caveats: AlphaFlow / ESMFlow (Jing et al., 2024, verify), MSA-subsampling to reveal alternative states (Del Alamo et al., 2022, verify), Boltzmann generators (Noé et al., 2019); emerging emulators (BioEmu, 2024–2025, verify). These sample alternative states but do **not** deliver validated Boltzmann populations.
- Allosteric-network inference: statistical coupling analysis / SCA (Lockless & Ranganathan, 1999; Ranganathan and co-workers), perturbation and normal-mode methods.
- Connection to Pack A: A13 (conformational ensembles with correct Boltzmann weights) is the on-machine analog; the *design* objective here inherits A13's unresolved sampling/force-field accuracy problem - a designer cannot yet trust in-silico populations.
- The consistent finding: single-state design is comparatively routine, ensemble/allostery-by-design is not; the ensemble objective is the open gap.

*Status as of mid-2026 - re-verify against current literature before starting any session.*

## 6. Attack plan

**Datasets/inputs.** Pull the frozen precedent set (designed switches + measured populations/switching) and a calibration set of natural two-state proteins. Fix target state models and a leakage-safe split (any design used to build a metric is held out).

**Pipeline (one prosumer GPU suffices for the neural stages).** Rosetta multistate design for the sequence-toward-two-backbones step; AF2 (MSA-subsampled/clustered), AlphaFlow/ESMFlow, or an ensemble emulator for state sampling; OpenMM with enhanced sampling (metadynamics/replica exchange) for switching and populations, with explicit acknowledgment of force-field/sampling limits (import A13's protocol and caveats); SCA/normal-mode analysis for coupling hypotheses. Calibrate population/switch predictors on the frozen set and report calibration on held-out designs.

**Failure modes to expect and report.** (i) *Single-structure mis-targeting* - pipelines and metrics that quietly optimize one state; guard by always evaluating both states and the gap. (ii) *Population inaccuracy* - in-silico populations/barriers that are not trustworthy free energies (the A13 problem); never present them as measured. (iii) *Self-consistency inflation* - high re-prediction confidence for one state read as ensemble success. (iv) *Collapse* - designs that in reality populate only one state despite a designed gap. (v) *Denominator hiding* - one working switch is not a capability without the tested count.

## 7. Verification and auditability requirements

1. **Leakage-safe evaluation.** Any design/protein used to build a metric is excluded from its evaluation; the frozen precedent set and splits are committed (hashed) before scoring; no tuning on the test design. Both states and the gap are always evaluated, never one state alone.
2. **Calibrated uncertainty.** Every delivered design carries calibrated predictions of population ratio and switch magnitude/direction; calibration is reported on held-out designs. **Every design is a labeled hypothesis about an ensemble, not a measured switch.**
3. **Separation of in-silico filters from real validation.** Multistate self-consistency, sampled populations, and MD barriers are kept physically separate from any measured populations/switching; no in-silico population is presented as a measured \(\Delta G\).
4. **Ensemble honesty.** Any in-silico population or barrier is reported with the explicit caveat that force-field/sampling accuracy for ensembles is itself unresolved (cross-reference A13); single-structure confidence is never presented as ensemble evidence.
5. **Independent reproduction.** A standalone script recomputes all in-silico metrics from committed inputs and model hashes; SHA-256 manifest over designs, state models, code, scores, and (if any) assay data.
6. **Preservation.** Design code, model/force-field versions, state definitions, and sampling protocols are part of the record. Anything not preserved is stated explicitly.
7. **Honest reporting.** The report states up front that the problem is reality-gated and NOT resolved; that *per-design real success rates are low* and that ensemble/allostery-by-design remains open because generators and in-silico populations target single structures; and it never presents a single-state, self-consistent design as a validated switch.
