# PROMPT FOR EXTREMAL SIDON SETS AND PERFECT DIFFERENCE FAMILIES

## \(F(N)=\max|\text{Sidon set}\subseteq\{1,\dots,N\}|\) and Singer difference sets

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 20 of 50  
**Area:** additive & combinatorial number theory  
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

A Sidon set (\(B_2\) set) is a set of integers whose pairwise sums are all distinct - equivalently, whose pairwise differences are all distinct. The extremal function \(F(N)\), the largest Sidon set inside \(\{1,\dots,N\}\), satisfies

\[
F(N)=\sqrt{N}+O(N^{1/4})
\]

by Erdős–Turán, with the exact second-order behaviour - whether \(F(N)-\sqrt N\) is bounded - a famous open problem carrying an Erdős prize. Exact values \(F(N)\) are computable by exhaustive search with a matching optimality certificate. The closely related **perfect (planar) difference sets** - Singer's cyclic construction from projective planes - give a certified-existence question with a direct link to problem 04 (projective plane of order 12).

Both sides are machine-checkable: an explicit Sidon set verifies a lower bound, and a SAT / ILP / backtracking infeasibility proof verifies a matching upper bound. The exact-\(F(N)\) determinations and the difference-set existence questions have crisp resolution standards (section 2); the asymptotic error-term conjecture does not, and its graded targets - certified structure over computed ranges - are the realistic product. Anything short of the stated standard is reported as partial, never as resolving the error term.

## 1. Exact problem statement

**Sidon sets.** A set \(A=\{a_1<\dots<a_s\}\subseteq\mathbb{Z}\) is a **Sidon set** if the sums \(a_i+a_j\) (\(i\le j\)) are pairwise distinct; equivalently the differences \(a_i-a_j\) (\(i\ne j\)) are pairwise distinct and nonzero. Define

\[
F(N)=\max\{|A|:\ A\subseteq\{1,2,\dots,N\}\ \text{is a Sidon set}\}.
\]

