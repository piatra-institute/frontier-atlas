---
id: inverse-z-y-logconcavity
result_class: B2
statement: >-
  For every finite matroid M, the coefficient sequence of its inverse Z-polynomial Y_M(x) is log-concave: y_i^2>=y_{i-1}y_{i+1} for every internal index i.
source:
  primary_locator: >-
    Tom Braden, Luis Ferroni, Jacob P. Matherne, and Nutan Nepal, “Inverse Kazhdan-Lusztig polynomials of matroids under deletion,” arXiv:2510.01086v1, Conjecture 1.2(d), https://arxiv.org/html/2510.01086v1#S1.
  access_date: 2026-08-02
  status_evidence: >-
    Exact-title, arXiv-ID, authors, Y-polynomial/log-concavity, and conjecture-number searches on 2026-08-02 found no resolution. The paper retains this claim after refuting a stronger real-rootedness proposal.
baseline:
  current_value_or_range: >-
    The source reports no Y-log-concavity counterexamples in the tested corank-2 forms and verification through cardinality 35. No independent matroid-to-Y recurrence implementation is bundled; only coefficient arithmetic is calibrated.
  replay_command: >-
    python checkers/check_matroid_polynomial.py fixtures/matroid_schema.json && python checkers/check_coefficient_logconcavity.py fixtures/logconcave_positive.json
witness:
  format: >-
    Canonical matroid encoding plus Y coefficients and a recurrence/flat-lattice trace sufficient for independent recomputation.
  checker_command: >-
    python checkers/check_matroid_polynomial.py fixtures/matroid_schema.json
  checker_hash: sha256:ca4f2f253d1f3d1bccd738248a620e8c0f14c019587fc4cc4db1eca17b9e6c89
  calibration_cases: >-
    coefficient arithmetic positive: [1,3,2]; negative: [1,1,2]; malformed: fixtures/malformed.json; frontier: no matroid-to-Y checker or <=35 replay.
search_edge: >-
  Target low-rank non-paving and sparse-paving matroids outside the corank-2 catalog, sharing flat-lattice/deletion caches with the Q lane. Y may amplify convolution effects differently from Q, but this claimed advantage is not yet experimentally established.
budget:
  model: "GPT-5.6 Pro plus Sage/C++ matroid enumeration"
  wall_clock: "24 h"
  cpu_gpu: "32 CPU cores"
  memory: "128 GB"
stop_rules: >-
  Stop immediately if the statement/status changes or the baseline cannot be replayed. Freeze on disagreement between two independent implementations. Require a method review after 20% of budget without new structural information; pause after a repeated plateau with no new representation; kill if measured growth exceeds the forecast by 4x. Require two independent Y implementations and replay of source examples before any new enumeration.
publication_path: >-
  Tom Braden, Luis Ferroni, Jacob P. Matherne, and Nutan Nepal; matroid KL-polynomial community.
aliases: ["matroid-Y-logconcavity", "bfmn-conjecture-1-2d"]
---

# inverse-z-y-logconcavity

**Admission label:** `needs-edge`  
**Gate count:** 6/9 green  
**Scout rank:** 8 of 17 (ordinal judgment; no score total)

## Admission gates

| # | Gate | State | Evidence |
|---:|---|:---:|---|
| 1 | Statement pinned | GREEN | Exact coefficientwise statement pinned. |
| 2 | Primary source pinned | GREEN | Conjecture 1.2(d) pinned. |
| 3 | Open status fresh | GREEN | No follow-up resolution found. |
| 4 | Artifact grammar fixed | GREEN | Matroid/Y/trace grammar specified. |
| 5 | Checker exists and calibrated | RED | Red: checker does not compute Y from M. |
| 6 | Baseline reproduces | RED | Reported baseline not replayed. |
| 7 | Search edge stated | RED | Shared new-family edge is unbenchmarked. |
| 8 | Budget and stop rule fixed | GREEN | Budget/two-engine rule fixed. |
| 9 | Scientific path named | GREEN | Authors/community named. |

## Priority vector

`[4, 3, 4, 4, 5, 2, 4, 3]` in the fixed order: open-status confidence, reachability, method advantage, witness/lemma plausibility, scientific value, verification quality, competition penalty, end-to-end cost.

| Dimension | Score | Evidence |
|---|:---:|---|
| open-status confidence | 4 | Current source still calls it a conjecture. |
| reachability | 3 | Same finite matroid frontier as Q, with potentially different failures. |
| method advantage | 4 | Cache-sharing gives practical advantage. |
| witness/lemma plausibility | 4 | Small matroid counterexample is plausible. |
| scientific value | 5 | Scientifically significant polynomial-positivity claim. |
| verification quality | 2 | Weak until full recurrence checker exists. |
| competition penalty | 4 | Relatively low direct competition. |
| end-to-end cost | 3 | Moderate/high setup cost. |

## Scout notes

Keep this as a distinct card because Q and Y can fail independently even if they share infrastructure.

## Deep-attack admission consequence

Do not allocate deep compute. Build and benchmark the stated search edge and reproduce the source baseline; where gate 5 is red, finish the independent checker before any generation/search.
