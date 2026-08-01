# Sparse ruler beating the best known at a spanning length

**Find.** A spanning ruler (a set of marks 0 = a_0 < ... < a_k = L whose pairwise differences cover every integer in [1, L]) with fewer marks than the best published construction, at a length L beyond the exhaustively verified range.

**What counts as a win (one-sided).** One mark set that spans [1, L] using k marks, where k is below the best known count for that L. A single shorter ruler beats the record; failure proves nothing.

**Checker (seconds).** Compute the multiset of pairwise differences, assert {1,...,L} is a subset. O(k^2). Confirm mark count and span exactly.

**Search plan.** Start from Wichmann-type parametric rulers (the standard near-optimal family), then perturb: remove a mark and refill by local search / ILP; SAT/CP with covering constraints "each distance d in [1,L] is realized"; meet-in-the-middle over half-rulers. Target lengths just past the exhaustively certified frontier where only Wichmann-type constructions are known.

**Prior art (verify).** Optimal sparse (minimal-mark spanning) rulers are known by exhaustive search only up to moderate L; beyond that the best constructions are Wichmann-type and their optimality is conjectural (the bounded-excess question is open). See Leech, Wichmann, Peter Luschny's perfect/optimal ruler tables, OEIS A046693 / A103294. Open beyond the certified range (verify).
