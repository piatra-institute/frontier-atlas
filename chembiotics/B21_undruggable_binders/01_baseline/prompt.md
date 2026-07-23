# PROMPT FOR RELIABLE DE NOVO BINDERS AGAINST FLAT, "UNDRUGGABLE" INTERFACES

## Designing protein binders to featureless epitopes on transcription factors and RAS-family targets

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** B - reality-gated (empirical verifier)
**Rank:** B-21 of 29
**Source:** chem/bio top-50 list #27, section D (design)
**Modes:** `[gen]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

De novo protein binder design has advanced from a heroic effort to a semi-routine pipeline (diffuse a backbone against a target epitope, design the sequence, filter by structure re-prediction, test) - yet the per-attempt success rate is still low, and it is lowest exactly where the medical need is highest: **flat, featureless "undruggable" interfaces** on transcription factors and RAS-family GTPases, which offer no deep pocket and few hydrophobic hotspots for an interface to grip. The objective is *reliable* de novo binders against such targets at a chosen epitope, with high affinity and specificity. This is a **reality-gated** problem: binding is a biophysical measurement (SPR/BLI/display), not an in-silico score, so the honest deliverable is a certified method contribution, an improved success-rate proxy on a held-out target, and a small ranked calibrated set of falsifiable binder designs - never a claimed resolution. In-silico interface metrics correlate with success only weakly, and their pass rates systematically overstate the real hit rate.

## 1. Exact problem statement

**Design target.** Given a target protein of known (or confidently predicted) structure and a *specified epitope* - typically a flat surface patch chosen for its biological relevance (e.g. a protein–protein interaction face, a RAS effector-binding surface) - output de novo protein sequences (mini-proteins, typically 50–150 aa) predicted to bind at that epitope.

**Success metric (the whole problem).**
- **Hit rate:** fraction of designs, from an unbiased ordered list, that show measurable binding in a biophysical assay. This is the headline number; on flat epitopes it is often single-digit percent.
- **Affinity:** equilibrium dissociation constant \(K_D\) (target: nM or tighter for a useful binder), from SPR/BLI.
- **Specificity / epitope correctness:** binding at the intended surface (competition, mutational epitope mapping), not an off-target patch.
- Plus expression/solubility and, for the strongest claim, a co-structure.

**Target class.** One target + one epitope per campaign, drawn from the "undruggable" flat-interface class (a transcription factor DNA-binding or dimerization surface; a RAS-family effector interface). Generality across targets is not assumed; flat epitopes are the explicit difficulty.

**The in-silico-scorable sub-question (separable).** Independent of the wet lab, one can score: does a diffused, sequence-designed binder (a) re-predict as a confident complex (AF2/AF3 ipTM, interface-pAE / pAE_interaction, pLDDT); (b) bury the intended hotspot residues; (c) score well by Rosetta interface ddG and shape complementarity. These are computable *filters*. **They are not binding.** The reliability gap lives in the difference between a design that passes every interface filter and one that actually engages a flat surface with measurable affinity - a gap widest precisely where hotspots are scarce.

## 2. Verifier and data

**In-silico oracles and filters (and their known unreliability).**
- **RFdiffusion target-conditioned binder generation** (optionally hotspot-conditioned) - diffuses backbones docked against the epitope. *Unreliable because* geometric complementarity to a flat surface is easy to draw and hard to make energetically real; the model has no direct affinity signal.
- **ProteinMPNN sequence design** for the diffused backbone. *Unreliable because* a well-packed, foldable sequence need not translate to interface affinity.
- **AF2 / AF3 complex re-prediction - interface-pAE and ipTM filters.** The standard success proxy. *Unreliable because* these metrics are trained/optimized for structure agreement, correlate only moderately with binding, and are known to be gameable; a design can clear the ipTM/pAE thresholds and not bind. **The in-silico pass rate is much higher than the real hit rate - often by an order of magnitude.**
- **Rosetta interface ddG / shape complementarity / SASA buried.** *Unreliable because* score-function affinity is not measured affinity, especially on flat, polar interfaces.
- **Hotspot targeting.** Concentrating the interface on predicted energy hotspots raises success on *pocketed* targets; on genuinely flat epitopes the hotspots may not exist, which is the crux.

**Frozen benchmark / precedent set.** A fixed set of *published* de novo binder campaigns with reported per-target experimental hit rates and affinities (see §5), committed before modeling. Reproducing their in-silico filter statistics and their *reported* hit rates is the leakage-controlled baseline. Where possible, include at least one genuinely flat/undruggable target to avoid the easy-pocket bias.

**Wet-lab gate (mandatory).** Binding cannot be established without new physical experiments: gene synthesis, expression (or on-yeast/on-phage display), and biophysical measurement - SPR or BLI for \(K_D\), or yeast/phage display for enrichment and affinity maturation, plus epitope-mapping controls. Rough cost: soluble expression + SPR/BLI on a handful of designs is on the order of \$1k–\$5k per design carried to clean kinetics; a display-based screen of a large designed library (build, sort, deep-sequence) is a defined campaign in the \$10k–\$50k range plus weeks of work; a co-crystal or cryo-EM structure to confirm the epitope is a separate major cost. **This line is not optional and must not be softened: passing every interface filter is a hypothesis about binding, not a measured \(K_D\).**

## 3. Standard of a genuine advance

A genuine advance is one of: (a) a **certified method contribution** - a binder-design/filter pipeline that, on the frozen precedent set, predicts per-target experimental hit rate better than a named baseline (e.g. raw ipTM), reproduced independently; (b) an **improved success-rate proxy on a held-out target** - a filter that raises the confirmed-binder fraction, validated on a target withheld from its construction, ideally a flat one; or (c) the top target: a **small, ranked, calibrated, expressible, falsifiable binder set** for one specified flat epitope, each design carrying a calibrated probability of binding and a predicted affinity class, handed to a wet-lab partner with pre-registered success criteria.

**Not accepted as resolution.**
- An in-silico "binder" - high ipTM, low interface-pAE, good ddG - presented as a binder. It is a hypothesis; only SPR/BLI/display makes it a binder.
- **AF2/AF3 interface confidence reported as affinity or as a binding guarantee.** Confidence is not \(K_D\).
- A high hit rate demonstrated only on easy, pocketed targets, presented as solving the flat/undruggable case.
- A binder confirmed at an *unintended* epitope, credited as hitting the specified surface.
- Retrospective enrichment of known binders presented as prospective design success.
- A single lucky binder from an unreported large pool presented as a reliable success rate; the denominator (designs ordered/tested) must be stated.

## 4. Graded targets

**P1 - Reproduce a published binder pipeline's in-silico metrics.** Rebuild an RFdiffusion → ProteinMPNN → AF2/AF3-filter pipeline and reproduce the reported filter statistics (ipTM/pAE distributions, filter pass rates) on a published campaign. *Certificate:* metrics within noise; committed code and hashes.

**P2 - Certified prediction of experimental hit rate on the frozen set.** Show the filter stack predicts *measured* per-target hit rate across the frozen precedent set better than a named baseline, with an honest correlation and confidence interval - including at least one flat target. *Certificate:* frozen set, frozen scores, independent recomputation.

**P3 - Improved success proxy on a held-out flat target.** Build a filter/ranking that raises the confirmed-binder fraction and validate it on a flat epitope withheld from construction; report the lift and the calibration curve. *Certificate:* held-out split fixed before scoring.

**P4 - A ranked, calibrated, falsifiable binder set for one flat epitope (top target).** For a single specified undruggable target + epitope, deliver ≤ 24 designs, ranked, each with a calibrated binding probability, a predicted affinity class, expression notes, and a pre-registered success criterion (e.g. "≥ 2 of the top 12 bind with \(K_D < 1\,\mu\mathrm{M}\) at the intended epitope"). *Certificate:* frozen design set + calibration model committed before any assay; wet-lab partner named.

**P5 - Prospective wet-lab confirmation with honest calibration.** Only with a lab: the P4 set expressed/displayed and assayed, reporting the realized hit rate against the pre-registered criterion, the affinity distribution, epitope-mapping results, and the calibration error - including, plainly, if the per-design real success rate was low. *Certificate:* raw SPR/BLI or sort/sequencing data, the frozen predictions predating them.

## 5. Known results and prior art

- Cao et al. (2022, Nature) - de novo mini-binders against a panel of targets using Rosetta rotamer-interaction-field docking and large-scale screening; established realistic (single-digit to low-tens percent) per-target hit rates.
- RFdiffusion binder design (Watson et al., 2023, Nature) and follow-ups improving hit rates and enabling target/hotspot conditioning (Bennett et al., 2023; Torres et al., verify authors/years).
- BindCraft (Pacesa et al., 2024, verify) and AlphaProteo (Google DeepMind, 2024, verify) - pipelines reporting substantially higher experimental hit rates on several targets; check the target set, whether flat/undruggable epitopes are included, and the reported reliability - these raise the bar but do **not** establish general reliability on flat interfaces.
- ProteinMPNN (Dauparas et al., 2022) for sequence design; AF2/AF-Multimer and AF3 (Jumper et al., 2021; Abramson et al., 2024, verify) as the re-prediction/filter oracles; the interface-pAE / ipTM filtering convention.
- The consistent finding: hit rates are real but modest, are inflated by in-silico filters, and are lowest on **flat, hotspot-poor epitopes** - the RAS-family and transcription-factor surfaces named here. Static binder-to-pocketed-target design is closer to routine than binder-to-flat-surface design.

*Status as of mid-2026 - re-verify against current literature before starting any session.*

## 6. Attack plan

**Datasets/inputs.** Pull the frozen precedent set (targets, epitopes, published designs, and reported hit rates/affinities), plus target structures (experimental or confidently predicted). Fix a leakage-safe split: any target used to build a filter is held out of its evaluation; keep a flat/undruggable target in the held-out set.

**Pipeline (one prosumer GPU suffices for the neural stages).** RFdiffusion (target/hotspot-conditioned) for backbones; ProteinMPNN for sequence; AF2/AF-Multimer or AF3 (or Boltz) for complex re-prediction and interface metrics; Rosetta for interface ddG / shape complementarity where used. Calibrate a binding-probability model on the frozen set and report calibration on held-out targets. Sample generously and filter hard, but track the denominator.

**Failure modes to expect and report.** (i) *Self-consistency / interface-confidence inflation* - ipTM/pAE pass rates far above the real hit rate; report both, separately. (ii) *Flat-epitope failure* - designs default toward any nearby pocket or edge rather than the specified flat patch; monitor epitope adherence explicitly. (iii) *Expression failure* - unexpressed designs yield no data regardless of scores. (iv) *Off-target binding* - a confirmed binder at the wrong epitope is not a success for the specified target. (v) *Denominator hiding* - a good hit rate is meaningless without the number of designs tested.

## 7. Verification and auditability requirements

1. **Leakage-safe evaluation.** Any target/epitope used to build a filter is excluded from its evaluation; the frozen precedent set and all splits are committed (hashed) before scoring; no tuning on the test target. The denominator (designs generated, filtered, ordered, tested) is always reported.
2. **Calibrated uncertainty.** Every delivered design carries a calibrated binding probability and a predicted affinity class; calibration is reported on held-out targets. **Every design is a labeled hypothesis, not a claimed binder.**
3. **Separation of in-silico filters from real validation.** The report keeps in-silico interface metrics (ipTM, interface-pAE, ddG) physically separate from any wet-lab affinity; no in-silico confidence is ever presented as \(K_D\) or as a binding guarantee.
4. **Independent reproduction.** A standalone script recomputes all in-silico metrics from committed inputs and model hashes; SHA-256 manifest over designs, code, scores, and (if any) assay data.
5. **Preservation.** Generation/design code, model versions/checkpoints, target/epitope definitions, and filter settings are part of the record. Anything not preserved is stated explicitly.
6. **Honest reporting.** The report states up front that the problem is reality-gated and NOT resolved; that *per-design real success rates are low, especially on flat/undruggable epitopes*; and that recent high-hit-rate pipelines do not establish general reliability on this class. No in-silico "binder" is presented as a binder.
7. **Epitope and specificity disclosure.** Any binding claim states the epitope it was mapped to and the specificity controls run; binding at an unintended surface is reported as such, not as target engagement.
