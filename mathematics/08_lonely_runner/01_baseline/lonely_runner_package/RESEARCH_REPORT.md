# Lonely Runner Conjecture
## Audited research report and exact obstruction to a proposed universal-grid extension

**Piatra Institute research artifact**  
**Status date:** 22 July 2026  
**Arithmetic:** exact rational arithmetic throughout

## 1. Verdict

The main Lonely Runner Conjecture was **not completely resolved** in this investigation. I found neither:

1. a proof valid for every number of runners; nor
2. an exact speed tuple that violates the conjecture.

Accordingly, this report does not claim a solution. It records the strongest result that survived exact checking and adversarial review:

> **The universal-denominator conjecture proposed as Conjecture 7.1 in Sungkawichai and Trakulthongchai (2026) is false as written, and fails in two robust ways.**

The report also gives:

- a complete symbolic proof of that statement;
- an exact critical-time lemma for concrete speed tuples;
- a corrected quantitative grid theorem;
- two machine-checkable certificates in the first currently unverified dimension, `k=13` relative speeds;
- exact Python verification code using only the standard library;
- the precise remaining gap to a complete resolution of the Lonely Runner Conjecture.

This is a rigorous correction to a proposed extension mechanism, but it is **not** a resolution of the original conjecture. I did not locate this specific obstruction in targeted public searches; that is not a certification of literature priority, and this report makes no novelty claim beyond the derivations it contains.

## 2. Problem and conventions

For a real number `x`, write `||x||` for its distance to the nearest integer. For a tuple of `k` nonzero integer relative speeds

`v = (v_1,...,v_k)`,  

set

`F_v(t) = min_i ||t v_i||`,  
`kappa(v) = max_{t in R/Z} F_v(t)`.

The stationary-runner form of the Lonely Runner Conjecture is

`kappa(v) >= 1/(k+1)`

for every admissible tuple. The threshold uses `k+1` because `k` nonzero relative speeds arise after fixing one runner among `k+1` total runners.

Negative speeds cause no change because `||-x||=||x||`. A common greatest common divisor causes no change after rescaling time. If two signed speeds have the same absolute value, they impose the same constraint; deleting the duplicate only strengthens the threshold available from the lower-dimensional conjecture.

As of 22 July 2026, the strongest publicly available verification proves the conjecture for `k <= 12`, corresponding to at most 13 total runners. The first unverified stationary case is `k=13`, or 14 total runners.

## 3. The proposed universal-grid conjecture

Sungkawichai and Trakulthongchai define a positive integer speed tuple to be **tight** when the strict inequalities

`||t v_i|| > 1/(k+1)` for every `i`

cannot hold simultaneously. Their Conjecture 7.1 states, in substance:

> For each fixed `k`, there is a constant `D` such that, for every integer `d >= D`, every coprime non-tight positive integer `k`-tuple has a witness in `(1/d)Z`.

The following theorem disproves this statement for every `k >= 2`. The tuple is allowed to depend on `d`: the conjecture quantifies over **every** non-tight coprime tuple after fixing the denominator, so one counterexample tuple for each large `d` is decisive.

## 4. Main theorem established here: failure for every sufficiently large denominator

### Theorem 4.1 - diagonal grid obstruction

Fix an integer `k >= 2`, put `q=k+1`, and let

`C_k = k(k+1)(k-1)/2`.

For every integer `d > C_k`, the tuple

`V_{k,d} = (1,2,...,k-1,d)`

has all of the following properties:

1. its entries are positive and distinct;
2. `gcd(V_{k,d})=1`;
3. it is non-tight, in fact `kappa(V_{k,d}) > 1/q`;
4. it has no witness in `(1/d)Z`.

Consequently, no constant `D` of the form proposed in Conjecture 7.1 can exist.

### Proof

The first two statements are immediate because the tuple contains `1` and `d>k-1`.

For the grid obstruction, take any grid time `t=a/d`. The last coordinate satisfies

`||d t|| = ||a|| = 0 < 1/q`.

Therefore no point of `(1/d)Z` is a witness.

It remains to prove that the tuple is nevertheless non-tight. At

`t_0=1/k`,

for every `i=1,...,k-1`,

`||i t_0|| = min(i/k,1-i/k) >= 1/k`.

The margin above the target threshold is

`1/k - 1/(k+1) = 1/[k(k+1)]`.

Choose a midpoint of a `d`-grid cell,

`t_*=(2m+1)/(2d)`,

nearest to `1/k`. Such a midpoint satisfies

`|t_*-1/k| <= 1/(2d)`.

