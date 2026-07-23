# PROMPT FOR BOLTZMANN-WEIGHTED FREE-ENERGY SAMPLING

## Generating the equilibrium ensemble and its free energies, certified by exact reweighting to reference MD

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Pack:** A - closed-loop (on-machine verifier)  
**Rank:** A-12 of 21  
**Source:** chem/bio top-50 list #9, section B (free energy, dynamics, sampling)  
**Modes:** `[struct]` `[func]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The named frontier past static structure is not "what does the molecule look like" but "how is the molecule distributed" - the Boltzmann-weighted ensemble and the free-energy differences that follow from it. A generative model that produces samples from the Boltzmann distribution of a molecular system would give folding and binding free energies without the ergodicity problem that cripples molecular dynamics. Boltzmann generators (Noé, Olsson, Köhler, Wu 2019) and their successors - stochastic normalizing flows, flow-matching, diffusion emulators - are the live attack. This prompt fixes the on-machine verifier at the one place it is exact: for a fixed Hamiltonian, **long reference molecular dynamics defines the target Boltzmann distribution, and any generator can be turned into an asymptotically unbiased estimator by exact reweighting** with weights $w(x)\propto e^{-\beta U(x)}/p_{\text{gen}}(x)$, provided $p_{\text{gen}}$ is known. The task is a generator plus a reweighting scheme that reproduces reference-MD observables and free-energy differences to a stated statistical tolerance, with the reweighting variance controlled and reported. The honesty spine, enforced throughout: **the target is the Boltzmann distribution of the chosen force field, not nature's.** A generator can be perfect for its Hamiltonian and still disagree with experiment because the Hamiltonian is wrong; conflating the two is the field's central confusion. Anything short of section 2 is a partial result.

## 1. Exact problem statement

**System class.** Small systems where a converged all-atom reference is attainable on a workstation: alanine dipeptide, chignolin (CLN025), Trp-cage, villin headpiece, and comparable fast-folding peptides - plus explicit-solvent or implicit-solvent variants as declared. Association/binding free energies for small host–guest or peptide systems are in scope where a reference is affordable.

**Hamiltonian (fixed and named).** A stated all-atom force field and (if explicit) water model define the potential $U(x)$ and thus the target density
$$
\mu(x) = Z^{-1}\, e^{-\beta U(x)}, \qquad Z = \int e^{-\beta U(x)}\,dx,\qquad \beta = 1/k_BT.
$$
All targets, weights, and free energies are defined by this $U$. The reference is the Hamiltonian, not experiment.

**Reference (on-machine ground truth).** Long unbiased MD (or replica-exchange / metadynamics-reweighted MD), run to a documented convergence, sampling $\mu$. Its ensemble averages $\langle O\rangle_\mu$ and free-energy differences between macrostates $S_1,S_2$,
$$
\Delta G_{12} = -k_BT\,\ln\frac{\int_{S_2} e^{-\beta U}\,dx}{\int_{S_1} e^{-\beta U}\,dx},
$$
are the ground-truth quantities. Convergence of the reference (block averaging, independent replicas, error bars) is itself a certified step (section 6), because an unconverged reference is not a verifier.

**Generator (the object to be built).** A model $p_\theta(x)$ with tractable (or tractably estimable) density from which i.i.d. or MCMC samples can be drawn: a normalizing flow, a stochastic normalizing flow, a flow-matching / continuous-normalizing-flow model, or a diffusion model equipped with a density/likelihood or an unbiasing MCMC wrapper. The generator must be usable for **exact reweighting**: given $p_\theta(x)$ and $U(x)$, define importance weights $w(x)=e^{-\beta U(x)}/p_\theta(x)$ (up to the constant $Z$), so that for any observable
$$
\langle O\rangle_\mu = \frac{\mathbb{E}_{x\sim p_\theta}[\,w(x)\,O(x)\,]}{\mathbb{E}_{x\sim p_\theta}[\,w(x)\,]},
$$
which is unbiased in the infinite-sample limit whenever $p_\theta$ covers the support of $\mu$.

**Accuracy thresholds (numeric).**
- *Observable agreement.* Reweighted generator estimates of stated observables (dihedral distributions, radius of gyration, native-contact fraction, macrostate populations) agree with the converged reference within combined statistical error, quantified as $\le 2\sigma$ discrepancy on each reported observable.
- *Free-energy difference.* A macrostate $\Delta G_{12}$ from the reweighted generator agrees with the reference $\Delta G_{12}$ to $\le 0.5$ kcal/mol, with both uncertainties reported.
- *Reweighting quality.* The effective sample size fraction $\mathrm{ESS}/N = (\sum w)^2 / (N\sum w^2)$ is reported; a claim standing on $\mathrm{ESS}/N$ below a stated floor (e.g. $10^{-2}$) is flagged as high-variance and not counted as converged.

## 2. Resolution standard

A resolution, for a stated system and fixed Hamiltonian, consists of:

1. A generator $p_\theta$ whose **exactly reweighted** estimates reproduce the converged reference-MD observables within $2\sigma$ and macrostate $\Delta G$ within $0.5$ kcal/mol, with reported ESS and uncertainties.
2. A demonstration of asymptotic unbiasedness: either a tractable-density flow with the reweighting identity above, or a flow/diffusion model wrapped in an MCMC scheme (independence Metropolis, neural-transport HMC, or flow-annealed importance sampling) proven to sample $\mu$ in the limit, with the estimator's bias shown to vanish as samples grow.
3. Validation on a **held-out** system or state point the generator was not trained on, reproducing that reference's observables after (re)weighting.

**Not accepted as resolution:**

- A generator whose *raw* samples look right but that was never reweighted - visual or distributional similarity to reference samples is not Boltzmann correctness. The reweighting (or an MCMC-unbiasing wrapper) is mandatory, because a generator can match marginals while mis-weighting the joint.
- A high-fidelity generator with $\mathrm{ESS}/N$ so low that the reweighted estimate has uncontrolled variance, reported as if converged.
- Matching *experimental* observables while skipping the reference-MD comparison (this hides force-field/generator error cancellation).
- A single-peptide result presented as solving free-energy sampling.
- Trained and evaluated on overlapping trajectory data (leakage).

**Benchmark-integrity clause.** The reference-MD verifier is exact for the Hamiltonian but has two failure modes that must be guarded. (i) *An unconverged reference is a false gold standard*: if the reference MD is itself non-ergodic, "agreement" is agreement between two biased estimates. Certify the reference's convergence independently (multiple replicas from different initial states must agree) before using it as ground truth. (ii) *Teaching-to-the-test*: a generator trained on the very trajectory it is validated against can memorize rather than sample. The guard is a held-out system/state point plus a frozen, hash-committed train/validation split, and reporting the reweighted (not raw) metric. Finally, keep the on-machine claim ("reproduces the Boltzmann distribution of this force field") strictly separate from any experiment comparison ("matches measured folding free energy"), which is downstream and force-field-limited.

## 3. Graded partial-result targets

- **P1 - Reproduce a Boltzmann-generator result with reweighting validation.** On alanine dipeptide (or a comparably small system), train a normalizing flow and reproduce the reference free-energy surface via *exact reweighting*, matching macrostate populations within $2\sigma$. *Certificate:* the flow, the reweighted vs reference free-energy profile with error bars, the ESS, and the converged reference. Establishes the toolchain.
- **P2 - Certified free-energy difference on a target with statistical error.** For a fast-folding peptide (chignolin or Trp-cage), produce a folded/unfolded $\Delta G$ from the reweighted generator agreeing with a converged reference to $\le 0.5$ kcal/mol, both errors reported. *Certificate:* reference-convergence evidence (replica agreement), reweighted $\Delta G$ with bootstrap error, ESS.
- **P3 - Held-out observable reproduction.** Show the generator reproduces reference-MD observables on a system or state point *not* in its training data, after reweighting. *Certificate:* frozen split hash, held-out reweighted observables vs reference within $2\sigma$.
- **P4 - Asymptotically unbiased sampling proof/test.** Wrap the generator in an MCMC scheme (independence Metropolis with flow proposals, or flow-annealed importance sampling) and demonstrate the estimator's bias decreasing to zero as sample count grows (empirical bias-vs-N curve on a system with an exactly known answer, plus the theoretical unbiasedness argument). *Certificate:* the bias-decay curve against a model system with analytic free energy, and the acceptance/weight diagnostics.
- **P5 - Transferable generator.** Strongest short of resolution: a generator (e.g. flow-matching with equivariance, or a coordinate-transferable architecture) that produces reweightable samples for a *family* of related systems from one trained model, with honest statement of where ESS collapses. *Certificate:* per-system reweighted observables and ESS, and the failure boundary named.

## 4. Known results and prior art

- Boltzmann generators: Noé, Olsson, Köhler, Wu 2019 (Science, "Boltzmann generators - sampling equilibrium states of many-body systems with deep learning"). Foundational normalizing-flow sampling of $\mu$.
- Stochastic normalizing flows: Wu, Köhler, Noé 2020. Combine deterministic flow layers with stochastic (MCMC/Langevin) steps for exactness.
- Flow-matching / continuous normalizing flows: Lipman, Chen, Ben-Hamu, Nickel, Le 2022 (flow matching for generative modeling). Equivariant flow matching for molecules: Klein, Köhler, Noé ~2023; Timewarp (Klein et al ~2023) for transferable MD emulation.
- Targeted free-energy perturbation and its learned generalization: Jarzynski 2002 (targeted FEP); learned maps as targeting transformations (Wirnsberger et al, DeepMind ~2020, "Targeted free energy estimation via learned mappings").
- Flow annealed importance sampling bootstrap (FAB): Midgley, Stimper, ... Hernández-Lobato ~2022 - training flows for asymptotically unbiased sampling with low variance.
- Diffusion emulators of MD / equilibrium ensembles: DiG (Distributional Graphormer, Zheng et al, Microsoft ~2023–2024); BioEmu (Microsoft ~2024–2025, verify). Str2Str (~2024, verify).
- Reference trajectories: Anton fast-folder simulations (Lindorff-Larsen, Piana, Shaw ~2011) as canonical long-MD references where accessible; otherwise self-generated converged references.

**Status as of mid-2026 - re-verify against current literature before starting any session.**

## 5. Attack plan

`[struct]` + `[func]` mode; one workstation, one GPU.

1. **Converged reference.** OpenMM (GPU) long MD or replica-exchange for the target peptide; convergence certified by $\ge 2$ independent replicas from distinct initial structures agreeing on macrostate populations within error. This reference is the verifier; do not proceed on an unconverged one.
2. **Generator.** PyTorch normalizing flow (for tractable density) or flow-matching/diffusion model with an unbiasing wrapper. `bgflow`/`bgmol`-style tooling or a from-scratch flow. Internal coordinates or equivariant representations to respect molecular symmetry.
3. **Reweighting and MCMC unbiasing.** Compute $w(x)=e^{-\beta U(x)}/p_\theta(x)$ with $U$ from the same OpenMM system; report ESS. For P4, independence Metropolis or FAB for asymptotic unbiasedness. Failure mode: exponential weight-variance blow-up in high dimension - the ESS gate catches it; treat ESS collapse as the honest scaling limit, not a tuning nuisance.
4. **Held-out validation.** Frozen, hash-committed split; reweighted observables on the held-out system. Failure mode: leakage between training trajectory and validation reference - disjoint trajectories, committed first.
5. **Rare events.** Folded/unfolded interconversion is the rare event; the generator's advantage is precisely to bypass it, so the test is whether the reweighted rare-state population matches the reference. Where the workstation cannot converge the reference itself, state that limit rather than lowering the bar.

## 6. Verification and auditability requirements

1. **Certified numerics.** Both the reference and the reweighted estimates carry block-averaged / bootstrap error bars; the reference's convergence is certified by independent-replica agreement; ESS is reported for every reweighted claim. A reweighted number without its ESS does not count.
2. **Independent verification.** The reweighting/estimation code is written separately from the generator-training code; a standalone checker recomputes each headline $\Delta G$ from stored samples, weights, and energies. For P4, the bias-decay test uses a model system with an analytically known free energy as an external check.
3. **Reproducibility.** Force field, water model, integrator/thermostat settings, seeds, network hyperparameters, and the frozen train/validation split are recorded with a SHA-256 manifest; splits committed before evaluation.
4. **Preservation.** Generator-training code, failed architectures, and runs with collapsed ESS are part of the record; an ESS collapse is a scaling finding, not a discard.
5. **Honest reporting.** The report states up front whether the section-2 tolerance was met against the *converged reference* (the resolution metric), reports the ESS for every free-energy claim, separates the "reproduces this force field's Boltzmann distribution" claim from any experiment comparison, and never presents raw generator samples' visual similarity as Boltzmann correctness.
