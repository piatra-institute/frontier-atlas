# PROMPT FOR ABSOLUTE BINDING FREE ENERGIES BELOW 1 kcal/mol

## The drug-discovery money problem - cycle closure on-machine, force-field limit against reality

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Pack:** A - closed-loop (on-machine verifier)  
**Rank:** A-15 of 21  
**Source:** chem/bio top-50 list #10, section B (free energy, dynamics, sampling)  
**Modes:** `[func]` `[struct]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

A reliable absolute binding free energy $\Delta G_{\text{bind}}$ accurate below 1 kcal/mol would change drug discovery, because a factor-of-ten error in predicted affinity is a $\sim 1.4$ kcal/mol error, and the whole enterprise turns on getting there. Alchemical free-energy methods (absolute FEP, double-decoupling, ML/FEP hybrids) can be made *self-consistent* on-machine: alchemical thermodynamic cycles close exactly for a fixed Hamiltonian, and cycle-closure residual is a precise, machine-checkable measure of statistical convergence. But this is exactly the problem the program flags as the highest **confident-but-wrong risk**, because the object anyone actually cares about - the *experimental* $\Delta G_{\text{bind}}$ - is capped by force-field error the on-machine verifier is blind to. The entire file is organized around one distinction, which is its spine: **cycle closure and statistical convergence are on-machine facts about the chosen Hamiltonian; agreement with experiment is a separate, reality-gated, force-field-limited fact.** A pipeline can close every cycle to $0.05$ kcal/mol and still be $2$ kcal/mol from experiment because the force field is wrong. Reporting the first as if it were the second is the failure mode this prompt exists to prevent. Anything short of section 2 is a partial result, and "matches experiment on a benchmark" is never by itself a resolution.

## 1. Exact problem statement

**System class.** Two tiers. *(T1) Host–guest:* rigid or semi-rigid host–guest complexes with converged references and no protein sampling problem (cucurbituril CB7/CB8, octa-acids OA/TEMOA, cyclodextrins) - the SAMPL blind-challenge chemical space. *(T2) Protein–ligand:* congeneric and cross-chemotype ligand sets against well-behaved targets (the standard published protein–ligand FEP benchmark sets). Declared per run.

**Hamiltonian (fixed and named).** A stated protein/host force field, ligand force field (e.g. GAFF2/OpenFF with a stated charge model), and water model define $U(x)$. The computed $\Delta G_{\text{bind}}$ is a property of this $U$.

**Target quantity.** The standard-state absolute binding free energy
$$
\Delta G_{\text{bind}} = -k_BT\,\ln\!\big(K_a\,c^\circ\big),
$$
computed by an alchemical double-decoupling / double-annihilation cycle: decouple the ligand from the binding site (with restraints whose free-energy contribution is analytically or numerically corrected) and from bulk solvent, along $\lambda$ paths, combining legs so restraint and standard-state corrections cancel exactly in the cycle. Equivalent formulations (attach–pull–release for host–guest; absolute FEP with Boresch restraints for protein–ligand) are admissible if the correction terms are stated and the cycle is closed.

**On-machine exactness - cycle closure.** For any closed alchemical thermodynamic cycle (e.g. a mutation $A\to B$ done directly and via an intermediate, or a relative $\Delta\Delta G$ decomposed two ways), the sum of leg free energies must be zero *exactly* for the true Hamiltonian averages. The measured cycle-closure residual is therefore a pure statistical-convergence diagnostic: it is nonzero only because of finite sampling, and it is machine-checkable to arbitrary precision by running the legs. This is the exact on-machine verifier.

**Accuracy thresholds (numeric).** Two *separate* thresholds, never merged.
- *On-machine (resolution metric).* Cycle-closure residual $\le 0.1$ kcal/mol; per-edge statistical error (from BAR/MBAR with overlap diagnostics and $\ge 2$ independent replicas) $\le 0.2$ kcal/mol; restraint/standard-state corrections itemized. "Below 1 kcal/mol" *as a convergence claim* means the free energy is statistically converged for the Hamiltonian to $< 1$ kcal/mol uncertainty.
- *Reality (downstream, force-field-limited).* RMSE vs *experimental* $\Delta G_{\text{bind}}$ on a frozen benchmark, reported with the explicit statement that this number is capped by force-field error and is not a convergence property. "Sub-kcal/mol vs experiment" means RMSE $\le 1.0$ kcal/mol (and, more strictly, $\le 0.5$) on a held-out set - a target that may be *unreachable at fixed force field* regardless of sampling.

## 2. Resolution standard

Because of the spine of this problem, resolution is defined in two explicitly separated parts, and a claim to the second requires the first.

**On-machine resolution (convergence).** For a stated system and Hamiltonian:
1. Absolute $\Delta G_{\text{bind}}$ with cycle-closure residual $\le 0.1$ kcal/mol and per-edge error $\le 0.2$ kcal/mol, all corrections itemized, references converged (overlap matrices, replica agreement).
2. Independent-estimator agreement (BAR vs TI, or two restraint schemes) within combined error.

**Reality-gated resolution (accuracy).** In addition:
3. RMSE $\le 1.0$ kcal/mol (target $\le 0.5$) vs experimental $\Delta G_{\text{bind}}$ on a **frozen, held-out** benchmark, reported with the force-field-limit caveat and with the cycle-closure evidence proving the residual error is force-field, not sampling.

**Not accepted as resolution:**

- Cycle closure and low statistical error presented *as if* they were accuracy against experiment. This is the headline prohibition: perfect on-machine convergence is not a solution to the binding-affinity problem.
- Experiment-matching RMSE on a benchmark **without** cycle-closure / convergence evidence - such a match can be sampling error compensating force-field error, and is confident-but-wrong.
- A benchmark result on a set used to tune the force field, the charge model, or the protocol.
- Host–guest success (T1) presented as solving protein–ligand affinity (T2).
- A single congeneric series' good ranking presented as general absolute-affinity accuracy (ranking is easier than absolute; state which is claimed).
- Any RMSE quoted without the frozen split committed before evaluation.

**Benchmark-integrity clause (the spine).** This problem is the program's flagged confident-but-wrong case, so the clause is load-bearing. The on-machine verifier (cycle closure) is *exact but blind to reality*: it certifies convergence for the Hamiltonian and nothing about whether the Hamiltonian is right. The reality verifier (experimental $\Delta G$ benchmarks - SAMPL host–guest, the standard protein–ligand FEP sets) is *right but confounded*: force-field error, protonation/tautomer/pose ambiguity, and buffer/salt conditions all enter the measured number. Two mandatory guards. (i) *Separation of metrics:* every report states the cycle-closure/convergence result and the experiment-RMSE result as two distinct numbers, and states which errors are sampling (reducible by more compute) versus force-field (irreducible at fixed $U$). (ii) *Held-out / prospective guard:* a frozen, hash-committed benchmark split committed before evaluation, and where possible a prospective set scored blind, to prevent teaching-to-the-test - the more so because published FEP benchmarks have been iterated against by force-field developers, so a strong retrospective number is weak evidence. An ML/FEP hybrid trained on experimental affinities is especially exposed and must show it has not simply memorized the benchmark's force-field-error pattern.

## 3. Graded partial-result targets

- **P1 - Reproduce a host–guest ΔG with certified cycle closure.** Compute an absolute $\Delta G_{\text{bind}}$ for a SAMPL host–guest system (T1) with cycle-closure residual $\le 0.1$ kcal/mol, itemized corrections, and converged references. *Certificate:* the cycle legs, closure residual, BAR/MBAR overlap matrices, replica agreement. Establishes the toolchain and the on-machine verifier.
- **P2 - Certified statistical convergence on a protein–ligand case.** For one protein–ligand complex (T2), deliver an absolute $\Delta G_{\text{bind}}$ with certified convergence (per-edge error $\le 0.2$ kcal/mol, replica agreement, independent-estimator agreement) - *making no accuracy claim vs experiment yet*, only convergence. *Certificate:* convergence diagnostics, restraint-correction itemization, BAR-vs-TI agreement.
- **P3 - Sub-kcal/mol on a frozen benchmark with held-out guard.** On a frozen, hash-committed benchmark split, report experiment-RMSE with the convergence evidence attached, hitting $\le 1.0$ kcal/mol on the held-out portion, and *decompose* the residual into the sampling part (from cycle closure) and the force-field part. *Certificate:* the committed split, held-out RMSE, cycle-closure-based error decomposition, and the force-field-limit statement. Benchmark-integrity guard mandatory.
- **P4 - Ranking accuracy with honest force-field-limit statement.** Report ranking metrics (Spearman/Kendall, with CI) for a congeneric series, clearly labeled as ranking (not absolute accuracy), with the frozen split and the statement that force-field error caps absolute accuracy. *Certificate:* rank-correlation CI, split hash, per-ligand convergence.
- **P5 - ML/FEP hybrid with a non-memorization guard.** Strongest short of resolution: an ML correction to alchemical FEP that improves held-out experiment-RMSE while *demonstrably not memorizing* the benchmark (leave-cluster-out / scaffold-split validation, and a prospective blind subset). *Certificate:* scaffold-split held-out RMSE, prospective-subset result, and an ablation isolating the ML gain from data leakage. This is the highest confident-but-wrong risk target and carries the strictest guard.

## 4. Known results and prior art

- Double-decoupling / absolute alchemical FEP: Gilson, Given, Bush, McCammon ~1997 (statistical-thermodynamic basis); Boresch, Tettinger, Leitgeb, Karplus 2003 (restraint corrections and standard state); Jorgensen; Deng & Roux ~2009 (review).
- Relative binding FEP at scale: Wang et al (Schrödinger) 2015 (FEP+, JACS benchmark set); Schindler et al 2020 (Merck/industry large-scale prospective FEP+ benchmark, verify).
- Open-source alchemical tooling: Yank and perses (Chodera group); OpenFE / openfe (Open Free Energy consortium ~2022–2024); GROMACS and AMBER TI/FEP; `pymbar` / MBAR (Shirts & Chodera 2008); alchemlyb.
- Host–guest attach–pull–release (APR): Velez-Vega & Gilson; Henriksen, Gilson (SAMPL host–guest, e.g. the APR pipeline ~2015–2018).
- SAMPL blind challenges (host–guest and beyond): Mobley, Gilson, and organizers (multiple rounds); the octa-acid and cucurbituril data sets.
- ML/FEP hybrids and force-field improvements: OpenFF (Mobley, Wang, and the Open Force Field Initiative); ML-corrected free energies and neural-network/MM (NNP/MM) alchemical schemes (Rufa, Chodera et al ~2020–2022, verify); Espaloma charge/parameter models (Wang, Chodera ~2022, verify).
- Force-field-limit analyses: repeated findings that converged FEP RMSE plateaus near ~1 kcal/mol regardless of sampling, attributed to force field (multiple groups; verify specific citations).

**Status as of mid-2026 - re-verify against current literature before starting any session.**

## 5. Attack plan

`[func]` + `[struct]` mode; one workstation, one GPU.

1. **Alchemical engine and cycle machinery.** OpenMM + perses/openfe, or GROMACS/AMBER, for the $\lambda$-window simulations; MBAR via `pymbar`/alchemlyb with overlap diagnostics; explicit thermodynamic cycles (direct + indirect legs) so closure residual is computed as the primary convergence certificate. Failure mode: missing or mis-signed restraint/standard-state correction - itemize every term and verify by an independent restraint scheme.
2. **Host–guest first (P1).** No protein sampling problem, so cycle closure isolates the alchemical bookkeeping; get closure $\le 0.1$ kcal/mol before touching proteins.
3. **Protein–ligand convergence (P2).** Enhanced sampling of the bound state (replica exchange along $\lambda$, or REST) to make the per-edge error real; certify convergence *before* any experiment comparison. Failure mode: slow protein/side-chain/water rearrangement leaving an edge unconverged while closure of a small cycle looks fine - use larger cycles and replica agreement.
4. **Experiment comparison, guarded (P3–P5).** Frozen hash-committed split; scaffold/cluster splits for any ML component; decompose residual into sampling (cycle closure) and force-field parts. Failure mode: leakage via force-field parameters previously fit to the benchmark - prospective blind subset.
5. **Force-field-limit reporting.** Every experiment number carries the caveat and the error decomposition. State plainly where sub-kcal/mol vs experiment is unreachable at the chosen force field, and that this is a force-field problem, not a sampling one.

## 6. Verification and auditability requirements

1. **Certified numerics.** Every $\Delta G_{\text{bind}}$ carries a cycle-closure residual, BAR/MBAR overlap diagnostics, per-edge statistical error, and $\ge 2$ independent replicas; convergence certification is the gating step. Experiment-RMSE is reported only with this convergence evidence attached.
2. **Independent verification.** The free-energy-estimation and cycle-closure code is separate from the simulation-driver code; a standalone checker recomputes each $\Delta G$ and closure residual from stored $\lambda$-window samples; a second estimator (BAR vs TI) and, where feasible, a second engine reproduce a headline number.
3. **Reproducibility.** All force-field files, charge model, water model, restraint definitions, $\lambda$-schedules, seeds, and the frozen benchmark split (with scaffold/cluster assignments) are recorded with a SHA-256 manifest; splits committed before evaluation.
4. **Preservation.** Alchemical setup code, any ML-correction training code, failed restraint schemes, and unconverged edges (with reasons) are part of the record.
5. **Honest reporting.** The report states, in its first sentences and as two distinct numbers, (a) the on-machine convergence result (cycle closure, statistical error) and (b) the experiment-RMSE with the explicit force-field-limit caveat and the sampling-vs-force-field error decomposition. It never presents cycle closure as accuracy, never presents an experiment match without convergence evidence, and never presents a retrospective benchmark number without the held-out/prospective guard.
