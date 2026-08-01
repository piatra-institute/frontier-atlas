# Adversarial tests

`test_two_slice_formula.py` independently computes the tensor rank of every one of the 256 tensors in \(\mathbb F_2^2\otimes\mathbb F_2^2\otimes\mathbb F_2^2\) by breadth-first search over rank-one summands. It compares all values with the two-slice matrix-rank formula used in the orbit-5 certificate. This is an implementation sanity check, not a substitute for the proof of the formula given in `REPORT.md`.
