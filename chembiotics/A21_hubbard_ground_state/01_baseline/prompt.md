# PROMPT FOR THE GROUND STATE OF THE 2D SQUARE-LATTICE HUBBARD MODEL

## Neural quantum states with certified variational bounds for the doped Hubbard model

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** A - closed-loop (on-machine verifier)
**Rank:** A-21 of 21
**Source:** chem/bio top-50 list #3, section A (electronic structure)
**Modes:** `[func]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

> **Audit note (July 2026 - see `../../STATUS_AUDIT_2026-07.md`):** SOTA moved in 2025. Pfaffian-based hidden-fermion NQS (arXiv 2511.07566) and transformer NQS (arXiv 2507.02644, Nat. Commun. 2026) resolved much of the metallic/stripe/superconducting energetics - SC coexists with partially-filled stripes for t′ < −0.1; a half-filled stripe appears in the ground state at the studied coupling. The headline "does the ground state superconduct" stays open, but the graded targets below must re-baseline against these 2025 energies, not pre-2024 references.

### Abstract

The two-dimensional square-lattice Hubbard model is the minimal model believed to contain the physics of cuprate high-temperature superconductivity. Its ground state - in particular the competition between stripe (charge/spin density wave) order and uniform $d$-wave superconductivity near optimal doping - is one of the most contested questions in condensed-matter physics, and settling the energetics is a genuine open problem. Neural quantum states (NQS) in the Carleo–Troyer lineage - now transformer- and CNN-based - have reached energies competitive with the best tensor-network and Monte Carlo methods for this model. This is deliberately the **lowest-priority Pack A item and the most "big-lab-adjacent"**: large groups compete hard here, and a single session will not settle the cuprate question. The framing is therefore modest and the graded targets are the product. The **on-machine verifier is rigorous and clean**: any variational wavefunction gives a *rigorous upper bound* to the ground-state energy, computed on-machine, and results are benchmarked against DMRG, AFQMC, and constrained-path methods where the sign is controlled. Anything short of the section-2 standard is reported as a partial result, never as a solution.

## 1. Exact problem statement

**The model.** The single-band Hubbard Hamiltonian on an $L\times L$ square lattice:

\[
H = -t\!\!\sum_{\langle i j\rangle,\sigma}\!\big(c^\dagger_{i\sigma}c_{j\sigma} + \text{h.c.}\big)
    + U\sum_i n_{i\uparrow}n_{i\downarrow}
    - \mu\sum_{i\sigma} n_{i\sigma},
\]

with nearest-neighbor hopping $t$ (energy unit; set $t=1$), on-site repulsion $U/t$, and filling $n = \langle N\rangle/L^2$ (or hole doping $\delta = 1-n$) fixed by $\mu$ or by working in a fixed particle-number sector. A next-nearest hopping $t'$ is included when stated (it matters for realism and for stripe vs SC balance). Boundary conditions (periodic / cylindrical), lattice size $L$, $U/t$, $t'/t$, and doping $\delta$ are **all stated explicitly** for every result - the answer depends on all of them.

**The targets.**
- *Ground-state energy per site* $e_0(L, U/t, t'/t, \delta)$ in units of $t$, in a fixed particle-number/momentum sector.
- *Order parameters:* the $d$-wave pairing correlation / order parameter, the charge- and spin-density-wave (stripe) order parameters and their periods, extracted from the variational state with statistical error bars.
- *Energetic ordering:* for contested regimes, the sign and magnitude of the energy difference between competing states (e.g. striped vs uniform-SC) at matched $(L, U/t, t', \delta)$.

**Admissible class.** A variational wavefunction $|\psi_\theta\rangle$ (neural quantum state: RBM, CNN, transformer/attention, autoregressive, or backflow/Jastrow–Slater–NQS hybrids) with computable amplitudes, sampled by variational Monte Carlo (VMC). The *only* rigorous guarantee it carries is the variational upper bound $E[\psi_\theta] = \langle\psi_\theta|H|\psi_\theta\rangle/\langle\psi_\theta|\psi_\theta\rangle \ge E_0$.

**Accuracy threshold (numeric).** Energies are reported as $e_0$ per site in units of $t$ with the VMC statistical error bar; the target is a *rigorous variational upper bound at least as low as* a stated published reference value at matched $(L, U/t, t', \delta, \text{BC})$, with the improvement (if any) stated in units of $t$ per site and exceeding the combined error bars. Order parameters are reported with error bars and finite-size context. No informal "competitive accuracy" without the numeric per-site energy and its error.

## 2. Resolution standard

Given the modest framing, "resolution" of the *full* physics question (the thermodynamic-limit phase near optimal doping) is explicitly out of reach for a session. The section-2 standard is therefore a *rigorous, benchmarked, certifiable* result at stated parameters:
- a variational upper bound reproducing or improving a published NQS/tensor-network/QMC energy at matched parameters, with the bound and its error bar certified on-machine; and/or
- a statistically certified order-parameter characterization or energetic ordering on a stated finite cluster, benchmarked against DMRG/AFQMC where those are reliable.

**Not accepted as resolution:**
- An energy quoted without stated $(L, U/t, t', \delta, \text{BC})$ and without a VMC error bar - the number is meaningless otherwise.
- A claimed "lower energy" within the error bars of the reference (not a certified improvement).
- An extrapolation to the thermodynamic limit or a claim about the *real* cuprate phase diagram from finite clusters - finite-size and the $U\to$realistic, $t'$-dependent subtleties forbid it in one session.
- An order parameter reported without error bars or without finite-size context (spurious order from a too-small cluster or a biased ansatz).
- A benchmark energy match on a *sign-free* or easy regime presented as resolving the *doped* (sign-problematic) regime where the controversy lives.
- Any presentation of a single-cluster energetic ordering as settling stripe-vs-SC in the thermodynamic limit.

**Benchmark-integrity clause.** The variational bound is rigorous (a real strength), but the surrounding benchmarks are biased. Named biases: (i) *Ansatz bias* - an NQS can favor whichever competing state it represents best, biasing the energetic *ordering* even when each individual energy is a valid bound; guard is to represent *both* competing states with comparably expressive ans\"atze and compare only matched-quality bounds, reporting the ansatz for each. (ii) *AFQMC/constrained-path sign bias* - in the doped regime the QMC benchmarks themselves rely on constraints (constrained-path, phaseless) that introduce an *uncontrolled* systematic error; a "benchmark" agreement can be agreement with a biased method. Guard: state which benchmarks are sign-controlled vs sign-constrained, and treat constrained-path numbers as references-with-bias, not ground truth. (iii) *Finite-size bias* - small clusters over- or under-stabilize stripes; guard is to report at least the size dependence over the accessible $L$, never a single cluster. A lower variational energy is always trustworthy as a *bound*; any *physics* claim (ordering, phase) carries these guards or is flagged as confident-but-wrong.

## 3. Graded partial-result targets

**P1 - Reproduce a published NQS energy with a verified variational bound.** For a stated $(L, U/t, t', \delta, \text{BC})$ with a published NQS/DMRG energy, train an NQS and reproduce the energy per site within combined error bars, with the bound certified (the energy is a genuine $\langle H\rangle$ upper bound, VMC error bars validated by binning). *Certificate:* the per-site energy with error bar; VMC autocorrelation/binning report; match to the published reference.

**P2 - Certified energy improvement at a stated point.** At a stated (ideally contested) $(L, U/t, t', \delta)$, produce a variational upper bound *lower* than the best published value by more than the combined error bars. *Certificate:* the improved bound with error bar; the reference value; the gap exceeding combined uncertainty; ansatz and optimizer fully specified.

**P3 - Order-parameter characterization with statistical certification.** On a stated cluster, characterize the ground-state order (stripe period, $d$-wave pairing correlations, spin structure) with error bars and a finite-size analysis over accessible $L$. *Certificate:* order parameters with jackknife error bars; size dependence; comparison to DMRG on cylinders where available.

**P4 - A resolved energetic ordering on a small cluster.** For a specific small cluster and parameters, certify the sign of the energy difference between two competing states (e.g. striped vs uniform) using matched-quality variational bounds and, where possible, a corroborating method. *Certificate:* both bounds with error bars, the certified sign of the difference, matched ansatz expressiveness argued explicitly, and the finite-size caveat stated.

**P5 - Cross-method consistency map.** Assemble, at a set of stated points, a consistency comparison across NQS (upper bound), DMRG (near-exact on cylinders of accessible width), and AFQMC/constrained-path (with its bias band), documenting where they agree and where the doped-regime disagreement lives. *Certificate:* the multi-method table with each method's error/bias character labeled.

## 4. Known results and prior art

- Hubbard (1963); Anderson (1987) - the model and its proposed link to cuprate superconductivity.
- Carleo & Troyer (2017) - neural quantum states (RBM) for quantum many-body ground states; the founding NQS result.
- Simons Collaboration on the Many-Electron Problem - LeBlanc et al. (2015) and Zheng et al. (2017, *Science*) - multi-method benchmark of the 2D Hubbard model; the stripe-ordered ground state at $U/t=8$, $1/8$ doping established by agreement of DMRG, AFQMC, iPEPS, DMET.
- Modern NQS for Hubbard: transformer/attention and CNN ans\"atze, autoregressive NQS, and backflow/hidden-fermion approaches - Nomura, Imada; Luo & Clark (hidden fermion / backflow, 2019–); Moreno, Carleo, Georges; von Delft/Schmitt and others; recent transformer-NQS reaching competitive doped-Hubbard energies (verify - this area moves fast and specific rankings change).
- Tensor networks / QMC benchmarks: DMRG on cylinders (White, Scalapino; Chan group); AFQMC and constrained-path/phaseless AFQMC (Zhang, Krakauer); iPEPS (Corboz); DMET (Chan, Booth). Xu, Zhang, Vitali, Qin, Shi, and the Flatiron/Simons follow-ups on stripes vs superconductivity near optimal doping (verify years).
- Software: NetKet (Carleo, Vicentini and co-workers) - VMC/NQS framework; ITensor / block2 / TeNPy for DMRG; bespoke AFQMC codes; QMCPACK.

*Status as of mid-2026 - re-verify against current literature before starting any session; NQS results for this model change on a months timescale.*

## 5. Attack plan

**Reference/verifier layer.** VMC with **NetKet** (JAX/PyTorch backends) provides the on-machine variational bound and error bars. DMRG references on cylinders via **ITensor** or **block2** where the width is tractable; published AFQMC/constrained-path numbers used as bias-labeled references. Exact diagonalization for the smallest clusters ($4\times4$ and below) gives an exact anchor. A single workstation with one prosumer GPU handles NQS on clusters up to $\sim 8\times8$–$16\times16$ depending on ansatz; DMRG cylinder width is the memory bottleneck.

**NQS layer `[func]`.** Implement competitive ans\"atze in NetKet: a CNN or transformer/attention backbone, optionally autoregressive for exact sampling, and a backflow/hidden-fermion Slater–NQS hybrid (which encodes fermionic sign structure well). Optimize with stochastic reconfiguration (natural gradient) / SR-based methods; fix particle number and, where relevant, momentum/spin sectors. For P4, build *two* ans\"atze biased toward each competing state (e.g. pinned-stripe vs uniform initial conditions) with matched expressiveness.

**Certification layer.** Every energy is $\langle H\rangle$ with a binned/jackknife error bar and a reported integrated autocorrelation time; the bound property is automatic (it is a real expectation value) but the *error bar's* validity is checked by binning convergence. Order parameters and their finite-size trends are computed with the same statistical care.

**Expected failure modes.** (i) Underestimated error bars from autocorrelation - validate by binning. (ii) Optimizer stuck in a metastable (e.g. wrong stripe period) minimum, giving a valid but non-optimal bound mistaken for the ground state - restart from multiple initializations. (iii) Ansatz bias skewing the *ordering* in P4 - match expressiveness and report the ansatz. (iv) Over-reading finite clusters as thermodynamic-limit physics - always report size dependence. (v) Treating constrained-path AFQMC as ground truth in the doped regime where it is itself biased.

## 6. Verification and auditability requirements

1. **Exact or certified numerics.** Every energy is a rigorous variational upper bound reported with a binning/jackknife-validated error bar and integrated autocorrelation time; improvements over references must exceed combined error bars; order parameters carry error bars and finite-size context. Floating-point training curves are not the reported result.
2. **Independent verification.** A standalone estimator - separate from the training code - recomputes $\langle H\rangle$ and observables from stored samples/weights and reproduces the error bars; the smallest clusters are checked against exact diagonalization; DMRG references reproduced with a second code where feasible.
3. **Reproducibility.** All of $(L, U/t, t'/t, \delta, \text{BC}, \text{sector})$, ansatz architecture and size, optimizer/SR settings, seeds, sampling parameters, and the reference values compared against are recorded; SHA-256 manifest over all artifacts.
4. **Preservation.** NQS training code, optimized weights, sampling logs, and reference-calculation inputs are part of the record. Anything not preserved is stated explicitly.
5. **Honest reporting.** The report states up front that the full physics question (thermodynamic-limit doped phase) is *not* addressed, always states the full parameter tuple and error bars, distinguishes a rigorous *energy bound* from any *physics* claim, labels each benchmark method's bias character (sign-controlled vs constrained), and never presents a finite-cluster energetic ordering as settling stripe-vs-superconductivity.
