# Multimagic square below the record order

**Find.** A bimagic or trimagic square of order smaller than the smallest known: a square of distinct integers that stays magic after replacing every entry by its square (bimagic) or by its square and its cube (trimagic), at an order below the current minimum.

**What counts as a win (one-sided).** One magic square of order m (below the record) whose entrywise-squared (and, for trimagic, entrywise-cubed) array is also magic. A single witness lowers the minimum order; failure proves nothing.

**Checker (seconds).** Assert the base array is magic (all line sums equal, entries distinct), then assert the squared array is magic, and for trimagic the cubed array too. O(m^2), exact integers.

**Search plan.** For a fixed small order, encode the base entries as a permutation of a chosen value set and impose the linear equal-sum constraints at degree 1, 2 (and 3) via CP/SAT or ILP; use symmetry breaking on the square. Evolutionary search scored by the sum of line-sum variances across the powers.

**Prior art (verify).** The smallest known bimagic square has order 8 and the smallest known trimagic square has order 12 (constructions by Christian Boyer, Walter Trump). Whether smaller orders are impossible is not fully settled in all cases. See www.multimagie.com, smallest-multimagic-squares pages, for the exact open orders (verify before starting).
