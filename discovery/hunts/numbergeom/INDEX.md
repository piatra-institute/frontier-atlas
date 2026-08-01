# numbergeom hunts index

Specific witness hunts in number theory, discrete geometry, and algebra. Each folder holds one `PROMPT.md`: a single small explicit witness settles it, a checker validates in seconds, and the win is one-sided (a witness or counterexample proves the claim; failure proves nothing). All "openness" claims are marked (verify): re-check the cited source before investing, since parameters, records, and proven ranges drift.

Win-type legend: **exist** = existence witness; **cx** = counterexample to an "always / optimal / none-exist" claim; **record** = one-sided record beat (better construction than best published); **found** = found object among candidates.

| # | slug | one-line | win-type | openness (verify) |
|---|------|----------|----------|-------------------|
| 01 | costas_32_33 | Costas array of order 32 or 33 | exist | open; none known, enumerated through order 29 |
| 02 | sparse_ruler_excess | spanning ruler with fewer marks past certified range | record | open beyond exhaustive range; Wichmann optimality conjectural |
| 03 | postage_stamp_basis | h-fold additive basis beating n(h,k) | record | open/improvable cells in tables |
| 04 | bh_sidon_set | B_h set larger than tabulated | record | lower bounds improvable for h>=3 |
| 05 | b2g_set | B_2[g] set larger than tabulated | record | maxima not proven for many (g,n) |
| 06 | difference_family_k6 | (v,k,1) difference family, k=6/7, open v | exist | sporadic open orders for k>=6 |
| 07 | cyclic_difference_set | cyclic (v,k,lambda) set at open triple | exist | La Jolla repository lists undecided triples |
| 08 | skew_hadamard_df | non-Paley skew Hadamard difference set | exist/found | classification incomplete since Ding-Yuan |
| 09 | perfect_1factorization | perfect 1-factorization of K_{2n}, open order | exist | Kotzig conjecture, infinitely many open orders |
| 10 | williamson_matrices | Williamson matrices at open order | exist | enumerated to order 59; some orders open |
| 11 | magic_square_of_squares | 3x3 magic square of 9 distinct squares | exist | open, prize-backed (multimagie) |
| 12 | magic_square_more_squares | 3x3 magic square with 8 square entries | record | best documented is 7; 8-9 open |
| 13 | multimagic_small | bi/trimagic square below record order | exist | smallest known orders 8/12; smaller cases open |
| 14 | magic_square_of_cubes | small magic/semimagic square of cubes | exist | specific cases open (multimagie) |
| 15 | mols_10 | three MOLS of order 10 | exist | famous open; hardened long shot |
| 16 | latin_bitrade_spectrum | Latin bitrade filling a spectrum gap | exist | documented open sizes/shapes |
| 17 | latin_min_intercalates | Latin square with fewer intercalates | record | exact minima open for many n |
| 18 | casas_alvero_degree | Casas-Alvero counterexample over Q at open degree | cx | open outside prime-power/verified range |
| 19 | casas_alvero_finite_field | new Casas-Alvero counterexample over F_q | found/cx | false over finite fields; classification open |
| 20 | real_rootedness_refute | non-real root in a conjectured real-rooted family | cx | several open families (Braenden survey) |
| 21 | log_concavity_refute | dip in a conjectured log-concave sequence | cx | many open unimodality/log-concavity claims |
| 22 | circulant_hadamard | circulant Hadamard matrix of order > 4 | cx | Ryser conjecture open; hardened by field descent |
| 23 | davenport_constant | zero-sum-free sequence beating D(G) bound | record | D(G) open for rank>=3 groups |
| 24 | zero_one_polytope_facets | 0/1-polytope with more facets than record | record | max facets open for small d (Ziegler) |
| 25 | kalai_3d_conjecture | centrally symmetric polytope with < 3^d faces | cx | Kalai 3^d conjecture open in general |
| 26 | acute_set | acute set larger than record in fixed d | record | maxima/best constructions open small d |
| 27 | empty_simplex_width | empty lattice simplex wider than record | record | max width open for d>=4 |
| 28 | lattice_covering_dim6 | lattice covering below record density | record | optima proven only through dim 5 |
| 29 | kissing_number_dim | kissing configuration beating record | record | exact kissing unknown outside 1,2,3,4,8,24 |
| 30 | sphere_packing_dim | lattice packing denser than record | record | optima unproven dims 9-15; hardened long shot |
| 31 | lattice_quantizer | lattice with lower second moment than record | record | optima proven only dims 1,2,3 |
| 32 | no_three_in_line_open_n | 2n points, no 3 collinear, on n x n grid | exist | open n in Flammenkamp tables |
| 33 | orchard_planting | more 3-point lines than record for n points | record | exact t_3(n) open for many n |
| 34 | heilbronn_rational | min-triangle configuration beating h(n) | record | exact optima only very small n |
| 35 | six_chromatic_unit_distance | 6-chromatic unit-distance graph | exist | chromatic number of plane in [5,7], open |
| 36 | smallest_5chromatic_udg | smaller 5-chromatic unit-distance graph | record | Polymath16 record not settled |
| 37 | wilson_prime_fourth | a 4th Wilson prime | found | only 3 known; searched past 2e13 |
| 38 | wolstenholme_prime_third | a 3rd Wolstenholme prime | found | only 2 known; searched past 1e9 |
| 39 | brocard_next | n!+1 = m^2 beyond n=7 | found/cx | only 3 known; searched into 1e9-1e12 |
| 40 | sun_conjecture_refute | counterexample to a Zhi-Wei Sun conjecture | cx | many finite-verified claims; some already refuted |
| 41 | odd_weird_number | an odd weird number | exist | open; none found to large bounds; plausibly false |
| 42 | lonely_runner_k8 | lonely runner counterexample, k>=8 | cx | proven only k<=7 |
| 43 | integer_distance_points | integral general-position set beating diameter record | record | minimum diameters unproven for larger n |
| 44 | pte_ideal | ideal PTE solution at open size | exist | smallest sizes with none known are open |
| 45 | antimagic_conjecture | connected graph with no antimagic labeling | cx | Hartsfield-Ringel conjecture open |

