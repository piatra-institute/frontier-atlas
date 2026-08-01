# Magic square of distinct cubes at small order

**Find.** An additive magic square whose entries are distinct positive cubes, at the smallest order for which existence is open (3x3 semimagic, or a small fully magic square of cubes).

**What counts as a win (one-sided).** One square of distinct cubes with the required line sums equal (all lines for magic, rows and columns for semimagic). A single witness settles the case; failure proves nothing.

**Checker (seconds).** Assert every entry is a perfect cube (integer cube root), entries distinct, and the required line sums (rows, columns, and diagonals for magic) all equal. Constant time, exact integers.

**Search plan.** Sieve over cubes sharing a common line sum; for 3x3 use the magic parameterization plus cube constraints, reducing to a Diophantine system searched by descent / point search on the associated curves; ILP or CP over a bounded cube-value set for small orders. Seed from known cube identities (e.g., taxicab-type equal sums of cubes).

**Prior art (verify).** A 3x3 fully magic square of distinct cubes is known not to exist by a short arithmetic argument, but related cases (3x3 semimagic of cubes, small magic squares of cubes) are open, and record constructions are tracked. See Christian Boyer, www.multimagie.com, magic-squares-of-cubes pages, for the precise open cases (verify).
