# 33. Periodicity of Grundy's game (or an unsettled octal game)

**Find.** A period (with pre-period) for the Sprague-Grundy sequence of Grundy's game (split a heap into two unequal nonempty heaps), or of a specified unsettled octal game from Flammenkamp's list (e.g. 0.6 "Officers," 0.06, or another "?"-marked code such as 0.104, 0.156). Grundy's game has been computed to many billions of values with no period found; its ultimate periodicity is a classic open problem.

**What counts as a win.** A stated pre-period, period P, and (for octal games) saltus, plus the finite periodicity certificate. One-sided: a verified periodic stretch to the Guy-Smith bound proves eventual periodicity forever. As with Treblecross, expectations are that no small period exists; the value here is a clean, finitely-checkable win *if* one appears.

**Checker (seconds-to-minutes).** Recompute the nim-values via the game's move/split rule up to 2*(pre-period + P) + (max heap referenced); assert G(n + P) = G(n) across the range. Grundy's game uses the splitting-move mex (over all unequal splits); octal games use their code's digits. Exact integer.

**Search plan.** Structured: high-throughput nim-value computation (bit-parallel mex, sparse-space acceleration a la Flammenkamp); prefix-scan for candidate periods; test the periodicity condition. Report the frontier and any candidate (p0, P) that survives partial testing.

**Prior art (verify).** Grundy's game periodicity (open; billions of values computed, e.g. by Flammenkamp); Guy & Smith arithmetic periodicity; Flammenkamp's octal-games page and unsettled.txt (65 unsettled 2-place + 8 3-place games); Guy, "Unsolved Problems in Combinatorial Games."
