# Reproduction environment

Scout host calibration used:

- Python 3.13.5
- networkx 3.6.1
- numpy 2.3.5
- sympy 1.14.0
- PyYAML 6.0.3

Install the core environment with:

```bash
python -m pip install -r requirements.txt
```

SageMath and Stim are intentionally not core requirements. Cards whose complete checker would require them retain red gate 5, and their preflight scripts print `full_checker_ready: false` when the dependency or source artifact is absent.
