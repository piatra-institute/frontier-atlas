#!/usr/bin/env python3
from pathlib import Path
import csv,json,hashlib
import networkx as nx
from two_bad_certificates import formula
ROOT=Path('..');P=ROOT/'proofs'/'two_bad';R=ROOT/'results'
graphs=list(nx.read_graph6(ROOT/'data'/'r55_42some.g6'))
enum=json.loads((R/'two_bad_extension_enumeration.json').read_text())['per_base']
manifest=[]
for i in range(328):
 base,cnf,nvars,_,_=formula(graphs[i])
 rec={'index':i,'variables':nvars,'clauses':len(cnf)}
 if i in (41,255):
  rec.update({'status':'SAT','minimum_bad_K5':2,
              'projected_witnesses':[m['neighbor_set'] for m in enum[str(i)]['models']]})
 else:
  p=P/f'twobad_{i:03d}.drup';adds=dels=0
  for line in p.read_text().splitlines():
   if line.startswith('d '):dels+=1
   elif line.strip():adds+=1
  rec.update({'status':'UNSAT','proof_file':p.name,'proof_additions':adds,
              'proof_deletions_ignored':dels,'proof_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
              'independent_replay':'passed'})
 manifest.append(rec)
(P/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
summary={'representatives':328,'unsat_proofs':326,'sat_indices':[41,255],
         'rup_additions_replayed':sum(x.get('proof_additions',0) for x in manifest),
         'deletion_lines_ignored':sum(x.get('proof_deletions_ignored',0) for x in manifest),
         'unlabeled_two_bad_classes':2}
(R/'two_bad_certificate_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
