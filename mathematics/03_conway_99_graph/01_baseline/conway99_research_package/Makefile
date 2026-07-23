PYTHON ?= python
export PYTHONPATH := src

.PHONY: test cases examples audit hashes clean

test:
	$(PYTHON) -m unittest discover -s tests -v

cases:
	$(PYTHON) scripts/generate_cases.py

examples:
	$(PYTHON) scripts/generate_examples.py

audit: test cases examples
	$(PYTHON) scripts/run_audit.py
	$(PYTHON) scripts/hash_tree.py

hashes:
	$(PYTHON) scripts/hash_tree.py

clean:
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
	rm -rf build dist *.egg-info src/*.egg-info
