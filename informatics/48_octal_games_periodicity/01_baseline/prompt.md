# PROMPT FOR A CERTIFIED PERIODICITY RESULT ON AN OCTAL GAME

## The eventual periodicity of the Grundy (nim-value) sequence of a specific octal game

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 48 of 50  
**Area:** search, sequences & games  
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

An octal game is a heap-splitting/removal game specified by a code \(.d_1 d_2 d_3\cdots\); by the Sprague–Grundy theory each heap size \(n\) has a nim-value \(G(n)\), and the sequence \(G(0),G(1),G(2),\dots\) governs all play. A central conjecture (Guy; Berlekamp–Conway–Guy) holds that every finite octal game has an **eventually arithmetic-periodic** Grundy sequence, yet it is unproven for many games - including the flagship Grundy's game and small octal games such as \(.007\) - while others (Dawson's chess, \(.137\)) are proven ultimately periodic. This is an exceptionally clean fit for certified computation because of the **Guy–Smith periodicity theorem**: eventual periodicity of a *finite* octal game is decided by verifying a recurrence over a finite, explicitly bounded window. So a period, once found, yields a genuine finite proof of periodicity for all larger heaps; and where no period is found, a certified massive extension of the sequence is itself a result. The verifier that closes the loop is an independent recomputation of the Grundy sequence (mex of the option-set values) plus a mechanical check of the periodicity window. Anything short of that - an apparent period not verified across the theorem's window, or an unreplayable computation - is a partial result, never a solution.

## 1. Exact problem statement

An **octal game** has code \(.d_1 d_2 d_3\cdots\) with each digit \(0\le d_k\le 7\). A move removes \(k\) tokens from a chosen heap; the digit \(d_k\), read in binary as \(d_k=b_2 b_1 b_0\), permits:

- \(b_0=1\): remove a whole heap of exactly \(k\) tokens (leaving 0 heaps);
- \(b_1=1\): remove \(k\) tokens from a larger heap, leaving one nonempty heap;
- \(b_2=1\): remove \(k\) tokens and split the remainder into two nonempty heaps.

A finite octal game has finitely many nonzero digits; let \(d\) be the index of the last nonzero digit.

**Grundy values.** Under normal play (last move wins), the nim-value of a single heap is

\[
G(n)=\operatorname{mex}\{\,G(a)\oplus G(b) : \text{a legal move sends a heap of } n \text{ to heaps } a,b\,\},
\]

with \(\operatorname{mex}\) the least non-negative integer absent from the set, \(\oplus\) the bitwise XOR, and an empty option (no split) contributing \(G(a)\) alone. By the Sprague–Grundy theorem a disjunctive sum of heaps of sizes \(n_1,\dots,n_r\) has value

\[
G(n_1)\oplus G(n_2)\oplus\cdots\oplus G(n_r),
\]

so the whole game is determined by the single-heap **Grundy sequence** \(\bigl(G(n)\bigr)_{n\ge 0}\).

**Eventual (arithmetic) periodicity.** The sequence is *eventually periodic* with period \(p\) and preperiod \(t\) if

\[
G(n+p)=G(n)\qquad\text{for all } n\ge t.
\]

Some games are *arithmetic-periodic* with **saltus** \(s\): \(G(n+p)=G(n)+s\) for \(n\ge t\).

**Guy–Smith periodicity theorem (the certified handle).** For a finite octal game with last nonzero digit at index \(d\), suppose a candidate period \(p\), preperiod \(t\), and saltus \(s\) are proposed. If the recurrence

\[
G(n+p)=G(n)+s\qquad\text{holds for all } n \text{ with } t\le n \le 2p+t+d,
\]

(equivalently, over \(t+\max\{d,\text{depth}\}\) successive values beyond the preperiod), then it holds for **all** \(n\ge t\). Eventual periodicity is thus a finitely checkable property - the entire open question, for any game where a period exists, reduces to a bounded computation.

**Reference games.** Nim is the octal game \(.333\cdots\); Dawson's chess is \(.137\); and **Grundy's game** removes no tokens but splits a heap into two *unequal* parts, so

\[
G(n)=\operatorname{mex}\bigl\{\,G(a)\oplus G(n-a)\ :\ 0<a<n-a\,\bigr\}.
\]

Grundy's game lies in the same nim-value family but is not itself an octal game, a distinction that matters for which periodicity theorem applies.

