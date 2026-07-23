# PROMPT FOR MEMBRANE-PROTEIN STRUCTURE IN NATIVE LIPID ENVIRONMENTS

## Predicting the lipid-coupled conformational state, not the detergent artifact

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** B - reality-gated (empirical verifier)
**Rank:** B-14 of 29
**Source:** chem/bio top-50 list #20, section C (beyond static structure)
**Modes:** `[struct]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

A third of the proteome and most drug targets are membrane proteins, yet most of their solved structures were determined in detergent - a non-native environment that can distort conformational state, oligomerization, and lipid contacts. AlphaFold-lineage models predict the transmembrane fold well but were trained largely on those detergent structures and treat the protein as if the membrane did not exist: they miss lipid-dependent conformational states, annular and structural lipid-binding sites, insertion depth and tilt, and the native oligomeric state. The scientifically important, and unsolved, quantity is the **lipid–conformation coupling**: which state a membrane protein adopts *in its native bilayer*, and where the functionally relevant lipids sit. This is **reality-gated** - the ground truth is an experimental structure determined in a near-native environment (cryo-EM in nanodiscs, SMALPs, or native membranes; native mass spectrometry for stoichiometry and lipid binding), and that corpus is small and hard to grow. Compute (AF-lineage models, coarse-grained MD, AF+CG hybrids) can advance the fold and propose lipid contacts; it cannot certify a native-environment state without new physical experiment. The honest deliverable is a certified method for native-state / lipid-contact prediction, a held-out benchmark on a leakage-safe split, and falsifiable predictions for a cryo-EM partner - never a claim that membrane-protein structure is "done."

## 1. Exact problem statement

**Input.** The sequence(s) of a membrane protein (with MSA), the membrane topology where known, and a declared **lipid/environment context** (bilayer composition, presence of specific lipids such as cholesterol/PIP₂/cardiolipin). MSA-based and single-sequence tracks are scored separately.

**Output.** A ranked ensemble of full-atom models, each with **calibrated confidence**, annotated with: (i) the predicted membrane-embedded **conformational state** (for multi-state proteins, which state); (ii) predicted **lipid-binding sites** (residues contacting structural/annular lipids); (iii) **membrane placement** (insertion depth and tilt relative to the bilayer normal); and (iv) the native **oligomeric state**.

**Metrics.** Fold accuracy by TM-score / lDDT to the native. Beyond fold - the metrics that capture the open gap:
- **State accuracy:** for proteins with multiple lipid-dependent experimental states $\{X^{(a)}\}$, whether the model matches the *native-environment* state,
$$\text{state-correct} = \big[\arg\max_a \mathrm{TM}(\hat X, X^{(a)}) = a^\star_{\text{native}}\big].$$
- **Lipid-site recovery:** precision/recall (or MCC) of predicted vs. experimentally resolved lipid-contacting residues.
- **Placement error:** deviation in insertion depth ($\Delta z$, Å) and tilt angle (degrees) vs. OPM/PPM reference.
- **Oligomer accuracy:** correct native stoichiometry.

**Population.** Non-redundant membrane proteins (α-helical and β-barrel classes reported separately), stratified by determination environment (detergent vs. nanodisc/SMALP/native), and by whether multiple lipid-dependent states are known. A metric without its environment stratum is uninformative here, because the detergent-vs-native distinction is the whole point.

**Compute-tractable sub-question.** On a frozen, homology- and time-separated split of *near-native-environment* structures, predict state, lipid sites, placement, and oligomer better than a detergent-biased AF baseline, with calibrated confidence.

**Empirically-gated whole.** Predict the conformational state and functional lipid interactions of a membrane protein *in a real bilayer* whose native-environment structure is unknown - verifiable only by new cryo-EM/native-MS, never by simulation alone.

## 2. Verifier and data

**Ground-truth source.**
- **PDB** - membrane-protein structures, with the resolved lipid/detergent molecules and (for cryo-EM) the sample environment recorded.
- **EMDB** - cryo-EM maps, including nanodisc/SMALP reconstructions that carry native-environment evidence.
- **OPM** (Orientations of Proteins in Membranes; Lomize et al.) and **PDBTM** - curated membrane placement (insertion depth, tilt) and topology; the placement ground truth.
- **mpstruc** (Stephen White lab) - curated database of membrane-protein structures with method/environment annotation.
- **MemProtMD** (Sansom lab; verify) - coarse-grained (and atomistic) MD of membrane proteins in bilayers; a *simulation* reference for annular-lipid patterns, used as a prior/feature, **not** as experimental truth.
- **Native mass spectrometry** datasets (Robinson lab and others; verify curated resource) - lipid-binding stoichiometry and oligomeric state.

**Frozen split (leakage-safe).** The test set is fixed before modeling under **fold/homology clustering** (no test protein sharing a family with training) intersected with a **time split** (deposition-date cutoff). Crucially, it also carries an **environment axis**: a held-out set of *nanodisc/SMALP/native* structures is reserved to test whether a model trained on the detergent-heavy corpus can predict native-environment states - the core generalization question. Split, cluster, and environment manifests are committed and hashed before any test number. MemProtMD-derived features must be recomputed only from training-side structures to avoid leaking test placements.

**Wet-lab gate (mandatory).** A native-environment structure or lipid-coupled state **cannot be established by computation**. It requires cryo-EM in a near-native environment (nanodiscs, SMALPs/polymer-encapsulated native membranes, or in-situ cryo-ET), and/or native mass spectrometry for lipid-binding stoichiometry and oligomeric state; functional confirmation of a lipid dependence needs reconstitution and activity assays. A single-particle cryo-EM structure in nanodiscs is typically many months of effort, roughly \$100k–\$500k including sample optimization, and multi-state or low-abundance targets are harder still. Molecular-dynamics simulation - however physically motivated - is a hypothesis generator, not a verifier; a force field is not a bilayer. This gate is not softenable.

## 3. Standard of a genuine advance

A genuine advance is one of:
1. A **certified method contribution** - a model that, on the held-out *native-environment* split, predicts state, lipid-binding sites, membrane placement, and/or oligomeric state significantly better than a detergent-biased AF baseline, at matched compute, with calibrated confidence validated on held-out data.
2. A **falsifiable, ranked prediction set** - for membrane proteins under active cryo-EM/native-MS determination, predicted native states + lipid sites + oligomeric states, registered before results, with pre-committed accuracy claims, ready for a structural partner.

**Not accepted as resolution:**
- A **leaderboard TM/lDDT treated as a guarantee** of the native-environment state - high fold accuracy on detergent structures says nothing about lipid coupling.
- **In-silico "validation"** - agreement with a coarse-grained MD simulation, MemProtMD annular-lipid patterns, or a second predictor is a hypothesis, not experimental confirmation.
- A **corpus-overfit metric** - accuracy driven by the detergent-heavy training mass and by homology to solved folds, that collapses on the native-environment held-out set; lipid-site "recovery" tuned on the same structures it is scored against.
- Reporting the fold as "solved" while the lipid-dependent state, placement, and oligomer - the actual open gap - are unaddressed.

## 4. Graded targets

**P1 - Reproduce a SOTA baseline.** Run AlphaFold2/AF3 (and OPM/PPM placement) on the frozen split; reproduce fold-accuracy and quantify the baseline's *state/lipid blindness* (where it returns a detergent-like state or misses resolved lipids). *Evidence:* committed split hashes, independent TM/placement/lipid scorers, environment-stratified tables.

**P2 - Calibrated confidence.** Validate model confidence as a predictor of realized fold and state accuracy on held-out data, per environment stratum. *Evidence:* reliability curves, expected calibration error.

**P3 - Certified method contribution.** A modeling change - lipid-context conditioning, AF+coarse-grained hybrid refinement, a lipid-site prediction head, multi-state generation - that significantly improves state/lipid/placement/oligomer accuracy on the *native-environment* held-out set over P1. *Evidence:* paired per-target deltas with confidence intervals, ablations, no test-set tuning.

**P4 - New held-out SOTA.** Best-in-class native-environment state, lipid-site, placement, and oligomer prediction on the committed split, at one-GPU-feasible inference. *Evidence:* full distributions, split manifests, independent reproduction.

**P5 - Wet-lab-ready prediction set.** A ranked, calibrated slate of native-state / lipid-site / oligomer predictions for membrane proteins under active cryo-EM/native-MS determination, registered before results, with a pre-committed falsifiable claim and honest post-hoc accounting including misses. The machine's ceiling; cryo-EM closes the loop.

## 5. Known results and prior art

- **AlphaFold2 / AlphaFold3** - Jumper et al. (2021); Abramson et al. (2024) - accurate transmembrane folds, but trained on a detergent-heavy corpus and lipid-agnostic; miss lipid-dependent states and functional lipid sites. **Re-verify state/lipid behavior on our native-environment split.**
- **OPM / PPM** - Lomize et al. - membrane placement (insertion depth, tilt) reference and predictor; the placement ground truth and baseline.
- **MemProtMD** - Stansfeld, Sansom et al. - large-scale coarse-grained (CG-MARTINI) MD of membrane proteins in bilayers; annular-lipid fingerprints as a prior/feature (a *simulation* reference, not experimental truth). **verify.**
- **mpstruc / PDBTM** - White lab; Tusnády et al. - curated membrane-protein structure resources with method/environment annotation.
- **Native mass spectrometry** - Robinson and collaborators - lipid-binding stoichiometry and oligomeric state in near-native conditions.
- **AF + CG / MD hybrids** - a growing line embedding AF models into bilayers and refining with coarse-grained or atomistic MD to recover lipid contacts and state (verify specific methods/years).
- **Lipid-dependent-state systems** - mechanosensitive channels (MscL/MscS), Kir/PIP₂-gated channels, cholesterol-modulated GPCRs, cardiolipin-dependent respiratory complexes - the functional anchors for lipid–conformation coupling.

*Status as of mid-2026 - re-verify against current literature before starting any session.* Check whether any AF-lineage or hybrid method has demonstrated *native-environment* state prediction validated against nanodisc/native cryo-EM on a leakage-safe split; the lipid-coupling gap is, as of writing, open.

## 6. Attack plan

**Data.** Assemble membrane-protein structures from the PDB with environment annotation (detergent vs. nanodisc/SMALP/native) from mpstruc/EMDB; pull OPM/PPM placements; cluster by fold/homology; commit a fold-cluster ∩ time split with a reserved **native-environment** held-out set. Derive annular-lipid priors from MemProtMD *training-side only*. Freeze and hash before modeling.

**Baselines.** AF2/AF3 folds, OPM/PPM placement, a CG-MD (MARTINI) refinement pipeline. Score TM/lDDT, state, lipid-site MCC, placement error, oligomer with independent scorers.

**Model.** Candidate contributions: (i) **lipid-context conditioning** (bilayer composition / specific lipids as input); (ii) an **AF + coarse-grained hybrid** that embeds the predicted fold in a bilayer and refines toward a lipid-coupled state; (iii) a **lipid-binding-site head** trained on resolved lipids; (iv) **multi-state generation** to expose lipid-dependent alternatives and rerank by native-environment evidence.

**Calibration.** Validate confidence against realized fold and state accuracy on held-out data, per environment stratum; report expected calibration error.

**Compute.** AF-lineage inference/fine-tuning and CG-MARTINI refinement are one-prosumer-GPU feasible (CG is cheap; atomistic MD is the expensive tail and is optional). The bottleneck is native-environment data, not compute.

**Failure modes.** (i) **Detergent bias / distribution shift** - training on detergent structures, testing on native environment; the central risk. (ii) **Data scarcity** - few multi-state and few native-environment structures. (iii) **Leakage** - fold homology to solved proteins inflates TM; MemProtMD features leaking test placements; strict separation required. (iv) **Verifier trap** - MD agreement is not experimental truth; a biased force field yields confident-but-wrong native states.

## 7. Verification and auditability requirements

1. **Leakage-safe evaluation.** Fold-cluster **and** time separation committed and hashed before evaluation, with a reserved native-environment held-out set; MSA/single-sequence tracks scored separately; simulation-derived features computed only from training-side structures; no test-set tuning.
2. **Calibrated uncertainty.** Every prediction (fold, state, lipid sites, placement, oligomer) carries calibrated confidence; calibration is reported on held-out data per environment stratum.
3. **Independent reproduction.** TM/lDDT, state accuracy, lipid-site MCC, placement error, and oligomer accuracy are recomputed by standalone scorers separate from training code, from committed splits and predictions.
4. **Cryptographic manifest.** A SHA-256 manifest covers split and environment definitions, data version hashes, model code, weights, MemProtMD-feature provenance, and every predicted structure and annotation.
5. **Preservation.** Training/fine-tuning and hybrid-refinement code, weights, force-field/CG configuration, and dataset version hashes are part of the record; anything not preserved is stated explicitly.
6. **Prospective-prediction registry.** Any native-state / lipid-site prediction handed to a partner (P5) is timestamped and registered with confidence and a pre-committed accuracy claim before results, and scored afterward including misses.
7. **Honest reporting.** The report states up front that native-environment membrane-protein structure is reality-gated and **not resolved**; separates in-silico metrics and MD agreement from experimental confirmation; labels every native-state and lipid prediction a wet-lab-pending hypothesis; and never presents a fold-accuracy number as a guarantee of the lipid-coupled state.
