# PROMPT TEMPLATE B - reality-gated problems (Pack B)

For problems where **the real verifier is empirical measurement**: a wet-lab assay, or a frozen experimental corpus that is itself the bottleneck. These cannot be *resolved* by compute alone; the deliverable is an advance: a certified method contribution, a benchmark result on a held-out split, and falsifiable prospective predictions for a wet-lab partner to test. The wet lab, not the machine, closes the loop. Each Pack B attempt subfolder contains a `prompt.md` following this structure. Sections may grow, none may be dropped.

---

# PROMPT FOR <TARGET PREDICTION / DESIGN / METHOD>

## <One-line subtitle naming the problem>

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** B - reality-gated (empirical verifier)
**Rank:** B-NN of 29
**Source:** chem/bio top-50 list #K, section <A-G, name>
**Modes:** `[struct]` `[gen]` `[data]` `[func]` `[algo]` `[sym]` *(keep only the applicable tags)*

### Abstract

One paragraph: the problem, its utility, and why current AI methods (AlphaFold-lineage, diffusion generators, sequence models) can *advance* but not *close* it. State plainly that this is reality-gated: the ground truth is empirical, so the target is a certified advance plus falsifiable predictions, never a claimed resolution.

## 1. Exact problem statement

Full definitions and the precise prediction/design/method target. Fix the input, the output, the metric, and the population over which performance is claimed. Distinguish the compute-tractable sub-question from the empirically-gated whole.

## 2. Verifier and data

State:
- **Ground-truth source:** the assay or frozen corpus that defines correctness (name the databases: e.g. ProteinGym, ClinVar/gnomAD, MaveDB, PDB, SKEMPI, Hi-C/MPRA atlases, etc. - "(verify)" any you are not certain exists).
- **Frozen split:** the held-out or temporally-split test set fixed *before* modeling, and why it resists leakage (homology/cluster separation, time-split).
- **Wet-lab gate:** exactly which claims cannot be established without new physical experiments, and roughly what those experiments cost. This line is mandatory and must not be softened.

## 3. Standard of a genuine advance

What counts as a real contribution here, and - titled **Not accepted as resolution** - the claims that must not be dressed as solving the problem (a leaderboard number as a real-world guarantee; a design "validated" only in silico; a corpus-overfit metric).

## 4. Graded targets

Ordered milestones P1, P2, … from "reproduce the SOTA baseline on the frozen split with our own verified pipeline" through "certified method contribution or new held-out SOTA" up to "a ranked, falsifiable prediction/design set ready to hand to a wet-lab partner, with calibrated uncertainties." Each carries its evidence standard.

## 5. Known results and prior art

Best current models, benchmark numbers, and datasets, with named references (authors and approximate year where confident; never fabricated arXiv IDs, DOIs, or page numbers; mark uncertain items "(verify)"). **Status as of mid-2026 - re-verify against current literature before starting any session.**

## 6. Attack plan

Concrete first steps: which frozen dataset to pull, the leakage-safe split protocol, the baseline to reproduce, the model/architecture, and how uncertainty is calibrated. Name actual tools (PyTorch, AlphaFold/OpenFold/Boltz, RFdiffusion/ProteinMPNN, ESM, Enformer, RDKit, DeepChem). State what runs on one prosumer GPU and the expected failure modes (data scarcity, distribution shift, label noise).

## 7. Verification and auditability requirements

1. **Leakage-safe evaluation:** frozen train/test split committed before any evaluation; homology/time separation documented; no test-set tuning.
2. **Calibrated uncertainty:** every prospective prediction carries a calibrated confidence; calibration is itself reported on held-out data.
3. **Independent reproduction:** metrics reproducible from committed splits and code by a separate script; SHA-256 manifest over data hashes, code, and predictions.
4. **Preservation:** training/generation code and dataset version hashes are part of the record. Anything not preserved is stated explicitly.
5. **Honest reporting:** the report states up front that the problem is reality-gated and NOT resolved; separates in-silico metrics from any experimental validation; labels every design or prediction as a hypothesis pending wet-lab test; and never represents a benchmark result as a real-world guarantee.
