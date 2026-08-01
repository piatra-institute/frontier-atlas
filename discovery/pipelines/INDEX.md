# Discovery pipelines index

Each pipeline is one ChatGPT Pro sandbox session that generates many candidate claims over a
class of conjectures, adversarially breaks them against structured families, and returns
refutations plus survivors. Method and verification discipline follow
`../graph_conjectures/PROMPT.md` (generator is not verifier; recompute every invariant
independently; no fabricated citations; report the denominator = generated / broken / survived).

Richness = prior likelihood a session yields a clean refutation (explicit witness).
**high** = hundreds of published bounds, many false, tiny witnesses; **med** = real open
conjectures, refutation plausible but bounds mostly hold; **low** = valuable but witnesses are
heavier to certify or the class rarely cracks at session scale.

| # | slug | one-line | target class | richness |
|---|------|----------|--------------|----------|
| 00 | `../graph_conjectures` | generic graph-invariant inequalities (the seed pipeline) | graph invariants | high |
| 01 | `01_zagreb_degree_indices` | Zagreb / forgotten / irregularity degree-index bounds | chemical/topological index | high |
| 02 | `02_randic_abc_connectivity` | Randic / ABC / geometric-arithmetic bounds, ABC-minimal trees | chemical/topological index | high |
| 03 | `03_sombor_family_indices` | Sombor and its 2021+ variants (freshest, most fragile) | chemical/topological index | high |
| 04 | `04_distance_based_indices` | Wiener / Szeged / Mostar / PI / eccentric bounds | distance-based invariant | high |
| 05 | `05_adjacency_spectral_bounds` | spectral radius / spread / gap / nullity inequalities | spectral | high |
| 06 | `06_laplacian_spectral_bounds` | Brouwer, signless-Laplacian, Laplacian-energy bounds | spectral | med |
| 07 | `07_distance_spectrum_bounds` | distance spectral radius / energy (Aouchiche-Hansen) | spectral / distance | med |
| 08 | `08_spectral_characterization_ds` | cospectral mates, determined-by-spectrum witnesses | spectral | med |
| 09 | `09_domination_inequalities` | domination / total / Roman / independent bounds (TxGraffiti) | domination | high |
| 10 | `10_chromatic_inequalities` | Reed, Borodin-Kostochka chromatic bounds | coloring | med |
| 11 | `11_coloring_variants` | list / total / AVD / game chromatic conjectures | coloring | med |
| 12 | `12_matching_independence_bounds` | independence / matching / residue / annihilation (Graffiti) | matching/independence | high |
| 13 | `13_nordhaus_gaddum` | f(G)+f(complement) sum/product relations | graph invariants | high |
| 14 | `14_graph_product_invariants` | Vizing / product inequalities (Hedetniemi refuted precedent) | graph products | med |
| 15 | `15_digraph_tournament` | Seymour 2nd-neighbourhood, Caccetta-Haggkvist, tournaments | digraph/tournament | med |
| 16 | `16_hypergraph_cover_matching` | Ryser, Erdos matching, hypergraph coloring | hypergraph | med |
| 17 | `17_poset_lattice_inequalities` | 1/3-2/3, linear-extension, log-concavity | poset/lattice | med |
| 18 | `18_matroid_conjectures` | Rota, White, Ingleton, log-concavity (small matroids) | matroid | low |
| 19 | `19_permutation_statistics` | Wilf-equivalence, equidistribution, stack-sorting | permutation statistic | med |
| 20 | `20_oeis_conjectured_properties` | first-failure of conjectured OEIS sequence properties | OEIS sequences | high |
| 21 | `21_additive_small_sets` | MSTD / Sidon / Davenport / sum-free small sets | additive combinatorics | med |
| 22 | `22_polytope_fvector_flag` | Kalai 3^d, flag-f, h*-unimodality | polytope f-vector/flag | low |
| 23 | `23_finite_geometry_incidence` | orchard / ordinary-lines / arcs / blocking sets | finite geometry | med |
| 24 | `24_boolean_function_complexity` | sensitivity / bs / degree / certificate gaps | Boolean function | med |
| 25 | `25_automaton_language` | Cerny reset bound, state complexity of operations | automaton/language | med |
| 26 | `26_combinatorial_game_values` | Grundy-sequence periodicity of heap games | combinatorial game | low |
| 27 | `27_small_group_algebra` | group-invariant inequalities over GAP SmallGroups | group/algebra | med |
| 28 | `28_knot_braid_invariants` | invariant-relation conjectures over KnotInfo | knot/braid | low |
| 29 | `29_design_existence_sweep` | resolve small design existence "?" cells | design existence | med |
| 30 | `30_graph_energy_unified` | energy / Estrada / LEL bounds, equienergetic pairs | spectral / energy | high |

## Notes on richness

- **Highest yield (01-04, 09, 12, 13, 20, 30).** Chemical/topological and energy indices are the
  richest vein: hundreds of published inequalities, many stated for trees only and false in
  general, all with sub-10-vertex witnesses checkable exactly in milliseconds. Sombor (03) is the
  freshest (post-2021) and least stress-tested. OEIS mining (20) and TxGraffiti/Graffiti bounds
  (09, 12) are machine-generated conjectures never hardened against structured families.
- **Lower yield but kept (18, 22, 26, 28).** These target genuinely open, well-cited questions but
  the checker is heavier or the class rarely cracks at session scale: matroid conjectures need
  axiom re-verification and grow explosively past n=9; polytope witnesses need a realizability
  certificate; game non-periodicity is not finitely provable (only period-breaks and certified
  extensions are clean wins); knot invariants require per-knot recomputation (still seconds each).
  Included because a single hit is a real result and the search cost is low.

## Classes considered and folded / dropped

- **Ramsey / van der Waerden / cap set / superpermutation / sorting-network / tensor-rank** —
  excluded by scope: hardened records a dedicated community already grinds.
- **Lattice (order-theoretic) inequalities** folded into `17_poset_lattice_inequalities` rather than
  a separate pipeline — same enumeration source and checker.
- **Braid-group invariants** folded into `28_knot_braid_invariants`; a standalone braid pipeline was
  judged too thin (most braid questions reduce to knot/link invariants already covered).
- **Ehrhart / lattice-point identities** folded into `22_polytope_fvector_flag` via the h*-vector.
- A separate **"algebra" pipeline** (rings, non-associative algebras) was dropped: small-case
  witnesses exist but openness is hard to document from a single citable table, and the strongest
  algebra targets (finite groups) are already covered by `27_small_group_algebra`.