The distance-to-nearest-integer function is 1-Lipschitz, hence for `1<=i<=k-1`,

`||i t_*|| >= ||i/k|| - i|t_*-1/k|`

`>= 1/k - (k-1)/(2d)`.

Because `d>C_k`,

`1/k - (k-1)/(2d) > 1/(k+1)`.

For the last speed,

`||d t_*|| = ||(2m+1)/2|| = 1/2 > 1/(k+1)`.

Thus every inequality is strict at `t_*`, so `V_{k,d}` is non-tight. This completes the proof. `□`

### Quantitative form

The proof gives the explicit lower bound

`kappa(V_{k,d}) >= 1/k - (k-1)/(2d) > 1/(k+1)`.

For the concrete `k=13, d=2000` certificate supplied with this report, the stronger identity

`kappa(1,2,...,12,2000)=1/13`

also has a short symbolic proof. The prefix `(1,...,12)` has maximum loneliness `1/13` by Lemma 5.1, so adjoining another coordinate cannot increase the maximum. At `t=1/13`, the added speed is congruent to `11 mod 13`, and every coordinate has distance at least `1/13`; hence equality holds. There are no witnesses on the `1/2000` grid, although the required threshold is only `1/14`.

## 5. Robust failure even when every speed is a unit modulo the grid denominator

A natural attempted repair is to prohibit speeds divisible by the grid denominator. That does not repair the conjecture.

### Lemma 5.1 - exact witnesses for the canonical tight tuple

For `q=k+1`,

`min_{1<=i<=k} ||i t|| >= 1/q`

holds if and only if

`t = s/q mod 1`

for some `s` with `gcd(s,q)=1`.

### Proof

Consider the `q` points

`0,t,2t,...,kt` in `R/Z`.

The distance between any two is `||(i-j)t||`, where `1<=|i-j|<=k`; by hypothesis every pair is separated by at least `1/q`. The `q` cyclic gaps between the sorted points therefore each have length at least `1/q`. Their lengths sum to `1`, so every gap is exactly `1/q`. The points form a regular `q`-gon. Hence `t=s/q mod 1`; the points are distinct precisely when `gcd(s,q)=1`. The converse follows immediately from the nonzero residues modulo `q`. `□`

### Theorem 5.2 - congruence-class obstruction

Fix `k>=2` and put `q=k+1`. For every sufficiently large integer `d` coprime to `q`, the tuple

`W_{k,d}=(1,2,...,k-1,d+k)`

is coprime and non-tight but has no witness in `(1/d)Z`.

If `d>k` is prime, every individual speed in `W_{k,d}` is coprime to `d`.

### Proof

At every grid time `t=a/d`, the tuple is congruent modulo `d` to `(1,2,...,k)`, because

`(d+k)a/d = a + ka/d`.

Thus a grid witness for `W_{k,d}` would also be a grid witness for `(1,...,k)`. By Lemma 5.1 it would have to satisfy

`a/d=s/q mod 1`

with `gcd(s,q)=1`. Since `gcd(d,q)=1`, no nonzero such time belongs to both grids. Therefore no grid witness exists.

Non-tightness follows from exactly the midpoint argument in Theorem 4.1, now using the last speed `d+k`; it is enough that

`d+k > C_k`.

If `d>k` is prime, the residues `1,...,k` are all nonzero modulo `d`, so every speed is individually coprime to `d`. `□`

For the supplied robust certificate,

`k=13`, `d=2003`, `W=(1,2,...,12,2016)`.

Here `2003` is prime and every speed is coprime to `2003`. Moreover, `2016` is congruent to `1` modulo `13`, so the same prefix upper bound and the witness `t=1/13` prove symbolically that the exact maximum loneliness is `1/13`. The `1/2003` grid contains no witness.

## 6. Why the failure is structural

The fixed grid sees only the residue class of each speed modulo its denominator. A high-frequency lift can preserve all grid data while changing the continuous-time geometry from tight to non-tight.

### Lemma 6.1 - congruence-blind lifting

Fix a threshold `alpha<1/2`, a denominator `d`, and a tuple `A=(a_1,...,a_k)` having no witness on the `1/d` grid. Suppose that, after deleting coordinate `j`, there is an open interval `I` on which every remaining coordinate is strictly above `alpha`.

Replace `a_j` by

`a_j+m d`.

For all sufficiently large positive integers `m`, the new tuple:

1. has exactly the same behavior as `A` on the `1/d` grid;
2. has a strict continuous-time witness in `I`.

### Proof

Grid behavior is unchanged because the replacement is congruent to `a_j` modulo `d`.

