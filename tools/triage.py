#!/usr/bin/env python3
"""Triage all 200 atlas problems by solvability shape and emit TRIAGE.md + triage.csv.

Shape tags:
  W  witness-shaped: one small checkable object (existence / counterexample / found
     object) settles it. The winnable regime (Maxwell/Ziegler/FunSearch).
  R  exact-value record: needs a construction AND a matching lower bound. Hard,
     two-sided, usually hardened by a community. Attack only loose cells.
  P  analytic proof: prove a theorem; no small witness. Not for this method.
  C  constant: compute/characterise a number. Not witness-solvable.
  RG reality-gated: needs wet-lab or held-out empirical data. Different program.

Tiers / disposition:
  T1 (W)  -> keep and sharpen toward the witness; primary targets.
  T2 (R)  -> deprioritise; only obscure/loose cells are worth a shot.
  T3 (P,C)-> reference only; out of scope for search-with-a-checker.
  T4 (RG) -> spin off into an empirical program with slow, expensive expectations.
"""
from pathlib import Path

TAG = {
 "physics": {
  "01_kochen_specker_minimal":"R","02_yang_baxter_9x9":"P","03_feynman_periods_bessel":"P",
  "04_percolation_critical_polynomials":"P","05_mub_dimension_6":"W","06_ising_susceptibility_2d":"C",
  "07_ame_existence_table":"W","08_central_configurations":"P","09_additivity_counterexample":"W",
  "10_npt_bound_entanglement":"W","11_zauner_sic_povm":"W","12_hard_squares_entropy":"C",
  "13_monomer_dimer":"C","14_ice_residual_entropy":"C","15_saw_connective_constant":"C",
  "16_chiral_potts_correlations":"P","17_six_vertex_arctic":"P","18_grothendieck_constant":"C",
  "19_triangular_billiards":"P","20_kam_golden_torus":"C","21_feigenbaum_constants":"C",
  "22_lyapunov_closed_forms":"P","23_meander_exponent":"C","24_abelian_sandpile":"P",
  "25_kpz_2plus1":"P","26_convection_bounds":"P","27_modular_bootstrap":"P","28_lieb_thirring":"C",
  "29_self_correcting_memory":"W","30_haldane_gap":"P","31_magic_angles":"P","32_neel_order_spin_half":"P",
  "33_almost_mathieu":"C","34_thooft_model":"P","35_bcj_duality":"P","36_choptuik_constants":"C",
  "37_kelvin_problem":"R","38_ising_in_field":"P","39_crystallization":"P","40_grad_conjecture":"W",
  "41_fast_dynamo":"P","42_parker_conjecture":"P","43_penrose_inequality":"P","44_ionization_conjecture":"P",
  "45_spin_glass_transition":"P","46_area_law_2d":"P","47_bec_thermodynamic":"P","48_anderson_2d":"P",
  "49_mbl_existence":"W","50_standard_map_entropy":"P",
 },
 "mathematics": {
  "01_ramsey_R5_5":"R","02_hadamard_668":"W","03_conway_99_graph":"W","04_projective_plane_12":"W",
  "05_hadwiger_nelson":"R","06_kissing_number_11":"R","07_moore_graph_degree_57":"W","08_lonely_runner":"P",
  "09_union_closed_sets":"W","10_jacobian_dimension_2":"P","11_kelvin_weaire_phelan_optimizer":"R",
  "12_schur_number_6":"R","13_ramsey_r46":"R","14_ramsey_r3k":"R","15_ramsey_multicolor_3333":"R",
  "16_van_der_waerden_w27":"R","17_cap_set_n7":"R","18_erdos_straus":"P","19_postage_stamp_bases":"R",
  "20_sidon_difference_families":"R","21_singmaster":"P","22_heilbronn_triangle":"R","23_borsuk_conjecture":"W",
  "24_tammes_problem":"R","25_reinhardt_octagon":"R","26_circle_packing":"R","27_no_three_in_line":"R",
  "28_srg_existence":"W","29_cage_orders":"R","30_zarankiewicz_crossing":"R","31_guy_crossing_kn":"R",
  "32_second_neighborhood":"W","33_graceful_labeling":"W","34_mols_order_10":"W","35_optimal_binary_codes":"R",
  "36_covering_codes_football_pool":"R","37_costas_arrays":"W","38_maximal_determinant":"R",
  "39_steiner_systems":"W","40_lehmer_mahler_measure":"P","41_casas_alvero":"W","42_markov_uniqueness":"P",
  "43_alon_tarsi":"P","44_rota_basis":"W","45_erdos_moser":"P","46_one_third_two_thirds":"P",
  "47_ryser_brualdi_stein":"W","48_sunflower_conjecture":"P","49_kobon_triangles":"R","50_thomson_problem":"R",
 },
 "informatics": {
  "01_sorting_networks":"R","02_sorting_comparisons":"R","03_matrix_mult_rank":"R","04_addition_chains":"R",
  "05_bilinear_complexity":"R","06_boolean_circuit_size":"R","07_matrix_rigidity":"R","08_apn_permutation":"W",
  "09_max_nonlinearity_odd":"R","10_bent_classification":"R","11_low_diff_uniformity":"R","12_algebraic_immunity":"R",
  "13_resilient_functions":"R","14_planar_functions":"W","15_complete_mappings":"R","16_log_rank":"W",
  "17_sensitivity_separations":"W","18_query_separations":"W","19_exact_query_complexity":"R",
  "20_formula_lower_bounds":"R","21_monotone_complexity":"R","22_proof_complexity":"R","23_busy_beaver":"R",
  "24_universal_turing_machine":"R","25_wang_tiles":"W","26_post_correspondence":"W","27_tag_systems":"W",
  "28_rewriting_termination":"W","29_state_complexity":"W","30_universal_cellular_automaton":"W",
  "31_life_spaceships":"W","32_life_oscillators":"W","33_gardens_of_eden":"W","34_superpermutations":"R",
  "35_covering_arrays":"R","36_t_count_synthesis":"R","37_clifford_cnot_synthesis":"R","38_quantum_code_parameters":"R",
  "39_quantum_mds_codes":"R","40_magic_state_distillation":"R","41_stabilizer_rank":"R","42_quantum_query_complexity":"R",
  "43_quantum_circuit_lower_bounds":"R","44_superstrings_debruijn":"R","45_coin_weighing":"R",
  "46_selection_networks":"R","47_arithmetic_circuits":"R","48_octal_games_periodicity":"W",
  "49_cerny_synchronizing":"R","50_pattern_avoidance":"R",
 },
}
# chembiotics: all reality-gated
TAG["chembiotics"] = {f"A{ i:02d}":"RG" for i in range(1,22)}
TAG["chembiotics"].update({f"B{ i:02d}":"RG" for i in range(1,30)})

