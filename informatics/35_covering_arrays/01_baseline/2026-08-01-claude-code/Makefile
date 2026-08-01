.PHONY: verify search manifest check-manifest

# Independent exact coverage check of both arrays.
verify:
	python3 src/verify_ca.py data/CA_13_2_8_3.csv 2 8 3
	python3 src/verify_ca.py data/CA_39_3_7_3.csv 3 7 3

# Record attempt: search for CA(38;3,7,3) (best known 39). ~600 s; null so far (best 5 uncovered).
search:
	python3 src/ca_search.py 600 38

manifest:
	find . -type f ! -name SHA256SUMS ! -name '.DS_Store' | LC_ALL=C sort | xargs shasum -a 256 > SHA256SUMS
	@echo "wrote SHA256SUMS"

check-manifest:
	shasum -a 256 -c SHA256SUMS
