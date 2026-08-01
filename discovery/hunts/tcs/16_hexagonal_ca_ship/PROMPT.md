# 16. Spaceship of an open speed in a hexagonal or triangular CA

**Find.** A spaceship of an unrealized velocity in a specified 2-state cellular automaton on a non-square lattice: a hexagonal-neighbourhood Life-like rule (e.g. Hex rules in Golly notation) or a triangular-grid rule. These lattices have small, actively-catalogued but sparse object zoos on Catagolue, with many velocities lacking any known ship (verify rule and gap).

**What counts as a win.** One RLE valid under the chosen hex/tri rule that is a spaceship of a velocity absent from that rule's census. One-sided: existence only.

**Checker (seconds).** Simulate under the exact hexagonal/triangular neighbourhood transition (fewer or differently-shaped neighbours than Moore). Verify true period and lattice-translation vector in the lattice's coordinate system. Integer-exact; validate the neighbourhood encoding against Golly's hex/tri algos.

**Search plan.** Structured: gfind/LLS variants that support hex neighbourhoods; Catagolue apgsearch hauls for the rule to surface tagged unknown-velocity partials, then clean up. Evolutionary soup search for exotic velocities.

**Prior art (verify).** LifeWiki, "Hexagonal neighbourhood" and "Triangular neighbourhood"; Golly rule-format docs; Catagolue hex/tri censuses. Verify the target velocity is still unrealized in the chosen rule.
