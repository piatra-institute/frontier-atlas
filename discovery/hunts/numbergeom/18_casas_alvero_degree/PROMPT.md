# Casas-Alvero counterexample at an open degree

**Refute.** The Casas-Alvero conjecture at a degree n where it is not settled: find a monic polynomial f of degree n over Q (or C) that shares a common root with each of its derivatives f', f'', ..., f^(n-1) yet is not of the form (x - a)^n.

**What counts as a win (one-sided).** One polynomial with gcd(f, f^(i)) nonconstant for every i in 1..n-1 that is not a pure n-th power. A single counterexample refutes the conjecture at that degree; failure proves nothing.

**Checker (seconds).** Over Q, compute gcd(f, f^(i)) for i = 1..n-1 (exact polynomial gcd) and assert each has positive degree; assert f is not (x - a)^n by checking f has more than one distinct root (squarefree part nonlinear). Exact rational arithmetic, sub-second.

**Search plan.** Set up the algebraic variety of counterexamples: f monic of degree n with the n-1 shared-root conditions gives a polynomial system; compute its Groebner basis / eliminate to test for solutions off the diagonal (x - a)^n. Use Macaulay2 / Singular. Numerical homotopy to locate candidate roots, then certify exactly.

**Prior art (verify).** The Casas-Alvero conjecture is proven for degrees that are prime powers and small multiples thereof (Graf von Bothmer, Labs, Schicho, van de Woestijne, ca. 2007) and verified computationally for small degrees, but remains open in general. Target the smallest degree outside the proven and computationally verified range (verify the current frontier).
