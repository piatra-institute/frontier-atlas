# PROMPT FOR COARSE-GRAINING THAT PRESERVES THERMODYNAMICS AND KINETICS

## A CG force field correct in structure, free energy, AND rates simultaneously - certified against all-atom reference

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Pack:** A - closed-loop (on-machine verifier)  
**Rank:** A-18 of 21  
**Source:** chem/bio top-50 list #15, section B (free energy, dynamics, sampling)  
**Modes:** `[func]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Coarse-graining replaces groups of atoms by effective sites to reach longer length and time scales. The persistent, crisp failure is that a coarse-grained (CG) model tuned to reproduce all-atom *structure* (radial distribution functions) generally gets *thermodynamics* wrong (pressure, free energies) and *kinetics* wrong (rates, diffusion), and a model fixed for one breaks another - the representability and transferability problem. Getting thermodynamics AND kinetics right *simultaneously* is the hard target, and it is well-posed because integrating out degrees of freedom provably changes the dynamics (removing friction and memory speeds the CG system up), so kinetic consistency requires more than a potential of mean force. This prompt fixes the on-machine verifier at the one place it is exact: for a fixed all-atom Hamiltonian, **the all-atom reference simulation defines the target structural, thermodynamic, AND kinetic observables**, and a CG model is judged by reproducing all three under the same mapping. The honesty spine: **"correct" means "reproduces the all-atom reference for this force field," not "matches experiment"** - the all-atom model is the ground truth here, and its own error vs reality is a separate matter. Anything short of section 2 is a partial result.

## 1. Exact problem statement

**System class.** Systems where an all-atom reference is affordable and a CG model is meaningful: molecular liquids (water, methanol), simple polymers, and small peptides. Declared per run, with the CG mapping stated.

**All-atom reference (fixed and named).** A stated all-atom force field and water model define $U_{\text{AA}}(x)$ and the reference dynamics (stated integrator, thermostat, friction). All target observables are computed from a converged all-atom trajectory.

**CG mapping.** A fixed linear mapping $M:\mathbb{R}^{3N}\to\mathbb{R}^{3n}$ ($n\ll N$) from atomistic coordinates $x$ to CG coordinates $R=Mx$ (e.g. center-of-mass of each bead). The mapping is part of the problem statement.

**Consistency conditions (what a correct CG model must satisfy).**
- *Thermodynamic (structural) consistency:* the CG equilibrium distribution equals the mapped all-atom distribution,
$$
p_{\text{CG}}(R) = \int \delta\big(M x - R\big)\, p_{\text{AA}}(x)\, dx,
$$
so the exact CG potential is the many-body potential of mean force (PMF) $U_{\text{CG}}(R) = -k_BT\ln p_{\text{CG}}(R) + \text{const}$. This makes CG RDFs, mapped free-energy differences, and mapped populations match the reference.
- *Kinetic consistency:* the CG dynamics must reproduce the mapped all-atom kinetic observables (autocorrelation times, diffusion coefficients, mean-first-passage times between CG metastable states). Because integrating out fast degrees of freedom removes friction and introduces memory, a Markovian CG model on $U_{\text{CG}}$ generically runs too fast; kinetic consistency requires a friction/memory term - a generalized Langevin equation (GLE) with a memory kernel (Mori–Zwanzig), or an explicitly calibrated friction.

**Target - simultaneous consistency (the hard object).** A CG model (potential $U_{\text{CG}}$ *plus* a friction/memory specification) that reproduces, under one fixed mapping and one fixed parameterization, the all-atom reference's structural, thermodynamic, and kinetic observables *at once*.

**Accuracy thresholds (numeric).**
- *Structural:* CG RDFs match mapped all-atom RDFs with integrated absolute deviation below a stated tolerance (e.g. RDF RMSD $\le 0.02$ over the first three solvation shells).
- *Thermodynamic:* a mapped free-energy difference (or pressure at a stated density) matches the reference to $\le 0.5$ kcal/mol (or a stated pressure tolerance).
- *Kinetic:* a target kinetic observable (diffusion coefficient, dominant relaxation time, or an inter-state MFPT) matches the reference *after* the friction/memory correction, to within a stated relative tolerance (e.g. $\le 20\%$), with the uncorrected (Markovian) model's discrepancy reported alongside to show the correction is doing the work.

No informal target ("captures the physics", "good agreement") is accepted without these.

## 2. Resolution standard

A resolution, for a stated system, mapping, and all-atom Hamiltonian, consists of:

1. A CG model (potential + friction/memory) that **simultaneously** meets the structural, thermodynamic, and kinetic tolerances above against the converged all-atom reference under the fixed mapping.
2. Explicit demonstration that the kinetic term is necessary - the same potential run as a plain Markovian CG model fails the kinetic tolerance, and the memory/friction correction fixes it.
3. A transferability statement: the model's performance at a **held-out** state point (different temperature or density) it was not fit to, quantified, with honest reporting of degradation.

**Not accepted as resolution:**

- A CG model matching RDFs only, presented as solving coarse-graining (structure-only matching is the classical partial result and generally breaks thermodynamics/kinetics).
- Thermodynamic + structural consistency with the kinetics either ignored or "fixed" by an unphysical global time-rescaling factor fit to the answer (a single scalar time-rescale is not kinetic consistency unless shown to be state-transferable and derived, not fit).
- A model fit and tested at a single state point, presented as transferable.
- Kinetic agreement claimed without reporting the uncorrected model's failure (so the reader cannot tell the correction is real).
- Matching *experimental* observables while skipping the all-atom-reference comparison (the all-atom model is the ground truth here; experiment is downstream).

**Benchmark-integrity clause.** The all-atom reference verifier is exact for the all-atom Hamiltonian and is the correct ground truth for CG-representability - but two guards apply. (i) *The reference must be converged*: structural, thermodynamic, and especially kinetic observables need independent-replica agreement and block-averaged errors before they are trusted as targets (kinetic observables converge slowly). (ii) *Transferability is the teaching-to-the-test guard*: a CG model fit at one state point and validated only there can hide a fit that memorizes that state; a frozen, hash-committed held-out state point (temperature/density) fit *before* evaluation is mandatory, and its degradation reported. Finally, the on-machine claim ("reproduces the all-atom reference") is kept separate from any experiment comparison - the CG model inherits the all-atom force field's own error vs reality, which is not this problem's concern.

## 3. Graded partial-result targets

- **P1 - Reproduce an MS-CG model matching all-atom RDFs.** Build a force-matched (multiscale CG) model for a molecular liquid and reproduce the mapped all-atom RDFs to tolerance. *Certificate:* the CG potential, mapped-AA vs CG RDFs with the reference converged (replica agreement), and the force-matching residual. Establishes the toolchain. (Structure-only; explicitly a partial result.)
- **P2 - Certified thermodynamic consistency on a target.** Extend P1 (or use relative-entropy minimization) to also match a mapped free-energy difference and the pressure/density to tolerance, showing the structure-only model's thermodynamic error and the corrected model's agreement. *Certificate:* thermodynamic observables vs converged reference, and the before/after comparison.
- **P3 - A CG model provably preserving a target kinetic observable (with memory kernel).** Add a GLE/friction term (Mori–Zwanzig memory kernel extracted from the all-atom reference) and reproduce a target kinetic observable (diffusion coefficient or relaxation time), *with the uncorrected Markovian model's discrepancy reported* to prove the memory term is doing the work. *Certificate:* the extracted memory kernel, corrected vs uncorrected kinetic observable, both vs the converged reference. This is the crux.
- **P4 - Simultaneous thermo + kinetics.** Deliver one model meeting the structural, thermodynamic, AND kinetic tolerances at once at a single state point - the hard, crisp target short of transferability. *Certificate:* all three observable classes vs reference, from one fixed parameterization.
- **P5 - Transferability across state points.** Strongest short of resolution: the P4 model evaluated at a held-out temperature/density it was not fit to, with quantified degradation and an honest transferability statement. *Certificate:* frozen held-out state-point hash, all-observable comparison there, and the degradation report.

## 4. Known results and prior art

- Force matching / multiscale CG (MS-CG): Izvekov & Voth 2005; Noid, Chu, Ayton, Krishna, Izvekov, Voth, Andersen, Das 2008 (the two-part "multiscale coarse-graining" theory papers - representability and the CG PMF/consistency conditions).
- Relative-entropy minimization: Shell 2008 (the relative-entropy framework for CG); Chaimovich & Shell.
- Structure-based inversion: (iterative) Boltzmann inversion; inverse Monte Carlo (Lyubartsev & Laaksonen ~1995).
- Top-down CG: MARTINI (Marrink, Risselada, Yefimov, Tieleman, de Vries ~2007) - transferable but not derived from all-atom consistency; a contrast case.
- Dynamical consistency / memory: Mori–Zwanzig formalism; generalized Langevin equations for CG; Hijón, Español, Vanden-Eijnden, Delgado-Buscalioni 2010 (Mori–Zwanzig for CG dynamics); Izvekov & Voth (CG with friction). Memory-kernel extraction methods (verify current standards).
- ML CG potentials: CGnets (Wang, Olsson, Clementi, Noé, ... 2019 - machine-learning of CG free-energy surfaces); graph-neural CG potentials; Clementi–Noé line of work; flow/score-based CG (verify recent).
- Time-scale mapping / dynamical rescaling discussions: reviews by Voth, by Español, by Clementi on why CG dynamics are accelerated and what consistency requires.

**Status as of mid-2026 - re-verify against current literature before starting any session.**

## 5. Attack plan

`[func]` mode; one workstation, one GPU.

1. **All-atom reference.** OpenMM/GROMACS long MD at the stated state point(s); converge structural, thermodynamic, and (slowest) kinetic observables with independent-replica agreement and block-averaged errors. Kinetic observables are the binding constraint on reference cost - state the limit honestly.
2. **CG potential.** Force matching (MS-CG) and/or relative-entropy minimization (both available in VOTCA / OpenMSCG-style tooling, or from scratch in PyTorch for an ML CG potential - CGnets-style free-energy surface). The potential targets the many-body PMF (thermodynamic consistency).
3. **Memory/friction (the crux, P3).** Extract a Mori–Zwanzig memory kernel from the all-atom reference (projected velocity autocorrelation / orthogonal-force correlation), parameterize a GLE, and integrate the CG model with memory. Failure mode: substituting a single fitted global time-rescale for real memory - forbidden as resolution; the transferability test exposes it.
4. **Simultaneity and transferability.** Verify all three observable classes from one parameterization (P4), then evaluate at a frozen held-out state point (P5). Failure mode: a model that meets thermo and kinetics only because they were co-fit at one state point - the held-out state point is the guard.
5. **Reporting the correction's necessity.** Always report the uncorrected (Markovian) model's kinetic error beside the corrected one, so the memory term's contribution is visible.

## 6. Verification and auditability requirements

1. **Certified numerics.** All reference observables (structural, thermodynamic, kinetic) carry block-averaged errors and independent-replica agreement; CG observables carry the same; the kinetic claim reports corrected vs uncorrected with errors. An observable without convergence evidence is not a target.
2. **Independent verification.** The observable-computation and memory-kernel-extraction code is separate from the CG-parameterization code; a standalone checker recomputes the headline structural/thermodynamic/kinetic observables from stored trajectories; a second method (force matching vs relative entropy) reproduces at least the potential-level result.
3. **Reproducibility.** All-atom force field, water model, CG mapping, parameterization method and hyperparameters, memory-kernel extraction settings, seeds, and the frozen held-out state point are recorded with a SHA-256 manifest; the held-out state point is committed before evaluation.
4. **Preservation.** CG-parameterization code, failed potentials, discarded memory-kernel forms, and unconverged reference attempts (with reasons) are part of the record.
5. **Honest reporting.** The report states up front whether structural, thermodynamic, AND kinetic tolerances were met *simultaneously* against the converged all-atom reference, reports the uncorrected-model kinetic failure beside the corrected result, reports held-out-state-point degradation, keeps the all-atom-reference (on-machine) claim separate from any experiment comparison, and never presents a structure-only or single-state-point model as solving coarse-graining.
