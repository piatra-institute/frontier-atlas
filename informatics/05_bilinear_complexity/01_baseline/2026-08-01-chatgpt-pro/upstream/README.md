# Upstream cross-check artifacts

These files are preserved as provenance cross-checks only. The local command
`./verify_all.sh` neither parses nor trusts them.

## Current certificate

`cert_matrix_q02_n223.pb.txt` was retrieved on 2026-08-01 from Chengu Wang's
current public repository `wcgbg/tensor-rank-lower-bound`, path:

`certs/matrix/cert_matrix_q02_n223.pb.txt`

SHA-256 at retrieval:

`cf930d9358d56e21dc953cd2618820ad788a364444bcb5fe16bb0cf4926a169b`

The certificate is for `matrix_q02_n223`, meaning the
\(\langle2,2,3\rangle\) matrix-multiplication tensor over \(\mathbb F_2\).
It records lower and upper bounds 11, the 11 restriction-orbit entries, and
backtracking proof sizes 13 and 1303. The local proof was reconstructed and
verified independently, but reproduces those two tree sizes.

## Legacy certificate

`legacy_rmms_n223.pb.txt` is the earlier certificate retrieved from
`wcgbg/matrix-multiplication-lower-bound-n3r20f2`, path
`proof_cert/rmms_n223.pb.txt`.

SHA-256 at retrieval:

`78eaac4cb7432a6a56aaee2aa74182d34e1abdd5fcf2e89d60c3dd8bcd56d2b7`

It is retained to document the literature/repository transition between the
older matrix-specific implementation and the current general bilinear-rank
framework.
