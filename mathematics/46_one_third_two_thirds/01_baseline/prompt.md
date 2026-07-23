# PROMPT FOR CERTIFYING BALANCED PAIRS TOWARD THE 1/3–2/3 CONJECTURE

## The 1/3–2/3 conjecture for finite partially ordered sets

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 46 of 50
**Area:** order theory & extremal set systems
**Modes:** `[proof]` `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Every finite poset that is not a total order is conjectured to contain an incomparable pair \((x,y)\) that a uniformly random linear extension separates almost evenly: the probability that \(x\) precedes \(y\) lies in \([1/3,2/3]\).

The statement sits exactly on the boundary between finite verification and infinitary proof. For any *fixed* poset the separating probability is an exact rational computable on the machine, so whole classes can be certified by exhaustive exact-arithmetic enumeration; but the conjecture quantifies over *all* posets, so the general case is a proof problem, and the best unconditional constant known - \((5-\sqrt5)/10\approx0.2764\) - sits strictly below \(1/3\).

This makes the problem a sibling of the union-closed conjecture (#09): an order/set-system extremal statement whose small cases are machine-checkable ground truth and whose general form resists. The resolution standard in section 2 is the target; a certified verification for a new class, a certified extremal characterization, or a certified improvement of the general constant is reported as exactly that partial result, never dressed as the whole conjecture.

## 1. Exact problem statement

Let \(P=(X,\le)\) be a finite partially ordered set with ground set \(X\), \(|X|=n\ge1\). Write \(x\parallel y\) when \(x\) and \(y\) are **incomparable** (neither \(x\le y\) nor \(y\le x\)).

A **linear extension** of \(P\) is a total order \(L\) on \(X\) compatible with \(\le\):
\[
x\le y\ \Longrightarrow\ x\le_L y \qquad\text{for all }x,y\in X.
\]
Let \(\mathcal E(P)\) be the set of linear extensions and \(e(P)=|\mathcal E(P)|\ge1\) their number.

For an incomparable pair \(x\parallel y\), define the **separating probability**
\[
\Pr[x\prec y]\;=\;\frac{\bigl|\{L\in\mathcal E(P):x\le_L y\}\bigr|}{e(P)}\in(0,1),
\qquad
\Pr[y\prec x]=1-\Pr[x\prec y].
\]

Call \((x,y)\) a **\(\delta\)-balanced pair** if
\[
\min\bigl(\Pr[x\prec y],\ \Pr[y\prec x]\bigr)\ \ge\ \delta .
\]
Define the **balance constant** of \(P\),
\[
\delta(P)\;=\;\max_{x\parallel y}\ \min\bigl(\Pr[x\prec y],\ \Pr[y\prec x]\bigr),
\]
with the convention \(\delta(P)=1\) when \(P\) is a total order (there is no incomparable pair; the conjecture is vacuous there and explicitly excludes it).

**Conjecture (1/3–2/3).** For every finite poset \(P\) that is not a total order,
\[
\delta(P)\ \ge\ \tfrac13,
\]
equivalently \(P\) has a \(\tfrac13\)-balanced pair.

**Tightness.** The bound is best possible: there exist posets with \(\delta(P)=\tfrac13\) exactly. The smallest witness is the three-element poset \(a<b\) with \(c\) incomparable to both ("\(\mathbf V\) plus a point" / the \(N=3\) chain-plus-antichain family): its linear extensions place \(c\) in one of three slots, giving \(\Pr[c\prec a]\in\{\tfrac13,\tfrac23\}\) and no better pair. The exact extremal family is Target P4.

For the extremal example above, writing the linear extensions explicitly (\(c\) inserted before \(a\), between \(a\) and \(b\), or after \(b\)) gives
\[
\Pr[c\prec a]=\tfrac13,\quad \Pr[a\prec c]=\tfrac23,\quad \Pr[c\prec b]=\tfrac23,\quad \Pr[b\prec c]=\tfrac13,
\]
so \(\delta(P)=\tfrac13\), realized simultaneously by both incomparable pairs.

**Two standard reformulations.**
\[
\text{(sorting)}\quad \delta(P)\ \text{lower-bounds the information gained by the best comparison in a sorting-under-partial-information tree;}
\]
\[
\text{(entropy)}\quad \text{if }h(P)=\log_2 e(P),\ \text{a }\delta\text{-balanced comparison drops }h\text{ by at least }H_2(\delta),\ H_2\ \text{binary entropy.}
\]

No informal reading ("nearly balanced", "some fairly even pair") is an acceptable target. The objects of study are the exact rational \(\Pr[x\prec y]\), the exact constant \(\delta(P)\), and the largest \(\delta^\*\) with \(\delta(P)\ge\delta^\*\) for all non-total finite \(P\) (the conjecture asserts \(\delta^\*=\tfrac13\); the record is \(\delta^\*\ge(5-\sqrt5)/10\)).

## 2. Resolution standard

A complete resolution is a proof of one of:

- **(Affirmative)** every finite non-total poset has a \(\tfrac13\)-balanced pair; or
- **(Negative)** an explicit finite poset \(P_0\) with \(\delta(P_0)<\tfrac13\), certified by exact computation of \(e(P_0)\) and of \(\Pr[x\prec y]\) for every incomparable pair.

**Certified form.** The affirmative case is an infinitary statement and cannot be settled by search; the accepted certificate is a **formal proof in Lean 4 + mathlib** (a "certified balanced-pair theorem"), or a complete human proof whose only finite lemmas are discharged by exact rational computation with independent replay. The negative case is a finite object: an exact-arithmetic **balance certificate** exhibiting \(\delta(P_0)<1/3\), listing \(e(P_0)\) and all pair probabilities as exact fractions, independently recomputable.

**Not accepted as resolution.**

- Any floating-point estimate of \(\Pr[x\prec y]\); certification requires exact integers/rationals.
- Verifying the conjecture for a single poset, or for finitely many, and calling the conjecture "confirmed".
- Re-proving a class already in the literature (width 2, semiorders, height 2, forests, \(N\)-free) and representing it as new or as the general theorem.
- A general lower bound \(\delta^\*\ge c\) with \(c\le(5-\sqrt5)/10\) (no improvement) presented as progress on the constant.
- A heuristic "checked millions of posets, no counterexample" narrative in place of an exhaustive isomorph-free enumeration with a completeness argument.

## 3. Graded partial-result targets

Each target names its certificate and how it is independently checked.

- **P1 - reproduce the exhaustive frontier.**
  Generate all posets on \(n\le11\) elements up to isomorphism, compute \(e(P)\) and every \(\Pr[x\prec y]\) in exact integer arithmetic, and confirm \(\delta(P)\ge1/3\) for every non-chain.
  *Certificate:* a replayable enumeration log with, per poset, a canonical code and one witnessed \(\tfrac13\)-balanced pair \((x,y,\,a/b)\), \(a/b\in[1/3,2/3]\); the independent checker recomputes \(e(P)\) by a second method (order-ideal DP vs. direct extension count) and re-verifies the fraction. Reproduces Peczarski's computational verification.

- **P2 - extend the certified frontier.**
  Push exhaustive verification to \(n=12\) (and \(n=13\) if resources allow), reporting the exact worst case \(\min_P\delta(P)\) as a function of \(n\) and the posets attaining it.
  *Certificate:* the P1 schema plus a completeness statement for the generator at that \(n\) (representative count matches the known number of unlabeled posets).

- **P3 - certify a structural class mechanically.**
  Produce a machine-checkable proof for a class not previously formalized: either an exact-enumeration certificate for a bounded-width family (width \(\le3,4\)) or bounded-height family up to a proven reduction bound, or a **Lean formalization** of an existing paper proof (width 2 or semiorders).
  *Certificate:* the Lean proof term, or the enumeration plus the reduction lemma that makes finitely many cases exhaustive.

- **P4 - certified extremal characterization.**
  Exactly enumerate, up to isomorphism, all posets on \(\le n\) elements attaining \(\delta(P)=\tfrac13\) (rational equality, not proximity), and identify the extremal family.
  *Certificate:* exact list with certified equalities \(\Pr[x\prec y]=1/3\) and a proof that no other incomparable pair does better.

- **P5 - certified constant on an infinite restricted class.**
  Prove \(\delta(P)\ge c\) with \(c>(5-\sqrt5)/10\) for an infinite class (e.g. width \(\le3\)), formalized or reduced to certified finite base cases (exact LP/SDP duality with rational rounding).
  *Certificate:* the written induction plus exact certificates for its finite lemmas.

- **P6 - improve the general constant (strongest short of full).**
  A new unconditional bound \(\delta^\*\ge c\) with \(c>(5-\sqrt5)/10\), beating Brightwell–Felsner–Trotter, with the correlation/entropy argument formalized and every finite computational lemma certified by exact arithmetic.
  *Certificate:* the full proof; a Lean skeleton for the analytic core is strongly preferred.

## 4. Known results and prior art

- **Origin.** Conjectured by Kislitsyn (1968); independently by Fredman (mid-1970s, verify) and by Linial (1984), who framed it via comparison-sorting lower bounds.
- **General constant.** Kahn–Saks (1984) proved every non-total poset has a pair with \(\Pr\in[3/11,8/11]\), \(3/11\approx0.2727\), via an entropy / log-concavity argument. Brightwell, Felsner and Trotter (1995) improved the guaranteed window to
\[
\Bigl[\tfrac{5-\sqrt5}{10},\ \tfrac{5+\sqrt5}{10}\Bigr]\approx[0.2764,\ 0.7236],
\]
the current record general constant \(\delta^\*\ge(5-\sqrt5)/10\) (verify no later improvement). The gap to the conjectured \([1/3,2/3]\) is what P5–P6 attack.
- **Classes proved.** Width 2 (Linial 1984); semiorders (Brightwell 1989); height-2 posets; \(N\)-free ordered sets (approx. 2011, verify authors); posets whose cover graph is a forest (approx. 2016, verify); "5-thin" posets; series-parallel / lexicographic-sum constructions.
- **Computational.** Peczarski's **gold partition conjecture** (approx. 2006–2008) implies 1/3–2/3 and was computationally verified, giving the conjecture for all posets on \(\le11\) elements (verify the exact size reached).
- **Surveys.** Brightwell's balanced-pairs survey; a 2025 expository chapter "On Partially Ordered Sets and the 1/3–2/3 Conjecture" (verify venue). No fabricated arXiv IDs, DOIs, or page numbers are to be introduced.
- **Sibling.** The union-closed conjecture (#09) - same "small cases finite, general case resistant" order/set-system profile.

**Status as of mid-2026 - re-verify against the current literature before starting any session.** Bounds and class results drift; confirm the record general constant, the largest \(n\) reached by exhaustive verification, and the current list of settled classes before claiming any as the frontier.

## 5. Attack plan

- **`[search]` exact enumeration.** Generate unlabeled posets isomorph-free (SageMath `Posets`, or orderly generation over transitively closed DAGs with `nauty`/`Traces` canonical forms). Count \(e(P)\) and each \(\Pr[x\prec y]\) by dynamic programming over the lattice of order ideals (down-set DP): with \(N(I)\) the number of linear extensions of the sub-poset on ideal \(I\),
\[
N(I)=\sum_{\,m\ \text{maximal in }I} N(I\setminus\{m\}),\qquad e(P)=N(X),
\]
and the same recurrence, restricted to ideals containing/avoiding \(x\) before \(y\), yields \(\Pr[x\prec y]\). All in GMP integers; derive \(\Pr\) as an exact fraction, cross-checked against a second counter.
- **`[proof]` formalization and bounds.** Lean 4 + mathlib for width-2 / semiorder proofs and the extremal characterization; mathlib's poset and finite-probability machinery is partial, and the entropy / FKG / XYZ-type inequalities behind the general constant are a substantial formalization effort (failure mode). For P5/P6, exact rational LP/SDP duality (Sage exact LP; SDP via SDPA-GMP then rational rounding checked by CAS).
- **One-workstation scope.** Unlabeled posets number \(\approx4.67\times10^{7}\) at \(n=11\) and \(\approx1.10\times10^{9}\) at \(n=12\): \(n=11\) is comfortable, \(n=12\) is a multi-day exact-arithmetic run needing a compact canonical form and streaming, and \(n=13\) (\(\approx3\times10^{10}\)) is out of reach by brute force. Bounded-width classes extend further because ideal-DP is cheap for small width.
- **Failure modes.** Linear-extension counting blows up for wide posets (\(\#P\)-hard in general, tractable here only for small width/size); the count of unlabeled posets explodes past \(n=12\); mathlib gaps force long formalization detours for the analytic bounds.

## 6. Verification and auditability requirements

1. **Exact/certified computation.** All \(e(P)\) and \(\Pr[x\prec y]\) values are exact integers/rationals (GMP); floating point is exploration only. Any general-constant bound rests on exact LP/SDP duals or a formal proof, never a numerical optimum.
2. **Independent verification.** A standalone checker, written separately from the search, recomputes \(e(P)\) by a second algorithm and re-verifies each witnessed fraction lies in \([1/3,2/3]\); Lean proof terms are kernel-checked; SOS/LP certificates are re-verified by a second CAS.
3. **Reproducibility.** Generator, seeds, canonical-form choice, DP code, and environment recorded; a SHA-256 manifest covers every enumeration log, certificate, and proof file.
4. **Preservation.** All enumeration and counting source is part of the record (the Hadamard-668 lost-source lesson). Anything pruned or unfinished (e.g. an aborted \(n=13\) pass) is stated, not obscured.
5. **Honest reporting.** The report states up front whether the resolution standard was met. A certified class, an extremal characterization, or a restricted-class constant is a partial result; only a general proof (or a certified counterexample) may be called a resolution, and the general constant is never claimed improved unless it strictly exceeds \((5-\sqrt5)/10\) with a checkable certificate.

### Honest calibration

The general conjecture is proof-hard and has resisted since 1968; a session will almost certainly not settle it. The realistic product is P1–P4: a clean, independently replayable exhaustive frontier and a certified extremal characterization. P5 (a better constant on an infinite restricted class) is a genuine stretch; P6 (beating Brightwell–Felsner–Trotter in general) would be a real research advance and should be attempted only after the finite infrastructure is solid.
