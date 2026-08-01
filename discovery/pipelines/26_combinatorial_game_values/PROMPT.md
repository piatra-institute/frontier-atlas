# Batch sweep: refute Grundy-value pattern conjectures for heap games

**Mode:** one ChatGPT Pro session, code sandbox, batch throughput.
**Goal:** either a specific index where a claimed period of a game's Grundy sequence first breaks (a clean refutation), or a new window-certified period, or a certified long extension. (No finite data can prove non-periodicity; that limit is stated up front.)

**Family + panel.** Subtraction games with subtraction set S, and octal games with code .d1 d2 … ; the object is the single-heap Grundy sequence G(0),G(1),… under the mex/XOR recurrence, and its eventual arithmetic periodicity (period p, preperiod t, saltus s). Panel: value spectrum, largest value, candidate (p,t,s).

**Enumerate / generate.** Sweep many games: all subtraction sets S ⊆ {1,…,k} for small k, and all one/two-digit octal codes. For each, compute G to a large index. Sanity-check reference games: Nim = .333… (G(n)=n), Dawson's chess = .137 (period 34). If these do not reproduce, the engine is wrong.

**Conjecture generation.** The backdrop is the Guy conjecture that every finite octal game is eventually arithmetic-periodic (Winning Ways). For each game, detect a candidate period from the data, then test it against the Guy-Smith finite window t ≤ n ≤ 2p+t+d. Also test any folklore/published period for these games by re-deriving it.

**Adversarial refutation.** A claimed period is refuted by exhibiting the first index where G(n+p) ≠ G(n)+s within or beyond the window — historically, plausible periods break after long runs, so extend well past the observed prefix.

**Checker (exact).** Recompute G(n) exactly by mex of option XOR-values (integers, no float); certify a period only via the full Guy-Smith window, not the observed prefix.

**Verification discipline.** Generator is not verifier: two independent Grundy engines must agree bit-for-bit; a third routine checks the window; cross-check small games against cgsuite. Report per game: certified period / first period-break index / certified extent N; and the denominator of games swept.
