# New Casas-Alvero counterexample over a finite field

**Find.** A monic polynomial f of degree n over F_q that shares a root with each derivative f', ..., f^(n-1) but is not (x - a)^n, at a pair (q, n) where no such counterexample is catalogued.

**What counts as a win (one-sided).** One polynomial over F_q with gcd(f, f^(i)) nonconstant for all i and more than one distinct root. A single new counterexample settles that (q, n) case; failure proves nothing.

**Checker (seconds).** Over F_q compute each gcd(f, f^(i)) (exact polynomial gcd in F_q[x]) and assert positive degree; assert f is not a single linear power (squarefree part has degree > 1). Exact finite-field arithmetic, sub-second.

**Search plan.** Enumerate monic f of degree n over small F_q up to affine substitution x -> ax + b and scaling, testing the gcd conditions (the group action shrinks the space sharply). For larger q, restrict to f with prescribed root multiplicity patterns; use the derivative-vanishing conditions as linear/algebraic constraints over F_q. Reuse known characteristic-p families as seeds.

**Prior art (verify).** The Casas-Alvero statement is false over finite fields, with counterexamples known in characteristic p (Graf von Bothmer, Labs, Schicho, van de Woestijne, ca. 2007; and later work). A full classification is not known, and specific (q, n) cases are open. Confirm the target pair has no catalogued example (verify).
