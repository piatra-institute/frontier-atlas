# PROMPT FOR CURING THE FERMION SIGN PROBLEM ON SPECIFIC HAMILTONIANS

## Learned contour deformations and sign-free bases for named model Hamiltonians - under an explicit NP-hardness ceiling

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** A - closed-loop (on-machine verifier)
**Rank:** A-20 of 21
**Source:** chem/bio top-50 list #2, section A (electronic structure)
**Modes:** `[func]` `[algo]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Quantum Monte Carlo (QMC) is the workhorse for correlated fermions and dense matter, but for most fermionic and frustrated systems it suffers the **sign problem**: the statistical weights are not positive, the average sign decays exponentially in system size and inverse temperature, and the variance explodes. There is a hard ceiling on ambition here that this prompt states first and keeps in view: **the general sign problem is NP-hard (Troyer & Wiese, 2005), so no universal cure exists** - a claimed universal solution is, modulo complexity assumptions, wrong. What *is* open and tractable is curing the sign for *specific* Hamiltonians: machine-learned Lefschetz-thimble / contour deformations that reduce the sign fluctuation, and basis or variable changes that render a particular model sign-free (finite-density lattice-QCD toy models, frustrated magnets, the uniform electron gas at target conditions). The **on-machine verifier is QMC itself**: the average sign, the variance, and observable convergence are measured on-machine, and where an independent exact answer exists (small clusters, sign-free reference points, exact diagonalization) the deformed/transformed estimator is checked against it. Anything short of the section-2 standard - and in particular any hint of a general cure - is reported as a partial result, never as a solution.

## 1. Exact problem statement

**Setup.** For a fermionic (or frustrated bosonic) Hamiltonian $H$ on a lattice at inverse temperature $\beta$ (or in a ground-state projector QMC), a Monte Carlo estimator writes an observable as

\[
\langle O\rangle = \frac{\sum_{\mathcal C} w(\mathcal C)\, O(\mathcal C)}{\sum_{\mathcal C} w(\mathcal C)},
\qquad w(\mathcal C)\in\mathbb{C}\ \text{or}\ \mathbb{R},
\]

over configurations $\mathcal C$ (auxiliary fields, world lines, determinant configurations). When $w$ is not nonnegative, one samples $|w|$ and carries the phase/sign; the **average sign**

\[
\langle \mathrm{sgn}\rangle = \frac{\sum_{\mathcal C} w(\mathcal C)}{\sum_{\mathcal C} |w(\mathcal C)|} \sim e^{-\beta V \Delta f}
\]

decays exponentially in volume $V$ (with $\Delta f \ge 0$ a free-energy density difference), and the relative statistical error of any observable scales as $1/\langle\mathrm{sgn}\rangle$ - exponential cost.

**Two admissible attack classes.**
- **Contour deformation `[func]`:** deform the integration manifold of the (continuous) auxiliary fields into complex space (Lefschetz thimbles / learned flows) so that $\mathrm{Im}$ of the action is stationary and the residual sign fluctuation is reduced, while Cauchy's theorem keeps $\langle O\rangle$ exactly invariant. The learned object is a diffeomorphism $\phi_\theta$ of field space with tracked Jacobian.
- **Basis / variable change `[algo]`:** a similarity or canonical transformation (choice of single-particle basis, Majorana rearrangement, cluster/bond variables, or a Hubbard–Stratonovich channel) under which $w \ge 0$ *exactly* for the specific $H$ - a provable sign-free reformulation, connecting to stoquasticity classification (whether $H$ can be made stoquastic / sign-free by a local basis change).

**Admissible class.** A *named, specific* Hamiltonian or Hamiltonian family: e.g. a finite-density lattice-QCD toy model (Thirring / Gross–Neveu in low dimensions), a frustrated Heisenberg/Hubbard model at stated frustration, the 3D uniform electron gas at a stated density/temperature, or a specific transition-metal model. The Hamiltonian, lattice, filling/density, and $\beta$ (or projection time) are fixed and stated. General claims are out of scope by the section-2 ceiling.

**Success metrics (numeric).**
- **Average sign:** report $\langle\mathrm{sgn}\rangle$ (or average phase) before and after, at matched $(V,\beta)$; the win is a stated *variance-reduction factor* or a stated increase in the accessible $(V,\beta)$ at fixed cost.
- **Variance reduction:** a certified factor $R = \mathrm{Var}_{\text{before}}/\mathrm{Var}_{\text{after}}$ for a named observable at matched sampling cost, with error bars.
- **Exactness of the transformed estimator:** where an independent exact answer exists, the transformed/deformed estimator agrees within combined error bars (this is the correctness check; variance reduction without correctness is worthless).

## 2. Resolution standard

Because a universal cure is precluded, "resolution" here means a *specific* result meeting one of:
(a) a **provably sign-free reformulation** of a named Hamiltonian family not previously known to be sign-free, with a proof that the transformed weights are nonnegative for all configurations and a QMC demonstration that the sign is identically absent; or
(b) a **learned contour deformation** for a named model that achieves a certified variance-reduction factor large enough to reach a stated new $(V,\beta)$ regime, with the deformed estimator verified exact against an independent reference and the reduction shown to persist (not collapse) as $V$ grows over the demonstrated range.

**Not accepted as resolution:**
- Any claim of a *general* or *universal* sign-problem solution - precluded by NP-hardness; such a claim is reported as an error, and the specific Hamiltonian for which it actually works is identified.
- A variance reduction that *does not survive* the correctness check (the deformed estimator must reproduce the exact observable where one exists).
- A reduction demonstrated at one small $(V,\beta)$ that vanishes as $V$ grows - the scaling of $\langle\mathrm{sgn}\rangle$ with $V$ over the accessible range must be shown, not a single point.
- A "sign-free basis" that is sign-free only at a special symmetric point (e.g. half-filling / particle-hole symmetry) already known to be sign-free, presented as new.
- Cherry-picked observables: the reduction and correctness must hold for the physically relevant observable, not just the partition function.

**Benchmark-integrity clause.** QMC self-verifies, but with named biases. (i) *Underestimated sign decay* - at small $V,\beta$ the sign has not yet decayed, so a method can look successful precisely where the problem is absent; guard: report $\langle\mathrm{sgn}\rangle$ and variance as functions of $V$ and $\beta$ across the accessible range, showing the trend, never a single easy point. (ii) *Ergodicity / autocorrelation masking* - a deformed sampler can appear low-variance because it is stuck (long autocorrelation undercounts error); guard: report integrated autocorrelation times and error bars validated by binning/jackknife, and check against an independent exact answer. (iii) *Reference availability bias* - exact references exist only for small systems or special points; a method validated only there may fail where it matters; guard: state explicitly the regime where correctness is *proved* vs *extrapolated*. A variance win without the scaling trend and the correctness check is flagged as confident-but-wrong.

## 3. Graded partial-result targets

**P1 - Reproduce a known sign-cured case with our pipeline.** Take a model with a *known* sign-free formulation (e.g. attractive Hubbard at half-filling; a Majorana-positive model; a meron-cluster case) and reproduce the sign-free behavior and a benchmark observable with our QMC, confirming the toolchain and the exact reference. *Certificate:* $\langle\mathrm{sgn}\rangle = 1$ (to noise) in the known basis; observable matching the exact/published reference.

**P2 - Learned contour deformation with certified variance reduction on a target model.** For a named model with a sign problem, train a contour deformation $\phi_\theta$ and demonstrate a certified variance-reduction factor for a physical observable at matched cost, with the deformed estimator verified exact against exact diagonalization on a small instance. *Certificate:* variance-reduction factor with error bars; agreement with exact reference within combined error; Jacobian correctly accounted.

**P3 - Reduction that scales over a demonstrated range.** Show the deformation's benefit (accessible $(V,\beta)$ at fixed cost) grows or holds as $V$ increases across the reachable range, mapping $\langle\mathrm{sgn}\rangle(V,\beta)$ before and after. *Certificate:* the $(V,\beta)$ scaling curves with error bars.

**P4 - A provably sign-free basis for a new specific Hamiltonian class.** Prove (symbolically) that a specific Hamiltonian family, not previously known to be sign-free, admits a local basis/variable change making all weights nonnegative, and demonstrate it in QMC. Connects to stoquasticity classification. *Certificate:* a machine-checkable proof of weight-nonnegativity for the transformed Hamiltonian; QMC with the sign identically absent.

**P5 - Characterize the boundary.** For a family with a tunable parameter, map where the sign problem is curable by the studied method and where it is not, ideally with a proof of an obstruction on the "not" side (e.g. a de-facto stoquasticity barrier). *Certificate:* the curability boundary with certified sign-free points on one side and demonstrated hardness/obstruction on the other.

## 4. Known results and prior art

- Troyer & Wiese (2005) - the general fermion/frustrated sign problem is NP-hard: the hardness ceiling.
- Loh, Gubernatis, Scalettar, White, Sugar, et al. (1990) - the sign problem in determinant QMC; Chandrasekharan & Wiese (1999) - meron-cluster solution of specific sign problems (a specific-Hamiltonian cure).
- Lefschetz-thimble / complex-Langevin program: Cristoforetti, Di Renzo, Scorzato (2012) - thimble regularization; Aarts and co-workers - complex Langevin for finite-density field theory; Alexandru, Bedaque, Lamm, Lawrence and co-workers - sign-optimized manifolds and *learned* contour deformations (neural-network manifolds) for field theories with a sign problem.
- Machine-learned normalizing-flow contour deformations for lattice field theory: Albergo, Kanwar, Shanahan and co-workers (flow-based sampling); Lawrence, Yamauchi and others on learned thimbles (verify specifics).
- Stoquasticity and basis-change cures: Bravyi, DiVincenzo, Oliveira, Terhal - stoquastic Hamiltonians and their complexity; Klassen, Terhal and co-workers (2019–) - deciding/removing stoquasticity by local basis change ("curing the sign problem" via single-qubit/orbital rotations), the direct link to P4/P5.
- Design principles for sign-free models: Wei, Wu, Li, Zhang, Xiang (2016) - Majorana-based sign-free conditions; Li & Yao and others - classes of sign-free Hubbard-type models; Honecker, Wessel and others on frustrated magnets.
- QMC software: ALF (auxiliary-field QMC, Assaad and co-workers), QUEST/DQMC, and Lefschetz-thimble / flow codes (often bespoke; verify).

*Status as of mid-2026 - re-verify against current literature before starting any session.*

## 5. Attack plan

**Reference/verifier layer.** Exact diagonalization (Lanczos, e.g. via QuSpin or a bespoke sparse solver) for small instances gives the exact observables to check correctness; known sign-free points (half-filling, Majorana-positive models) give a zero-sign baseline. QMC engine: **ALF** or a bespoke determinant/auxiliary-field QMC for the target models, or a world-line code for spin models. Fits on one workstation for small-to-moderate lattices; one prosumer GPU accelerates the flow/deformation networks.

**Contour-deformation layer `[func]`.** Parameterize $\phi_\theta$ as a normalizing flow / neural diffeomorphism of the (continuous) auxiliary-field manifold in **PyTorch**; train to minimize sign/phase fluctuation (or maximize $|\langle\mathrm{sgn}\rangle|$) with the Jacobian tracked exactly (or via a tractable flow architecture). Cauchy's theorem guarantees the observable is invariant *if* the deformation is a valid homotopy avoiding poles - verify this by the correctness check on small instances.

**Basis-change / sign-free layer `[algo]`/`[sym]`.** For a target family, search over local single-particle/orbital rotations and Hubbard–Stratonovich channels for a formulation with provably nonnegative weights; where structure suggests it, prove weight-nonnegativity symbolically (Majorana-positivity conditions, or a stoquasticity criterion checked in SymPy over the model parameters). This connects to the stoquasticity-classification Pack A item.

**Certification layer.** Report $\langle\mathrm{sgn}\rangle$, variance, integrated autocorrelation time, and jackknife error bars as functions of $(V,\beta)$; verify the transformed estimator against exact diagonalization wherever a small-system reference exists.

**Expected failure modes.** (i) A "cure" that only works below the sign-onset scale - always show the $V$-scaling. (ii) Deformed sampler stuck in one thimble (broken ergodicity) giving false low variance - check autocorrelation and exact agreement. (iii) Jacobian mis-accounting silently biasing the observable - the correctness check catches it. (iv) A basis-change that is sign-free only at a symmetric point already known - verify novelty. (v) Overclaiming generality - the NP-hardness ceiling forbids it; the specific model must be named.

## 6. Verification and auditability requirements

1. **Exact or certified numerics.** Every variance-reduction claim carries jackknife/binned error bars and an integrated-autocorrelation-time report; correctness is verified against an independent exact reference (exact diagonalization or a known sign-free point) within combined error bars; sign-free proofs are machine-checkable weight-nonnegativity arguments, not numerical observations at sampled points.
2. **Independent verification.** A standalone estimator - separate from the training/deformation code - recomputes the observable from stored configurations and reproduces the sign/variance statistics; the exact reference is computed by a second method (Lanczos vs full diagonalization) on small instances.
3. **Reproducibility.** The named Hamiltonian, lattice, filling/density, $\beta$/projection time, deformation architecture and seeds, QMC parameters, and the $(V,\beta)$ grid are recorded; SHA-256 manifest over all artifacts; the regime where correctness is *proved* vs *extrapolated* is stated explicitly.
4. **Preservation.** Deformation/training code, QMC inputs, sampled-configuration checkpoints (or the means to regenerate them), and symbolic proofs are part of the record. Anything not preserved is stated explicitly.
5. **Honest reporting.** The report states up front that no general cure is claimed (NP-hardness ceiling), names the specific Hamiltonian, reports $\langle\mathrm{sgn}\rangle$ and variance as functions of $(V,\beta)$ across the accessible range (not a single easy point), shows the correctness check, and never presents a below-onset or special-point result as curing the sign problem.
