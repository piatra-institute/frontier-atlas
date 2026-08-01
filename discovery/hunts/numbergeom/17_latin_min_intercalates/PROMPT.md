# Latin square with fewer intercalates than the best known

**Find.** A Latin square of order n whose number of intercalates (2x2 Latin subsquares) is strictly below the best published value for that n, for an order where the exact minimum is unknown.

**What counts as a win (one-sided).** One order-n Latin square with intercalate count below the current record. A single square beats the record; failure proves nothing.

**Checker (seconds).** Count intercalates: for every pair of rows and pair of columns, test whether the 2x2 submatrix is a Latin subsquare; equivalently count ordered pairs of cells forming a 2x2 cycle. O(n^3) with a symbol-position index; exact.

**Search plan.** Simulated annealing over Latin squares (via row/column/symbol moves that preserve the Latin property) minimizing intercalate count; start from group-table and Steiner-quasigroup based squares that are intercalate-poor; targeted local moves that destroy intercalates without creating new ones. CP with an objective on the 2x2-cycle count.

**Prior art (verify).** The asymptotic minimum number of intercalates in an order-n Latin square was recently determined (Kwan, Sah, Sawhney, Simkin, ca. 2022), but exact minima for many specific small n are open and tabulated only as bounds. See that work and OEIS entries for intercalate-minimal Latin squares. Confirm the target n is open (verify).
