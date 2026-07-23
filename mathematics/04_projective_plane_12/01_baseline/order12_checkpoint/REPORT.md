# Order-12 projective plane: exact deductions and remaining gap

**Research checkpoint, 21 July 2026**

## 1. Result

A complete resolution was not obtained. The supplied standard requires either a full 157 x 157 incidence structure or an exhaustive, independently checkable nonexistence proof. This package contains neither, so it must not be represented as a solution.

What follows is a conditional theorem: every projective plane of order 12 would have to satisfy a sharply constrained ternary coding-theory structure. The derivation does not assume any nontrivial automorphism.

## 2. Incidence matrix and affine reduction

Let `N` be the 157 x 157 binary line-by-point incidence matrix. The projective-plane axioms are equivalent to

`N 1 = 13 1`, `N^T 1 = 13 1`, and `N N^T = 12 I + J`.

Since the right-hand side is nonsingular, `N` is nonsingular. The same identities imply `N^T N = 12 I + J`.

Deleting a line and its 13 points leaves an affine plane of order 12. Equivalently, existence is the same as existence of an orthogonal array `OA(144,13,12,2)`, or a complete set of 11 mutually orthogonal Latin squares of order 12. This is exact but does not reduce the intrinsic difficulty.

## 3. Determinant, inverse, and Smith constraints

The eigenvalues of `12 I + J` are 169 once and 12 with multiplicity 156. Hence

`det(N)^2 = 169*12^156`, so `|det N| = 13*12^78`.

Using `(12I+J)^{-1}` and the row/column sums gives

`N^{-1} = (13 N^T - J)/156`.

Equivalently,

`N(13N^T-J)=(13N^T-J)N=156I`.

Therefore every invariant factor in the Smith normal form of `N` divides 156. Since

`|det N| = 2^156 * 3^78 * 13`,

exactly 78 Smith factors are divisible by 3 and exactly one is divisible by 13. Thus

`rank_F3(N)=79`, `rank_F13(N)=156`.

If `r=rank_F2(N)`, the multiplicities of 2-adic valuations 0, 1, and 2 among the Smith factors are

`r`, `158-2r`, and `r-1`, respectively, so `1 <= r <= 79`.

## 4. The ternary incidence code

Work over `F_3`. Let `r_i` be the incidence vector of line `i`, and let

`C = span{r_i}`.

The rank calculation gives `dim C=79`. Every two rows, including a row with itself, have inner product 1 modulo 3. For `c in C`, define

`s(c) = sum of its 157 coordinates in F_3`.

Then every line has the same scalar product with `c`:

`r_i . c = s(c)` for all `i`.

Let

`D = span{r_i-r_j}`.

The differences span the kernel of `s` on `C`, so `dim D=78`. They are orthogonal to every row. Hence

`D = C^perp`, and `C = D direct-sum <r_0>`.

Also

`wt(c) = c.c = s(c)^2 (mod 3)`.

Consequently, words of `D` have weights divisible by 3, while words in the two nonzero cosets `C\D` have weights congruent to 1 modulo 3.

## 5. Minimum words in C

Take `c in C\D`. Since every line sum is the nonzero value `s(c)`, every line meets the support of `c`. Thus the support is a blocking set.

A blocking set has at least 13 points: choose a point outside it; the 13 lines through that point must each contain a support point. If equality holds, any line through two support points must consist entirely of support points, so the support is a line.

Therefore `wt(c)>=13`. At weight 13, the support is a line `L`. Every other line meets `L` once, and its line sum forces the coefficient at that intersection to equal `s(c)`. Thus `c` is exactly `+1_L` or `-1_L`.

Hence:

- `C` is a ternary `[157,79,13]` code;
- its 314 words of weight 13 are exactly the two signed vectors of each of 157 lines.

## 6. The dual code has no word below weight 18

Let `0 != d in D`, with support `S`. Every line sum is zero. At any `P in S`, each of the 13 lines through `P` must contain another support point. Since distinct points of `S\{P}` lie on distinct lines through `P`, `|S|-1>=13`. Thus `|S|>=14`; divisibility by 3 improves this to `|S|>=15`.

Suppose `|S|=15`. At each support point, the other 14 support points are distributed among 13 lines with no empty part. Therefore exactly one line through the point is a trisecant of `S`, and the other 12 are bisecants. The five trisecants partition `S` into five triples.

On a bisecant, the two nonzero ternary symbols must be opposite. On a trisecant, the three symbols must be equal. Choose one point from each of three distinct triples. Their three joining lines are bisecants, so the three selected symbols would have to be pairwise opposite. Three nonzero elements of `F_3` cannot be pairwise opposite. Contradiction.

Therefore

`D=C^perp` has parameters `[157,78,d]` with `d>=18`.

The script `line_distribution.py` gives an independent integer-equation verification that weight 15 has no possible line-type distribution.

## 7. Exact structure at weight 18

Suppose `d in D` has weight 18. Write `A` for the points carrying `+1` and `B` for those carrying `-1`, with sizes `a,b`.

