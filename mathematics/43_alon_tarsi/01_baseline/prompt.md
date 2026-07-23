# PROMPT FOR CERTIFYING THE ALON–TARSI SIGNED COUNT AT AN OPEN EVEN ORDER

## The Alon–Tarsi conjecture: even and odd Latin squares of even order are unequal in number

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 43 of 50  
**Area:** number theory & algebra  
**Modes:** `[sym]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The Alon–Tarsi conjecture states that for every even \(n\) the number of even Latin squares of
order \(n\) differs from the number of odd ones - equivalently the signed count
\(\mathrm{AT}(n)=\mathrm{els}(n)-\mathrm{ols}(n)\) is nonzero. It implies list-edge-coloring results
and, via Huang–Rota/Onn, cases of Rota's basis conjecture (#44) over the reals. It is proved for
\(n=p\pm1\) with \(p\) an odd prime (Drisko for \(p+1\); Glynn for \(p-1\)) by evaluating a structured
permanent modulo \(p\); the smallest even order not of that form is \(n=26\) (**verify**). This is a
`[sym]` problem: \(\mathrm{AT}(n)\) has an exact algebraic expression (a coefficient extraction /
permanent), and - decisively - to prove \(\mathrm{AT}(n)\neq0\) it suffices to certify
\(\mathrm{AT}(n)\not\equiv0\pmod p\) for a single prime \(p\), a computation reachable by Ryser's
formula in exact \(\mathbb F_p\) arithmetic for orders well beyond direct Latin-square enumeration.
The resolution standard in section 2 is the target for a specified open even order; a floating-point
estimate, an uncertified formula, or a single order presented as the conjecture is reported as a
partial result and never as a solution.

## 1. Exact problem statement

A **Latin square** of order \(n\) is an \(n\times n\) array \(L=(L_{r,c})\) with entries in
\(\{1,\dots,n\}\) such that every row and every column is a permutation of \(\{1,\dots,n\}\). For row
\(r\), let \(R_r\in S_n\) be the permutation \(c\mapsto L_{r,c}\); for column \(c\), let \(C_c\in S_n\)
be \(r\mapsto L_{r,c}\). The **sign** of \(L\) is
\[
\varepsilon(L)=\prod_{r=1}^{n}\operatorname{sgn}(R_r)\ \prod_{c=1}^{n}\operatorname{sgn}(C_c)\in\{\pm1\}.
\]
\(L\) is **even** if \(\varepsilon(L)=+1\) and **odd** if \(\varepsilon(L)=-1\). Let \(\mathrm{els}(n)\)
and \(\mathrm{ols}(n)\) count even and odd Latin squares, and define the **Alon–Tarsi constant**
\[
\mathrm{AT}(n)=\mathrm{els}(n)-\mathrm{ols}(n).
\]
For odd \(n\) a sign-reversing involution gives \(\mathrm{AT}(n)=0\), so the content is even \(n\).

**Alon–Tarsi conjecture.** For every even \(n\), \(\mathrm{AT}(n)\neq0\).

**Algebraic form (to be re-derived and certified).** \(\mathrm{AT}(n)\), up to an explicit nonzero
normalization, equals a coefficient-extraction / permanent expression amenable to exact evaluation;
Drisko and Glynn realize a nonzero multiple of \(\mathrm{AT}(p\pm1)\) as a **permanent of a specific
matrix modulo \(p\)**. The precise identity used in a session must be taken from Glynn (2010) / Drisko
(1997) and **re-derived and certified** (see section 2), not assumed.

An even order \(n\) is **open** here when it is not of the form \(p\pm1\) for a prime \(p\) and is
beyond direct enumeration; the smallest such is \(n=26\), then \(34,36,\dots\) (**verify** the list).

## 2. Resolution standard

A **complete resolution** is a proof that \(\mathrm{AT}(n)\neq0\) for all even \(n\), formalized to the
standard below. A **certified result for a specified open even order \(n\)** is an exact proof that
\(\mathrm{AT}(n)\neq0\) for that \(n\) - a genuine new theorem.

**Certified form.** (i) An **exact algebraic identity** \(\mathrm{AT}(n)=\kappa\cdot F(n)\) with \(\kappa\)
an explicit nonzero rational constant and \(F(n)\) a permanent/coefficient computable in exact
arithmetic, the identity itself proved (not assumed). (ii) An **exact evaluation** of \(F(n)\) over
\(\mathbb Z\), or of \(F(n)\bmod p\) over \(\mathbb F_p\) via **Ryser's formula** in exact modular
arithmetic, exhibiting a prime \(p\) with \(F(n)\not\equiv0\pmod p\) - which certifies
\(\mathrm{AT}(n)\neq0\). (iii) Independent recomputation of the value by a second method (a different
formula, or a different prime, or direct enumeration where feasible). (iv) Reduction lemmas and the
sign-count identity are candidates for **Lean 4 + mathlib** formalization, turning a computed nonzero
residue into a formal nonvanishing theorem.

**Not accepted as resolution.**
- A floating-point or Monte-Carlo estimate of \(\mathrm{els}(n)-\mathrm{ols}(n)\).
- A permanent computed modulo \(p\) via an identity that is *assumed* rather than proved to equal
  \(\mathrm{AT}(n)\bmod p\) (you must certify what you computed is \(\mathrm{AT}(n)\)).
- \(|\mathrm{AT}(n)|\) estimated or bounded but not shown \(\neq0\).
- A result for one open order presented as the full conjecture.
- Nonvanishing "mod \(p\)" reported without an exact \(\mathbb F_p\) arithmetic trace.
- Reproduction of \(n=p\pm1\) presented as progress on an open order.

## 3. Graded partial-result targets

**P1 - Reproduce known values, two ways.** Compute \(\mathrm{AT}(n)\) exactly for all even \(n\) with
known values (small \(n\)) by two independent routes - direct signed enumeration and the
coefficient/permanent identity - and match OEIS. *Certificate:* both exact computations agree; the
identity's normalization \(\kappa\) is pinned down and checked.

**P2 - Certify Drisko/Glynn nonvanishing.** For chosen primes \(p\), evaluate the Drisko/Glynn
permanent modulo \(p\) in exact \(\mathbb F_p\) arithmetic and certify \(\mathrm{AT}(p\pm1)\not\equiv0\).
*Certificate:* the exact permanent value in \(\mathbb F_p\) (Ryser), plus a re-derivation of the
identity that ties it to \(\mathrm{AT}\).

**P3 - Certified nonvanishing at an open even order.** For \(n=26\) (then the next open orders),
compute \(\mathrm{AT}(n)\bmod p\) by exact Ryser evaluation over \(\mathbb F_p\) and exhibit a prime
\(p\) with \(\mathrm{AT}(n)\not\equiv0\), certifying \(\mathrm{AT}(n)\neq0\). *Certificate:* the exact
modular trace, the certified identity (P1), and independent recomputation with a second prime. This is
the headline deliverable.

**P4 - Exact integer value at an open order.** Where feasible, evaluate \(\mathrm{AT}(n)\in\mathbb Z\)
exactly (CRT over several primes with a proven size bound). *Certificate:* the per-prime residues, the
size bound, and the reconstruction.

**P5 - Congruence structure and mining.** Tabulate \(\mathrm{AT}(n)\bmod p\) across even \(n\) and small
\(p\); study the \(2\)-adic valuation and residue patterns; form a precise conjecture. *Certificate:*
exact residue tables with an honest multiple-testing account.

**P6 - Formalize the identity.** Lean 4 proof of the exact sign-count/permanent identity
\(\mathrm{AT}(n)=\kappa F(n)\), so any certified \(F(n)\not\equiv0\pmod p\) becomes a formal theorem.
*Certificate:* the compiled development.

**P7 - A new infinite family.** If the algebra permits, prove \(\mathrm{AT}(n)\neq0\) for a family beyond
\(p\pm1\) (e.g. a product or \(2(p\pm1)\) shape) via a certified modular argument. *Certificate:* the
proof plus a certified check at the smallest new member.

## 4. Known results and prior art

- **Alon, Tarsi (1992)** - "Colorings and orientations of graphs": the conjecture and its list-edge-coloring
  consequences (list chromatic index of \(d\)-regular bipartite graphs).
- **Huang, Rota (1994)** - link to Rota's basis conjecture via the supersymmetric bracket algebra;
  \(\mathrm{AT}(n)\neq0\) (even \(n\)) implies Rota's conjecture for order \(n\) over characteristic-\(0\)
  fields (verify exact statement).
- **Onn (1997)** - a "colorful" algebraic reformulation.
- **Drisko (1997)** - "On the number of even and odd Latin squares of order \(p+1\)": \(\mathrm{AT}(p+1)\neq0\).
- **Glynn (2010)** - "The conjectures of Alon–Tarsi and Rota in dimension prime minus one":
  \(\mathrm{AT}(p-1)\neq0\), via a permanent modulo \(p\) and Wilson-type number theory.
- **Zappa (1997)** - the Alon–Tarsi constant and permanents (verify).
- **Stones, Wanless; Kotlar** - sign structure and enumeration of Latin squares (verify).
- **OEIS** - the sequence \(\mathrm{els}(n)-\mathrm{ols}(n)\) with known small values (verify current extent).
- Direct even/odd enumeration is feasible only for small \(n\); the smallest even order neither \(p\pm1\)
  nor directly enumerable is \(n=26\) (verify).

**Status as of mid-2026 - re-verify against the current literature before starting any session**
(the proved families \(p\pm1\), the smallest open even order, and the range of known exact values all
require confirmation; several nearby problems fell in 2019–2024).

## 5. Attack plan

**`[sym]` pin the identity.** In **SageMath** / **SymPy**, re-derive the exact identity
\(\mathrm{AT}(n)=\kappa F(n)\) from Glynn/Drisko, verifying the normalization \(\kappa\) against
directly enumerated small-\(n\) values (P1). Treat the identity as a claim to be proved, not imported.

**`[sym]` exact evaluation.** Implement **Ryser's formula** for the relevant permanent in exact
arithmetic - over \(\mathbb Z\) for small \(n\), over \(\mathbb F_p\) for open \(n\). Ryser is
\(O(2^{n}\,\mathrm{poly}(n))\); for \(n\) in the twenties/thirties this is a few times \(10^{7}\)–\(10^{10}\)
term-updates, feasible on one workstation with bit-parallel Gray-code enumeration and word-sized
\(\mathbb F_p\) accumulation. To certify \(\mathrm{AT}(n)\neq0\) it suffices to find one \(p\) with the
residue nonzero (P3).

**`[sym]` mining and CRT.** For P4, evaluate modulo several primes and reconstruct \(\mathrm{AT}(n)\) via
CRT under a proven magnitude bound. For P5, tabulate residues and study valuations with honest
multiple-testing discipline (many candidate congruence patterns → spurious ones expected).

**`[cert]` formalization.** In **Lean 4 + mathlib**, formalize the sign-count/permanent identity (P6),
so a certified modular nonvanishing yields a formal theorem.

**One-workstation scope and failure modes.** The dominant risk is picking the **wrong identity or
normalization** - an off-by-sign or wrong \(\kappa\) makes a correct permanent meaningless; guard with
the two-route agreement at small \(n\). Ryser cost is \(2^{n}\): orders past the high-30s exhaust the
budget, so report the exact \(n\) reached. A residue that happens to be \(0\bmod p\) is not a
disproof - try more primes; only a nonzero residue certifies nonvanishing, and only \(\mathrm{AT}(n)=0\)
proved over \(\mathbb Z\) would be a counterexample.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** All signs, permanents, and residues are computed in exact
   integer or \(\mathbb F_p\) arithmetic; the identity \(\mathrm{AT}(n)=\kappa F(n)\) is proved and its
   \(\kappa\) checked at small \(n\). Floating point is exploration only.
2. **Independent verification.** Each nonvanishing is recomputed by a second method - a different prime,
   a different permanent identity, or direct enumeration where feasible - with a standalone Ryser
   checker written independently of the search; the identity is re-derived in a second CAS or in Lean.
3. **Reproducibility.** The chosen identity and normalization, prime(s), Gray-code order, and tool
   versions are recorded; a **SHA-256 manifest** covers the code and every residue/value.
4. **Preservation.** The identity derivation, the Ryser evaluator, and mining scripts are part of the
   record; anything not preserved is stated explicitly, not obscured (the Hadamard-668 lost-source
   lesson).
5. **Honest reporting.** The report states up front whether \(\mathrm{AT}(n)\neq0\) was certified for a
   genuinely open even order and gives the exact \(n\) and prime; it never presents a floating-point
   estimate, an uncertified identity, or a \(p\pm1\) reproduction as a resolution of the conjecture.
