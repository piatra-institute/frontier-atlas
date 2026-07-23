# PROMPT FOR A SIMULATION-CERTIFIED SPACESHIP OF AN OPEN OR RECORD VELOCITY

## The smallest Conway-Life spaceship of a given speed, and the still-unrealised velocities

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 31 of 50  
**Area:** discrete dynamics & pattern search  
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Conway's Game of Life is the outer-totalistic cellular automaton \(\mathrm{B3/S23}\) on \(\mathbb Z^2\). A *spaceship* is a finite pattern that returns to itself, translated, after a fixed number of steps; its velocity is the pair (displacement, period). Fifty-five years after the rule was published, the set of *achievable* velocities is only partly mapped, and for most achievable velocities the *smallest* spaceship is unknown. The frontier is concrete and machine-checkable: a candidate is settled by deterministically simulating one full period and confirming an exact rigid translation of the live-cell set. This matches AI search because the discovery loop is a bounded combinatorial search - row-by-row de Bruijn / breadth-first search as in `gfind`/`ntzfind`, or SAT over a fixed bounding box and period - closed by a trivial, independently re-runnable verifier. The on-machine verifier that closes the loop is a deterministic Life engine plus a translation-equality check. Anything short of the Section 2 standard - a partial, a puffer, an unverified velocity claim, an unreplayable search - is a partial result, never a solution.

## 1. Exact problem statement

**The rule.** A state is a function \(c:\mathbb Z^2\to\{0,1\}\) with finite support. Write \(n(c,x)=\sum_{y\in \mathcal N(x)} c(y)\) for the number of live cells in the eight-cell Moore neighbourhood \(\mathcal N(x)\) of \(x\). The Life transition \(T\) is

\[
(Tc)(x)=
\begin{cases}
1 & \text{if } c(x)=0 \text{ and } n(c,x)=3,\\
1 & \text{if } c(x)=1 \text{ and } n(c,x)\in\{2,3\},\\
0 & \text{otherwise,}
\end{cases}
\]

i.e. birth on 3, survival on 2 or 3. \(T\) is deterministic and commutes with every lattice translation \(\sigma_{(a,b)}\).

**Spaceship.** A finite nonempty pattern \(S\) is a **spaceship** of velocity \((dx,dy)c/p\) when

\[
T^{p}(S)=\sigma_{(dx,dy)}(S),\qquad (dx,dy)\ne(0,0),
\]

with \(p\ge1\) the least such period. Its \(p\) intermediate images \(S,T S,\dots,T^{p-1}S\) are the **phases**. The triple \((dx,dy,p)\) is reduced so that no smaller period gives the same displacement direction.

**Speed and velocity type.** The displacement per period classifies the ship:

\[
\text{orthogonal } (d,0)c/p,\qquad
\text{diagonal } (d,d)c/p,\qquad
\text{oblique } (dx,dy)c/p\ \text{with } 0<|dy|<|dx|.
\]

A **knightship** is the oblique case \((2,1)c/p\) (or a symmetric image). Conway's 1970 **speed limit** bounds every spaceship by the light cone:

\[
\frac{|dx|+|dy|}{p}\;\le\;\frac12,
\qquad\text{so orthogonal}\le c/2,\ \text{diagonal}\le c/4 .
\]

**Minimality measures.** For a fixed velocity, order spaceships by (i) live-cell population of the smallest phase, then (ii) bounding-box area of the smallest phase, then (iii) the minimum over phases; the chosen order must be stated. A ship is **elementary** if no strict sub-pattern is itself a spaceship of the same velocity and it cannot be partitioned into interacting smaller ships plus scaffold (working definition).

**The open question, two forms.**

- **(A) Existence.** Exhibit a spaceship of a velocity for which none is currently known (respecting the speed limit).
- **(B) Minimisation.** For a velocity already realised, exhibit a spaceship with strictly smaller population (or bounding box) than the current record.

Both are decided cell-exactly. Non-goals: puffers (leave debris), rakes (emit ships), and wickstretchers, except as sources of a genuine spaceship extracted and verified in isolation.

**What is known about achievability.** Two structural facts frame the search:

\[
\text{(constructive) all sufficiently slow velocities are realised by large engineered ships,}
\]
\[
\text{(hard) a small or } \textit{elementary}\ \text{ship of a given low velocity may be very difficult to find or absent.}
\]

The engineered constructions (adjustable caterpillars) certify a dense set of achievable velocities but produce enormous patterns; the open, valuable objects are the *small* ships. A velocity is treated as "open" here when no spaceship of it is recorded in the standard trackers, regardless of whether an engineered construction is believed possible in principle.

**Normalization.** Fix a canonical orientation by reflecting/rotating so that \(dx\ge dy\ge0\); report the ship in its lexicographically least phase under the eight dihedral images and translation to the first quadrant. This canonical form is what enters the `apgcode` and the record comparison, so two sessions cannot disagree on which object was found.

