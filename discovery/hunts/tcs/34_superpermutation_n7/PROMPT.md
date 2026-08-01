# 34. A superpermutation of 7 symbols shorter than 5906

**Find.** A superpermutation on n = 7 symbols of length strictly less than 5906. A superpermutation contains every one of the n! permutations of {1..n} as a contiguous substring. For n = 7 the best known upper bound is 5906 (Egan, using Houston's ideas, 2019) and the best lower bound is 5884; the exact minimum is unknown, so any string below 5906 that still contains all 5040 permutations is a new record.

**What counts as a win.** One explicit string over {1..7} of length < 5906 that contains all 5040 permutations as substrings. One-sided: exhibiting a shorter valid superpermutation beats the record; no matching lower bound is needed.

**Checker (seconds).** Slide a length-7 window across the string; collect every window that is a permutation of {1..7} into a set; assert the set has all 5040 permutations. Assert the total length is below 5906. Hashing windows is O(length), microseconds.

**Search plan.** Structured: model as a shortest-covering-walk / asymmetric-TSP over the 5040 permutations with weighted overlaps and search for improved patchings of the Egan/Houston construction; local search (Lin-Kernighan-style) on the permutation ordering; SAT/CP for short local reorderings that shave symbols.

**Prior art (verify).** Houston, Egan, and the anonymous 4chan lower bound (2011); Quanta coverage (2019); OEIS A180632. UB 5906, LB 5884 for n=7 (verify current values); exact minimum open for n >= 6? (n=6 minimum is 872, proven; n >= 7 open).
