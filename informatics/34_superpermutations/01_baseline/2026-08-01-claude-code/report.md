# Superpermutation s(6): verifier + greedy construction

Run by Claude Code (Opus), 2026-08-01. A pilot on the open case n=6
(867 <= s(6) <= 872). No new result: a valid but suboptimal superpermutation.

## What was established

- An exact verifier (`verify`): a string over {1..n} is a superpermutation iff all
  n! permutations occur as length-n substrings. Self-certifying.
- A max-overlap greedy construction (`greedy`), validated against the known exact
  minima: n=1..5 give 1, 3, 9, 33, 153, all optimal and valid.
- For n=6 the greedy gives a **valid** superpermutation of length **873**
  (= sum_{k<=6} k!), verified (all 720 permutations present).

## Honest verdict

873 does not beat, or even match, the record 872 (Houston), and is well above the
867 lower bound. The greedy stops being optimal exactly at n=6, which is why n=6 is
the first open case. Matching 872, let alone pushing toward 867, needs a dedicated
search (Chaffin method, or asymmetric-TSP / large-neighborhood over permutation
overlaps), not plain greedy. That search was not run here.

## Denominator

- One max-overlap greedy construction, < a few seconds. No search sweep, no
  solver. Best length 873; record 872; gap to beat = 1 (to reach 871), gap to the
  lower bound = 6.

## Next steps

- Implement a Chaffin-method depth-first search or an ATSP/LNS over the 720-node
  permutation-overlap graph, seeded from the 873 greedy string, to try to shave to
  871 or below. Any shorter valid string is instantly certified by `verify`.
