#!/usr/bin/env python3
"""Dependency/artifact preflight for a frozen Vine-code Stim circuit."""
from __future__ import annotations
import argparse,hashlib,json,shutil
from pathlib import Path
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('payload',type=Path); a=ap.parse_args(); p=json.loads(a.payload.read_text())
    f=Path(p.get('circuit_file',''))
    out={"stim_available":shutil.which('stim') is not None,"circuit_exists":f.is_file(),"expected_distance":p.get('expected_distance'),"full_checker_ready":False}
    if f.is_file():out['sha256']=hashlib.sha256(f.read_bytes()).hexdigest()
    out['reason']='archive internal filename and exact-distance executable are not frozen in this scout package'
    print(json.dumps(out,indent=2,sort_keys=True))
