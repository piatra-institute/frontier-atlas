# PROMPT FOR AUTOMATED REACTION-MECHANISM DISCOVERY

## Inferring elementary-step networks and transition states from data, with each step confirmed on-machine by TS + IRC + frequency analysis

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** A - closed-loop (on-machine verifier)
**Rank:** A09 of 21
**Source:** chem/bio top-50 list #50, section G (higher-order structure)
**Modes:** `[algo]` `[sym]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

A reaction mechanism is a network of elementary steps - each with its own transition state - connecting reactants through intermediates to products, with a rate-limiting step and an overall barrier that should match measured kinetics. This prompt applies the AI-scientist loop to mechanism inference: automatically *discover* the network rather than assume it. The loop closes on-machine because each proposed elementary step is *checkable*: a transition-state search locates a first-order saddle, a frequency analysis confirms **exactly one imaginary mode**, and an **intrinsic-reaction-coordinate (IRC)** trace confirms it connects the intended two minima. That TS$+$IRC$+$frequency test is the **on-machine verifier** - a step is admitted only when it passes, so the discovered network is proof-carrying edge by edge. Reaction-network exploration (AFIR/GSM-style automated search, KinBot, YARP) proposes steps; the verifier certifies them; a bounded, enumerable search space gives a *checkable completeness criterion*. The honesty is twofold: the verifier is DFT (level-relative energetics) and "completeness" is only relative to the defined space and sampler, never "all chemistry". Anything short of the section-2 standard - a plausible network with unverified edges, or "completeness" over an undefined space - is a partial result, never a discovered mechanism.

## 1. Exact problem statement

**System.** A chemical system is a set of reactant species plus fixed conditions and a fixed electronic-structure level:

- functional $+$ basis, and a solvation model or gas phase - committed up front;
- minima and saddles are computed at that level.

**Elementary step.** A unimolecular or bimolecular transformation $R \leftrightarrow P$ via a single first-order saddle. A step is **verified** iff:

- the Hessian at the saddle has **exactly one negative eigenvalue** (one imaginary frequency, within a stated $|\nu|$ window); and
- forward/backward **IRC** relaxes to minima matching $R$ and $P$ by connectivity/RMSD tolerance.

An unverified proposed step (barrierless, multiple imaginary modes, or IRC connecting the wrong minima) is rejected and logged.

**Reaction network.** A graph whose:

- nodes are minima (species/intermediates, conformers optionally lumped by a stated rule);
- edges are *verified* elementary steps, each labelled with a converged barrier and reaction energy at the fixed level.

**Mechanism.** A subnetwork of verified steps connecting designated reactants to designated products, with a rate-limiting step identified (via the Kozuch–Shaik energetic-span model) and an overall effective barrier.

**Completeness criterion (bounded space).** The search space is defined by explicit bounds so the candidate set is *finite and enumerable*:

- a maximum number of heavy atoms;
- at most $k$ bonds broken/formed per step;
- stated element/valence/coordination rules.

Completeness over this space means every candidate step up to the bound was generated and either verified (saddle found and IRC-confirmed) or excluded with a reason (no saddle at the level, or IRC connects outside the space). Completeness is asserted only relative to $(\text{level}, k, \text{atom/element bounds}, \text{sampler})$.

**Targets.** For a system:

- produce a verified mechanism (every reported step passing the TS$+$IRC$+$frequency test) connecting reactants to products;
- identify the rate-limiting step with a certified barrier;
- for the strong targets, a completeness-certified network over an explicitly bounded space.

**Accuracy threshold.** Exact on the verifier: every reported step passes the one-imaginary-frequency and IRC-endpoint tests; every barrier is converged with a stated tolerance at the fixed level. Kinetic comparison (overall barrier vs experimental $\Delta G^{\ddagger}$ from a measured rate via Eyring) is reported as a bias check, not as the acceptance test.

## 2. Resolution standard

Full resolution is an automated pipeline that, for a committed system and bounded space, discovers a reaction network whose every edge is TS$+$IRC$+$frequency-verified, identifies the rate-limiting step with a certified barrier, and - for the strong claim - certifies completeness over the defined space, with every step object re-checkable by a standalone verifier written separately from the explorer. Where a mechanistic conclusion is drawn (rate-limiting step, dominant pathway), it is supported by the energetic-span computation over the verified network, and its kinetic prediction is stated against experiment as a reality check.

**Not accepted as resolution:**

- A network with edges asserted from geometry or a learned score but not IRC-verified (the common silent failure - a "TS" that is not a saddle, or connects the wrong minima).
- "Completeness" claimed over an undefined or open-ended space, or asserted from a sampler with no enumeration bound.
- A mechanism recovered only because the search was seeded toward the known answer (confirmation bias); the explorer must report verified steps *not* in the assumed mechanism.
- A rate-limiting-step claim from uncertified or unconverged barriers, or from relative energies at a level too low to resolve the competing steps.
- A single-pathway result presented as *the* mechanism when competing verified pathways exist and were not compared.
- Level-relative energetics presented as experimental truth (see integrity clause).

**Benchmark-integrity clause.** The verifier's biases must be stated:

- **DFT level:** barriers and relative energies carry the functional's error ($\sim 1$–$4\,\text{kcal}\,\text{mol}^{-1}$), which can reorder competing steps; spot-check the rate-limiting region at a higher reference (DLPNO-CCSD(T)) where feasible.
- **Sampling completeness:** AFIR/GSM/KinBot may *miss* pathways; completeness is only over the enumerated bounded space, and the bound must be stated with every completeness claim.
- **Conformational and lumping choices** affect which minima and barriers appear.

The guard against teaching-to-the-test: reproduce a mechanism with an *independently established consensus* (experimental kinetics plus prior computation), check that the discovered rate-limiting step and overall barrier match the known kinetics, and explicitly report discovered steps absent from the consensus (as either new candidates or artifacts). A plausible-looking network with unverified edges, or a completeness claim over an undefined space, is confident-but-wrong and must be flagged.

## 3. Graded partial-result targets

- **P1 (verified pipeline reproduces a known mechanism's TS network).** For a well-studied mechanism (a textbook organic sequence or a small catalytic cycle), reproduce its elementary-step network with the pipeline, every step IRC-verified and energetics matching published values within DFT uncertainty. *Certificate:* per-step TS/IRC logs + the energy diagram versus the published one.
- **P2 (certified elementary-step verification).** For a proposed step of a target reaction, produce a fully certified step object: a saddle with exactly one imaginary frequency, IRC endpoints matching the intended minima, and a converged barrier. *Certificate:* the audited step object, reproducible from a manifest.
- **P3 (automated network discovery with a completeness criterion).** Over an explicitly bounded space, run automated exploration (AFIR/GSM/KinBot) and verify every generated step; certify that all candidate steps up to the bound $k$ were enumerated and resolved (verified or excluded with reason). *Certificate:* the enumeration log + per-step verification + the completeness argument relative to the stated bounds, independently replayable.
- **P4 (rate-limiting step with certified barriers).** From the verified network, identify the rate-limiting step via the energetic-span model with certified barriers and stated error bars; compare the predicted rate to experiment. *Certificate:* the energetic-span computation + the barrier certificates + the kinetic comparison.
- **P5 (strongest, reality-flagged).** A discovered pathway containing a verified step *not* in the prior consensus mechanism, fully certified and kinetically consistent - a genuine mechanistic candidate (its biological/chemical truth reality-gated by experiment; flag). *Certificate:* the full verified network + the novel step's certificate + the kinetic prediction, with the reality-gate caveat stated.

Full resolution (P3 completeness plus a P5 novel-yet-consistent step for a real system) is unlikely in one session; P1–P2 are realistic, P3–P4 are the target, P5 is the stretch.

## 4. Known results and prior art

- Maeda & Morokuma ~2010–2011 - Artificial Force Induced Reaction (AFIR) and the GRRM automated reaction-space search program.
- Zimmerman ~2013–2015 - the Growing String Method, ZStruct/pyGSM, single- and double-ended TS finding for automated exploration.
- Gao, Allen, Green, West 2016 - RMG (Reaction Mechanism Generator), rule-based network generation for kinetics.
- Van de Vijver & Zádor ~2019–2020 - KinBot, automated TS search and network exploration for gas-phase kinetics.
- Zhao & Savoie ~2021–2022 - YARP (Yet Another Reaction Program), systematic elementary-step enumeration and verification.
- Reiher group (Unsleber, Grimmel, Reiher) 2022 - Chemoton 2.0 / SCINE, autonomous reaction-network exploration with verification; Bergeler, Simm, Proppe, Reiher 2015 - heuristics-guided exploration.
- Kozuch & Shaik 2011 - the energetic-span model for turnover frequency and rate-limiting-step identification from a computed cycle.
- Young, Silcock, Sterling, Duarte 2021 - autodE, automated reaction profiles with TS verification; Hermes, Sargsyan, Najm, Zádor 2022 - Sella, saddle-point optimization.
- Dewyer, Argüelles, Zimmerman 2018 - review of methods for exploring reaction space (verify).
- Grambow, Pattanaik, Green 2020 - computed elementary-reaction dataset (context for data-driven step proposal).

Automated mechanism discovery is an active frontier: the tools exist, but a pipeline with *edge-by-edge certification* and a *defensible completeness criterion* over a bounded space is not a settled capability. **Status as of mid-2026 - re-verify against current literature before starting any session.**

## 5. Attack plan

**[algo] Verifier and step proposal.** autodE and Sella locate and refine saddles; PySCF or ORCA is the electronic-structure engine; every candidate saddle passes the one-imaginary-frequency test and an IRC that must connect the intended minima before the step is admitted. Step *proposals* come from automated exploration - AFIR (via GRRM), GSM/pyGSM double-ended searches between enumerated minima, or KinBot/YARP enumeration under the bond-change bound $k$. Proposals are untrusted until the verifier certifies them.

**[sym] Network assembly and completeness.** Assemble verified edges into a network; enumerate candidate steps up to $k$ bond changes over the bounded atom/element space so the candidate set is finite; track which candidates were resolved to make the completeness statement checkable. Kozuch–Shaik energetic span over the verified network yields the rate-limiting step and overall barrier.

**One-workstation scope.** Small systems ($\lesssim 30$–$40$ atoms) are feasible on a single multicore workstation (ORCA/PySCF CPU-parallel; no GPU required); network exploration is many TS searches and is embarrassingly parallel, so a modest network is a multi-day campaign. **Failure modes:** TS-search non-convergence or spurious saddles (two or more imaginary modes); IRC failing to converge or connecting minima outside the intended pair; conformer explosion inflating the node set; combinatorial growth of the candidate-step set (contained by the bound $k$); DFT error reordering competing steps (guarded by higher-level spot-checks); and sampler-driven incompleteness (guarded by the explicit enumeration bound and reported honestly).

## 6. Verification and auditability requirements

1. **Certified per-step numerics.** Every reported step passes the one-imaginary-frequency test and an IRC-endpoint match, with converged energies at a stated tolerance; completeness claims name the bounded space $(\text{level}, k, \text{atom/element bounds}, \text{sampler})$ they are relative to; floating-point exploration never counts as certification.
2. **Independent verification.** The TS$+$IRC$+$frequency checker is written separately from the explorer that proposed the geometry; headline barriers are recomputed by a standalone run; the energetic-span analysis is re-checkable.
3. **Reproducibility.** Electronic-structure level, autodE/Sella/PySCF/ORCA and explorer versions, TS/IRC criteria, the space bounds, conformer/lumping rules, seeds, and manifests are recorded; a SHA-256 manifest covers every minimum, saddle, Hessian, and IRC.
4. **Preservation.** Exploration logs (including failed and excluded steps), all step objects, and the network are part of the record; discarded candidates are listed as discarded with their exclusion reason.
5. **Honest reporting.** The report states the DFT level and the completeness bound up front, distinguishes verified edges from proposed-but-unverified ones, reports discovered steps absent from any assumed mechanism, gives the kinetic comparison to experiment as a bias check, and never presents a plausible network or a bounded-space completeness claim as *the* proven mechanism.
