# PROMPT FOR BINDING KINETICS: k_on, k_off, AND RESIDENCE TIMES

## Predicting association and dissociation rates, certified by weighted-ensemble / MSM convergence and MFPT consistency

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Pack:** A - closed-loop (on-machine verifier)  
**Rank:** A-14 of 21  
**Source:** chem/bio top-50 list #12, section B (free energy, dynamics, sampling)  
**Modes:** `[struct]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Binding affinity is the number the field optimizes, but the *rate* - how fast a ligand binds ($k_{\text{on}}$) and, more importantly, how slowly it leaves ($k_{\text{off}}$, whose inverse is the residence time) - often predicts drug efficacy better than affinity and is far less solved. Residence time is set by the dissociation barrier, a rare-event property invisible to equilibrium free-energy methods. This prompt fixes the on-machine verifier where it is exact: for a fixed Hamiltonian, **long molecular dynamics and rare-event samplers (weighted ensemble, Markov state models, milestoning) estimate rate constants with quantifiable statistical error**, and those estimates carry internal consistency checks that are themselves verifiable - detailed balance, and the equality of the rate with the inverse mean-first-passage-time (MFPT). The task is a rate-prediction pipeline that reproduces a published rate with certified convergence, and delivers a rate on a target with honest error bars. The honesty spine, enforced throughout: **a computed rate is the rate of the chosen force field's dynamics, not nature's.** Rates depend on barrier *heights*, so they are exponentially sensitive to force-field error - even more than free energies - and on-machine convergence must never be presented as agreement with experiment. Anything short of section 2 is a partial result.

## 1. Exact problem statement

**System class.** Systems where an unbinding/binding event is rare but a reference rate is attainable on a workstation: host–guest complexes (e.g. cyclodextrin or cucurbituril with small guests), the benzamidine–trypsin association (a canonical computed-$k_{\text{on}}$ benchmark), and small protein–ligand systems with fast enough kinetics. Congeneric ligand series for the ranking target (P4). Declared per run.

**Hamiltonian (fixed and named).** A stated force field and water model define $U(x)$ and thus the dynamics (stated integrator, thermostat, friction). All rates are properties of this dynamics.

**Target quantities.** For bound state $B$ and unbound state $U$,
$$
k_{\text{off}} = \tau_{\text{res}}^{-1}, \qquad \tau_{\text{res}} = \langle \tau_{B\to U}\rangle \ \ (\text{mean first passage time, MFPT}),
$$
$$
k_{\text{on}} = \frac{1}{[\,L\,]\,\langle \tau_{U\to B}\rangle}\ \ (\text{concentration-normalized association MFPT}),
$$
with the equilibrium constraint $K_d = k_{\text{off}}/k_{\text{on}}$ and $\Delta G_{\text{bind}} = -k_BT\ln(K_d/c^\circ)$ providing an internal cross-check against an equilibrium free-energy calculation on the same Hamiltonian.

**Estimators (the objects to be built/run).** A rate must come from one of: a Markov state model (MSM) built from many short trajectories, from which MFPTs and rates follow via transition-path theory; a weighted-ensemble (WE) simulation resolving the flux into the target state; milestoning; or a metadynamics/infrequent-metadynamics rate estimate with the requisite time-rescaling. Each is a means to the same on-machine quantity.

**On-machine consistency checks (exact for the Hamiltonian).**
- *Detailed balance / reversibility:* the MSM transition matrix estimated under a reversibility constraint must be consistent (within error) with the unconstrained one; stationary distribution must match the equilibrium populations.
- *MFPT–rate equality:* the rate from the leading MSM eigenvalue/implied timescale must equal $1/\text{MFPT}$ from transition-path theory, within error.
- *Flux stationarity (WE):* the WE flux into the target must reach a steady state, with the recycling boundary condition documented.

**Accuracy thresholds (numeric).**
- *Rate reproduction.* A reproduced published rate must agree in $\log_{10} k$ to within the combined stated uncertainty, and the pipeline's own estimate must carry a statistical error (from independent WE replicas or MSM bootstrap) of $\le 0.5$ in $\log_{10} k$.
- *Consistency.* MFPT-vs-eigenvalue rate and forward/backward detailed-balance checks agree within their error bars.
- *Ranking (P4).* For a congeneric series, Spearman/Kendall rank correlation of predicted vs reference residence times, reported with a bootstrap confidence interval, and against a stated reference.

No informal target ("captures the trend") is accepted without one of these.

## 2. Resolution standard

A resolution, for a stated system and fixed Hamiltonian, consists of:

1. A rate ($k_{\text{off}}$ and/or $k_{\text{on}}$) estimated with a WE/MSM/milestoning pipeline whose **convergence is certified** (independent-replica or bootstrap error $\le 0.5$ in $\log_{10} k$), passing the MFPT-vs-eigenvalue and detailed-balance consistency checks.
2. An internal cross-check that $k_{\text{off}}/k_{\text{on}}$ reproduces the equilibrium $K_d$ computed independently on the same Hamiltonian, within combined error.
3. Validation on a system or ligand not used to tune the protocol.

**Not accepted as resolution:**

- A single unbinding event (or a handful) reported as a rate - a rate is a converged statistical quantity, and $N=1$ has no error bar.
- A rate that passes no consistency check (MFPT vs eigenvalue, detailed balance, $K_d$ closure) - an isolated number from one estimator can be badly biased by an unconverged slow process.
- Matching an *experimental* rate while skipping the on-machine convergence certification (experiment agreement can come from error cancellation and is force-field-limited).
- A host–guest success presented as solving protein–ligand kinetics.
- Infrequent-metadynamics rates without the required time-rescaling validity check (Kolmogorov–Smirnov test on the escape-time distribution).
- A ranking result on a series that was used to tune the CVs/protocol.

**Benchmark-integrity clause.** The rare-event verifier is exact for the Hamiltonian but carries a specific, severe hazard: *rates are exponentially sensitive to the barrier, so an unconverged sampler or a slightly wrong CV can be off by orders of magnitude while looking self-consistent.* The internal consistency checks (MFPT vs eigenvalue, detailed balance, $K_d$ closure) are the primary guard and are mandatory. The teaching-to-the-test guard for the ranking target is a frozen, hash-committed ligand split - CVs, state definitions, and protocol frozen on a training subset, then applied blind. And the on-machine claim ("this is the rate of this force field's dynamics") is kept strictly separate from experiment comparison: because rates depend on barrier heights, force-field error hits them harder than it hits free energies, so an experiment-matching rate is *weaker* evidence of correctness here than elsewhere, not stronger.

## 3. Graded partial-result targets

- **P1 - Reproduce a published k_off with a verified WE/MSM pipeline.** Reproduce a literature rate (e.g. a benzamidine–trypsin $k_{\text{on}}$ or a host–guest $k_{\text{off}}$) with our own WESTPA or MSM pipeline, matching within combined uncertainty and passing the consistency checks. *Certificate:* the WE flux-vs-time / MSM implied-timescale plots, bootstrap error bars, MFPT-vs-eigenvalue agreement. Establishes the toolchain.
- **P2 - Certified rate with error bars on a model host–guest.** Compute $k_{\text{off}}$ and $k_{\text{on}}$ for a host–guest system with $\ge 2$ independent WE replicas (or a bootstrapped MSM) agreeing within $0.5$ in $\log_{10} k$, and verify $k_{\text{off}}/k_{\text{on}}$ closes to the independently computed $K_d$. *Certificate:* replica agreement, $K_d$-closure residual, detailed-balance check.
- **P3 - A rate prediction on a target with convergence certification.** Predict a rate for a small protein–ligand system, with full convergence certification and consistency checks, on the same Hamiltonian. *Certificate:* convergence diagnostics, consistency checks, and an explicit statement of the force-field caveat.
- **P4 - Residence-time ranking of a congeneric series.** Rank a congeneric ligand series by predicted residence time and report Spearman/Kendall correlation with bootstrap CI against a reference, with the protocol **frozen on a held-out split** before ranking. *Certificate:* frozen split hash, per-ligand converged rates with errors, rank-correlation CI, and the benchmark-integrity statement. Guard mandatory.
- **P5 - Cross-validated estimator agreement.** Strongest short of resolution: show two independent estimators (e.g. WE and an MSM from adaptive short trajectories, or milestoning and infrequent metadynamics) agree on a rate within error for the same system - the closest on-machine analog of an external check. *Certificate:* both estimators' rates with errors, and the escape-time-distribution validity test for the metadynamics estimate.

## 4. Known results and prior art

- Markov state models for kinetics: Prinz, Wu, Sarich, ... Noé 2011; Chodera & Noé ~2014; Bowman, Pande, Noé (MSM book ~2014). MSMBuilder (Pande group); PyEMMA / deeptime (Noé group).
- Weighted ensemble: Huber & Kim 1996 (original); WESTPA (Zuckerman, Chong, Dickson, and collaborators ~2015–2019); computed $k_{\text{on}}$/$k_{\text{off}}$ for protein–ligand via WE (Saglam & Chong; Dickson).
- Long-MD computed association: benzamidine–trypsin $k_{\text{on}}$ from unbiased MD (Buch, Giorgino, De Fabritiis 2011). Anton fast-kinetics studies (Shaw group, where accessible).
- Milestoning: Faradjian & Elber 2004; Elber's milestoning and Markovian milestoning (e.g. SEEKR - Amaro, Votapka, Amaro ~2017, verify).
- Metadynamics-based rates: infrequent metadynamics (Tiwary & Parrinello 2013), with the Salvalaglio–Tiwary–Parrinello KS-test validity check (2014). $\tau$-RAMD (random acceleration MD) for relative residence times: Kokh, Wade et al ~2018.
- Adaptive multilevel splitting (AMS) for rare events: Cérou & Guyader; Lelièvre and collaborators.
- Residence time and drug efficacy: Copeland, Pompliano, Meek 2006 (drug–target residence time concept); Copeland reviews.

**Status as of mid-2026 - re-verify against current literature before starting any session.**

## 5. Attack plan

`[struct]` mode; one workstation, one GPU (WE and MSM parallelize over many short trajectories, which fits GPU-batched MD well).

1. **Reference dynamics.** OpenMM (GPU) for the underlying MD; many short trajectories for MSM/WE. Stated integrator, thermostat, friction - the dynamics is part of the Hamiltonian for kinetics.
2. **Estimators.** WESTPA for weighted ensemble; deeptime/PyEMMA for MSMs (with the automated-MSM discipline of the sibling MSM problem - VAMP scoring, CK test, implied-timescale convergence); SEEKR/milestoning or PLUMED infrequent-metadynamics as the second estimator for P5. Failure mode: an unconverged slow process the CV/state-decomposition misses biases the rate by orders of magnitude - the consistency checks and the second estimator are the guard.
3. **Consistency machinery.** Compute MFPT via transition-path theory and via the leading implied timescale; check detailed balance; close $k_{\text{off}}/k_{\text{on}}$ against an independent equilibrium $K_d$ (alchemical or PMF). This is the certificate, not a diagnostic afterthought.
4. **Ranking (P4).** Freeze protocol on a training ligand subset; commit the split hash; rank the held-out ligands blind; bootstrap the rank correlation. Failure mode: CV/state tuning leaking the answer - frozen split before ranking.
5. **Force-field honesty.** Report the force-field caveat prominently: a converged rate is the force field's rate; barrier sensitivity makes experiment comparison a weak check here. Where a workstation cannot converge a system's slow unbinding, state the limit.

## 6. Verification and auditability requirements

1. **Certified numerics.** Every rate carries a statistical error from $\ge 2$ independent WE replicas or an MSM bootstrap; convergence is certified by flux-stationarity (WE) or implied-timescale plateau and CK test (MSM). A rate without an error bar and a consistency check does not count.
2. **Independent verification.** The rate-estimation and consistency-check code is separate from the trajectory-generation code; a standalone checker recomputes MFPT and the rate from stored transition counts / flux data; a second estimator (P5) reproduces at least one rate.
3. **Reproducibility.** Force field, water model, integrator/thermostat/friction, seeds, WE binning / MSM lag-time and state definitions, and the frozen ligand split are recorded with a SHA-256 manifest; splits committed before ranking.
4. **Preservation.** Estimator code, failed state decompositions, and non-converged runs (with reasons) are part of the record; a rate that failed a consistency check is a finding.
5. **Honest reporting.** The report states up front whether a rate was *converged and consistency-checked* on the given Hamiltonian (the resolution metric), reports the force-field caveat with emphasis on barrier sensitivity, presents any experiment comparison separately and as a weak check, and never reports a single unbinding event or a consistency-check-failing number as a rate.