## Flags: openness or plausibility-of-falsehood I could not fully confirm

These are grounded in real open problems, but I could not confirm the exact current frontier from within this session. Re-verify the cited source before committing effort.

- **Hardened / witness may effectively be out of reach** (open in principle, but extensive search or theory makes a small witness unlikely): 15 mols_10, 22 circulant_hadamard, 30 sphere_packing_dim, 41 odd_weird_number, and to a lesser degree 37 wilson_prime_fourth and 38 wolstenholme_prime_third (a witness likely exists heuristically but may lie past reachable bounds). Kept because the check is clean and the problem is genuinely open; flagged as long shots.
- **Specific target must be pinned live**: 06, 07, 08, 09, 10 (open order/triple from tables that shift), 13, 14 (which multimagic orders remain open, per multimagie.com), 16 (which bitrade sizes are open), 18 (smallest Casas-Alvero degree past the computational and prime-power-multiple frontier), 20, 21 (which real-rootedness / log-concavity families are still open), 40 (which Sun conjecture still stands). The prompt states the hunt; the exact open instance needs a source check.
- **Proven range may have advanced**: 42 lonely_runner_k8 (I state proven for k<=7; confirm the current proven bound before targeting the smallest open k).
- **Record-beat targets** (02, 03, 04, 05, 12, 17, 23, 24, 26, 27, 28, 29, 31, 33, 34, 36, 43): openness means "best published value not proven optimal," so the win is a strict improvement, not a resolution. These are one-sided and checkable, but the current record must be read off the cited table before starting.

No fabricated citations, arXiv IDs, or DOIs are used; all references are by author/venue name and marked (verify) where the exact current status was not confirmed here.
