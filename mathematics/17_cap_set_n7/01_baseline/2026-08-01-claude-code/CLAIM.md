# Claim

**Claim.** Two results, neither a new bound on a(7).
1. The hyperplane-profile reduction staircase for caps in AG(7,3) is independently reproduced for M in {291,290,289,288}: a hypothetical M-cap is forced to contain the listed "maximal" hyperplane profiles (exceptional sets of size 1, 2, 4, 6) with minimum multiplicities 7, 15, 16, 11. Each reduction is confirmed twice: by recomputing the published separating functional, and by an LP-derived separator with different integer coefficients. These are reductions, not bounds; proving a(7) <= M-1 still needs a SAT/ILP elimination of the exceptional profiles, not done here.
2. Lower bound unchanged: no cap larger than 236 found by randomized greedy (786 restarts, best 145) or local repair of the 236-cap (370 trials, best 236).
3. CP-SAT (OR-tools) with affine-frame symmetry breaking proves no 21-cap in AG(4,3) (INFEASIBLE, 6.8 s), giving a(4) <= 20; with a triple-scan-verified 20-cap this is a(4)=20, solver-attested. The a(5) and a(6) bounds did not close (UNKNOWN at 90 s / 120 s); 45- and 112-point witnesses were handled. This is calibration against known values, not a new claim.
4. Certified SAT with independently checked DRAT proofs (CaDiCaL 3.0.1 + drat-trim): a(2) <= 4, a(3) <= 9, a(4) <= 20, each drat-trim VERIFIED. a(4)=20 is thus proof-certified (up to the frame-WLOG lemma) plus a triple-scan-verified 20-cap, a real upgrade over the solver-attested CP-SAT verdict. a(5) <= 45 did not close in 300 s (1.0 GB proof unfinished). All known values; no new result on a(7).
5. Slice floor (exact integer Farkas certificate, `y = (199910685, -32896, 439)`, aggregate -332669): every 237-cap in AG(7,3) has a hyperplane slice of size >= 89, and all-slices-<=89 is LP-feasible, so the first-three-moment method cannot force >= 90. This is a new exact fact (not a bound on a(7)) that pins the moment method's reach at 89, against rigidity starting near 110. A nonlocal 237-cap search (fixed size, minimize violated lines) found no 237-cap over 300 s (best E=10); the lower bound stays 236.

**Checker.**
- `python3 src/verify_staircase.py` regenerates `certificates/staircase_{291,290,289,288}.json` and self-checks every assertion (exceptional sets, aggregates, forced-direction counts, exact-integer LP separators). Re-run 2026-08-01: all pass.
- `python3 src/lower_bound_search.py 25` reruns the search (seed 20260801).
- `python3 src/certify_small_caps.py 4 120` reproduces the a(4) <= 20 INFEASIBLE result (needs OR-tools). Re-run 2026-08-01: INFEASIBLE in 6.8 s; 20-cap witness triple-scan PASS.
- `make sat` (or `python3 src/sat_cap_bound.py $(command -v cadical) tools/drat-trim proofs 2,3,4 300`) reproduces the drat-trim VERIFIED bounds for a(2)..a(4). Needs `cadical` on PATH and `tools/drat-trim` built from source.
- `make verify-fast` runs the staircase check. Toolchain: Python 3.12.4, scipy 1.14.1 (HiGHS), OR-tools CP-SAT (pip), CaDiCaL 3.0.1 (brew), drat-trim (built from `tools/drat-trim.c`). Pin exact versions before archival.

**Trust base.** Exact integer arithmetic for every asserted number in the staircase. The reductions assume a(6)=112 (max slice size), not re-proved here. scipy HiGHS LP is used only to *find* separators; each is re-checked in exact integers, so the LP solver is not in the trust base. For the CP-SAT calibration, the INFEASIBLE verdict is solver-attested (OR-tools trusted). For the certified SAT bounds a(2)..a(4), CaDiCaL is NOT trusted: its DRAT proof is checked by the independent drat-trim, so the trust base is drat-trim, the CNF encoding (line + frame + sequential-counter cardinality), and the frame-WLOG lemma (any cap larger than a(d-1) affinely spans, so K+1 > a(d-1) makes fixing {0,e_1,...,e_d} sound). Any cap a solver returns is re-checked by an independent triple scan. No custom axioms or oracles.

**Encoding fidelity.** Profiles (a,b,c), a+b+c=M, 112 >= a >= b >= c >= 0. Moment multiplicities D=1093=(3^7-1)/2, pair=364=(3^6-1)/2, triple=121=(3^5-1)/2, derived from F_3^7 hyperplane geometry and asserted in code. Cap = no 3 distinct points summing to 0 mod 3; the search maintains this invariant incrementally.

**Review level.** self. Claude Code (Opus), building on the 2026-08-01-chatgpt-pro run. Not human-refereed, not community-confirmed.

**Provenance.** Claude Code (Opus), 2026-08-01. Independent reimplementation. Confirms the ChatGPT Pro run's arithmetic (including its previously unverified M=290 and M=288 reductions) and adds LP-derived independent separators.

**Cost and attempts.** Local compute only, no model/API spend. Staircase < 1 s; lower-bound search ~25 s; CP-SAT calibration a(4) 6.8 s, a(5)/a(6) not closed (90 s / 120 s); certified SAT a(2)/a(3) < 0.1 s, a(4) 18.9 s (drat-trim VERIFIED), a(5) timeout 300 s (1.0 GB proof, not closed). No new result on a(7): independent reproduction of the staircase, a documented null lower-bound attempt, and proof-certified a(2)..a(4) calibration.
