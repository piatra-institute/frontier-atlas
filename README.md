# Frontier Atlas

**200 open problems across four domains - physics, mathematics, informatics, chembiotics**

A monorepo of well-posed, unsolved problems in theoretical physics, mathematics, theoretical computer science, and computational chemistry/biology. Each is selected because a frontier AI reasoning system, a single workstation, and disciplined verification can plausibly produce a certified partial result. The filter is tractable-but-nontrivial, with machine-checkable ground truth. No quantum-gravity or Millennium-headline flagships.

Each numbered problem folder is one issue: a self-contained task holding a `README.md` and one or more numbered attempt subfolders (`01_baseline/`, `02_.../`), each with its own `prompt.md` and every artifact generated from it. A task holds multiple attempts, not a single shot.

## The four programs

| Program | Problems | Character |
|---|---|---|
| [`physics/`](physics/README.md) | 50 | Quantum information, rigorous many-body, exactly-solvable models, dynamical systems, fluids/plasmas, QFT, gravitation. Certified/SAT search, symbolic mining, computer-assisted proof, bound optimization. |
| [`mathematics/`](mathematics/README.md) | 50 | Combinatorics, discrete geometry, number theory, algebra. SAT-provable bounds, exact enumeration, symbolic mining. Problems 01-11 carry full worked packages; 12-50 are ready prompts. |
| [`informatics/`](informatics/README.md) | 50 | Theoretical computer science: algorithms & bilinear complexity, Boolean/cryptographic functions, complexity separations, computation models & automated reasoning, discrete dynamics, quantum computation & codes. SAT, exact search, machine-checked proof. |
| [`chembiotics/`](chembiotics/README.md) | 50 | Learned functionals, free-energy sampling, structure/ensemble prediction, generative design, genomics. Split by **where the verifier lives**: Pack A (on-machine, closed-loop) vs Pack B (empirical / wet-lab-gated). |

Each program has a `README.md` (full index of all 50) and `STRATEGY.md` (ranking and doctrine). Chembiotics adds `STATUS_AUDIT_2026-07.md`, a dated audit of which problems' SOTA baselines have moved.

## Shared doctrine

Each `STRATEGY.md` details this; in brief:

- **Intelligence-rich, resource-poor.** Pick problems where reasoning plus a workstation plus verification beats brute force.
- **Certified partial results are the product.** Every session ends with something independently checkable: a bound with a proof trace, an exact reduction, an obstruction certificate, a verified construction, or a leakage-safe held-out result. Full resolutions are windfalls.
- **Distrust the verifier; re-verify before every session.** Open-problem status drifts monthly. Prompts state prior art "as of mid-2026"; treat it as stale until re-checked.
- **Everything is auditable.** Exact or certified computation for any load-bearing claim, independent replay checkers, SHA-256 manifests, preserved search/training source.
- **Honest reporting.** Reports state up front whether the standard was met; a partial or numerical result is never dressed as a full solution, and an in-silico prediction is never dressed as a proof.

## Anatomy of an issue

A task folder (`NN_slug/`) holds a `README.md` (title, one-liner, attempts table) plus one or more attempt subfolders (`01_baseline/`, `02_.../`). Each attempt subfolder contains:

- `prompt.md` - the task definition: exact statement, resolution (or genuine-advance) standard with a "not accepted" list, graded certifiable targets, prior art with `(verify)` flags, an attack plan naming real tools, and auditability requirements. Physics, maths, and informatics use one closed-loop template; chembiotics uses template A or B by verifier regime. The maths originals 01-11 keep their pre-template prompt documents inside `01_baseline`.
- Once worked: `chat.md` (transcript), scripts, and a research package - report (md/pdf), source, certificates, independent verifiers, SHA-256 manifest. A paused line leaves a `NEXT_STEPS.md`. A new approach becomes a new attempt subfolder (`02_...`, `03_...`).

## Working protocol

Every session runs under the atlas `SOLVER.md` (agency, compute, adversarial self-verification).
1. **Pick** a problem (each program's README flags the strongest machine-checkable starting points).
2. **Re-verify** its current status in the literature first.
3. **Seed** a frontier-model session with the attempt's `prompt.md`.
4. **Preserve** the transcript as `chat.md`.
5. **Produce** a self-contained, auditable package; keep the search/training source.
6. **Report** honestly whether the standard was met.
7. **Leave** a `NEXT_STEPS.md` when pausing a line.

## Layout

```
frontier-atlas/
├── README.md            ← this file
├── .gitignore
├── physics/             README + STRATEGY + PROMPT_TEMPLATE + 50 task folders
├── mathematics/         README + STRATEGY + PROMPT_TEMPLATE + 50 task folders
├── informatics/         README + STRATEGY + PROMPT_TEMPLATE + 50 task folders
└── chembiotics/         README + STRATEGY + two templates + STATUS_AUDIT + 50 task folders
```

Each task folder holds a `README.md` plus numbered attempt subfolders:

```
physics/01_kochen_specker_minimal/
├── README.md            ← task overview + attempts table
└── 01_baseline/
    ├── prompt.md
    └── (chat, scripts, certificates, package … as the attempt is worked)
```
