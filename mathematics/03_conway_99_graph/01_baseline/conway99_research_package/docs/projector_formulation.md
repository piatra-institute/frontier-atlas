# Integral-projector formulation

## Status of the viewpoint

This formulation is mathematically derived and implemented in the package. Its publication-level novelty has **not** been established. It has not yet eliminated a normalized case or constructed the graph.

## 1. A quadratic root of a fixed line graph

Let

\[
R=MM^T-2I.
\]

Because `M` is the unsigned incidence matrix of

\[
C=K_{2,2,2,2,2,2,2},
\]

`R` is the adjacency matrix of its line graph `L(C)`.

The reduced quadratic equation becomes

\[
B^2+B+R=10I+2J.
\tag{P1}
\]

The fixed matrix `R` has spectrum

\[
22^1,\quad10^7,\quad8^6,\quad(-2)^{70}.
\]

Equation `BM=MT` forces the `B`-eigenvalues `12`, `0`, and `-2` on the first three corresponding eigenspaces. All remaining freedom lies in the 70-dimensional `(-2)`-eigenspace of `R`, where `B` has eigenvalues `3` and `-4` with multiplicities 40 and 30.

## 2. Rank-40 orthogonal projector

Let `E_22`, `E_10`, `E_8`, and `E_-2` be the spectral projectors of `R`. There must be a rank-40 orthogonal projector `P`, supported in `E_-2`, such that

\[
B=12E_{22}-2E_8-4E_{-2}+7P.
\tag{P2}
\]

The diagonal ranks of the fixed projectors are constant:

\[
(E_{22})_{ii}=\frac1{84},\quad
(E_{10})_{ii}=\frac1{12},\quad
(E_8)_{ii}=\frac1{14},\quad
(E_{-2})_{ii}=\frac56.
\]

Since `B_ii=0`,

\[
P_{ii}=\frac{10}{21}.
\]

Thus `P` is the Gram matrix of 84 equal-norm vectors in `R^40` forming a Parseval tight frame.

## 3. Integral scaling

Define

\[
G=105P.
\]

A valid graph produces an integer symmetric matrix satisfying

\[
G^2=105G,
\qquad
G\mathbf1=0,
\qquad
G_{ii}=50,
\qquad
\operatorname{rank}G=40.
\tag{P3}
\]

Write

\[
G=G_0+15B.
\]

The fixed baseline matrix is

\[
G_0=-15(12E_{22}-2E_8-4E_{-2}).
\]

It also has the exact line-graph polynomial form

\[
G_0=
\frac{(R-10I)(R^2-30R-184I)}{24}.
\tag{P4}
\]

The package constructs `G_0` both combinatorially and from `(P4)` and checks equality entry by entry.

## 4. Fixed residue class modulo 15

For distinct base edges `e,f`, the baseline entry depends only on their relationship:

| Relationship | `G0_ef` | Permitted `G_ef` |
|---|---:|---:|
| overlap; other endpoints are mates | -5 | -5 or 10 |
| overlap; other endpoints in distinct parts | -6 | -6 or 9 |
| disjoint; two base parts used | 0 | 0 or 15 |
| disjoint; three base parts used | -1 | -1 or 14 |
| disjoint; four base parts used | -2 | -2 or 13 |

Every adjacency decision therefore adds exactly 15. In particular,

\[
G\pmod{15}
\]

is fixed before any search begins.

## 5. Potential research mechanisms

The formulation suggests several exact avenues:

1. **Integral-lattice obstruction:** rule out positive-semidefinite rank-40 lifts of the fixed residue matrix.
2. **Local principal-minor pruning:** reject partial `+15` lifts using exact determinant and rank conditions.
3. **Finite-field lifting:** exploit `G^2=0` modulo 3, 5, 7, and their compatible row spaces.
4. **Tight-frame constraints:** apply Schur-product positivity, few-distance bounds, or coherent-configuration refinements.
5. **Canonical augmentation:** search over lift choices modulo `S2 wr S7`, rather than over an unstructured 84-vertex graph.

None is yet a completed obstruction. The next useful theorem would eliminate at least one of the 11 normalized cases or prove a nontrivial restriction on the cycle type of the forced 2-factor.
