---
id: trianglefree-chi-zero-forcing-half-bound
result_class: B2
statement: >-
  For every finite simple triangle-free graph G, 2*chi(G) <= Z(G)+4, where chi is chromatic number and Z is the standard zero-forcing number; equivalently chi(G) <= Z(G)/2 + 2.
source:
  primary_locator: >-
    Dickson Y. B. Annor and Ben Howerton, “Induced Subgraph Bounds on the Zero Forcing Number and Chromatic Consequences,” arXiv:2607.20137v2, Conjecture 11, https://arxiv.org/html/2607.20137v2#S4.
  access_date: 2026-08-02
  status_evidence: >-
    Version 2 was posted/revised 2026-07-29. Exact-title, arXiv-ID, author, and formula searches on 2026-08-02 found no later resolution. Version 2 itself records and repairs a counterexample to a broader version-1 claim, while retaining this triangle-free conjecture.
baseline:
  current_value_or_range: >-
    The source reports exhaustive checking of all 1,144,061 connected triangle-free graphs on 12 vertices: 23 are 4-chromatic, with Z=5 for 16 and Z=6 for 7; no counterexample through order 12. The paper mentions ancillary code/shards/checksums, but that full corpus was not vendored or replayed in this scout package.
  replay_command: >-
    BLOCKED: obtain the authors’ ancillary n=12 shards, then run their documented replay; local calibration only: python checkers/check_trianglefree_chi_z.py fixtures/triangle_c5.json
witness:
  format: >-
    Canonical graph6 string, or JSON {"n":...,"edges":[[u,v],...]}; checker recomputes triangle-freeness, exact chi, and exact zero forcing.
  checker_command: >-
    python checkers/check_trianglefree_chi_z.py fixtures/triangle_c5.json
  checker_hash: sha256:c8eed733e9669bffa51fe7d1d27da9c267ea9a06fba3be88ff0f13bd543a70e3
  calibration_cases: >-
    known-positive/equality: C5 in fixtures/triangle_c5.json gives chi=3,Z=2; near-miss negative: C6 in fixtures/triangle_c6.json is strict; malformed: fixtures/malformed.json exits nonzero; frontier: authors’ n=12 corpus is not locally replayed.
search_edge: >-
  Generate only triangle-free k-critical graphs while co-optimizing for low zero-forcing number: canonical augmentation/nauty for criticality, SAT for colorability, and fort-based branch-and-bound for Z. This should avoid the overwhelming mass of irrelevant triangle-free graphs, but no benchmark yet shows it crosses the authors’ n=12 frontier.
budget:
  model: "GPT-5.6 Pro plus nauty/SAT/exact Z code"
  wall_clock: "24 h"
  cpu_gpu: "32 CPU cores"
  memory: "96 GB"
stop_rules: >-
  Stop immediately if the statement/status changes or the baseline cannot be replayed. Freeze on disagreement between two independent implementations. Require a method review after 20% of budget without new structural information; pause after a repeated plateau with no new representation; kill if measured growth exceeds the forecast by 4x. Before attack, require replay of the n=12 author corpus and a benchmark showing critical-graph generation reaches at least one order beyond it.
publication_path: >-
  Dickson Y. B. Annor and Ben Howerton; zero-forcing and graph-coloring venues, with the authors’ ancillary repository as the first validation path.
aliases: ["triangle-free-chi-vs-Z", "annor-howerton-conjecture-11"]
---

# trianglefree-chi-zero-forcing-half-bound

**Admission label:** `needs-edge`  
**Gate count:** 7/9 green  
**Scout rank:** 2 of 17 (ordinal judgment; no score total)

## Admission gates

| # | Gate | State | Evidence |
|---:|---|:---:|---|
| 1 | Statement pinned | GREEN | Conjecture 11 fixes domain, invariants, and inequality. |
| 2 | Primary source pinned | GREEN | arXiv v2 and section locator pinned. |
| 3 | Open status fresh | GREEN | Four-day-old version plus fresh searches; no later resolution found. |
| 4 | Artifact grammar fixed | GREEN | Graph6/edge-list grammar is fixed. |
| 5 | Checker exists and calibrated | GREEN | Independent exact small-graph checker passes equality and strict cases. |
| 6 | Baseline reproduces | RED | The claimed n=12 exhaustive frontier has not been independently replayed. |
| 7 | Search edge stated | RED | Critical/SAT/fort edge is plausible but not benchmarked beyond n=12. |
| 8 | Budget and stop rule fixed | GREEN | 24-hour resources and pre-attack benchmarks are frozen. |
| 9 | Scientific path named | GREEN | Authors and field venues named. |

## Priority vector

`[5, 3, 4, 4, 4, 5, 4, 3]` in the fixed order: open-status confidence, reachability, method advantage, witness/lemma plausibility, scientific value, verification quality, competition penalty, end-to-end cost.

| Dimension | Score | Evidence |
|---|:---:|---|
| open-status confidence | 5 | Very fresh explicit conjecture. |
| reachability | 3 | Critical graphs sharply reduce space, but exact Z is expensive. |
| method advantage | 4 | Joint criticality and fort search is more targeted than bulk enumeration. |
| witness/lemma plausibility | 4 | Counterexample is an ordinary finite graph with a definitive checker. |
| scientific value | 4 | Would connect two active graph invariants and correct a fresh program. |
| verification quality | 5 | Exact chi and Z can be independently recomputed. |
| competition penalty | 4 | Small-team source, though zero forcing has an active community. |
| end-to-end cost | 3 | Moderate implementation and enumeration cost. |

## Scout notes

Do not revive the broader version-1 inequality; version 2 already refutes it.

## Deep-attack admission consequence

Do not allocate deep compute. Build and benchmark the stated search edge and reproduce the source baseline; where gate 5 is red, finish the independent checker before any generation/search.
