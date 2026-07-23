# PROMPT FOR AUTOMATIC REACTION-COORDINATE AND COLLECTIVE-VARIABLE DISCOVERY

## Learning the coordinate that governs a rare event, certified against the committor

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Pack:** A - closed-loop (on-machine verifier)  
**Rank:** A-08 of 21  
**Source:** chem/bio top-50 list #11, section B (free energy, dynamics, sampling)  
**Modes:** `[data]` `[func]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Enhanced sampling - metadynamics, umbrella sampling, adaptive biasing - works only as well as the collective variable (CV) it biases. A poor CV leaves the slow, hidden degrees of freedom unsampled and produces a confidently converged, wrong free-energy surface. Discovering the reaction coordinate automatically is therefore the bottleneck of the whole free-energy program. This prompt fixes two on-machine verifiers, both exact and both simulation-native. First, the **committor function** $q(x)$ - the probability that a trajectory launched from $x$ reaches product before reactant - is, by transition-path theory, *the* exact reaction coordinate; its isosurfaces are testable directly by shooting (committor analysis). Second, for a proposed CV, the **convergence gain in enhanced sampling** it produces is measurable against a long unbiased reference. The task is a method that discovers a CV and then certifies it: either that a discovered CV is a genuine function of the committor (iso-committor consistency), or that biasing it demonstrably accelerates convergence to the reference free energy. The honesty spine, stated once: **all of this is defined relative to a fixed Hamiltonian** - a "correct reaction coordinate" is correct for that potential's dynamics, and says nothing about whether the potential itself matches reality. Anything short of section 2 is a partial result.

## 1. Exact problem statement

**System class.** Systems with a metastable-state structure and at least one identifiable slow transition on a fixed potential energy surface: the alanine dipeptide ($\phi,\psi$ rotamer transitions), the Müller–Brown two-dimensional model potential, small folding peptides (chignolin, Trp-cage), and simple conformational or association transitions. Reactant set $A$ and product set $B$ are defined as disjoint regions of configuration space.

**Dynamics and Hamiltonian (fixed).** Overdamped or underdamped Langevin dynamics on a stated potential $U(x)$ (analytic model potential, or an MM force field with stated water model), at temperature $T$, $\beta=1/k_BT$, with a stated thermostat/friction. The committor, the free-energy surface, and CV quality are all properties of this fixed $U$ and the chosen dynamics.

**Notation.** $N$ atoms, configuration $x\in\mathbb{R}^{3N}$; free energies in kcal/mol; committor $q\in[0,1]$ dimensionless; shooting count $K$ per validation point; CV dimension $d$. The equilibrium density is $Z^{-1}e^{-\beta U(x)}$ with $Z$ the configurational partition function. The generator $\mathcal{L}$ and its adjoint (Fokker–Planck operator) are defined by the chosen integrator; a run states which.

**The committor (exact reaction coordinate).** For states $A,B$, the forward committor is

\[
q(x) \;=\; \Pr\big[\tau_B < \tau_A \,\big|\, X_0 = x\big],
\]

the probability that dynamics started at $x$ hits $B$ before $A$. It satisfies the backward Kolmogorov equation with Dirichlet boundary data,

\[
\mathcal{L}\,q = 0 \ \ \text{on the transition region}, \qquad q|_A = 0,\quad q|_B = 1,
\]

where $\mathcal{L}$ is the generator of the dynamics. For overdamped Langevin dynamics with diffusion $D(x)$ and potential $U$, the generator acts as

\[
\mathcal{L} f \;=\; D(x)\Big[\, \Delta f - \beta\, \nabla U(x)\cdot \nabla f \,\Big],
\]

so the committor equation is a linear elliptic boundary-value problem, exactly solvable on a grid for low-dimensional model systems and estimable by shooting for high-dimensional ones. By transition-path theory (E & Vanden-Eijnden), $q$ carries the full reactive-flux structure: the probability current of reactive trajectories is

\[
J(x) \;=\; Z^{-1}\, e^{-\beta U(x)}\, D(x)\,\nabla q(x),
\]

so the transition-state ensemble is the $q=\tfrac12$ isosurface and the reactive rate is the total flux across it,

\[
k_{A\to B} \;=\; \frac{1}{Z\,\pi_A}\int D(x)\,e^{-\beta U(x)}\,\lvert\nabla q(x)\rvert^2\, dx ,
\]

with $\pi_A$ the reactant population. A CV $s(x)$ is a *perfect* reaction coordinate iff $s$ is a monotone function of $q$, equivalently iff the committor is constant on each isosurface of $s$. A single perfect CV is one-dimensional; when no one-dimensional $s$ achieves constancy the honest output is a low-dimensional $s$ (2–3 components) that jointly resolves $q$, reported as such rather than forced into a scalar.

**Collective variable (the object to be discovered).** A differentiable, low-dimensional map $s_\theta: \mathbb{R}^{3N}\to\mathbb{R}^d$ ($d$ small, typically 1–3), computable and differentiable at simulation speed, usable as the biased coordinate in an enhanced-sampling engine. Admissible constructions: TICA, VAMPnets, diffusion maps, SGOOP, autoencoder/RAVE latent variables, spectral-gap or committor-regression objectives.

**Committor-consistency metric (numeric).** For a proposed CV $s$, bin configurations by $s$; within each bin, launch $K$ shooting trajectories and estimate the empirical committor $\hat q$. Decompose the total variance of $q$ into a part explained by $s$ and a residual within-isosurface part,

\[
\mathrm{Var}(q) \;=\; \underbrace{\mathrm{Var}\big(\mathbb{E}[q\mid s]\big)}_{\text{explained by } s} \;+\; \underbrace{\mathbb{E}\big[\mathrm{Var}(q\mid s)\big]}_{\text{residual}} .
\]

The CV passes if the residual within-surface standard deviation is $\le 0.1$ across the transition region, with binomial error bars from $K\ge 200$ shots per point.

**Sampling-gain metric (numeric).** Biasing $s$ in metadynamics recovers the free energy along $s$ as the negative converged bias, $F(s) = -V_{\text{bias}}(s) + \text{const}$; the test is whether this, reweighted onto an *independent* coordinate,

\[
F(\xi) \;=\; -k_BT\,\ln \big\langle \delta(\xi - \xi(x))\, e^{\beta V_{\text{bias}}(s(x))}\big\rangle_{\text{biased}} ,
\]

reproduces the long-reference free-energy profile to within $0.5$ kcal/mol using at least a stated factor (e.g. $\ge 5\times$) less simulation time than unbiased MD, with the reference itself converged to $\le 0.1$ kcal/mol. No informal target ("good CV", "captures the physics") is accepted without one of these two metrics.

## 2. Resolution standard

A resolution, for a stated system and fixed Hamiltonian, consists of:

1. An automatically discovered CV $s_\theta$ (no hand-tuned atom selection specific to the answer) that passes the committor-consistency test (within-surface committor std $\le 0.1$) across the transition region, with shooting error bars.
2. A demonstration that biasing $s_\theta$ accelerates convergence to the long-unbiased-reference free energy by the stated factor, at the stated tolerance.
3. Both certified on the *same* fixed Hamiltonian, with the reference free energy independently converged.

**Not accepted as resolution:**

- A CV that yields a smooth-looking free-energy surface but was never committor-validated - a smooth FES is fully consistent with a hidden orthogonal slow variable, the classic silent failure.
- Recovering a *known* CV (e.g. $\phi$ for alanine dipeptide) by a method that was given the answer through its features or its state definitions.
- A method demonstrated on one model potential and presented as general.
- A sampling-gain claim measured against a poorly converged reference, or measured along the biased coordinate itself (circular).
- "Discovery" that requires the user to already know the transition to define states $A,B$ tightly around it - state the input assumptions honestly.

**Benchmark-integrity clause.** The committor verifier is exact but *expensive and Hamiltonian-bound*: it certifies that $s$ is the reaction coordinate for the given $U$, not that $U$ is physically correct. A CV validated on a model potential or a specific force field must not be represented as validated for the real molecule. The guard against teaching-to-the-test is a **held-out transition**: discover and freeze the CV on one transition/temperature, then committor-validate on a *different* transition or state point of the same system without refitting. Report the frozen-CV committor-consistency, not only the fitted one. Where the CV is learned from trajectory data, the training trajectories and the validation shooting points must be disjoint and the split committed by hash before shooting.

## 3. Graded partial-result targets

- **P1 - Reproduce a known CV on a model system.** Recover the committor-consistent reaction coordinate for the Müller–Brown potential and for alanine dipeptide ($\phi$/$\psi$) using TICA and a VAMPnet, and *independently* committor-validate it by shooting. *Verifier:* for the model potential, the grid-solved exact committor (Kolmogorov equation on a mesh) plus shooting; for alanine dipeptide, shooting. *Certificate:* the learned CV, the shooting-based committor scatter ($\hat q$ vs $s$) with binomial error bars, and the within-surface variance. Establishes toolchain and validator.
- **P2 - Certified committor validation of a discovered CV.** On a system where the reaction coordinate is *not* obvious (e.g. a peptide conformational switch), discover a CV by an automated method and pass the committor-consistency test on a **held-out** transition. *Verifier:* shooting-based committor on held-out configurations. *Certificate:* frozen-CV committor scatter, disjoint train/validation split hash, within-surface std $\le 0.1$.
- **P3 - A CV that provably accelerates sampling.** Bias the discovered CV in metadynamics or OPES and show a measured convergence gain (stated factor) to the long-reference free energy, with the reference converged independently to $\le 0.1$ kcal/mol. *Verifier:* long unbiased reference MD. *Certificate:* biased and unbiased free-energy profiles with block-averaged error bars, effective-sample/wall-clock accounting, and reference-convergence evidence.
- **P4 - Committor as direct regression target.** Learn $q$ directly (committor-network / Kolmogorov-equation loss) and show the resulting CV is self-consistent under shooting *and* recovers the transition-state ensemble ($q=\tfrac12$) whose members shoot to $\hat q = 0.5 \pm$ error. *Verifier:* shooting from the predicted $q=\tfrac12$ surface. *Certificate:* the $q$-network and a transition-state-ensemble shooting histogram peaked at $0.5$.
- **P5 - Enhanced sampling with a wrong CV, characterized.** Deliberately bias a plausible-but-imperfect CV and quantify the resulting free-energy error against the reference, demonstrating the failure mode the committor test is meant to catch. *Verifier:* long unbiased reference and the committor test showing the CV's residual within-surface variance. *Certificate:* the mismatched free-energy profile beside the committor-failure evidence - a negative result that certifies the diagnostic works.
- **P6 - Transferable CV discovery.** Strongest short of resolution: a discovery procedure that produces committor-consistent CVs across *several* related systems or state points without per-system hand-holding, with an honest statement of what transfers and what must be relearned. *Verifier:* per-system shooting committor for a frozen procedure. *Certificate:* per-system committor-consistency and the named failure cases.

## 4. Known results and prior art

- Time-lagged independent component analysis (TICA): Pérez-Hernández, Hoffmann, Olsson, Noé ~2013; Schwantes & Pande ~2013.
- VAMPnets and the variational approach for Markov processes: Mardt, Pasquali, Wu, Noé 2018; Wu & Noé 2020. State-free reversible VAMPnets / Deep-TICA: Bonati, Piccini, Parrinello ~2021.
- Diffusion maps for molecular systems: Coifman–Lafon (~2006); Rohrdanz, Zheng, Maggioni, Clementi ~2011 (locally scaled diffusion maps, LSDMap).
- SGOOP (Spectral Gap Optimization Of Order Parameters): Tiwary & Berne 2016. RAVE (Reweighted Autoencoded Variational Bayes): Ribeiro, Bravo, Wang, Tiwary ~2018.
- Committor as the exact reaction coordinate and transition-path theory: E & Vanden-Eijnden ~2006–2010; Berezhkovskii & Szabo. Likelihood-maximization committor coordinates: Peters & Trout 2006; Peters, Beckham, Trout ~2007.
- Transition path sampling and committor (shooting) analysis: Bolhuis, Chandler, Dellago, Geissler ~2002; Dellago, Bolhuis, Geissler.
- Autoencoder / deep-learning CVs and committor networks: Chen & Ferguson ~2018; Rotskoff, Vanden-Eijnden; Hénin, Lelièvre; deep committor solvers (verify specific architectures and years).
- Enhanced-sampling engines that consume learned CVs: metadynamics (Laio–Parrinello 2002) and OPES (Invernizzi–Parrinello ~2020), via PLUMED.

**Status as of mid-2026 - re-verify against current literature before starting any session.**

## 5. Attack plan

`[data]` + `[func]` mode; one workstation, one GPU.

1. **Reference dynamics and committor engine.** OpenMM (GPU) for the MD; a shooting harness that launches $K$ short trajectories from stored configurations and records first-hit of $A$ vs $B$ to build empirical committors. For the model potentials, a Langevin integrator in NumPy suffices and makes the *exact* committor (backward Kolmogorov equation on a grid) available as an independent gold standard. Failure mode: loosely defined $A,B$ corrupts the committor - fix and document them first.
2. **CV learners.** deeptime / PyEMMA for TICA and VAMPnets; PyTorch for autoencoder/RAVE and committor networks; PLUMED for the SGOOP and biasing side. Keep training trajectories disjoint from validation shooting points; commit the split hash first.
3. **Committor validation.** For each candidate CV, bin by $s$, shoot, and compute within-surface committor variance with binomial error bars. This is the certificate, run separately from the learner and, for model systems, cross-checked against the grid committor.
4. **Sampling-gain measurement.** Metadynamics/OPES on the discovered CV vs a long unbiased reference; block-averaged free-energy error bars; effective-sample and wall-clock accounting. Failure mode: measuring the gain along the biased CV (circular) - always measure convergence of an *independent* observable or an orthogonal coordinate.
5. **Rare-event honesty.** If the true slow coordinate is orthogonal to the discovered CV, biasing accelerates nothing and the committor test fails - report this as the informative outcome, not a bug, and state where a workstation cannot converge the reference.

## 6. Verification and auditability requirements

1. **Certified numerics.** Committor estimates carry binomial ($\sqrt{p(1-p)/K}$) error bars with $K\ge 200$ shots per point; free-energy references carry block-averaged errors and $\ge 2$ independent replicas. For model potentials, the grid-solved exact committor is the independent gold standard and must agree with shooting.
2. **Independent verification.** The committor-validation harness is written separately from the CV-learning code; a second implementation reproduces at least one committor scatter; for model systems, the analytic/grid committor cross-checks shooting.
3. **Reproducibility.** Trajectories, seeds, state definitions $A,B$, network hyperparameters, biasing parameters, and the frozen train/validation split are recorded with a SHA-256 manifest; the split is committed before any shooting.
4. **Preservation.** CV-learning code, discarded architectures, and CVs that failed the committor test are part of the record; a failed CV is a finding about the coordinate, not a discard.
5. **Honest reporting.** The report states up front whether a discovered CV passed committor-validation on a *held-out* transition and whether the sampling gain was measured against a converged reference; it labels every result as valid for the stated Hamiltonian only, and never presents a smooth free-energy surface as evidence of a correct reaction coordinate absent the committor test.
