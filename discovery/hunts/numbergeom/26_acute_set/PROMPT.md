# Acute set larger than the record in fixed dimension

**Find.** A set of points in R^d, more than the best published count, such that every triple spans an acute triangle (all three angles strictly less than 90 degrees), for a dimension d where the maximum acute-set size is open.

**What counts as a win (one-sided).** One point set of size s in R^d, with s above the current record, all of whose triples are acute. A single larger set beats the record; failure proves nothing.

**Checker (seconds).** For every triple of points, verify all three vertex angles are acute, i.e. every dot product (v_i - v_j) . (v_k - v_j) > 0 at each vertex. With rational coordinates this is exact. O(s^3) dot products; seconds for the relevant s.

**Search plan.** Use rational or small-integer coordinates so the angle tests certify exactly; local search / simulated annealing adding points while all triples stay acute; seed from cube-vertex-perturbation constructions (Erdos-Furedi style) and from known record sets. Evolutionary search scored by the number of non-acute triples (drive to zero, then grow).

**Prior art (verify).** The maximum size of an acute set in R^d grows exponentially (Erdos and Furedi), but exact maxima and the best explicit constructions are known only for small d and improve irregularly. See Erdos-Furedi and later work (Bevan; Harangi). Confirm the record for the target d before starting (verify).
