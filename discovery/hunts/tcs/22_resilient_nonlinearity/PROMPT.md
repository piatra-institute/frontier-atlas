# 22. A resilient Boolean function meeting an open nonlinearity target

**Find.** A t-resilient Boolean function f: F_2^n -> F_2 whose nonlinearity attains a value that is conjectured maximal but for which no explicit function is known, at a specific small (n, t). The trade-off between resiliency order t and nonlinearity is bounded (Sarkar-Maitra, Tarannikov), and for several (n, t) the maximum achievable nonlinearity, or an explicit optimal function, is open (verify the target cell).

**What counts as a win.** One explicit truth table that is (a) t-resilient and (b) has nonlinearity equal to (or exceeding) the best published value for that (n, t). One-sided: an explicit function reaching the target settles achievability there.

**Checker (seconds).** t-resiliency: verify the Walsh spectrum W_f(a) = 0 for all a with Hamming weight <= t (correlation immunity of order t) and that f is balanced (W_f(0) = 0). Nonlinearity from max|W_f|. All from one fast Walsh-Hadamard transform; exact integer.

**Search plan.** Structured: constructions from the Maiorana-McFarland and Tarannikov elementary-construction families, then local search to lift nonlinearity while preserving the zero-Walsh-coefficient pattern; SAT with linear constraints fixing low-weight Walsh coefficients to 0.

**Prior art (verify).** Siegenthaler (1984); Sarkar & Maitra, "Nonlinearity bounds and constructions of resilient Boolean functions" (2000); Tarannikov constructions; tables of best-known resilient nonlinearities (verify the open (n,t) cell).
