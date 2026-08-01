# Bilinear complexity of small bilinear maps

Pin one bilinear map, field, and rank notion; certify an exact rank with matching
upper (explicit decomposition) and lower (nonexistence) certificates. Levels: task,
one folder per approach (`prompt.md`), and a dated run folder per execution.

## Approaches and runs

| approach | run | result | review |
|---|---|---|---|
| `01_baseline` (`[sym]`) | `2026-08-01-chatgpt-pro` | certified R_F2(<2,2,3>) = 11 (known value; substitution-method lower certificate + explicit 11-product upper). Package self-verifies. | agent; reproduction, no new result |
| `01_baseline` (`[sym]`) | `2026-08-01-claude-code` | upper bound R <= 11 independently re-derived (all 1024 inputs, 0 mismatches); independent SAT lower-bound method validated on Strassen (<2,2,2> >= 7, drat-trim VERIFIED) but <2,2,3> R=10 UNSAT did not close in 600 s | self; verification of a known value |

## Notes

- `2026-08-01-chatgpt-pro` is a complete, replayable P1 reproduction of a settled
  value (R_F2(<2,2,3>)=11; upper is classical Hopcroft-Kerr, the F2 lower bound is
  in arXiv:2603.07280). It pivoted from the prompt's Q target to F2, where the value
  is certifiable. `verify_all.sh` passes here (drat-independent C++ two-slice check +
  backtracking-tree verifier). No new result.
- `2026-08-01-claude-code` verifies the chatgpt-pro result. The upper bound is
  re-derived directly over F2 (independent, confirmed). The lower bound is attacked
  by a from-scratch SAT encoding (rank-R decomposition existence -> UNSAT) with a
  drat-trim-checked proof, a different method from the substitution certificate. That
  method is validated (it independently proves the Strassen bound R_F2(<2,2,2>) >= 7),
  but the target <2,2,3> R=10 UNSAT did not close in 600 s, so R >= 11 still rests on
  the chatgpt-pro certificate. Raw SAT does not scale to <2,2,3>, which is why the
  substitution method was needed there.
- To get a *new* result here, attack an open format (e.g. <3,3,3>, rank in [19,23]);
  the settled small cases only yield reproductions.
