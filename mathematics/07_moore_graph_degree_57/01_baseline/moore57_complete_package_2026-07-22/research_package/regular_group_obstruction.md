# A character obstruction to all regular group constructions

## Theorem

There is no degree-57 Moore graph whose rooted branch-to-branch matchings are all induced by
a semiregular permutation group on the 56 labels in a branch.

Equivalently, the missing Moore graph cannot arise as a regular `(57,56,1)` antipodal cover
of `K_57` from a group of deck transformations of order 56.

## Proof

Fix a root. Its 57 neighbors define 57 fibres, each containing 56 distance-two vertices.
Between every two distinct fibres there is a perfect matching. Normalize the labels so that
the matchings from one distinguished fibre are the identity.

Assume every matching permutation belongs to a semiregular permutation group `G` on the 56
labels. A semiregular group has all orbits of size `|G|`, so `|G|` divides 56. For any fixed
fibre, the 55 nonidentity matching permutations to the other non-distinguished fibres are
pairwise distinct: equality of two would create a 4-cycle. Hence `|G| >= 56`, and therefore
`|G| = 56`; the action is regular.

Every group of order 56 has a nontrivial one-dimensional complex character. Indeed, the
number `n_7` of Sylow 7-subgroups is 1 or 8.

- If `n_7=1`, the quotient by the normal Sylow 7-subgroup has order 8 and has a quotient of
  order 2.
- If `n_7=8`, the eight Sylow 7-subgroups contribute 48 distinct nonidentity elements. The
  remaining seven nonidentity elements form the unique Sylow 2-subgroup, which is normal;
  the quotient has order 7.

Thus in either case `G` has a nontrivial linear character `chi`.

Let `C` be the adjacency matrix of the 3192-vertex distance-two subgraph. In 57-by-57 block
form its off-diagonal blocks are the regular permutation matrices `P(g_ij)` and its diagonal
blocks are zero. The rooted Moore equations give

```text
C^2 = 56 I - C + J - P,
```

where `P` is block diagonal with 57 copies of `J_56`.

Apply `chi` blockwise to the group algebra. Because `chi` is nontrivial,
`sum_{g in G} chi(g)=0`; consequently both `J` and `P` map to zero. We obtain a Hermitian
57-by-57 matrix `S_chi` satisfying

```text
S_chi^2 + S_chi = 56 I_57,
tr(S_chi)=0.
```

Its only eigenvalues are 7 and -8. If their multiplicities are `a` and `b`, then

```text
a+b=57,
7a-8b=0.
```

This forces `a=152/5`, not an integer. Contradiction.

Therefore no semiregular group construction exists. The argument includes cyclic, abelian,
and nonabelian groups of order 56. It does not exclude a genuinely nonregular cover whose
matching permutations do not lie in a semiregular group.
