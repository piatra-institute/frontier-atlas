# Certified P1 reproduction: \(R_{\mathbb F_2}(\langle2,2,3\rangle)=11\)

This package is one worked attempt under the Piatra Institute solver protocol. It fixes exactly one map, field, and measure:

- **map:** multiplication of a \(2\times2\) matrix by a \(2\times3\) matrix;
- **field:** \(\mathbb F_2\);
- **measure:** ordinary tensor rank / bilinear complexity, not border rank;
- **claim:** exact rank 11.

Run:

```bash
./verify_all.sh
```

Regenerate the finite substitution certificates independently, then byte-compare them with the preserved copies:

```bash
./reproduce_certificates.sh
```

## Audit surface

- `CLAIM.md`: exact proposition and trust base.
- `decomposition.json`, `ALGORITHM.md`, `verify_upper.py`: length-11 algorithm and exact checker.
- `orbits.json`, `certificates/`, `verify_lower.py`, `two_slice_rank9.cpp`: lower-bound certificate and independent verifier.
- `REPORT.md`: mathematical explanation, literature audit, limitations, and attempt denominator.
- `MANIFEST.sha256`: hashes of every preserved source, certificate, report, and log.

No numerical floating-point computation is used. The package contains no claim over \(\mathbb Q\) or \(\mathbb R\).
