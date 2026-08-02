# Checker and baseline calibration report

All commands were run from the package root on 2026-08-02. These are B0/preflight results only.

| Checker | Positive/frontier result | Adversarial or near-miss result |
|---|---|---|
| Signed circulant | n=8 optimizer rho=2.326846269604655 equals target within 4.5e-16; full n=8..18 minima reproduced | all-positive n=8 has rho=4 and is not an optimizer |
| Triangle-free chi/Z | C5: chi=3, Z=2, equality | C6: chi=2, Z=2, strict inequality |
| Augmented Sombor | T6(3): ASO=27.712812921102042, equality | K3,2,1: ASO=25.3981..., strict |
| Total 2-coalition | K5 four-part certificate reaches bound 4 | five singleton parts fail coalition condition |
| LC condensation | P4-derived LC-equivalent pair remains equivalent after allowed condensation | alternate C fails the source-side condition |
| Arboreal bunkbed | K2, lambda=1: same weight 8, cross weight 6 | K2, lambda=0 rejected at the strict domain boundary |
| Prime powers | 24=8+16 | 23 is outside conjecture domain |
| Path zero-forcing polynomial | P6,k=2: z=12 equals path benchmark | C6,k=2: z=6 |
| UR edge coloring | valid P4 coloring accepted | invalid P4 coloring rejected |
| Coefficient log-concavity | [1,3,2] accepted | [1,1,2] rejected |
| Perfect matching | schema parsed | `full_checker_ready:false`; Sage/recomputation absent |
| Matroid Q/Y | matroid schema parsed | `full_checker_ready:false`; recurrence absent |
| Vine circuit rows | row metadata parsed | `full_checker_ready:false`; archive/circuit/Stim absent |
| FlowBoost | supplied n=4 target sequence matches | `full_checker_ready:false`; E_n not independently constructed |

## Signed-circulant B0 frontier

| n | switching classes | minimum | rho_-(n) | absolute error |
|---:|---:|---:|---:|---:|
| 8 | 512 | 2.326846269604655 | 2.3268462696046543 | <1e-15 |
| 10 | 2,048 | 2.4972120409568332 | 2.497212040956833 | <1e-15 |
| 12 | 8,192 | 2.594619588218836 | 2.5946195882188357 | <1e-15 |
| 14 | 32,768 | 2.6549797248797047 | 2.654979724879705 | <1e-15 |
| 16 | 131,072 | 2.694804747545855 | 2.694804747545853 | <2.3e-15 |
| 18 | 524,288 | 2.7224022714892406 | 2.72240227148924 | <1e-15 |

The exact-root mode isolates the spectral radius of a supplied integer signed-adjacency matrix. A future claimed counterexample must have a gap safely larger than both the rational root interval and high-precision target uncertainty.


## Execution records

- `calibration/SIGNED_BASELINE_TIMED_2026-08-02.log`: full signed-circulant n=8..18 replay.
- `calibration/SIGNED_BASELINE_TIMED_2026-08-02.time`: `real 24.20`, `user 24.28`, `sys 0.30` seconds on the scout host.
- `calibration/FULL_RUN_2026-08-02.log`: first calibration batch; the surrounding tool invocation reached its 180-second envelope during a later LC near-miss run, after the signed frontier and preceding cases had completed.
- `calibration/CONTINUATION_2026-08-02.log`: continuation from that point through all remaining cases and malformed-input rejection; exit status 0.

The split logs reflect the execution envelope, not a checker disagreement.


## Signed-circulant search-edge preflight (no witness search)

Command:

```bash
python checkers/benchmark_signed_dihedral.py 8 10 12 14 16 18
```

| n | switching classes | dihedral orbits | reduction factor | Burnside cross-check |
|---:|---:|---:|---:|:---:|
| 8 | 512 | 60 | 8.53x | pass |
| 10 | 2,048 | 156 | 13.13x | pass |
| 12 | 8,192 | 448 | 18.29x | pass |
| 14 | 32,768 | 1,374 | 23.85x | pass |
| 16 | 131,072 | 4,500 | 29.13x | pass |
| 18 | 524,288 | 15,370 | 34.11x | pass |

The script also samples representatives under every tested order and verifies spectral-radius invariance under the induced dihedral action. This benchmarks a representation reduction only; it does not evaluate any new n or search for a witness. Raw output and timing are in `calibration/SIGNED_DIHEDRAL_BENCHMARK_2026-08-02.json` and `.time`.
