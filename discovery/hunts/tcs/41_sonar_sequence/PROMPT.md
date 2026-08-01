# 41. A sonar sequence (2D distinct-difference array) at an open size

**Find.** A sonar sequence of size m x n at parameters where existence is open. A sonar sequence is an m x n array with exactly one mark per column such that all n(n-1)/2 difference vectors between marks in distinct columns are distinct (a Costas-array relaxation allowing rectangular arrays and no row constraint). Existence tables for m x n sonar sequences have gaps analogous to the Costas-array gaps; specific (m, n) are unresolved (verify the target).

**What counts as a win.** One explicit function c: {1..n} -> {1..m} (the row of the mark in each column) whose difference vectors (j - i, c(j) - c(i)) over all i < j are pairwise distinct. One-sided: a single array settles existence for that (m, n).

**Checker (seconds).** Enumerate all C(n,2) pairs, form the vectors (j - i, c(j) - c(i)), and assert they are pairwise distinct (hash into a set, check for collisions). O(n^2), microseconds. Exact integer.

**Search plan.** Structured: local search / backtracking with the distinct-difference constraint and strong pruning (as for Costas arrays); derive candidates from Welch/Golomb Costas generators of nearby orders by deleting rows/columns and repairing; SAT/CP with all-different difference-vector constraints.

**Prior art (verify).** Golomb & Taylor, "Two-dimensional synchronization patterns for minimum ambiguity" (sonar sequences, 1982); Costas-array open-problems literature (Drakakis). Verify the target (m, n) is still open in the sonar-sequence existence tables.
