# 38. A long word settling an open avoidability question

**Find.** For a specified open word-avoidance question, a witness word: a long (ideally arbitrarily extendable via an explicit morphism) word over a k-letter alphabet avoiding the target pattern/repetition, or a proof no such word exists past a computed length. Candidates: avoidability of a pattern with reversal/permutation, generalized repetition thresholds (fractional powers) over small alphabets, or simultaneous avoidance of two patterns where the k-avoidability index is unknown (verify the target).

**What counts as a win.** For the existence side: an explicit uniform morphism h and letter such that the fixed point h^omega avoids the pattern (checked to be pattern-avoiding by a finite argument), OR a single long avoiding word beyond the current known length. One-sided in the direction claimed by the open question.

**Checker (seconds).** Generate a long prefix (millions of symbols) of the candidate word (iterate the morphism); scan for any occurrence of the forbidden pattern/repetition with a suffix-automaton or direct window check; assert none occurs. For morphic words, additionally verify the standard "no short violation implies none" bound for the pattern. Exact string processing.

**Search plan.** Structured: search uniform morphisms of small size whose fixed points avoid the pattern (backtracking over morphism images, pruned by early violations); for the non-existence side, exhaustively generate the avoidance tree up to the branching-death length.

**Prior art (verify).** Thue (square-free words); Dejean's theorem (repetition thresholds, proved 2009) and its open generalizations; Currie, Rampersad, Shallit on pattern avoidance; specific open avoidability indices in Cassaigne's and later problem lists (verify the target is still open).
