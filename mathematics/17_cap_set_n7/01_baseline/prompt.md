# PROMPT FOR DETERMINING \(a(7)\), THE MAXIMUM CAP IN \(\mathrm{AG}(7,3)\)

## The largest line-free set in the seven-dimensional affine space over \(\mathbb{F}_3\)

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 17 of 50  
**Area:** additive & combinatorial number theory  
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

A *cap* in the affine geometry \(\mathrm{AG}(n,3)=(\mathbb{Z}/3\mathbb{Z})^n\) is a set of points containing no affine line - equivalently no three distinct points summing to \(0\). The maximum cap size \(a(n)\) is known exactly only through \(n=6\):

\[
a(1),\dots,a(6)=2,\ 4,\ 9,\ 20,\ 45,\ 112,
\]

and the value \(a(7)\) is open, with a current certified window of roughly \(236\le a(7)\le 291\). This is a finite, exactly-defined extremal integer with machine-checkable ground truth on both sides: an explicit cap certifies a lower bound, and an infeasibility proof - exhaustive isomorph-free search, integer-program duality, or SAT UNSAT - certifies an upper bound. That two-sided checkability makes it an ideal target for certified search on one workstation.

**Critical scope note.** This prompt targets the *exact finite value* \(a(7)\). It is emphatically **not** the cap-set *growth-rate* problem. The Croot–Lev–Pach and Ellenberg–Gijswijt polynomial-method breakthrough (2016) bounds the asymptotic exponent - the largest \(c\) with \(a(n)\gtrsim c^{\,n}\), and the matching upper bound \(a(n)=o(2.756^{\,n})\) - and says nothing sharp about the single integer \(a(7)\). The resolution standard in section 2 is the target. Any lower bound without a matching upper bound, and any growth-rate statement, is reported as a partial result and never represented as determining \(a(7)\).

## 1. Exact problem statement

Fix the ground ring \(\mathbb{F}_3=\mathbb{Z}/3\mathbb{Z}\) and the affine space \(V=\mathbb{F}_3^{\,n}\), whose points are the \(3^n\) vectors over \(\mathbb{F}_3\). An **affine line** is a coset of a one-dimensional subspace,

\[
\ell_{a,d}=\{a,\ a+d,\ a+2d\},\qquad a\in V,\ d\in V\setminus\{0\},
\]

a three-point set because \(\operatorname{char}\mathbb{F}_3=3\). Since

\[
a+(a+d)+(a+2d)=3a+3d=0,
\]

three **distinct** points \(x,y,z\in V\) are collinear if and only if \(x+y+z=0\).

A **cap** is a set \(C\subseteq V\) with no three distinct collinear points:

\[
\forall\,x,y,z\in C\ \text{distinct}:\quad x+y+z\neq 0 .
\]

Equivalently:
- \(C\) contains no nontrivial 3-term arithmetic progression (\(x+z=2y=-y\) forces \(x=z\) inside \(C\));
- every affine line meets \(C\) in at most two points;
- the equation \(x+y+z=0\) with \(x,y,z\in C\) forces two of them equal.

Define the extremal function

\[
a(n)=\max\{|C|:C\subseteq\mathbb{F}_3^{\,n}\ \text{is a cap}\}.
\]

The number of affine lines in \(\mathrm{AG}(n,3)\) is

\[
\frac{3^n(3^n-1)}{6}=3^{\,n-1}\cdot\frac{3^n-1}{2},
\qquad\text{for } n=7:\quad 729\cdot 1093 = 796{,}797 .
\]

The natural symmetry group is the affine general linear group

\[
\mathrm{AGL}(n,3)=V\rtimes \mathrm{GL}(n,3),
\]

which acts on caps and preserves \(|C|\); hence \(a(n)\) is an \(\mathrm{AGL}(n,3)\)-invariant, and the search may work up to affine equivalence.

**The open determination.** Compute the exact integer \(a(7)\), with both a matching cap and a matching impossibility proof. Nothing informal (e.g. "a large cap", "close to the upper bound") is an acceptable target.

## 2. Resolution standard

A complete resolution is the exact integer \(a(7)=m\), delivered as a **matched cap certificate**, namely both of the following.