**Target.** Fix a specific octal game (or Grundy's game). Either (i) certify its eventual (arithmetic) periodicity by exhibiting \(p,t,s\) and verifying the periodicity window; or (ii) where no period is found, produce a certified extension of the Grundy sequence to a documented length \(N\), with the search reproducible. The quantity of interest is the pair (period, preperiod) or the certified extent \(N\).

A reader starting from this prompt alone has the octal code semantics, the Grundy recurrence, eventual/arithmetic periodicity, and the finite periodicity criterion.

## 2. Resolution standard

**Named certified form: verified Grundy-sequence computation.** A resolution consists of independently checkable artifacts.

1. **Periodicity claim.** The triple \((p,t,s)\) plus a Grundy sequence \(G(0),\dots,G(M)\) computed to \(M\ge t+p+\max\{d,\text{depth}\}\), together with a mechanical check that the Guy–Smith window recurrence holds across the required range. An independent recomputation of \(G\) (a second implementation of the mex/XOR recurrence) must reproduce the sequence bit-for-bit, and the window check must be re-runnable.
2. **Certified extension (when no period is found).** A Grundy sequence to length \(N\) with a reproducible search, an independent recomputation confirming it, and a report of the observed value distribution and the largest heap-index reached. This is a bounded result, not a periodicity proof.

For periodicity, the theorem's window is mandatory: a period is proven only when the recurrence is verified across the full Guy–Smith range

\[
t\ \le\ n\ \le\ 2p+t+d,
\]

not merely observed on whatever prefix happened to be computed.

**Not accepted as resolution.**

- An apparent period read off the data but not verified over the Guy–Smith window (the sequence may break after the observed range - this has happened historically).
- A periodicity claim without the finite-window theorem, or with the window applied to a game to which it does not apply (e.g. treating Grundy's game as a finite octal game without justification).
- A single-implementation computation with no independent recomputation, or an extension that cannot be replayed.
- Floating point or heuristic shortcuts in the mex/XOR recurrence; asymptotic hand-waving where an exact (period, preperiod) is asked.
- A machine-learned or statistically-inferred "period" - the theory offers an exact finite test, and only that test certifies.

## 3. Graded partial-result targets

Ordered from reproducing known results to the strongest result short of settling a flagship open game. Each carries its own certificate standard - the artifact that proves it and how it is independently checked.

**P1 - Reproduce a proven-periodic game.** Recompute the Grundy sequence of Dawson's chess (\(.137\)) and re-verify its ultimate periodicity via the Guy–Smith window with two independent implementations.
*Certificate:* bit-identical sequences from two codebases; a re-runnable window check.

**P2 - Reproduce a settled large-period game.** Recompute a known large-period octal game (e.g. \(.106\)) far enough to re-confirm the published (period, preperiod), or honestly report the reachable extent.
*Certificate:* independent recomputation matched against the cited record and access date.

**P3 - New certified periodicity.** For a currently unsettled finite octal game, find a period and certify eventual periodicity through the Guy–Smith window.
*Certificate:* \((p,t,s)\), the window verification, and dual-implementation agreement under a SHA-256 manifest.

**P4 - Certified extension of an open sequence.** For Grundy's game or another open game (\(.007\) etc.), extend the certified Grundy sequence beyond the current published extent, with a reproducible search and independent recomputation.
*Certificate:* the sequence to length \(N\), the search log, and a dual-implementation check; the new extent stated against the prior record.

**P5 - Structural report.** From the extended data, report the value spectrum, the frequency of rare values, and any window statistics bearing on the periodicity conjecture, each figure recomputed independently.
*Certificate:* the statistics with a replay script; no periodicity claimed beyond the certified window.

**P6 - Cross-check against cgsuite.** Validate our engine against an independent tool (cgsuite) on a battery of small games, establishing a trusted baseline before any new claim.
*Certificate:* a diff table showing agreement on all tested games.

**P7 - Window-refutation report.** For a game where a widely-quoted candidate period is folklore, either certify it through the window or exhibit the exact index at which the recurrence first fails, settling the folklore.
*Certificate:* the window check output, with the first failing index if any.

## 4. Known results and prior art

- Sprague (~1935) and Grundy (~1939) established the nim-value theory independently; the mex/XOR recurrence and disjunctive-sum rule are the foundation, and every claim here descends from them.
- R. Guy and C. Smith, "The G-values of various games" (~1956), introduced the systematic octal-game framework and the finite periodicity theorem that makes eventual periodicity checkable.
- Berlekamp, Conway, and Guy, *Winning Ways* (~1982), conjectured that every finite octal game is eventually arithmetic-periodic - still open, and a headline problem of the field.
- Dawson's chess is octal game \(.137\); it is proven ultimately periodic (period 34, with finitely many exceptions) - verify the exact period and exceptional set.
- A. Flammenkamp's octal-games page records the frontier: \(.106\) settled with period \(328{,}226{,}140{,}474\) and preperiod \(465{,}384{,}263{,}797\) (2002); \(.454\) with period \(60{,}620{,}715\), preperiod \(160{,}949{,}019\); \(.104\) with period \(11{,}770{,}282\), preperiod \(197{,}769{,}598\) (verify all figures). Roughly 65 two-digit and 8 three-digit octal games remain unsettled, along with Grundy's game and \(.6\overline{1}\).
- Grundy's game (split a heap into two unequal heaps) is computed to heap index \(21{,}544{,}358{,}589\) (ultimate depth 42) with no period yet found; whether its Grundy sequence is eventually periodic is open (verify the current extent).
- A caution specific to Grundy's game: its splitting rule is not captured by the octal formalism, so the standard finite-octal periodicity theorem does not directly apply; any periodicity certificate there needs a separately justified criterion.
- Values of Grundy's game are recorded in OEIS (sequence A002188 and related); re-verify the id and the extent before use.
- Tools: cgsuite (A. Siegel) computes combinatorial-game and Grundy values; Flammenkamp's space-efficient rare-value algorithm underlies the large computations.

**Status as of mid-2026 - re-verify against the current literature (and Flammenkamp's tracker) before starting any session.**

## 5. Attack plan

`[search]` - first computations on one workstation. The whole plan rests on a trusted Grundy engine plus a separate, trusted window checker; scale comes last.

- **Two independent engines.** Implement the mex/XOR Grundy recurrence twice - once in a CAS/high-level language (or cgsuite) for correctness, once in cache-friendly C++ for scale. Require bit-identical output on every game before trusting either.
- **Correctness of the option enumeration.** For each heap size, the option set must enumerate exactly the moves the octal digits license (whole-heap removal, single-residue, and two-part splits); an off-by-one in the split range silently corrupts every downstream value, so this is unit-tested against hand-computed prefixes.
- **Reproduce (P1, P2, P6).** Recompute \(.137\), a large-period game, and a battery of small games; diff against cgsuite and against published (period, preperiod) values. This validates the pipeline and the window checker before any novel search is trusted.
- **Window checker.** Implement the Guy–Smith criterion as a standalone routine: given \((p,t,s)\) and a computed prefix, verify \(G(n+p)=G(n)+s\) across the required window and certify (or refute) eventual periodicity. It must be separate from the sequence generator so a bug in one cannot mask a bug in the other.
- **Value-width safety.** Grundy values and heap indices both grow; use index and value types wide enough that no XOR or counter overflows across the full computed range, and assert this at run time.
- **Scale for extensions (P4).** Use the rare-value / sparse-representation technique of Flammenkamp: store only the positions of infrequent Grundy values, since a small set of common values dominates the sequence. This is what makes billions of heap-indices reachable on one machine.
- **Checkpointing.** Log periodic checkpoints of the generator state so the search is replayable and resumable, and so an independent recomputation can restart from any checkpoint rather than from zero.
- **Search for new periods (P3).** For unsettled finite games, compute far enough to expose a candidate period, then invoke the window checker. A candidate that fails the window is discarded, not reported - the historical lesson is that plausible periods can break after millions of terms.
- **Rare-value monitoring.** Track the largest Grundy value and the positions of rare values as the sequence grows; a sudden new maximal value near a suspected period is a red flag against periodicity and is logged.
- **One-workstation scope and failure modes.** Memory bandwidth and the \(O(n^2)\)-ish option enumeration are the walls; the largest games needed billions of values and specialized memory layouts. Expect (i) false periods that break beyond the observed range (only the window theorem guards against this); (ii) integer-index and XOR-width overflow at large \(n\) (use 64-bit indices and sufficient value width); (iii) divergence between engines signalling a bug - halt and reconcile; (iv) applying the octal periodicity theorem to Grundy's game without justification. Record the exact extent reached and whether a window-certified period was obtained.

## 6. Verification and auditability requirements

1. **Exact computation.** All Grundy values are exact integers from the mex/XOR recurrence; no floating point, no sampling. A periodicity claim is backed by the Guy–Smith window check, not by visual pattern-matching.
2. **Independent verification.** Two separate implementations of the recurrence must agree bit-for-bit; the window checker is a third, separate program; small-game results are cross-validated against cgsuite.
3. **Reproducibility.** The game code, algorithm, memory layout, checkpoint scheme, tool versions, and any resumption seeds are recorded; a SHA-256 manifest covers the sequence files, logs, and the window certificate. The prior extent or published (period, preperiod) being reproduced or extended is cited with source and access date.
4. **Preservation.** Both engines, the window checker, and the checkpoint data are part of the record. Any discarded run or lost checkpoint is stated explicitly.
5. **Honest reporting.** The report states up front whether a window-certified period was obtained (hence eventual periodicity proven), or only a certified extension of length \(N\) with no period; it never presents an observed-but-unverified period as a proof, and it flags clearly when the octal periodicity theorem does not apply (Grundy's game).
