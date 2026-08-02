---
id: arboreal-bunkbed-full-ladder
result_class: B2
statement: >-
  For every finite graph G, vertices u,v in V(G), and lambda>0, form the full bunkbed graph G_tilde with two copies of G and a vertical edge joining the two copies of every vertex. Under the arboreal-gas measure on spanning forests F of G_tilde, with probability proportional to lambda^{|E(F)|}, P(u_1 connected to v_1) >= P(u_1 connected to v_2).
source:
  primary_locator: >-
    Arvind Ayyer, Svante Linusson, and Mohan Ravichandran, “The bunkbed problem and the random cluster model,” arXiv:2509.18788, Conjecture 1.7, page 3, https://arxiv.org/pdf/2509.18788.
  access_date: 2026-08-02
  status_evidence: >-
    Exact-title, arXiv-ID, authors, “arboreal gas,” and Conjecture 1.7 follow-up searches on 2026-08-02 found no resolution. This is a distinct arboreal variant; the classical percolation bunkbed conjecture is not the target.
baseline:
  current_value_or_range: >-
    The paper proves selected graph/post regimes and asymptotic lambda regimes. The local exact forest enumerator calibrates K2 at lambda=1: same-layer connection weight 8 versus cross-layer 6. The paper’s full special-case baseline was not replayed.
  replay_command: >-
    python checkers/check_arboreal_bunkbed.py fixtures/bunkbed_k2_lambda1.json
witness:
  format: >-
    JSON {base graph, u, v, lambda as rational string}; a witness is a base graph and rational lambda for which exact weighted forest sums reverse the inequality.
  checker_command: >-
    python checkers/check_arboreal_bunkbed.py fixtures/bunkbed_k2_lambda1.json
  checker_hash: sha256:33dee230008fea09365539247332ff50298b30346373ce997f6da56f3a48a225
  calibration_cases: >-
    known-positive: K2, lambda=1 gives exact weights 8>=6; adversarial domain-boundary negative: K2, lambda=0 is rejected because the conjecture requires lambda>0; malformed: fixtures/malformed.json is rejected; frontier: source special cases not replayed.
search_edge: >-
  Use deletion-contraction with treewidth-aware memoization on the full ladder, compute the signed difference polynomial in lambda exactly, and search its positive real roots rather than sampling lambda. Quotient by layer swap and base-graph automorphisms. This could turn each graph into one polynomial certificate, but no beyond-baseline benchmark exists.
budget:
  model: "GPT-5.6 Pro plus exact polynomial deletion-contraction"
  wall_clock: "24 h"
  cpu_gpu: "32 CPU cores"
  memory: "128 GB"
stop_rules: >-
  Stop immediately if the statement/status changes or the baseline cannot be replayed. Freeze on disagreement between two independent implementations. Require a method review after 20% of budget without new structural information; pause after a repeated plateau with no new representation; kill if measured growth exceeds the forecast by 4x. Require exact reproduction of at least one nontrivial theorem case and polynomial-state growth below 4x per added base vertex.
publication_path: >-
  Arvind Ayyer, Svante Linusson, and Mohan Ravichandran; probability/combinatorics and random-cluster community.
aliases: ["arboreal-gas-bunkbed-conjecture-1-7", "forest-bunkbed"]
---

# arboreal-bunkbed-full-ladder

**Admission label:** `needs-edge`  
**Gate count:** 7/9 green  
**Scout rank:** 14 of 17 (ordinal judgment; no score total)

## Admission gates

| # | Gate | State | Evidence |
|---:|---|:---:|---|
| 1 | Statement pinned | GREEN | Measure, full bunkbed, quantifiers, and inequality pinned. |
| 2 | Primary source pinned | GREEN | Conjecture 1.7/page 3 pinned. |
| 3 | Open status fresh | GREEN | Exact-title/status searches found no resolution. |
| 4 | Artifact grammar fixed | GREEN | Graph plus rational lambda grammar fixed. |
| 5 | Checker exists and calibrated | GREEN | Exact rational forest enumerator passes K2 calibration and rejects the lambda=0 boundary case. |
| 6 | Baseline reproduces | RED | Published special-case frontier not replayed. |
| 7 | Search edge stated | RED | Polynomial/treewidth edge is concrete but not benchmarked. |
| 8 | Budget and stop rule fixed | GREEN | Budget and growth kill rule fixed. |
| 9 | Scientific path named | GREEN | Authors and venue path named. |

## Priority vector

`[4, 2, 4, 3, 5, 5, 3, 2]` in the fixed order: open-status confidence, reachability, method advantage, witness/lemma plausibility, scientific value, verification quality, competition penalty, end-to-end cost.

| Dimension | Score | Evidence |
|---|:---:|---|
| open-status confidence | 4 | No resolution found, but source is nearly a year old. |
| reachability | 2 | Forest state space is severe despite treewidth opportunities. |
| method advantage | 4 | Exact difference polynomials improve over lambda sampling. |
| witness/lemma plausibility | 3 | Counterexample would be finite, but may require larger graphs/parameters. |
| scientific value | 5 | A resolution would matter in probability and bunkbed theory. |
| verification quality | 5 | Exact rational sums and polynomial root isolation are strong. |
| competition penalty | 3 | Bunkbed variants attract attention. |
| end-to-end cost | 2 | Deletion-contraction can become expensive quickly. |

## Scout notes

Classical bunkbed counterexamples do not settle this arboreal-gas statement.

## Deep-attack admission consequence

Do not allocate deep compute. Build and benchmark the stated search edge and reproduce the source baseline; where gate 5 is red, finish the independent checker before any generation/search.
