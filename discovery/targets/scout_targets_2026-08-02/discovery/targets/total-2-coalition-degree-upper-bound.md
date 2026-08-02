---
id: total-2-coalition-degree-upper-bound
result_class: B2
statement: >-
  For every finite simple graph G with minimum degree delta>=2 and maximum degree Delta, the total 2-coalition number satisfies TC_2(G) <= floor(delta/2)*(Delta-2*floor(delta/2)+1)+ceil(delta/2).
source:
  primary_locator: >-
    Boštjan Brešar, Sandi Klavžar, and Babak Samadi, “Total k-coalition: bounds, exact values and an application to double coalition,” arXiv:2502.07310v1 / DMTCS 27:3 (2025), Conjecture 1, https://arxiv.org/html/2502.07310v1#S4.
  access_date: 2026-08-02
  status_evidence: >-
    Exact-title, formula, author, and citation/follow-up searches on 2026-08-02 found no resolution. The paper is about 18 months old and no maintainer/author confirmation or complete citation graph was obtained, so openness is not promoted to green.
baseline:
  current_value_or_range: >-
    The paper proves the conjectured bound for delta<=5 and when Delta>=4*floor(delta/2)-2, and gives sharp families. The scout checker validates a supplied coalition partition; K5 attains the bound with four parts. The full proved regimes were not independently replayed.
  replay_command: >-
    python checkers/check_total2coalition.py fixtures/total2_k5_equality.json
witness:
  format: >-
    JSON graph plus a set partition of V(G); each part must fail to be a total 2-dominating set and must have a partner part whose union is total 2-dominating.
  checker_command: >-
    python checkers/check_total2coalition.py fixtures/total2_k5_equality.json
  checker_hash: sha256:cd7d7a29bcd202f6c7f3703c616db619cab7f70a83af801c200f8924d1e239ae
  calibration_cases: >-
    known-positive/equality: K5 four-part partition; adversarial negative: five singleton parts in fixtures/total2_k5_invalid_singletons.json; malformed: fixtures/malformed.json; frontier: proved delta/Delta regimes not replayed.
search_edge: >-
  Encode the partition and partner graph jointly in CP-SAT, compress true/false twin classes, and target only the residual strip delta>=6 and Delta<4*floor(delta/2)-2. This avoids all regimes already proved and turns the existential partner relation into a sparse auxiliary graph.
budget:
  model: "GPT-5.6 Pro plus CP-SAT/nauty"
  wall_clock: "20 h"
  cpu_gpu: "24 CPU cores"
  memory: "64 GB"
stop_rules: >-
  Stop immediately if the statement/status changes or the baseline cannot be replayed. Freeze on disagreement between two independent implementations. Require a method review after 20% of budget without new structural information; pause after a repeated plateau with no new representation; kill if measured growth exceeds the forecast by 4x. Do not attack until an author or recent citation audit confirms the conjecture is still open; then require CP-SAT to reproduce sharp examples first.
publication_path: >-
  Boštjan Brešar, Sandi Klavžar, and Babak Samadi; DMTCS or domination/coalition graph theory community.
aliases: ["tc2-degree-bound", "bresar-klavzar-samadi-conjecture-1"]
---

# total-2-coalition-degree-upper-bound

**Admission label:** `needs-status`  
**Gate count:** 7/9 green  
**Scout rank:** 4 of 17 (ordinal judgment; no score total)

## Admission gates

| # | Gate | State | Evidence |
|---:|---|:---:|---|
| 1 | Statement pinned | GREEN | Exact formula and graph domain pinned. |
| 2 | Primary source pinned | GREEN | Primary arXiv/journal locator pinned. |
| 3 | Open status fresh | RED | No resolution found, but 18-month gap lacks author/maintainer confirmation. |
| 4 | Artifact grammar fixed | GREEN | Graph plus partition/partner semantics fixed. |
| 5 | Checker exists and calibrated | GREEN | Independent certificate checker passes equality and invalid cases. |
| 6 | Baseline reproduces | RED | Published proved regimes and sharp-family baseline not fully replayed. |
| 7 | Search edge stated | GREEN | Residual-strip CP-SAT with twin compression is concrete and excludes proved regions. |
| 8 | Budget and stop rule fixed | GREEN | Budget and status-first stop rule fixed. |
| 9 | Scientific path named | GREEN | Authors and venue named. |

## Priority vector

`[3, 4, 5, 4, 3, 5, 5, 4]` in the fixed order: open-status confidence, reachability, method advantage, witness/lemma plausibility, scientific value, verification quality, competition penalty, end-to-end cost.

| Dimension | Score | Evidence |
|---|:---:|---|
| open-status confidence | 3 | Search-negative status only; source is no longer fresh. |
| reachability | 4 | Theorems leave a narrow parameter strip and certificates are small. |
| method advantage | 5 | Residual targeting and partner-graph encoding are strong. |
| witness/lemma plausibility | 4 | A violating graph plus partition is finite and exact. |
| scientific value | 3 | Meaningful within coalition theory, specialized outside it. |
| verification quality | 5 | Certificate checking is combinatorial and independent. |
| competition penalty | 5 | Low visible traffic. |
| end-to-end cost | 4 | Moderate CP-SAT cost. |

## Scout notes

Primary blocker is status, not computation.

## Deep-attack admission consequence

Do not allocate deep compute. Resolve every red status/statement gate first; a negative web search alone is insufficient where author clarification or an older citation graph is missing.
