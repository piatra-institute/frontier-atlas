#!/usr/bin/env python3
from pathlib import Path
import csv,json,hashlib,sys
from collections import Counter
ROOT=Path('..');RES=ROOT/'results';PROOF=ROOT/'proofs'

def read_csvs(pattern):
 rows=[]
 for p in sorted(RES.glob(pattern)):
  with p.open() as f:rows.extend(csv.DictReader(f))
 return rows
# Bound 1 and 2 consolidated tables
for b in (1,2):
 rows=read_csvs(f'bad_bound{b}_*.csv');rows.sort(key=lambda r:int(r['index']))
 out=RES/f'bad_bound{b}_all.csv'
 with out.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
 summary={'bound':b,'graphs':len(rows),'satisfiable_count':sum(r['sat']=='True' for r in rows),
          'satisfiable_indices':[int(r['index']) for r in rows if r['sat']=='True']}
 (RES/f'bad_bound{b}_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
# Merge one-bad proof manifests
one=[]
for p in sorted((PROOF/'one_bad').glob('manifest_*.json')):one.extend(json.loads(p.read_text()))
one.sort(key=lambda x:x['index'])
(PROOF/'one_bad'/'manifest.json').write_text(json.dumps(one,indent=2)+'\n')
# Build complete near-radius manifest without changing proofs.
sys.path.insert(0,str(Path('.').resolve()))
from near_radius_certificates import formula
near=[]
for r in range(1,6):
 cs,nv,hist=formula(r);p=PROOF/'near_radius_seq'/f'radius_{r}.drup';adds=dels=0
 for line in p.read_text().splitlines():
  if line.startswith('d '):dels+=1
  elif line.strip():adds+=1
 near.append({'radius':r,'variables':nv,'clauses':len(cs),'proof_file':p.name,
              'proof_additions':adds,'proof_deletions_ignored':dels,
              'proof_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'histogram':hist,
              'independent_replay':'passed'})
(PROOF/'near_radius_seq'/'manifest.json').write_text(json.dumps(near,indent=2)+'\n')
# Top-level concise summary
summary={
 'known_42_representatives':328,
 'known_42_plus_complements':656,
 'one_vertex_extensions_found':0,
 'extensions_with_at_most_one_bad_K5':0,
 'representatives_with_at_most_two_bad_K5':[41,255],
 'two_bad_unlabeled_extension_classes':2,
 'near_miss_certified_exclusion_radius':5,
 'status':'Does not determine R(5,5); the known 42-vertex catalogue is incomplete.'
}
(RES/'research_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
