# 27. A witness meeting an open worst-case state complexity

**Find.** For a specified regular-language operation (or composition of two operations) whose exact worst-case deterministic state complexity is not settled, a pair/tuple of witness DFAs that push the state complexity of the result to (or above) the best known lower bound at fixed input sizes. Combined-operation state complexity (e.g. star-of-union, reversal-then-star, intersection-then-reversal) has several cases where the tight bound and its witnesses are open, especially over restricted alphabets (verify the target operation).

**What counts as a win.** Explicit input DFAs (with fixed state counts m, n and a fixed alphabet size) such that the minimal DFA for the operation's result has at least the target number of states, exceeding the best published witness for that alphabet size. One-sided: a stronger witness advances the lower bound.

**Checker (seconds).** Construct the result DFA by the standard construction (product / subset / reversal + subset), then minimize (Hopcroft) and count states; assert it meets the target. Determinism and exactness make this fast for m, n up to a few dozen and small alphabets.

**Search plan.** Structured/exhaustive: enumerate small DFAs (isomorph-reduced) as witness candidates over the fixed alphabet; evaluate the operation and record maxima; local search around near-maximal witnesses. Target minimal-alphabet cases where general-alphabet witnesses are known but small-alphabet ones are not.

**Prior art (verify).** Yu, Zhuang, Salomaa (1994) and the state-complexity surveys (Gao, Moreira, Reis, Yu, 2017); the "magic number" line (Iwama et al.; Geffert). Verify the specific operation/alphabet cell is still open.
