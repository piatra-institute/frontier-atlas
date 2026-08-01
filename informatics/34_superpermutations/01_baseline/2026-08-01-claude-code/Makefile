.PHONY: build manifest check-manifest

# Reproduce the greedy superpermutation and verify it (validates n=1..5 optima too).
build:
	python3 src/superperm.py 6

manifest:
	find . -type f ! -name SHA256SUMS ! -name '.DS_Store' | LC_ALL=C sort | xargs shasum -a 256 > SHA256SUMS
	@echo "wrote SHA256SUMS"

check-manifest:
	shasum -a 256 -c SHA256SUMS
