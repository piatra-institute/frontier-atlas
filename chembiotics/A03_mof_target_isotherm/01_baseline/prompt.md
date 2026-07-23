# PROMPT FOR MOFs DESIGNED TO A TARGET ADSORPTION ISOTHERM

## Inverse design of porous frameworks whose GCMC isotherm matches a specified target, with the simulation as the on-machine verifier

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** A - closed-loop (on-machine verifier)
**Rank:** A03 of 21
**Source:** chem/bio top-50 list #32, section D (design)
**Modes:** `[gen]` `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Metal–organic frameworks (MOFs) are crystalline, tunable porous solids assembled from metal nodes and organic linkers; they are leading candidate materials for gas separations and direct air capture. The standard question is inverted here: rather than "characterize this framework", the task is "design a framework whose adsorption isotherm hits a *specified target curve*" - for instance, high CO$_2$ uptake at $400\,\text{ppm}$ with a large working capacity between capture and regeneration pressures, at a stated selectivity over N$_2$. The loop closes on-machine because, for any candidate framework, its isotherm is *computable*: grand-canonical Monte Carlo (**GCMC**, run in RASPA) is the **on-machine verifier**. This makes it a Pack A design problem - generate/search over building blocks, verify by simulation, iterate - without leaving the workstation. The essential honesty is that GCMC uses a *classical force field with a rigid framework*: it is a self-consistent verifier, not physical reality. Real synthesis and a measured isotherm are the reality gate; the design$+$GCMC loop is genuinely closed but reports a force-field-relative result. Anything short of the section-2 standard - a candidate matched only by a cheap descriptor surrogate, or a match inside the force field's known error envelope reported as an experimental match - is a partial result, never a solution.

## 1. Exact problem statement

**Framework.** A candidate framework $F$ is a periodic crystal, committed as a CIF file:

- lattice vectors and fractional atomic coordinates;
- atom types and partial charges;
- drawn from an explicitly defined space - an enumerated building-block set (metal-node SBUs $\times$ organic linkers $\times$ net topologies), a hypothetical-MOF database, or a generative model over these. The space is written down and hashed.

**Adsorbate models.** Guest gases are fixed rigid molecular models, part of the frozen specification:

- CO$_2$ and N$_2$ as TraPPE three-site models;
- CH$_4$ as united-atom TraPPE (state whichever is used).

**Force field.** Framework–guest and guest–guest interactions, committed and hashed *before* any design, since they *are* the definition of the verifier:

- Lennard-Jones (UFF or DREIDING for framework atoms - fix one) plus electrostatics via Ewald summation;
- framework partial charges from one fixed method (EQeq, Qeq, or DDEC - fix one).

**GCMC protocol.**

- Temperature $T$ fixed (e.g. $298\,\text{K}$); a fixed pressure grid $\{P_i\}$; fugacities from the Peng–Robinson equation of state.
- Specified equilibration and production cycles; insertion/deletion/translation/rotation moves.
- Inaccessible-pocket blocking from a geometric pre-pass.
- Output at each $P_i$: absolute loading $q_i$ (in $\text{mmol}\,\text{g}^{-1}$) with a block-averaged statistical error $\sigma_i$. The isotherm is the vector $\{(P_i,q_i,\sigma_i)\}$.

**Target and match metric.** A target isotherm is a curve $q^\star(P)$ on the grid, or a set of scalar targets - uptake $q^\star(P_{\text{ads}})$, working capacity $\Delta q^\star = q^\star(P_{\text{ads}}) - q^\star(P_{\text{des}})$, and CO$_2$/N$_2$ selectivity $S^\star$ (from co-adsorption GCMC or IAST on single-component isotherms). A candidate *matches within tolerance* iff a committed metric holds, for example

\[
\max_i \frac{|q_i - q^\star(P_i)|}{q^\star(P_i)} \le \varepsilon_{\text{rel}}
\qquad\text{and}\qquad
|q_i - q^\star(P_i)| \le \max\!\big(\varepsilon_{\text{abs}},\, k\,\sigma_i\big)\ \ \forall i,
\]

i.e. the deviation is within a stated relative/absolute tolerance *and* commensurate with GCMC statistical error. Scalar-target variants (working capacity within $\delta$; selectivity within a factor) are stated numerically up front.

**Target.** Over the committed framework space, force field, and protocol, produce $F$ whose GCMC isotherm matches $q^\star$ within the committed tolerance - with GCMC as the verifier - and, for the strong targets, certify optimality/non-dominance or exhaustiveness over an enumerated set.

**Accuracy threshold.** Numeric: the committed match metric, judged against converged GCMC with reported error bars. "Good uptake" or "high selectivity" without a number and a tolerance is not a target.

## 2. Resolution standard

Full resolution is a design pipeline that, for a committed target isotherm $q^\star$ under a committed (space, force field, protocol, metric), returns a framework $F$ whose *converged* GCMC isotherm meets the metric - verified by a GCMC run reproduced by a standalone pipeline separate from the generator/search. At the strong end, it further returns either a certified Pareto front over (working capacity, selectivity, geometric stability descriptors) or a certified exhaustive screen over an enumerated topology/building-block set naming the in-set optimum.

**Not accepted as resolution:**

- A candidate selected by a cheap surrogate (an ML uptake predictor, a geometric-descriptor regressor) but never confirmed by converged GCMC.
- A match reported from an unconverged GCMC run (too few cycles, unblocked inaccessible pockets inflating loading), or with no error bars.
- A force-field-relative match presented as an experimental match (see integrity clause).
- A "designed" framework that is not charge-, topology-, or chemically well-defined enough to simulate reproducibly, or that no plausible synthesis could target (unflagged synthesizability).
- Best-in-a-random-sample presented as optimal over the defined space; "optimal" requires either enumeration or a certified search.

**Benchmark-integrity clause.** The GCMC verifier's biases are known and must be stated:

- a *rigid* framework (no breathing/gate-opening, which real MOFs like MIL-53 or ZIF-8 show);
- *generic* LJ parameters (UFF/DREIDING) that systematically misestimate CO$_2$ uptake, often by tens of percent;
- *no chemistry at open metal sites* - chemisorption and strong CO$_2$–open-metal binding (Mg-MOF-74) are not captured by a classical LJ$+$Coulomb model;
- charge-method sensitivity (EQeq vs DDEC can shift electrostatic uptake noticeably).

The mandatory guard is a **force-field error-envelope calibration**: run the identical pipeline on a set of well-characterized MOFs with published experimental isotherms (IRMOF-1/MOF-5, HKUST-1, ZIF-8, Mg-MOF-74) and report the GCMC-vs-experiment deviation, so every design match is read against that envelope. A match *inside* the envelope is not evidence of an experimental match and must be flagged. Real synthesis with a measured isotherm remains the reality gate.

## 3. Graded partial-result targets

- **P1 (verified pipeline reproduces a published isotherm).** Reproduce a published GCMC isotherm for a known MOF (e.g. IRMOF-1 CO$_2$ or CH$_4$ from the Snurr-group literature) with our RASPA pipeline, matching within stated statistical error, including pocket blocking and Ewald convergence. *Certificate:* RASPA inputs, the converged isotherm with error bars, and the comparison to the published curve, all reproducible from a manifest.
- **P2 (calibrate the verifier's bias).** Run the pipeline on the experimental-benchmark MOF set and report GCMC-vs-experiment deviations per gas and pressure range - the force-field error envelope that contextualizes all later matches. *Certificate:* the benchmark table + charge/force-field provenance.
- **P3 (inverse design to a target isotherm).** Over a defined building-block/topology space, search or generate a framework whose GCMC isotherm meets the committed match metric for a target $q^\star$ (e.g. a direct-air-capture CO$_2$ target). *Certificate:* the CIF + the converged GCMC isotherm + the metric evaluation + the search/generation log.
- **P4 (Pareto front).** Produce a certified non-dominated set over (CO$_2$ working capacity, CO$_2$/N$_2$ selectivity, a geometric stability/void descriptor from Zeo++/PoreBlazer), every point GCMC-verified. *Certificate:* the candidate set, per-candidate GCMC + descriptors, and the dominance check.
- **P5 (certified exhaustive screen).** Over a *finite enumerated* set (a fixed topology $\times$ a fixed node set $\times$ a fixed linker library, within stated bounds), run GCMC on every member and certify the in-set optimum / feasible set for the target. *Certificate:* the complete enumeration manifest + per-candidate converged GCMC + the selection argument, independently replayable.
- **P6 (strongest, reality-flagged).** A P3/P4 winner accompanied by a synthesizability assessment and a higher-fidelity cross-check (a DFT-derived or ab-initio-informed force field, or DFT binding energies at key sites) quantifying how far the classical-force-field match might move under better physics - the honest bridge toward the reality gate. *Certificate:* the cross-check computations + a revised uncertainty on the match.

Full resolution (P5 over a lab-relevant space, or P3/P4 that survive P6 scrutiny) is unlikely in one session; P1–P3 are realistic and independently valuable.

## 4. Known results and prior art

- Wilmer, Leaf, Farha, Hupp, Snurr et al. 2012 (*Nature Chemistry*) - the hypothetical-MOF database (~137,000 frameworks) and large-scale CO$_2$-capture screening; the template for enumerate-then-simulate.
- Chung, Haldoupis, Sikora, Snurr et al. 2014, with a 2019 update - CoRE MOF (Computation-Ready Experimental MOF) database.
- Dubbeldam, Calero, Ellis, Snurr 2016 - RASPA 2, the standard GCMC/molecular-simulation code for nanoporous materials (*Mol. Simul.*).
- Willems, Rycroft, Kazi, Meza, Haranczyk 2012 - Zeo++ for geometric pore analysis; Sarkisov and co-workers - PoreBlazer.
- Boyd, Chidambaram, García-Díez, … Smit et al. 2019 (*Nature*) - MOF design/screening for CO$_2$ capture in humid flue gas.
- Yao, Sánchez-Lengeling, … Aspuru-Guzik, Smit et al. 2021 (*Nature Machine Intelligence*) - generative (supramolecular VAE) inverse design of reticular materials (verify exact scope).
- Kadantsev, Boyd, Daff, Woo 2013 - EQeq fast charge assignment; Manz & Sholl - DDEC charges; Nazarian, Camp, Sholl - DFT-derived charges for CoRE MOF (verify).
- Myers & Prausnitz 1965 - Ideal Adsorbed Solution Theory (IAST) for mixture selectivity; Simon, Smit, Haranczyk 2016 - pyIAST.
- Colón, Gómez-Gualdrón, Snurr - ToBaCCo topology-based MOF construction; Lee, Kim et al. - PORMAKE (verify), for enumerating frameworks from building blocks.
- Fanourgakis, Gkagkas, Tylianakis, Froudakis - ML descriptors/surrogates for MOF adsorption (verify).

Screening is mature; robust *inverse design to a target isotherm* with simulation-verified guarantees, and honest force-field-error accounting, is not settled. **Status as of mid-2026 - re-verify against current literature before starting any session.**

## 5. Attack plan

**[search] GCMC verifier first.** Stand up RASPA with the committed force field, adsorbate models, charge method, Ewald settings, and pressure grid; add a Zeo++ pre-pass for pore-limiting diameter, accessible surface area, void fraction, and inaccessible-pocket blocking. Validate on P1/P2 before trusting any design number. Converge cycles until the block-averaged $\sigma_i$ is below the tolerance scale.

**[gen] Framework generation/search.** Build the framework space explicitly: enumerate building blocks with ToBaCCo/PORMAKE, or draw from the hypothetical-MOF/CoRE databases, or train a generative model over building blocks and topologies. Cheap geometric descriptors (Zeo++/PoreBlazer) and optional ML surrogates *rank* candidates, but nothing is accepted until GCMC confirms it. For P5, enumerate a finite set and screen exhaustively.

**[search] Selectivity and objectives.** Selectivity via co-adsorption GCMC or pyIAST on single-component isotherms; working capacity from the isotherm at $P_{\text{ads}}$ and $P_{\text{des}}$; these combine into the committed match metric or the Pareto objective.

**One-workstation scope.** A single GCMC point is minutes to hours; a full isotherm is a handful of points; screening is embarrassingly parallel, and a single multicore workstation handles hundreds to thousands of frameworks over days. No GPU is required for GCMC (RASPA is CPU); a GPU only helps a generative model. **Failure modes:** unconverged GCMC (too few cycles); inaccessible-pocket loading if blocking is skipped; charge-assignment errors (EQeq artifacts); force-field non-transferability (open-metal sites, strong electrostatics); rigid-framework error for flexible MOFs; and "designed" CIFs that are geometrically strained or chemically implausible - all of which the P2 envelope and P6 cross-check exist to expose.

## 6. Verification and auditability requirements

1. **Converged, error-barred numerics.** Every reported loading carries a block-averaged statistical error; the match metric is judged against converged GCMC, never a single short run; Ewald and cutoff convergence are demonstrated.
2. **Independent verification.** The design/search code and the verification GCMC pipeline are separate; a candidate's headline isotherm is re-run by the standalone pipeline and, where warranted, cross-checked against an independent GCMC code or the P6 higher-fidelity force field.
3. **Reproducibility.** Force field, charge method, adsorbate models, protocol (cycles, moves, EOS), pressure grid, framework-space definition, tool versions, and seeds are recorded; a SHA-256 manifest covers every CIF, force-field file, RASPA input, and isotherm; the experimental-benchmark set and the target are committed before any design run.
4. **Preservation.** Generator/search code, all candidate CIFs (accepted and rejected), GCMC inputs/outputs, and descriptor computations are part of the record; discarded candidates are listed as discarded.
5. **Honest reporting.** The report states up front that matches are force-field-relative, gives the P2 error envelope alongside every claimed match, distinguishes GCMC-verified from surrogate-ranked candidates, flags synthesizability and rigid-framework assumptions, and never presents a classical-force-field isotherm match as an experimental one.
