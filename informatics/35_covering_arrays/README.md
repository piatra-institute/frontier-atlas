# Optimal covering array numbers CAN(t,k,v)

Determine CAN(t,k,v), the fewest rows of a covering array in which every t of the k
columns shows all v^t symbol combinations. A smaller array than the best known is a
new record, one-sided (no lower bound needed) and instantly checkable. Levels: task,
one folder per approach (`prompt.md`), and a dated run folder per execution.

## Approaches and runs

| approach | run | result | review |
|---|---|---|---|
| `01_baseline` (`[search]` `[opt]`) | `2026-08-01-chatgpt-pro` | certified CAN(2,8,3)=13 (known value; CA(13) + no-CA(12) enumeration). Package self-verifies. Exploratory CAN(3,7,3) N=38 attempt reached 5 uncovered, no record. | agent; reproduction |
| `01_baseline` (`[search]` `[opt]`) | `2026-08-01-claude-code` | independent re-verification of both arrays; serious record attempt at CAN(3,7,3) N=38 (best known 39, not proven optimal) | self; record attempt |

## Notes

- `2026-08-01-chatgpt-pro` certifies CAN(2,8,3)=13 (Colbourn-Keri-Rivas
  Soriano-Schlage-Puchta, Thm 5.2; a known value). `verify_all.sh` passes here (upper
  CA(13) + Bron-Kerbosch lower-bound enumeration, no K6, so no CA(12)). No new result.
- `2026-08-01-claude-code` independently verified both covering arrays (CA(13;2,8,3)
  and the exploration's CA(39;3,7,3), 0 missing interactions each), and attacks the
  open record CAN(3,7,3): the best known is 39 (Colbourn table, "SAT Local Search
  (Hnich et al.)", not marked optimal), so a valid CA(38;3,7,3) would be a new record.
- CAN(3,7,3) is the live target here: genuinely open, search-driven record, and any
  CA(38) is checkable in seconds.
