# Piatra Institute - Physics Research Program

Fifty well-posed open problems in theoretical physics, selected for tractability by SOTA reasoning models and ranked in strategic priority order; work in numeric order. No quantum gravity, no Millennium flagships. See `STRATEGY.md` for the ranking rationale and `PROMPT_TEMPLATE.md` for the prompt structure every folder follows.

Mode tags: `[search]` certified construction/counterexample search · `[cert]` computer-assisted proof (SAT, interval arithmetic, Lean) · `[sym]` symbolic/series mining with CAS · `[bound]` optimizing rigorous bounds · `[proof]` short-clever-argument hunting.

## Index

Tier 1 (01-10): machine-checkable ground truth, months-scale plausible. Tier 2 (11-25): strong footholds, exact data or optimization structure. Tier 3 (26-37): defined certificate pipelines, harder. Tier 4 (38-50): deep proof problems, background/opportunistic.

| # | Folder | Problem | Modes | Orig | Cat | Tier | Status |
|---|--------|---------|-------|------|-----|------|--------|
| 01 | `01_kochen_specker_minimal` | Minimal Kochen-Specker sets in d=3, SAT-certified | cert, search | 6 | A | 1 | not started |
| 02 | `02_yang_baxter_9x9` | Classify constant 9×9 Yang-Baxter solutions | search, cert | 30 | C | 1 | not started |
| 03 | `03_feynman_periods_bessel` | Bessel-moment and φ⁴ coaction conjectures | sym | 45 | G | 1 | not started |
| 04 | `04_percolation_critical_polynomials` | Prove Scullard-Ziff exact thresholds; square-site closed form | sym, proof | 27 | C | 1 | not started |
| 05 | `05_mub_dimension_6` | More than 3 mutually unbiased bases in C⁶? | proof, search | 1 | A | 1 | not started |
| 06 | `06_ising_susceptibility_2d` | Structure/closed form of the 2D Ising susceptibility | sym | 21 | C | 1 | not started |
| 07 | `07_ame_existence_table` | Undecided absolutely-maximally-entangled (n,d) entries | search, cert | 5 | A | 1 | not started |
| 08 | `08_central_configurations` | Smale's 6th for n≥6; Saari's conjecture | cert | 35 | E | 1 | not started |
| 09 | `09_additivity_counterexample` | Explicit low-dim minimum-output-entropy violation | search | 4 | A | 1 | not started |
| 10 | `10_npt_bound_entanglement` | NPT bound entanglement; Werner 2-copy distillability | proof, search | 3 | A | 1 | not started |
| 11 | `11_zauner_sic_povm` | SIC-POVMs in every dimension; Stark-unit structure | sym, proof | 2 | A | 2 | not started |
| 12 | `12_hard_squares_entropy` | Closed form for the hard-squares entropy constant | sym | 23 | C | 2 | not started |
| 13 | `13_monomer_dimer` | 2D monomer-dimer entropy; 3D dimer constant | sym | 24 | C | 2 | not started |
| 14 | `14_ice_residual_entropy` | Residual entropy of ice Ih, exact | sym | 25 | C | 2 | not started |
| 15 | `15_saw_connective_constant` | Square-lattice SAW connective constant | proof, sym | 26 | C | 2 | not started |
| 16 | `16_chiral_potts_correlations` | Chiral Potts / XYZ correlation functions | sym | 28 | C | 2 | not started |
| 17 | `17_six_vertex_arctic` | Rigorous arctic curves; ASM↔DPP bijection | proof, search | 29 | C | 2 | not started |
| 18 | `18_grothendieck_constant` | Exact K_G, K_G(3), I3322 maximum | bound, proof | 7 | A | 2 | not started |
| 19 | `19_triangular_billiards` | Periodic orbits in obtuse triangles, certified | cert, search | 36 | E | 2 | not started |
| 20 | `20_kam_golden_torus` | Exact breakup threshold of the golden KAM torus | sym | 38 | E | 2 | not started |
| 21 | `21_feigenbaum_constants` | Closed form / transcendence of δ and α | sym | 39 | E | 2 | not started |
| 22 | `22_lyapunov_closed_forms` | Exact Lyapunov exponents of random matrix products | sym | 34 | D | 2 | not started |
| 23 | `23_meander_exponent` | Prove the meandric exponent prediction | proof | 33 | D | 2 | not started |
| 24 | `24_abelian_sandpile` | Rigorous 2D avalanche exponents; identity scaling limit | proof, sym | 31 | C | 2 | not started |
| 25 | `25_kpz_2plus1` | Exact 2+1 KPZ exponents / fixed point | sym, proof | 32 | D | 2 | not started |
| 26 | `26_convection_bounds` | Close the Nusselt-Rayleigh rigorous-bound gap | bound | 40 | F | 3 | not started |
| 27 | `27_modular_bootstrap` | Sharp modular-bootstrap gaps at general central charge | bound | 48 | G | 3 | not started |
| 28 | `28_lieb_thirring` | Optimal γ=1 Lieb-Thirring constant | bound | 18 | B | 3 | not started |
| 29 | `29_self_correcting_memory` | 3D finite-temperature self-correcting quantum memory | search | 8 | A | 3 | not started |
| 30 | `30_haldane_gap` | Rigorous spin-1 Heisenberg chain gap | cert | 9 | B | 3 | not started |
| 31 | `31_magic_angles` | Flat bands beyond the chiral limit (TBG) | cert | 15 | B | 3 | not started |
| 32 | `32_neel_order_spin_half` | Néel LRO for square-lattice S=1/2 antiferromagnet | cert, proof | 10 | B | 3 | not started |
| 33 | `33_almost_mathieu` | Critical Hofstadter spectrum fractal dimension | proof, sym | 14 | B | 3 | not started |
| 34 | `34_thooft_model` | Closed-form 't Hooft model meson spectrum | sym, proof | 46 | G | 3 | not started |
| 35 | `35_bcj_duality` | Color-kinematics duality at loop level | sym, proof | 47 | G | 3 | not started |
| 36 | `36_choptuik_constants` | Derive Choptuik critical-collapse constants | sym | 50 | H | 3 | not started |
| 37 | `37_kelvin_problem` | Weaire-Phelan optimality / a better foam | search, bound | 44 | F | 3 | not started |
| 38 | `38_ising_in_field` | 2D Ising free energy at H≠0 | sym, proof | 22 | C | 4 | not started |
| 39 | `39_crystallization` | Periodic ground states; FCC universal optimality | proof, bound | 19 | B | 4 | not started |
| 40 | `40_grad_conjecture` | 3D MHD equilibria with flux surfaces; quasisymmetry | proof, bound | 41 | F | 4 | not started |
| 41 | `41_fast_dynamo` | Arnold's fast kinematic dynamo | proof, cert | 43 | F | 4 | not started |
| 42 | `42_parker_conjecture` | Current-sheet formation / non-smooth relaxation | proof | 42 | F | 4 | not started |
| 43 | `43_penrose_inequality` | The spacetime Penrose inequality | proof, bound | 49 | H | 4 | not started |
| 44 | `44_ionization_conjecture` | Z+1 ionization bound; Hund's first rule | proof | 20 | B | 4 | not started |
| 45 | `45_spin_glass_transition` | Existence of the 3D Edwards-Anderson transition | proof, cert | 17 | B | 4 | not started |
| 46 | `46_area_law_2d` | Entanglement area law for gapped 2D systems | proof | 11 | B | 4 | not started |
| 47 | `47_bec_thermodynamic` | BEC at fixed density in the thermodynamic limit | proof | 16 | B | 4 | not started |
| 48 | `48_anderson_2d` | 2D Anderson localization at weak disorder | proof | 13 | B | 4 | not started |
| 49 | `49_mbl_existence` | Many-body localization in 1D, settled either way | proof | 12 | B | 4 | not started |
| 50 | `50_standard_map_entropy` | Positive metric entropy of the standard map | proof | 37 | E | 4 | not started |

Categories: A quantum information and foundations · B rigorous many-body and condensed matter · C exactly solvable models and lattice statistics · D nonequilibrium and stochastic · E dynamical systems and classical mechanics · F fluids, plasmas, continuum · G QFT and mathematical particle theory · H classical gravitation.

## Working protocol

Every session runs under the atlas `SOLVER.md` (agency, compute, adversarial self-verification).
1. **Pick** the lowest-numbered problem not yet started; numeric order is priority order.
2. **Re-verify** the problem's current status in the literature first.
3. **Seed** a SOTA reasoning-model session with the attempt's `prompt.md`.
4. **Preserve** the full transcript as `chat.md` in the folder.
5. **Require** a self-contained research package: report (md + pdf), all source code, certificates, independent verifiers, SHA-256 manifest. Search source is part of the record.
6. **Record** honestly whether the complete-resolution standard was met; certified partial results are the expected product.
7. **Update** the Status column: `not started` → `in progress` → `partial` / `resolved` / `blocked`, and leave a `NEXT_STEPS.md` when pausing a line.

Related prior work: `research/frontier-atlas/mathematics/11_kelvin_weaire_phelan_optimizer` contains a Kelvin-problem audit (frustration-gap result, flat-A15 candidate) that folder 37 builds on.
