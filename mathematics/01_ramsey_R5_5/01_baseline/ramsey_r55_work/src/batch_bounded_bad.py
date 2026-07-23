#!/usr/bin/env python3
from pathlib import Path
from collections import Counter
import argparse,csv,json,time
import networkx as nx
from bounded_bad_extension import solve_bound

ap=argparse.ArgumentParser();ap.add_argument('bound',type=int);ap.add_argument('start',type=int);ap.add_argument('end',type=int);args=ap.parse_args()
Gs=list(nx.read_graph6('../data/r55_42some.g6'));rows=[];t=time.perf_counter()
for i in range(args.start,min(args.end,len(Gs))):
 sat,cost,S,nclauses,nvars,proof,ni,nk=solve_bound(Gs[i],args.bound)
 rows.append({'index':i,'bound':args.bound,'sat':sat,'cost':cost if cost is not None else '',
              'new_degree':len(S) if sat else '', 'neighbor_mask_hex':hex(sum(1<<v for v in S)) if sat else '',
              'cnf_clauses':nclauses,'cnf_variables':nvars,'i4':ni,'k4':nk})
out=Path(f'../results/bad_bound{args.bound}_{args.start}_{args.end}.csv')
with out.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
print(json.dumps({'bound':args.bound,'start':args.start,'end':args.end,'seconds':time.perf_counter()-t,
 'sat_count':sum(r['sat'] for r in rows),'sat_indices':[r['index'] for r in rows if r['sat']]},indent=2))
