# Target card

The atomic unit of the atlas. A prompt is a disposable view of a target card, not the
other way round. Copy to `discovery/targets/<canonical-id>.md` and fill in. A card
earns deep compute only after every admission gate below is green.

Rationale (`BREAKTHROUGH_STRATEGY.md`): a cheap checker is an admission condition, not
a tractability forecast. Open, reachable, and valuable are three separate tests.

## Card

```yaml
id: canonical-target-id            # one ID; list aliases below, not duplicate cards
result_class: B1 | B2 | B3         # see classes; B0 (calibration) is not a target
statement: >-
  exact statement: quantifiers, domain, conventions, success condition
source:
  primary_locator: paper/table URL + theorem or row number
  access_date: YYYY-MM-DD
  status_evidence: follow-up searches done; maintainer/author note if any
baseline:
  current_value_or_range: ...
  replay_command: ...              # must replay within the preflight budget
witness:                           # or lemma, for the proof-obligation lane
  format: ...                      # canonical encoding of a candidate
  checker_command: ...             # small, independent, exists BEFORE search
  checker_hash: ...
  calibration_cases: known-positive, near-miss negative, malformed, frontier case
search_edge: >-
  why THIS attack beats prior searches: a representation, symmetry reduction, tool,
  data, model capability, or algorithm prior work did not use. If none, not ready.
budget: { model: ..., wall_clock: ..., cpu_gpu: ..., memory: ... }
stop_rules: explicit continuation and kill criteria (see below)
publication_path: expert / community / table maintainer who can validate and absorb it
aliases: [other atlas folders naming the same target]
```

## Admission gates (all must be true for deep compute)

1. Statement pinned (exact quantifiers, domain, success condition).
2. Primary source pinned (locator + access date).
3. Open status fresh (checked against follow-ups within 30 days; sooner for fast records).
4. Artifact grammar fixed (candidate's canonical format).
5. Checker exists first, and passes positive + adversarial-negative calibration.
6. Baseline reproduces within the preflight budget.
7. Search edge stated (what is new vs prior attempts).
8. Budget and stop rule fixed in advance.
9. Scientific path named (who validates and absorbs a result).

A card failing any gate is **not ready**, not merely low priority.

## Priority (score 0-5 per dimension, with written evidence; keep the vector, no single total)

open-status confidence | reachability (residual search space, weak prior search, useful
relaxations) | method advantage | witness/lemma plausibility | scientific value |
verification quality | competition penalty (low attention, slow frontier, no optimized
incumbent) | end-to-end cost.

## Result classes

- **B0 calibration** - reproduce a known result with an independent checker. Validates a
  harness. Not a contribution.
- **B1 frontier datum** - improve a live table entry / record / finite case / verified
  range, novelty and baseline independently confirmed.
- **B2 open-claim resolution** - prove or refute a currently-open claim, with statement
  match, exact evidence, and expert review. The default breakthrough target.
- **B3 method breakthrough** - a new search/reduction/proof method that transfers across
  independent targets or unlocks a new scale. Transfer is part of the claim.
- **B4 major** - a B2/B3 that shifts a field or removes a field-wide obstruction; requires
  external validation. The atlas cannot award this to itself.

Heuristic nulls, model-generated conjectures, status audits, and reproductions are inputs,
never counted as B1-B4 unless they meet these criteria.

## Kill rules (during deep attack)

- status/statement ambiguity found -> stop immediately;
- baseline not reproduced in preflight -> reclassify as infrastructure, not research;
- repeated plateau with no new representation/lemma -> pause and do a method review;
- projected proof/search growth exceeds budget by a fixed factor -> stop;
- second implementation disagrees -> freeze the claim, debug before any new search;
- no new structural information after 20% of budget -> require a method review.

"Persist" means persistent hypothesis revision, not persistent consumption of the same
search distribution.

## On completion

Blind verification (verifier sees the frozen statement + artifact + checker, NOT the
generator's derivation; reconcile after). Then: statement-match review, was-it-open-at-the-
timestamp review, would-an-expert-call-it-new review. For B2-B4, expert contact is part of
completion - the result is done when it survives informed external scrutiny, not when the
local checker prints PASS.

Record the outcome in the attempt ledger (`ATTEMPTS.jsonl`): target id, statement version,
status-check date, method, cost/seeds, best score, response-curve summary, outcome class or
null, verifier status, updated reachability estimate, exact next obligation, and the
continue/pause/kill/publish decision.
