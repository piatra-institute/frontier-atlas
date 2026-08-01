# Non-load-bearing exploration: CAN(3,7,3)

The preserved November 2024 upper-bound table lists a 39-row construction for seven ternary columns at strength 3. The supplied `search_minconf.cpp` uses focused min-conflicts: it repeatedly selects a missing 3-tuple and changes one row to realize it, choosing the least damaging row.

Results recorded in this package:

- `array_CA_39_3_7_3.csv` was found at seed 9 in 0.607070 seconds and independently coverage-checked.
- The \(N=38\) branch was run with multiple seeds. The best states had five uncovered 3-tuples, but no valid \(\mathrm{CA}(38;3,7,3)\) was found.

No inference of nonexistence is made from the failed \(N=38\) searches. This folder does not contribute to the certified \(\mathrm{CAN}(2,8,3)=13\) claim.
