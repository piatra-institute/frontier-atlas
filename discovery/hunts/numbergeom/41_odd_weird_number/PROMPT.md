# An odd weird number

**Find.** An odd weird number: an odd integer n that is abundant (sigma(n) > 2n) but not pseudoperfect (no subset of its proper divisors sums to n).

**What counts as a win (one-sided).** One odd n that is abundant and has no divisor subset summing to n. A single witness settles the long-open existence question; failure proves nothing.

**Checker (seconds).** Factor n (candidates are smooth by construction, so factoring is easy), list proper divisors, confirm their sum exceeds n (abundant), then confirm no subset of the proper divisors sums to n via a subset-sum / dynamic-program up to n (or meet-in-the-middle when the divisor count is large). Exact integer arithmetic.

**Search plan.** Odd weird numbers, if any, are abundant with a divisor set whose subset sums miss n exactly; target odd abundant numbers with few, large prime factors (these have sparse divisor sets and are the best candidates), and test the subset-sum non-representability. Sieve odd abundant n in ranges beyond prior searches; the subset-sum test is the gate.

**Prior art (verify).** No odd weird number is known; searches have excluded them up to large bounds (into the 10^21 range and beyond in some accounts), and existence is a well-known open problem. See Benkoski-Erdos (weird numbers), OEIS A006037 (weird) and the odd-weird literature. Open; being false (none exist) is plausible, so treat the hunt as high-risk (verify the current bound).
