# PROMPT FOR DE NOVO ENZYMES AT NATURAL-ENZYME CATALYTIC EFFICIENCY

## Designing a novel protein that catalyzes a specified reaction with evolved-level k_cat/K_M

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** B - reality-gated (empirical verifier)
**Rank:** B-20 of 29
**Source:** chem/bio top-50 list #24, section D (design)
**Modes:** `[gen]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

> **Audit note (July 2026 - see `../../STATUS_AUDIT_2026-07.md`):** SOTA moved in 2025. RFdiffusion2 zinc metallohydrolases (Nature 2025) reached k_cat/K_M ≈ 5.3×10⁴, and de novo serine hydrolases (Baker Lab, Science 2025) ≈ 2.2×10⁵ M⁻¹s⁻¹ - approaching natural (~10⁵). Crucially this *confirms* the framing below: most gain comes from binding (lower K_M), while k_cat still trails natural by 1–3 orders. Re-baseline against these campaigns and re-scope the open target to the catalytic-**rate** (k_cat) gap specifically.

### Abstract

De novo enzyme design can now reliably produce a folded protein with a preorganized active site and *weak* catalytic activity for a chosen reaction. What it cannot do reliably is match the catalytic efficiency of a naturally evolved enzyme: designed catalysts typically start orders of magnitude below natural \(k_{\text{cat}}/K_M\), and most of the gap is closed - when it is closed at all - by rounds of directed evolution, not by the design itself. The payoff of closing this gap by design is large: made-to-order green-chemistry biocatalysts, plastic (e.g. PET) depolymerases, and reactions with no natural enzyme. This is a **reality-gated** problem: catalytic efficiency is a kinetic measurement on an expressed, purified protein, so no amount of in-silico scoring establishes it. The honest deliverable is a certified design/method contribution plus a small, ranked, calibrated set of falsifiable designs a wet-lab partner can express and assay - never a claimed resolution. The catalytic-efficiency gap is the crux and is treated as such throughout.

## 1. Exact problem statement

**Design target.** Given a specified reaction - substrate(s), product(s), and a chosen chemical mechanism (a transition-state model with the catalytic groups that stabilize it) - output a protein sequence (and predicted structure) that, when expressed and purified, catalyzes that reaction.

**Formally, fix:**
- *Input:* a reaction specification - substrate(s), product(s), a mechanism, and a quantum transition-state (TS) model with the catalytic residues/cofactors that stabilize it (the theozyme).
- *Output:* a protein sequence, its predicted structure, and the placed active-site geometry, with a proposed expression construct.
- *Metric:* the measured catalytic efficiency \(k_{\text{cat}}/K_M\) on the purified protein.
- *Population:* the claim is per-reaction and per-design, over an ordered (unbiased) list of outputs, so that a hit rate - the fraction of ranked designs that are measurably active - is well defined.

**Success metric (the whole problem).** The catalytic efficiency

\[
\frac{k_{\text{cat}}}{K_M}\ \ [\mathrm{M^{-1}\,s^{-1}}],
\]

measured by a Michaelis–Menten kinetic assay on the purified protein, referenced against (i) the uncatalyzed rate \(k_{\text{uncat}}\) (rate enhancement \(k_{\text{cat}}/k_{\text{uncat}}\)) and (ii) the natural-enzyme regime \(10^{5}\!-\!10^{8}\,\mathrm{M^{-1}\,s^{-1}}\). A design is *interesting* at \(k_{\text{cat}}/K_M \gtrsim 10^{3}\) without evolution; it *matches nature* only in the \(10^{5}\!-\!10^{8}\) band. Additional required reporting: expression yield, solubility, whether the assay used the designed sequence as-is or a laboratory-evolved variant, catalytic multiple-turnover (is it a true catalyst, not a stoichiometric reactant), and enantio-/regioselectivity where the reaction has stereochemistry.

**Target class.** A single named reaction per campaign - candidates: ester/amide hydrolysis (serine-hydrolase chemistry), retro-aldol, Kemp elimination, Michael addition, Diels–Alder, or a polyester (PET) hydrolysis. The claim is per-reaction; generality across reactions is not assumed and must not be inferred from one success.

**Falsifiability.** Each delivered design must come with a prediction sharp enough to be wrong: a predicted activity band and a stated threshold such that a null kinetic result (no measurable turnover above \(k_{\text{uncat}}\)) refutes that design. A design set with no threshold at which it could fail is not a scientific deliverable.

**The in-silico-scorable sub-question (separable).** Independent of the wet lab, one can score:
- (a) whether a theozyme (TS geometry + catalytic residues) embeds into a designed scaffold with sub-Ångström catalytic geometry;
- (b) whether the designed sequence folds to that scaffold by re-prediction (self-consistency);
- (c) whether the active-site geometry survives molecular dynamics (preorganization, not collapse; near-attack-conformation population; controlled active-site hydration);
- (d) whether a QM/MM barrier estimate on the shortlist is plausible.

These are computable *proxies* for catalysis. **They are not catalysis.** The efficiency gap lives precisely in the space between a geometrically perfect in-silico active site and a fast real enzyme.

**Why the efficiency gap is hard (what design underserves).** Natural \(k_{\text{cat}}/K_M\) is the product of several effects that current single-structure design captures poorly:
- *Electrostatic preorganization* - the folded active site is pre-arranged to stabilize the TS charge distribution without paying reorganization energy; a geometrically correct but electrostatically inert pocket is catalytically weak.
- *Near-attack-conformation population* - the fraction of time reactive atoms sit in a productive geometry; a dynamic property, not a static one.
- *Desolvation and water exclusion* - controlled removal of water from the reactive center; mis-hydrated pockets quench catalysis.
- *Dynamics and conformational selection* - motions coupling substrate binding to the reactive state.
- *Product release* - turnover is limited if products do not leave; single-turnover "activity" is not \(k_{\text{cat}}\).

Each is only partly scored by geometry, self-consistency, or a static barrier - which is why design routinely delivers the fold and a weak start, and evolution supplies the rest.

## 2. Verifier and data

**In-silico oracles and filters (and their known unreliability).**
- **Theozyme placement / RosettaMatch–style embedding** - positions catalytic residues around a QM transition-state model. *Unreliable because* a geometrically ideal theozyme predicts almost nothing about rate; TS stabilization is an ensemble-electrostatics property, not a rigid-geometry property.
- **RFdiffusion / RFdiffusionAA active-site scaffolding** - builds a backbone around a fixed functional-site motif (including a small-molecule/TS analog for the all-atom variant). *Unreliable because* scaffolds that "hold" the motif in a static pose need not preorganize its electrostatics or exclude water correctly.
- **ProteinMPNN / LigandMPNN sequence design + AlphaFold3 re-prediction (self-consistency).** Standard filter: does AF3/AF2 re-predict the intended backbone (Cα-RMSD, pLDDT, and for the ligand/TS, pocket geometry / ipTM-like scores). *Unreliable because* self-consistency measures foldability, not function; a sequence can pass every self-consistency filter and be catalytically dead. **In-silico self-consistency success rates systematically overstate real catalytic success.**
- **Rosetta interface/packing energy and constraint satisfaction** - reports whether the catalytic constraints are met at low energy. *Unreliable because* a favorable score function is not a favorable free energy of the reactive state.
- **MD of catalytic geometry** - preorganization, near-attack-conformation population, active-site hydration. *Unreliable because* force-field and timescale limits; a stable pocket in MD is necessary, not sufficient.
- **QM/MM barrier estimate** - the closest in-silico proxy to rate. *Unreliable because* sensitive to the QM region, sampling, and the (unknown) real conformational ensemble; error bars easily exceed the kcal/mol that separates a good from a dead design.

**Frozen benchmark / precedent set.** A fixed panel of *published* de novo enzymes with reported pre- and post-evolution \(k_{\text{cat}}/K_M\) - retroaldolase, Kemp eliminase, Diels–Alderase, designed luciferase, designed serine hydrolases (see §5) - committed (hashed) before modeling. Reproducing their reported in-silico metrics and rank-ordering their known measured activities is the leakage-controlled baseline. Where a design used in the precedent set overlaps a model's training data, that overlap is flagged; retrospective rank-ordering is never presented as prospective design success.

**Wet-lab gate (mandatory).** Catalytic efficiency cannot be established without new physical experiments:
- gene synthesis of each construct (roughly \$50–\$300 per gene);
- expression (typically *E. coli*) and purification;
- a Michaelis–Menten kinetic assay measuring \(k_{\text{cat}}\) and \(K_M\), with the uncatalyzed-rate control, multiple-turnover confirmation, and - where relevant - chiral analysis of product.

Rough cost: expression + purification + a clean kinetics panel is on the order of \$1k–\$5k per design carried through; a realistic campaign (design → filter → test a dozen or more, possibly with a directed-evolution follow-up) runs \$20k–\$100k+ and months of wet-lab time. **This line is not optional and must not be softened: an in-silico "hit" is a hypothesis about a molecule, not a measured catalyst.**

**The gap between in-silico and real success is large and must be stated numerically.** Across the design literature, the fraction of self-consistent, well-scored designs that show *any* measurable activity is commonly a small minority, and the fraction reaching natural-band \(k_{\text{cat}}/K_M\) *without* directed evolution is near zero. A pipeline that reports only its in-silico pass rate, without an estimate of the expected real-activity rate and its basis, is misrepresenting the problem.

## 3. Standard of a genuine advance

The ordering principle: an advance is real if it either improves a *verifiable in-silico contribution* (a reproducible method or a held-out proxy) or produces a *falsifiable prospective artifact* (a design set with pre-registered success criteria). A genuine advance is one of: (a) a **certified method contribution** - a design/scoring pipeline that, on the frozen precedent panel, rank-orders known designs by measured activity better than a named baseline, with the improvement reproduced by an independent script; (b) an **improved in-silico success proxy on a held-out reaction** - a filter that raises the fraction of designs later confirmed active, validated on a reaction not used to build it; or (c) the top target: a **small, ranked, calibrated, synthesizable, falsifiable design set** for one specified reaction, each design carrying a calibrated probability of measurable activity and an explicit predicted \(k_{\text{cat}}/K_M\) band, handed to a wet-lab partner with pre-registered success criteria. The top target is the point of the exercise; (a) and (b) are the credible stepping stones to it.

**Not accepted as resolution.**
- An in-silico "hit" - theozyme embedded, sequence self-consistent, pocket stable in MD - presented as a catalyst. It is a hypothesis; only kinetics on the purified protein makes it a catalyst.
- **Self-consistency (AF3/AF2 re-prediction agreement) reported as function.** Foldability is not activity.
- A design that is active *only after directed evolution*, credited to the design method without stating that evolution, not design, supplied the efficiency.
- A QM/MM barrier or docking score presented as a measured rate.
- A stoichiometric (single-turnover) reaction reported as catalysis; multiple turnover is required for the "enzyme" claim.
- A rate enhancement over background reported as if it were natural-enzyme efficiency; the \(10^{5}\!-\!10^{8}\) band is the bar for the "matches nature" claim and must be stated separately from any weaker claim.
- Retrospective rank-ordering of already-known designs presented as prospective design success.

## 4. Graded targets

**P1 - Reproduce a published design pipeline's in-silico metrics.** Rebuild a Rosetta or RFdiffusion(AA)+MPNN+AF3 enzyme-design pipeline and reproduce the reported self-consistency / scaffolding metrics on a published system (e.g. a designed serine hydrolase or Kemp eliminase). *Certificate:* metrics matching within noise; committed code, seeds, and hashes.

**P2 - Certified retrospective discrimination on the frozen panel.** Show the scoring pipeline rank-orders the frozen precedent panel by *measured* activity (pre-evolution where available) better than a stated baseline (e.g. raw AF3 pLDDT or a docking score), with an honest correlation and its confidence interval. *Certificate:* the panel, the frozen scores, an independent recomputation, and training-overlap flags.

**P3 - Improved in-silico success proxy on a held-out reaction.** Construct a filter predicting eventual measured activity and validate it on a reaction family withheld from its construction; report the lift in confirmed-active fraction and the calibration curve. *Certificate:* the held-out split fixed (hashed) before scoring.

**P4 - A ranked, calibrated, falsifiable design set for one reaction (top target).** For a single specified reaction, deliver ≤ 24 designs, ranked, each with a calibrated probability of measurable activity, a predicted \(k_{\text{cat}}/K_M\) band, expression-feasibility notes, and a pre-registered success criterion (e.g. "≥ 3 of the top 8 show \(k_{\text{cat}}/K_M > 10^{2}\,\mathrm{M^{-1}\,s^{-1}}\) without evolution"). *Certificate:* frozen design set + calibration model committed (hashed) before any assay; wet-lab partner named.

**P5 - Prospective wet-lab confirmation with honest calibration.** Only in partnership with a lab: the P4 set expressed and assayed, reporting the realized hit rate against the pre-registered criterion and the calibration error - including, plainly, if per-design real success was low. *Certificate:* raw kinetic traces, the frozen predictions provably predating them.

## 5. Known results and prior art

- Baker-lab computational enzyme design: retroaldolase (Jiang et al., 2008), Kemp eliminase (Röthlisberger et al., 2008), Diels–Alderase (Siegel et al., 2010) - all fold with weak activity, most improved dramatically only by directed evolution. (verify exact years)
- Designed luminescent/luciferase enzymes (Yeh et al., 2023, "de novo luciferases", verify).
- Designed serine hydrolases with reactive catalytic sites (Lauko et al., 2024–2025, verify) - a leading recent claim of designed multistep catalytic machinery; check the reported \(k_{\text{cat}}/K_M\) and whether evolution was required.
- Directed-evolution complement: Arnold and co-workers established that laboratory evolution routinely supplies the efficiency that design does not - the reason the efficiency gap is attributed to design, not to protein chemistry in general.
- Rosetta enzyme design framework: theozyme + RosettaMatch + design (Baker, Houk, and co-workers, 2006–); the "inside-out" design paradigm.
- RFdiffusion active-site scaffolding (Watson et al., 2023, Nature) and RFdiffusionAA / all-atom diffusion for small-molecule and functional-site scaffolding (Krishna et al., 2024, Science, verify).
- ProteinMPNN (Dauparas et al., 2022) and LigandMPNN (Dauparas et al., 2023–2024, verify) for sequence design around ligands/functional sites.
- Warshel and co-workers - the electrostatic-preorganization theory of enzyme catalysis, the mechanistic reason a geometrically correct active site is not automatically a fast one.
- Kemp-eliminase directed evolution (Khersonsky, Tawfik and co-workers, ~2010–2013, verify) - the canonical demonstration that evolution, not the original design, supplied most of the efficiency.
- PET-hydrolase engineering (e.g. engineered/evolved cutinases such as the LCC variants and PETase relatives, Tournier et al., 2020, verify) illustrates the target regime - but these are engineered natural enzymes, not de novo designs.
- The recurring finding across this literature: design yields the fold and modest activity; **evolved-level \(k_{\text{cat}}/K_M\) is generally reached by laboratory evolution, not by design** - this efficiency gap is the open problem, not folding.

*Status as of mid-2026 - re-verify against current literature before starting any session.*

## 6. Attack plan

**Datasets/inputs.** Pull the frozen precedent panel (PDB structures + published kinetics), and the TS/theozyme models for the chosen reaction. Fix a leakage-safe split: any reaction family used to build a filter is held out of its evaluation; flag any precedent that overlaps a model's training set.

**Pipeline (one prosumer GPU is sufficient for the neural stages).** RFdiffusion / RFdiffusionAA for scaffold generation around the theozyme; ProteinMPNN / LigandMPNN for sequence; AlphaFold3 (or AF2/Boltz) for re-prediction and self-consistency filtering; RDKit for ligand/TS handling; short MD (OpenMM) for active-site stability and near-attack-conformation population; optional QM/MM (a semiempirical or DFT QM region) for a barrier estimate on the shortlist; Rosetta for theozyme matching and constraint/ddG scoring. Calibrate any success-probability model on the frozen panel and report its calibration on held-out data.

**Compute budget / one-GPU scope.** RFdiffusion(AA) generation, ProteinMPNN, and AF3/AF2 re-prediction all run on a single 24 GB prosumer GPU for the design sizes here; the practical throughput bottleneck is re-prediction over large design pools, not memory. Short equilibrium MD runs on the same GPU; QM/MM barrier estimates are CPU/GPU-bound and are reserved for a small shortlist. The whole in-silico loop (generate → design → filter → shortlist) is feasible on one workstation; only the wet-lab gate needs external resources.

**Suggested first reaction.** Begin with a well-precedented, easy-to-assay chemistry (ester hydrolysis or Kemp elimination) where \(k_{\text{uncat}}\) is known and a spectrophotometric readout exists - so that P1–P3 can be executed against real published kinetics before committing to a novel target reaction.

**Failure modes to expect and report.**
- *Self-consistency inflation* - high AF3 re-prediction agreement that does not survive contact with kinetics; report the self-consistency pass rate and the (much lower) expected real-activity rate separately.
- *Docking / barrier-score unreliability* - QM/MM barriers and docking scores with error bars exceeding the kcal/mol that separates good from dead.
- *Expression failure* - a design that never yields soluble protein produces no kinetics regardless of its scores.
- *Electrostatic preorganization gap* - a geometrically correct but electrostatically inert active site.
- *Substrate binding without catalysis* - a pocket that binds substrate but does not lower the barrier; \(K_M\) improves while \(k_{\text{cat}}\) does not.
- *Single-turnover artifacts* - apparent activity that is stoichiometric consumption, not catalysis.
- *The efficiency gap itself* - designs that are catalytically real but 3–6 orders below natural efficiency; this is the expected outcome, not a bug, and must be reported honestly.

## 7. Verification and auditability requirements

1. **Leakage-safe evaluation.** Any reaction/scaffold used to build a scoring filter is excluded from its evaluation; the frozen precedent panel and all splits are committed (hashed) before scoring; no tuning on the test reaction; training-overlap flagged.
2. **Calibrated uncertainty.** Every delivered design carries a calibrated probability of measurable activity and a predicted \(k_{\text{cat}}/K_M\) band; calibration is itself reported on held-out data. **Every design is a labeled hypothesis, not a claimed catalyst.**
3. **Separation of in-silico filters from real validation.** The report keeps in-silico metrics (self-consistency, MD stability, barrier estimates) in a section physically separate from any wet-lab kinetics; no in-silico number is ever presented as a rate.
4. **Independent reproduction.** A standalone script recomputes all in-silico metrics from committed inputs and model hashes; SHA-256 manifest over designs, code, scores, and (if any) assay data.
5. **Preservation.** Generation/design code, model versions/checkpoints, theozyme definitions, and MD inputs are part of the record. Anything not preserved is stated explicitly.
6. **Honest reporting.** The report states up front that the problem is reality-gated and NOT resolved; that current *per-design real success rates are low* and that matching natural \(k_{\text{cat}}/K_M\) by design (without evolution) remains unsolved; and it never presents a self-consistent, MD-stable, low-barrier in-silico design as a catalyst.
7. **Evolution and turnover disclosure.** Any activity figure states explicitly whether it belongs to the designed sequence as-is or to a laboratory-evolved variant, and whether multiple turnover was demonstrated; credit for efficiency is assigned accordingly.
