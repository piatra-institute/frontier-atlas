---
id: augmented-sombor-kpartite-turan-extremal
result_class: B2
statement: >-
  For integers n>=3 and 2<=k<=n, every finite simple k-partite graph G of order n for which the augmented Sombor index is defined satisfies ASO(G) <= ASO(T_n(k)), with equality only when G is isomorphic to the balanced Turan graph T_n(k). Here ASO(G)=sum_{uv in E(G)} sqrt((d(u)^2+d(v)^2)/(d(u)+d(v)-2)); graphs with a P2 component are excluded so denominators are nonzero.
source:
  primary_locator: >-
    Chunlei Xu, Kinkar Chandra Das, and Jayanta Bera, “Structural Properties and Applications of the Augmented Sombor Index,” arXiv:2606.26509v2, Conjecture 4.1, https://arxiv.org/html/2606.26509v2#S4.
  access_date: 2026-08-02
  status_evidence: >-
    Version 2 is dated 2026-07-22. Exact-title, arXiv-ID, author, “Conjecture 4.1,” and Turan/augmented-Sombor follow-up searches on 2026-08-02 found no proof or refutation.
baseline:
  current_value_or_range: >-
    No exhaustive order frontier is stated in an executable form. The source conjectures the Turan extremum. The local checker reproduces equality for T_6(3) and a strict lower value for K_{3,2,1}. The displayed closed-form right-hand side in the source appears typographically fragile, so the card pins the unambiguous ASO(G)<=ASO(T_n(k)) formulation.
  replay_command: >-
    python checkers/check_augmented_sombor.py fixtures/aso_t6_3.json && python checkers/check_augmented_sombor.py fixtures/aso_k321.json
witness:
  format: >-
    JSON {"n":integer,"k":integer,"edges":[[u,v],...],"parts":[[vertices],...]}; the supplied k-partition is validated and ASO is recomputed.
  checker_command: >-
    python checkers/check_augmented_sombor.py fixtures/aso_t6_3.json
  checker_hash: sha256:762d16d68eec7e603bd942bc53782148c9a7de3939c172a6f0f6ad66e8000951
  calibration_cases: >-
    known-positive/equality: T_6(3); near-miss negative: K_{3,2,1}; malformed: fixtures/malformed.json; frontier: no published exhaustive frontier is locally available.
search_edge: >-
  Search in degree-pair-histogram space before graph realization, then realize promising histograms by isomorph-free k-partite augmentation or SAT. ASO depends only on endpoint degree pairs, giving a stronger quotient than generic graph enumeration; however this advantage is not yet benchmarked against any prior search.
budget:
  model: "GPT-5.6 Pro plus nauty/SAT and exact algebraic comparison"
  wall_clock: "16 h"
  cpu_gpu: "24 CPU cores"
  memory: "64 GB"
stop_rules: >-
  Stop immediately if the statement/status changes or the baseline cannot be replayed. Freeze on disagreement between two independent implementations. Require a method review after 20% of budget without new structural information; pause after a repeated plateau with no new representation; kill if measured growth exceeds the forecast by 4x. Require a histogram relaxation that beats the Turan value or certifies a nontrivial order before graph generation.
publication_path: >-
  Chunlei Xu, Kinkar Chandra Das, and Jayanta Bera; chemical graph theory / discrete applied mathematics venues.
aliases: ["aso-turan-conjecture", "augmented-sombor-conjecture-4-1"]
---

# augmented-sombor-kpartite-turan-extremal

**Admission label:** `needs-edge`  
**Gate count:** 7/9 green  
**Scout rank:** 3 of 17 (ordinal judgment; no score total)

## Admission gates

| # | Gate | State | Evidence |
|---:|---|:---:|---|
| 1 | Statement pinned | GREEN | Exact extremal family, domain, objective, and equality condition pinned. |
| 2 | Primary source pinned | GREEN | arXiv v2 and Conjecture 4.1 pinned. |
| 3 | Open status fresh | GREEN | Fresh exact-title/status search found no resolution. |
| 4 | Artifact grammar fixed | GREEN | Graph plus explicit k-partition grammar fixed. |
| 5 | Checker exists and calibrated | GREEN | Checker validates partition and recomputes both ASO values; equality/strict cases pass. |
| 6 | Baseline reproduces | RED | No prior exhaustive baseline or code was available to reproduce. |
| 7 | Search edge stated | RED | Degree-histogram quotient is concrete but unbenchmarked. |
| 8 | Budget and stop rule fixed | GREEN | Budget and histogram-first stop rule fixed. |
| 9 | Scientific path named | GREEN | Authors and natural venue named. |

## Priority vector

`[5, 4, 4, 4, 3, 4, 5, 4]` in the fixed order: open-status confidence, reachability, method advantage, witness/lemma plausibility, scientific value, verification quality, competition penalty, end-to-end cost.

| Dimension | Score | Evidence |
|---|:---:|---|
| open-status confidence | 5 | Fresh explicit conjecture. |
| reachability | 4 | Endpoint-degree reduction may make moderate n reachable. |
| method advantage | 4 | Histogram quotient attacks the invariant directly. |
| witness/lemma plausibility | 4 | A counterexample is a small k-partite graph. |
| scientific value | 3 | Clean correction to a new index paper, but specialized. |
| verification quality | 4 | Checker is simple; exact radical comparison needs a certified second layer. |
| competition penalty | 5 | Low-traffic index literature and recent source. |
| end-to-end cost | 4 | Low-to-moderate compute and implementation cost. |

## Scout notes

A deep attack must use exact algebraic-number or interval-certified comparison, not floating-point ASO alone.

## Deep-attack admission consequence

Do not allocate deep compute. Build and benchmark the stated search edge and reproduce the source baseline; where gate 5 is red, finish the independent checker before any generation/search.