## 2. Resolution standard

Produce a **simulation-certified spaceship (SCS)**: an explicit finite pattern \(S\) (as RLE and as an `apgcode`), a stated velocity \((dx,dy)c/p\), and a deterministic simulation transcript establishing

\[
T^{p}(S)=\sigma_{(dx,dy)}(S)
\quad\text{and}\quad
T^{k}(S)\ne \sigma_{(dx',dy')}(S)\ \text{for all } 0<k<p,
\]

The reported measures are

\[
\mathrm{pop}(S)=\min_{0\le k<p}\bigl|\mathrm{supp}(T^{k}S)\bigr|,
\qquad
\mathrm{box}(S)=\min_{0\le k<p}\ \bigl(\text{area of bounding rectangle of } T^{k}S\bigr),
\]

both recorded, and the transcript replayable in two independent engines. For form (A) the velocity must have no prior known spaceship; for form (B) the reported measure must be strictly below the cited record for that velocity.

A **bounded-nonexistence certificate** resolves a sharper sub-question: a SAT/exhaustive proof (with a DRAT/LRAT trace where a SAT encoding is used) that *no* spaceship of velocity \((dx,dy)c/p\) fits in a bounding box of width \(\le W\) and height \(\le H\) - a certified statement about a finite window, never about all spaceships of that velocity.

**Not accepted as resolution.**

- A partial (an incomplete BFS/`gfind` front, a head-and-tail fragment) not closed into a genuinely periodic ship.
- A pattern that is actually a puffer, rake, or eventually-decaying object - anything where \(T^{p}(S)\) is not an exact rigid translate of \(S\).
- A velocity claim not backed by exhibiting the period-\(p\) translation cell-for-cell.
- A "smaller" ship that is only smaller in a non-minimal phase, or whose minimal phase was mis-measured, or that is a known ship in disguise.
- A minimality claim for population/bounding box asserted without either a matching exhaustive/SAT lower bound or an explicit, sourced comparison to the standing record.
- Any result whose simulation cannot be re-run deterministically from the recorded seed pattern and engine version.
- Floating-point or GPU-approximate evolution used as the certifying step (fine for exploration only).

## 3. Graded partial-result targets

Ordered milestones; each names the artifact that certifies it.

- **P1 - Toolchain reproduction.** Re-derive, in your own harness, the velocity of a panel of known ships: glider \(c/4\) diagonal; LWSS/MWSS/HWSS \(c/2\) orthogonal; `copperhead` \(c/10\) orthogonal; Sir Robin \((2,1)c/6\). *Certificate:* two-engine simulation transcripts confirming each translation and period, with populations tabulated.
- **P2 - Search reproduction.** Rediscover a known elementary ship of a chosen velocity from scratch with `gfind`/`ntzfind` or LLS, matching the published object up to phase/translation. *Certificate:* search configuration, run log, and an SCS transcript; equality to the known ship stated by canonical `apgcode`.
- **P3 - New minimal record (existing velocity).** For a realised velocity, find a spaceship with strictly smaller minimal-phase population or bounding box than the standing record. *Certificate:* SCS transcript plus a sourced record comparison (record value, source, access date).
- **P4 - First small/elementary representative.** For a velocity known only via large engineered constructions, exhibit a genuinely smaller or elementary ship. *Certificate:* SCS transcript and an argument or search that no known smaller object exists.
- **P5 - New velocity (existence).** Exhibit an SCS for a velocity with no previously known spaceship, respecting the speed limit. *Certificate:* SCS transcript in two engines; independent confirmation the velocity was previously unrealised.
- **P6 - Certified bounded nonexistence.** For a target velocity, prove by SAT/exhaustive search that no ship fits within a stated box and period window. *Certificate:* DRAT/LRAT UNSAT trace (or exhaustive enumeration log) with the exact encoding and window recorded.
- **P7 - New oblique family or second elementary knightship.** A new oblique velocity realised by a small ship, or a second elementary knightship distinct from Sir Robin. *Certificate:* SCS transcript plus a novelty audit against the ship database.

## 4. Known results and prior art

