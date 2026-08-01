# Independent verification of R_F2(<2,2,3>) = 11

Run by Claude Code (Opus), 2026-08-01, checking the sibling `2026-08-01-chatgpt-pro`
package by independent means. No new result: R_F2(<2,2,3>) = 11 is a settled value.

## What was done

### Upper bound (independently confirmed)
`upper_recheck.py` re-implements the 11-product F2 algorithm from scratch and checks
it against true 2x2-by-2x3 multiplication over all 2^10 = 1024 input pairs: 0
mismatches. So R_F2(<2,2,3>) <= 11 by our own code, not a replay.

### Lower bound (independent method, validated but not closed for the target)
`sat_bilinear_lb.py` encodes "a rank-R decomposition over F2 exists" as CNF (Tseitin
AND for the u*v*w products, XOR parity for each structure-tensor coefficient, lex
ordering on the R triples to break the S_R symmetry) and seeks UNSAT with a
drat-trim-checked proof. This is a different method from the substitution-method
certificate in the chatgpt-pro package.

| instance | expected | result |
|---|---|---|
| <2,2,2> R=7 | SAT (Strassen exists) | SAT, 0.1 s |
| <2,2,2> R=6 | UNSAT (rank 7 optimal) | UNSAT, drat-trim VERIFIED, 0.2 s |
| <2,2,3> R=11 | SAT (decomposition exists) | SAT, 12.7 s |
| <2,2,3> R=10 | UNSAT (=> R >= 11) | timeout at 600 s (1.3 GB partial proof) |

The Strassen row is the validation: our method independently proves the classical
R_F2(<2,2,2>) >= 7 with a checked proof. But the target <2,2,3> R=10 UNSAT did not
close in 600 s. Raw SAT with lex symmetry breaking is not enough here, which is
exactly why the chatgpt-pro package used the substitution method (restriction
geometry + backtracking) rather than a monolithic SAT refutation.

## Honest status

- R <= 11: independently established by us.
- R >= 11: independently *validated in method* (Strassen), but for <2,2,3> it still
  rests on the sibling substitution certificate (which replays here: `verify_all.sh`
  ALL CHECKS PASSED). We did not close it independently.
- No new result; this is verification of a settled value.

## Next steps

- Add the substitution-method restrictions to the SAT encoding (fix a maximal
  first-factor restriction, branch on quotient vectors) to shrink the R=10 instance,
  or port the chatgpt-pro backtracking into a second independent implementation.
- For a *new* result, target an open format (<3,3,3>, rank in [19,23]) where even a
  one-sided improvement would be a record.
