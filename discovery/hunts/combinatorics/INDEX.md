# Combinatorics witness hunts

Specific witness hunts in graph theory, design theory, and combinatorics. Each `NN_slug/PROMPT.md` names one small explicit object to find (or one "for all / optimal / doesn't exist" claim to refute) whose witness a checker validates exactly in seconds. All are one-sided: a single valid object settles the task. Ground truth for openness is the cited table / survey / database; re-verify each is still open before spending compute (these frontiers drift).

**Win-type:** existence (build an object whose existence is unknown) | found-object (beat a best-known record / bound) | counterexample (refute a universally-quantified conjecture).
**Openness:** documented-open (the source table explicitly marks it open) | verify (openness stated but re-confirm the specific parameter before starting).

| # | slug | one-line | win-type | openness |
|---|------|----------|----------|----------|
| 01 | srg_69_20_7_5 | strongly regular graph srg(69,20,7,5) | existence | documented-open |
| 02 | srg_88_27_6_9 | strongly regular graph srg(88,27,6,9) | existence | documented-open |
| 03 | srg_96_35_10_14 | strongly regular graph srg(96,35,10,14) | existence | documented-open |
| 04 | srg_100_33_8_12 | strongly regular graph srg(100,33,8,12) | existence | documented-open |
| 05 | srg_111_30_5_9 | strongly regular graph srg(111,30,5,9) | existence | documented-open |
| 06 | srg_115_18_1_3 | sparse strongly regular graph srg(115,18,1,3) | existence | documented-open |
| 07 | srg_133_24_5_4 | srg(133,24,5,4) = point graph of GQ(6,3) | existence | documented-open |
| 08 | srg_105_40_15_15 | strongly regular graph srg(105,40,15,15) | existence | documented-open |
| 09 | drg_open_intersection_array | DRG for an open feasible intersection array | existence | verify |
| 10 | drackn_antipodal_cover | distance-regular antipodal cover of K_n, open params | existence | verify |
| 11 | steiner_2_6_46 | Steiner system S(2,6,46) / (46,6,1)-BIBD | existence | verify |
| 12 | costas_array_32 | Costas array of order 32 (or 33) | existence | documented-open (verify) |
| 13 | perfect_1factorization | perfect 1-factorization of K_2n at smallest open order | existence | verify |
| 14 | conference_matrix_66 | symmetric conference matrix of order 66 | existence | verify |
| 15 | skew_hadamard_open_order | skew-Hadamard matrix at a small open order | existence | verify |
| 16 | difference_set_open | (v,k,lambda)-difference set for an open parameter set | existence | documented-open (verify) |
| 17 | covering_pairs_improve | beat a best-known C(v,k,2) covering | found-object | documented-open |
| 18 | covering_triples_improve | beat a best-known C(v,k,3) covering | found-object | documented-open |
| 19 | packing_improve | beat a best-known packing D(v,k,t) | found-object | documented-open |
| 20 | turan_system_improve | beat a best-known Turan system T(n,k,r) | found-object | documented-open |
| 21 | lotto_design_improve | beat a best-known lotto design L(n,k,p,t) | found-object | documented-open |
| 22 | cage_3_13 | smaller (3,13)-cage graph | found-object | documented-open |
| 23 | cage_4_7 | smaller (4,7)-cage graph | found-object | documented-open |
| 24 | cage_record_general | smaller cage for any open (r,g) with small gap | found-object | documented-open |
| 25 | mols_lower_bound | more MOLS at an under-tested order (raise N(n)) | found-object | documented-open |
| 26 | atomic_latin_square | atomic Latin square at an open composite order | existence | verify |
| 27 | mols_10_triple | three MOLS of order 10 (famous long shot) | existence | documented-open (famous) |
| 28 | snake_dim_11 | longer snake-in-the-box in Q_11 | found-object | documented-open |
| 29 | snake_dim_13 | longer snake-in-the-box in Q_13 | found-object | documented-open |
| 30 | coil_in_box | longer coil-in-the-box in Q_11 or Q_12 | found-object | documented-open |
| 31 | graceful_generalized_petersen | graceful labeling of an open P(n,k) | found-object / counterexample | verify |
| 32 | harmonious_open_family | harmonious labeling of an open family member | found-object / counterexample | verify |
| 33 | graceful_open_union | graceful labeling of an open disjoint union | found-object / counterexample | verify |
| 34 | ramsey_3_10 | triangle-free witness settling R(3,10)=41 | found-object | documented-open |
| 35 | ramsey_4_7 | improve the lower bound for R(4,7) | found-object | documented-open |
| 36 | ramsey_5_6 | improve the lower bound for R(5,6) | found-object | documented-open |
| 37 | ramsey_multicolor_3333 | improve lower bound for R(3,3,3,3) | found-object | documented-open |
| 38 | turan_girth5 | denser girth-5 graph than best-known ex(n;{C3,C4}) | found-object | documented-open (verify) |
| 39 | total_coloring_conjecture | graph with chi'' >= Delta+3 (refute TCC) | counterexample | documented-open |
| 40 | reconstruction_conjecture | two non-isomorphic graphs with equal decks | counterexample | documented-open |
| 41 | cycle_double_cover | bridgeless graph with no cycle double cover | counterexample | documented-open |
| 42 | seymour_second_neighborhood | oriented graph refuting second-neighborhood | counterexample | documented-open |
| 43 | berge_fulkerson | cubic graph with no Berge-Fulkerson cover | counterexample | documented-open |
| 44 | hadwiger_7 | 7-chromatic K7-minor-free graph (refute Hadwiger t=7) | counterexample | documented-open |
| 45 | ryser_4partite | r-partite hypergraph with tau > (r-1)nu (refute Ryser) | counterexample | documented-open |

