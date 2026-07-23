# PROMPT TEMPLATE A - closed-loop problems (Pack A)

For problems where **the machine verifies its own answer without leaving the machine**: a proof, a CAS identity, a physics simulation (QM / MD / GCMC) the AI runs, or synthetic data with a known answer. These carry a genuine *resolution* standard. Each Pack A attempt subfolder contains a `prompt.md` following this structure. Sections may grow, none may be dropped.

---

# PROMPT FOR <TARGET RESULT OR OBJECT>

## <One-line subtitle naming the problem>

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** A - closed-loop (on-machine verifier)
**Rank:** A-NN of 21
**Source:** chem/bio top-50 list #K, section <A-G, name>
**Modes:** `[func]` `[gen]` `[sym]` `[algo]` `[cert]` `[struct]` `[data]` *(keep only the applicable tags)*

### Abstract

One paragraph: the problem, its utility (or adjacent utility), and why it is matched to current AI methods (learned functionals/potentials, generative search, symbolic regression, certified computation). Name the **on-machine verifier** explicitly: the simulation, proof, or exact reference that closes the loop. State that anything short of the section-2 standard is reported as a partial result, never as a solution.

## 1. Exact problem statement

Full definitions and the precise statement of the target. Fix notation, units, reference method, accuracy threshold, and admissible class. If several formulations circulate, adopt one and justify it. No informal phrasing ("chemical accuracy", "good enough") is an acceptable target without a numeric definition.

## 2. Resolution standard

The exact object(s) to produce and the verification each must pass. Include the numeric accuracy threshold and the reference against which it is judged. Then a list titled **Not accepted as resolution**: the weakened, benchmark-overfit, narrow-domain, or single-system claims that must not be represented as solving the problem.

**Benchmark-integrity clause:** if the verifier is a frozen or computed benchmark, state the known biases and the held-out / prospective test that guards against teaching-to-the-test. A benchmark win with a biased verifier is confident-but-wrong; flag it as such.

## 3. Graded partial-result targets

Ordered milestones P1, P2, … from "reproduce the known frontier with our own verified toolchain" up to "strongest result short of full resolution". Each carries its own certificate standard (what artifact proves it; how it is independently checked). These are the realistic product of a session.

## 4. Known results and prior art

Best current methods, accuracies, and datasets, with named references (authors and approximate year where confident; never fabricated arXiv IDs, DOIs, or page numbers; mark uncertain items "(verify)"). **Status as of mid-2026 - re-verify against current literature before starting any session.**

## 5. Attack plan

Concrete first computations per mode tag: the reference calculations, the model architecture or search encoding, the certified-verification step. Name actual tools (PySCF, ORCA, Psi4, VASP/Quantum ESPRESSO, PSI, OpenMM/GROMACS, PLUMED, RASPA, MACE/NequIP, DeepChem, Arb/FLINT, SDP solvers, Lean 4). State what runs on a single workstation / one prosumer GPU, and the expected failure modes.

## 6. Verification and auditability requirements

1. **Exact or certified numerics** for any claim that depends on it (rational/interval arithmetic, converged-simulation error bars, held-out test protocol); floating-point exploration never counts as certification.
2. **Independent verification:** a standalone checker written separately from the training/search code; where warranted, a second implementation.
3. **Reproducibility:** all inputs, seeds, hyperparameters, dataset splits, and environment recorded; SHA-256 manifest over every artifact; frozen train/test splits committed before evaluation.
4. **Preservation:** training and search code is part of the record. Anything not preserved is stated explicitly.
5. **Honest reporting:** the report states up front whether the resolution standard was met, reports the held-out/prospective metric (not just the tuned one), and never dresses a benchmark or single-system result as the full solution.
