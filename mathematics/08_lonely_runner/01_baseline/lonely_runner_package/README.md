# Lonely Runner research package

This package accompanies an audited attempt to resolve the Lonely Runner Conjecture from the supplied Piatra Institute prompt.

## Result status

The original conjecture is not claimed solved. The package proves, exactly, that Conjecture 7.1 of Sungkawichai-Trakulthongchai (2026), a proposed universal-grid extension mechanism, is false as written. It also proves a corrected speed-dependent grid theorem.

## Files

- `Lonely_Runner_Research_Report.pdf` - formatted final report.
- `Lonely_Runner_Research_Report.docx` - editable formatted report.
- `RESEARCH_REPORT.md` - source report with full statements, proofs, audit, and exact remaining gap.
- `RESEARCH_LOG.md` - approach registry and blockers.
- `lrc_exact.py` - exact rational checker and critical-time evaluator.
- `verify_certificate.py` - certificate verification wrapper.
- `lrc_grid_obstruction_certificate.json` - two exact `k=13` examples.
- `verification_output.txt` - captured output from the exact regression and certificate checks.
- `SHA256SUMS` - integrity hashes.

## Requirements

Python 3.10 or newer. No third-party packages are required.

## Verify everything

```bash
python lrc_exact.py --self-test
python verify_certificate.py lrc_grid_obstruction_certificate.json
sha256sum -c SHA256SUMS
```

## Reproduce the two examples

```bash
python lrc_exact.py --speeds 1 2 3 4 5 6 7 8 9 10 11 12 2000 --grid 2000 --maximum
python lrc_exact.py --speeds 1 2 3 4 5 6 7 8 9 10 11 12 2016 --grid 2003 --maximum
```

Each command should report threshold `1/14`, zero grid witnesses, and exact maximum loneliness `1/13`.