Let `n_{ij}` count lines containing `i` points of `A` and `j` points of `B`. Orthogonality gives `i-j=0 mod 3`. Counting lines, point-line incidences, pairs inside `A`, pairs inside `B`, and cross pairs gives:

- `sum n_ij = 157`;
- `sum i n_ij = 13a`, `sum j n_ij = 13b`;
- `sum C(i,2)n_ij = C(a,2)`;
- `sum C(j,2)n_ij = C(b,2)`;
- `sum i j n_ij = ab`.

Exact integer enumeration has one solution:

`a=b=9`, and

`n_00=52`, `n_30=12`, `n_11=81`, `n_03=12`.

Thus the 12 triples on `A` form a `2-(9,3,1)` design, as do the 12 triples on `B`. The unique such design is `STS(9)=AG(2,3)`.

For an outside point `x`, let `alpha_x` and `beta_x` count the `A`-triples and `B`-triples through `x`. Counting the 9 points of each sign on the 13 lines through `x` gives `alpha_x=beta_x in {0,1,2,3}`. If `x_t` is the number of outside points with this value `t`, then for some integer `u` with `0<=u<=4`,

`(x_0,x_1,x_2,x_3)=(31-u,96+3u,12-3u,u)`.

A further incidence argument sharpens this. Each `AG(2,3)` has four parallel classes of three triples. A class is either concurrent in the ambient plane, or its three pairs meet at three distinct outside points. A nonconcurrent class has three pair-intersection points, and these must correspond to three distinct nonconcurrent classes on the opposite sign side. Hence the number of nonconcurrent classes is either 0 or at least 3. Therefore

`u in {0,1,4}`.

This is a strong local normal form, but no contradiction is currently derived from any of the three cases.

## 8. A forced ternary self-dual code of length 160

For each line row `r_i`, define

`b_i=(r_i,1,1,0) in F_3^160`,

and define

`z=(0^157,1,-1,1)`.

All `b_i` are mutually orthogonal, and each is orthogonal to `z`; also `z.z=0`. The span of the `b_i` has dimension 79, and adjoining `z` gives a self-orthogonal dimension-80 code. It is therefore self-dual. Explicitly,

`E = {(u,s+c,s-c,c): u in C, s=s(u), c in F_3}`.

Every word has weight divisible by 3, so `E` is Type III. From the minimum-weight results above:

- only `+z` and `-z` have weight 3;
- there are no words of weights 6, 9, or 12;
- each of the 314 signed line words of `C`, combined with any of three values of `c`, gives weight 15;
- no other source of weight 15 exists.

Thus `E` must be a ternary Type-III self-dual `[160,80]` code with

`A_3=2`, `A_6=A_9=A_12=0`, and `A_15=942`.

## 9. Adversarial checks that did not yield a contradiction

### 9.1 Ordinary Gleason enumeration

For a Type-III self-dual code of length 160, the Hamming weight enumerator lies in the span

`sum_{j=0}^{13} a_j f^(40-3j) g^j`,

where `f=x^4+8xy^3` and `g=y^3(x^3-y^3)^3`.

Imposing the forced coefficients through weight 15, and even setting all coefficients at weights 18 through 39 to zero, produces a formal polynomial with nonnegative integer coefficients summing to `3^80`. Therefore the ordinary one-variable Gleason theorem alone cannot exclude `E`. `verify_gleason.py` checks this exactly.

### 9.2 MacWilliams linear constraints

Let `A_j` be the weight distribution of `D`, and `B_i` that of `C=D^perp`. The proven structure imposes:

- `A_0=1`, `A_j=0` unless `j=0` or `j>=18` and `3|j`;
- `B_i=A_i` for `3|i`;
- `B_i=0` for `i=2 mod 3`;
- `B_1=B_4=B_7=B_10=0`, `B_13=314`;
- all coefficients are nonnegative;
- the MacWilliams transform holds exactly.

This rational linear system is feasible. The certificate in `certificates/macwilliams_rational_feasible.json` is checked with exact fractions by `verify_macwilliams_rational.py`. Therefore no floating-point solver report of infeasibility is trustworthy here. The certificate is not integral and does not construct a code.

## 10. Exact remaining gap

A complete resolution still requires one of:

1. construct and verify a 157 x 157 binary matrix satisfying all projective-plane identities; or
2. prove that every possible matrix is impossible, including the trivial-automorphism branch, with a complete conceptual proof or an exhaustive proof certificate.

Within the coding route developed here, a sufficient next breakthrough would be an obstruction to every ternary `[157,78,>=18]` self-orthogonal code `D` whose dual contains exactly the 314 signed blocks of a `2-(157,13,1)` design as its weight-13 words. Ordinary Hamming weight enumerators are too weak. Promising stronger objects are complete or genus-2 weight enumerators, exact classification of the weight-18 `AG(2,3)` pair configurations, or a canonical augmentation that uses the ternary code as an isomorph-rejection invariant.