The Erdős–Turán inequality gives (Lindström's form)

\[
F(N)\ \le\ \sqrt N+N^{1/4}+1,
\]

and Singer / Bose constructions give \(F(N)\ge \sqrt N\,(1-o(1))\); thus \(F(N)=\sqrt N+O(N^{1/4})\). The **error term**

\[
E(N)=F(N)-\sqrt N
\]

and its true order are open.

**Perfect difference sets.** A **planar (perfect) difference set** of order \(q\) is a set \(D=\{d_0,\dots,d_q\}\subseteq\mathbb{Z}/v\mathbb{Z}\), with \(v=q^2+q+1\), such that every nonzero residue of \(\mathbb{Z}/v\mathbb{Z}\) is represented **exactly once** as a difference \(d_i-d_j\). Such a \(D\) is a cyclic \((v,q+1,1)\)-difference set, equivalent to a projective plane of order \(q\) admitting a **Singer** (regular cyclic) automorphism. The counting is forced: the \(k=q+1\) elements give

\[
k(k-1)=(q+1)q=v-1
\]

ordered differences, exactly enough to cover each nonzero residue once. More generally a **perfect difference family** partitions the nonzero residues into difference sets of prescribed block sizes.

**\(B_h\) generalization.** A set \(A\) is a **\(B_h\) set** if all sums of \(h\) elements (with repetition, unordered) are distinct; \(B_2\) is the Sidon case. A **\(B_h[g]\) set** relaxes this so each sum has at most \(g\) representations. The Bose–Chowla construction produces \(B_h\) sets of near-optimal size inside \(\{1,\dots,q^h\}\) from the multiplicative structure of \(\mathbb{F}_{q^h}\); the extremal function \(F_h(N)=\max|B_h\cap\{1,\dots,N\}|\) generalizes \(F(N)=F_2(N)\) and carries its own open second-order questions.

**Adopted formulations.**
- (i) Exact \(F(N)\) for specified \(N\).
- (ii) Structure of \(E(N)\) over an explicitly computed range.
- (iii) Existence / nonexistence of a planar difference set of a specified order \(q\).

No informal target is accepted.

**Link to problem 04.** A planar difference set of order \(q\) yields a projective plane \(\mathrm{PG}(2,q)\); Singer's theorem constructs one for every prime power \(q\). The prime-power conjecture asserts these exist only for prime-power \(q\). Order \(q=12\) (\(v=157\)) is open - the same wall as problem 04's projective plane of order 12 - so a certified difference-set search modulo \(157\) is a shared attack surface.

## 2. Resolution standard

Three tracks, each with a crisp standard.

**(A) Exact \(F(N)\).** For a specified \(N\), the exact integer \(F(N)=s\), delivered as an **extremal-Sidon certificate**:
- an explicit \(s\)-element Sidon set in \(\{1,\dots,N\}\), verified by exhibiting all \(\binom{s}{2}\) differences pairwise distinct; and
- a certified proof that no \((s+1)\)-element Sidon set fits in \(\{1,\dots,N\}\) - an exhaustive backtracking search with justified pruning, or a SAT UNSAT (DRAT/LRAT), or an ILP infeasibility certificate.

**(B) Error term.** A genuine theorem on \(E(N)\) - e.g. a proof that

\[
E(N)=F(N)-\sqrt N = O(1),
\]

or a disproof exhibiting \(\limsup_N |E(N)|=\infty\) - is the (famous, hard) resolution. Short of it, certified bounds on \(E(N)\) over an explicit verified range of \(N\), obtained as a by-product of exact \(F(N)\) computation.

**(C) Difference sets.** For a specified order \(q\):
- an explicit planar difference set modulo \(q^2+q+1\), verified by checking that its \(q(q+1)\) ordered differences hit each nonzero residue exactly once; or
- a certified **nonexistence** proof for the cyclic case (exhaustive orbit search under the multiplier group, or a SAT UNSAT).

**Not accepted as resolution.**
- An asymptotic statement \(F(N)=\sqrt N+O(N^{1/4})\), or a numerically-fitted error term, presented as an exact value or as settling \(E(N)\).
- A large Sidon set without a matching, certified upper bound.
- Existence / nonexistence of a difference set asserted from a partial or heuristic search without a checkable certificate.
- Any floating-point or probabilistic argument used for certification.

## 3. Graded partial-result targets

- **\(P_1\) - reproduce the \(F(N)\) table.** Recompute exact \(F(N)\) for the range already in the literature / OEIS with our own exhaustive search + optimality certificates.
  - *Certificate:* extremal sets + difference-distinctness checks + replayable UNSAT / backtracking completeness.

- **\(P_2\) - one new exact \(F(N)\).** For the smallest open \(N\), certify \(F(N)\) with an extremal-Sidon certificate.
  - *Certificate:* the full track-(A) artifact.

- **\(P_3\) - extend the exact table and mine \(E(N)\).** A contiguous new range of exact \(F(N)\), with the sequence \(E(N)=F(N)-\sqrt N\) tabulated and any monotonicity / plateau structure recorded as certified data (not proof).
  - *Certificate:* per-\(N\) artifacts + a data manifest.

- **\(P_4\) - difference-set construction or refutation.** Certify a Singer / Bose–Chowla difference set for a new parameter, or a **nonexistence** certificate for the cyclic planar difference set of a specified composite order (target the \(q=12\), \(v=157\) case shared with problem 04).
  - *Certificate:* difference-multiset check, or exhaustive orbit search / SAT UNSAT.

- **\(P_5\) - certified error-term bounds over a range.** Verified interval bounds \(c_1\le E(N)\le c_2\) for all \(N\) in an explicit computed window, or a certified \(B_h[g]\)-generalization value.
  - *Certificate:* the union of per-\(N\) exact values with a completeness argument for the window.

- **\(P_6\) - strongest short of resolution.** A certified improvement to the upper-bound constant in \(F(N)\le\sqrt N+cN^{1/4}\) validated over a verified range, or an extremal construction beating Singer / Bose–Chowla density on a range. The error-term theorem itself is a windfall.

## 4. Known results and prior art

- Sidon (1932) introduced \(B_2\) sets; Erdős–Turán (1941) proved the \(\sqrt N+N^{1/4}+1\)-type upper bound and the \(\sqrt N+O(N^{1/4})\) asymptotic.
- Singer (1938) constructed cyclic planar difference sets from \(\mathrm{PG}(2,q)\), \(q\) a prime power; Bose (1942) and Bose–Chowla (1962/63) gave \(B_2\) and \(B_h\) constructions of near-optimal density.
- Lindström (1969) sharpened the upper bound to \(F(N)<\sqrt N+N^{1/4}+1\).
- Erdős's conjecture / prize problem: whether \(F(N)-\sqrt N=O(1)\) (or \(O(N^\varepsilon)\)); widely open.
- Ruzsa (1998) gave alternative Sidon constructions; Cilleruelo (2000s–2010) gave precise results and \(B_h[g]\) generalizations.
- Prime-power conjecture for planar difference sets (Hall, Ryser); multiplier theorems (Hall) constrain cyclic searches. The order-10 projective plane was ruled out (Lam–Thiel–Swiercz, 1989); order 12 is open - see problem 04.
- Existence of a cyclic planar difference set of order \(q\) is known for all prime powers \(q\le\) large bounds and excluded for various non-prime-powers by exhaustive search and by multiplier / character-sum arguments; \(q=12\) (\(v=157\)) is the smallest fully open cyclic case aligned with problem 04.
- Exact \(F(N)\) values appear in OEIS (confirm the precise A-number for the extremal function; it is distinct from A005282, the greedy Mian–Chowla sequence, which is *not* extremal). The related perfect-difference-set and \(B_h\) sequences are separately indexed.

**Status as of mid-2026 - re-verify against the current literature before starting any session.** Confirm the current extent of exact \(F(N)\) tables and any recent error-term or difference-set results.

## 5. Attack plan

`[search]` on a single workstation.

**Exact \(F(N)\) by backtracking.** Depth-first, add elements \(1\le x_1<\dots<x_s\le N\), maintaining a bitset of used differences; reject an added element that repeats a difference. Branch-and-bound with the incumbent \(s\); prune by the Erdős–Turán / Lindström upper bound and by density arguments on the remaining interval. Break the reflection symmetry

\[
x\ \longmapsto\ N+1-x
\]

by fixing \(x_1\) small / lex-least. For the certified upper bound, a **SAT** encoding uses a variable \(z_x\) per \(x\in\{1,\dots,N\}\), a clause per equal-difference quadruple \(x+w=y+u\) forbidding all four, and cardinality \(\sum_x z_x\ge s+1\); solve with kissat / CaDiCaL and emit DRAT for UNSAT. ILP is a parallel route with a Farkas certificate.

**Difference sets.** Search cyclic \((v,k,1)\)-difference sets modulo \(v=q^2+q+1\) by orbit-reduced backtracking, using the multiplier theorem to fix a numerical multiplier and restrict to multiplier-invariant sets. Concretely:
- normalize \(D\) so that a chosen multiplier \(t\) (a prime dividing \(q\), by Hall's multiplier theorem) fixes \(D\) setwise, so \(D\) is a union of \(t\)-multiplier orbits modulo \(v\);
- assemble \(D\) from orbits, maintaining a running difference-tally and backtracking on any residue that would be hit twice;
- verify a completed candidate by forming the multiset of \(k(k-1)\) differences and checking that each nonzero residue occurs exactly once.

For nonexistence, exhaust the multiplier-reduced search space or encode it as SAT UNSAT with DRAT. For \(q=12\), \(v=157\), the modulus is small enough that the multiplier-reduced search is a realistic single-workstation task and directly informs problem 04.

**Cross-link to problem 17.** Sidon sets over \(\mathbb{F}_3^n\) are closely related to caps: a set with all pairwise sums distinct in \((\mathbb{Z}/3\mathbb{Z})^n\) is exactly a set with no solution to \(x+y=z+w\) beyond the trivial, which for distinct triples is the cap (no-3-term-progression) condition. Toolchain and symmetry-breaking ideas transfer directly between this problem and the cap-set search of problem 17; verified components should be shared.

**Scope and failure modes.** Exact \(F(N)\) by backtracking is feasible up to \(N\) in the low thousands; the SAT UNSAT certificate for the upper bound is the bottleneck and sets the true frontier. Cyclic difference-set search for \(v=157\) is small enough to attempt with multiplier reductions. Expected failure modes:
- backtracking / SAT blow-up in \(N\);
- weak pruning bounds;
- the multiplier theorem alone not pinning the search enough, leaving an infeasible exhaustive residue.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Difference-distinctness, difference-multiset counts, and all set arithmetic are exact integer computations; upper bounds carry DRAT/LRAT (SAT), exact Farkas (ILP), or replayable backtracking-completeness certificates. Floating point - including \(\sqrt N\) in \(E(N)\) - is used only for reporting, with exact comparisons done via \((F(N))^2\) versus \(N\).
2. **Independent verification.** A standalone Sidon-checker (all pairwise differences distinct) and a standalone difference-set checker (each nonzero residue once), both independent of the search; a DRAT checker for UNSAT; enumeration replay for exhaustive claims. Dual formulations (sum-distinct vs. difference-distinct) cross-check the Sidon property.
3. **Reproducibility.** \(N\), encodings, symmetry-breaking predicates, multiplier choices, solver versions, and seeds are recorded; a SHA-256 manifest spans set files, CNFs, proof traces, and logs.
4. **Preservation.** The search and construction source is part of the record; anything not preserved is stated explicitly (the Hadamard-668 lost-source lesson).
5. **Honest reporting.** The report states up front whether an exact \(F(N)\), an error-term bound, or a difference-set determination was achieved, and never presents an asymptotic statement, an unmatched lower bound, or a heuristic search as a resolution.
