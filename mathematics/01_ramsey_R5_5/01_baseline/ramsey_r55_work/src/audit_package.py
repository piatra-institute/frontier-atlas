#!/usr/bin/env python3
"""Audit package manifests, certificate hashes, matrices, and report metadata."""
from __future__ import annotations
import hashlib, json, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

from itertools import combinations

def decode_graph6_42(line: bytes) -> list[int]:
    s=line.strip(); vals=[b-63 for b in s]
    if not vals or vals[0] != 42: raise ValueError("expected order-42 graph6")
    bits=[]
    for v in vals[1:]: bits.extend((v>>sh)&1 for sh in (5,4,3,2,1,0))
    adj=[0]*42; q=0
    for j in range(1,42):
        for i in range(j):
            if bits[q]: adj[i] |= 1<<j; adj[j] |= 1<<i
            q += 1
    return adj

def extension_bad_count(adj: list[int], neighbours: set[int]) -> int:
    bad=0
    for S in combinations(range(42),4):
        edges=sum((adj[a]>>b)&1 for a,b in combinations(S,2))
        if edges==6 and all(v in neighbours for v in S): bad += 1
        if edges==0 and all(v not in neighbours for v in S): bad += 1
    return bad

def matrix_stats(rows: list[str]) -> dict:
    n=len(rows); edges=sum(rows[i][j]=='1' for i in range(n) for j in range(i+1,n)); badK=badI=0
    for S in combinations(range(n),5):
        e=sum(rows[a][b]=='1' for a,b in combinations(S,2))
        badI += (e==0); badK += (e==10)
    return {'edges':edges,'clique_K5s':badK,'independent_K5s':badI,'total_bad_K5s':badK+badI}

def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()

def check_manifest(path: Path, directory: Path, name_key: str, hash_key: str):
    rows = json.loads(path.read_text())
    failures=[]; total_bytes=0
    for row in rows:
        if name_key == '__extension__':
            p = directory / f"ext_{row['index']:03d}.drup"
        else:
            p = directory / row[name_key]
        if not p.is_file(): failures.append({'missing':str(p.relative_to(ROOT))}); continue
        total_bytes += p.stat().st_size
        got=sha(p); expected=row[hash_key]
        if got != expected: failures.append({'file':str(p.relative_to(ROOT)),'expected':expected,'got':got})
    return {'records':len(rows),'total_bytes':total_bytes,'failures':failures}

out={}
out['exact_extension']=check_manifest(ROOT/'proofs/manifest.json',ROOT/'proofs','__extension__','proof_sha256')
out['one_bad']=check_manifest(ROOT/'proofs/one_bad/manifest.json',ROOT/'proofs/one_bad','proof_file' if False else '__onebad__','sha256') if False else None
# one_bad manifest predates proof_file field; derive filenames from indices.
rows=json.loads((ROOT/'proofs/one_bad/manifest.json').read_text()); fails=[]; total=0
for row in rows:
    p=ROOT/'proofs/one_bad'/f"onebad_{row['index']:03d}.drup"; total += p.stat().st_size if p.exists() else 0
    if not p.exists(): fails.append({'missing':str(p.relative_to(ROOT))})
    elif sha(p)!=row['sha256']: fails.append({'file':str(p.relative_to(ROOT)),'expected':row['sha256'],'got':sha(p)})
out['one_bad']={'records':len(rows),'total_bytes':total,'failures':fails}
rows=json.loads((ROOT/'proofs/two_bad/manifest.json').read_text()); fails=[]; total=0; certified=0; sat_records=[]
for row in rows:
    if row.get('status') == 'SAT':
        sat_records.append({'index':row['index'],'witness_count':len(row.get('projected_witnesses',[]))})
        continue
    p=ROOT/'proofs/two_bad'/row['proof_file']; certified += 1; total += p.stat().st_size if p.exists() else 0
    if not p.exists(): fails.append({'missing':str(p.relative_to(ROOT))})
    else:
        got=sha(p)
        if got!=row['proof_sha256']: fails.append({'file':str(p.relative_to(ROOT)),'expected':row['proof_sha256'],'got':got})
out['two_bad']={'records':len(rows),'certified_unsat_records':certified,'sat_records':sat_records,'total_bytes':total,'failures':fails}
# Independently verify all four projected SAT witnesses by direct 4-subset enumeration.
graph_lines=[x for x in (ROOT/'data/r55_42some.g6').read_bytes().splitlines() if x.strip()]
witness_checks=[]
for row in rows:
    if row.get('status') != 'SAT': continue
    adj=decode_graph6_42(graph_lines[row['index']])
    for j,w in enumerate(row.get('projected_witnesses',[])):
        count=extension_bad_count(adj,set(w))
        witness_checks.append({'base_index':row['index'],'witness':j,'new_degree':len(w),'bad_K5s':count,'passed':count==2})
out['two_bad']['direct_witness_checks']=witness_checks
if not all(x['passed'] for x in witness_checks): out['two_bad']['failures'].append({'invalid_SAT_witness':witness_checks})
out['near_radius']=check_manifest(ROOT/'proofs/near_radius_seq/manifest.json',ROOT/'proofs/near_radius_seq','proof_file','proof_sha256')

# Validate matrix shape, symmetry, diagonal, and binary alphabet.
matrices={}
for name in ('near43_graph1.matrix','near43_graph2.matrix'):
    p=ROOT/'data'/name; rows=[x.strip() for x in p.read_text().splitlines() if x.strip()]
    ok_shape=len(rows)==43 and all(len(r)==43 for r in rows)
    ok_alpha=all(set(r)<=set('01') for r in rows)
    ok_diag=ok_shape and all(rows[i][i]=='0' for i in range(43))
    ok_sym=ok_shape and all(rows[i][j]==rows[j][i] for i in range(43) for j in range(43))
    matrices[name]={'sha256':sha(p),'shape_43x43':ok_shape,'binary':ok_alpha,'zero_diagonal':ok_diag,'symmetric':ok_sym,**matrix_stats(rows)}
out['matrices']=matrices

# Input and report metadata.
out['key_files']={}
for rel in ('input_prompt.pdf','R55_RESEARCH_REPORT.pdf','data/r55_42some.g6','RESEARCH_REPORT.md','VERIFICATION_LOG.md'):
    p=ROOT/rel; out['key_files'][rel]={'bytes':p.stat().st_size,'sha256':sha(p)}
try:
    info=subprocess.run(['pdfinfo',str(ROOT/'R55_RESEARCH_REPORT.pdf')],check=True,capture_output=True,text=True).stdout
    pages=next(int(line.split(':',1)[1]) for line in info.splitlines() if line.startswith('Pages:'))
except Exception:
    pages=None
out['report_pages']=pages
out['all_manifest_hashes_pass']=all(not out[k]['failures'] for k in ('exact_extension','one_bad','two_bad','near_radius'))
out['proof_records_total']=sum(out[k]['records'] for k in ('exact_extension','one_bad','two_bad','near_radius'))
(ROOT/'results/package_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
if not out['all_manifest_hashes_pass'] or not all(all(v[k] for k in ('shape_43x43','binary','zero_diagonal','symmetric')) for v in matrices.values()):
    raise SystemExit(1)
