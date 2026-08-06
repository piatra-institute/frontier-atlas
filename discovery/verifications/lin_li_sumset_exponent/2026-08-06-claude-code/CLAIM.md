# Claim

**Claim.** Verification of an external result, not a new one. The load-bearing combinatorial
steps of Lin and Li, "Settling the Optimal Exponent Relating Sumsets and Difference Sets"
(arXiv:2607.27199v1, 29 Jul 2026) were independently re-derived here and all hold. 69 checks,
0 failures. This does not certify the paper; see "Not checked" below.

**What the paper claims.** For finite nonempty `A` in an abelian group, `sigma(A) = |A+A|/|A|`
and `delta(A) = |A-A|/|A|` satisfy `sigma^(1/2) <= delta <= sigma^2`. Exponent 2 was known
optimal; exponent 1/2 was open. With `C(A) = log sigma(A) / log delta(A) <= 2`, the paper gives
explicit `A_K` in Z with `C(A_K) > 2K/(K+3)` for every positive even K, so `sup C(A) = 2` and
1/2 is optimal. Corollary 2.1 (via Staps): the supremum is not attained.

**Checked (`verify.py`, all pass).**
- Section 2.1: `(W+W) mod 12 = Z/12Z` and `(W-W) mod 12 = Z/12Z` minus `{6}` for
  `W = {0,1,2,4,5,9}`; the integer difference set `Delta = W-W` exactly as printed; `|Y_j| = 6^j`
  and Lemma 2.1 by direct enumeration, `j <= 4`.
- Lemma 2.2: the carry automaton rebuilt from its definition reproduces transition matrix (7)
  exactly as `[[5,3,3],[4,5,3],[4,4,4]]`, with no reachable carry-set outside `{X1,X2,X3}`;
  `t_j = e1^T M^j 1` agrees with brute-force `|(Y_j - Y_j) mod 12^j| = 1, 11, 127, 1475, 17143`;
  the recurrence `t_{j+2} = 13 t_{j+1} - 16 t_j` and closed form (5) both reproduce those values;
  `(M^2 - 13M + 16I)1 = 0`; coefficients in (5) positive and summing to 1 with `0 < mu < lam`.
- Lemma 2.3: `lambda/12 < 31/32` and `(31/32)^22 < 1/2`.
- Lemma 2.4 for `K = 2, 4, 6, 8`: `H cap V = {0}`, `|I| = 2s-1`, `I = -I`, `I+I = Z/QZ`, and every
  `x` outside `I` lies in both `B+B` and `B-B`. Also `s = 2 (mod 3)`, the paper's CRT
  coprimality step.
- Lemmas 2.5, 2.6, 2.7 and size formula (14), exactly, on five scaled-down `(K,d)` instances:
  `(2,2), (2,3), (4,2), (4,3), (6,2)`. These lemmas are stated for general `K` and `d`, so small
  `d` is a genuine test of them. The paper's own `d = 22(K+2)` is unenumerable.

**Not checked.** The Lean development at github.com/linhaowei1/sum-diff-proof (repo exists,
language Lean, pushed 2026-07-30; contents not inspected). The final assembly of Theorem 1.1 and
Corollary 2.1 was read, not machine-checked; Staps' equality characterization was not consulted.
The paper's historical baseline claims, in particular that Penman-Wells (2013) stood at 1.125944
under the same normalization while AlphaEvolve reported 1.1219 against a 1.0598 baseline, were
not independently confirmed: only that Lin and Li assert them.

**Reading caveat.** `pdftotext` drops superscripts and renders `s = 2^K + 1` as `2K+1`. That
reading is inconsistent with the paper's own `2^K = 1 (mod 3)` and `alpha = 2^(K+1-d)` steps and
makes Lemma 2.4 fail the CRT coprimality condition at `K = 4`. The correct reading was confirmed
against arxiv.org/html/2607.27199v1. Use the HTML for this paper.

**Trust base.** Exact integer and set arithmetic throughout; `numpy` used only with dtype=object
for exact integer matrix powers. The two floating-point checks (closed form (5), Lemma 2.3) have
margins far above double precision. Every check is deterministic and exhaustive over its stated
range; `verify.py` exits nonzero on any failure.

**Why this was done.** Not to attack the problem, which is settled. The atlas's `FRONTIER_LOG.md`
records this result at status `checked`, and that status requires a replayable re-derivation. The
result's value to the atlas is methodological and recorded there: Table 1 of the paper is a
public ledger of eight agent systems plateauing at 1.079-1.145 by enumerating explicit integer
sets, in a region that could not contain the answer, since the smallest record-beating `A_K` has
about `10^143` elements.

**Review level.** self. Re-derived by Claude Code from the paper's definitions, not by rerunning
any author-supplied code. Not human-refereed.

**Provenance.** Source arXiv:2607.27199v1 (29 Jul 2026), PDF and HTML both fetched 2026-08-06.
This run: Claude Code (Opus 5), 2026-08-06. `run.log` is regenerable output of `verify.py`.
