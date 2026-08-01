# A 6-chromatic unit-distance graph

**Find.** A finite unit-distance graph in the plane (vertices with exact coordinates, edges exactly between points at distance 1) whose chromatic number is at least 6.

**What counts as a win (one-sided).** One unit-distance graph that is not 5-colorable. A single such graph raises the lower bound for the chromatic number of the plane from 5 to 6; failure proves nothing.

**Checker (seconds).** Verify every edge joins points at exact distance 1 and every non-edge does not, using exact arithmetic in the relevant number field (coordinates typically lie in Q(sqrt 3) and similar). Then verify non-5-colorability with a SAT solver and export a DRAT/LRAT proof of unsatisfiability of the 5-coloring instance; check the proof independently.

**Search plan.** Build from Moser-spindle and de Grey style gadgets; take unions and spindles of the known 5-chromatic graphs, and rotations by angles with rational cos, then test 5-colorability with a SAT solver; grow the graph guided by fractional-chromatic and clause-conflict signals. This is the natural continuation of the Polymath16 machinery.

**Prior art (verify).** The chromatic number of the plane is known to lie between 5 and 7: de Grey (2018) exhibited a 5-chromatic unit-distance graph, and the Polymath16 project pushed constructions and lower vertex counts. Whether a 6-chromatic unit-distance graph exists is open. See de Grey (2018) and the Polymath16 project pages (verify).
