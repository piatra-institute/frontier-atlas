# Piatra Institute - Mathematics Research Program

Fifty open problems in combinatorics, discrete geometry, number theory, and algebra, selected for tractability by SOTA reasoning models: certified/SAT search, exact enumeration, symbolic mining, computer-assisted proof, bound optimization. The signature: finite or algebraic structure with machine-checkable ground truth.

Problems 01-11 are the original sprint (July 2026), each carrying a full research package (report, source, certificates, independent verifiers, SHA-256 manifests). Problems 12-50 each carry a `prompt.md` (in `01_baseline`) following `PROMPT_TEMPLATE.md`. See `STRATEGY.md` for selection criteria and doctrine.

Mode tags: `[search]` certified/SAT construction or bound · `[cert]` computer-assisted proof (DRAT, interval arithmetic, Lean) · `[enum]` exhaustive isomorph-free enumeration · `[sym]` symbolic/CAS mining · `[opt]` rigorous bound optimization · `[proof]` short-argument / counterexample hunting.

## Original eleven (01-11) - packaged results

| # | Folder | Problem | Status |
|---|--------|---------|--------|
| 01 | `01_ramsey_R5_5` | Diagonal Ramsey number R(5,5) | partial (certified reductions) |
| 02 | `02_hadamard_668` | Hadamard matrix of order 668 | partial (near-miss, no existence) |
| 03 | `03_conway_99_graph` | Conway's 99-graph | partial (84×84 reduction) |
| 04 | `04_projective_plane_12` | Projective plane of order 12 | partial (coding-theory constraints) |
| 05 | `05_hadwiger_nelson` | Chromatic number of the plane | partial (G510 flexibility theorem) |
| 06 | `06_kissing_number_11` | Kissing number in dimension 11 | partial (verified 604 construction) |
| 07 | `07_moore_graph_degree_57` | Moore graph of degree 57 | partial (PSL(3,4) extension branches) |
| 08 | `08_lonely_runner` | Lonely runner conjecture | partial (grid-obstruction certificate) |
| 09 | `09_union_closed_sets` | Union-closed sets conjecture | prompt only |
| 10 | `10_jacobian_dimension_2` | Jacobian conjecture, dimension 2 | prompt only |
| 11 | `11_kelvin_weaire_phelan_optimizer` | Kelvin / Weaire-Phelan foam | partial (frustration-gap dossier) |

## New thirty-nine (12-50) - prompts ready

### Ramsey, Schur & van der Waerden - SAT-shaped siblings of R(5,5)
| # | Folder | Problem | Modes |
|---|--------|---------|-------|
| 12 | `12_schur_number_6` | Schur number S(6) (S(5)=160 via SAT) | search, cert |
| 13 | `13_ramsey_r46` | Two-colour Ramsey R(4,6) | search |
| 14 | `14_ramsey_r3k` | Ramsey R(3,10) and the R(3,k) ladder | search |
| 15 | `15_ramsey_multicolor_3333` | Multicolour Ramsey R(3,3,3,3) | search |
| 16 | `16_van_der_waerden_w27` | Van der Waerden number W(2,7) | search |

### Additive & combinatorial number theory - siblings of lonely runner
| # | Folder | Problem | Modes |
|---|--------|---------|-------|
| 17 | `17_cap_set_n7` | Maximum cap in AG(7,3) | search |
| 18 | `18_erdos_straus` | Erdős-Straus conjecture (4/n) | search, proof |
| 19 | `19_postage_stamp_bases` | Postage-stamp problem / extremal additive bases | search |
| 20 | `20_sidon_difference_families` | Sidon sets & perfect difference families | search |
| 21 | `21_singmaster` | Singmaster's multiplicity conjecture | proof, search |

### Discrete & combinatorial geometry - siblings of kissing-11 / Kelvin
| # | Folder | Problem | Modes |
|---|--------|---------|-------|
| 22 | `22_heilbronn_triangle` | Heilbronn triangle problem | opt, search |
| 23 | `23_borsuk_conjecture` | Smallest dimension where Borsuk fails | search |
| 24 | `24_tammes_problem` | Tammes problem for open N | cert, opt |
| 25 | `25_reinhardt_octagon` | Reinhardt conjecture (smoothed octagon) | opt |
| 26 | `26_circle_packing` | Optimal circle packing for open N | opt, cert |
| 27 | `27_no_three_in_line` | No-three-in-line problem | search |

