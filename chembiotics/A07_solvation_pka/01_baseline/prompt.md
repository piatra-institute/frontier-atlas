# PROMPT FOR ACCURATE IMPLICIT SOLVATION AND PROTEIN pKa

## Continuum electrostatics and protonation-state free energies, certified against explicit-solvent reference

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Pack:** A - closed-loop (on-machine verifier)  
**Rank:** A-07 of 21  
**Source:** chem/bio top-50 list #13, section B (free energy, dynamics, sampling)  
**Modes:** `[func]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Implicit solvation - replacing explicit water by a continuum electrostatic and nonpolar model - is decades old and still routinely wrong at the sub-kcal/mol level that electrostatics and protonation demand. Protein $pK_a$ prediction and constant-pH molecular dynamics inherit that error and add sampling problems of their own; the result is a standing embarrassment for a quantity as basic as which side chains are charged. This prompt fixes the on-machine verifier as **explicit-solvent alchemical free energy** (thermodynamic integration / free-energy perturbation with a *fixed, named* solute force field and water model): for a given Hamiltonian, the exact hydration free energy of a solute, or the exact deprotonation free energy of a titratable group, is a converged simulation output, not a matter of opinion. The task is a solvation functional (and a protonation-free-energy pipeline) that reproduces that explicit-solvent reference to a stated numeric tolerance, plus a certified $pK_a$ benchmark result with error bars. The central honesty hazard, stated once and enforced throughout: **"correct" here means "converged for the chosen Hamiltonian," not "matches experiment."** Agreement with measured hydration free energies or measured $pK_a$ values is a separate, downstream, force-field-limited question. Anything short of the section-2 standard is reported as a partial result, never as a solution.

## 1. Exact problem statement

**Systems.** Two coupled system classes.

- *(S1) Small-molecule hydration.* Neutral and charged organic solutes (the FreeSolv chemical space and its charged extensions), a single solute in a periodic water box.
- *(S2) Protein protonation.* Titratable side chains (Asp, Glu, His, Lys, Cys, Tyr, and the terminal groups) in folded proteins, with staphylococcal nuclease (SNase) internal-residue variants as the canonical stress set for buried, strongly shifted charges.

**Reference Hamiltonian (fixed and named).** A run must declare its force field and water model and hold them fixed across the entire comparison. Default reference: solute parameters from a stated general force field (e.g. GAFF2 with AM1-BCC or RESP charges for S1; Amber ff19SB or CHARMM36m for S2) and explicit water from a stated three- or four-site model (TIP3P, TIP4P/2005, or OPC). The reference is the choice of Hamiltonian, *not* nature.

**Notation and standard state.** Temperature $T$, $\beta=1/k_BT$; standard-state concentration $c^\circ = 1\,\mathrm{mol/L}$; energies in kcal/mol. Long-range electrostatics by particle-mesh Ewald with documented finite-size corrections for net-charged solutes. All free energies are reversible works at fixed $T,p$.

**Target quantity - hydration free energy.** For solute $M$, the hydration free energy is the reversible work of transferring $M$ from ideal gas to dilute aqueous solution. On-machine it is computed by alchemical decoupling: switch off solute–solvent electrostatics, then Lennard-Jones interactions, along a coupling parameter $\lambda\in[0,1]$, and integrate

\[
\Delta G_{\mathrm{hyd}}(M) \;=\; \int_0^1 \Big\langle \frac{\partial U(\lambda)}{\partial \lambda}\Big\rangle_\lambda \, d\lambda
\qquad\text{(TI)},
\]

or equivalently estimate it by BAR/MBAR over the $\lambda$ windows,

\[
\Delta G_{\mathrm{hyd}}(M) \;=\; -k_BT\,\ln \frac{\big\langle e^{-\beta \Delta U_{i\to i+1}}\big\rangle_i}{\cdots}
\quad\text{(BAR, with overlap-matrix diagnostics)} .
\]

This explicit-solvent $\Delta G_{\mathrm{hyd}}$, with periodic-boundary and finite-size corrections applied and documented, is the ground truth an implicit model must reproduce.

**Target quantity - protonation free energy.** For a titratable group in state (protonated $HA$) vs (deprotonated $A^-$ + proton in bulk), the on-machine quantity is the *relative* deprotonation free energy between two environments (e.g. a model compound in water vs the same group in the protein), obtained by an alchemical thermodynamic cycle that never requires the absolute proton solvation free energy:

\[
\Delta pK_a \;=\; \frac{\Delta\Delta G_{\text{deprot}}}{k_BT\ln 10},
\qquad
\Delta\Delta G_{\text{deprot}} \;=\; \Delta G^{\text{protein}}_{\text{deprot}} - \Delta G^{\text{model}}_{\text{deprot}} ,
\]

each $\Delta G_{\text{deprot}}$ computed by explicit-solvent TI/FEP over the charging/annihilation of the titratable proton with the fixed Hamiltonian. Working with the *shift* cancels the unknown absolute proton free energy exactly, keeping the on-machine quantity well defined.

*Why the shift, not the absolute.* An absolute $pK_a$ requires the absolute proton solvation free energy and a chosen reference convention, both of which are reality- and convention-gated, not on-machine facts. The **relative** deprotonation free energy between two environments (protein vs model compound) is a difference of two alchemical works on the same Hamiltonian and is therefore fully on-machine verifiable. The resolution standard is stated in terms of shifts for exactly this reason; an absolute-$pK_a$ claim carries an extra reality caveat that must be labeled.

**Solvation functional (the object to be built).** A map $\mathcal{F}_\theta$ from solute configuration (coordinates, partial charges, atom types) to a polar + nonpolar solvation free energy and its gradient, deployable as an implicit-solvent potential. Admissible forms:

- Poisson–Boltzmann (PB) continuum electrostatics plus a nonpolar surface/cavity term.
- Generalized Born variants (GB-HCT, GB-OBC, GBn2) with a stated surface-area nonpolar term.
- Continuum QM models (PCM, COSMO, SMD) recast for MM solutes.
- Learned functionals: graph neural networks over the solute graph, or $\Delta$-learning corrections on top of a GB/PB baseline.

Whatever the form, the functional is expected to decompose the solvation free energy into a polar (electrostatic) and a nonpolar (cavity + dispersion) contribution,

\[
\Delta G_{\mathrm{solv}} \;=\; \Delta G_{\mathrm{pol}} + \Delta G_{\mathrm{npol}},
\qquad
\Delta G_{\mathrm{npol}} \;\approx\; \gamma\, A_{\mathrm{SASA}} + b + \Delta G_{\mathrm{disp}},
\]

with the polar term the object the PB/GB/learned electrostatics must get right and the nonpolar term (surface-area $A_{\mathrm{SASA}}$ with tension $\gamma$, plus a dispersion correction) reported separately so the two error sources are never conflated.

**Accuracy threshold (numeric, no informal targets).** "Sub-kcal/mol" is defined as:

- root-mean-square error $\le 0.5$ kcal/mol against the explicit-solvent reference on a held-out set;
- mean signed error $|\text{MSE}| \le 0.2$ kcal/mol (no systematic offset);
- the reference itself converged to a reported statistical uncertainty $\le 0.1$ kcal/mol per solute.

For $pK_a$: RMSE $\le 0.5\ pK_a$ units against the explicit-solvent alchemical reference on the same Hamiltonian. "Chemical accuracy" and "good enough" are not acceptable targets.

**Constant-pH consistency (the internal check P4 uses).** A constant-pH titration must, for a single well-behaved site, produce a fraction-deprotonated $s(\text{pH})$ obeying Henderson–Hasselbalch with Hill coefficient $n$,

\[
s(\text{pH}) \;=\; \frac{1}{1 + 10^{\,n\,(pK_a - \text{pH})}},
\]

and the $pK_a$ read from this titration curve must equal, within error, the *independent* alchemical $\Delta pK_a$ for the identical Hamiltonian. Disagreement between the two on-machine routes is a convergence or coupling failure, not a modeling choice - this equality is exactly what makes constant-pH MD auditable rather than merely plausible.

## 2. Resolution standard

A resolution, for a stated system class and stated Hamiltonian, consists of:

1. A solvation functional $\mathcal{F}_\theta$ that, on a **frozen held-out** set of solutes disjoint from any fitting data, reproduces explicit-solvent $\Delta G_{\mathrm{hyd}}$ to RMSE $\le 0.5$ and $|\text{MSE}|\le 0.2$ kcal/mol, with per-solute reference uncertainties reported.
2. A $pK_a$ pipeline (implicit or constant-pH MD) that reproduces the explicit-solvent alchemical $\Delta pK_a$ reference to RMSE $\le 0.5$ units on a held-out titratable-group set, with error bars.
3. A demonstration that the functional generalizes across the two system classes, or an explicit statement of the domain on which it is validated.

**Not accepted as resolution:**

- A model that reproduces *experimental* hydration free energies or $pK_a$ values but has not been checked against the explicit-solvent reference on its own Hamiltonian. Matching experiment can occur by cancellation of a functional error against a force-field error, and is not evidence the functional is correct.
- Sub-kcal/mol on neutral solutes only, presented as solving solvation - ions and formal charges are where continuum models fail hardest, and are the load-bearing case.
- A single-protein or single-residue-type $pK_a$ success presented as a general method.
- A GB/PB parameter set tuned on the test proteins or the test solutes.
- Constant-pH MD titration curves that look sigmoidal but were never checked for internal thermodynamic consistency (section 3, P4).
- Any claim resting on non-converged explicit-solvent references (unstated $\lambda$-schedule, missing finite-size correction, no BAR/MBAR overlap check).

**Benchmark-integrity clause.** The two verifiers have opposite biases and both must be reported. *The on-machine reference (explicit-solvent TI/FEP) is exact for the chosen Hamiltonian but silent about reality* - it cannot tell you the water model is wrong. *Experimental $pK_a$/hydration sets (FreeSolv, SAMPL, SNase variants) are reality but confound functional error with force-field error.* A functional tuned to reproduce experiment through a biased water model is confident-but-wrong: it will fail on any new solute where the two errors do not cancel. The mandatory guard is a frozen train/test split committed by SHA-256 before evaluation, plus a *prospective* set of solutes/residues whose explicit-solvent reference is computed only after the functional is frozen. Report both metrics side by side: (a) error vs explicit-solvent reference (the resolution metric), and (b) error vs experiment (the downstream, force-field-limited metric), never collapsing them into one number.

## 3. Graded partial-result targets

Ordered milestones; each names its verifier and certificate.

- **P1 - Certified reproduction of an implicit-vs-explicit comparison.** Reproduce a published GB-OBC or PB hydration-free-energy comparison for a handful of FreeSolv neutrals *with our own convergence-certified explicit-solvent references* (independent $\lambda$ windows, BAR overlap matrix, block-averaged error bars $\le 0.1$ kcal/mol). *Verifier:* our explicit-solvent TI/FEP. *Certificate:* the reference outputs, overlap diagnostics, a standalone re-weighting checker, and the implicit-model evaluation script. Establishes the toolchain.
- **P2 - Certified $pK_a$ on a benchmark with error bars.** Compute explicit-solvent alchemical $\Delta pK_a$ for a curated set of SNase internal-residue variants (or an equivalent standard set - *verify which sets are canonical*), each with a converged deprotonation free energy and reported statistical error. *Verifier:* alchemical TI on the fixed Hamiltonian. *Certificate:* per-residue $\lambda$-schedules, cycle-closure residuals, replica agreement.
- **P3 - A learned solvation functional beating a held-out set.** Train $\mathcal{F}_\theta$ (GNN or $\Delta$-GB) to reproduce explicit-solvent $\Delta G_{\mathrm{hyd}}$ and show it improves on the best classical GB/PB baseline on a **frozen held-out** split, hitting the section-1 tolerance. *Verifier:* explicit-solvent reference on the held-out solutes. *Certificate:* the committed split hash, both metrics (vs reference and vs experiment), and an ablation showing the gain is not from test leakage. Benchmark-integrity guard mandatory.
- **P4 - Constant-pH consistency test.** Run constant-pH MD (continuous CpHMD or discrete/replica-exchange) on a titratable group and show the titration curve's inferred $pK_a$ agrees, within error, with the *independent* alchemical TI $\Delta pK_a$ for the identical Hamiltonian, and that the curve obeys Henderson–Hasselbalch with a Hill coefficient consistent with the coupling structure. *Verifier:* two independent free-energy routes (titration-curve fit vs alchemical TI) that must agree. *Certificate:* both estimates, the titration data, and the Hill-fit residuals.
- **P5 - Charged-solute and multi-site coupling.** Extend P3 to ions and formally charged solutes with documented finite-size/Ewald corrections, and to proteins with coupled titratable pairs where the naive single-site picture fails. *Verifier:* explicit-solvent reference with corrections; coupled-site alchemical free energies. *Certificate:* correction terms itemized; coupled-site free energies vs reference.
- **P6 - Transferable functional across Hamiltonians.** Strongest short of resolution: a functional validated against explicit-solvent references for *two different water models*, with an honest statement of how much of its accuracy is water-model-specific. *Verifier:* two independent reference sets. *Certificate:* both reference sets, both held-out metrics, and the transfer degradation.

## 4. Known results and prior art

- Generalized Born family: Still, Tempczyk, Hawley, Hendrickson 1990 (original GB); Hawkins–Cramer–Truhlar 1996 (GB-HCT); Onufriev–Bashford–Case 2004 (GB-OBC); Nguyen–Roe–Simmerling ~2013 (GBn2).
- Poisson–Boltzmann solvers: APBS (Baker, Sept, Holst, McCammon ~2001); DelPhi (Honig and co-workers).
- QM continuum: Tomasi, Mennucci, Cammi (PCM, review ~2005); Klamt 1993 (COSMO); Marenich–Cramer–Truhlar 2009 (SMD); the SMx series (Cramer–Truhlar).
- Hydration free-energy benchmark: FreeSolv database (Mobley, Guthrie ~2014) - experimental and calculated hydration free energies for ~640 small molecules. SAMPL blind challenges (Mobley, Gilson organizers) - solvation and host–guest rounds.
- Protein $pK_a$: PROPKA (Li, Robertson, Jensen ~2005; Olsson et al 2011); H++ server (Anandakrishnan, Onufriev, Gordon); the $pK_a$ Cooperative blind prediction and García-Moreno's SNase internal-residue measurements (~2000s–2010s) - the canonical hard cases for buried charges. The PKAD experimental $pK_a$ database (verify version and coverage).
- Constant-pH MD: continuous CpHMD (Lee, Salsbury, Brooks ~2004; Wallace & Shen ~2011); discrete/replica-exchange constant-pH (Mongan, Case, McCammon ~2004; Swails, York, Roitberg ~2014). Reviews by Chen, Shen.
- ML solvation: graph-neural and $\Delta$-learning solvation models; Vermeire & Green ~2021 (SolProp, ML solvation across solvents); directional message-passing hydration models (verify specific architectures and years).
- Water models: TIP3P (Jorgensen et al 1983), TIP4P/2005 (Abascal–Vega 2005), OPC (Izadi, Anandakrishnan, Onufriev 2014), TIP3P-FB / TIP4P-FB (Wang, Martinez, Pande ~2014).

**Status as of mid-2026 - re-verify against current literature before starting any session.**

## 5. Attack plan

`[func]` mode; one workstation with one GPU throughout.

1. **Explicit-solvent reference engine.** OpenMM (Python, GPU) or GROMACS for the alchemical TI/FEP references; soft-core Lennard-Jones, 12–20 $\lambda$ windows, MBAR via `pymbar` with overlap-matrix diagnostics; finite-size electrostatic corrections for charged solutes. Every reference free energy carries a block-averaged error bar and a replica-agreement check. Failure mode: poor $\lambda$-overlap silently biases the reference - the overlap matrix is a gating check, not a diagnostic afterthought.
2. **Classical baselines.** GB-OBC / GBn2 / PB (APBS) evaluated on the identical solute configurations to fix the frontier the learned functional must beat, so any claimed improvement is measured against a real baseline.
3. **Learned functional.** A GNN or $\Delta$-GB correction in PyTorch, trained to the explicit-solvent references with the frozen split committed first. Report both metrics. Failure mode: the model learns water-model artifacts; the prospective set and the second-water-model test (P6) expose this.
4. **$pK_a$ / constant-pH.** Alchemical $\Delta pK_a$ references via the same engine; CpHMD (OpenMM/AMBER) for P4; PROPKA/H++ as fast classical baselines for context. Failure mode: sampling ergodicity - protonation is coupled to slow conformational rearrangement of buried residues; report exchange/mixing diagnostics and treat non-ergodic titrations as unconverged, not as data.
5. **Rare-event / ergodicity guards.** For buried titratable groups, couple constant-pH to enhanced sampling (Hamiltonian replica exchange) and document mixing. State honestly where a single workstation cannot converge a case rather than lowering the bar.

## 6. Verification and auditability requirements

1. **Certified numerics.** Every explicit-solvent reference free energy is reported with a block-averaged statistical error and an MBAR/BAR overlap diagnostic; a reference without overlap and replica-agreement evidence does not count. Convergence certification (block averaging, $\ge 2$ independent replicas, error bars) is the gating step, not a footnote.
2. **Independent verification.** A standalone re-weighting/free-energy checker, written separately from the training and simulation-driver code, recomputes each headline $\Delta G$ and $\Delta pK_a$ from the raw $\lambda$-window samples. Where warranted, a second engine (GROMACS vs OpenMM) reproduces a reference.
3. **Reproducibility.** All force-field files, water model, $\lambda$-schedules, seeds, hyperparameters, and the frozen train/test/prospective splits are recorded with a SHA-256 manifest over every input and artifact; splits are committed before evaluation.
4. **Preservation.** Training code, failed functional forms, and non-converged (discarded) titrations are part of the record; a discarded run is stated with its reason.
5. **Honest reporting.** The report states up front whether the section-1 tolerance was met against the *explicit-solvent reference* (the resolution metric), reports the experiment-comparison metric separately and labels it force-field-limited, and never presents an experiment-matching result as evidence the functional is correct for its Hamiltonian.
