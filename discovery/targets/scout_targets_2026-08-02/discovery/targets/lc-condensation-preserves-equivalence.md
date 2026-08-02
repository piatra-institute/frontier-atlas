---
id: lc-condensation-preserves-equivalence
result_class: B2
statement: >-
  Interpret graph condensation at C as identifying all vertices of C into one vertex and simplifying loops/multiple edges. If finite simple graphs G and G_prime are local-complementation equivalent and every vertex of C has at most one neighbor in V\C in both G and G_prime, then condense_C(G) and condense_C(G_prime) are local-complementation equivalent.
source:
  primary_locator: >-
    Lina Vandré et al., “Distinguishing Graph States by the Properties of Their Marginals,” arXiv:2406.09956v2 / Physical Review A 111, 052449 (2025), Conjecture 16, page 12, https://arxiv.org/abs/2406.09956 and https://doi.org/10.1103/PhysRevA.111.052449.
  access_date: 2026-08-02
  status_evidence: >-
    Exact-title, DOI, “Conjecture 16,” local-complementation, and condensation follow-up searches on 2026-08-02 found no clear resolution. The source wording about “each node in C connected to at most one node in the neighbourhood in V\C” admits more than one formal reading, and no author clarification was obtained.
baseline:
  current_value_or_range: >-
    The scout checker enumerates local-complementation orbits for small graphs under the stated interpretation. A P4-derived equivalent pair with C={3} condenses to equivalent graphs. This is calibration only; the paper’s computational evidence/classification was not replayed.
  replay_command: >-
    python checkers/check_lc_condensation.py fixtures/lc_positive.json
witness:
  format: >-
    JSON containing G, G_prime, C, and optionally a local-complement sequence; simple graphs are encoded by n and edge lists, with sorted vertex labels after condensation.
  checker_command: >-
    python checkers/check_lc_condensation.py fixtures/lc_positive.json
  checker_hash: sha256:8e7f117ae06ac47daf5e7a15158c8e081cd334ac533f9438f024bf6742375322
  calibration_cases: >-
    known-positive: fixtures/lc_positive.json; near-miss condition failure: fixtures/lc_condition_nearmiss.json; malformed: fixtures/malformed.json; frontier: no source orbit corpus replayed.
search_edge: >-
  Canonicalize entire local-complementation orbits using graph-state stabilizer invariants, quotient candidate subsets C by orbit automorphisms, and test condensation as a map between orbit representatives. This is a finite orbit problem with strong symmetry, but source-scale advantage is not yet measured.
budget:
  model: "GPT-5.6 Pro plus C++/nauty stabilizer-orbit code"
  wall_clock: "18 h"
  cpu_gpu: "24 CPU cores"
  memory: "64 GB"
stop_rules: >-
  Stop immediately if the statement/status changes or the baseline cannot be replayed. Freeze on disagreement between two independent implementations. Require a method review after 20% of budget without new structural information; pause after a repeated plateau with no new representation; kill if measured growth exceeds the forecast by 4x. First obtain author confirmation of the quantifier/condition and current status; otherwise kill rather than search an interpretation.
publication_path: >-
  Lina Vandré and coauthors; graph-state/local-Clifford quantum-information community and Physical Review A follow-up.
aliases: ["graph-state-condensation-conjecture-16", "lc-orbit-condensation"]
---

# lc-condensation-preserves-equivalence

**Admission label:** `needs-status`  
**Gate count:** 6/9 green  
**Scout rank:** 6 of 17 (ordinal judgment; no score total)

## Admission gates

| # | Gate | State | Evidence |
|---:|---|:---:|---|
| 1 | Statement pinned | RED | Red: the source condition has a material formalization ambiguity; this card records one interpretation. |
| 2 | Primary source pinned | GREEN | arXiv, DOI, conjecture number, and page pinned. |
| 3 | Open status fresh | RED | No resolution found, but neither author confirmation nor exhaustive citation audit. |
| 4 | Artifact grammar fixed | GREEN | JSON graph/subset/sequence grammar fixed for the recorded interpretation. |
| 5 | Checker exists and calibrated | GREEN | Small exact LC-orbit checker passes positive and condition-near-miss cases. |
| 6 | Baseline reproduces | RED | Paper-scale baseline not replayed. |
| 7 | Search edge stated | GREEN | Orbit/subset symmetry reduction is concrete. |
| 8 | Budget and stop rule fixed | GREEN | Budget and clarification-first kill rule fixed. |
| 9 | Scientific path named | GREEN | Authors/community named. |

## Priority vector

`[3, 4, 4, 4, 4, 5, 4, 4]` in the fixed order: open-status confidence, reachability, method advantage, witness/lemma plausibility, scientific value, verification quality, competition penalty, end-to-end cost.

| Dimension | Score | Evidence |
|---|:---:|---|
| open-status confidence | 3 | Status and wording need author confirmation. |
| reachability | 4 | LC orbits and subset symmetries are finite and often compress well. |
| method advantage | 4 | Stabilizer invariants and orbit quotient are natural advantages. |
| witness/lemma plausibility | 4 | A counterexample is a pair of small graphs plus C. |
| scientific value | 4 | Relevant to graph-state classification and marginals. |
| verification quality | 5 | LC equivalence and condensation can be checked independently. |
| competition penalty | 4 | Moderate attention, not a famous public target. |
| end-to-end cost | 4 | Small-graph computation is affordable. |

## Scout notes

Do not attack until the source condition is disambiguated in writing.

## Deep-attack admission consequence

Do not allocate deep compute. Resolve every red status/statement gate first; a negative web search alone is insufficient where author clarification or an older citation graph is missing.
