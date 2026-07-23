# PROMPT FOR A UNIVERSAL CCSD(T)-ACCURATE MACHINE-LEARNED INTERATOMIC POTENTIAL

## A transferable foundation MLIP matching coupled-cluster energetics across chemical space

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** A - closed-loop (on-machine verifier)
**Rank:** A-05 of 21
**Source:** chem/bio top-50 list #4, section A (electronic structure)
**Modes:** `[func]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

A single machine-learned interatomic potential (MLIP) that reproduces gold-standard CCSD(T)/CBS energies and forces *uniformly* across chemical space - all main-group elements, charges, spin states, and bonding environments - would replace density functional theory as the default engine for molecular dynamics, folding, catalysis screening, and materials search.

Foundation MLIPs are close in a weak sense: MACE-OFF and MACE-MP (Batatia, Csányi and co-workers), Allegro/NequIP (Kozinsky group), Orb, and related equivariant message-passing models reach roughly $1\,\mathrm{kcal/mol}$ on standard benchmarks - but *not uniformly*, failing on out-of-distribution chemistries, charged and open-shell species, and reactive transition states.

The distinguishing feature of this problem is that **the verifier is on-machine and definitive**: the model's own claims are checked by CCSD(T)/CBS single-points that the session itself runs on held-out geometries. The task is therefore not "train a bigger model" but "characterize and certifiably close the accuracy gap on a named domain, with a prospective held-out test the model never saw." Anything short of the section-2 standard is reported as a partial result, never as a solution.

## 1. Exact problem statement

**Reference method (ground truth).** The target label for a configuration $R$ (nuclei $Z_i$, positions, total charge $q$, spin multiplicity $2S{+}1$) is the Born–Oppenheimer energy at the **complete-basis-set CCSD(T)** level,

\[
E_{\text{ref}}(R) = \lim_{X\to\infty} E_{\text{CCSD(T)}}^{\text{cc-pV}XZ}(R),
\]

estimated by a fixed, documented composite recipe:

- Hartree–Fock and CCSD(T) correlation extrapolated from at least cc-pVTZ→cc-pVQZ (two-point $X^{-3}$ correlation extrapolation);
- frozen-core unless stated; counterpoise or CBS handling specified per subset;
- the exact recipe frozen and version-stamped.

Forces are analytic or finite-difference CCSD(T) gradients under the same recipe. For heavy elements the reference is CCSD(T) with a named small-core relativistic ECP and matching basis; the relativistic treatment is documented per element.

**Admissible model class.** A single set of weights $\theta$ defining a potential $E_\theta(R)$ that is:

- translation-, rotation-, and permutation-invariant;
- size-extensive / decomposable into local atomic contributions with a finite cutoff;
- smooth ($C^1$ at least, $C^2$ preferred) so forces $-\nabla_R E_\theta$ and Hessians are defined;
- conditioned on total charge and spin where those are degrees of freedom.

No per-system refitting: the same $\theta$ is evaluated on the held-out set.

**Accuracy threshold (numeric).** "CCSD(T) accuracy" is defined, not gestured at:

- **Energies:** mean absolute error (MAE) $\le 1\,\mathrm{kcal/mol}$ ($\approx 1.6\,\mathrm{mHartree}$) *and* 95th-percentile absolute error $\le 2\,\mathrm{kcal/mol}$ on relative energies (conformers, reaction energies, interaction energies) over the held-out set, referenced to CCSD(T)/CBS.
- **Forces:** MAE $\le 1\,\mathrm{kcal/mol/\text{\AA}}$ (per component) vs CCSD(T) gradients on held-out geometries.
- **Barriers:** transition-state relative energies within $1\,\mathrm{kcal/mol}$ where reactive data is in scope.

The tail matters: a low mean with a fat error tail on OOD chemistry does **not** meet the threshold. Units are kcal/mol throughout with the mHartree equivalence fixed.

## 2. Resolution standard

Full resolution is a single $\theta$ meeting the section-1 thresholds *uniformly* across a stated, broad admissible domain (defined element set, charge range, spin range, bonded/non-bonded/reactive environments), demonstrated on a **prospective** held-out test whose reference labels are computed *after* the model is frozen.

The deliverable is the model, the frozen test protocol, the CCSD(T) reference calculations the session ran, and per-subset error distributions including tails.

**Not accepted as resolution:**

- A benchmark MAE $\le 1\,\mathrm{kcal/mol}$ on a public test set whose chemistries overlap the training distribution - publicly frozen benchmarks leak into foundation-model pretraining.
- A model matching CCSD(T) on neutral closed-shell organic molecules only, presented as "universal" - charge, spin, transition metals, and reactive TSs are in scope for the full claim.
- Low mean error with an unreported or fat error tail (a few large failures make dynamics unreliable).
- Matching a *DFT* reference and calling it CCSD(T) accuracy.
- A model whose forces are inconsistent with its energies (non-conservative), or whose good energetics come from error cancellation that breaks under MD (assessed by energy drift in NVE).

**Benchmark-integrity clause.** The CCSD(T) verifier is strong but has named biases.

- *CCSD(T) is itself imperfect* for strong static correlation (multireference character): near bond dissociation, biradicals, and some transition-metal centers, the $\mathcal T_1$ diagnostic flags unreliability. Such points must be labeled and either excluded with justification or referenced to a higher method (e.g. CCSDT(Q) or DMRG), not silently trusted.
- *Basis/extrapolation bias.* CBS extrapolation carries its own error ($\sim 0.2$–$0.5\,\mathrm{kcal/mol}$); the composite recipe's uncertainty is reported and must be smaller than the claimed model accuracy.
- *Distribution leakage.* The single most important guard is that the held-out test is *prospective* - geometries and chemistries generated and labeled after $\theta$ is frozen, drawn from a domain deliberately shifted from training (new element combinations, new charge/spin states). A benchmark win on a possibly-leaked public set is reported as "in-distribution", never as the uniform claim.

## 3. Graded partial-result targets

**P1 - Reproduce a foundation-MLIP benchmark with our verified pipeline.** Re-run a published foundation MLIP (or retrain a MACE/NequIP-class model) and reproduce its reported error on a standard set (e.g. an atomization/reaction-energy or MD17-class benchmark), *and* independently recompute a random 5% of the reference labels with our own CCSD(T)/CBS pipeline to confirm the reference itself. *Certificate:* matching errors within noise; our recomputed references agreeing with the published ones within the recipe uncertainty.

**P2 - Certified error characterization on a held-out chemistry.** Take a frozen foundation model and measure its error distribution (mean *and* tail) on a chemistry it was not trained for, using freshly computed CCSD(T)/CBS labels. *Certificate:* the prospective label set, the frozen-model hash, and the full per-subset error CDF with $\mathcal T_1$ diagnostics flagging multireference points.

**P3 - Fine-tune to CCSD(T) on a target domain with prospective test.** Fine-tune a foundation model on a defined domain (e.g. neutral organosulfur, or a specific reaction family) to meet the section-1 thresholds, verified on a prospective held-out test computed after freezing. *Certificate:* frozen-model hash predating the test-label computation; error CDF meeting thresholds including the 95th percentile.

**P4 - Active learning to close a specified accuracy gap.** Given a domain where the model fails P2, run an on-machine active-learning loop (uncertainty-driven sampling → CCSD(T) labeling → retrain) and demonstrate the gap closes to threshold on a prospective test, reporting the label budget spent. *Certificate:* the full AL trajectory, uncertainty metric, and final prospective CDF.

**P5 - Broaden the certified domain.** Extend a P3/P4 model to an additional axis (charge *or* spin *or* one transition-metal block) with the thresholds still met on the enlarged prospective test - a documented step toward uniformity, explicitly short of the full universal claim. *Certificate:* held-out errors across the enlarged domain, tails included.

## 4. Known results and prior art

- Behler & Parrinello (2007) - high-dimensional neural network potentials, the local-decomposition template. Bartók, Payne, Kondor, Csányi (2010) - GAP/SOAP.
- Schütt et al. (2017–2018) - SchNet; Gasteiger (Klicpera) et al. - DimeNet (directional message passing).
- Batzner, Kozinsky et al. (2022) - NequIP (E(3)-equivariant message passing). Musaelian, Kozinsky et al. (2023) - Allegro (strictly local equivariant).
- Batatia, Csányi et al. (2022) - MACE (higher-order equivariant messages). MACE-MP-0 / MACE-OFF (2023–2024) - foundation potentials for materials and organic chemistry.
- Orb (Orbital Materials, 2024, verify), Equiformer/EquiformerV2 (Liao, Smidt et al.), and other foundation MLIPs; the Open Catalyst (OC20/OC22) and Materials Project / MPtrj / Matbench-Discovery efforts as pretraining/benchmark corpora - mostly DFT-labeled, a key caveat for a CCSD(T) claim.
- Smith, Isayev, Roitberg (2017) - ANI-1; ANI-1ccx (2019) - transfer learning to CCSD(T) accuracy on organic molecules, an important precedent that is *not* universal (neutral CHNO organics).
- Chen & Ong (2022) - M3GNet; Deng et al. - CHGNet (charge-aware, materials).
- Benchmarks: GMTKN55 (Goerigk, Grimme) for main-group thermochemistry/kinetics (DFT-oriented but with high-level references); MD17 / rMD17; SPICE dataset (Eastman et al., 2023) for drug-like chemistry with $\omega$B97 references (not CCSD(T)).

*Status as of mid-2026 - re-verify against current literature before starting any session.*

## 5. Attack plan

**Reference/verifier layer.** CCSD(T)/CBS single-points and gradients with **PSI4** or **PySCF** (DF-CCSD(T) or conventional) for light elements; **ORCA** (DLPNO-CCSD(T) with tight thresholds, calibrated against canonical CCSD(T) on a subset) for larger molecules where canonical CCSD(T) is infeasible. Fix the composite recipe (HF/CBS + correlation TZ→QZ extrapolation, frozen core) in a single script, and compute $\mathcal T_1$/$D_1$ diagnostics for every reference point. A single workstation handles up to $\sim 20$–$30$ atoms canonically at TZ; DLPNO extends this but its threshold error must be calibrated and reported.

**Model layer `[func]`.** Start from a **MACE** or **NequIP/Allegro** implementation (PyTorch, one prosumer GPU - 24 GB is workable for these architectures). For P1, retrain on an existing corpus; for P3/P4, fine-tune from a foundation checkpoint. Ensure a charge/spin embedding where those are in scope. Train forces and energies jointly with a conservative (gradient-of-energy) force head so the potential is exactly conservative - verify by NVE energy drift in a short MD.

**Active-learning layer `[func]`.** Estimate uncertainty via a deep ensemble or the model's native committee disagreement; sample high-uncertainty geometries from short MD or normal-mode displacement; label the top-$k$ with the CCSD(T) pipeline; retrain. Track the label budget throughout.

**Certified-evaluation layer.** Freeze $\theta$ and hash it. Generate the prospective test geometries and compute their CCSD(T)/CBS labels *after* freezing. Report the full error CDF per subset, the tail percentiles, and $\mathcal T_1$-flagged multireference points separately.

**Expected failure modes.**

- DLPNO threshold error masquerading as model error - calibrate first.
- Multireference reference points where CCSD(T) is itself wrong; the model "fails" against a bad label.
- Charge/spin states poorly represented - foundation models often assume neutral closed-shell.
- Force/energy inconsistency causing MD energy drift despite good static errors.
- Silent distribution overlap between "held-out" and pretraining - only a genuinely prospective, domain-shifted test controls this.

## 6. Verification and auditability requirements

1. **Exact or certified numerics.** Every accuracy claim is a held-out MAE *and* tail percentile against freshly computed CCSD(T)/CBS labels with a stated recipe uncertainty; the recipe uncertainty must be smaller than the claimed model accuracy. Energy–force consistency is verified by NVE drift. Floating-point training loss is never the reported metric.
2. **Independent verification.** A standalone evaluation script - separate from training - loads the frozen $\theta$ and the reference labels and recomputes all error statistics; a random subset of reference labels is recomputed with a second code (PSI4 vs PySCF vs ORCA) to bound the reference's own error.
3. **Reproducibility.** Training data, splits, seeds, hyperparameters, model version/hash, the CCSD(T) recipe, and the prospective-test generation protocol are recorded; SHA-256 manifest over all artifacts; the frozen-model hash provably predates the prospective label computation (timestamped).
4. **Preservation.** Training code, checkpoints, active-learning logs, and the reference-calculation inputs are part of the record. Anything not preserved is stated explicitly.
5. **Honest reporting.** The report states up front whether the uniform section-2 standard was met (it very likely was not - graded targets are the product), reports the prospective held-out CDF including tails and multireference flags, distinguishes in-distribution from prospective results, and never presents an in-distribution benchmark win as universality.
