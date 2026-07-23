# PROMPT FOR A SIMULATION-CERTIFIED MINIMAL OSCILLATOR OF A GIVEN PERIOD

## The smallest Conway-Life oscillator per period - after omniperiodicity was proved

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 32 of 50  
**Area:** discrete dynamics & pattern search  
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

An *oscillator* in Conway's Life (\(\mathrm{B3/S23}\) on \(\mathbb Z^2\)) is a finite pattern that returns exactly to itself after a fixed number of steps and never translates. In December 2023 the community closed the last existence question: **Conway's Game of Life is omniperiodic** - an oscillator exists for *every* period \(p\ge 1\) (the final holdouts, periods 19 and 41, were filled in July 2023). This prompt therefore does **not** target existence of any period. The open, machine-checkable frontier is *minimisation*: for each period \(p\), the **smallest** oscillator by population and by bounding box, minimal-population records, and constrained oscillator variants. As with spaceships, a candidate is settled by deterministically simulating one full period and confirming exact self-return; minimality is pushed by SAT / exhaustive search over a fixed box. The on-machine verifier that closes the loop is a deterministic Life engine (self-return check) together with a SAT/enumeration lower bound where minimality is claimed. Anything short of Section 2 - an existence claim, an unverified period, a "record" without a sourced baseline - is a partial result, never a solution.

## 1. Exact problem statement

**The rule.** With \(n(c,x)\) the live Moore-neighbour count of cell \(x\), the Life map \(T\) is birth on 3, survival on 2 or 3:

\[
(Tc)(x)=\mathbf 1\!\left[\,n(c,x)=3\ \lor\ \bigl(c(x)=1\land n(c,x)=2\bigr)\,\right].
\]

**Oscillator.** A finite nonempty pattern \(O\) is a **period-\(p\) oscillator** when

\[
T^{p}(O)=O,\qquad T^{k}(O)\ne O\ \text{for } 0<k<p .
\]

Because it must return to *itself* (not a translate), \(O\) is not a spaceship. Still-lifes are the degenerate \(p=1\) case and are excluded unless a variant explicitly admits them.

**Rotor, stator, triviality.** Decompose the cells touched over one period into

\[
\mathrm{rotor}(O)=\{x:\ \exists\, k,\ (T^{k}O)(x)\ne (T^{k+1}O)(x)\},
\qquad
\mathrm{stator}(O)=\{x:\ (T^{k}O)(x)=1\ \forall k\}.
\]

An oscillator is **non-trivial** if it does not reduce to a smaller period-\(p\) oscillator plus inert still-life padding - operationally, no strict sub-pattern is itself a period-\(p\) oscillator.

**Size measures.** With the phase convention fixed and reported,

\[
\mathrm{pop}(O)=\max_{0\le k<p}\bigl|\mathrm{supp}(T^{k}O)\bigr|
\ \ (\text{or }\min,\text{ stated}),
\qquad
\mathrm{box}(O)=\text{area of the bounding rectangle of } \textstyle\bigcup_k T^{k}O .
\]

**Minimality problem.** For each period \(p\) let

\[
\mathrm{minpop}(p)=\min_{O:\ \mathrm{period}(O)=p}\mathrm{pop}(O),
\qquad
\mathrm{minbox}(p)=\min_{O:\ \mathrm{period}(O)=p}\mathrm{box}(O).
\]

Determine, or improve the known bounds on, these quantities and exhibit witnesses. Both are cell-exact and finite-window-decidable.

**Finite-window reduction.** For a claimed bound "no period-\(p\) oscillator has population \(\le N\)", the search is finite once a bounding box is fixed: any period-\(p\) oscillator with \(\mathrm{pop}\le N\) has \(\mathrm{box}\) bounded (a pattern that stays within a population budget cannot spread without light-cone growth over \(p\) steps), so

\[
\mathrm{minpop}(p)\le N \iff \exists\, O\ \text{in a } W(N,p)\times H(N,p)\ \text{box with } T^{p}O=O,\ \mathrm{pop}(O)\le N,
\]

and the right side is a single finite SAT/enumeration instance. The box function \(W,H\) must be justified (light-cone / no-escape argument) and recorded; an unjustified box silently weakens the lower bound.

**Gate (must be stated in every session).** Omniperiodicity is *settled*: existence of a period-\(p\) oscillator is open for no \(p\), and no session may claim novelty for merely exhibiting one. Novelty lives only in smallness, minimal population, or a certified structural constraint.

## 2. Resolution standard

Produce a **simulation-certified minimal oscillator (SCMO)** for a period \(p\): an explicit finite pattern \(O\) (RLE and `apgcode`), the stated period, and a deterministic transcript proving

