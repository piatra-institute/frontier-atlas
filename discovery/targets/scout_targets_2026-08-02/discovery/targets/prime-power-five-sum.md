---
id: prime-power-five-sum
result_class: B2
statement: >-
  Every natural number n>23 can be written as n=q_1+...+q_m with 2<=m<=5, where each q_i=p_i^{a_i} is a prime power with p_i prime and exponent a_i>=2. This card provisionally permits repeated prime powers because the source does not make the repetition convention explicit.
source:
  primary_locator: >-
    Julius Stricker, “On the Representation of Integers as Sums of Limited Prime Powers,” arXiv:2508.01686v1, Conjecture 1, https://arxiv.org/html/2508.01686v1#S1.
  access_date: 2026-08-02
  status_evidence: >-
    Exact-title, arXiv-ID, author, and exact-conjecture searches on 2026-08-02 found no resolution. The source is about a year old, the repetition convention is not explicit, and the reported computational range differs between snippets/sections; no author confirmation or artifact was obtained.
baseline:
  current_value_or_range: >-
    The body reports exhaustive verification through 10^7 and sampling up to 10^10, while some summary text appears to advertise a different upper scale. No code, checksum, or complete exception table was pinned. Local calibration only verifies 24=8+16.
  replay_command: >-
    python checkers/check_prime_power_sum.py fixtures/prime_power_24.json
witness:
  format: >-
    JSON {"n":integer,"representation":[prime powers]}; a refutation candidate is an n>23 plus an independently checked certificate that no 2-5 term representation exists.
  checker_command: >-
    python checkers/check_prime_power_sum.py fixtures/prime_power_24.json
  checker_hash: sha256:dbf0955cd80d961ad2d1b79df425b271f0f8f32930fbaa79f0fab007eb30c3d4
  calibration_cases: >-
    known-positive: 24=[8,16]; near-miss/out-of-domain: 23; malformed: fixtures/malformed.json; frontier: reported 10^7 exhaustive range is not replayable from a pinned artifact.
search_edge: >-
  Use modular residue sieves to identify sparse candidate integers, then exact bitset convolution / meet-in-the-middle over prime powers, with independent modular certificates for nonrepresentability. This is a concrete acceleration, but it cannot compensate for the unresolved statement convention and baseline artifact.
budget:
  model: "GPT-5.6 Pro plus C++ bitsets/MITM"
  wall_clock: "12 h"
  cpu_gpu: "24 CPU cores"
  memory: "128 GB"
stop_rules: >-
  Stop immediately if the statement/status changes or the baseline cannot be replayed. Freeze on disagreement between two independent implementations. Require a method review after 20% of budget without new structural information; pause after a repeated plateau with no new representation; kill if measured growth exceeds the forecast by 4x. Obtain author clarification on repetition and the exact verified range before any search; otherwise kill.
publication_path: >-
  Julius Stricker; additive number theory/preprint author validation, followed by a computational number theory venue.
aliases: ["limited-prime-powers-conjecture-1", "five-prime-power-sum"]
---

# prime-power-five-sum

**Admission label:** `needs-status`  
**Gate count:** 6/9 green  
**Scout rank:** 15 of 17 (ordinal judgment; no score total)

## Admission gates

| # | Gate | State | Evidence |
|---:|---|:---:|---|
| 1 | Statement pinned | RED | Red: repetition convention is not explicit; card states a provisional reading. |
| 2 | Primary source pinned | GREEN | Primary arXiv and Conjecture 1 pinned. |
| 3 | Open status fresh | RED | No resolution found, but no author confirmation and source is a year old. |
| 4 | Artifact grammar fixed | GREEN | Representation JSON grammar fixed. |
| 5 | Checker exists and calibrated | GREEN | Term-level checker passes positive/out-of-domain cases. |
| 6 | Baseline reproduces | RED | Published exhaustive frontier has no pinned replay artifact. |
| 7 | Search edge stated | GREEN | Residue sieve plus bitset/MITM is concrete. |
| 8 | Budget and stop rule fixed | GREEN | Budget and clarification-first rule fixed. |
| 9 | Scientific path named | GREEN | Author/venue path named. |

## Priority vector

`[3, 4, 3, 4, 2, 5, 5, 4]` in the fixed order: open-status confidence, reachability, method advantage, witness/lemma plausibility, scientific value, verification quality, competition penalty, end-to-end cost.

| Dimension | Score | Evidence |
|---|:---:|---|
| open-status confidence | 3 | Search-negative status with statement ambiguity. |
| reachability | 4 | Representation testing is extremely fast and modular sieves scale. |
| method advantage | 3 | Technique is standard but well matched. |
| witness/lemma plausibility | 4 | A least exception is a simple integer with a strong certificate. |
| scientific value | 2 | The claim is narrow and computational. |
| verification quality | 5 | Independent arithmetic verification is excellent. |
| competition penalty | 5 | Low visible traffic. |
| end-to-end cost | 4 | Cheap once conventions/baseline are fixed. |

## Scout notes

A nonrepresentation checker must prove absence, not merely fail to find a sum.

## Deep-attack admission consequence

Do not allocate deep compute. Resolve every red status/statement gate first; a negative web search alone is insufficient where author clarification or an older citation graph is missing.
