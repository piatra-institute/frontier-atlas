# PROMPT FOR A CERTIFIED CASAS–ALVERO RESOLUTION AT AN OPEN DEGREE

## The Casas–Alvero conjecture: a polynomial sharing a root with every derivative is a pure power

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 41 of 50  
**Area:** number theory & algebra  
**Modes:** `[sym]` `[cert]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The Casas–Alvero conjecture asserts that, over a field of characteristic \(0\), a degree-\(n\)
polynomial \(f\) that shares a common root with each of its derivatives
\(f',f'',\dots,f^{(n-1)}\) must be \(f=c(x-a)^n\) - a single \(n\)-fold root. It is proved when
\(n\) is a prime power or twice a prime power (Graf von Bothmer–Labs–Schicho–van de Woestijne and
others), leaving composite \(n\) not of that shape open, the smallest being \(n=12\). The problem is
a crisp algebraic sibling of the Jacobian conjecture (#10): it is a **finite polynomial-system
question** - the shared-root conditions are resultant equations in the coefficients - so it is
matched to **symbolic elimination** (Gröbner bases, resultants) producing a **machine-checkable
certificate** (a Nullstellensatz certificate over \(\mathbb Q\)) that the ideal forces the pure
power. The resolution standard in section 2 is the target for a specific open degree; a numerical
or modular-only computation, or a proof for an already-settled degree, is reported as a partial
result and never represented as resolving the conjecture.

## 1. Exact problem statement

Fix a field \(K\) of characteristic \(0\) (take \(K=\mathbb Q\) with algebraic closure
\(\overline{\mathbb Q}\); the statement is characteristic-\(0\) invariant). Let
\[
f(x)=x^{n}+c_{n-1}x^{n-1}+\dots+c_1x+c_0\in K[x]
\]
be monic of degree \(n\ge 2\). For \(1\le i\le n-1\) write \(f^{(i)}\) for the \(i\)-th derivative.

**Shared-root condition.** \(f\) and \(f^{(i)}\) share a common root in \(\overline K\) iff
\(\gcd(f,f^{(i)})\neq 1\) iff \(\operatorname{Res}_x\!\bigl(f,f^{(i)}\bigr)=0\).

**Casas–Alvero conjecture.** If \(\operatorname{Res}_x(f,f^{(i)})=0\) for **all** \(1\le i\le n-1\),
then \(f(x)=(x-a)^n\) for some \(a\in\overline K\) (equivalently, over \(K\) with the monic
normalization, \(f=(x-a)^n\) with \(a\in K\)).

**Normalization to a finite variety.** Translating \(x\mapsto x-\tfrac{c_{n-1}}{n}\) (legitimate in
characteristic \(0\)) removes the degree-\((n-1)\) term, so we may assume \(c_{n-1}=0\); the pure-power
solution becomes \(f=x^n\), i.e. \(c_{n-2}=\dots=c_0=0\). Set variables \(\mathbf c=(c_0,\dots,c_{n-2})\)
and
\[
R_i(\mathbf c)\;=\;\operatorname{Res}_x\!\bigl(f,f^{(i)}\bigr)\in\mathbb Z[\mathbf c],
\qquad 1\le i\le n-1,
\]
each an integer polynomial (weighted-homogeneous under the grading \(\deg c_j=n-j\)). Define the
**Casas–Alvero ideal**
\[
I_n=\bigl(R_1,\dots,R_{n-1}\bigr)\subseteq \mathbb Q[c_0,\dots,c_{n-2}].
\]
Every \(R_i\) vanishes at the origin. The conjecture for degree \(n\) is exactly:
\[
V\bigl(I_n\bigr)=\{\mathbf 0\}\ \text{ in }\ \overline{\mathbb Q}^{\,n-1},
\]
equivalently \(\sqrt{I_n}=\mathfrak m:=(c_0,\dots,c_{n-2})\), the maximal ideal at the origin.

A degree \(n\) is **open** when it is not a prime power \(p^k\) and not \(2p^k\); the smallest open
degree is \(n=12\), followed by \(15,20,21,24,\dots\) (**verify** the full ordering).

## 2. Resolution standard

A **complete resolution for degree \(n\)** is a proof of \(V(I_n)=\{\mathbf 0\}\) over
\(\overline{\mathbb Q}\), delivered with an **independently checkable exact certificate**. The
accepted certified form is a **Nullstellensatz certificate over \(\mathbb Q\)**: for each variable
\(c_j\) an exponent \(m_j\ge 1\) and explicit polynomials \(g_{ji}\in\mathbb Q[\mathbf c]\) with
\[
c_j^{\,m_j}\;=\;\sum_{i=1}^{n-1} g_{ji}\,R_i,
\]
proving \(c_j\in\sqrt{I_n}\). Since each \(R_i\in\mathfrak m\), this yields \(\sqrt{I_n}=\mathfrak m\),
hence \(V(I_n)=\{\mathbf 0\}\). The certificate is verified by **exact polynomial expansion** (a
second CAS), independent of the Gröbner engine that produced it. Equivalent accepted forms: a reduced
**Gröbner basis** of \(I_n\) over \(\mathbb Q\) whose staircase proves \(\mathbb Q[\mathbf c]/I_n\) is
finite-dimensional and supported only at the origin, **together with** the membership certificates
above; and a **Lean 4** proof that checks such a certificate. Resolving a single specified open degree
\(n\) (e.g. \(n=12\)) is a complete resolution *for that degree* - a genuine new theorem - not of the
conjecture in general.

**Not accepted as resolution.**
- A Gröbner computation trusted as a black box with no membership/Nullstellensatz certificate.
- A computation done **only** modulo primes \(p\) (\(V(I_n\bmod p)=\{\mathbf 0\}\)); bad primes and
  lifting make this evidence, not a proof over \(\mathbb Q\).
- Floating-point or numerical-homotopy solution counts presented as an existence/uniqueness proof.
- A proof for a degree already covered by \(p^k\)/\(2p^k\) dressed as progress on an open degree.
- A partial result (zero-dimensionality, a solution-count bound) presented as the full \(V(I_n)=\{\mathbf0\}\).
- Set-theoretic \(V(I_n)=\{\mathbf0\}\) claimed from a numerical Gröbner basis with inexact coefficients.

## 3. Graded partial-result targets

**P1 - Validate the pipeline on settled degrees.** Recompute \(I_n\) and produce full Nullstellensatz
certificates proving \(V(I_n)=\{\mathbf0\}\) for small settled \(n\) (e.g. \(n=6,8,9,10\)). *Certificate:*
the explicit multipliers \(g_{ji}\), verified by independent exact expansion; a replay confirms
\(c_j^{m_j}=\sum g_{ji}R_i\) identically.

**P2 - Certified resolution at the smallest open degree \(n=12\).** Produce a reduced Gröbner basis
of \(I_{12}\) over \(\mathbb Q\) (via modular computation + rational reconstruction) **and** the
Nullstellensatz certificates for each \(c_j\), proving \(V(I_{12})=\{\mathbf0\}\). *Certificate:* the
exact multipliers plus an independent expansion checker. This is the headline deliverable.

**P3 - Structural certificates when full membership is out of reach.** If P2's certificate is too
large, certify weaker but exact facts: (i) \(\dim_{\mathbb Q}\mathbb Q[\mathbf c]/I_{12}<\infty\)
(zero-dimensional) with a Gröbner staircase certificate; (ii) an exact upper bound on
\(|V(I_{12})|\); (iii) that the only real/rational solution is the origin. *Certificate:* the staircase
and the exact reductions, independently replayed.

**P4 - Modular evidence, honestly labeled.** Compute \(V(I_{12}\bmod p)=\{\mathbf0\}\) for a large set
of primes as a stepping stone to P2. *Certificate:* the prime list and per-prime Gröbner outputs -
explicitly marked **non-certifying over \(\mathbb Q\)**.

**P5 - Push to the next open degrees or a subfamily.** Certified resolution for \(n=15\) or \(n=20\),
or for a structured subfamily at an open degree (prescribed support / few nonzero \(c_j\)).
*Certificate:* Nullstellensatz certificates as in P2.

**P6 - Formalize the checker.** A **Lean 4** development that takes a Nullstellensatz certificate and
checks \(c_j^{m_j}=\sum g_{ji}R_i\) and \(R_i\in\mathfrak m\), turning any produced certificate into a
formal degree-\(n\) theorem. *Certificate:* the compiled Lean proof for at least one open degree.

**P7 - Exploit and certify the weighted-homogeneous structure.** Prove and use a general reduction
lemma (grading \(\deg c_j=n-j\); \(\mathbb G_m\)-action) that shrinks the computation, with an exact
certificate of correctness. *Certificate:* the lemma's proof plus a certified smaller equivalent system.

## 4. Known results and prior art

- **Casas–Alvero (c. 2001)** - the conjecture arose in his study of the singularities/polar germs of
  plane curves (verify venue and exact year).
- **Graf von Bothmer, Labs, Schicho, van de Woestijne (2007)** - "The Casas–Alvero conjecture for
  infinitely many degrees": proved for \(n=p^k\) and \(n=2p^k\) (and some further families - verify)
  by reduction to positive characteristic.
- **Draisma, de Jong (c. 2011)** - expository account of the conjecture and the reduction machinery
  (Nieuw Archief voor Wiskunde) (verify).
- **Diaz-Toca, Gonzalez-Vega; and others** - resultant/subresultant formulations and small-degree
  computational checks (verify specifics).
- **Cima, Gasull, Mañosas** - analytic/dynamical reformulations (verify).
- Small open degrees have been probed computationally; the ideal \(I_n\) has very large Gröbner
  bases, and \(n=12\) has historically been at or beyond the edge of direct exact computation (verify
  the current computational frontier).
- **Recent full-proof claims (2020s).** Several preprints have claimed a complete proof of Casas–Alvero
  in characteristic \(0\); as of this writing none is confirmed as consensus-accepted here (**verify
  urgently** - a confirmed proof would change the framing from "open degree" to "reproduce and certify
  the argument", and this problem may have moved).

**Status as of mid-2026 - re-verify against the current literature before starting any session**
(the settled-degree families, the smallest open degree, the computational frontier, and any recent
full-proof claims all require confirmation; several nearby problems fell in 2019–2024).

## 5. Attack plan

**`[sym]` build the system.** In **SageMath** / **Singular** / **Macaulay2**, form
\(f=x^n+\sum_{j\le n-2}c_jx^j\), compute the subresultant-based \(R_i=\operatorname{Res}_x(f,f^{(i)})\)
exactly, and record the weighted grading \(\deg c_j=n-j\). Sanity-check \(R_i(\mathbf0)=0\) and the
degrees.

**`[sym]` Gröbner over \(\mathbb Q\) via modular lifting.** Direct rational Gröbner bases for \(I_{12}\)
suffer coefficient explosion; use **msolve** / **Singular**'s modular Gröbner (`modStd`) - compute over
many \(\mathbb F_p\), reconstruct over \(\mathbb Q\) by CRT + rational reconstruction, then **verify**
the lifted basis is a true Gröbner basis of \(I_{12}\) over \(\mathbb Q\) (ideal membership of each
\(R_i\), Buchberger criterion on the lift). This route yields P2/P4.

**`[cert]` extract Nullstellensatz certificates.** From the Gröbner basis, obtain for each \(c_j\) the
smallest \(m_j\) with \(c_j^{m_j}\in I_{12}\) and the cofactors \(g_{ji}\) (tracked reductions /
`liftstd`). Export the multipliers; the certificate stands on its own - an **independent exact
expansion** (a second CAS, or a Lean checker, P6) confirms \(c_j^{m_j}=\sum_i g_{ji}R_i\) identically.

**`[sym]` structure exploitation.** Use the \(\mathbb G_m\)-grading and any symmetry to reduce variables
before the heavy computation (P7), and to predict the staircase.

**One-workstation scope and failure modes.** \(I_{12}\) is large; the honest risk is that the exact
rational Gröbner basis or the Nullstellensatz cofactors exceed memory. Mitigations: degree/weight-graded
term orders, modular lifting, and settling for P3/P4 with explicit statements of what remains. Modular
computation can hit **bad primes** (wrong reduction) - cross-check several primes and verify the
\(\mathbb Q\)-lift; never present modular success as a \(\mathbb Q\)-proof. Cofactor blow-up may force a
smaller open degree or a subfamily (P5) as the certified product.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** All resultants, ideal memberships, and cofactors are exact over
   \(\mathbb Q\); any modular step is explicitly a heuristic accelerator whose \(\mathbb Q\)-lift is
   verified. No floating point enters a certified claim.
2. **Independent verification.** Every Nullstellensatz certificate \(c_j^{m_j}=\sum_i g_{ji}R_i\) is
   re-expanded by a CAS independent of the one that produced it (ideally a Lean checker, P6); the
   Gröbner basis is re-validated (membership + Buchberger) by a second implementation.
3. **Reproducibility.** Term orders, prime lists, reconstruction bounds, tool versions, and all
   intermediate ideals are recorded; a **SHA-256 manifest** covers the system, the basis, and every
   certificate.
4. **Preservation.** The generation source (system construction, modular Gröbner driver, cofactor
   extraction) is part of the record; anything not preserved is stated explicitly, not obscured (the
   Hadamard-668 lost-source lesson).
5. **Honest reporting.** The report states up front, per degree attempted, whether \(V(I_n)=\{\mathbf0\}\)
   was **certified over \(\mathbb Q\)**, or only established modulo primes, or only partially (P3), and
   never presents a modular or partial result - or a re-derivation at a settled degree - as a resolution
   of the conjecture.