\[
T^{p}(O)=O
\quad\text{and}\quad
T^{k}(O)\ne O\ \ (0<k<p),
\]

together with **one** of the following minimality artifacts.

- **Record form.** \(O\) has strictly smaller population (or bounding box, stated) than the standing record for period \(p\), with the record cited by value, source, and access date.
- **Optimality form.** A SAT / exhaustive certificate that no period-\(p\) oscillator of population \(\le N-1\) (resp. no oscillator inside a smaller box) exists, so \(O\) is provably minimal, i.e.

\[
\mathrm{pop}(O)=N \quad\text{and}\quad \bigl(\nexists\, O'\ \text{period } p,\ \mathrm{pop}(O')\le N-1\bigr),
\]

the second conjunct carrying a DRAT/LRAT UNSAT trace over the justified finite window.

A **constrained-variant** resolution is also acceptable: a certified smallest oscillator under a declared, decidable side constraint (non-trivial rotor of a given kind, phoenix / all-cells-die, statorless, or specified symmetry), with the constraint machine-checkable and the minimality artifact as above.

**Not accepted as resolution.**

- Any existence claim for a period, or any framing that treats omniperiodicity as still open.
- A pattern whose \(T^{p}(O)=O\) is asserted but not exhibited cell-for-cell, or whose true period is a proper divisor of the claimed \(p\).
- A "smaller" oscillator that is only smaller because inert padding was stripped inconsistently, or whose population/box convention differs from the cited record's.
- A minimality claim with neither a matching SAT/exhaustive lower bound nor a sourced record comparison.
- An oscillator built from a large engineered mechanism (Herschel/Snark loop, gun-based construction) presented as a *minimal* result - such objects certify existence, not smallness.
- Any result whose simulation or SAT proof cannot be re-run deterministically from the recorded seed and solver version.
- Floating-point/GPU evolution as the certifying step (exploration only).

## 3. Graded partial-result targets

