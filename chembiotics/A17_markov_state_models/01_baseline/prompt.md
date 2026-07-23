# PROMPT FOR AUTOMATED MARKOV STATE MODEL CONSTRUCTION

## Building a validated MSM without human babysitting, certified by CK test and VAMP score

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Pack:** A - closed-loop (on-machine verifier)  
**Rank:** A-17 of 21  
**Source:** chem/bio top-50 list #14, section B (free energy, dynamics, sampling)  
**Modes:** `[algo]` `[data]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

A Markov state model (MSM) turns a pile of short molecular-dynamics trajectories into a discrete-state kinetic model - stationary populations, metastable states, transition rates, and slow timescales. Building one well is a craft: featurization, dimensionality reduction, clustering, lumping into metastable states, and lag-time selection are all hand-tuned, and the same trajectory data yield different MSMs in different hands. Automating this end to end - with the choices made by verifiable quality criteria rather than by a human - is the target. This prompt fixes the on-machine verifier at the standard MSM validation battery, all of which are exact, quantitative, and simulation-native: the **Chapman–Kolmogorov (CK) test** (does the model propagated to $k\tau$ match the data at $k\tau$?), **implied-timescale convergence** (are the slow timescales flat in lag time?), and the **VAMP-2 score** (a cross-validated variational bound on the captured slow dynamics). The task is an automated construction pipeline whose outputs pass this battery, with the model-selection decisions made by the scores rather than by eye. The honesty spine: **an MSM is a model of the given force field's trajectories; passing the CK test certifies self-consistency with those trajectories, not fidelity to nature.** And the CK test is necessary, not sufficient - a poorly sampled trajectory set can yield a self-consistent but incomplete MSM. Anything short of section 2 is a partial result.

## 1. Exact problem statement

**Inputs.** A set of MD trajectories $\{X^{(m)}_t\}$ on a fixed Hamiltonian, sampling (ideally) the relevant metastable states with some inter-state transitions. The trajectories are the data; the MSM is the model.

**The MSM (object to be constructed automatically).** A discrete-time Markov model at lag time $\tau$: a partition of configuration space into $n$ states and a row-stochastic transition matrix $T(\tau)\in\mathbb{R}^{n\times n}$, $T_{ij}(\tau)=\Pr[X_{t+\tau}\in j\mid X_t\in i]$, estimated (typically under a reversibility constraint) from transition counts. From $T(\tau)$ follow the stationary distribution $\pi$ (left eigenvector, eigenvalue 1), the implied timescales $t_k(\tau)=-\tau/\ln|\lambda_k(\tau)|$, and - after lumping via PCCA+ - a small set of metastable states with inter-state rates.

**The automation target.** A pipeline
$$
\{\text{trajectories}\} \ \xrightarrow{\ \text{automated}\ }\ \big(\text{featurization},\,\text{reduction},\,\text{clustering},\,\text{lag }\tau,\,\text{lumping}\big)\ \longrightarrow\ \text{validated MSM},
$$
in which every bracketed choice is made by a **verifiable quality criterion** (VAMP-2 cross-validation score, timescale convergence, CK residual), not by human inspection. The pipeline must be a fixed algorithm applied without per-system hand-tuning.

**On-machine verifiers (exact, quantitative).**
- *Implied-timescale convergence:* the slow timescales $t_k(\tau)$ must become independent of $\tau$ (within error) above some $\tau^\*$; the automated choice of $\tau$ is at/after this plateau.
- *Chapman–Kolmogorov test:* for metastable states, $T(k\tau)$ estimated from data must match $[T(\tau)]^k$ within statistical error, for a range of $k$. Quantified by the CK residual per state pair with error bands.
- *VAMP-2 score:* a cross-validated (train/test split of trajectories) VAMP-2 score measures how much of the slow dynamics the model captures; it is the objective for model selection and must be reported with its cross-validation variance.

**Accuracy / acceptance thresholds (numeric).** An automated MSM is *validated* iff: implied timescales are flat within error above the selected $\tau$; the CK test passes within the stated statistical band for all metastable-state pairs (no systematic deviation beyond $2\sigma$); and the VAMP-2 score is reported with cross-validation error and is not improved beyond noise by the next-more-complex model in the search. No informal target ("looks Markovian") is accepted.

## 2. Resolution standard

A resolution consists of:

1. A **fully automated** construction pipeline (no per-system human tuning of features, cluster count, lag, or lumping) that, applied to a trajectory set, outputs an MSM passing the full validation battery (timescale convergence + CK test within band + reported cross-validated VAMP-2).
2. Demonstration that the pipeline's automated choices are driven by the quality criteria - i.e. an ablation showing the selected model is the VAMP-2/CK-optimal one in the search, not a lucky default.
3. The pipeline works across **multiple** systems without re-tuning, with a stated quality criterion computed per system.

**Not accepted as resolution:**

- An MSM that passes the CK test but was hand-tuned to do so - automation is the point; a human-in-the-loop pipeline does not resolve the problem.
- A pipeline validated on one trajectory set / one system, presented as general.
- Passing the CK test on trajectories that never sampled a relevant slow process - the CK test certifies self-consistency of what *was* sampled, not completeness. A missing state makes a self-consistent but wrong MSM; sampling sufficiency must be argued separately.
- VAMP-2 score maximization without the CK test - a high VAMP-2 model can still fail Markovianity at the chosen lag.
- Reporting a single "best" MSM without cross-validation, hiding overfitting of the state decomposition.

**Benchmark-integrity clause.** The MSM validation battery is exact and on-machine, but it validates the model *against its own input trajectories* for a fixed Hamiltonian. Two guards. (i) *Sampling sufficiency is not tested by the CK test*: a trajectory set missing a slow transition yields an MSM that is internally consistent and externally wrong; the pipeline must report a sampling-sufficiency diagnostic (e.g. state connectivity, number of independent transitions per slow process, sensitivity to trajectory subsampling) and flag under-sampled MSMs as such. (ii) *Cross-validation of model selection*: the VAMP-2 score used to pick features/clusters/lag must be computed on held-out trajectories (train/test split by trajectory, not by frame, to respect correlation), with the split committed by hash before selection - otherwise the automation overfits the state decomposition to noise. And the on-machine claim ("this is a validated model of these force-field trajectories") is kept separate from any claim about experimental kinetics, which is downstream and force-field-limited.

## 3. Graded partial-result targets

- **P1 - Reproduce a published MSM with a verified automated pipeline.** Take a standard trajectory set (e.g. alanine dipeptide, or a published fast-folder dataset) and reproduce its published MSM's slow timescales and metastable states using an *automated* deeptime/PyEMMA pipeline, passing timescale convergence and the CK test. *Certificate:* implied-timescale plot, CK-test panels with error bands, cross-validated VAMP-2. Establishes the toolchain.
- **P2 - Certified CK-test-passing MSM on a target trajectory set.** For a new trajectory set, produce an MSM that passes the full battery, with the lag and state count selected automatically by the scores. *Certificate:* the automated selection trace (scores vs candidate models), CK residuals within band, sampling-sufficiency diagnostic.
- **P3 - An automated construction algorithm with a verifiable quality criterion across systems.** A single fixed pipeline that, applied without re-tuning to several systems, outputs battery-passing MSMs, each with its per-system VAMP-2 (cross-validated) and CK result. *Certificate:* per-system validation panels for one frozen pipeline, and the ablation showing scores drive the choices.
- **P4 - Robustness characterization.** Characterize how the automated MSM's slow timescales and metastable populations vary under trajectory subsampling, seed changes, and reasonable perturbations of the pipeline hyperparameters - i.e. deliver error bars on the *construction*, not just the model. *Certificate:* subsampling/bootstrap distributions of the key MSM observables, and a stability statement.
- **P5 - Deep-MSM / VAMPnet automation.** Strongest short of resolution: an end-to-end learned MSM (VAMPnet / deep MSM) whose training objective is the VAMP score and whose output passes the CK test, compared honestly against the classical automated pipeline (does the learned featurization help beyond noise?). *Certificate:* CK-passing deep MSM, cross-validated VAMP-2 vs the classical pipeline, and the honest verdict.

## 4. Known results and prior art

- MSM theory and validation: Prinz, Wu, Sarich, Keller, Senne, Held, Chodera, Schütte, Noé 2011 ("Markov models of molecular kinetics: generation and validation" - the CK test and implied-timescale framework). Bowman, Pande, Noé (MSM book ~2014).
- Variational approach and VAMP: Nüske, Keller, Pérez-Hernández, Schütte, Noé ~2014 (variational approach to conformational dynamics); Wu & Noé 2020 (VAMP - variational approach for Markov processes, the VAMP-1/VAMP-2 scores). Cross-validated model selection: McGibbon & Pande 2015.
- Metastable-state lumping: PCCA+ (Deuflhard & Weber ~2005; robust Perron-cluster analysis).
- Software: PyEMMA (Scherer, Trendelkamp-Schroer, ... Noé 2015); deeptime (Hoffmann, Scherer, Hempel, ... Noé, Clonts, Noé 2021); MSMBuilder (Harrigan, Beauchamp, ... Pande ~2017).
- TICA for MSM featurization: Pérez-Hernández, Noé 2013; Schwantes & Pande 2013.
- Deep MSMs / VAMPnets: Mardt, Pasquali, Wu, Noé 2018 (VAMPnets); Mardt, Noé (deep MSMs / state-free); Wu, Mardt, Pasquali, Noé ~2018 (deep generative MSMs, verify).
- Reference trajectory data: Anton fast-folder trajectories (Lindorff-Larsen, Piana, Shaw ~2011) where accessible; the DESRES datasets.

**Status as of mid-2026 - re-verify against current literature before starting any session.**

## 5. Attack plan

`[algo]` + `[data]` mode; one workstation, one GPU (MSM construction is CPU/GPU-light; the cost is the trajectory data, which can be reused public sets).

1. **Toolchain.** deeptime (primary) and PyEMMA (cross-check) for featurization (TICA), clustering (k-means / regular-space), estimation (reversible MLE), PCCA+ lumping, and the validation battery. Public trajectory sets (alanine dipeptide, fast folders) as data, reused rather than regenerated.
2. **Automation layer.** A pipeline that searches over featurizations, TICA dimensions, cluster counts, and lag times, selecting by *cross-validated VAMP-2* (trajectory-level train/test split), then confirming with the CK test. The search and the split are the algorithm; commit the split hash first. Failure mode: frame-level (not trajectory-level) splitting leaks correlated frames and inflates VAMP-2 - split by trajectory.
3. **Sampling-sufficiency diagnostics.** State connectivity, transitions-per-slow-process counts, and subsampling sensitivity, reported so under-sampled MSMs are flagged, not silently accepted. Failure mode: a beautiful CK test on an incomplete state space - this diagnostic is the guard.
4. **Robustness (P4).** Bootstrap over trajectories and over seeds to put error bars on the constructed timescales/populations.
5. **Deep MSM (P5).** VAMPnet in PyTorch with VAMP-2 objective; honest comparison to the classical pipeline. Failure mode: over-parameterized VAMPnet overfitting short data - cross-validation and CK test gate it.

## 6. Verification and auditability requirements

1. **Certified numerics.** Every validated MSM ships with implied-timescale-vs-lag data, CK-test panels with statistical bands, and a cross-validated VAMP-2 with its variance; a sampling-sufficiency diagnostic accompanies each. An MSM without the full battery does not count.
2. **Independent verification.** The validation battery (CK test, timescale computation, VAMP scoring) is implemented separately from the construction pipeline, and a second package (PyEMMA vs deeptime) reproduces at least one full validation.
3. **Reproducibility.** Trajectory-set provenance/hashes, featurization, all searched hyperparameters, the automated selection trace, the trajectory-level train/test split, and seeds are recorded with a SHA-256 manifest; the split is committed before model selection.
4. **Preservation.** The construction/search code, rejected candidate models, and the selection trace are part of the record; a rejected model is evidence the scores drove the choice.
5. **Honest reporting.** The report states up front whether a *fully automated* pipeline (no per-system hand-tuning) produced battery-passing MSMs across multiple systems, reports the sampling-sufficiency diagnostic beside every CK pass, keeps the on-machine (self-consistency) claim separate from any experimental-kinetics claim, and never presents a hand-tuned or single-system MSM as automated construction.
