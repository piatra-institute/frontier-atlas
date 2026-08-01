# Hunts: theoretical CS and discrete dynamics

Specific witness hunts. Each is one-sided: a single small explicit object resolves it, and a checker validates that object exactly in seconds. Not a proof program; the win is the object.

**Win-type:** EX existence witness · CE counterexample to a for-all/never claim · REC object beating a loose record (one-sided bound) · PER finite periodicity certificate.

**Openness:** "open" = openness documented and cross-checked here; "open (verify)" = real open area but the *exact* target cell/record must be re-confirmed against the live source before a session (records and object zoos drift weekly).

| # | slug | one-line | win | openness |
|---|------|----------|-----|----------|
| 01 | life_strictly_volatile_oscillator | Life strictly volatile oscillator at a period with none known (e.g. p7) | EX | open (verify period) |
| 02 | life_new_velocity_spaceship | Life spaceship of an unrealized velocity | EX | open |
| 03 | life_open_period_spaceship | Life spaceship of a period with no known example | EX | open (verify period) |
| 04 | life_true_period_gun | Life true-period glider gun at an open period | EX | open (verify period) |
| 05 | life_no_known_synthesis | Glider synthesis of a Life object that has none | EX | open (verify object) |
| 06 | life_smaller_orphan | Garden-of-Eden orphan smaller than the record | REC | open (verify record) |
| 07 | life_period_rake | Life rake of an open period/velocity | EX | open (verify) |
| 08 | life_oblique_spaceship | Elementary oblique Life ship of a new slope | EX | open |
| 09 | highlife_open_spaceship | HighLife (B36/S23) ship/oscillator of an open velocity/period | EX | open (verify gap) |
| 10 | nontotalistic_open_ship | Isotropic non-totalistic rule ship at an open velocity | EX | open (verify gap) |
| 11 | generations_open_ship | Generations-rule (StarWars/Brian's Brain) ship at open speed | EX | open (verify gap) |
| 12 | larger_than_life_ship | Larger-than-Life bug at an open velocity | EX | open (verify gap) |
| 13 | turmite_highway | Turmite highway/cycle for an unclassified table | EX | open (verify entry) |
| 14 | life_methuselah_longevity | Small Life pattern beating the methuselah record | REC | open (verify record) |
| 15 | rule110_family_glider | New glider/collision in Rule 110 / a 1D CA | EX | open (verify catalogue) |
| 16 | hexagonal_ca_ship | Hex/triangular-lattice CA ship at an open velocity | EX | open (verify gap) |
| 17 | apn_permutation_dim8 | APN permutation in dimension 8 (Big APN problem) | EX | open |
| 18 | apn_function_dim9 | New CCZ-class APN function in dim 9/10 | EX | open |
| 19 | max_nonlinearity_n15 | Boolean function beating best nonlinearity, odd n | REC | open |
| 20 | costas_array_order32 | Costas array of order 32 (or 33) | EX | open |
| 21 | rotation_symmetric_bent | Rotation-symmetric / homogeneous bent function, open n | EX | open (verify n) |
| 22 | resilient_nonlinearity | Resilient function at an open nonlinearity target | REC | open (verify cell) |
| 23 | planar_semifield | New planar function / commutative semifield, open order | EX | open (verify order) |
| 24 | algebraic_immunity_optimal | Optimal-immunity function with record nonlinearity | REC | open (verify cell) |
| 25 | cerny_extremal_dfa | New synchronizing automaton meeting (n-1)^2 | EX | open |
| 26 | slowly_synchronizing_series | Automaton beating the known slow-reset series | REC | open (verify record) |
| 27 | state_complexity_witness | Witness meeting an open worst-case state complexity | REC | open (verify cell) |
| 28 | partial_automaton_reset | Carefully-synchronizing PFA with record reset word | REC | open (verify record) |
| 29 | pcp_hard_instance | Small PCP instance with record-long shortest solution | REC | open (verify record) |
| 30 | tag_system_halting | Halting/periodicity witness for an open tag system | EX | open (verify instance) |
| 31 | rewriting_nontermination_loop | Non-termination loop for an open TPDB rewriting system | CE | open (verify instance) |
| 32 | octal_treblecross_period | Period of Treblecross, octal game 0.007 | PER | open |
| 33 | grundy_game_period | Period of Grundy's game / an unsettled octal game | PER | open |
| 34 | superpermutation_n7 | Superpermutation of 7 symbols shorter than 5906 | REC | open |
| 35 | sorting_network_n13 | 13-input sorting network below 46 comparators | REC | open |
| 36 | addition_chain_scholz | Short addition chain at an open Scholz-Brauer value | REC | open |
| 37 | universal_cycle_ksubsets | Universal cycle of k-subsets at an open (n,k) | EX | open (verify cell) |
| 38 | pattern_avoidance_word | Word settling an open avoidability question | EX | open (verify question) |
| 39 | labs_merit_factor | Binary sequence beating the LABS merit-factor record | REC | open (verify record) |
| 40 | comma_free_code | Comma-free code beating the best known size | REC | open (verify cell) |
| 41 | sonar_sequence | Sonar sequence (2D distinct-difference) at open size | EX | open (verify cell) |
| 42 | de_bruijn_special | Constrained de Bruijn sequence at open parameters | EX | open (verify cell) |
| 43 | greedy_superstring_counterexample | Counterexample to a greedy-superstring ratio | CE | open |
| 44 | sparse_ruler | Sparse/perfect ruler beating the record at open length | REC | open (verify cell) |
| 45 | snake_in_the_box | Longer snake/coil in Q_n for open dimension | REC | open |

## Sources of openness (primary)

- **Life / Life-like (01-16):** LifeWiki "List of unsolved problems in Conway's Game of Life," "Spaceship," "Gun," "Rake," "Garden of Eden," "Oblique spaceship/Sir Robin," "Methuselah"; Catagolue censuses; ConwayLife.com forums. Life is now omniperiodic for *oscillators* (arXiv 2312.02799, 2023), so those hunts target still-open shapes (strict volatility, spaceship velocities/periods, guns, syntheses, orphans) — not oscillator periods.
- **Boolean/crypto (17-24):** Big APN problem (Dillon et al. 2009; dim-8 Groebner searches 2026); covering radius of RM(1,n) / Patterson-Wiedemann; Drakakis "Open problems in Costas arrays" (arXiv 1102.5727); Carlet's Boolean-functions monograph; APN/bent/planar/resilient tables (Budaghyan, Kaleyski, et al.).
- **Automata (25-28):** Cerny conjecture; Volkov survey; "List of Results on the Cerny Conjecture and Reset Thresholds" (arXiv 2508.15655, 2025); state-complexity surveys (Gao-Moreira-Reis-Yu 2017); magic-number line (Iwama, Geffert); Martyugin/Gonze-Jungers on partial automata.
- **Computation models & games (29-33):** PCP hard-instance searches (Ling & Zhao); tag-system (un)decidability (Post; De Mol); Termination Competition / TPDB; Flammenkamp "Sprague-Grundy values of octal games" (uni-bielefeld.de/~achim/octal.html + unsettled.txt: 65 unsettled 2-place + 8 3-place games, plus Grundy's game); Guy & Smith arithmetic periodicity; Guy "Unsolved Problems in Combinatorial Games."
- **Sequences & found objects (34-45):** superpermutation bounds (Houston, Egan; OEIS A180632); optimal sorting networks (Codish et al.; Bose-Nelson settled for n<=12, arXiv 2012.04400); addition chains (Knuth; OEIS A003313/A003064); Ucycles (Chung-Diaconis-Graham 1992; Hurlbert); pattern avoidance (Thue; Dejean 2009; Currie-Rampersad-Shallit); LABS (Mertens 1996; memetic solvers); comma-free codes (Golomb-Gordon-Welch; Eastman); sonar sequences (Golomb-Taylor 1982); constrained de Bruijn (Etzion-Lempel); Greedy Conjecture for superstrings (Blum et al. 1994; Tarhio-Ukkonen); sparse rulers (OEIS A046693); snake-in-the-box (Kautz 1958; record trackers).

## Openness I could not fully confirm this session (treat as "(verify)")

Confirmed live-open from sources fetched/searched this session: **02, 03 (velocity problem), 06, 08, 17, 19, 20, 25, 26, 28, 32, 33, 34, 35 (n=13), 43, 45**, plus omniperiodicity closing the *oscillator-period* framing.

Not independently re-confirmed to the exact cell this session (real open areas, but the specific target must be pulled from the live source before running):

- **01** strictly volatile oscillator: the area is open, but the *smallest still-open period* (I cite p7) needs confirmation against the current LifeWiki table.
- **04, 05, 07** (true-period gun period, no-known-synthesis object, rake period): open categories; the specific target cell must be taken from current LifeWiki/Catagolue.
- **09-12, 15, 16** (HighLife, non-totalistic, Generations, LtL, Rule 110 catalogue, hex/tri): other-CA object zoos are on Catagolue and move constantly; the exact unrealized velocity/period is (verify).
- **13** turmite: the specific unclassified transition-table entry is (verify).
- **14** methuselah, **29** PCP, **39** LABS, **44** sparse ruler: genuine open records, but the *current best* to beat must be re-read (these drift).
- **18, 21, 22, 23, 24** (new APN class dim 9/10; rotation-symmetric/homogeneous bent; resilient-nonlinearity cell; new planar/semifield order; optimal-immunity nonlinearity cell): all real open lines in the Boolean-function literature; the exact open (n, t)/order was not re-confirmed cell-by-cell.
- **27** state complexity, **30** tag halting, **31** TPDB non-termination, **37** Ucycle (n,k), **38** avoidance question, **40** comma-free (q,k), **41** sonar (m,n), **42** constrained de Bruijn: open families; the precise instance/cell is (verify).

No fabricated citations: references name authors/venues/resources only where recalled with confidence; every uncertain item carries "(verify)". Fetched directly this session: Flammenkamp octal page (unsettled counts), and search-confirmed: omniperiodicity 2023, Costas 32/33, superperm n=7 bounds, sorting n=11/12 closed & n=13 open, Cerny/slow-synchronization, Big APN.
