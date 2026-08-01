.PHONY: upper strassen manifest check-manifest

# Independent upper bound: 11-product algorithm over all 1024 inputs (no solver).
upper:
	python3 src/upper_recheck.py

# Validate the SAT lower-bound method: prove Strassen R_F2(<2,2,2>) >= 7 (drat-trim VERIFIED).
strassen: tools/drat-trim
	python3 src/sat_bilinear_lb.py $$(command -v cadical) tools/drat-trim proofs 2 2 2 6 120

tools/drat-trim: tools/drat-trim.c
	clang -O2 -o tools/drat-trim tools/drat-trim.c

manifest:
	find . -type f ! -name SHA256SUMS ! -name '.DS_Store' ! -name '*.drat' ! -path './tools/drat-trim' | LC_ALL=C sort | xargs shasum -a 256 > SHA256SUMS
	@echo "wrote SHA256SUMS"

check-manifest:
	shasum -a 256 -c SHA256SUMS
