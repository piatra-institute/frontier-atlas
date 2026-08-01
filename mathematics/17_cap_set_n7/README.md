# Maximum cap in AG(7,3)

Determine a(7), the largest line-free set in AG(7,3). Three levels: this task, one folder per approach (each with its `prompt.md`), and a dated run folder per execution of an approach (each with `CLAIM.md`, the report, artifacts, and `SHA256SUMS`).

Frontier as of 2026-08: literature gives roughly 236 <= a(7) <= 288 (lower: Edel / Calderbank-Fishburn; upper: the 2022 no-289-cap claim, arXiv:2206.09804). A win here means a cap larger than 236 or a certified upper bound below 288.

## Approaches and runs

| approach | run | result | review |
|---|---|---|---|
| `01_baseline` (`[search]`) | `2026-08-01-chatgpt-pro` | 236 <= a(7) <= 291, reproduction (no record improvement) | self + agent; both bounds re-verified locally |
| `01_baseline` (`[search]`) | `2026-08-01-claude-code` | staircase reproduced (LP separators); a(2)..a(4) certified with drat-trim-VERIFIED proofs; exact Farkas certificate that every 237-cap has a slice >= 89; 237-cap search null (best E=10); no cap > 236 | self; no new bound on a(7), one new exact fact (>=89 floor) |

## Notes

- The `2026-08-01-chatgpt-pro` run reproduced the known 236-cap and independently re-derived the weaker exact upper bound 291. Both checked on a second setup (triple scan PASS; independent C++ upper checker PASS). It is a validated pipeline and a set of replayable certificates, not a frontier advance.
- The `2026-08-01-claude-code` run independently reproduced the 291..288 profile-reduction staircase with its own code and LP-derived separators (confirming the previously chat-only 290 and 288 numbers), ran a null lower-bound search (best greedy cap 145; local repair of the 236-cap found no improvement), and built a proof-logging toolchain (CaDiCaL + drat-trim) that certifies a(2) <= 4, a(3) <= 9, a(4) <= 20 with independently VERIFIED DRAT proofs. a(5) did not close in 300 s (1.0 GB proof). Calibration finding: past a(4), certification needs real symmetry engineering (lex/stabilizer breaking), not just a solver.
- Structural ceiling (from the difficulty analysis): the slice/profile method only bites in the near-maximal-slice regime, so the SAT staircase can reproduce <= 288 and perhaps <= 287, then stalls far above 236. Closing the 236-288 gap needs new mathematics, not solver time.
- The run pins this quantitatively: an exact Farkas certificate proves every 237-cap has a hyperplane slice >= 89, and the moment method cannot force >= 90, while the rigidity classifications only start near 110. The 89..110 gap is the verified core of the difficulty. A nonlocal 237-cap search found none (best E=10 violated lines).
- Next: this upper track is a certified *reproduction* of <= 288, not a path to the answer. A new result needs a 237+ construction (lower bound) or new structural mathematics. Weigh against pivoting the discovery effort to a higher-odds pilot.