## Sources of openness (re-verify before each attempt)

- **SRG (01-08):** A.E. Brouwer, "Parameters of strongly regular graphs," online table, aeb.win.tue.nl/graphs/srg/. The listed rows carry existence status "?" as of the fetch for this batch.
- **DRG (09-10):** Brouwer's distance-regular graph tables (aeb.win.tue.nl/drg/); van Dam, Koolen, Tanaka, "Distance-regular graphs," EJC dynamic survey DS22.
- **Designs (11-16):** Colbourn & Dinitz (eds.), "Handbook of Combinatorial Designs," 2nd ed. (CRC, 2007); La Jolla Difference Set Repository (D. Gordon); Costas-array enumeration literature.
- **Coverings/packings (17-21):** La Jolla Covering Repository, D. Gordon, ljcr.dmgordon.org.
- **Cages (22-24):** Exoo & Jajcay, "Dynamic Cage Survey," EJC dynamic survey DS16.
- **Latin squares (25-27):** Handbook of Combinatorial Designs (MOLS chapter); Wanless, "Atomic Latin squares" (EJC).
- **Snakes/coils (28-30):** OEIS A099155 (snake), A000937 (coil); Allison-Paulusma 2016 bounds and later record searches.
- **Labelings (31-33):** J.A. Gallian, "A Dynamic Survey of Graph Labeling," EJC dynamic survey DS6.
- **Ramsey/Turan (34-38):** S. Radziszowski, "Small Ramsey Numbers," EJC dynamic survey DS1; extremal-girth-5 tables.
- **Conjecture refutations (39-45):** standard open conjectures with computational frontiers (McKay reconstruction to n=11; House of Graphs snark catalogue for CDC / Berge-Fulkerson; Total Coloring, Seymour second neighborhood, Hadwiger t=7, Ryser r>=4).

## Honesty notes

- Items marked **verify** name a plausible open target but the exact parameter must be re-confirmed against the live source; some (Steiner S(2,6,46), the smallest open perfect-1-factorization order, conference matrix 66, skew-Hadamard smallest open order, atomic Latin orders) are cases I could not confirm are *currently* open to the exact value cited, only that the family has documented open cases.
- Items 27 (3 MOLS of order 10), 44 (Hadwiger t=7), and the Ramsey lower bounds (34-37) are genuinely open but heavily attacked; they are long shots included because the scope explicitly calls for specific small open cases. The under-tested wins are more likely in coverings/packings (17-21), snakes/coils (28-30), cages (22-24), and the SRG rows (01-08).
- SRG rows 01-08 were read off Brouwer's "?" list via automated fetch; treat the specific tuples as high-confidence-but-re-verify, since the extraction was machine-summarized.