- **Speed limits.** Conway (1970): orthogonal ships \(\le c/2\), diagonal \(\le c/4\), light-cone bound \((|dx|+|dy|)/p\le 1/2\). Standard textbook result.
- **Classical small ships.** Glider (\(c/4\) diagonal) and the \(*\)WSS family LWSS/MWSS/HWSS (\(c/2\) orthogonal), all from the earliest Life work (Conway et al., ~1970).
- **Modern low-period ships.** `loafer` (\(c/7\) orthogonal, Josh Ball, 2013, verify); `copperhead` (\(c/10\) orthogonal, discoverer "zdr", 2016, verify); `Sir Robin`, the first elementary knightship \((2,1)c/6\), found by Adam P. Goucher, 6 March 2018, using `ikpx`, closing partials by Tomas Rokicki and Josh Ball (2017) (verify the partial attribution).
- **Engineered arbitrarily-slow ships.** `Caterpillar` (\(17c/45\), Gabriel Nivasch and collaborators, ~2004, verify) and the adjustable `Caterloopillar` (Michael Simkin, ~2016, verify) show all sufficiently slow velocities are achievable by construction; these are large, not minimal.
- **New-technology period families.** 2c/7 and 3c/7 orthogonal ships and higher-period \((2,1)c/6\) knightships (Dylan Chen, John Winston Garth, and others, 2020–2021, via `ikpx2`) (verify).
- **Search programs.** `gfind` (David Eppstein, ~2000); the `zfind`/`ntzfind` lineage (community, ~2010s); `WLS` (Winning Life Search); `ikpx`/`ikpx2` (Adam P. Goucher); `LLS` (Logic Life Search, SAT-based, Oscar Cunningham); `apgsearch`/`apgluxe` soup search (Goucher) as a serendipity source. Objects catalogued on the LifeWiki and Catagolue.
- **Open landscape.** Many low velocities (numerous orthogonal, diagonal, and nearly all oblique speeds) have no known small ship; the achievable-velocity set is not fully mapped below the speed limit.

Never cite a discoverer, date, or object name you have not re-checked; the identifiers above marked "(verify)" are precisely the ones to confirm. Life records move fast - web-verify every claim, discoverer, and record value. **Status as of mid-2026 - re-verify against the current literature and record trackers (LifeWiki, Catagolue, the ConwayLife forums) before starting any session.**

## 5. Attack plan

`[search]` - concrete first computations on one workstation.

1. **Verifier first.** Implement a deterministic Life stepper (bitboard/`lifelib`) and a translation-equality check; wrap `Golly`'s HashLife and QuickLife as a second, independent engine. Every candidate must pass both.
2. **Row-based search.** Run `gfind` and `ntzfind` for target velocities, sweeping search width and lookahead; these do breadth/depth-first search over partial spaceship rows via a de Bruijn graph. Expect the practical wall to be search *width* (memory and branching explode with width and period).
3. **SAT for short periods.** Use `LLS` to encode "spaceship of velocity \(v\) in a \(W\times H\) box with period \(p\)" as SAT; solve with CaDiCaL/kissat, logging DRAT for UNSAT windows (feeds P6). SAT is strongest for small boxes and short periods.
4. **Head/tail assembly.** For higher-period ships, use `ikpx2`-style iterated partial extension, then close and re-verify in the independent engines.
5. **Serendipity.** Mine `apgsearch`/Catagolue for unexpected ships at target speeds; treat any hit as a P1-style candidate to be re-verified from scratch.
6. **Extraction.** Where only a puffer/rake/wickstretcher is available for a velocity, attempt to isolate a self-contained ship: run the emitter, excise a single emitted object, and re-verify it in isolation as an SCS. An extraction counts only if the isolated pattern is itself periodic-with-translation.

One-workstation scope: `gfind`/`ntzfind` and `LLS` short-period runs are feasible; long high-period searches and wide widths are not - bound the window and report it. **Failure modes:** combinatorial blow-up in search width; partials that never close; mistaking a puffer/rake for a ship; engine disagreement from off-by-one phase or bounding-box handling; unverified solver output (always check the DRAT); mis-identifying the minimal phase.

## 6. Verification and auditability requirements

1. **Exact computation.** Every load-bearing claim rests on exact integer-lattice simulation or a checked SAT proof; floating-point/GPU evolution is exploration only. Period and translation are asserted only after cell-exact confirmation.
2. **Independent verification.** Each SCS is re-simulated in a second engine written separately from the search (`Golly` HashLife vs `lifelib` vs a custom stepper); each bounded-nonexistence claim carries a DRAT/LRAT trace checked by a standalone checker (`drat-trim`/`lrat-check`).
3. **Reproducibility.** Seed pattern (RLE and `apgcode`), engine names and versions, search program versions, flags, seeds, and box/period windows recorded; SHA-256 manifest over every artifact; each record being beaten is cited with source and access date so the claimed gain is unambiguous.
4. **Preservation.** Search source, configuration, and run logs are part of the record; anything not preserved is stated explicitly (the lost-source lesson from the sister programs).
5. **Honest reporting.** The report states up front whether an SCS of an open velocity, a strict record improvement, or only a bounded-nonexistence/reproduction result was obtained, and in which measure (population vs bounding box). A partial, a puffer, or an unreplayable search is never represented as a certified spaceship.
