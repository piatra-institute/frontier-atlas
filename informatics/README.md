# Piatra Institute - Informatics Research Program

Fifty open problems in theoretical computer science, selected for tractability by SOTA reasoning models: certified/SAT search, exhaustive enumeration, symbolic/algebraic computation, computer-assisted proof, bound optimization. The signature: crisp cost measures with machine-checkable ground truth. Scoped to complexity, algorithms, automated reasoning, and quantum computation, avoiding the combinatorics/designs/classical-codes territory of the mathematics program.

Each attempt's `prompt.md` follows `PROMPT_TEMPLATE.md`. See `STRATEGY.md` for selection criteria and doctrine. Mode tags: `[search]` certified/SAT search · `[cert]` computer-assisted proof · `[enum]` exhaustive enumeration · `[sym]` symbolic/algebraic · `[opt]` bound optimization · `[proof]` short-argument / counterexample hunting.

## Index

### A. Exact algorithm optima & bilinear complexity
| # | Folder | Problem | Modes |
|---|--------|---------|-------|
| 01 | `01_sorting_networks` | Optimal sorting networks (size & depth) beyond known n | search, cert |
| 02 | `02_sorting_comparisons` | Minimum comparisons to sort n elements | search |
| 03 | `03_matrix_mult_rank` | Tensor rank of small matrix multiplication (3×3, …) | sym, search |
| 04 | `04_addition_chains` | Shortest addition chains / Scholz-Brauer | search |
| 05 | `05_bilinear_complexity` | Bilinear complexity of small bilinear maps | sym |
| 06 | `06_boolean_circuit_size` | Minimum circuit/formula size for explicit functions | search |
| 07 | `07_matrix_rigidity` | Explicit matrix rigidity, small cases | sym, search |

### B. Boolean & cryptographic functions
| # | Folder | Problem | Modes |
|---|--------|---------|-------|
| 08 | `08_apn_permutation` | APN permutation in even dimension (big APN problem) | search |
| 09 | `09_max_nonlinearity_odd` | Max nonlinearity in odd dimension (covering radius of RM(1,n)) | search, opt |
| 10 | `10_bent_classification` | Bent / almost-bent function classification | enum, search |
| 11 | `11_low_diff_uniformity` | Optimal differentially-uniform permutations (S-boxes) | search |
| 12 | `12_algebraic_immunity` | Boolean functions with optimal algebraic immunity | search |
| 13 | `13_resilient_functions` | Optimal correlation-immune / resilient functions | search |
| 14 | `14_planar_functions` | Planar / perfect-nonlinear functions | search, sym |
| 15 | `15_complete_mappings` | Complete mappings / orthomorphisms of groups | search, enum |

### C. Complexity separations & communication/query
| # | Folder | Problem | Modes |
|---|--------|---------|-------|
| 16 | `16_log_rank` | Log-rank conjecture, small-case exact communication complexity | search, opt |
| 17 | `17_sensitivity_separations` | Sensitivity vs block-sensitivity / degree exact separations | search, proof |
| 18 | `18_query_separations` | Quantum vs classical query separations, small functions | search |
| 19 | `19_exact_query_complexity` | Exact randomized/quantum query complexity, small functions | search |
| 20 | `20_formula_lower_bounds` | Formula-size lower bounds for explicit small functions | search, cert |
| 21 | `21_monotone_complexity` | Monotone circuit complexity exact values | search |
| 22 | `22_proof_complexity` | Minimum resolution-proof size for specific tautologies | cert, search |

### D. Computation models, automated reasoning & decidability frontiers
| # | Folder | Problem | Modes |
|---|--------|---------|-------|
| 23 | `23_busy_beaver` | Busy beaver BB(6) frontier and variants | cert, search |
| 24 | `24_universal_turing_machine` | Smallest universal Turing machine | search |
| 25 | `25_wang_tiles` | Smallest aperiodic tile sets & variants | search, cert |
| 26 | `26_post_correspondence` | Smallest undecidable PCP instances | search |
| 27 | `27_tag_systems` | Small tag / cyclic-tag halting frontiers | search |
| 28 | `28_rewriting_termination` | Open term-rewriting termination problems | cert |
| 29 | `29_state_complexity` | Exact state complexity of automaton operations | search, enum |
| 30 | `30_universal_cellular_automaton` | Smallest intrinsically universal cellular automaton | search |

