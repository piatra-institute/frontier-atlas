# Ramsey R(5,5) research package

Start with `R55_RESEARCH_REPORT.pdf` or `RESEARCH_REPORT.md`.

## What is certified

Using the supplied official collection of 328 known 42-vertex representatives:

- all 328 records independently verify as `(5,5)`-Ramsey graphs;
- none has an exact one-vertex Ramsey extension;
- none has an extension with at most one monochromatic `K5`;
- exactly representatives 41 and 255 have extensions with at most two monochromatic `K5`s;
- those extensions form exactly two unlabeled 43-vertex near-miss classes;
- no 43-vertex Ramsey graph is within five edge flips of near-miss Graph 1.

The package **does not determine** `R(5,5)`. The known 42-vertex collection is not a proved complete catalogue.

## Package map

- `R55_RESEARCH_REPORT.pdf`: seven-page human-readable report;
- `RESEARCH_REPORT.md`: source report with formulas and reproduction commands;
- `VERIFICATION_LOG.md`: completed independent-replay totals;
- `data/`: graph6 collection and two near-miss adjacency matrices;
- `proofs/`: DRUP certificates and per-family manifests;
- `src/`: generators, exact analyzers, and independent proof checkers;
- `results/`: machine-readable summaries and the package integrity audit;
- `SHA256SUMS.txt`: checksum for every distributed file other than itself.

## Reproduce the independent checks

Run from `src/`:

```bash
python check_extension_proofs.py \
  --graphs ../data/r55_42some.g6 \
  --proof-dir ../proofs

g++ -O3 -std=c++17 -o check_one_bad_drup check_one_bad_drup.cpp
./check_one_bad_drup ../data/r55_42some.g6 ../proofs/one_bad 0 328

g++ -O3 -std=c++17 -o check_two_bad_drup check_two_bad_drup.cpp
./check_two_bad_drup ../data/r55_42some.g6 ../proofs/two_bad 0 328

g++ -O3 -std=c++17 -o check_near_radius_drup check_near_radius_drup.cpp
./check_near_radius_drup \
  ../data/near43_graph1.matrix \
  ../proofs/near_radius_seq 5

python audit_package.py
```

Python generators require the packages listed in `requirements.txt`; the independent exact-extension checker uses only the Python standard library, and the C++ replay checkers require only a C++17 compiler.
