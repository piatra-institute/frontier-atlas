# 16. Difference set for an open parameter set

**Target.** Construct a (v,k,lambda)-difference set in an abelian group of order v for a parameter set currently listed as open (existence undecided) in the difference-set tables, or prove nonexistence. A (v,k,lambda)-difference set D is a k-subset of a group G of order v such that every nonidentity element of G has exactly lambda representations as a difference d - d' with d,d' in D. Pick a specific open (v,k,lambda) and group from the table.

**What counts as a win.** One explicit subset D of the named group settles existence for that parameter set and group (one-sided YES). A difference set yields a symmetric 2-(v,k,lambda) design automatically.

**Checker (seconds).** Read D as a k-subset of G (given by generators). Form the multiset { d - d' : d != d' in D } (k(k-1) differences); assert every nonidentity element of G occurs exactly lambda times. O(k^2), microseconds.

**Search plan.** Cyclotomic-class and character-sum constructions; multiplier-restricted search (a numerical multiplier fixes D up to a union of orbits, collapsing the search); SAT/ILP over group-element indicators with the difference constraint.

**Prior art (verify).** Open parameter sets are catalogued in the La Jolla Difference Set Repository (D. Gordon, ljcr.dmgordon.org) and in Colbourn-Dinitz "Handbook of Combinatorial Designs." Re-verify the chosen (v,k,lambda) is still open before committing.

**Openness:** documented-open (verify). **Win-type:** existence.
