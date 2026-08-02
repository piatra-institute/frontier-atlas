---
id: perfect-matching-scheme-second-eigenvalue
result_class: B2
statement: >-
  Let n>=2 and let mu be a partition of n containing at least two parts equal to 1. In the perfect-matching association scheme on perfect matchings of K_{2n}, let A_mu join two matchings when their union has cycle half-length partition mu. The second-largest eigenvalue of A_mu is attained on the S_{2n}-irreducible indexed by [2n-2,2] (equivalently 2*[n-1,1]).
source:
  primary_locator: >-
    Himanshu Gupta, Allen Herman, Alice Lacaze-Masmonteil, Roghayeh Maleki, and Karen Meagher, “On the second largest eigenvalue of certain graphs in the perfect matching association scheme,” arXiv:2510.17135v1, Conjecture 1.1, https://arxiv.org/html/2510.17135v1#S1. The source also includes a separate branch mu=[n-1,1], n!=4; this card isolates the “at least two 1-parts” branch.
  access_date: 2026-08-02
  status_evidence: >-
    Exact-title, arXiv-ID, authors, and Conjecture 1.1 follow-up searches on 2026-08-02 found no resolution. The source repository remains the principal computational artifact located.
baseline:
  current_value_or_range: >-
    The authors verify the conjecture for n<=15 and prove several infinite partition families. Code/data are linked at https://github.com/Himanshugupta23/Perfect-Matching-Association-Scheme. Sage is not installed in the scout environment, so the n<=15 baseline was not independently replayed; the bundled checker is schema/dependency preflight only.
  replay_command: >-
    python checkers/check_pm_eigenvalue.py fixtures/pm_schema.json  # then replay the authors’ Sage repository through n=15
witness:
  format: >-
    JSON {n, mu, exact eigenvalues indexed by partitions lambda of n, provenance trace}; a counterexample is a mu with an exact eigenvalue larger than that at lambda=[n-1,1].
  checker_command: >-
    python checkers/check_pm_eigenvalue.py fixtures/pm_schema.json
  checker_hash: sha256:c54f63f8a444dce0f6db28820bbf06a75b7d0c300c15e617bdd18441e99bc6c6
  calibration_cases: >-
    schema/dependency preflight: fixtures/pm_schema.json; known-positive and near-miss eigenvalue cases are unavailable until Sage/repository replay; malformed: fixtures/malformed.json; frontier: n=15 reported, not replayed.
search_edge: >-
  Compute zonal-spherical eigenvalues by a partition dynamic program with memoized character/Jack evaluations, exploit conjugacy and dominance pruning, and target balanced mu just beyond n=15 rather than enumerating all scheme rows. This is concrete but not benchmarked against the authors’ Sage code.
budget:
  model: "GPT-5.6 Pro plus Sage/C++ exact partition DP"
  wall_clock: "20 h"
  cpu_gpu: "24 CPU cores"
  memory: "64 GB"
stop_rules: >-
  Stop immediately if the statement/status changes or the baseline cannot be replayed. Freeze on disagreement between two independent implementations. Require a method review after 20% of budget without new structural information; pause after a repeated plateau with no new representation; kill if measured growth exceeds the forecast by 4x. No attack until the authors’ n<=15 table is reproduced bit-for-bit and the partition DP beats it on at least one held-out row.
publication_path: >-
  Himanshu Gupta, Allen Herman, Alice Lacaze-Masmonteil, Roghayeh Maleki, and Karen Meagher; algebraic combinatorics / association schemes community.
aliases: ["pm-association-scheme-conjecture-1-1", "two-fixed-edges-second-eigenvalue"]
---

# perfect-matching-scheme-second-eigenvalue

**Admission label:** `needs-edge`  
**Gate count:** 6/9 green  
**Scout rank:** 5 of 17 (ordinal judgment; no score total)

## Admission gates

| # | Gate | State | Evidence |
|---:|---|:---:|---|
| 1 | Statement pinned | GREEN | Exact isolated branch and eigenvalue representation pinned. |
| 2 | Primary source pinned | GREEN | arXiv Conjecture 1.1 and repository pinned. |
| 3 | Open status fresh | GREEN | Fresh follow-up searches found no resolution. |
| 4 | Artifact grammar fixed | GREEN | Partition/eigenvalue table grammar fixed. |
| 5 | Checker exists and calibrated | RED | Red: bundled checker is only preflight, not exact recomputation. |
| 6 | Baseline reproduces | RED | n<=15 baseline not replayed because Sage/repo environment is absent. |
| 7 | Search edge stated | RED | Partition DP is unbenchmarked. |
| 8 | Budget and stop rule fixed | GREEN | Budget and benchmark-first rule fixed. |
| 9 | Scientific path named | GREEN | Authors/community named. |

## Priority vector

`[4, 4, 4, 4, 4, 3, 5, 4]` in the fixed order: open-status confidence, reachability, method advantage, witness/lemma plausibility, scientific value, verification quality, competition penalty, end-to-end cost.

| Dimension | Score | Evidence |
|---|:---:|---|
| open-status confidence | 4 | No resolution found and explicit repository remains active artifact. |
| reachability | 4 | Partition space is much smaller than graph space and n=16 is close. |
| method advantage | 4 | Exact DP/caching can outperform generic Sage evaluation. |
| witness/lemma plausibility | 4 | A violating partition/eigenvalue row is compact. |
| scientific value | 4 | Clean association-scheme spectral result. |
| verification quality | 3 | Exact arithmetic is available once implementation is complete. |
| competition penalty | 5 | Low-traffic specialized problem. |
| end-to-end cost | 4 | Moderate setup and cheap checking thereafter. |

## Scout notes

The extra source branch mu=[n-1,1], n!=4 is intentionally not duplicated here.

## Deep-attack admission consequence

Do not allocate deep compute. Build and benchmark the stated search edge and reproduce the source baseline; where gate 5 is red, finish the independent checker before any generation/search.
