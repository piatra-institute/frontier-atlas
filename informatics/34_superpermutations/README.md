# Shortest superpermutation of n symbols

Determine s(n), the length of the shortest string over {1..n} containing all n!
permutations as contiguous substrings. Levels: this task, one folder per approach
(`prompt.md`), and a dated run folder per execution.

Frontier: s(1..5) = 1, 3, 9, 33, 153 (exact). n=6 is the first open case,
867 <= s(6) <= 872 (upper bound Houston). A win is a valid string shorter than 872.

## Approaches and runs

| approach | run | result | review |
|---|---|---|---|
| `01_baseline` (`[search]` `[opt]`) | `2026-08-01-claude-code` | verified max-overlap greedy: optimal for n<=5, length 873 for n=6 (record 872 not beaten) | self; no new result |

## Notes

- The `2026-08-01-claude-code` run built an exact verifier and a max-overlap greedy
  construction. Greedy is optimal through n=5 and gives 873 = sum k! at n=6, one
  above the record. Matching 872 or reaching 867 needs a dedicated search
  (Chaffin method / ATSP / large-neighborhood), not run here.
