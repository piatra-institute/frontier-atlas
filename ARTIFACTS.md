# Artifacts policy - regenerate-only

Git tracks the reproducible core of each attempt, not its bulky output. This keeps the repo at tens of MB (one worked task, Ramsey R(5,5), is ~135 MB of proof traces alone).

## Tracked
- `prompt.md` (and the maths 01-11 prompt PDFs)
- source: generators, solvers, encoders, verifiers
- reports (`.md`/`.pdf`), `chat.md`
- `SHA256SUMS` / `MANIFEST.sha256` (hashes of every artifact, including ignored ones)
- small certificates and metadata

## Not tracked (gitignored, kept on local disk)
- proof traces: `*.drup`, `*.drat`, `*.lrat`
- binary dumps: `*.npy`, `*.npz`, `*.u8`
- large generated instances: `**/extension_instances/*.txt`
- anything under `generated/`, `_artifacts/`, `_large/`

These are regenerable from the tracked source; the manifests verify them after regeneration.

## Load-bearing certificates
A load-bearing certificate is a file a checker consumes exactly (it is the verified object, not regenerable evidence: a DRAT/LRAT proof the result stands on, a kernel-checked term, an exact dual). Track it or archive it with a DOI, however large, and pin the checker version beside its hash. Regenerate-only applies only to output re-derivable from committed source.

## New work
Put bulky (>~1 MB) regenerable output under `generated/` (or `_artifacts/` / `_large/`), add its hashes to `SHA256SUMS`, keep the generator and manifest tracked. Ship a `CLAIM.md` (see `CLAIM_TEMPLATE.md`) stating the exact result, its checker, its trust base, and its review level.

## Durable retention
If a package needs archival, push its heavy files to external storage (Zenodo for a DOI, or an object store) and record the URLs beside the hashes. The gitignore policy is unchanged.
