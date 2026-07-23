# Dimension 11 kissing number: verified result and remaining gap

**Status date:** 22 July 2026

## 1. Final status against the prompt

The requested complete resolution was **not obtained**. The exact value of `tau_11` remains undetermined. The package verifies the lower endpoint `604` but contains no unrestricted upper-bound certificate meeting it.

| Prompt requirement | Status |
|---|---:|
| Exact 604-point construction in `R^11` | PASS |
| Exact norms and all pairwise inner products | PASS |
| Positive semidefiniteness / rank at most 11 | PASS, rank exactly 11 |
| Exact proof that the fixed 604-code cannot be augmented | PASS |
| Universal proof excluding every 605-point code | NOT OBTAINED |
| Exact value of `tau_11` | UNRESOLVED |

The strongest verified theorem obtained here is substantially stronger than merely checking the lower-bound coordinates, but it is still logically local to one construction.

## 2. Exact 604-point construction

Work in the norm-2 convention: all code vectors have squared norm 4 and the kissing constraint is `<v,w> <= 2`. Divide by 2 to obtain the usual unit-vector convention.

Let

- `P0={0,6}`, `P1={1,4}`, `P2={2,5}`, `P3={3,7}`;
- `u0=(2,1,2)/3`, `u1=(2,-2,-1)/3`, `u2=(1,2,-2)/3` in the last three coordinates.

The code is the disjoint union of:

1. `16` vectors `±2e_i`, for `0 <= i < 8`;
2. `480` vectors consisting of all 16 signings on 30 four-coordinate supports;
3. `96` vectors `±e_a ±e_b ±sqrt(2)u_j`, with `{a,b}=P_r`;
4. `12` vectors `sqrt(2)(±u_i ±u_j)`.

The exact verifier establishes:

- 604 distinct vectors;
- every squared norm is exactly 4;
- all `604*603/2 = 182,106` unordered pairs satisfy `<v,w> <= 2`;
- the maximum distinct-vector inner product is exactly 2;
- the coordinate matrix has rank exactly 11;
- the code is antipodal, with 302 lines;
- there are 19,704 contact pairs.

The canonical coordinate file has SHA-256

`3dc8aba270c31474cd5fb4ba3f9733311b35a5dd23a827c3f7005661c41701f7`.

Therefore `tau_11 >= 604` rigorously.

## 3. Exact saturation theorem

Let `C` denote the norm-2 code and define its kissing-threshold polar

`P(C) = { y : |<v,y>| <= 2 for every v in C }`.

A vector that could be adjoined to the kissing code would have to belong to `P(C)` and have squared norm 4.

### Theorem

`max_{y in P(C)} ||y||^2 = 3`.

### Reduction to 67 nonnegative affine forms

Write `y=(x,z)` with `x in R^8`, `z in R^3`, and set `p_i=|x_i|`. Because each construction family contains all relevant signings, membership in `P(C)` implies:

- `0 <= p_i <= 1`;
- `sum_{i in P_r union P_s} p_i <= 2` for the six pair-union supports;
- `sum_{i in T} p_i + |z_k| <= 2` for the 24 layer supports;
- `p_a+p_b+sqrt(2)|u_j dot z| <= 2` for the 12 `E1` families;
- `|u_i dot z|+|u_j dot z| <= sqrt(2)` for the three `E2` families.

The signs of

`z_0,z_1,z_2,u_0 dot z,u_1 dot z,u_2 dot z`

split `R^3` into 32 nonempty open chambers. Exact Gordan certificates rule out the other 32 formal sign patterns. A 96-element exact symmetry group has five chamber orbits, represented by

`----+-`, `-+---+`, `------`, `-+----`, and `-----+`.

### Exact Handelman identities

For each representative chamber, the package gives an identity

`3 - sum_i p_i^2 - ||z||^2 = sum_alpha c_alpha product_{j in alpha} g_j(p,z)`,

where every `g_j` is one of the 67 nonnegative affine forms and every coefficient `c_alpha` is a strictly positive element of `Q(sqrt(2))`.

| Chamber representative | Degree | Orbit terms | Expanded products | Orbit size |
|---|---:|---:|---:|---:|
| `----+-` | 3 | 42 | 534 | 6 |
| `-+---+` | 4 | 61 | 2,760 | 2 |
| `------` | 3 | 64 | 480 | 12 |
| `-+----` | 3 | 41 | 570 | 6 |
| `-----+` | 3 | 41 | 570 | 6 |

The independent verifier expands all 4,914 products exactly in `Q(sqrt(2))`, verifies coefficient positivity without decimal approximation, checks all chamber symmetries, and obtains the polynomial identity with zero residual.

Thus every `y in P(C)` has `||y||^2 <= 3`.

The reverse inequality is attained by

`y=(1,1,1,0,0,0,0,0,0,0,0)`,

which is checked directly against all 604 vectors and has squared norm 3. Hence the polar squared radius is exactly 3.

### Corollary

No squared-norm-4 vector can be adjoined to `C`. Equivalently, the normalized 604-point spherical code is saturated. Its antipodal covering parameter is exactly `1/sqrt(3)`, corresponding to covering angle `arccos(1/sqrt(3))`.

## 4. Why this does not determine `tau_11`

Saturation means only that this particular 604-point configuration cannot be extended while keeping all its existing points fixed. A 605-point code could be globally different, or could require deleting and moving many points at once. Therefore the theorem does not imply `tau_11 <= 604`.

The exact missing object is an unrestricted upper-bound proof applying to every spherical code in `S^10`, at some integer `N` for which a matching exact construction is known. No such certificate is contained here.

## 5. Reproduction

Run:

```bash
./verify_all.sh
```

The two main proof programs use only exact integer and rational arithmetic in `Q(sqrt(2))`. No floating-point value is accepted as part of either proof.