1. **Lower witness.** An explicit cap \(C^\star\subseteq\mathbb{F}_3^7\) with \(|C^\star|=m\), given as machine-readable coordinates, together with a line-free proof that either
   - checks all \(\binom{m}{3}\) triples for \(x+y+z=0\), or
   - (equivalent, faster) confirms the multiset of pairwise sums \(\{x+y:x,y\in C^\star\}\) exhibits no collision that would witness a third cap point.

2. **Upper witness.** A proof that no cap of size \(m+1\) exists in \(\mathbb{F}_3^7\), in one certified form:
   - an exhaustive **isomorph-free enumeration** (orderly generation / canonical augmentation under \(\mathrm{AGL}(7,3)\)), whose completeness is argued and replayable; or
   - an **integer-program infeasibility certificate** - a rational **Farkas / dual** certificate for the LP relaxation, strengthened to integer infeasibility and checkable in exact arithmetic; or
   - a **SAT UNSAT proof** (DRAT/LRAT) for the encoding "there is a cap of size \(m+1\)".

**Not accepted as resolution.**
- Any statement about the *growth rate* / capacity exponent (Ellenberg–Gijswijt, Croot–Lev–Pach, or improved asymptotic lower bounds) presented as the value \(a(7)\).
- A large explicit cap without a matching, certified upper bound (a lower bound only).
- An LP or SDP relaxation reported as \(a(7)\le U\) without an exact rational dual certificate and an integrality argument.
- A value emitted by an ILP or SAT solver with no independently checkable UNSAT / infeasibility trace.
- Any floating-point, probabilistic, or heuristic argument on either side.

## 3. Graded partial-result targets

Ordered \(P_1\) (reproduce the frontier) \(\to P_6\) (strongest short of resolution); each names its certificate.

- **\(P_1\) - reproduce \(a(6)=112\).** Construct a \(112\)-cap in \(\mathbb{F}_3^6\) and certify optimality (no \(113\)-cap) with our own toolchain.
  - *Certificate:* explicit cap + replayable isomorph-free enumeration or SAT UNSAT at size \(113\), independently rechecked. Validates the pipeline against Potechin's result.

- **\(P_2\) - reproduce the lower frontier for \(n=7\).** Rebuild and verify an explicit cap of size \(\ge 236\) in \(\mathbb{F}_3^7\) (Calderbank–Fishburn class).
  - *Certificate:* coordinates + exhaustive line-free check; generator source preserved.

- **\(P_3\) - improve the lower bound.** A certified cap of size \(> 236\) (the current best exact-dimension construction), with the construction method preserved and reproducible.
  - *Certificate:* coordinates + line-free check + generator source.

- **\(P_4\) - nontrivial certified upper bound.** Prove \(a(7)\le U\) for the smallest \(U\) achievable (targeting \(U<291\)), via an LP/Delsarte-type or ILP relaxation with an **exact rational dual certificate**, or a completed partial exhaustive search eliminating a hyperplane-distribution case.
  - *Certificate:* rational Farkas vector or completed case-log, rechecked in exact arithmetic.

- **\(P_5\) - shrink the window from both sides.** A two-sided certified interval strictly inside the currently accepted \([236,291]\), combining an improved cap and an improved impossibility proof.
  - *Certificate:* the union of a \(P_3\) and a \(P_4\) artifact.

- **\(P_6\) - determine \(a(7)\).** The full resolution of section 2 (a windfall). Short of it, the tightest verified two-sided window plus a documented obstruction analysis explaining what blocks closure.

## 4. Known results and prior art

- Exact values \(a(1..6)=2,4,9,20,45,112\). The step \(a(4)=20\) is Pellegrino (1971); \(a(6)=112\) is Potechin (2008), by exhaustive computation, confirming/correcting earlier work.
- Lower bound for \(n=7\): Calderbank–Fishburn (1994) constructed a \(7\)-cap of size \(236\) by an extended product / design construction; this remains the best certified exact-dimension lower bound (verify against newer product constructions).
- Upper bound for \(n=7\): computational optimization work of the ~2021–2022 era - including *The cap set problem: up to dimension 7* (2022) and *Improved explicit upper bounds for the cap set problem* (2021) - places \(a(7)\le 291\) (verify), with intermediate facts such as the nonexistence of certain \(289\)-caps in \(7\)-flats.
- **Asymptotics (a distinct problem - do not conflate):** Croot–Lev–Pach (2016) and Ellenberg–Gijswijt (2016) gave the polynomial-method bound \(a(n)=O(2.756^{\,n})\); Tyrrell (2022, *New Lower Bounds for Cap Sets*) improved the asymptotic capacity lower bound. These bound the exponent, not \(a(7)\).
- Bierbrauer–Edel and Edel product constructions; Hill's coding-theory correspondence (caps \(\leftrightarrow\) certain codes / ovoids). OEIS **A090245** lists \(a(n)\).

