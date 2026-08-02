---
id: zero-forcing-polynomial-path-extremal
result_class: B2
statement: >-
  For every finite simple graph G on n vertices and every integer k with 0<=k<=n, z(G;k)<=z(P_n;k), where z(G;k) is the number of k-element zero-forcing sets of G and P_n is the n-vertex path.
source:
  primary_locator: >-
    Samuel German, “The Path-Extremal Conjecture for Zero Forcing: Distance-Hereditary Graphs and a Split-Decomposition Reduction,” arXiv:2605.10836, main conjecture in abstract/introduction, https://arxiv.org/abs/2605.10836.
  access_date: 2026-08-02
  status_evidence: >-
    Exact-title, arXiv-ID, author, and “Path-Extremal Conjecture” follow-up searches on 2026-08-02 found no resolution. The paper proves the distance-hereditary case and reduces the general problem to prime split-decomposition bags.
baseline:
  current_value_or_range: >-
    The source proves the conjecture for distance-hereditary graphs and supplies a split-decomposition reduction. The local exact subset checker gives z(P6;2)=12 and z(C6;2)=6. The theorem-scale baseline and implementation were not independently replayed.
  replay_command: >-
    python checkers/check_path_zero_forcing.py fixtures/path_p6_k2.json && python checkers/check_path_zero_forcing.py fixtures/path_c6_k2.json
witness:
  format: >-
    Canonical graph6/JSON graph plus k; checker enumerates k-subsets and performs deterministic zero-forcing closure.
  checker_command: >-
    python checkers/check_path_zero_forcing.py fixtures/path_p6_k2.json
  checker_hash: sha256:4478a54f648372cd361e5f23e5d4f27d05e6581cf61c574584c57ad56a9f73a7
  calibration_cases: >-
    known-positive/equality: P6,k=2; strict near-miss: C6,k=2; malformed: fixtures/malformed.json; frontier: distance-hereditary theorem not replayed.
search_edge: >-
  Enumerate only prime split-decomposition cores, cache zero-forcing closures by fort signatures, and lift through decomposition with a boundary-state dynamic program. This follows the source reduction but adds an explicit finite-state representation; no benchmark yet demonstrates a new order or class.
budget:
  model: "GPT-5.6 Pro plus nauty and boundary-state DP"
  wall_clock: "24 h"
  cpu_gpu: "32 CPU cores"
  memory: "96 GB"
stop_rules: >-
  Stop immediately if the statement/status changes or the baseline cannot be replayed. Freeze on disagreement between two independent implementations. Require a method review after 20% of budget without new structural information; pause after a repeated plateau with no new representation; kill if measured growth exceeds the forecast by 4x. Require independent reproduction of the distance-hereditary theorem on a finite corpus and measurable compression on prime bags.
publication_path: >-
  Samuel German and the zero-forcing polynomial community; author validation followed by graph polynomial / linear algebraic graph theory venue.
aliases: ["path-extremal-zero-forcing-polynomial", "zGk-path-conjecture"]
---

# zero-forcing-polynomial-path-extremal

**Admission label:** `needs-edge`  
**Gate count:** 7/9 green  
**Scout rank:** 13 of 17 (ordinal judgment; no score total)

## Admission gates

| # | Gate | State | Evidence |
|---:|---|:---:|---|
| 1 | Statement pinned | GREEN | Exact coefficientwise statement pinned. |
| 2 | Primary source pinned | GREEN | Recent arXiv source pinned. |
| 3 | Open status fresh | GREEN | Fresh title/status search found no resolution. |
| 4 | Artifact grammar fixed | GREEN | Graph+k grammar fixed. |
| 5 | Checker exists and calibrated | GREEN | Exact subset checker passes equality and strict cases. |
| 6 | Baseline reproduces | RED | Published theorem frontier not replayed. |
| 7 | Search edge stated | RED | Prime-bag boundary DP is plausible but unbenchmarked. |
| 8 | Budget and stop rule fixed | GREEN | Budget and preflight rules fixed. |
| 9 | Scientific path named | GREEN | Author/community named. |

## Priority vector

`[4, 3, 4, 4, 4, 5, 2, 3]` in the fixed order: open-status confidence, reachability, method advantage, witness/lemma plausibility, scientific value, verification quality, competition penalty, end-to-end cost.

| Dimension | Score | Evidence |
|---|:---:|---|
| open-status confidence | 4 | Recent explicit open conjecture. |
| reachability | 3 | Split reduction helps, but prime graphs remain large. |
| method advantage | 4 | Boundary-state DP is aligned with the new structural theorem. |
| witness/lemma plausibility | 4 | Counterexample is a finite graph and coefficient k. |
| scientific value | 4 | Would settle a natural graph-polynomial extremal claim. |
| verification quality | 5 | Exact enumeration offers clean verification. |
| competition penalty | 2 | Zero forcing is active and the path conjecture is visible. |
| end-to-end cost | 3 | Moderate/high implementation cost. |

## Scout notes

Do not spend compute rechecking distance-hereditary graphs; the source already proves them.

## Deep-attack admission consequence

Do not allocate deep compute. Build and benchmark the stated search edge and reproduce the source baseline; where gate 5 is red, finish the independent checker before any generation/search.