For frequency `w=a_j+md`, the bad set `||w t||<=alpha` is a union of intervals, each of length `2alpha/w`. Once `w` is large enough that `2alpha/w<|I|`, the whole interval `I` cannot be contained in one bad component. Hence some `t in I` satisfies `||w t||>alpha`; the other coordinates were already strict throughout `I`. `□`

This lemma explains why a denominator independent of the tuple cannot distinguish tight residue data from non-tight high-frequency lifts.

## 7. Exact critical-time lemma

The checker uses the following finite characterization.

### Lemma 7.1 - a maximum occurs at a pair-sum denominator

Let `v_1,...,v_k` be nonzero integers and

`F(t)=min_i ||v_i t||`.

There is a maximizing time of the form

`t=a/(|v_i|+|v_j|)`

for some indices `i,j`, allowing `i=j`, and some integer `a`.

### Proof

Each function `||v_i t||` is a triangular wave: continuous and piecewise affine with slopes `+|v_i|` and `-|v_i|`. Hence `F`, the lower envelope, is continuous and piecewise affine.

Choose a maximizer at an endpoint if the maximizing set contains an interval. If an active triangular wave has a breakpoint there, its denominator divides `2|v_i|=|v_i|+|v_i|`.

Otherwise, at a local maximum of the lower envelope, active affine branches of both slope signs must meet. Equality between a branch of slope `+|v_i|` and one of slope `-|v_j|` gives

`(|v_i|+|v_j|)t` equal to an integer.

This proves the claim. `□`

### Corollary 7.2 - exact rationality and slack quantization

Let `M=max_i |v_i|`, `q=k+1`, and suppose

`kappa(v)>1/q`.

Then for some `N<=2M`,

`kappa(v)=m/N`

with integer `m`, and therefore

`kappa(v)-1/q >= 1/(qN) >= 1/(2qM)`.

This gives a completely explicit separation between a non-tight integer tuple and the boundary once its speed scale is fixed.

## 8. Corrected quantitative grid theorem

The failed conjecture becomes true after the denominator is allowed to depend on the speed scale.

### Theorem 8.1 - speed-bounded universal grid

Let `v` be a non-tight integer `k`-tuple, let `M=max_i |v_i|`, and put `q=k+1`. Then every integer grid denominator

`d >= q M^2`

contains a witness for `v`.

More sharply, if a maximizing time in Lemma 7.1 has denominator `N`, then

`d >= q M N/2`

is sufficient.

### Proof

Take a maximizing time `t_0=a/N`. By Corollary 7.2,

`kappa(v)-1/q >= 1/(qN)`.

Choose `b/d` within circular distance `1/(2d)` of `t_0`. Every function `||v_i t||` is `|v_i|`-Lipschitz, so their minimum is `M`-Lipschitz. Therefore

`F(b/d) >= kappa(v)-M/(2d)`.

If `d>=qMN/2`, then `M/(2d)<=1/(qN)`, and hence `F(b/d)>=1/q`. Since `N<=2M`, the simpler condition `d>=qM^2` suffices. `□`

### Near-necessity of speed dependence

Theorem 4.1 has maximum speed `M=d` and no witness on the `1/d` grid. Thus no denominator threshold independent of `M` can work, and even a general sublinear-in-`M` threshold is impossible. The exact optimal growth rate between the linear obstruction and the quadratic upper bound remains open.

## 9. Audited routes toward the main conjecture

The following routes were pursued or checked. None produced a complete all-`k` proof or an exact counterexample.

### 9.1 Fixed universal grids

**Outcome:** blocked decisively by Theorems 4.1 and 5.2.

A fixed denominator cannot see high-frequency changes by multiples of that denominator. This is not a numerical issue; it is an exact congruence obstruction.

### 9.2 Exact finite critical times

**Outcome:** valid and implemented, but tuple-dependent.

Lemma 7.1 makes every concrete tuple exactly decidable. It does not provide a bound independent of the input speeds or of `k`, so it does not by itself meet the complete-resolution standard.

### 9.3 Prefix induction with slack

Assuming the conjecture for `k-1` speeds, if the sorted tuple satisfies

`v_k > k v_{k-1}`,

a witness for the first `k-1` speeds at threshold `1/k` gives an interval on which they remain above `1/(k+1)`; the last runner oscillates fast enough that its safe set intersects that interval. This is a valid lacunary induction step, but it leaves the medium-growth regime.

At the opposite extreme, if

`v_k <= k v_1`,

then `t=1/(v_1+v_k)` is already a witness. The unresolved regime lies between these easy geometric extremes and includes highly structured tuples.

### 9.4 Shifted or phase-perturbed induction

