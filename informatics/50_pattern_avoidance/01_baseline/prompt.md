# PROMPT FOR CERTIFIED BOUNDS ON A POWER-FREE-WORD GROWTH RATE OR AVOIDANCE THRESHOLD

## Open frontiers in repetition avoidance - growth rates, pattern/formula thresholds, abelian and undirected variants (Dejean excluded)

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 50 of 50  
**Area:** search, sequences & games  
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The combinatorics of repetition-avoiding words began with Thue's ternary square-free and binary overlap-free sequences and remains full of exact, machine-checkable open questions. **One central problem is closed and is not a target here:** Dejean's conjecture on the repetition threshold \(\mathrm{RT}(k)\) was **proven** (final cases ~2009, published 2011, by Rao and independently by Currie–Rampersad, after Carpi's large-alphabet reduction). This prompt is deliberately re-scoped to the still-open frontiers: the exact **growth rate (entropy)** of power-free languages - for ternary square-free words only bracketing bounds are known, not the exact constant - together with **pattern/formula avoidance thresholds**, **abelian-power avoidance thresholds**, and the **undirected repetition threshold**. These are a strong fit for certified computation: word counts are exact big-integer transfer-matrix/DP computations, growth rates are pinned by rigorous interval bounds, and avoidance of a pattern by a morphic word is verified by a finite, checkable test. The verifier that closes the loop is an exact language-counting engine plus interval arithmetic (for growth rates) or a machine-checked avoidance proof (for thresholds). Anything short of a rigorously bracketed bound or a checkable avoidance certificate - a floating-point growth-rate estimate, or a morphism asserted power-free without verification - is a partial result; and any drift back onto Dejean's (settled) \(\mathrm{RT}(k)\) is out of scope.

## 1. Exact problem statement

Fix an alphabet \(\Sigma_k=\{0,1,\dots,k-1\}\). For a finite word \(v\) with smallest period \(p\) (so \(v_i=v_{i+p}\) where defined), the **exponent** is \(\exp(v)=|v|/p\); a **fractional power** of exponent \(\alpha\) is any factor \(v\) with \(\exp(v)\ge\alpha\). A word is **\(\alpha\)-power-free** if no factor has exponent \(\ge\alpha\), and **\(\alpha^+\)-power-free** if none has exponent \(>\alpha\). A **square** is a \(2\)-power \(xx\); an **overlap** is a \(2^+\)-power. For example, over \(\Sigma_3\)

\[
0102012021\cdots
\]

can be continued to an infinite square-free word (Thue), whereas over \(\Sigma_2\) every word of length \(\ge4\) contains a square, so squares are unavoidable on two letters.

**Repetition threshold (Dejean - PROVEN, not a target).**

\[
\mathrm{RT}(k)=\inf\{\alpha : \text{an infinite } \alpha^{+}\text{-power-free word over } \Sigma_k \text{ exists}\}.
\]

Dejean's theorem gives \(\mathrm{RT}(2)=2\), \(\mathrm{RT}(3)=\tfrac74\), \(\mathrm{RT}(4)=\tfrac75\), and \(\mathrm{RT}(k)=\tfrac{k}{k-1}\) for \(k\ge5\). **This is settled; do not attempt to re-prove or "compute" it.** It is stated only to fix terminology and to gate the scope.

**Open target A - growth rate of a power-free language.** For a factorial (factor-closed) language \(L\) let \(L_n=\#\{w\in L:|w|=n\}\). Because a square-free word of length \(m+n\) restricts injectively to its length-\(m\) prefix and length-\(n\) suffix,

\[
L_{m+n}\le L_m\,L_n,
\]

so by Fekete's lemma the limit

\[
\beta(L)=\lim_{n\to\infty} L_n^{1/n}=\inf_{n} L_n^{1/n}
\]

exists and is the **growth rate** (its logarithm the entropy). For the ternary square-free language the exact value of \(\beta\) is **open**; numerically \(\beta\approx 1.3017597\) (verify), with only rigorous - but non-tight - upper and lower bounds proven. The subadditivity above is precisely why each exact count \(L_n\) is a rigorous *upper* bound \(\beta\le L_n^{1/n}\); the *lower* bound is the hard side.

**Open target B - avoidance thresholds.** The **avoidability index** \(\lambda(P)\) of a pattern \(P\) is the least \(k\) over which \(P\) is avoidable; the repetition threshold of a pattern or formula, and the exponents at which specific patterns become avoidable, include open cases.

**Open target C - abelian and undirected variants.** An **abelian \(m\)-power** is a factor \(w_1w_2\cdots w_m\) whose blocks are permutations of one another, i.e. equal Parikh vectors

\[
\psi(w_1)=\psi(w_2)=\cdots=\psi(w_m),\qquad \psi(w)=\bigl(\#_0(w),\dots,\#_{k-1}(w)\bigr).
\]

The **abelian repetition threshold** \(\mathrm{ART}(k)\) is the abelian analogue of \(\mathrm{RT}(k)\) and is open for most \(k\); the **undirected repetition threshold** (a recent variant treating a word and its reversal alike) has open values.

**Target.** Fix one concrete open quantity - the ternary (or another) square-free/power-free growth rate, a specific pattern's avoidability threshold, an \(\mathrm{ART}(k)\), or an undirected-threshold value - and certify improved rigorous bounds, or an exact value where a finite certificate exists. The quantity, the alphabet, and the exact/`>`/`≥` conventions are fixed and stated.

A reader starting from this prompt alone has alphabets, factors, exponents, power-freeness, the (settled) repetition threshold, the growth rate, and the avoidance/abelian/undirected targets.

## 2. Resolution standard

**Named certified form: exhaustive search or transfer-matrix computation with exact (rational/interval) arithmetic and a checked certificate.** A resolution consists of independently checkable artifacts appropriate to the target.

1. **Growth-rate upper bound.** An exact big-integer count \(L_n\) for a specific \(n\), from which \(\beta\le L_n^{1/n}\) follows by subadditivity; the \(n\)-th root is bracketed above in exact interval arithmetic. The count plus the counting automaton is the certificate.
2. **Growth-rate lower bound.** A certified sub-language (a subshift generated by an explicit morphism, or a transfer matrix on an explicit factor set) whose count grows at rate \(\ge\gamma\), with \(\gamma\) a rigorously bracketed lower bound of the transfer matrix's Perron root; then \(\beta\ge\gamma\).
3. **Avoidance threshold.** For "pattern \(P\) is avoidable over \(\Sigma_k\)", an explicit infinite word (a morphic fixed point) with a **machine-checked avoidance proof** - a finite test over a bounded window certifying the image avoids \(P\). For "unavoidable", an exhaustive finiteness proof (the language of \(P\)-avoiding words over \(\Sigma_k\) is finite, shown by complete backtracking).

For any exact-value claim both matching bounds are mandatory; a bracketing result reports the certified interval

\[
\gamma\ \le\ \beta\ \le\ L_n^{1/n},
\]

with both endpoints proven. Every arithmetic step is exact or interval - never bare floating point.

**Not accepted as resolution.**

- **Targeting Dejean's \(\mathrm{RT}(k)\)** in any form (re-proving it, "computing" it, or presenting a repetition-threshold value as new) - it is proven and out of scope.
- A floating-point estimate of a growth rate without a rigorous enclosing interval.
- Conflating the repetition threshold (an exponent) with the growth rate (an entropy) - different quantities with different answers.
- A morphic word asserted power-free/pattern-avoiding without a finite checkable verification; an "unavoidable" claim from a partial search.
- An asymptotic statement where a rigorous bound or exact value is asked, or a transfer-matrix eigenvalue computed only numerically.

## 3. Graded partial-result targets

Ordered from reproducing the known frontier to the strongest result short of an exact growth rate. Each names its certificate.

**P1 - Reproduce exact power-free counts.** Recompute the counts \(L_n\) of ternary square-free words up to a known \(n\) (the published range reaches into the low hundreds) with an exact big-integer engine, matching the record sequence.
*Certificate:* the count sequence with the counting automaton, diffed against the published values.

**P2 - Reproduce known growth-rate bounds.** Re-derive a published rigorous upper bound (via \(L_n^{1/n}\)) and a published lower bound (via a certified construction) for the ternary square-free growth rate.
*Certificate:* interval-arithmetic brackets matching the cited bounds and access dates.

**P3 - Narrow the growth-rate interval.** Certify a strictly tighter upper or lower bound on a specific power-free growth rate than the published record, with exact/interval arithmetic.
*Certificate:* the improved bound with its exact computation and the prior record cited.

**P4 - Pattern avoidability threshold.** For a specific pattern or formula with open avoidability, certify its avoidability index (a morphic witness with a checked avoidance proof, plus a finiteness proof at \(k-1\)).
*Certificate:* the morphism, the window-check certificate, and the exhaustive finiteness proof.

**P5 - Abelian repetition threshold.** For a specific \(k\), certify an improved bound (or a value) of \(\mathrm{ART}(k)\), with a checked abelian-avoidance construction or an exhaustive obstruction.
*Certificate:* the construction with an abelian-avoidance verifier, or the finiteness proof.

**P6 - Undirected / formula threshold.** Certify a value or improved bound of the undirected repetition threshold, or of a specific formula's threshold, with a checkable certificate.
*Certificate:* the construction or exhaustive proof, independently replayed.

**P7 - Extend exact counts and mine structure.** Extend a power-free count sequence beyond the published length and mine the data (letter frequencies, entropy trend) for a precise conjecture.
*Certificate:* the extended exact sequence with a replay script; no bound claimed beyond what interval arithmetic certifies.

## 4. Known results and prior art

- A. Thue (~1906, 1912): an infinite ternary square-free word and an infinite binary overlap-free word exist - the origin of the subject, and the base cases \(\mathrm{RT}(2)=2\) and the existence side of the ternary problem.
- Shur's theory frames these as questions about the growth of \(\alpha\)-power-free languages, unifying the counting and threshold viewpoints.
- **Dejean's theorem (settled):** conjectured by F. Dejean (~1972); \(\mathrm{RT}(2)=2\) (Thue), \(\mathrm{RT}(3)=7/4\) (Dejean), \(\mathrm{RT}(4)=7/5\) (Pansiot ~1984), \(\mathrm{RT}(k)=k/(k-1)\) for \(k\ge5\).
- The remaining cases were closed by A. Carpi (large \(k\), ~2007), then J. Currie–N. Rampersad and independently M. Rao (~2009, published ~2011); earlier partial ranges by Moulin-Ollagnier and others (verify). **This result is complete and out of scope - the prompt gates against re-deriving it.**
- Ternary square-free growth: early bounds by Brandenburg (~1983) and Brinkhuis; Baake–Grimm and Richard–Grimm estimated the entropy (growth rate \(\approx 1.3017597\)); Kolpakov (~2007) gave efficient counting.
- A. Shur developed the cluster/cell method giving rigorous upper and lower bounds that can be pushed arbitrarily close, yet the **exact value of \(\beta\) remains open** - the gap between best certified bounds is what a session narrows.
- Exact counts of ternary square-free words were computed to \(n=110\) (Grimm, ~2001) and extended toward \(n\approx141\) (verify); the sequence is recorded in OEIS (verify the id).
- A. Shur's theory of power-free-language growth (connective constants; the growth of \(\alpha\)-power-free languages); Shur's conjecture on power-free-language growth over large alphabets was proven (~2025, MFCS - verify).
- Pattern avoidability: Bean–Ehrenfeucht–McNulty and Zimin (characterization of avoidable patterns); Cassaigne and Ochem determined many avoidability indices, with open cases remaining (verify).
- Abelian repetitions: V. Keränen (~1992) constructed an abelian-square-free word over 4 letters (abelian squares are unavoidable on 3), a standard validation baseline.
- The abelian repetition threshold \(\mathrm{ART}(k)\) (Samsonov–Shur) is conjectured but open for small \(k\); the abelian setting is subtler than the ordinary one because Parikh-equality is weaker than equality (verify current partial results).
- Undirected repetition threshold: a recent line (Currie, Mol, Rampersad, ~2020s) with values still being determined (verify).
- Tooling note: Walnut (Mousavi/Shallit) mechanically proves avoidance/repetition properties of automatic and morphic sequences and can produce machine certificates.

**Status as of mid-2026 - re-verify against the current literature (and OEIS) before starting any session; in particular confirm Dejean's theorem remains fully settled and out of scope.**

## 5. Attack plan

`[search]` - first computations on one workstation. Growth-rate work splits into a cheap exact upper bound (counting) and a harder certified lower bound (transfer matrix); avoidance work splits into a construction with a checkable proof and an exhaustive finiteness search.

- **Exact counting engine (P1, P3, P7).** Recognize power-free words by their forbidden factors (an Aho–Corasick automaton over the minimal forbidden squares/powers) and count length-\(n\) words by dynamic programming with big integers (FLINT / Python `int`).
- **Validate the engine.** Reproduce the published \(L_n\) sequence exactly before any bound is trusted; a single wrong count invalidates every downstream bracket.
- **Growth-rate upper bounds.** From exact \(L_n\), bracket \(\beta\le L_n^{1/n}\) using interval arithmetic (Arb) for the root - never a floating-point `pow`. Subadditivity makes each exact count a rigorous upper bound.
- **Growth-rate lower bounds.** Construct an explicit sub-shift of the language - a morphic image, or an explicit set of allowed factors closed under the avoidance constraint - and form its transfer (adjacency) matrix \(T\). Its Perron root \(\rho(T)\) lower-bounds \(\beta\).
- **Certifying the Perron root.** Bracket \(\rho(T)\) from below in exact arithmetic: rational power iteration with interval rounding, or an exact enclosure of the largest root of the integer characteristic polynomial (Sturm/interval). The certified \(\gamma\le\rho(T)\) yields \(\beta\ge\gamma\); a bare floating-point eigenvalue is not accepted.
- **Avoidance, avoidable direction (P4, P6).** Exhibit a morphism \(h:\Sigma_k^\ast\to\Sigma_k^\ast\), generate its fixed point, and verify avoidance by the standard bounded-window test set - a finite check that no image \(h(u)\) of a short word \(u\) contains the forbidden pattern - optionally machine-checked in Walnut. The window bound must be provably sufficient for the pattern in question.
- **Avoidance, unavoidable direction.** Exhaustive backtracking that the \(P\)-avoiding language over \(\Sigma_{k}\) is finite: grow all \(P\)-avoiding words letter by letter; if the tree is finite the pattern is unavoidable at that alphabet size, with the tree itself the certificate.
- **Abelian (P5).** Track Parikh vectors along a backtracking search or a morphic construction; reproduce Keränen's abelian-square-free word as a validation baseline; verify abelian-power-freeness with an exact Parikh-vector checker.
- **Mechanized proofs.** Where the witness word is automatic or morphic, encode the avoidance property in Walnut and preserve its machine certificate - an independent, replayable proof object beyond our own verifier.
- **One-workstation scope.** The counting DP is cheap into the hundreds of letters; the certified lower bound via transfer matrices is the effort-limited half, since tighter bounds need larger factor sets and bigger matrices.
- **Failure modes.** Expect (i) transfer matrices too large for a tight lower bound; (ii) floating-point \(n\)-th roots or eigenvalues silently giving a non-rigorous "bound" (forbidden - interval/exact only); (iii) a morphism's avoidance proof with an inadequate window, where the test set is not provably sufficient; (iv) drifting onto Dejean's settled threshold; (v) conflating growth rate with repetition threshold. Report the certified interval actually obtained, never a numerical guess.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Word counts are exact big integers; growth-rate bounds use interval/exact arithmetic (Arb/FLINT) for every root and eigenvalue; avoidance is a finite checkable test. Floating point is for exploration only and never underlies a reported bound.
2. **Independent verification.** The counting engine, the interval-bound computation, and the avoidance verifier are separate programs; each count is reproduced by a second implementation; each morphic avoidance claim is re-checked by an independent test set (and, where possible, by Walnut).
3. **Reproducibility.** The target quantity and conventions, the forbidden-factor automaton, morphisms, transfer matrices, tool names and versions, and any seeds are recorded; a SHA-256 manifest covers count files, certificates, and logs. Every reproduced or improved bound cites its baseline with source and access date.
4. **Preservation.** Counting engine, bound computation, and avoidance-verifier source are part of the record. Any discarded run or lost certificate is stated explicitly.
5. **Honest reporting.** The report states up front which open quantity was addressed, the certified interval or exact value obtained, and in which convention; it explicitly confirms the work did **not** target Dejean's settled threshold, and never presents a numerical estimate as a certified bound or a growth rate as a repetition threshold.
