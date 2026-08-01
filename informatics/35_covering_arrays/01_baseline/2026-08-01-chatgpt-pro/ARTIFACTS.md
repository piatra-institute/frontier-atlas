# Artifact map

## Claim surface

- `CLAIM.md`: precise proposition, checker command, trust base, encoding fidelity, provenance, and cost.
- `PROOF_NOTE.md`: mathematical reduction from a hypothetical \(\mathrm{CA}(12;2,8,3)\) to a \(K_6\) in one of seven finite graphs.
- `PRIOR_ART.md`: literature and table-status check as of 2026-08-01.

## Upper certificate

- `array_CA_13_2_8_3.csv`: explicit 13-row witness.
- `certificate/upper_coverage_counts.csv`: multiplicity of every ordered pair in every column pair.
- `src/verify_coverage.py`: independent set-based scanner.
- `src/verify_coverage_independent.cpp`: independent bitmask scanner.
- `src/search_upper_CA13.py`: deterministic heuristic provenance, not load-bearing.

## Lower certificate

- `certificate/lower_bound_summary.json`: seven cases and exact graph statistics.
- `certificate/multiplicity_patterns.csv`: canonical pair-frequency matrices and orbit sizes.
- `certificate/pattern_*_candidates.txt`: complete vertex lists.
- `certificate/pattern_*_edges.txt`: complete edge lists.
- `src/generate_certificate.cpp`: exact primary enumeration.
- `src/verify_lower_bound_independent.py`: independent exact reconstruction and maximal-clique enumeration.

## Reproduction and integrity

- `verify_all.sh`: integrity and independent verification entry point.
- `reproduce.sh`: full certificate regeneration and verification.
- `ARTIFACT_MANIFEST.sha256`: immutable-file checksums.
- `TOOL_VERSIONS.txt`: recorded toolchain.
- `logs/`: replay logs, excluded from the immutable manifest because times vary.

## Non-load-bearing exploration

- `exploration_CAN_3_7_3/`: valid 39-row strength-3 witness plus an unsuccessful, explicitly uncertified 38-row search branch.
