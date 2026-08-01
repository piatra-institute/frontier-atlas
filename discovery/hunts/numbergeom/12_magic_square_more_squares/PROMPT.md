# 3x3 magic square with eight square entries

**Find.** A 3x3 magic square with at least eight of its nine entries perfect squares (all entries distinct, all eight line sums equal), improving on the best published count of square entries.

**What counts as a win (one-sided).** One magic square with eight (or nine) square entries. A single such square beats the current record; failure proves nothing.

**Checker (seconds).** Assert the array is magic (eight equal line sums, distinct entries) and count entries that are perfect squares (isqrt); assert the count is at least eight. Constant time, exact integers.

**Search plan.** Parameterize 3x3 magic squares by center and two step sizes; impose that eight chosen entries are squares, reducing to rational points on a curve; use elliptic-curve / Diophantine search (descent, point search) on the resulting system. Complement with a sieve pairing squares that share a magic sum.

**Prior art (verify).** The best documented 3x3 magic squares reach seven perfect-square entries (constructions attributed to Andrew Bremner and others). Whether eight, let alone nine, is achievable is open and prize-backed. See Christian Boyer, www.multimagie.com, magic-squares-of-squares pages. Open (verify).
