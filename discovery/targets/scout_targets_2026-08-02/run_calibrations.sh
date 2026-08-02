#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
run(){ echo "== $*"; "$@"; }
expect_fail(){ echo "== EXPECT-FAIL $*"; if "$@" >/dev/null 2>&1; then echo "ERROR: command unexpectedly succeeded" >&2; exit 1; fi; echo "Expected rejection observed."; }
run python checkers/check_signed_circulant.py fixtures/signed_n8_optimizer.json --certify
run python checkers/check_signed_circulant.py fixtures/signed_n8_all_positive.json
run python checkers/check_signed_circulant.py --baseline 8 10 12 14 16 18
run python checkers/benchmark_signed_dihedral.py 8 10 12 14 16 18
run python checkers/check_trianglefree_chi_z.py fixtures/triangle_c5.json
run python checkers/check_trianglefree_chi_z.py fixtures/triangle_c6.json
run python checkers/check_augmented_sombor.py fixtures/aso_t6_3.json
run python checkers/check_augmented_sombor.py fixtures/aso_k321.json
run python checkers/check_total2coalition.py fixtures/total2_k5_equality.json
run python checkers/check_total2coalition.py fixtures/total2_k5_invalid_singletons.json
run python checkers/check_lc_condensation.py fixtures/lc_positive.json
run python checkers/check_lc_condensation.py fixtures/lc_condition_nearmiss.json
run python checkers/check_arboreal_bunkbed.py fixtures/bunkbed_k2_lambda1.json
expect_fail python checkers/check_arboreal_bunkbed.py fixtures/bunkbed_k2_lambda0.json
run python checkers/check_prime_power_sum.py fixtures/prime_power_24.json
run python checkers/check_prime_power_sum.py fixtures/prime_power_23_out_of_domain.json
run python checkers/check_path_zero_forcing.py fixtures/path_p6_k2.json
run python checkers/check_path_zero_forcing.py fixtures/path_c6_k2.json
run python checkers/check_planar_ur_edge.py fixtures/planar_p4_valid.json
run python checkers/check_planar_ur_edge.py fixtures/planar_p4_invalid.json
run python checkers/check_coefficient_logconcavity.py fixtures/logconcave_positive.json
run python checkers/check_coefficient_logconcavity.py fixtures/logconcave_negative.json
run python checkers/check_pm_eigenvalue.py fixtures/pm_schema.json
run python checkers/check_matroid_polynomial.py fixtures/matroid_schema.json
for f in fixtures/vine_*_preflight.json; do run python checkers/check_vine_distance.py "$f"; done
run python checkers/check_flowboost_spectrum.py fixtures/flowboost_n4_spectrum.json

# Every JSON checker must reject malformed JSON.
for checker in checkers/check_*.py; do
  if python "$checker" fixtures/malformed.json >/dev/null 2>&1; then
    echo "ERROR: $checker accepted malformed JSON" >&2; exit 1
  fi
done
echo "All malformed-input rejection checks passed."
