# Certified reproduction: CAN(2,8,3) = 13

This package contains an explicit \(\mathrm{CA}(13;2,8,3)\) and a completed exact enumeration proving that no \(\mathrm{CA}(12;2,8,3)\) exists.

## Headline status

- Result type: P2, independently reproduced known optimum.
- Exact value: \(\mathrm{CAN}(2,8,3)=13\).
- Upper certificate: explicit CSV array plus two independent full coverage scans.
- Lower certificate: seven normalized multiplicity cases, complete candidate graphs, and independently checked absence of \(K_6\) in every graph.
- Review level: agent.
- New mathematical record: no.

## Fast verification

From this directory:

```bash
./verify_all.sh
```

Expected final line:

```text
ALL_CHECKS_PASS
```

This verifies the immutable SHA-256 manifest, checks the 13-row construction twice, reconstructs all seven lower-bound cases independently, compares every candidate and edge, and recomputes every graph's maximum clique.

## Full regeneration

```bash
./reproduce.sh
```

This compiles `src/generate_certificate.cpp`, regenerates the array and lower-bound certificate, and then runs the independent verification suite. Generated logs are deliberately excluded from the immutable manifest because elapsed times vary.

## Key files

- `CLAIM.md`: exact audit claim and trust surface.
- `PROOF_NOTE.md`: human-readable proof of encoding completeness.
- `array_CA_13_2_8_3.csv`: upper-bound witness.
- `certificate/lower_bound_summary.json`: compact lower-bound result.
- `certificate/pattern_*_candidates.txt`: all canonical added-column candidates.
- `certificate/pattern_*_edges.txt`: complete compatibility graphs.
- `src/generate_certificate.cpp`: primary exact generator.
- `src/verify_lower_bound_independent.py`: independent reconstruction and Bron-Kerbosch verifier.
- `src/verify_coverage.py`: set-based coverage scanner.
- `src/verify_coverage_independent.cpp`: bitmask coverage scanner.
- `src/search_upper_CA13.py`: deterministic heuristic provenance only.
- `exploration_CAN_3_7_3/`: separate non-load-bearing attempt at the neighboring open cell.

## Trust model

The load-bearing computations use exact integer enumeration only. The heuristic search is not trusted. The encoding itself is small enough to audit directly from `PROOF_NOTE.md` and the two source implementations.