**Status as of mid-2026 - re-verify against the current literature before starting any session.** The exact-\(n=7\) window is under active revision; confirm the current best lower and upper bounds and their certificates.

## 5. Attack plan

`[search]` on a single workstation.

**SAT encoding.** One Boolean variable \(x_p\) per point \(p\in\mathbb{F}_3^7\), so \(3^7=2187\) variables. For each of the \(796{,}797\) lines \(\{p,q,r\}\), a clause

\[
(\lnot x_p\lor\lnot x_q\lor\lnot x_r)
\]

forbidding a full line. Impose the cardinality bound \(\sum_p x_p\ge k\) with a sequential-counter or totalizer encoding. Feed to CaDiCaL / kissat / CryptoMiniSat; **emit DRAT** for the UNSAT instance at \(k=m+1\). Symmetry breaking under \(\mathrm{AGL}(7,3)\) is essential but the group is enormous - use a lex-leader constraint on a fixed coordinate order, and/or seed a known optimal cap of a hyperplane as fixed points.

**Integer program.** Maximize \(\sum_p x_p\) subject to \(x_p+x_q+x_r\le 2\) per line, \(x\in\{0,1\}\). The LP relaxation plus valid inequalities yields upper bounds; for any claimed \(a(7)\le U\), extract and check an **exact rational dual** (Farkas) certificate. A Delsarte / Fourier linear-programming bound over the character group \(\widehat{\mathbb{F}_3^7}\) is a second, independent upper-bound route to be made rigorous in exact arithmetic.

**Exhaustive enumeration.** Orderly generation / canonical augmentation of caps under \(\mathrm{AGL}(7,3)\), pruned by the induced hyperplane cap-size distribution: a cap meets the affine hyperplanes in sizes constrained by counting identities, and case-splitting on that distribution partitions the search. Use `nauty`/`Traces` for canonical forms of derived structures.

**Scope and failure modes.** Building and certifying large lower-bound caps is clearly feasible; \(P_1\) (the \(n=6\), size-\(113\) UNSAT) is a realistic reproduction. The full upper bound for \(n=7\) is exactly why the value is open: the SAT UNSAT and full exhaustive search are expected to be **intractable** without a genuine new symmetry reduction or LP/SDP idea - state this plainly and target \(P_4\) (a single improved certified bound) rather than promising closure. Expected failure modes:
- symmetry group too large for effective lex-leader breaking;
- cardinality-constrained UNSAT beyond solver reach at high \(k\);
- LP / Delsarte bound too weak to beat \(291\).

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Line-free checks and the cap/line combinatorics run in exact integer / \(\mathbb{F}_3\) arithmetic. Upper bounds are backed by DRAT/LRAT (SAT), exact rational Farkas duals (LP/ILP), or replayable isomorph-free completeness (enumeration). Floating point is exploration only, never certification.
2. **Independent verification.** For every certificate, a small standalone checker written separately from the search: a triple-scanning line-free verifier for caps; a DRAT/LRAT checker for UNSAT; a rational dual-feasibility checker for LP bounds; an enumeration replay for exhaustive claims. Dual implementations of the line-free test (triple scan vs. sumset/collision test) where warranted.
3. **Reproducibility.** All encodings, variable orderings, symmetry-breaking predicates, seeds, solver versions, and flags are recorded; a SHA-256 manifest spans every cap file, CNF, proof trace, and log.
4. **Preservation.** All construction and search source (cap generators, CNF emitters, enumeration code) is part of the record; anything not preserved is stated explicitly (the Hadamard-668 lost-source lesson).
5. **Honest reporting.** The report states up front whether \(a(7)\) was determined. A lower-bound cap, an upper-bound certificate, or a shrunk window is reported as exactly that - never as the value \(a(7)\), and never conflated with the cap-set growth-rate results.
