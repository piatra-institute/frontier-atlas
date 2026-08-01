# 35. A sorting network on 13 inputs with fewer than 46 comparators

**Find.** A sorting network on n = 13 channels using fewer than 46 comparators (or a new best for n = 14, 15, 16, whose optimal sizes are likewise open). The optimal sizes for n <= 12 are now settled (n=11: 35, n=12: 39, proven 2020-2021); n = 13 is the smallest open case, with 46 the best known upper bound. Any correct 13-channel network below 46 comparators improves the record.

**What counts as a win.** One explicit comparator sequence (list of (i, j) compare-exchange pairs) on 13 wires of length < 46 that sorts every input. One-sided: a shorter sorting network is a new upper-bound record; no lower bound is required.

**Checker (seconds).** Zero-one principle: apply the comparator sequence to all 2^13 = 8192 binary inputs and assert each output is sorted (nondecreasing). 8192 x 46 operations, milliseconds, exact. This certifies the network sorts all inputs.

**Search plan.** Structured: start from the known 46-comparator network and apply local "generalize/optimize" moves (comparator removal + repair) verified by the 0-1 test; SAT/CP encodings for the last few layers (prefix-fixed, suffix-searched) as in Codish-Cruz-Frank-Itzhakov; evolutionary search over comparator sequences with the 0-1 objective.

**Prior art (verify).** Knuth TAOCP vol. 3; Codish, Cruz-Filipe, Frank, Schneider-Kamp on optimal-size networks; Bose-Nelson problem settled for n=11,12 (arXiv 2012.04400). n=13 best-known 46 (verify current record).