TIER = {"W":"T1","R":"T2","P":"T3","C":"T3","RG":"T4"}
ACTION = {"W":"keep, sharpen toward the witness",
          "R":"deprioritise; only loose/obscure cells",
          "P":"reference only; out of scope",
          "C":"reference only; out of scope",
          "RG":"spin off into an empirical program"}

def main():
    root = Path(__file__).resolve().parents[1]
    rows = []
    for dom, d in TAG.items():
        for slug, tag in d.items():
            rows.append((dom, slug, tag, TIER[tag], ACTION[tag]))
    (root/"triage.csv").write_text("domain,problem,shape,tier,action\n" +
        "\n".join(f"{a},{b},{c},{t},{ac}" for a,b,c,t,ac in rows) + "\n")
    from collections import Counter
    tally = Counter(r[2] for r in rows)
    tier_tally = Counter(r[3] for r in rows)
    lines = ["# Triage of the 200",
             "",
             "Generated by `tools/triage.py`. Shape tags and tiers are defined there.",
             "",
             f"Totals: W={tally['W']} R={tally['R']} P={tally['P']} C={tally['C']} RG={tally['RG']} "
             f"(of {len(rows)}).",
             f"Tiers: T1(winnable)={tier_tally['T1']} T2(record)={tier_tally['T2']} "
             f"T3(proof/const)={tier_tally['T3']} T4(reality-gated)={tier_tally['T4']}.",
             "",
             "Only the T1 set is on-method for search-with-a-checker. T2 is a long shot",
             "(loose cells only), T3 is out of scope, T4 belongs in a separate program.",
             ""]
    for tier, title in [("T1","Tier 1 - winnable (witness-shaped)"),
                        ("T2","Tier 2 - exact-value records (hard; loose cells only)"),
                        ("T3","Tier 3 - analytic proofs / constants (out of scope)"),
                        ("T4","Tier 4 - reality-gated (spin off)")]:
        members = [r for r in rows if r[3]==tier]
        lines.append(f"## {title}  ({len(members)})")
        for dom in ("physics","mathematics","informatics","chembiotics"):
            got = [f"{b} [{c}]" for a,b,c,t,ac in members if a==dom]
            if got:
                lines.append(f"- **{dom}** ({len(got)}): " + ", ".join(got))
        lines.append("")
    (root/"TRIAGE.md").write_text("\n".join(lines))
    print(f"wrote TRIAGE.md and triage.csv: {len(rows)} problems; "
          f"W={tally['W']} R={tally['R']} P={tally['P']} C={tally['C']} RG={tally['RG']}")

if __name__ == "__main__":
    main()
