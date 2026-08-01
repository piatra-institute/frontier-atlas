# 30. Halting witness for a small tag system of open behaviour

**Find.** For a specified small Post tag system whose halting on a given initial word is an open question, a witness that it halts. A tag system with deletion number m repeatedly deletes the first m symbols and appends a production determined by the first symbol; several small tag systems (including historically studied 2-tag and 3-tag systems, and instances arising in the "3n+1"-flavoured tag encodings) have initial words whose halting/periodicity status is undetermined (verify the specific instance).

**What counts as a win.** One initial word plus a step count N at which the machine reaches a halting configuration (word shorter than the deletion number, or an empty word). One-sided: a halt is a definite result. (A detected exact configuration repeat instead certifies non-halting periodicity, also a definite result.)

**Checker (seconds).** Deterministically simulate the tag system from the given word for N steps, applying the deletion-and-append rule; assert the configuration at step N is halting (or, for the periodic case, equals an earlier configuration). Integer/string-exact; one run.

**Search plan.** Structured: simulate the open instances far (the word length is the only cost; billions of steps are cheap) with a cycle-detector hashing the current word to catch periodicity, and a length monitor to catch halting. Try the documented "hard" seeds first.

**Prior art (verify).** Post (1943, tag systems); De Mol, "Tag systems and Collatz-like functions" and studies of small tag-system (un)decidability; Wang, and the 2-tag simulation literature. Verify the chosen instance's status is open.
