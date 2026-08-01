.PHONY: verify-fast staircase lower manifest check-manifest

# Fast, deterministic, self-checking. Safe for CI.
verify-fast: staircase
	@echo "verify-fast: OK"

staircase:
	python3 src/verify_staircase.py

# Timed heuristic search (not deterministic across time budgets).
lower:
	python3 src/lower_bound_search.py 25

# Exact Farkas certificate: every 237-cap has a hyperplane slice >= 89.
floor:
	python3 src/verify_slice_floor.py

# Nonlocal 237-cap search (fixed size 237, minimize violated lines). Null so far.
lns:
	python3 src/cap_lns.py 300

# CP-SAT calibration of exact small caps (needs OR-tools). a(4) closes; a(5)/a(6) do not.
caps:
	python3 src/certify_small_caps.py 4,5,6 120

# Certified upper bounds with an independently checked DRAT proof.
# Needs cadical on PATH (brew install cadical). a(4) ~17s and VERIFIED; a(5) may not close.
sat: tools/drat-trim
	python3 src/sat_cap_bound.py $$(command -v cadical) tools/drat-trim proofs 2,3,4 300

tools/drat-trim: tools/drat-trim.c
	clang -O2 -o tools/drat-trim tools/drat-trim.c

manifest:
	find . -type f ! -name SHA256SUMS ! -name '.DS_Store' ! -name '*.drat' ! -path './tools/drat-trim' | LC_ALL=C sort | xargs shasum -a 256 > SHA256SUMS
	@echo "wrote SHA256SUMS"

check-manifest:
	shasum -a 256 -c SHA256SUMS
