# Reproduction commands

Tested environment:

- Python 3.13.5
- GCC/G++ 14.2.0
- GNU coreutils 9.7
- Linux x86-64

No third-party Python package is required.

```bash
unzip piatra_bilinear_rank_223_f2_attempt01.zip
cd piatra_bilinear_rank_223_f2_attempt01
./verify_all.sh
./reproduce_certificates.sh
```

`verify_all.sh` first validates `MANIFEST.sha256`, compiles the C++ rank-metric enumerator, runs the exhaustive 2x2x2 formula test, verifies all 144 upper-bound tensor coefficients and 1,024 inputs, reconstructs all 67 restriction subspaces and 11 symmetry orbits, and replays both finite substitution trees.
