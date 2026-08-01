# Cyclic difference set at an open parameter

**Find.** A (v, k, lambda) cyclic difference set at a parameter triple flagged "existence open" in the difference-set tables: a k-subset D of Z_v such that every nonzero element of Z_v is a difference d_i - d_j in exactly lambda ways.

**What counts as a win (one-sided).** One k-subset D whose difference multiset covers each nonzero residue exactly lambda times. A single set settles existence for that triple; failure proves nothing.

**Checker (seconds).** Compute all ordered differences of D mod v, tally, assert every nonzero residue has count lambda. O(k^2). Exact modular arithmetic; re-check from raw D.

**Search plan.** Exploit multiplier theorems: a numerical multiplier of the putative set fixes it, so search only multiplier-invariant unions of orbits, collapsing the space. Backtracking with partial-difference pruning; SAT/CP encoding the constant-difference condition. Seed from cyclotomic and Singer-type constructions near the target parameters.

**Prior art (verify).** The La Jolla Difference Set Repository (Daniel Gordon) lists (v, k, lambda) triples that pass known nonexistence tests (Bruck-Ryser-Chowla, multiplier obstructions) but whose existence is undecided. See Gordon's repository and Lander, "Symmetric Designs: An Algebraic Approach." Pick a currently open triple with small v; status open (verify at the repository before starting).