### Graph theory - siblings of Conway-99 / Moore-57
| # | Folder | Problem | Modes |
|---|--------|---------|-------|
| 28 | `28_srg_existence` | Strongly regular graphs, open feasible parameters | search, enum |
| 29 | `29_cage_orders` | Missing cage orders, e.g. (3,11)-cage | search |
| 30 | `30_zarankiewicz_crossing` | Zarankiewicz crossing-number conjecture | search, opt |
| 31 | `31_guy_crossing_kn` | Guy's conjecture, crossing number of Kₙ | search |
| 32 | `32_second_neighborhood` | Seymour's second-neighbourhood conjecture | proof |
| 33 | `33_graceful_labeling` | Graceful/harmonious tree labelings | search |

### Designs & codes - siblings of Hadamard-668 / projective-plane-12
| # | Folder | Problem | Modes |
|---|--------|---------|-------|
| 34 | `34_mols_order_10` | MOLS of order 10 (is N(10) ≥ 3?) | search |
| 35 | `35_optimal_binary_codes` | Optimal binary codes A(n,d), open values | search, opt |
| 36 | `36_covering_codes_football_pool` | Covering codes / football-pool K(n,3) | search |
| 37 | `37_costas_arrays` | Costas arrays at the smallest open order | search |
| 38 | `38_maximal_determinant` | Maximal ±1 determinant, orders ≢ 0 (mod 4) | search, opt |
| 39 | `39_steiner_systems` | Small Steiner systems / t-designs | search, enum |

### Number theory & algebra - siblings of the Jacobian conjecture
| # | Folder | Problem | Modes |
|---|--------|---------|-------|
| 40 | `40_lehmer_mahler_measure` | Lehmer's problem (smallest Mahler measure > 1) | opt, sym |
| 41 | `41_casas_alvero` | Casas-Alvero conjecture | sym, cert |
| 42 | `42_markov_uniqueness` | Markov uniqueness (Frobenius) conjecture | proof |
| 43 | `43_alon_tarsi` | Alon-Tarsi conjecture (Latin squares) | sym |
| 44 | `44_rota_basis` | Rota's basis conjecture | search |
| 45 | `45_erdos_moser` | Erdős-Moser equation | search, sym |

### Order theory, extremal set systems & misc - siblings of union-closed
| # | Folder | Problem | Modes |
|---|--------|---------|-------|
| 46 | `46_one_third_two_thirds` | The 1/3-2/3 conjecture for posets | proof, search |
| 47 | `47_ryser_brualdi_stein` | Ryser-Brualdi-Stein transversal conjecture | search, proof |
| 48 | `48_sunflower_conjecture` | Sunflower conjecture (close the constant) | proof |
| 49 | `49_kobon_triangles` | Kobon triangle problem | search |
| 50 | `50_thomson_problem` | Thomson problem for open N | opt, cert |

## Working protocol

Every session runs under the atlas `SOLVER.md` (agency, compute, adversarial self-verification).
1. **Pick** a problem; the strongest machine-checkable starting points are 12 (Schur S(6)), 17 (cap set n=7), 27 (no-three-in-line), 34 (MOLS(10)), 38 (maximal determinant), and 28 (SRG existence).
2. **Re-verify** current status first; several nearby problems fell in 2019-2024 (Erdős-Faber-Lovász, the sensitivity conjecture, Kaplansky's unit conjecture, possibly Gerver's moving-sofa optimality).
3. **Seed** a SOTA session with the attempt's `prompt.md`.
4. **Preserve** the transcript as `chat.md`.
5. **Require** a self-contained package matching the 01-11 standard: report, source, certificates, independent verifiers, SHA-256 manifest. Search source is part of the record.
6. **Report** honestly whether the resolution standard was met; certified partial results are the expected product.
7. **Leave** a `NEXT_STEPS.md` when pausing a line.

Sister programs: `research/frontier-atlas/physics` (50 problems) and `research/frontier-atlas/chembiotics` (50 problems, split into closed-loop and reality-gated packs).
