---
id: signed-circulant-c2-global-spectral-minimum
result_class: B2
statement: >-
  For every even integer n >= 8, let C_n(1,2) be the 4-regular circulant graph on Z/nZ with edges of steps 1 and 2. For an edge signing sigma:E(C_n(1,2))-> {+1,-1}, let A_sigma be the signed adjacency matrix and rho(A_sigma) its spectral radius. Then min_sigma rho(A_sigma) = rho_-(n) := 2*sqrt(cos(pi/n)^2 + cos(2*pi/n)^2); equivalently, the alpha=-1 twisted switching class is a global minimizer.
source:
  primary_locator: >-
    Vaibhav Suvagiya, “Signed circulants at the Ramanujan bound,” arXiv:2607.18334v1, Conjecture 3, https://arxiv.org/html/2607.18334v1#S3 (source text around Conjecture 3).
  access_date: 2026-08-02
  status_evidence: >-
    The preprint was posted 2026-07-19. Exact-title, arXiv-ID, author/repository, and conjecture-phrase follow-up searches on 2026-08-02 found no proof or counterexample; the source still labels it Conjecture 3. This is a high-confidence fresh-status check, not a claim that every private communication has been searched.
baseline:
  current_value_or_range: >-
    The source enumerates all 2^(n+1) switching classes for n=8,10,12,14,16,18 and reports agreement with rho_-(n) to 1e-9. The bundled independent NumPy enumerator reproduced all six rows; largest absolute error was below 2.3e-15.
  replay_command: >-
    python checkers/check_signed_circulant.py --baseline 8 10 12 14 16 18
witness:
  format: >-
    JSON object {"n": even integer >=8, "bits": binary string of length n+1}; gauge fixes n-1 step-1 edges positive, then encodes the wrap edge and all n step-2 edges.
  checker_command: >-
    python checkers/check_signed_circulant.py fixtures/signed_n8_optimizer.json --certify
  checker_hash: sha256:122ecffa9b4ee3b3d3bf04b286d1134036bcd8f2f464cb99e90d2ac1b4de5934
  calibration_cases: >-
    known-positive/equality: fixtures/signed_n8_optimizer.json; near-miss negative: fixtures/signed_n8_all_positive.json (rho=4, not an optimizer); malformed: fixtures/malformed.json must exit nonzero; frontier: --baseline 18 enumerates 524,288 switching classes.
search_edge: >-
  Replace raw 2^(n+1) enumeration by an exact threshold decision for both rho(A)<=t and rho(-A)<=t at t=rho_-(n), using the bandwidth-2 cyclic structure, Schur-complement/LDL recurrences, dihedral orbit canonicalization, and interval/Sturm certificates. The bundled no-search preflight independently reduces the n=18 switching classes from 524,288 to 15,370 dihedral orbits (34.11x), with the orbit count cross-checked by Burnside averaging and sampled spectral invariance. The threshold recurrence is the remaining Stage-1 method obligation.
budget:
  model: "GPT-5.6 Pro for method design; deterministic Python/C++ exact search"
  wall_clock: "12 h"
  cpu_gpu: "32 CPU cores; no GPU required"
  memory: "64 GB"
stop_rules: >-
  Stop immediately if the statement/status changes or the baseline cannot be replayed. Freeze on disagreement between two independent implementations. Require a method review after 20% of budget without new structural information; pause after a repeated plateau with no new representation; kill if measured growth exceeds the forecast by 4x. Continue only if the recurrence compresses states or yields a monotonicity lemma by the 20% review.
publication_path: >-
  Vaibhav Suvagiya (author) and the signed-graphs/spectral-graph community; first route is an author-checked note tied to arXiv:2607.18334 and its public repository.
aliases: ["bilu-linial-parity-conjecture-3", "signed-circulant-rho-minus"]
---

# signed-circulant-c2-global-spectral-minimum

**Admission label:** `ready`  
**Gate count:** 9/9 green  
**Scout rank:** 1 of 17 (ordinal judgment; no score total)

## Admission gates

| # | Gate | State | Evidence |
|---:|---|:---:|---|
| 1 | Statement pinned | GREEN | Exact quantifiers, graph, signing convention, objective, and equality value are frozen from Conjecture 3. |
| 2 | Primary source pinned | GREEN | arXiv version and Conjecture 3 locator pinned; accessed 2026-08-02. |
| 3 | Open status fresh | GREEN | Fresh 14-day-old source plus exact-title/ID/follow-up searches found no resolution. |
| 4 | Artifact grammar fixed | GREEN | Gauge-fixed n+1-bit switching-class grammar is canonical and independently decoded. |
| 5 | Checker exists and calibrated | GREEN | Independent checker exists; equality, nonoptimizer, malformed input, and n=18 frontier were exercised. |
| 6 | Baseline reproduces | GREEN | All source baseline orders n=8..18 reproduced locally in 24.20 seconds on the scout host. |
| 7 | Search edge stated | GREEN | The symmetry component is measured: 524,288 n=18 classes collapse to 15,370 orbits (34.11x), independently matched by Burnside counting; the bandwidth-2 threshold recurrence is explicitly scoped as the next obligation. |
| 8 | Budget and stop rule fixed | GREEN | 12-hour/32-core/64-GB budget and explicit review/kill criteria are frozen. |
| 9 | Scientific path named | GREEN | Author and immediate specialist validation route are named. |

## Priority vector

`[5, 4, 5, 4, 3, 5, 5, 5]` in the fixed order: open-status confidence, reachability, method advantage, witness/lemma plausibility, scientific value, verification quality, competition penalty, end-to-end cost.

| Dimension | Score | Evidence |
|---|:---:|---|
| open-status confidence | 5 | Source is two weeks old and still explicitly conjectural. |
| reachability | 4 | Residual finite classes grow exponentially, but cycle bandwidth offers strong compression. |
| method advantage | 5 | Dihedral quotienting already yields 34.11x at n=18; threshold DP and exact inertia certificates target the remaining exponential factor. |
| witness/lemma plausibility | 4 | A small counterexample would be a bit string; a proof may emerge from finite-state recurrence. |
| scientific value | 3 | Useful spectral-signing result, though narrower than a field-wide conjecture. |
| verification quality | 5 | Integer matrices, exact root isolation, and a second implementation give excellent verification. |
| competition penalty | 5 | One-author fresh preprint and little visible follow-up. |
| end-to-end cost | 5 | Cheap checker, reproduced frontier, no large dependencies. |

## Scout notes

Stage 0 only: the bundled enumeration is B0 calibration. No n>18 witness search was performed.

## Deep-attack admission consequence

All nine gates are green. This card may enter preflight/deep compute, subject to a final same-day status refresh. The bundled work remains B0 calibration, not an attack result.
