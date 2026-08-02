---
id: inverse-kl-q-logconcavity
result_class: B2
statement: >-
  For every finite matroid M, the coefficient sequence of its inverse Kazhdan-Lusztig polynomial Q_M(x) is log-concave: q_i^2>=q_{i-1}q_{i+1} for every internal index i.
source:
  primary_locator: >-
    Tom Braden, Luis Ferroni, Jacob P. Matherne, and Nutan Nepal, “Inverse Kazhdan-Lusztig polynomials of matroids under deletion,” arXiv:2510.01086v1, Conjecture 1.2(c), https://arxiv.org/html/2510.01086v1#S1.
  access_date: 2026-08-02
  status_evidence: >-
    Exact-title, arXiv-ID, authors, Q-polynomial/log-concavity, and conjecture-number searches on 2026-08-02 found no resolution. The same paper explicitly refutes a stronger normalized real-rootedness conjecture but retains Q-log-concavity.
baseline:
  current_value_or_range: >-
    The source reports no Q-log-concavity counterexamples in its tested corank-2 family and verifies all corank-2 matroids of cardinality <=35. The bundled preflight only validates an encoding and a coefficient-list checker; it does not independently compute Q_M from M, so the source baseline is not replayed.
  replay_command: >-
    python checkers/check_matroid_polynomial.py fixtures/matroid_schema.json && python checkers/check_coefficient_logconcavity.py fixtures/logconcave_positive.json
witness:
  format: >-
    Canonical matroid encoding (rank, ordered ground set, and sorted bases or a frozen Sage matroid serialization), plus Q coefficients and a recurrence trace independently recomputable from the lattice of flats.
  checker_command: >-
    python checkers/check_matroid_polynomial.py fixtures/matroid_schema.json
  checker_hash: sha256:ca4f2f253d1f3d1bccd738248a620e8c0f14c019587fc4cc4db1eca17b9e6c89
  calibration_cases: >-
    coefficient arithmetic positive: [1,3,2]; negative: [1,1,2]; malformed: fixtures/malformed.json; frontier: matroid-to-Q computation and corank-2 <=35 replay are absent.
search_edge: >-
  Leave the heavily tested corank-2 family and enumerate low-rank non-paving/sparse-paving matroids using canonical base-exchange augmentation, memoizing deletion recurrences and flat lattices. The representation change is plausible, but a full independent Q engine and benchmark are prerequisites.
budget:
  model: "GPT-5.6 Pro plus Sage/C++ matroid enumeration"
  wall_clock: "24 h"
  cpu_gpu: "32 CPU cores"
  memory: "128 GB"
stop_rules: >-
  Stop immediately if the statement/status changes or the baseline cannot be replayed. Freeze on disagreement between two independent implementations. Require a method review after 20% of budget without new structural information; pause after a repeated plateau with no new representation; kill if measured growth exceeds the forecast by 4x. Do not search until two independent implementations reproduce published Q polynomials and the <=35 corank-2 baseline subset.
publication_path: >-
  Tom Braden, Luis Ferroni, Jacob P. Matherne, and Nutan Nepal; matroid Kazhdan-Lusztig community.
aliases: ["matroid-Q-logconcavity", "bfmn-conjecture-1-2c"]
---

# inverse-kl-q-logconcavity

**Admission label:** `needs-edge`  
**Gate count:** 6/9 green  
**Scout rank:** 7 of 17 (ordinal judgment; no score total)

## Admission gates

| # | Gate | State | Evidence |
|---:|---|:---:|---|
| 1 | Statement pinned | GREEN | Exact polynomial family and coefficient inequality pinned. |
| 2 | Primary source pinned | GREEN | arXiv and Conjecture 1.2(c) pinned. |
| 3 | Open status fresh | GREEN | Fresh follow-up search found no resolution. |
| 4 | Artifact grammar fixed | GREEN | Canonical matroid/coefficient/trace grammar specified. |
| 5 | Checker exists and calibrated | RED | Red: no independent matroid-to-Q checker exists in package. |
| 6 | Baseline reproduces | RED | Reported corank-2 <=35 baseline not replayed. |
| 7 | Search edge stated | RED | New family/recurrence-cache edge is unbenchmarked. |
| 8 | Budget and stop rule fixed | GREEN | Budget and two-engine stop rule fixed. |
| 9 | Scientific path named | GREEN | Authors/community named. |

## Priority vector

`[4, 3, 4, 4, 5, 2, 4, 3]` in the fixed order: open-status confidence, reachability, method advantage, witness/lemma plausibility, scientific value, verification quality, competition penalty, end-to-end cost.

| Dimension | Score | Evidence |
|---|:---:|---|
| open-status confidence | 4 | Current source still retains the conjecture. |
| reachability | 3 | Matroid enumeration is hard, but leaving corank 2 opens untested structure. |
| method advantage | 4 | Canonical augmentation plus recurrence caching is useful. |
| witness/lemma plausibility | 4 | A small matroid and failed coefficient inequality is finite. |
| scientific value | 5 | Log-concavity of KL-type polynomials is scientifically significant. |
| verification quality | 2 | Weak until Q computation is independently certified. |
| competition penalty | 4 | Less watched than real-rootedness; source is a small team. |
| end-to-end cost | 3 | Substantial but bounded software work. |

## Scout notes

The stronger normalized inverse-KL real-rootedness claim is already refuted and is not a target.

## Deep-attack admission consequence

Do not allocate deep compute. Build and benchmark the stated search edge and reproduce the source baseline; where gate 5 is red, finish the independent checker before any generation/search.
