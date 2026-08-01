# 3x3 magic square of distinct perfect squares

**Find.** A 3x3 magic square whose nine entries are distinct perfect squares: nine distinct integers a_ij = s_ij^2 with all three rows, three columns, and both diagonals summing to the same value.

**What counts as a win (one-sided).** One 3x3 array of distinct squares with all eight line sums equal. A single witness settles the existence question; failure proves nothing.

**Checker (seconds).** Assert all nine entries are perfect squares (isqrt), distinct, and that all three row sums, three column sums, and two diagonal sums are equal. Constant time; exact integers.

**Search plan.** A 3x3 magic square is parameterized by center c and two generators, so entries lie on an arithmetic structure; search rational points on the associated elliptic-curve conditions forcing extra entries to be squares. Also: direct sieve over squares with common magic sum; constraint solver over s_ij with the eight equal-sum equations plus square constraints. Known near-misses have up to seven square entries; the target is nine.

**Prior art (verify).** Martin Gardner popularized this as an open problem with a standing prize. Christian Boyer's site www.multimagie.com documents the state of the art, near-misses (seven-square magic squares), and the open question of whether a fully-square 3x3 magic square exists. Open (verify at multimagie.com).
