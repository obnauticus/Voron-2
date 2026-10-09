#!/usr/bin/env python3
"""Regenerate only licensed stock reference PNGs listed in the source lockfile."""
from pathlib import Path
import argparse
import hashlib
import json
import fitz

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--stealthburner-manual', type=Path, help='Local copy of the pinned SB PDF (needed to regenerate its figures)')
args = parser.parse_args()
lock = json.loads((ROOT / 'data/sources.lock.json').read_text())
sources = {s['id']: s for s in lock['sources']}
inputs = {'upstream-voron2-manual': REPO / 'Manual/Assembly_Manual_2.4r2.pdf'}
if args.stealthburner_manual:
    inputs['stealthburner-manual'] = args.stealthburner_manual
docs = {}
for id, path in inputs.items():
    expected = sources[id]['sha256']
    if hashlib.sha256(path.read_bytes()).hexdigest() != expected:
        raise SystemExit(f'Wrong source PDF hash: {id}')
    docs[id] = fitz.open(path)
count = 0
for asset in lock['assets']:
    if 'pdf_index' not in asset:
        continue
    source = asset['source_id']
    if source not in docs:
        continue
    docs[source][asset['pdf_index']].get_pixmap(matrix=fitz.Matrix(1.3,1.3)).save(ROOT / asset['path'])
    count += 1
print(f'Rendered {count} pinned reference pages; SB pages skipped unless --stealthburner-manual is provided')
