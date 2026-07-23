# Artifact provenance

## What this archive is

This archive is a clean reconstruction of the mathematical reduction, verifier, case normalization, OPB encoding, projector formulation, and small-instance audits preserved in the conversation.

## What this archive is not

The exploratory runtime used before this archive was requested did not preserve its temporary working directory. Consequently:

- temporary source files from that runtime were not recoverable;
- interrupted solver processes and partial solver states are not included;
- no solver `UNKNOWN` output is elevated into evidence;
- this archive is not byte-identical to the exploratory code.

The code here was rewritten, tested, and packaged after the download request. It should therefore be cited as a reconstructed research package, not as a forensic copy of the earlier runtime.

## Included evidence

- original uploaded PDF prompt;
- exact derivations in human-readable form;
- source implementing the derivations;
- deterministic 11-case manifest;
- exhaustive enumeration of all 10,395 local perfect matchings;
- exhaustive `m=2` reduced search;
- independent construction checks for the projector baseline;
- exact OPB generator and a semantically checked small OPB instance;
- unit-test output, audit JSON, and SHA-256 hashes.

## Excluded claims

The archive deliberately excludes unsupported statements of existence, nonexistence, novelty, solver completeness, or runtime duration.
