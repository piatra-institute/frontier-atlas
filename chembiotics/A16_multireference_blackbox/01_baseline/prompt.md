# PROMPT FOR A BLACK-BOX MULTIREFERENCE METHOD

## Automatic active-space selection and static-correlation capture for strongly correlated molecules

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** A - closed-loop (on-machine verifier)
**Rank:** A-16 of 21
**Source:** chem/bio top-50 list #6, section A (electronic structure)
**Modes:** `[algo]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Single-reference methods (DFT, MP2, CCSD(T)) fail qualitatively when a molecule has strong static correlation: stretched and breaking bonds, diradicals, transition-metal centers, catalytic intermediates. The correct tool is a multireference method (CASSCF, CASPT2, NEVPT2, DMRG), but it is *not* black-box - it requires an expert to choose the active space (the set of near-degenerate orbitals treated exactly), and a poor choice gives wrong answers with no warning. This human-in-the-loop step is the perennial bottleneck blocking routine strong-correlation chemistry. The task is an **algorithm** that selects the active space automatically and captures static correlation with a *verifiable success criterion* across a molecule class - turning the black art into a black box. The **on-machine verifier** is energies (and other observables) versus full-CI on small systems and versus large-bond-dimension DMRG on larger ones, both computable by the session itself. Anything short of the section-2 standard is reported as a partial result, never as a solution.

## 1. Exact problem statement

**Reference method (ground truth).** For each benchmark system:
- *Small:* full configuration interaction (FCI) total energy in a converged basis - exact within the basis.
- *Larger:* density-matrix renormalization group (DMRG) at a bond dimension large enough that the energy is converged to a stated tolerance (extrapolated in discarded weight / bond dimension $M$), serving as the near-exact reference where FCI is infeasible.
Relative energies (bond-dissociation curves, spin-state gaps, reaction/barrier energies) are the primary targets because they are what strong correlation gets wrong.

**The algorithm to produce.** A procedure $\mathcal A$ that, given a molecule (geometry, charge, spin) and a basis, *automatically*:
1. Selects an active space - a subset of orbitals and electrons $(n, m)$ - with no human input beyond declared, system-independent hyperparameters;
2. Runs the multireference calculation (CASSCF/CASPT2/NEVPT2/DMRG-SCF) in that space;
3. Returns the energy (and requested observables) **with a self-reported reliability signal** (e.g. a diagnostic that flags when the chosen space is insufficient).

**Admissible class.** Any deterministic (or seed-fixed) selection algorithm: entropy/occupation-based (natural-orbital occupations, orbital entanglement entropy from a cheap DMRG pre-pass), AVAS-style projection onto atomic valence characters, energy-based ranking, or an ML selector - provided its inputs are computable and its hyperparameters are fixed *across the whole molecule class* (not retuned per molecule).

**Accuracy threshold (numeric).** For a stated molecule class, the automatically selected calculation must reproduce the reference relative energies within a stated tolerance - target **$1\,\mathrm{kcal/mol}$ ($\approx 1.6\,\mathrm{mHartree}$)** MAE on relative energies (or a stated eV tolerance for spin-state gaps / excitations) - for a stated fraction of the class (e.g. $\ge 90\%$), with the reliability signal correctly flagging the remainder. "Correct active space" is defined operationally by this energy criterion plus stability (see section 2), never by matching a human's choice.

## 2. Resolution standard

Full resolution is an algorithm $\mathcal A$ with *fixed* hyperparameters that meets the section-1 threshold on a *held-out* molecule class (spanning bond-breaking, spin-state, and transition-metal cases), where the reliability signal reliably separates the successes from the failures. Deliverable: the algorithm, the reference calculations, the held-out class results, and the calibration of the reliability signal.

**Not accepted as resolution:**
- Per-molecule hyperparameter tuning - the active-space threshold must be fixed across the class; retuning is choosing the space by hand in disguise.
- Matching a *published expert* active space rather than reproducing the reference *energy* - the energy is the criterion; a "correct-looking" space that gives a wrong energy is a failure.
- Success on equilibrium geometries only, where static correlation is weak and almost any space works - bond-breaking / genuinely strongly correlated points must be in scope.
- A method with no reliability signal (silent failure is the exact problem being solved).
- Good energies from a space that is unstable - a slightly perturbed geometry or basis flips the selected orbitals and the energy jumps discontinuously along a curve.
- A single-molecule or single-metal success presented as a general black-box method.

**Benchmark-integrity clause.** The verifier (FCI / converged DMRG) is strong but biased. Named biases: (i) *DMRG convergence bias* - an under-converged DMRG reference (too-small bond dimension) is itself wrong, especially for the hardest, most strongly correlated cases where the reference is most needed; the reference must be extrapolated in $M$/discarded weight with a reported uncertainty smaller than the claimed tolerance. (ii) *Class-selection bias* - an algorithm can be tuned on an easy, homogeneous set (e.g. organic diradicals) and fail on transition metals; guard is a held-out class deliberately spanning distinct strong-correlation mechanisms, with results reported per subclass. (iii) *Smoothness bias* - energies can look accurate at sampled points yet the potential curve is discontinuous where the active space switches; guard is a continuity check along at least one full dissociation coordinate. A per-point benchmark win with a discontinuous curve or an under-converged reference is flagged as confident-but-wrong.

## 3. Graded partial-result targets

**P1 - Reproduce automated-active-space results on a benchmark with our pipeline.** Run an existing automated selector (AVAS, atomic-valence active space; or entropy-based selection) on a published benchmark set and reproduce its active spaces and energies, *and* independently confirm the references with our own FCI/DMRG. *Certificate:* matching selected spaces/energies; references reproduced with quantified convergence.

**P2 - Certified energy accuracy vs DMRG on small systems.** For a set of small strongly-correlated systems, run an automated selection + multireference calculation and certify the relative-energy error against extrapolated DMRG (and FCI where feasible). *Certificate:* held-out relative-energy CDF vs converged references; DMRG extrapolation uncertainty reported.

**P3 - Automated selection with a verifiable success criterion across a class.** Deliver $\mathcal A$ with fixed hyperparameters meeting the threshold on a stated molecule class, with a reliability diagnostic calibrated to flag failures. *Certificate:* held-out class error per subclass; ROC/calibration of the reliability signal separating success from failure.

**P4 - Continuity and stability along reaction coordinates.** Demonstrate that $\mathcal A$ produces smooth, continuous potential energy curves through bond dissociation (no active-space-switch discontinuities) for a set of bond-breaking cases. *Certificate:* full dissociation curves vs reference with a continuity metric; no spurious jumps above tolerance.

**P5 - Failure-mode characterization.** Map where $\mathcal A$ breaks - which strong-correlation mechanisms, sizes, or spin states defeat it - and show the reliability signal catches these cases. *Certificate:* a characterized failure boundary with the reliability signal's true/false-positive rates on it.

## 4. Known results and prior art

- Roos (1980s) - CASSCF and the complete-active-space concept; Andersson, Malmqvist, Roos (1990s) - CASPT2. Angeli, Cimiraglia, Malrieu (2001–2002) - NEVPT2.
- White (1992) - DMRG; Chan & Head-Gordon (2002), Chan and co-workers, Reiher and co-workers (Legeza, Marti, Keller) - ab initio DMRG and quantum-chemical DMRG (Block, CheMPS2, QCMaquis).
- Sayfutyarova, Sun, Chan, Knizia (2017) - AVAS (atomic valence active space): automated selection by projection onto atomic valence orbitals. Knizia (2013) - IBO/IAO intrinsic bonding orbitals underpinning AVAS.
- Stein & Reiher (2016–2019) - automated active-space selection via orbital entanglement entropy (single-orbital entropy, mutual information) from a cheap DMRG pre-pass; the "autoCAS" program.
- Keller, Boguslawski, Janowski, Reiher, Pulay - selecting active orbitals from correlation measures. Bao, Truhlar and co-workers - automated active spaces (e.g. via unrestricted natural orbitals; the "Auto-CAS"/related schemes, verify).
- ML active-space selection - several groups have proposed learned selectors (verify specific attributions; this area moves quickly and claims should be checked).
- Diagnostics of multireference character: the $\mathcal T_1$/$D_1$ diagnostics (Lee), the $M$-diagnostic, natural-orbital occupation spread, and DMRG entropy as reliability signals.
- Software: PySCF (CASSCF, AVAS, DMRG interfaces), OpenMolcas (CASSCF/CASPT2, autoCAS interface), Block2 / CheMPS2 / QCMaquis (DMRG), ORCA (CASSCF/NEVPT2/DMRG).

*Status as of mid-2026 - re-verify against current literature before starting any session.*

## 5. Attack plan

**Reference/verifier layer.** FCI with **PySCF** for small systems; DMRG with **Block2** (or CheMPS2 / QCMaquis) converged and extrapolated in bond dimension for larger references, with a reported extrapolation uncertainty. Assemble a benchmark class spanning distinct mechanisms: single/multiple bond dissociation (H$_2$, N$_2$, F$_2$, C$_2$), diradicals, and a first-row transition-metal set (e.g. spin-state gaps of Fe/Co complexes' model systems). A single workstation covers FCI to $\sim 16$ orbitals and DMRG references for active spaces up to $\sim 30$–$50$ orbitals depending on entanglement.

**Selection-algorithm layer `[algo]`.** Implement and compare selectors with *class-fixed* hyperparameters: AVAS (projection thresholds), entropy-based (single-orbital entropy cutoff from a cheap low-$M$ DMRG pre-pass), and natural-orbital-occupation ranking; optionally an ML selector trained on labeled (space → reference-accuracy) pairs. Every selector's hyperparameters are frozen across the whole class before held-out evaluation. Feed the selected space to CASSCF→CASPT2/NEVPT2 or DMRG-SCF.

**Reliability-signal layer.** Attach a diagnostic (residual entropy outside the active space, occupation of the highest included / lowest excluded natural orbital, or a perturbative correction magnitude) and calibrate it against actual reference error to build the success/failure classifier.

**Continuity layer.** Run full dissociation scans and measure curve continuity; detect active-space-switch discontinuities.

**Expected failure modes.** (i) Under-converged DMRG reference on the hardest cases - extrapolate and report uncertainty first. (ii) Hidden per-molecule tuning creeping in via "adjusted" thresholds - freeze them. (iii) Active-space switching along a curve producing discontinuities that per-point metrics miss. (iv) An algorithm that works for organic diradicals but not transition metals (different entanglement structure) - the held-out class must span both. (v) A reliability signal that is well-calibrated on the training class but not held-out.

## 6. Verification and auditability requirements

1. **Exact or certified numerics.** Accuracy claims are held-out relative-energy errors vs FCI / bond-dimension-extrapolated DMRG whose convergence uncertainty is quantified and smaller than the claimed tolerance; continuity is a computed metric along a coordinate. Reliability-signal performance is reported as calibration/ROC, not asserted.
2. **Independent verification.** A standalone runner - separate from the selection code - takes the algorithm's chosen space, recomputes the multireference energy in a second code (PySCF vs OpenMolcas vs ORCA), and re-evaluates errors; a subset of DMRG references is reproduced with a second DMRG code.
3. **Reproducibility.** Class-fixed hyperparameters, benchmark composition, held-out split (frozen before evaluation), seeds, DMRG bond dimensions and extrapolation, code versions, and convergence thresholds are recorded; SHA-256 manifest over all artifacts.
4. **Preservation.** Selection code, calibration data for the reliability signal, and reference-generation inputs are part of the record. Anything not preserved is stated explicitly.
5. **Honest reporting.** The report states up front whether $\mathcal A$ met the threshold on the held-out class with a *fixed* hyperparameter set, reports per-subclass results and the reliability signal's false-negative rate (silent failures are the whole point), shows continuity along at least one dissociation, and never presents equilibrium-geometry success or per-molecule tuning as a black-box method.
