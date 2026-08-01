# Claim

**Claim.** Independent verification of the sibling `2026-08-01-chatgpt-pro` result
R_F2(<2,2,3>) = 11 (a known value; no new result), by two methods distinct from
their package.
1. **Upper bound R <= 11: independently confirmed.** `upper_recheck.py` (our own,
   self-contained) checks the 11-product F2 algorithm against true 2x2-by-2x3
   multiplication for all 1024 input pairs: 0 mismatches.
2. **Lower bound R >= 11: method validated, target not closed.** We attack the
   lower bound by a completely different route than their substitution certificate:
   encode "a rank-R decomposition exists over F2" as SAT and seek UNSAT with a
   drat-trim-checked proof. The encoder is validated: it proves the classical
   Strassen bound R_F2(<2,2,2>) >= 7 (R=6 UNSAT, drat-trim VERIFIED, 0.2 s) and
   confirms <2,2,3> R=11 is SAT (12.7 s). But <2,2,3> R=10 UNSAT did **not** close
   in 600 s (CaDiCaL timeout, 1.3 GB partial proof). So our independent lower bound
   is incomplete; R >= 11 still rests on the chatgpt-pro substitution certificate,
   which replays here (`verify_all.sh`: ALL CHECKS PASSED).

Net: the upper bound is now ours independently; the lower bound is independently
validated in method (Strassen) but not re-closed for <2,2,3> in budget. This is a
verification of a settled value, not a new result.

**Checker.**
- `python3 src/upper_recheck.py` (upper, exact over 1024 inputs; re-run 2026-08-01: 0 mismatches).
- `python3 src/sat_bilinear_lb.py $(command -v cadical) tools/drat-trim proofs 2 2 2 6 120` reproduces Strassen R>=7 (UNSAT + drat-trim VERIFIED).
- The sibling run's `verify_all.sh` for the full R=11 certificate.
- Toolchain: Python 3.12, CaDiCaL 3.0.1 (brew), drat-trim (built from `tools/drat-trim.c`).

**Trust base.** Upper bound: exact F2 arithmetic over all inputs, no solver, fully independent. SAT lower bound: CaDiCaL is not trusted (its DRAT proof is checked by the independent drat-trim); trust base is drat-trim, the CNF encoding (Tseitin AND for products, XOR parity for tensor coefficients, lex ordering to break the S_R triple symmetry), and the structure-tensor definition. The <2,2,3> lower bound is not established by us (timeout); it relies on the sibling substitution certificate.

**Review level.** self. Independent verification of the agent (chatgpt-pro) run. Not human-refereed.

**Provenance.** Claude Code (Opus), 2026-08-01. Independent second implementations; no code imported from the chatgpt-pro package.

**Cost and attempts.** Local, no model spend. Upper < 1 s; Strassen R=6 0.2 s / R=7 0.1 s; <2,2,3> R=11 12.7 s (SAT); R=10 600 s timeout (not closed). DRAT proofs are regenerable and git-ignored; the `.cnf` inputs and the VERIFIED verdicts in `certificates/` are tracked.
