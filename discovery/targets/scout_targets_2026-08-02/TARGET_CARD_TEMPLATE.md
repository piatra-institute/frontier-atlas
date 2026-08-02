# Target card template

This file is copied from the schema supplied in the 2026-08-02 scout request. The repository path `../../TARGET_CARD_TEMPLATE.md` was not present in the accessible filesystem, so this copy is the controlling local schema.

```yaml
id: canonical-target-id
result_class: B1 | B2 | B3
statement: >-
  exact statement: quantifiers, domain, conventions, success condition
source:
  primary_locator: paper/table URL + theorem or row number
  access_date: YYYY-MM-DD
  status_evidence: follow-up searches done; maintainer/author note if any
baseline:
  current_value_or_range: ...
  replay_command: ...
witness:
  format: ...
  checker_command: ...
  checker_hash: ...
  calibration_cases: known-positive, near-miss negative, malformed, frontier case
search_edge: >-
  why this attack beats prior searches
budget: { model: ..., wall_clock: ..., cpu_gpu: ..., memory: ... }
stop_rules: explicit continuation and kill criteria
publication_path: expert / community / table maintainer
aliases: [other atlas folders naming the same target]
```

## Admission gates

1. Statement pinned.
2. Primary source pinned.
3. Open status fresh.
4. Artifact grammar fixed.
5. Checker exists first and is calibrated.
6. Baseline reproduces within preflight budget.
7. Search edge stated and evidenced.
8. Budget and stop rule fixed.
9. Scientific path named.

A red gate means **not ready**.

## Result classes

- B0: calibration/reproduction only.
- B1: live finite frontier datum.
- B2: resolution of a currently open claim.
- B3: transferable method breakthrough.
- B4: externally validated field-shifting B2/B3; never self-awarded by the atlas.