- **P1 - Toolchain reproduction.** Re-derive the periods and populations of a panel of standard oscillators (blinker \(p2\), pulsar \(p3\), pentadecathlon \(p15\), Kok's galaxy, a queen-bee-shuttle-based \(p30\), and one high-period engineered example). *Certificate:* two-engine self-return transcripts with populations tabulated.
- **P2 - Record-table reproduction.** Reproduce the current smallest-known population and bounding box for a chosen band of periods, matching published records up to phase. *Certificate:* per-period SCMO transcripts plus a sourced record table with access dates.
- **P3 - New minimal-population or bounding-box record.** For some period \(p\), beat the standing population or box record with a verified oscillator. *Certificate:* SCMO transcript and sourced record comparison.
- **P4 - Certified optimality for a small period.** For a small \(p\), prove \(\mathrm{minpop}(p)\) (or \(\mathrm{minbox}(p)\)) exactly via SAT/exhaustive search. *Certificate:* the witness plus a DRAT/LRAT UNSAT trace (or exhaustive enumeration log) ruling out anything smaller.
- **P5 - Constrained-variant record.** A certified smallest oscillator under a declared constraint (statorless, phoenix, symmetry class, non-trivial rotor). *Certificate:* SCMO transcript, machine-checkable constraint predicate, and minimality artifact.
- **P6 - Frontier consolidation.** A reproducible, audited catalogue of minimal-known oscillators across a period range with canonical identifiers and hashes. *Certificate:* the catalogue, its generator, and an independent replay.

## 4. Known results and prior art

- **Omniperiodicity (the gate).** "Conway's Game of Life is Omniperiodic", by Nora Brown, Carson Cheng, Tanner Jacobi, Maia Karpovich, Matthias Merzenich, David Raucci, and Mitchell Riley, arXiv:2312.02799 (December 2023); the last two periods realised were 19 and 41 in July 2023. Enabling technology included David Buckingham's Herschel conduits (~1996) giving all \(p\ge 58\), and Mike Playle's `Snark` reflector (April 2013) giving all \(p\ge 43\) (verify the exact thresholds and dates).
- **Classical oscillators.** Blinker (\(p2\)), pulsar (\(p3\)), pentadecathlon (\(p15\)), figure-eight, Kok's galaxy, queen-bee shuttle and the derived \(p30\) - all early Life results (Conway et al. and the 1970s–80s community).
- **Minimal-population / smallest-known tables.** The LifeWiki maintains per-period smallest-known oscillators and minimal-population records; these have shifted repeatedly as new rotors and billiard-table configurations were found. Treat every entry as a live, re-verifiable record, not a settled value.
- **Variants.** Phoenixes (every live cell dies each step), statorless oscillators, and symmetry-constrained oscillators are studied separately with their own records (verify current holders).
- **Exhaustive/SAT minimality.** Small-box exhaustive enumeration and SAT-based minimality (in the spirit of the Garden-of-Eden and still-life work) have certified optimal small objects; extending this to per-period oscillator minimality is the natural target where the box is small enough (verify what is already certified).
- **Still-life precedent.** The exhaustive enumeration of small still-lifes and strict still-life counts (the \(p=1\) analogue) is a solved, fully certified template; the oscillator problem is its dynamic generalisation, and the same canonical-generation and SAT machinery transfers (verify the current strict-still-life enumeration frontier).
- **Population records for engineered periods.** Even where a period has a small oscillator, high-period *minimal-population* records are often held by non-obvious billiard-table or catalytic constructions rather than the first-found object; the smallest-known and the minimal-population holder for a period can differ.

Never cite a discoverer, date, record value, or period threshold you have not re-checked. Life records move fast - web-verify every claim. **Status as of mid-2026 - re-verify against the current literature and record trackers (LifeWiki, Catagolue, the ConwayLife forums) before starting any session, and re-confirm that omniperiodicity remains the settled backdrop.**

## 5. Attack plan

`[search]` - concrete first computations on one workstation.

1. **Verifier first.** Deterministic Life stepper plus a self-return check (\(T^{p}(O)=O\), least period), wrapped around `Golly` HashLife/QuickLife and `lifelib` as two independent engines. No record is claimed without both agreeing.
2. **SAT minimality.** Encode "period-\(p\) oscillator inside a \(W\times H\) box with population \(\le N\)" as SAT: one Boolean per cell per timestep, Life clauses linking successive layers, the wrap-to-self identity, and a cardinality bound,

\[
x^{(t+1)}=\mathrm{Life}(x^{(t)})\ (0\le t<p),
\qquad x^{(p)}=x^{(0)},
\qquad \textstyle\sum_{x} x^{(0)}\le N,
\]

using `LLS`-style encodings; solve with CaDiCaL/kissat; log DRAT for the UNSAT (no-smaller) direction. This is the engine for certified optimality (P4), strongest for small \(p\) and small boxes.
3. **Exhaustive small-box enumeration.** For the smallest boxes, enumerate seeds and simulate, canonicalising phases; feeds both records and lower bounds.
4. **Rotor/billiard-table search.** For mid-range periods, search catalytic / oscillating-rotor constructions and `apgsearch`/Catagolue soups for small period-\(p\) hits, then re-verify from scratch.
5. **Constrained encodings.** Add the variant predicate (statorless, phoenix, symmetry) directly to the SAT / enumeration model for P5.
6. **Box justification.** For every lower bound, derive and record the light-cone / no-escape bound \(W(N,p),H(N,p)\) that makes the search finite; an unjustified or too-small box invalidates the UNSAT. Cross-check the bound by re-running the SAT at one box larger and confirming it stays UNSAT.

One-workstation scope: SAT/exhaustive optimality is feasible only for small periods and boxes - state the window. Large engineered oscillators are out of scope as *minimal* results. **Failure modes:** SAT blow-up as box/period grow; mistaking a divisor period for \(p\); inconsistent population/box conventions versus the cited record; unverified DRAT; phase-canonicalisation bugs; soup-search hits that are not actually minimal.

## 6. Verification and auditability requirements

1. **Exact computation.** Every load-bearing claim rests on exact integer-lattice simulation or a checked SAT proof; floating-point/GPU is exploration only. Period, self-return, and minimality are asserted only after cell-exact confirmation.
2. **Independent verification.** Each SCMO is re-simulated in a second engine written separately from the search; each optimality (no-smaller) claim carries a DRAT/LRAT trace checked by a standalone checker (`drat-trim`/`lrat-check`) and, where feasible, a second solver.
3. **Reproducibility.** Seed pattern (RLE and `apgcode`), population/box convention, engine and solver versions, encodings, seeds, and box/period windows recorded; SHA-256 manifest over every artifact; each record being beaten is cited with source and access date.
4. **Preservation.** Search and encoding source, plus run logs, are part of the record; anything not preserved is stated explicitly.
5. **Honest reporting.** The report states up front that omniperiodicity is the settled backdrop, and whether the result is a strict record, a certified optimum, a constrained-variant record, or only a reproduction - in which measure (population vs bounding box). An existence claim, a mis-periodised pattern, or an unreplayable search is never represented as a certified minimal oscillator.
