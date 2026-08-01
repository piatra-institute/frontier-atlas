# Cap-set a(7): independent verification and staircase reduction

Run by Claude Code (Opus), 2026-08-01, continuing the 2026-08-01-chatgpt-pro run.
This run did **not** produce a new bound on a(7). It independently verifies the
prior work, reproduces the upper-bound reduction staircase with its own code and
its own separating functionals, and records an honest null lower-bound attempt.

## What was established

### 1. Independent reproduction of the hyperplane-profile staircase

For a hypothetical M-cap in AG(7,3), each of the 1093 hyperplane directions gives
a sorted profile (a,b,c), a+b+c=M, 112 >= a >= b >= c >= 0. The moment identities
(sum n_t = 1093, sum n_t P = 364*C(M,2), sum n_t Q = 121*C(M,3)) fix the aggregate
of any affine slack functional. `src/verify_staircase.py` reimplements this from
scratch and confirms, for each M:

| M | exceptional profiles forced | count | aggregate slack | min directions | reduces to |
|---|---|---|---|---|---|
| 291 | (112,112,67) | 1 | -505661 | 7 | a(7) <= 290 |
| 290 | (112,112,66), (112,111,67) | 2 | -145476 | 15 | a(7) <= 289 |
| 289 | (112,112,65),(112,111,66),(112,110,67),(111,111,67) | 4 | -499824 | 16 | a(7) <= 288 |
| 288 | (112,112,64),(112,111,65),(112,110,66),(112,109,67),(111,111,66),(111,110,67) | 6 | -15984 | 11 | a(7) <= 287 |

Two independent confirmations per row:
- the published separating functionals (from the committed 291/289 generators,
  and the 290/288 functionals proposed in review) are recomputed and their sign
  patterns and aggregates verified;
- a separating functional is **rederived from scratch by LP** (HiGHS), then
  checked in exact integer arithmetic. The LP-found coefficients differ entirely
  from the published ones (e.g. M=288: `[553506, -50000000, ...]` vs `[3, -271, ...]`)
  yet force the same exceptional set and a negative aggregate. The reduction is
  therefore intrinsic to the profile geometry, not an artifact of chosen constants.

The M=290 and M=288 reductions, previously computed only in a chat, are now
regenerated and hashed here (`certificates/staircase_290.json`,
`staircase_288.json`), closing the verify-before-cite gap.

### 2. Honest lower-bound attempt (null)

`src/lower_bound_search.py`, no exact solver available:
- randomized greedy construction: 786 restarts, best cap size **145** (gap 91 below 236);
- local repair of the 236-cap (remove R points, greedy refill; R in 8..32): 370
  trials, best **236**, no improvement.

No cap larger than 236 was found. Heuristic construction lands far below the
structured record; beating 236 requires an exact solver with local branching.
OR-tools CP-SAT was installed after this search (section 3); a CP-SAT
local-branching lower-bound run is the next attempt and was not done here.

### 3. CP-SAT calibration of exact small caps (OR-tools)

Decision formulation (prove no (K+1)-cap) with affine-frame symmetry breaking:
fix {0, e_1, ..., e_d}, valid because any cap larger than a(d-1) cannot lie in a
hyperplane and so spans (K+1 > a(d-1): 21>9, 46>20, 113>45).

| d | value | no-(K+1)-cap | result | witness |
|---|---|---|---|---|
| 4 | a(4)=20 | INFEASIBLE, 6.8 s | a(4) <= 20 proven (solver-attested) | 20-cap, triple-scan PASS |
| 5 | a(5)=45 | UNKNOWN, 90 s | not closed | 45-cap, triple-scan PASS |
| 6 | a(6)=112 | UNKNOWN, 120 s | not closed | not found in 30 s witness budget |

a(4) closes in seconds; a(5) and a(6) do not. That jump is the calibration finding:
frame-fixing alone suffices for a(4) but not beyond, so the a(7) profile-elimination
staircase will need real symmetry engineering (lex-leader / frame-stabilizer
breaking), not just a solver and time. It also shows why a(6)=112 (the premise the
whole upper argument rests on) is a serious computation, not a quick CP-SAT call.
A CP-SAT INFEASIBLE verdict is solver-attested, not an LRAT proof; a self-contained
a(4) <= 20 certificate should be re-run with a proof-logging SAT solver.

### 4. Certified SAT upper bounds with independently checked proofs

Toolchain: CaDiCaL 3.0.1 (brew) emits a DRAT proof; drat-trim (built from
`tools/drat-trim.c`) independently checks it. Same encoding as section 3 (no
(K+1)-cap containing the affine frame), now producing a checkable refutation.

