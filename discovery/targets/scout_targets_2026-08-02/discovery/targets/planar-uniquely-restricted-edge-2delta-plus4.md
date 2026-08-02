---
id: planar-uniquely-restricted-edge-2delta-plus4
result_class: B2
statement: >-
  For every finite simple planar graph G of maximum degree Delta, the uniquely restricted edge chromatic number satisfies chi'_ur(G)<=2*Delta+4. A color class must be a uniquely restricted matching: the subgraph induced by its endpoints has that matching as its unique perfect matching.
source:
  primary_locator: >-
    Yuquan Lin and Wensong Lin, “Semistrong edge colorings of planar graphs,” arXiv:2412.19230v2 / Journal of Combinatorial Optimization 50 (2025), Conjecture 7.1, page 22, https://arxiv.org/pdf/2412.19230 and https://doi.org/10.1007/s10878-025-01346-8.
  access_date: 2026-08-02
  status_evidence: >-
    Exact-title, DOI, authors, “Conjecture 7.1,” and uniquely-restricted edge-coloring follow-up searches on 2026-08-02 found no resolution.
baseline:
  current_value_or_range: >-
    The paper proves planar semistrong/uniquely-restricted edge-coloring bounds and poses 2Delta+4 as Conjecture 7.1. The scout script validates planarity and a supplied coloring only; it does not certify that <=2Delta+4 colors are impossible. No source-scale baseline was replayed.
  replay_command: >-
    python checkers/check_planar_ur_edge.py fixtures/planar_p4_valid.json
witness:
  format: >-
    A refutation artifact must contain a planar graph6/edge list, Delta, an edge coloring using >2Delta+4 colors, and a SAT/DRAT proof that no uniquely restricted edge coloring with <=2Delta+4 colors exists.
  checker_command: >-
    python checkers/check_planar_ur_edge.py fixtures/planar_p4_valid.json
  checker_hash: sha256:d358ffb1fb102d292f69c5944ead62b93234bac5fcc681e8889d4a8e01297aff
  calibration_cases: >-
    known-positive coloring: P4 valid fixture; adversarial negative coloring: P4 invalid fixture; malformed: fixtures/malformed.json; frontier: no lower-bound/UNSAT proof checker is bundled.
search_edge: >-
  Generate only planar edge-coloring-critical graphs, encode conflicts as a hypergraph over alternating cycles, and use incremental SAT with DRAT proof logging. The required missing piece is an independently checkable lower-bound certificate; until it exists and is benchmarked, this is not ready.
budget:
  model: "GPT-5.6 Pro plus planar generation and proof-logging SAT"
  wall_clock: "24 h"
  cpu_gpu: "32 CPU cores"
  memory: "128 GB"
stop_rules: >-
  Stop immediately if the statement/status changes or the baseline cannot be replayed. Freeze on disagreement between two independent implementations. Require a method review after 20% of budget without new structural information; pause after a repeated plateau with no new representation; kill if measured growth exceeds the forecast by 4x. No attack before an end-to-end DRAT-verifying checker and reproduction of a nontrivial published lower-bound instance.
publication_path: >-
  Yuquan Lin and Wensong Lin; Journal of Combinatorial Optimization / edge-coloring community.
aliases: ["ur-edge-planar-conjecture-7-1", "planar-ur-index-bound"]
---

# planar-uniquely-restricted-edge-2delta-plus4

**Admission label:** `needs-edge`  
**Gate count:** 6/9 green  
**Scout rank:** 16 of 17 (ordinal judgment; no score total)

## Admission gates

| # | Gate | State | Evidence |
|---:|---|:---:|---|
| 1 | Statement pinned | GREEN | Domain, invariant, and bound pinned. |
| 2 | Primary source pinned | GREEN | Paper, DOI, page, and conjecture number pinned. |
| 3 | Open status fresh | GREEN | Fresh searches found no resolution. |
| 4 | Artifact grammar fixed | GREEN | Graph/coloring/UNSAT-certificate grammar is specified. |
| 5 | Checker exists and calibrated | RED | Red: current script checks only upper certificates, not the crucial noncolorability proof. |
| 6 | Baseline reproduces | RED | No source frontier replayed. |
| 7 | Search edge stated | RED | Critical-generation/SAT idea is concrete but lacks a certified benchmark. |
| 8 | Budget and stop rule fixed | GREEN | Budget and checker-first stop rule fixed. |
| 9 | Scientific path named | GREEN | Authors and venue named. |

## Priority vector

`[4, 2, 4, 3, 4, 2, 3, 1]` in the fixed order: open-status confidence, reachability, method advantage, witness/lemma plausibility, scientific value, verification quality, competition penalty, end-to-end cost.

| Dimension | Score | Evidence |
|---|:---:|---|
| open-status confidence | 4 | No resolution found; source about 20 months old. |
| reachability | 2 | Planar critical graph search plus edge-coloring lower bounds is difficult. |
| method advantage | 4 | Alternating-cycle SAT structure is promising. |
| witness/lemma plausibility | 3 | Finite counterexample, but proving chromatic lower bound is heavy. |
| scientific value | 4 | Would improve planar edge-coloring theory. |
| verification quality | 2 | Currently weak because no lower-bound proof checker. |
| competition penalty | 3 | Moderate specialist attention. |
| end-to-end cost | 1 | Highest end-to-end engineering cost in the graph set. |

## Scout notes

A coloring with many colors is not a counterexample; the lower bound chi'_ur>2Delta+4 is the essential certificate.

## Deep-attack admission consequence

Do not allocate deep compute. Build and benchmark the stated search edge and reproduce the source baseline; where gate 5 is red, finish the independent checker before any generation/search.
