# Frontier Atlas

**A verification-first workbench for AI-assisted attacks on open problems, plus a triaged bank of 200 candidate problems.**

The method: a frontier model (ChatGPT Pro, Claude) searches for a small explicit witness; a second, independent system checks it exactly. Generator is not verifier. Every result ships a `CLAIM.md`, an independent checker, a manifest, and an honest denominator.

## What is actually winnable (read this first)

The wins in this method are small explicit objects a checker validates in seconds: a counterexample to a conjecture, an existence witness, a found object, a strictly beaten *loose* record. They are not: analytic proofs, physical constants, hardened optimization records, or predictions needing a wet lab.

Measured against that, the 200 problems triage as follows (`TRIAGE.md`, from `tools/triage.py`):

| Tier | Shape | Count | On method? |
|---|---|---:|---|
| **T1** | witness-shaped (existence / counterexample / found object) | **38** | yes - the primary targets |
| **T2** | exact-value record (construction + matching lower bound) | 62 | long shot; only loose/obscure cells |
| **T3** | analytic proof or constant | 50 | no - out of scope for search-with-a-checker |
| **T4** | reality-gated (chembiotics; needs wet-lab / held-out data) | 50 | no - belongs in a separate empirical program |

Five deep attempts this session on T2 problems (cap set a(7), superpermutation s(6), bilinear rank, two covering-array numbers) produced clean *reproductions* and zero new records - the honest evidence that T2/T3/T4 do not win at session scale. Work T1, and treat the rest as a verification substrate and a reference bank.

## Two ways to work

1. **`discovery/` - the winnable atlas (192 tasks, the center of gravity).** 31 throughput pipelines (each sweeps a whole class of claims per session) plus 160 single-witness hunts (find one object, or refute one under-tested claim). NOTE (per `BREAKTHROUGH_STRATEGY.md`): these are mostly *topics*, not pinned experiments, and a cheap checker is an admission condition, not a tractability forecast - open, reachable, and valuable are three separate tests. The next step is not more prompts but scouted `TARGET_CARD`s (pinned statement, fresh open-status, named search edge). See [`discovery/README.md`](discovery/README.md) and [`TARGET_CARD_TEMPLATE.md`](TARGET_CARD_TEMPLATE.md).
2. **The 200 bank, T1 first.** Curated single problems where one witness settles it. See `TRIAGE.md` for the T1 list (Life objects, an open SRG or Steiner system, MOLS-10, APN dim 8, Casas-Alvero, and the physics quantum-information existence questions).

## The verification discipline (this is the durable value)

- **Generator is not the verifier.** The searcher (ChatGPT Pro) proposes; a second system (Claude Code) re-derives every load-bearing claim with its own code. Two independent systems, per `SOLVER.md`.
- **Ship the audit surface, not just the answer.** `CLAIM.md` states the exact proposition, the checker command with pinned versions, the trust base, the review level, and the denominator (attempts and total cost, not just the winning run). See `CLAIM_TEMPLATE.md`.
- **Re-verify first; the frontier drifts in days.** Prior art is stale until re-checked. `FRONTIER_LOG.md` tracks external results that resolve or sit adjacent to atlas problems.
- **Regenerate-only artifacts.** Git tracks source, checkers, reports, and SHA-256 manifests; bulky proof traces are regenerable and git-ignored (`ARTIFACTS.md`).
- **Honest reporting.** State whether the standard was met; never dress a reproduction as a discovery, a heuristic null as a proof, or an in-silico metric as a real-world result.

## The programs (the 200 bank)

| Program | Problems | T1 (winnable) |
|---|---|---:|
| [`physics/`](physics/README.md) | 50 | 8 (mostly quantum-information existence) |
| [`mathematics/`](mathematics/README.md) | 50 | 15 |
| [`informatics/`](informatics/README.md) | 50 | 15 |
| [`chembiotics/`](chembiotics/README.md) | 50 | 0 (all reality-gated) |

Each program has a `README.md` and `STRATEGY.md`. Chembiotics is reality-gated throughout and is a candidate to spin off.

## Layout

```
frontier-atlas/
├── README.md            ← this file
├── TRIAGE.md            all 200 tagged by winnability (from tools/triage.py)
├── triage.csv           the same, machine-readable
├── SOLVER.md            method layer every attempt runs under
├── FRONTIER_LOG.md      dated ledger of external results and rescopes
├── CLAIM_TEMPLATE.md    per-attempt claim + checker + trust base stub
├── TARGET_CARD_TEMPLATE.md  atomic unit: pinned statement + admission gates + scorecard
├── BREAKTHROUGH_STRATEGY.md deep critique + operating plan (funnel, gates, portfolio)
├── ARTIFACTS.md         what git tracks vs regenerates
├── .gitignore
├── tools/               triage.py (winnability tags) + audit.py (control-plane checks)
├── discovery/           192 winnable tasks: 31 pipelines + 160 witness hunts (see discovery/README.md)
├── physics/             README + STRATEGY + PROMPT_TEMPLATE + 50 task folders
├── mathematics/         README + STRATEGY + PROMPT_TEMPLATE + 50 task folders
├── informatics/         README + STRATEGY + PROMPT_TEMPLATE + 50 task folders
└── chembiotics/         README + STRATEGY + two templates + STATUS_AUDIT + 50 task folders
```

A worked task holds a `README.md` plus dated run subfolders, each with `prompt.md`, `chat.md`, `CLAIM.md`, source, certificates, and `SHA256SUMS`. See `mathematics/17_cap_set_n7` for a fully worked example.
