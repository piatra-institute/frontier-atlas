# Scout package: pinned finite targets, Stage 0

**Frozen:** 2026-08-02  
**Scope:** source discovery, statement/status pinning, checker preflight, baseline analysis, and search-edge admission.  
**Explicitly excluded:** witness search, counterexample generation beyond B0 calibration, or claims of a new result.

## Outcome

- 17 target cards from 13 source families.
- 1 `ready` card.
- 3 `needs-status` cards.
- 13 `needs-edge` cards.
- 43 claim-level candidates screened; 26 rejected before card admission.

The sole all-green target is `signed-circulant-c2-global-spectral-minimum`. Its bundled n=8..18 enumeration merely reproduces the source frontier and is classified B0.

## Important provenance limitation

Neither `../../TARGET_CARD_TEMPLATE.md` nor the requested upstream `BREAKTHROUGH_STRATEGY.md` existed in the accessible filesystem. `TARGET_CARD_TEMPLATE.md` is copied from the schema pasted in the request. `BREAKTHROUGH_STRATEGY.md` is explicitly marked as an operational reconstruction from the pasted rationale and rules. No claim is made that either file reproduces an inaccessible upstream document byte-for-byte.

## Layout

- `discovery/targets/`: 17 atomic cards.
- `SHORTLIST.md`: ranked eight-dimensional score vectors, no totals.
- `STATUS_AUDIT.md`: freshness method and target-by-target confidence.
- `SCREENING_LOG.md`: retained/rejected counts and reasons.
- `CALIBRATION_REPORT.md`: checker and B0 replay results.
- `checkers/`, `fixtures/`, `calibration/`: independent scout harness.
- `validate_package.py`: schema/gate/label validator.
- `requirements.txt`, `ENVIRONMENT.md`: frozen core Python environment.
- `MANIFEST.sha256`: content hashes generated after validation.

## Run

From this directory:

```bash
python validate_package.py
bash run_calibrations.sh
```

On runners with a short per-process execution cap, use the individual replay commands in each card; the bundled calibration logs were intentionally split at the execution boundary.

The full signed-circulant baseline enumerates 698,880 switching classes across n=8,10,12,14,16,18. It completed in 24.20 seconds on the scout host; the timed log is bundled. A separate no-search symmetry preflight reduces the n=18 space from 524,288 switching classes to 15,370 dihedral orbits (34.11x), with agreement between canonical enumeration and Burnside counting. Partial preflight scripts for matroids, perfect-matching schemes, Vine circuits, and FlowBoost deliberately print `full_checker_ready: false`; this is evidence for red gate 5, not a checker success.

## Interpretation of labels

- `ready`: all nine gates green; eligible for a separate preflight/deep-attack session after status refresh.
- `needs-status`: statement or open-status evidence is insufficient, regardless of computational attractiveness.
- `needs-edge`: checker/baseline/search method is not yet demonstrated, regardless of source freshness.

A target card is not a result. The package contains no B1-B4 claim.