**Outcome:** unsafe as a general mechanism.

Perturbing a rational base time turns the remaining constraints into shifted simultaneous approximation conditions. The shifted Lonely Runner Conjecture is not equivalent to the ordinary conjecture and now has explicit counterexamples, so a proof step that silently invokes the shifted statement is circular or false.

### 9.5 Fourier and measure arguments

**Outcome:** rigorous lower bounds remain below the target.

The best current asymptotic Riesz-product bound has the form `1/(2k)+1/k^(5/3+o(1))`; the target `1/(k+1)` is asymptotically `1/k`, so a factor-two leading-order gap remains. For a tight tuple the strict-witness set is empty, so a positive-measure argument cannot by itself establish the inclusive boundary equality.

### 9.6 Bounded computation in the first unknown case

Exploratory exact and mixed-integer searches did not produce a `k=13` counterexample in the bounded regions tested. Such a non-result is not evidence of the conjecture and is not used in any theorem in this report. A bounded search without a proved complete bound cannot meet the prompt's resolution standard.

## 10. Exact remaining gap

A complete solution still requires exactly one of the following:

1. a uniform proof that `kappa(v)>=1/(k+1)` for every `k` and every admissible tuple; or
2. a finite exact tuple with `kappa(v)<1/(k+1)`, together with a symbolic full-circle forbidden-interval cover.

The results above do neither. They establish that one proposed route to a uniform proof is impossible as stated and replace it with a correct speed-dependent theorem.

## 11. Stationary and moving-runner translation

Given `k+1` runners with distinct speeds `w_0,...,w_k`, fix runner `r` and subtract its speed. The `k` relative speeds

`u_i=w_i-w_r`, `i != r`,

are distinct and nonzero. A stationary-form witness satisfies

`||t(w_i-w_r)|| >= 1/(k+1)`

for every other runner, exactly saying that runner `r` is lonely at time `t`. Applying the stationary theorem separately for each choice of `r` gives the usual statement that every runner is lonely at some possibly different time.

Conversely, append a stationary runner of speed `0` to any stationary-form tuple. The boundary is preserved exactly because the conjecture uses `>=`, not `>`.

## 12. Reproduction

The package contains:

- `lrc_exact.py`: exact checker and critical-time evaluator;
- `lrc_grid_obstruction_certificate.json`: two exact `k=13` certificates;
- `verify_certificate.py`: independent command-line wrapper;
- `RESEARCH_LOG.md`: approach registry and blockers;
- `SHA256SUMS`: integrity hashes.

Run:

```bash
python lrc_exact.py --self-test
python verify_certificate.py lrc_grid_obstruction_certificate.json
```

To reproduce the exact diagonal example:

```bash
python lrc_exact.py \
  --speeds 1 2 3 4 5 6 7 8 9 10 11 12 2000 \
  --grid 2000 --maximum
```

To reproduce the unit-modulo-grid example:

```bash
python lrc_exact.py \
  --speeds 1 2 3 4 5 6 7 8 9 10 11 12 2016 \
  --grid 2003 --maximum
```

Expected in both examples:

- threshold `1/14`;
- grid witness count `0`;
- exact maximum loneliness `1/13`.

## 13. References

1. T. Sungkawichai and T. Trakulthongchai, *Eleven, twelve, and thirteen lonely runners*, arXiv:2604.23906, 2026.
2. R. D. Malikiosis, F. Santos, and M. Schymura, *Linearly-exponential checking is enough for the Lonely Runner Conjecture and some of its variants*, arXiv:2411.06903, revised 2025.
3. V. Giri and N. Kravitz, *The structure of Lonely Runner spectra*, Mathematical Proceedings of the Cambridge Philosophical Society 180 (2026), 343-361.
4. B. Bedert, *Riesz products and the Lonely Runner Conjecture: A wider gap of loneliness*, arXiv:2511.16636, 2025.
5. M. Blanco, F. Criado, and F. Santos, *Coloopless and cosimple zonotopes, and the Lonely Runner Conjectures*, arXiv:2603.24784, 2026.
6. G. Perarnau and O. Serra, *The Lonely Runner Conjecture turns 60*, arXiv:2409.20160, 2024.

## 14. Final takeaway

The original Lonely Runner Conjecture remains open beyond 13 total runners. The main rigorously verified advance here is that the 2026 universal-denominator proposal is false in every dimension `k>=2`, including under the natural repair that all speeds be coprime to a prime grid denominator. The correct replacement must depend on the tuple's speed scale or an equivalent quantitative compactness parameter; `d >= (k+1)M^2` is one explicit sufficient bound.
