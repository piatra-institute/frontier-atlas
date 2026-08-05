# Claim

**Claim.** No counterexample found. B1 (computational corroboration). Conjecture 4.1 of
arXiv:2606.26509v2 (Xu, Das, Bera, "Structural Properties and Applications of the Augmented
Sombor Index") conjectures that the balanced Turan graph `T_n(k)` maximizes the augmented
Sombor index `ASO(G) = sum_{uv in E} sqrt((d_u^2+d_v^2)/(d_u+d_v-2))` over all k-partite
graphs of order n, with equality only for `T_n(k)`. Three independent refutation routes were
run; all failed. The conjecture stands, with new computational support in the ranges below.

**Statement provenance.** The conjecture was pinned by extracting text directly from the
source PDF (arXiv:2606.26509v2, Section 4, "Concluding Remarks and Future Work"), not from a
paraphrase. Verbatim framing sentence: "We conjecture that `T_n(k)` attains the maximum ASO
value among all k-partite graphs of order n." The displayed closed-form right-hand side of
Conjecture 4.1 is typographically fragile under text extraction, so the invariant form
`ASO(G) <= ASO(T_n(k))` was used; that form is what the paper's own framing sentence asserts
and is what the equality case `G = T_n(k)` refers to.

**Checker / routes run.**
1. `aso_probe.py` - all complete k-partite graphs, i.e. every partition of n into k parts,
   `2 <= k <= 6`, `k <= n <= 60`. Closed form per partition: parts `n_i`, degrees `n - n_i`,
   `n_i*n_j` edges between parts i and j. Result: the balanced partition is the strict maximum
   in every case. No unbalanced partition beats Turan.
2. `aso_probe2.py` (a) - delete a single edge from `T_n(k)`, all edges, `2 <= k <= 5`,
   `k < n <= 40`. Result: no single-edge deletion raises ASO.
3. `aso_probe2.py` (b) - hill-climbing on edge toggles within a fixed balanced k-partition,
   from `T_n(k)` and from 3 random 0.7-density starts, `2 <= k <= 4`, `k+2 <= n <= 24`.
   Result: every climb terminates at `T_n(k)`; no k-partite graph found exceeding it.

**Why these routes.** The ASO edge term is not monotone in the degrees: for
`f(x) = (x^2+c^2)/(x+c-2)`, `f'(x) < 0` when `x < 2-c+sqrt(2c^2-4c+4)` (e.g. `x < 4.81` for
`c = 10`). So raising a low degree adjacent to a high-degree vertex lowers that edge's term,
and edge deletion can in principle raise ASO. That non-monotonicity is the conjecture's
plausible failure mode, and routes 2 and 3 target it directly. It did not materialize.

**Trust base.** Double precision; margins are large (the balanced-vs-unbalanced gaps are
order 1 or more, far above 1e-9 tolerances), so floating point is not load-bearing. Route 1 is
exhaustive over its stated range. Routes 2 and 3 are complete (route 2) and heuristic (route 3)
respectively, so they are evidence, not proof.

**Scope limits (not covered).** Non-complete k-partite graphs on an *unbalanced* partition were
not searched: route 1 covers unbalanced-but-complete, route 3 covers non-complete-but-balanced.
No exhaustive enumeration over all k-partite graphs was done at any n. `k >= 7`, `n > 60`
(route 1), `n > 40` (route 2), `n > 24` (route 3) are untested. Disconnected graphs and graphs
with a `K_2` component are excluded, since the denominator `d_u+d_v-2` vanishes there.

**Review level.** self + agent. Target scouted by ChatGPT Pro (card
`augmented-sombor-kpartite-turan-extremal`, `needs-edge`); statement pinned from the source PDF
and all routes implemented and run by Claude Code. Not human-refereed. Not sent to the authors.

**Provenance.** Source arXiv:2606.26509v2 (v1 2026-06-25, v2 2026-07-22). Scout 2026-08-02.
This run: Claude Code (Opus), 2026-08-05.

**Cost and attempts.** Three routes, about 20 minutes total on one core, no tuning. Outcome:
no counterexample; the conjecture gains computational support it did not previously have (the
source states no exhaustive verification range). This is the atlas's 7th deep attempt and 7th
non-discovery. Value delivered: a fast, cheap, decisive null, and an author-absorbable
corroboration note.
