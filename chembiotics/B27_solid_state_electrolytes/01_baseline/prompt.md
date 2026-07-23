# PROMPT FOR SOLID-STATE ELECTROLYTE DISCOVERY UNDER THE JOINT FUNCTIONAL-DEVICE CONSTRAINT

## Crystals that are simultaneously stable, ion-conducting, synthesizable, and interface-compatible - the post-GNoME synthesis gap

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** B - reality-gated (empirical verifier)
**Rank:** B-27 of 29
**Source:** chem/bio top-50 list #33, section D (design)
**Modes:** `[gen]` `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Large-scale machine-learning screening (GNoME) expanded the catalogue of predicted-stable inorganic crystals by an order of magnitude, and generative models (MatterGen-class) now propose novel compositions on demand. This reframed, rather than solved, the materials problem: the bottleneck moved downstream to the **joint functional-device constraint set** and the **prediction-to-synthesis gap**. A working solid-state electrolyte must satisfy *several* properties *at once* - thermodynamic (and kinetic) stability, high ionic conductivity, a wide electrochemical stability window, chemical/mechanical compatibility with both electrodes, and above all **synthesizability by a real route** - and predicted-stable is not synthesized, while a good in-silico conductivity is a proxy, not a measurement. The central post-GNoME lesson is that a pile of hypothetically stable structures is not a pile of materials: autonomous-lab and follow-up analyses found many predicted "novel" compounds to be known, disordered, or unmakeable. Compute can *advance* this - screen, rank, and generate candidates with jointly predicted properties and calibrated uncertainty - but it cannot *close* it: only synthesis and electrochemical characterization decide. This item is **reality-gated**. The honest deliverable is a certified screening/generation method, a held-out benchmark on experimentally measured properties, and a ranked, calibrated, synthesizability-scored candidate slate for an experimental partner - never a claim that solid-state-electrolyte discovery is "solved."

## 1. Exact problem statement

**Input.** A chemical search space (composition families and prototype structures for a mobile ion, primarily Li⁺, optionally Na⁺/K⁺/Mg²⁺), or a generative target specification (desired conductivity/stability window). Auxiliary inputs: a machine-learning interatomic potential (MLIP), a phase-diagram reference set, and declared operating conditions (temperature, contacting electrode chemistries).

**Output.** A ranked set of candidate crystals, each carrying **jointly predicted** properties with **calibrated uncertainty**:
- thermodynamic stability (energy above the convex hull, $E_{\text{hull}}$);
- room-temperature ionic conductivity $\sigma$ (S cm⁻¹) and activation energy $E_a$ from MLIP/AIMD diffusion;
- electrochemical stability window from grand-potential phase diagrams;
- interfacial compatibility (predicted decomposition energetics against named electrodes);
- a **synthesizability score** with a proposed precursor route.

**Metrics.** For property regression against experiment: mean absolute error in $\log_{10}\sigma$ (conductivity spans orders of magnitude, so log-error is the decision-relevant quantity), MAE in $E_a$ (eV) and in stability-window bounds (V). For screening: enrichment / precision@$k$ of experimentally confirmed superionic conductors within the top-$k$ ranked list. For synthesizability: agreement with known-synthesizable vs. never-made labels, and - prospectively - the fraction of top candidates a partner can actually make. For generation: validity, novelty (checked against ICSD/Materials Project, not just the training set), and fraction of generated candidates that survive the full joint filter. A metric is meaningful only with its population and split.

**Population.** Performance is claimed over a named population - e.g. Li-ion solid electrolytes across sulfide, oxide (garnet, NASICON, perovskite), halide, and argyrodite families - stratified by family and by novelty relative to the training crystals. Aggregate numbers pooled across families are not accepted.

**Compute-tractable sub-question (in-silico).** Given a frozen, leakage-safe split of experimentally measured conductivities/stabilities, produce jointly predicted properties whose held-out log-conductivity MAE / stability MAE / screening enrichment meets or beats a named SOTA, with calibrated uncertainty - *within the chemistry the data covers* - and produce novel generated candidates that pass the full joint in-silico filter.

**Empirically-gated whole.** Produce a *new* solid electrolyte - a composition/structure not previously synthesized - that is actually made and measured to have the target conductivity, stability window, and interfacial behavior. No amount of compute, no MLIP diffusivity, no convex-hull number closes this; only synthesis and electrochemical characterization do.

## 2. Verifier and data

**Ground-truth source.**
- **Materials Project** (Jain et al., ~2013) - DFT formation energies, phase diagrams, and structures; the in-silico stability reference.
- **GNoME dataset** (Merchant, Cubuk et al., *Nature* 2023) - ML-predicted stable structures and their DFT-relaxed energies; a candidate pool, **not** an experimental verifier.
- **ICSD** (Inorganic Crystal Structure Database, access-gated) - experimentally realized crystal structures; the reference for "has this ever actually been made?"
- **Experimental ionic-conductivity compilations** (verify) - curated datasets of measured room-temperature conductivities and activation energies for solid electrolytes (e.g. Sendek-style screening compilations and later aggregations); these, not computed diffusivities, are the conductivity ground truth.
- **AIMD / MLIP-MD diffusion data** - computed conductivities via MLIPs (M3GNet, CHGNet, MACE) or ab-initio MD; explicitly **in-silico proxies** to be validated against experiment.
- **The Materials Project electrochemical-stability and interface-reaction tooling** (Ong/Ceder-lineage grand-potential and interfacial-reaction methods) for window and compatibility estimates.

**Frozen split (leakage-safe).** For property prediction, the test set is fixed before modeling under **composition/structure-family separation**: cluster by chemical family and structural prototype and hold out entire clusters, so no test electrolyte shares a family/prototype with training. Where records are time-stamped (publication date of a measured conductivity), add a **time split**. Random splits over a family-clustered dataset inflate scores and are reported only as an interpolation upper bound. For generation, novelty is assessed against **ICSD and Materials Project**, not merely against the model's training set, to avoid rediscovering known compounds as "novel." Split and cluster manifests are committed and hashed before any test number.

**Wet-lab gate (mandatory).** A predicted-stable structure with a good computed conductivity **is not a material**. Establishing a candidate requires physical **synthesis** (solid-state, mechanochemical, or solution routes - many predicted compositions never form the target phase, forming known or disordered products instead) and **electrochemical characterization**: X-ray/neutron diffraction for phase confirmation, AC electrochemical impedance spectroscopy for conductivity, and cell cycling for window and interfacial stability. A single candidate's synthesis-and-characterization campaign costs roughly \$20k–\$100k and weeks to months, with a substantial failure-to-form rate. This gate is the whole point of the item: the **prediction-to-synthesis gap** is the open problem, and it is closed only in the lab.

## 3. Standard of a genuine advance

A genuine advance is one of:
1. A **certified method contribution** - a screening or generative pipeline that achieves a *new held-out result* on **experimentally measured** conductivity/stability (better log-$\sigma$ MAE, stability MAE, or top-$k$ enrichment on a family-separated split), *or* a synthesizability predictor that measurably improves the hit rate of makeable candidates, with the improvement holding on novel families and with calibrated uncertainty validated on held-out data.
2. A **calibrated, falsifiable candidate slate** for an experimental partner: a ranked list of novel compositions/structures with jointly predicted properties, per-candidate calibrated uncertainties, a synthesizability score, and a proposed route, registered before synthesis, with a pre-committed claim (e.g. "≥ $k$ of top-$n$ form the target phase and exceed $10^{-4}$ S cm⁻¹").

**Not accepted as resolution:**
- A **convex-hull or MLIP-diffusivity number treated as a real-world guarantee** - predicted-stable is not synthesized, and a computed conductivity is a proxy, not a measurement.
- A **generated-candidate count** ("N novel stable structures") presented as discovery - novelty checked only against a training set, or against DFT stability alone, is the exact post-GNoME failure mode; many such candidates are known, disordered, or unmakeable.
- **In-silico-only "validation"** - agreement between two DFT functionals, or between an MLIP and AIMD, is not experimental confirmation.
- A candidate that optimizes one property (e.g. conductivity) while silently failing another constraint (window, interfacial stability, synthesizability); the constraint set is **joint**.
- "Solved solid-electrolyte discovery" claimed from any in-silico screen.

## 4. Graded targets

**P1 - Reproduce a SOTA baseline on our verified pipeline.** Reproduce (a) a stability/property predictor (MLIP formation energies vs. Materials Project; a conductivity regressor vs. an experimental compilation) and (b) an MLIP-MD conductivity estimate for a known superionic conductor (e.g. Li₁₀GeP₂S₁₂, argyrodite Li₆PS₅Cl, garnet Li₇La₃Zr₂O₁₂) against measured values, on our frozen family-separated split. *Evidence:* committed split hashes, independent scoring, per-family tables. Independently valuable as a leakage-audited baseline.

**P2 - Calibrated uncertainty and joint filtering.** Attach calibrated uncertainty to each predicted property and compose the **joint** filter (stability ∧ conductivity ∧ window ∧ interface ∧ synthesizability), reporting how many candidates survive all constraints and the calibration of each property head on held-out data. *Evidence:* reliability curves per property, joint-survival statistics, per-family strata.

**P3 - Certified method contribution.** A modeling advance - better MLIP for Li diffusion, a synthesizability model that raises makeable-hit rate, a generative model conditioned on the joint constraint set - that yields a *statistically significant, leakage-audited* improvement over P1 on novel families. *Evidence:* paired per-material deltas with confidence intervals, ablations, novelty checked against ICSD/MP, no test-set tuning.

**P4 - New held-out SOTA / novel validated candidates in-silico.** Best-in-class on the committed family- and time-separated split across the joint property set, and a generated slate whose members are novel against ICSD/MP and survive the full in-silico filter. *Evidence:* full error distributions, split and novelty manifests, independent reproduction from committed code.

**P5 - Synthesis-ready candidate slate.** A ranked, calibrated, synthesizability-scored slate of novel electrolyte candidates with proposed routes, registered before synthesis with a partner (or an autonomous lab), with a pre-committed falsifiable claim on phase formation and conductivity. *Evidence:* timestamped registration, post-hoc scoring against synthesis + impedance data, honest accounting of failures-to-form and off-target phases. This is the ceiling the machine reaches; closing the synthesis gap is the lab's job.

## 5. Known results and prior art

- **GNoME** - Merchant, Batzner, Schoenholz, Aykol, Cheon, Cubuk (*Nature* 2023): deep-learning-driven expansion of predicted-stable inorganic crystals (~380k on-hull); the defining large-scale screen and the origin of the synthesis-gap debate.
- **Post-GNoME synthesis-gap critiques** - Cheetham & Seshadri (~2024, *Chem. Mater.*, verify) and follow-up analyses (Leeman, Persson et al., verify) questioning the novelty/synthesizability of ML-predicted compounds; the autonomous-lab **A-Lab** (Szymanski et al., *Nature* 2023) and the ensuing scrutiny of its "new" materials. The central cautionary literature for this item.
- **Universal MLIPs** - M3GNet (Chen & Ong, ~2022), CHGNet (Deng et al., ~2023), MACE (Batatia et al., ~2022) - force fields enabling large-scale relaxation and MD-based diffusion screening.
- **MLIP-driven conductivity screening** - Ong/Ceder/Mo-lineage AIMD and MLIP-MD studies of Li superionic diffusion (activation energies, room-temperature $\sigma$ extrapolation); LGPS/argyrodite/garnet/NASICON literature.
- **Holistic conductor screening** - Sendek, Cubuk, Reed et al. (~2017–2019, *Energy Environ. Sci.*): data-driven screening of thousands of Li-containing candidates for conductivity.
- **Interface / window computation** - Richards, Miara, Ceder et al. (~2016, *Chem. Mater.*): grand-potential interfacial-reaction energetics for solid-electrolyte/electrode stability.
- **Generative materials** - MatterGen (Zeni et al., Microsoft, ~2024–2025, verify): diffusion generation of inorganic crystals with property targeting; CDVAE and successors.
- **Data infrastructure** - Materials Project (Jain et al., ~2013); ICSD; OQMD; experimental conductivity compilations (verify).

*Status as of mid-2026 - re-verify against current literature before starting any session.* This area moves fast; re-verify whether newer MLIPs, generative models, or autonomous-lab campaigns have narrowed the prediction-to-synthesis gap, and confirm the access terms and provenance of every conductivity compilation before use.

## 6. Attack plan

**Data.** Pull Materials Project structures/energies, the GNoME candidate pool, an experimental conductivity compilation, and ICSD reference labels. Build family/prototype clustering; commit a **family-separated** split (primary) plus a random split (interpolation upper bound) and a time split where dates exist. Freeze and hash before modeling. Define novelty against ICSD + MP.

**Baselines.** Reproduce an MLIP formation-energy check against MP, a conductivity regressor against the experimental compilation, and an MLIP-MD diffusion estimate for a known superionic conductor. Score with an independent script.

**Model.** Candidate contributions: (i) a better/finetuned MLIP for Li-ion diffusion with uncertainty (ensemble MLIPs) feeding calibrated $\sigma$/$E_a$; (ii) a multi-property joint model with calibrated heads; (iii) a **synthesizability model** trained on ICSD-realized vs. never-made labels and precursor availability; (iv) a generative model (diffusion / VAE) conditioned on the joint constraint set, with novelty enforced against ICSD/MP.

**Calibration.** Fit and validate per-property uncertainty on held-out experimental data (ensemble spread, conformal intervals) and report coverage/expected calibration error per family, foregrounding the gap between in-silico-proxy calibration and experiment.

**Compute.** MLIP relaxation, MLIP-MD for diffusion (short trajectories, elevated-temperature extrapolation), property regressors, and generative models are all feasible on one prosumer GPU for screening scales; full AIMD confirmation is expensive and reserved for shortlist candidates. Compute enables ranking, not closure.

**Failure modes.** (i) **Prediction-to-synthesis gap** - predicted-stable compositions frequently fail to form the target phase; this is the dominant, defining risk. (ii) **In-silico-proxy error** - MLIP/AIMD conductivities carry systematic and statistical error and can be off by orders of magnitude versus experiment. (iii) **Novelty illusion** - generated "novel" compounds already in ICSD, or disordered/unphysical. (iv) **Data scarcity** - measured conductivities exist for relatively few, family-clustered materials, so distribution shift to novel chemistries is severe. (v) **Single-property tunnel vision** - optimizing conductivity while ignoring window/interface/synthesizability yields useless candidates.

## 7. Verification and auditability requirements

1. **Leakage-safe evaluation.** The train/test split is committed and hashed before any evaluation, under documented **composition/structure-family separation** and, where applicable, time separation; random splits are reported only as a labeled interpolation upper bound; per-family strata are reported separately; there is no test-set tuning.
2. **In-silico-proxy honesty.** Every computed property (convex-hull stability, MLIP/AIMD conductivity, grand-potential window) is explicitly labeled a proxy, with its expected error versus experiment stated; no computed number is presented as a measurement.
3. **Novelty against realized structures.** Generated or screened candidates are checked for novelty against **ICSD and Materials Project**, not merely the training set, and the check is part of the record - directly addressing the post-GNoME novelty-illusion failure mode.
4. **Joint-constraint accounting.** Candidates are reported against the **full** constraint set (stability, conductivity, window, interface, synthesizability) simultaneously; a candidate passing one constraint while failing another is not counted as a hit.
5. **Calibrated uncertainty.** Every prospective property carries a calibrated uncertainty; coverage and expected calibration error are reported on held-out experimental data, per family, with the proxy-to-experiment gap foregrounded.
6. **Cryptographic manifest, preservation, and registry.** A SHA-256 manifest covers split definitions, dataset and structure-version hashes, MLIP and model code/weights, and every prediction/generation file; MLIP versions, MD settings, and data versions are preserved; anything not preserved is stated. Synthesis-ready slates (P5) are timestamped and registered before synthesis and scored afterward including failures-to-form.
7. **Honest reporting.** The report states up front that solid-electrolyte discovery is reality-gated and **not resolved**; separates in-silico proxies from any synthesis/characterization result; foregrounds the prediction-to-synthesis gap as the defining obstacle; labels every candidate a synthesis-pending hypothesis; and never presents a stability or computed-conductivity number as a real-world guarantee.
