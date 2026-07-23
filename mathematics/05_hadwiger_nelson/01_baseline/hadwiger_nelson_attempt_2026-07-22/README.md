# Hadwiger-Nelson research package

This package records an exact partial result from a research attempt dated 22 July 2026. It does not claim to determine the chromatic number of the plane.

## Main certified statement

For the supplied exact 510-vertex unit-distance graph, every nonedge pair is color-flexible across the supplied proper 5-colorings: one certificate row colors the pair equally and another colors it differently.

Consequently, neither the full graph nor any subgraph obtained only by deletion can be a nontrivial two-terminal forced-color gadget on one of its nonedges.

Read `REPORT.md` for the mathematical argument and exact remaining gap.

## Files

- `REPORT.md`: research result, reduction lemma, audit, and next steps.
- `verify_all.py`: exact geometry and coloring-certificate verifier.
- `verify_coloring.cpp`: independent C++ verifier for coloring validity and pair coverage.
- `data/510.vtx`: exact coordinate expressions.
- `data/510.edge`: listed graph edges.
- `certificates/colorings_84.csv`: compact constructive certificate.
- `certificates/special_pair_witness_rows.json`: witnesses for the golden-ratio pairs.
- `metadata.json`: machine-readable summary.
- `MANIFEST.sha256`: hashes of all packaged files except the manifest itself.

## Verify

```bash
python -m pip install -r requirements.txt
python verify_all.py
```

Optional independent coloring check:

```bash
g++ -O2 -std=c++17 verify_coloring.cpp -o verify_coloring
./verify_coloring data/510.edge certificates/colorings_84.csv
```
