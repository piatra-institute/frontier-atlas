# Claim

**Claim.** Independent verification of the sibling `2026-08-01-chatgpt-pro` run, plus a
serious but unsuccessful record attempt.
1. **Both covering arrays independently verified by our own code.** `verify_ca.py`
   checks that CA(13;2,8,3) covers all 28 column-pairs (0 missing) and CA(39;3,7,3)
   covers all 35 column-triples (0 missing). So CAN(2,8,3) <= 13 and CAN(3,7,3) <= 39
   confirmed independently. (The CAN(2,8,3) lower bound, no CA(12), self-verifies in
   the sibling package via Bron-Kerbosch; we ran it: ALL_CHECKS_PASS.)
2. **Record attempt CAN(3,7,3) N=38: no record.** The best known is 39 (Colbourn
   table, "SAT Local Search (Hnich et al.)", not marked optimal), so a valid
   CA(38;3,7,3) would be a new record. A min-conflicts + simulated-annealing search
   (`ca_search.py`), warm-started from the CA(39), ran 50 starts over 600 s and
   plateaued at **5 uncovered interactions**, never reaching 0. No CA(38) found.
   CP-SAT (`ca_cpsat.py`) was not competitive: it could not find even the known
   CA(39) from scratch in 60 s. Best-known 39 stands.

Net: verification of known values plus a documented, unsuccessful record attempt. Two
independent serious searches (the sibling's and ours) both floor at exactly 5
uncovered for N=38, strong empirical evidence that 39 is effectively optimal.

**Checker.**
- `python3 src/verify_ca.py <csv> t k v` (independent, exact coverage check). Re-run 2026-08-01: CA(13;2,8,3) and CA(39;3,7,3) both VALID, 0 missing.
- `python3 src/ca_search.py 600 38` reproduces the N=38 attempt (best 5 uncovered, seed 20260801).
- The sibling `verify_all.sh` for the full CAN(2,8,3)=13 certificate.
- Toolchain: Python 3.12, OR-tools CP-SAT (for `ca_cpsat.py`).

**Trust base.** Coverage verification is exact combinatorial checking (no solver, no floating point), fully independent, and a found array is self-certifying. The record attempt is heuristic: a hit would be exactly verified, but a non-result is not a proof that CA(38) is impossible. CP-SAT is not load-bearing (non-competitive here).

**Review level.** self. Independent verification of the agent (chatgpt-pro) run and an independent record attempt. Not human-refereed.

**Provenance.** Claude Code (Opus), 2026-08-01. Own implementations; no code imported from the chatgpt-pro package.

**Cost and attempts.** Local, no model spend. Verification < 1 s; SA record attempt 600 s (50 starts, best 5 uncovered); CP-SAT N=39 sanity 60 s (UNKNOWN). No new result: two known values re-verified, one open record attacked and not taken.
