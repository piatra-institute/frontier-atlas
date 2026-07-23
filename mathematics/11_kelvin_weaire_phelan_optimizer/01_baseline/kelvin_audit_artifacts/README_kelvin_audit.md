# Kelvin / Weaire-Phelan audit artifacts

## Files

- `kelvin_partial_resolution_dossier.md`: theorem statements, proof sketches, obstructions, and exact remaining gap.
- `verify_flat_a15.py`: exact symbolic certificate for the equal-volume flat A15/Laguerre competitor, plus an optional independent half-space reconstruction.
- `flat_a15_candidate.json`: machine-readable torus, site, weight, and exact area data.

## Run

```bash
python -m pip install sympy numpy scipy
python verify_flat_a15.py
```

The exact certificate uses SymPy. NumPy and SciPy are used only for an independent floating-point reconstruction of the two cell orbits.

## Scope

These artifacts do not certify the curved relaxed Weaire-Phelan foam and do not prove global optimality in the unrestricted Kelvin problem.
