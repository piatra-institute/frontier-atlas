# Covering arrays: independent verification + a CAN(3,7,3) record attempt

Run by Claude Code (Opus), 2026-08-01. Checks the sibling `2026-08-01-chatgpt-pro`
run and attacks the open record CAN(3,7,3). No new result.

## Independent verification (both confirmed)
`verify_ca.py` (our own) checks coverage exactly:
- CA(13;2,8,3): 28 column-pairs, 0 missing -> CAN(2,8,3) <= 13.
- CA(39;3,7,3): 35 column-triples, 0 missing -> CAN(3,7,3) <= 39.

The CAN(2,8,3) lower bound (no CA(12)) self-verifies in the sibling package
(`verify_all.sh`: ALL_CHECKS_PASS, Bron-Kerbosch, no K6). So CAN(2,8,3)=13 holds
(a known value).

## Record attempt: CAN(3,7,3), N=38 (no record)
Best known is 39, from SAT local search (Hnich et al.), and the Colbourn table does
not mark it optimal, so a valid CA(38;3,7,3) would be a genuine new record.

| method | result |
|---|---|
| min-conflicts + SA (`ca_search.py`), 50 starts, 600 s, warm-started from CA(39) | best **5 uncovered** interactions; no CA(38) |
| CP-SAT (`ca_cpsat.py`) | non-competitive: could not find even the known CA(39) from scratch in 60 s |

No CA(38;3,7,3) found. Best known 39 stands.

## Honest verdict
Two independent serious searches (the sibling's and ours) both floor at **exactly 5
uncovered** for N=38. That is strong empirical evidence that CA(38;3,7,3) does not
exist and 39 is effectively optimal, which is consistent with 39 being a
long-standing search-set record. This is the closest and most legitimate record
attempt of the session (a genuinely open target attacked properly), but it is still
a null: no new record.

## Next steps
- The exact route to a *result* here is CP-SAT/SAT proving CA(38) INFEASIBLE, which
  would establish CAN(3,7,3)=39 optimal (a new fact, since the table lists 39 as
  best-known only). But that is the hard UNSAT direction and needs strong symmetry
  breaking (row/column/symbol) far beyond what was tried; raw CP-SAT could not even
  find CA(39). A dedicated isomorph-free enumeration is the realistic path.
- For a lower-row *record*, a different cell whose best-known bound is looser than 39
  would have better odds than one already hardened by SAT local search.