| d | bound | solve | proof | drat-trim |
|---|---|---|---|---|
| 2 | a(2) <= 4 | < 0.1 s | 190 B | VERIFIED |
| 3 | a(3) <= 9 | < 0.1 s | 1.9 KB | VERIFIED |
| 4 | a(4) <= 20 | 18.9 s | 42 MB | VERIFIED |
| 5 | a(5) <= 45 | timeout 300 s | 1.0 GB, not closed | n/a |

This upgrades a(4) <= 20 from the CP-SAT solver-attested verdict to a genuine
independently checked proof; with the triple-scan-verified 20-cap, a(4)=20 is now
proof-certified up to the frame-WLOG lemma. a(5) did not close in 300 s (its proof
reached 1.0 GB unfinished), confirming that frame-fixing plus a sequential-counter
cardinality encoding is not enough past a(4); lex-leader / frame-stabilizer
symmetry breaking is the next step. Proofs are regenerable (`make sat`) and
git-ignored; the CNF inputs and the VERIFIED verdicts in
`certificates/sat_bounds.json` are the tracked evidence.

### 5. Slice floor for 237-caps, and a nonlocal 237-cap search

Slice floor (exact certificate): `verify_slice_floor.py` proves via an exact
integer Farkas certificate (y = (199910685, -32896, 439), aggregate -332669) that
every 237-cap has a hyperplane slice of size >= 89, and that all-slices-<=89 is
LP-feasible, so the moment method cannot force >= 90. This pins the moment method's
reach at exactly 89, while the rigidity classifications only start near 110. The
89..110 interval is the unbridged core of the a(7) upper-bound difficulty, and it
is now an independently verified fact.

Nonlocal 237-cap search (null): `cap_lns.py` fixes the set size at 237 and
minimizes the number of selected affine lines E by point swaps (the 236-cap is
complete, so greedy extension is dead; a 237-cap needs rearrangement). Over 300 s
and 10 restarts, seeding from the 236-cap plus one point reaches E=10 (ten violated
lines) and never E=0; random 237-seeds do far worse (E=89..138). No 237-cap found;
the lower bound remains 236. A hit would have been a new record, checkable by the
triple scan. Reaching E=10 but not 0 reflects how rigid the 236-cap is; a serious
attempt needs simulated annealing / tabu with structured moves or an exact ILP with
local branching.

## What this is NOT

- **Not a new bound.** The staircase rows are *reductions*: proving a(7) <= M-1
  still requires a SAT/ILP proof that the listed profiles cannot occur as a
  hyperplane decomposition of a cap. That elimination was not attempted here.
- The staircase to 288 only reproduces the known literature bound
  (a(7) <= 288, arXiv:2206.09804). Only a(7) <= 287 (eliminating the six M=288
  profiles) would beat it.
- The whole upper argument still assumes a(6)=112, not re-proved here.
- **Structural ceiling on this whole approach.** The slice/profile method only has force in the near-maximal-slice regime: at 289 it forces two rigid ~112-slices (classified, eliminable), but a diffuse split like (79,79,79) at 237 forces no near-maximal slice, so the classification leverage vanishes. The SAT staircase can reproduce <= 288 and perhaps <= 287, then stalls far above 236. Closing the 236-288 gap needs new mathematics (a 237+ construction, a medium-density slice theorem, or a new additive-energy invariant), not solver time.

## Denominator

- Staircase verification: pure exact arithmetic, < 1 s, no model calls.
- Lower-bound search: ~25 s wall, 786 greedy restarts + 370 repair trials, seed 20260801.
- CP-SAT calibration (OR-tools, 8 workers): a(4) proven in 6.8 s; a(5) (90 s) and a(6) (120 s) not closed.
- Certified SAT (CaDiCaL 3.0.1 + drat-trim): a(2)/a(3)/a(4) proven and independently VERIFIED (a(4) 18.9 s); a(5) timeout at 300 s (1.0 GB proof, not closed).
- Slice floor: exact Farkas certificate (< 1 s) that every 237-cap has a slice >= 89.
- Nonlocal 237-cap search: 300 s, 10 restarts, best E=10 (no cap found).
- No new result on a(7). The proof-certified bounds are a(2)..a(4) (known values); the one new exact fact is the >= 89 slice floor.

## Next steps (unchanged priority)

1. Install an exact solver; run the U1 profile-SAT to eliminate (112,112,67)
   (validates the 7-dim pipeline; yields a(7) <= 290 independently, still inside
   the known frontier).
2. Certify a(6)=112 (the no-113 UNSAT proof) to make the upper argument self-contained.
3. Exact-solver lower-bound search (local branching around the 236-cap) as the
   real record attempt.
4. Only eliminating the six M=288 profiles (-> a(7) <= 287) or finding a 237+ cap
   would move the frontier.
