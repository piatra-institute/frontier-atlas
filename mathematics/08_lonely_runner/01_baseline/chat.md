You: 

08\_lonely\_runner(1).pdf

PDF

read the prompt and solve it

ChatGPT: 

Worked for 94m 14s

> **Task understood:** Resolve the attached Lonely Runner Conjecture prompt by either proving the conjecture uniformly for every $k$, producing an exact counterexample, or, if neither survives verification, reporting only the strongest rigorous result together with reproducible artifacts.

# Verdict

**I did not obtain a complete resolution of the original Lonely Runner Conjecture.** No uniform all-$k$ proof and no tuple violating

$$
\max_t\min_i\|t u_i\|\geq \frac1{k+1}
$$

survived the audit.

That distinction matters because the prompt requires either a uniform proof or an exact counterexample, while explicitly instructing that a hard stop must produce the strongest verified derivation rather than fabricated success.

08\_lonely\_runner

08\_lonely\_runner

The current public verification reaches $k\leq 12$ relative speeds, corresponding to 13 total runners. Thus $k=13$, or 14 total runners, remains the first unverified case. [![](https://www.google.com/s2/favicons?domain=https://arxiv.org&sz=128)arXiv](https://arxiv.org/abs/2604.23906)

However, the investigation produced a complete and machine-checked result against a recent proposed route to the conjecture:

> **Conjecture 7.1 of Sungkawichai and Trakulthongchai, the proposed universal-denominator theorem for non-tight tuples, is false as written for every $k\geq2$.**

That conjecture appears in the concluding section of their 2026 paper. [![](https://www.google.com/s2/favicons?domain=https://arxiv.org&sz=128)arXiv+1](https://arxiv.org/abs/2604.23906)

## 1\. Exact counterexample family to the universal-denominator conjecture

Fix $k\geq2$, write $q=k+1$, and define

$$
C_k=\frac{k(k+1)(k-1)}2.
$$

For every integer $d>C_k$, consider

$$
V_{k,d}=(1,2,\ldots,k-1,d).
$$

Then:

1.  all entries are positive and distinct;
    
2.  $\gcd(V_{k,d})=1$;
    
3.  $V_{k,d}$ is non-tight, meaning it has a time at which every inequality is strictly above $1/(k+1)$;
    
4.  nevertheless, it has no witness in $\frac1d\mathbb Z$.
    

### Proof

At any $d$\-grid time $t=a/d$,

$$
\|dt\|=\|a\|=0.
$$

Therefore no $t\in\frac1d\mathbb Z$ can be a witness.

To prove that the tuple is non-tight, start from $t_0=1/k$. For $1\leq i\leq k-1$,

$$
\left\|\frac{i}{k}\right\|\geq\frac1k.
$$

Choose a midpoint of a $d$\-grid cell,

$$
t_*=\frac{2m+1}{2d},
$$

nearest to $1/k$. Then

$$
\left|t_*-\frac1k\right|\leq\frac1{2d}.
$$

Since distance to the nearest integer is 1-Lipschitz,

$$
\|it_*\| \geq \left\|\frac{i}{k}\right\|-i\left|t_*-\frac1k\right| \geq \frac1k-\frac{k-1}{2d}.
$$

The condition $d>C_k$ is exactly sufficient to give

$$
\frac1k-\frac{k-1}{2d}>\frac1{k+1}.
$$

For the last coordinate,

$$
\|dt_*\| = \left\|\frac{2m+1}{2}\right\| = \frac12>\frac1{k+1}.
$$

Hence $t_*$ is a strict continuous-time witness, while the complete $1/d$\-grid contains no witness.

This disproves the universal-denominator conjecture because its quantifiers permit the tuple to depend on $d$: for each sufficiently large denominator, $V_{k,d}$ is an admissible counterexample to the auxiliary statement.

## 2\. The natural coprimality repair also fails

One might repair the conjecture by requiring every speed to be coprime to the grid denominator. That still does not work.

For $q=k+1$, the canonical tuple $(1,\ldots,k)$ satisfies

$$
\min_{1\leq i\leq k}\|it\|\geq\frac1q
$$

exactly at times

$$
t=\frac{s}{q}\pmod 1,\qquad \gcd(s,q)=1.
$$

Indeed, the $q$ points

$$
0,t,2t,\ldots,kt
$$

must be pairwise separated by at least $1/q$. Their $q$ cyclic gaps sum to one, so every gap must equal $1/q$.

Now take an integer $d$ coprime to $q$ and define

$$
W_{k,d}=(1,2,\ldots,k-1,d+k).
$$

At every $t=a/d$, this tuple is congruent to $(1,\ldots,k)$ modulo $d$. A grid witness would therefore have to lie simultaneously on the $1/d$\-grid and the $1/q$\-grid. When $\gcd(d,q)=1$, their only common point is $0$, which is not a witness.

For sufficiently large $d$, the preceding midpoint argument proves that $W_{k,d}$ is non-tight. When $d>k$ is prime, every speed in $W_{k,d}$ is individually coprime to $d$.

## 3\. Exact $k=13$ certificates

The original threshold for 13 relative speeds is $1/14$.

| Construction | Speeds | Tested grid | All speeds coprime to grid denominator | Exact $\kappa$ | Grid witnesses |
| --- | --- | --- | --- | --- | --- |
| Diagonal | $(1,2,\ldots,12,2000)$ | $1/2000$ | No | $1/13$ | $0$ |
| Congruence robust | $(1,2,\ldots,12,2016)$ | $1/2003$ | Yes | $1/13$ | $0$ |

For the diagonal tuple, an exact strict witness is

$$
t=\frac{307}{4000}, \qquad \min_i\|t u_i\|=\frac{307}{4000}>\frac1{14}.
$$

For the robust tuple, an exact strict witness is

$$
t=\frac{311}{4032}, \qquad \min_i\|t u_i\|=\frac{25}{336}>\frac1{14}.
$$

The exact maximum $1/13$ also follows symbolically, not merely computationally. Both tuples contain the prefix $(1,\ldots,12)$, whose maximum loneliness is $1/13$, giving an upper bound. At $t=1/13$, the added speeds have nonzero residues modulo 13, giving the matching lower bound.

These tuples **are not counterexamples to the original Lonely Runner Conjecture**. They satisfy it with strict slack. They are counterexamples only to the proposed universal-grid extension.

## 4\. Corrected grid theorem

The failed statement becomes true when the denominator is allowed to depend on the tuple’s speed scale.

Let

$$
F_v(t)=\min_i\|v_i t\|, \qquad M=\max_i|v_i|, \qquad q=k+1.
$$

### Critical-time lemma

A maximum of $F_v$ occurs at a time

$$
t=\frac{a}{|v_i|+|v_j|}
$$

for some $i,j$, allowing $i=j$.

This follows because $F_v$ is the lower envelope of triangular waves. At a local maximum, either an active wave is at a breakpoint, giving denominator $2|v_i|$, or active affine branches of opposite slopes meet, giving denominator $|v_i|+|v_j|$.

Consequently, a maximizing denominator $N$ can be chosen with

$$
N\leq2M.
$$

If the tuple is non-tight, then its exact rational maximum satisfies

$$
\kappa(v)-\frac1q\geq\frac1{qN}.
$$

### Speed-dependent universal grid

Every non-tight integer $k$\-tuple has a witness on every grid whose denominator satisfies

$$
d\geq qM^2.
$$

More sharply,

$$
d\geq\frac{qMN}{2}
$$

is sufficient when $N$ is a maximizing denominator.

To see this, choose the closest $b/d$ to a maximizing time $t_0$. Since $F_v$ is $M$\-Lipschitz,

$$
F_v(b/d) \geq \kappa(v)-\frac{M}{2d}.
$$

The stated bound ensures that the approximation loss is at most the exact slack $1/(qN)$.

Thus the corrected theorem is:

> A sufficiently fine grid always detects a non-tight integer tuple, but the required denominator must depend quantitatively on the tuple. A denominator uniform over all coprime non-tight tuples cannot exist.

## Exact remaining gap

A complete resolution of the original prompt still requires one of:

$$
\kappa(v)\geq\frac1{k+1}
$$

for every admissible tuple and every $k$, proved uniformly; or a finite exact tuple satisfying

$$
\kappa(v)<\frac1{k+1},
$$

together with a symbolic full-circle forbidden-interval cover.

The work here establishes neither alternative. It does eliminate one proposed extension mechanism, explains the structural reason for its failure, and supplies a correct quantitative replacement. I am not asserting literature priority for the obstruction.

## Artifacts

Download the complete research package

Lonely\_Runner\_Research\_Report.pdf

Lonely\_Runner\_Research\_Report.docx

The package also contains the RESEARCH\_REPORT.md, lrc\_exact.py, verify\_certificate.py, lrc\_grid\_obstruction\_certificate.json, captured verification output, research log, source prompt, and SHA-256 hashes. Both the regression suite and independent certificate verification pass.

![](https://www.google.com/s2/favicons?domain=https://www.researchgate.net&sz=32)

![](https://www.google.com/s2/favicons?domain=https://arxiv.org&sz=32)

Sources