You: 

06\_kissing\_number\_11(1).pdf

PDF

read prompt and solve it

ChatGPT: 

Worked for 67m 23s

## Task interpreted

Determine the exact 11-dimensional kissing number $\tau_{11}$, accepting a result only when an exact construction and an unrestricted, rigorously checkable upper bound meet at the same integer. That is the completion standard imposed by the prompt.

06\_kissing\_number\_11

# Result

**I did not establish the exact value of $\tau_{11}$.**

As of **22 July 2026**, the public best-known range remains

$$
\boxed{604\le \tau_{11}\le 868}.
$$

Henry Cohn’s current table records these two bounds, and the recent construction paper reports the improvement of the lower bound from 593 to 604. [![](https://www.google.com/s2/favicons?domain=https://cohn.mit.edu&sz=128)cohn.mit.edu+1](https://cohn.mit.edu/kissing-numbers/)

| Required result | Outcome |
| --- | --- |
| Exact 604-point construction | **Proved** |
| Exact audit of all $182{,}106$ pairs | **Passed** |
| Rank at most 11 | **Passed, rank exactly 11** |
| Proof that this 604-code cannot be augmented | **Proved exactly** |
| Universal exclusion of every 605-point code | **Not obtained** |
| Exact value of $\tau_{11}$ | **Unresolved** |

The distinction matters because the prompt explicitly rejects a construction or special-configuration result without a matching unrestricted upper bound.

06\_kissing\_number\_11

# Strongest exact result obtained

I reconstructed the published 604-point configuration over

$$
\mathbb Q(\sqrt2)
$$

and derived an exact certificate proving something substantially stronger than numerical saturation.

Let $C\subset\mathbb R^{11}$ be the reconstructed code in the normalization

$$
\|v\|^2=4,\qquad \langle v,w\rangle\le 2 \quad(v\ne w).
$$

Dividing all vectors by $2$ gives the conventional unit-vector formulation with inner products at most $1/2$.

Define the kissing-threshold polar

$$
P(C)=\left\{y\in\mathbb R^{11}: |\langle v,y\rangle|\le2\text{ for every }v\in C\right\}.
$$

I proved the exact identity

$$
\boxed{\max_{y\in P(C)}\|y\|^2=3}.
$$

An additional kissing vector would need squared norm $4$. Therefore:

$$
\boxed{\text{No 605th vector can be adjoined to this particular 604-point code.}}
$$

The configuration is thus **geometrically saturated with an exact squared-norm gap of $1$**.

In the unit-vector normalization, this is equivalently

$$
\min_{\|x\|=1}\max_{u\in C/2}|\langle u,x\rangle| =\frac1{\sqrt3}.
$$

Its antipodal covering angle is exactly

$$
\arccos\!\left(\frac1{\sqrt3}\right)\approx54.7356^\circ,
$$

strictly below the $60^\circ$ angle required for adding another kissing point.

## Exact construction audit

The verifier establishes, with no floating-point arithmetic:

-   $604$ distinct vectors in $\mathbb R^{11}$;
    
-   squared norm exactly $4$ for every vector;
    
-   all $604\cdot603/2=182{,}106$ unordered inner products checked exactly;
    
-   maximum distinct-vector inner product exactly $2$;
    
-   rank exactly $11$;
    
-   $302$ antipodal lines;
    
-   $19{,}704$ contact pairs;
    
-   coordinate-file SHA-256:
    

```
```
3dc8aba270c31474cd5fb4ba3f9733311b35a5dd23a827c3f7005661c41701f7
```
```

## Saturation-certificate structure

Writing a prospective added vector as $y=(x,z)\in\mathbb R^8\oplus\mathbb R^3$ and putting $p_i=|x_i|$, the 604 code implies 67 nonnegative affine inequalities involving

$$
p_0,\ldots,p_7,\quad z_0,z_1,z_2.
$$

The six signs

$$
z_0,z_1,z_2,\quad u_0\!\cdot z,u_1\!\cdot z,u_2\!\cdot z
$$

produce:

-   64 formal sign patterns;
    
-   32 exactly feasible chambers;
    
-   32 patterns excluded by exact Gordan certificates;
    
-   five chamber orbits under a 96-element exact symmetry group.
    

For each chamber representative I generated an identity of the form

$$
3-\sum_{i=0}^{7}p_i^2-\sum_{j=0}^{2}z_j^2 = \sum_\alpha c_\alpha \prod_{k\in\alpha}g_k(p,z),
$$

where:

-   every $g_k$ is one of the nonnegative affine constraints;
    
-   every $c_\alpha$ is a strictly positive element of $\mathbb Q(\sqrt2)$;
    
-   the identities have degree at most $4$;
    
-   an independent verifier expands every term and obtains zero residual exactly.
    

| Chamber | Degree | Compact orbit terms | Expanded products | Chambers covered |
| --- | --- | --- | --- | --- |
| `----+-` | 3 | 42 | 534 | 6 |
| `-+---+` | 4 | 61 | 2,760 | 2 |
| `------` | 3 | 64 | 480 | 12 |
| `-+----` | 3 | 41 | 570 | 6 |
| `-----+` | 3 | 41 | 570 | 6 |
| **Total** |  | **249** | **4,914** | **32** |

The upper value $3$ is attained by

$$
y=(1,1,1,0,0,0,0,0,0,0,0),
$$

which was checked directly against all 604 vectors. Hence the polar-radius result is an equality, not merely a bound.

# Why this is not an upper bound for $\tau_{11}$

Saturation fixes all 604 existing points. It rules out

$$
C\subset C',\qquad |C'|=605.
$$

It does **not** rule out a completely different 605-point configuration, or a deformation that first deletes and moves many of the 604 points. Therefore

$$
\max_{y\in P(C)}\|y\|^2=3
$$

does not imply

$$
\tau_{11}\le604.
$$

The missing object remains an upper certificate applying to **every** spherical code in $S^{10}$.

The published source underlying the reported upper bound says that its high-precision three-point SDP computations could be made rigorous by interval arithmetic, but that the authors did not perform that verification procedure. Consequently, that paper’s numerical output by itself does not satisfy the stricter exact-certificate standard imposed by this prompt. [![](https://www.google.com/s2/favicons?domain=https://link.springer.com&sz=128)Springer](https://link.springer.com/article/10.1007/s12532-024-00264-w)

The attached prompt instructs that, when execution stops without a complete resolution, success must not be fabricated and only the strongest rigorously verified result and exact remaining gap should be reported.

06\_kissing\_number\_11

# Files

Download the complete exact verification package

RESULT.md

verification\_saturation\_604.json

ZIP SHA-256:

```
```
27a81005fa2b2ccd7e00ed8ccf6e4314934e9bf007f650b7632da5559dde7647
```
```

The package contains the coordinates, all five exact certificates, independent standard-library verifiers, the original prompt, software information, and a complete hash manifest. Running `./verify_all.sh` reconstructs and audits the construction and the saturation theorem without using floating-point arithmetic in any mathematical check.

![](https://www.google.com/s2/favicons?domain=https://link.springer.com&sz=32)

![](https://www.google.com/s2/favicons?domain=https://arxiv.org&sz=32)

![](https://www.google.com/s2/favicons?domain=https://cohn.mit.edu&sz=32)

Sources

Do you like this personality?