### E. Discrete dynamics & pattern search
| # | Folder | Problem | Modes |
|---|--------|---------|-------|
| 31 | `31_life_spaceships` | Smallest Life spaceship of a given speed / open velocities | search |
| 32 | `32_life_oscillators` | Life oscillators of open periods / minimal cost | search |
| 33 | `33_gardens_of_eden` | Smallest orphan patterns (Gardens of Eden) | search, enum |
| 34 | `34_superpermutations` | Shortest superpermutation of n symbols | search, opt |
| 35 | `35_covering_arrays` | Optimal covering array numbers CAN(t,k,v) | search, opt |

### F. Quantum computation & codes
| # | Folder | Problem | Modes |
|---|--------|---------|-------|
| 36 | `36_t_count_synthesis` | Optimal T-count for specific unitaries | search, cert |
| 37 | `37_clifford_cnot_synthesis` | Optimal CNOT / Clifford circuit synthesis | search |
| 38 | `38_quantum_code_parameters` | Best ((n,K,d)) quantum-code parameters | search, opt |
| 39 | `39_quantum_mds_codes` | Quantum MDS / specific quantum-code existence | search, sym |
| 40 | `40_magic_state_distillation` | Optimal small magic-state distillation protocols | search |
| 41 | `41_stabilizer_rank` | Stabilizer rank of |T⟩^⊗n and specific states | search, opt |
| 42 | `42_quantum_query_complexity` | Exact quantum query complexity, small functions | search |
| 43 | `43_quantum_circuit_lower_bounds` | Gate-count lower bounds for specific operators | search, cert |

### G. Search, sequences & games
| # | Folder | Problem | Modes |
|---|--------|---------|-------|
| 44 | `44_superstrings_debruijn` | Shortest superstrings / de Bruijn optimizations | search |
| 45 | `45_coin_weighing` | Combinatorial search (Rényi-Ulam / group testing) exact bounds | search |
| 46 | `46_selection_networks` | Optimal selection & merging networks | search, cert |
| 47 | `47_arithmetic_circuits` | Minimal arithmetic circuits (FFT / multiplication / linear maps) | sym, search |
| 48 | `48_octal_games_periodicity` | Periodicity of octal games (Grundy sequences) | search |
| 49 | `49_cerny_synchronizing` | Černý conjecture / shortest reset words | search, cert |
| 50 | `50_pattern_avoidance` | Repetition thresholds / power-free word frontiers | search |

## Working protocol

Every session runs under the atlas `SOLVER.md` (agency, compute, adversarial self-verification).
1. **Pick** a problem; the strongest machine-checkable starting points are 01 (sorting networks), 08 (APN permutation), 23 (busy beaver), 34 (superpermutations), 36 (T-count), and 49 (Černý reset words).
2. **Re-verify** current status first; CS records move fast (busy beaver, matrix-multiplication decompositions, sorting networks, and Life constructions shifted in 2023-2025; BB(5) was settled in 2024).
3. **Seed** a SOTA session with the attempt's `prompt.md`.
4. **Preserve** the transcript as `chat.md`.
5. **Require** a self-contained, auditable package: report, source, certificates, independent verifiers, SHA-256 manifest. Search source is part of the record.
6. **Report** honestly whether the resolution standard was met; certified partial results (a new record with a proof trace, an exact value, a matching lower bound) are the expected product.
7. **Leave** a `NEXT_STEPS.md` when pausing a line.

Sister programs: `physics`, `mathematics`, and `chembiotics` (see the top-level `frontier-atlas/README.md`).
