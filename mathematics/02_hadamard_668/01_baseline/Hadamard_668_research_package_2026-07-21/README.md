# Hadamard order 668 research package

**Status: unresolved.** This archive does not contain a Hadamard matrix of order 668 and does not prove nonexistence.

It contains the strongest exact result preserved from the available execution: a cyclic Goethals-Seidel candidate with full periodic-autocorrelation defect score **1920**, compared in the report with a public checkpoint of **2496**. Under the same metric, the numerical improvement is 576 points, or 23.08 percent.

## Central result

- Four sign sequences of length 167: `candidate/best_GS_sequences_score1920.csv`
- Row sums: `(17, 17, 9, 3)`
- Equivalent SDS parameters: `(167; 75,75,79,82;144)`
- Exact target: every nonzero combined periodic autocorrelation equals zero
- Actual result: 39 of 83 independent shifts are nonzero
- Full defect score: `1920`
- Maximum absolute combined autocorrelation: `8`
- Full 668 x 668 Goethals-Seidel expansion: **not Hadamard**

## Exact local certificate preserved

Every fixed-row-sum state within Hamming distance at most 4 was reported as exhaustively checked:

| Class | States checked | Best neighbor score |
|---|---:|---:|
| One balanced swap | 27,722 | 2368 |
| One swap in each of two rows | 288,189,040 | 2688 |
| Two balanced swaps in one row | 46,882,338 | 2048 |
| **Total** | **335,099,100** | **2048** |

The preserved audit record concludes that no such state improves 1920, so the candidate is a strict fixed-row-sum local minimum through Hamming radius 4. This is not a global optimality result. The original enumeration source was not preserved; see `PACKAGE_STATUS.md`.

## Quick sequence verification

Python:

```bash
python3 verification/verify_sequences.py \
  candidate/best_GS_sequences_score1920.csv --json
```

C++:

```bash
c++ -O2 -std=c++17 verification/verify_sequences.cpp -o verify_sequences
./verify_sequences candidate/best_GS_sequences_score1920.csv
```

Both verifiers should report:

```text
shape=4x167
row_sums=[17,17,9,3]
full_score=1920
max_abs_paf=8
nonzero_unique=39
exact_complementary_quad=false
```

## Contents

- `source/02_hadamard_668_prompt.pdf`: original task prompt
- `report/Hadamard_668_research_report.pdf`: mathematical and computational report
- `report/Hadamard_668_research_report.docx`: editable report
- `candidate/best_GS_sequences_score1920.csv`: central sequence certificate
- `candidate/combined_periodic_autocorrelation.csv`: all 166 nonzero-shift values
- `candidate/metrics.json`: exact machine-readable candidate metrics
- `verification/verify_sequences.py`: strict Python verifier
- `verification/verify_sequences.cpp`: independent C++ verifier
- `verification/fixed_weight_hamming_radius4_audit.json`: preserved local-audit result
- `verification/matrix_level_audit.json`: direct 668 x 668 Gram-audit result
- `PACKAGE_STATUS.md`: scope and reproducibility limitations
- `MANIFEST.sha256`: checksums for every other package file

## Acceptance gate

A positive solution requires score 0, expansion to a 668 x 668 sign matrix, and exact verification of `H H^T = 668 I`. The archived candidate deliberately fails that gate and is labeled accordingly.
