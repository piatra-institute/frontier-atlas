# Research log and approach registry

## Target

Resolve the stationary-runner Lonely Runner Conjecture for all `k`, or provide an exact counterexample and a full symbolic nonexistence certificate.

## Normalizations audited

- Work on `R/Z` because integer-speed trajectories are 1-periodic.
- Replace signed speeds by absolute values; `||-x||=||x||`.
- A common gcd is removed by time rescaling.
- `k` relative speeds correspond to `k+1` total runners.
- The target boundary is inclusive: `>=1/(k+1)`.

## Approach family A: torus and interval covers

### Work performed

- Recast failure as a cover of the time circle by forbidden sets
  `B_i={t: ||v_i t||<1/(k+1)}`.
- Examined mean multiplicity, pair intersections, endpoint structure, and exact cell decompositions.

### Surviving fact

A concrete tuple is exactly decidable because the lower envelope is piecewise linear and a maximum occurs at a denominator `|v_i|+|v_j|`.

### Blocker

Measure and low-order moment bounds permit tight covers up to measure-zero boundary witnesses. They do not distinguish a tight tuple from a genuine counterexample at the required boundary.

## Approach family B: fixed rational grids and modular sieves

### Work performed

- Studied whether every non-tight primitive tuple must eventually have a witness on every sufficiently fine universal grid.
- Tested diagonal and congruence-preserving lifts symbolically.

### Result

This route produced the main theorem of the package: the proposed universal-grid conjecture is false for every `k>=2` and every sufficiently large denominator.

### Blocker for the original conjecture

The obstruction refutes the auxiliary grid mechanism, not the Lonely Runner inequality itself. The constructed tuples satisfy the original conjecture with strict slack.

## Approach family C: simultaneous Diophantine approximation

### Work performed

- Used the exact pair-sum critical-time characterization.
- Quantized the strictness margin for bounded integer speeds.
- Approximated an exact maximizing time by arbitrary rational grids.

### Result

For maximum speed `M`, every non-tight tuple has a witness on every grid of denominator at least `(k+1)M^2`.

### Blocker

The dependence on `M` cannot be removed. The main conjecture requires a uniform inequality, not merely a speed-dependent sampling theorem.

## Approach family D: induction with a slack parameter

### Work performed

- Deleted the fastest runner and used the stronger `1/k` threshold supplied by the `(k-1)`-speed conjecture.
- Quantified the interval around a prefix witness that remains safe at threshold `1/(k+1)`.

### Surviving lemma

If sorted speeds satisfy `v_k>k v_{k-1}` and LRC holds for `k-1`, then the `k`-tuple satisfies LRC. At the other extreme, `v_k<=k v_1` is immediate from time `1/(v_1+v_k)`.

### Blocker

No invariant was found that propagates through the medium-growth regime without becoming a shifted simultaneous-approximation statement as strong as, or false beyond, the original conjecture.

## Approach family E: Fourier analysis

### Work performed

- Considered products of safe-arc indicators, Fourier coefficients, positive-definite minorants, and second-moment cover constraints.

### Blocker

Known exact boundary examples have no open witness interval, so positivity-of-integral arguments cannot establish the inclusive boundary without a separate rigidity theorem. Current general Fourier bounds remain below the target.

## Approach family F: additive combinatorics and residue covers

### Work performed

- Recast a missing `1/p`-grid witness as a cover of `F_p` by multiplicative dilates of a short symmetric interval.
- Examined incidence counts and canonical covers associated with `(1,2,...,k)`.

### Blocker

A classification or stability theorem for all such multiplicative interval covers is missing. The canonical cover can be lifted to non-tight continuous tuples without changing its residue data, as shown by the congruence-blind lifting lemma.

## Approach family G: exact computation

### Work performed

- Implemented exact rational evaluation of concrete tuples.
- Checked the complete critical-time set, not a floating-point time mesh.
- Produced two independent `k=13` obstruction certificates.

### Blocker

No bounded computation performed here came with a uniform all-input bound sufficient to resolve `k=13`, much less all `k`. Exploratory absence of counterexamples was therefore excluded from the proof claims.

## Strongest verified conclusions

1. The proposed universal denominator for all primitive non-tight tuples does not exist.
2. The failure persists for arbitrarily large prime denominators even when each speed is individually coprime to the denominator.
3. The exact continuous maximum of a concrete integer tuple occurs at a pair-sum denominator.
4. A corrected grid theorem holds with denominator at least `(k+1)M^2`.
5. The original all-`k` Lonely Runner Conjecture remains the exact unresolved gap.
