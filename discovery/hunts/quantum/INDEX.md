# Quantum-information witness hunts

Twenty-five specific-witness hunts where a single small explicit object settles a real open question and a second system checks it by exact (or high-precision certified) finite linear algebra in seconds. Each folder holds one `PROMPT.md`. Wins are one-sided: an existence object, a counterexample, or a record-beating found object. Openness is "as of mid-2026"; re-verify every "(verify)" cell before a session.

Win-type: **exist** = existence witness closes a cell; **refute** = counterexample to a for-all / undistillable / nonexistence claim; **record** = a found object beating a loose record or bound.

| # | slug | one-line | win-type | openness (verify) |
|---|------|----------|----------|-------------------|
| 01 | `mub_dim6_quadruple` | 4 mutually unbiased bases in C^6 | exist / refute | open, no proof max is 3; strong numerical evidence against |
| 02 | `mub_nonprimepower` | a 4th MUB in C^10 (or C^14, C^22) | exist / record | open for all d=2p; max MUB count unknown for non-prime-powers |
| 03 | `real_mub_open_cell` | real MUBs beyond the known count in R^d | record | open cells in r(d); verify target d |
| 04 | `ame_qudit_open_cell` | AME state at an open (n,d) cell | exist | open; tableofAME (Huber-Wyderka), verify cell |
| 05 | `k_uniform_open_cell` | k-uniform state at an open (n,d,k) | exist | open cells (Scott; later tables), verify cell |
| 06 | `sic_exact_open_dim` | exact WH-SIC fiducial in a gap dimension | record (found) | exact frontier; d=22,23,25,... lack exact solutions |
| 07 | `etf_open_cell` | equiangular tight frame at an open (d,N) | exist | open cells, Fickus-Mixon ETF table |
| 08 | `butson_open_cell` | Butson Hadamard BH(n,q) at an open cell | exist | open cells, Lampio-Ostergard-Szollosi table |
| 09 | `complex_hadamard_order6` | new isolated complex Hadamard of order 6 | record (found) | order-6 classification open; verify new beyond S6 |
| 10 | `qecc_beat_loose_cell` | stabilizer [[n,k,d]] beating a loose cell | record | open gap cells, codetables.de (Grassl) |
| 11 | `selfdual_gf4_graphstate` | record-distance graph state / self-dual GF(4) code | record | records improve; Danielsen-Parker, codetables, verify n |
| 12 | `ppt_entangled_open_rank` | PPT entangled state at an open rank cell | exist | open cells, Chen-Djokovic low-rank classification |
| 13 | `werner_distillability_witness` | refute n-undistillability of an NPT Werner state | refute | open; NPT bound entanglement (2-copy claimed settled 2026) |
| 14 | `upb_min_size_qubits` | minimum UPB on p qubits, p = 8,12,16,... | record / exist | open when parties are a multiple of 4 > 4 (Johnston) |
| 15 | `i3322_quantum_lower_bound` | beat the I3322 quantum-value record | record (bound) | quantum max unknown (Pal-Vertesi) |
| 16 | `sliwa_max_violation` | beat a Sliwa tripartite Bell record | record (bound) | several of the 46 Sliwa maxima open; verify functional |
| 17 | `ks_min_rays_d3` | Kochen-Specker set in R^3 below 31 rays | record | minimum open (~60 yr); overlaps physics/01 |
| 18 | `stabilizer_rank_magic` | stabilizer decomposition of |T>^n below record | record (bound) | upper bounds loose and actively improved |
| 19 | `superactivation_small_dim` | small-dimensional quantum-capacity superactivation | record | minimal dimensions not settled (Smith-Yard; 2026 work) |
| 20 | `quantum_mols_order6` | 3+ mutually orthogonal quantum Latin squares, order 6 | exist / record | pair known (AME(4,6)); >=3 open, verify |
| 21 | `umeb_open_cell` | unextendible maximally entangled basis at open cell | exist | open sizes in C^d x C^d (Bravyi-Smolin; Chen-Fei) |
| 22 | `hardy_paradox_max` | record Hardy nonlocality success probability | record (bound) | multiparty/higher-setting maxima open; verify config |
| 23 | `real_equiangular_lines` | more equiangular lines in R^d (d=18,19,20,...) | record | open cells, OEIS A002853; verify d |
| 24 | `quantum_chromatic_rankr` | smaller graph separating rank-r quantum chromatic no. | record | plain case closed at G14; rank-r (G21) minimality open |
| 25 | `unitary_error_basis_d6` | genuinely quantum unitary error basis in C^6 | exist (found) | non-nice/non-classical UEB existence open; verify |

## Notes on openness confidence

Firmly documented open (canonical source): 01, 04, 06, 07, 08, 10, 12, 13, 14, 15, 17, 18, 23. Plain quantum-vs-classical chromatic separation is now settled (G14 minimal, Mancinska-Roberson); 24 targets the still-open rank-r variant. Yu-Oh 13-ray minimal state-independent contextuality is proven minimal, so no separate task; contextuality minimality lives in 17 (KS, d=3).

Softer / needs re-check before a session: 03 (which r(d) cells), 05 (which (n,d,k) cell), 09 (isolated beyond S6), 11 (which length n), 16 (which Sliwa functional), 19 (current smallest superactivation), 20 (>=3 MOQLS order 6), 21 (which (d,N)), 22 (which Hardy configuration), 25 (equivalence-class novelty).
