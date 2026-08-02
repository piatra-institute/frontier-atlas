---
id: flowboost-en-singular-spectrum
result_class: B2
statement: >-
  For every integer n>=3, let E_n be the n-by-n coupling matrix defined in Equation (15) of the source. Its singular value on span(1) is 1, and the n-1 singular values of E_n restricted to W=1^perp are exactly 2^{-k/2} for k=1,...,n-1; in particular the nontrivial spectrum is independent of n except for truncation.
source:
  primary_locator: >-
    Baran Hashemi, “Spectral Structure in Finite Free Information Inequalities and p-Stam Phase Transitions,” arXiv:2604.11922v2 (15 May 2026), Conjecture 4.1 and Equation (15), https://arxiv.org/html/2604.11922v2#S4.SS1.
  access_date: 2026-08-02
  status_evidence: >-
    Exact arXiv-ID, current/earlier title, author, “Conjecture 4.1,” FlowBoost, and singular-spectrum searches on 2026-08-02 found no proof or counterexample. The source reports high-precision numerics rather than a proof.
baseline:
  current_value_or_range: >-
    The source reports numerical verification through n<=90 and small relative error for the first ten modes. The bundled script only compares a supplied list to the conjectured sequence; it does not independently construct E_n from Hermite roots/weights, so this baseline is not replayed.
  replay_command: >-
    python checkers/check_flowboost_spectrum.py fixtures/flowboost_n4_spectrum.json
witness:
  format: >-
    JSON containing n, a fully specified exact/high-precision construction trace for E_n, and either singular vectors/values or an exact residual/minor certificate showing departure from 2^{-k/2}.
  checker_command: >-
    python checkers/check_flowboost_spectrum.py fixtures/flowboost_n4_spectrum.json
  checker_hash: sha256:2fbf8acc1e322c2b329a407d91d4b7c0c549d2b70f116c524f7b30e7f34a152c
  calibration_cases: >-
    sequence-shape positive: supplied n=4 target list; no independent E_n positive/negative pair; malformed: fixtures/malformed.json; frontier: n=90 reported, not replayed.
search_edge: >-
  Express E_n in an orthogonal Hermite/cumulant basis where the conjectured singular values suggest a triangular or weighted-shift operator, then derive exact rational/algebraic matrix identities. This is a proof-obligation lane rather than blind numerical search, but the basis reduction is only a hypothesis and has not been demonstrated.
budget:
  model: "GPT-5.6 Pro plus SymPy/Arb high-precision algebra"
  wall_clock: "20 h"
  cpu_gpu: "16 CPU cores"
  memory: "64 GB"
stop_rules: >-
  Stop immediately if the statement/status changes or the baseline cannot be replayed. Freeze on disagreement between two independent implementations. Require a method review after 20% of budget without new structural information; pause after a repeated plateau with no new representation; kill if measured growth exceeds the forecast by 4x. Require an independent E_n constructor matching the source through at least n=20 and a symbolic simplification at n=3..6 before scaling.
publication_path: >-
  Baran Hashemi; information theory / free probability / spectral analysis community.
aliases: ["flowboost-conjecture-4-1", "finite-free-En-spectrum"]
---

# flowboost-en-singular-spectrum

**Admission label:** `needs-edge`  
**Gate count:** 6/9 green  
**Scout rank:** 17 of 17 (ordinal judgment; no score total)

## Admission gates

| # | Gate | State | Evidence |
|---:|---|:---:|---|
| 1 | Statement pinned | GREEN | Operator, domain, subspace, and target singular values pinned. |
| 2 | Primary source pinned | GREEN | arXiv, equation, and conjecture locator pinned. |
| 3 | Open status fresh | GREEN | Fresh title/ID searches found no resolution. |
| 4 | Artifact grammar fixed | GREEN | Construction trace plus spectrum certificate grammar specified. |
| 5 | Checker exists and calibrated | RED | Red: checker does not independently construct E_n. |
| 6 | Baseline reproduces | RED | n<=90 numerical baseline not replayed. |
| 7 | Search edge stated | RED | Hermite-basis idea is unproved and unbenchmarked. |
| 8 | Budget and stop rule fixed | GREEN | Budget and symbolic-preflight stop rule fixed. |
| 9 | Scientific path named | GREEN | Author/community named. |

## Priority vector

`[4, 2, 4, 2, 4, 2, 4, 2]` in the fixed order: open-status confidence, reachability, method advantage, witness/lemma plausibility, scientific value, verification quality, competition penalty, end-to-end cost.

| Dimension | Score | Evidence |
|---|:---:|---|
| open-status confidence | 4 | Recent explicit conjecture with no follow-up found. |
| reachability | 2 | A proof may be elegant, but finite numerical witness is unlikely after n=90. |
| method advantage | 4 | Basis change could expose exact structure. |
| witness/lemma plausibility | 2 | Counterexample plausibility is low given extensive numerics; lemma plausibility remains uncertain. |
| scientific value | 4 | Could explain a striking universal spectrum. |
| verification quality | 2 | Current verification is only list comparison. |
| competition penalty | 4 | Low-traffic one-author preprint. |
| end-to-end cost | 2 | Symbolic algebra may become difficult quickly. |

## Scout notes

This is retained as a proof-obligation card, not as a likely small-counterexample search.

## Deep-attack admission consequence

Do not allocate deep compute. Build and benchmark the stated search edge and reproduce the source baseline; where gate 5 is red, finish the independent checker before any generation/search.
