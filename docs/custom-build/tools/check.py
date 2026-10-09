#!/usr/bin/env python3
"""Check real guide links/assets, records, omissions and non-deployable examples."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import copy
import hashlib
import json
import re
import sys
from functools import lru_cache
import xml.etree.ElementTree as ET
import markdown
from bs4 import BeautifulSoup
from pdf_inputs import pdf_input_sha256

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
errors = []
counts = {'local_links': 0, 'images': 0, 'html_pages': 0}

def require(condition, message):
    if not condition:
        errors.append(message)

def load(name):
    return json.loads((ROOT / 'data' / name).read_text())

def manifest_errors(m):
    e = []
    if [x['id'] for x in m['purchases']] != [f'{i:02}' for i in range(1,15)]:
        e.append('Inventory must contain exactly IDs 01..14 once, in order')
    if m['identity']['voron_design_revision'] != '2.4R2':
        e.append('Design and kit revision fields are mixed')
    if m['readiness']['physical_machine_verified'] or m['readiness']['ready_to_commission_heaters'] or m['readiness']['ready_to_deploy_configuration']:
        e.append('Readiness falsely clears unresolved physical/electrical/config gates')
    for x in m['purchases']:
        if x['allocation']['actual_installed_pieces'] is not None:
            e.append(f'Actual installed count lacks physical evidence: {x["id"]}')
        n, a, b = x['package']['pieces_per_reported_unit'], x['allocation']['planned_installed_pieces'], x['allocation']['planned_surplus_pieces']
        if n is not None and a is not None and b is not None and n*x['purchase']['reported_units'] != a+b:
            e.append(f'Package allocation does not balance: {x["id"]}')
    if m['main_path']['active_stock_alternatives']:
        e.append('Incompatible stock alternatives remain active')
    if (m['main_path']['xy_belt_mm'],m['main_path']['z_open_belt_mm'],m['main_path']['z_reduction_loop_mm']) != (6,9,6):
        e.append('Independent belt widths disagree with selected purchased motion path')
    clamps = next((x for x in m['purchases'] if x['id']=='10'), None)
    if clamps and (clamps['allocation']['planned_installed_pieces'],clamps['allocation']['planned_surplus_pieces']) != (2,2):
        e.append('Separate bottom clamps conflict with rigid integrated lower captures')
    return e

def cfg_errors(content):
    return [f'Active line {i}' for i,l in enumerate(content.splitlines(),1) if l.strip() and not l.lstrip().startswith('#')]

@lru_cache(maxsize=None)
def document(path):
    if path.suffix == '.md':
        return BeautifulSoup(markdown.markdown(path.read_text(),extensions=['extra','toc','sane_lists']),'html.parser')
    return BeautifulSoup(path.read_text(),'html.parser')

def check_links(path):
    soup = document(path)
    require(len([x['id'] for x in soup.select('[id]')]) == len(set(x['id'] for x in soup.select('[id]'))), f'Duplicate anchor: {path}')
    for tag in soup.select('a[href],img[src]'):
        attr = 'href' if tag.name=='a' else 'src'
        url = urlsplit(tag[attr])
        if url.scheme or tag[attr].startswith('//'):
            if tag.name=='img':
                errors.append(f'Guide image requires network: {path}: {tag[attr]}')
            continue
        target = (path.parent / unquote(url.path)).resolve() if url.path else path
        counts['local_links'] += 1
        if tag.name=='img':
            counts['images'] += 1
        require(target.exists(),f'Broken local link/asset: {path.relative_to(REPO)} -> {tag[attr]}')
        if target.exists() and url.fragment and target.suffix in ['.md','.html']:
            ids = {x['id'] for x in document(target).select('[id]')}
            require(unquote(url.fragment) in ids,f'Broken fragment: {path.relative_to(REPO)} -> {tag[attr]}')

def run():
    manifest = load('build-manifest.json')
    errors.extend(manifest_errors(manifest))
    questions = load('questions.json')
    gate_ids = {g['id'] for g in questions}
    require(len(gate_ids)==len(questions),'Duplicate gate IDs')
    chapters = sorted((ROOT/'chapters').glob('*.md'))
    require(len(chapters)==10,'All ten assembly phases must exist')
    for g in questions:
        p=ROOT/g['location']
        require(p.exists() and re.search(r'\b'+re.escape(g['id'])+r'\b',p.read_text()),f'Gate lacks immediate procedure location: {g["id"]}')
    for x in manifest['purchases']:
        require(set(x['unresolved_fields']) <= gate_ids,f'Unknown gate for purchase{x["id"]}')
        require((ROOT/x['guide_location']).exists(),f'Missing procedure for purchase{x["id"]}')
        require(x['id'] in (ROOT/x['guide_location']).read_text(),f'Purchase{x["id"]} unaccounted in its chapter')
    crosswalk=load('crosswalk.json')
    indices=[]
    for x in crosswalk:
        indices.extend(range(x['pdf_index_start'],x['pdf_index_end']+1))
        require((ROOT/x['custom_location']).exists(),'Crosswalk replacement absent')
    require(indices==list(range(263)),'Crosswalk must cover all263 PDF indices exactly once')
    print_rows=load('printed-parts.json')
    source_index=load('source-file-index.json')
    for x in print_rows:
        omit=any(k in x['status'].lower() for k in ['omit','replaced'])
        require(not omit or x['quantity']==0,f'Omitted STL still activated: {x["filename"]}')
        require(x.get('source_revision') is not None,f'Print source revision absent: {x["filename"]}')
        source=x.get('source')
        if source in source_index:
            require(x['filename'] in source_index[source]['files'],f'Nonexistent printed-part source member: {source}:{x["filename"]}')
        require(source is not None,f'Printed-part source absent: {x["filename"]}')
    for f in (ROOT/'config').glob('*.cfg.example'):
        errors.extend(f'{f.name}: {e}' for e in cfg_errors(f.read_text()))
    require(len(list((ROOT/'config').glob('*.cfg.example')))==4,'Four distinct configuration worksheets required')
    lock=load('sources.lock.json')
    sources={x['id']:x for x in lock['sources']}
    for s in sources.values():
        require(bool(s.get('retrieved_at')) and bool(s.get('url')) and bool(s.get('license')),f'Source metadata incomplete:{s["id"]}')
        require(bool(s.get('commit')) or bool(s.get('sha256')),f'Source has no pin/hash:{s["id"]}')
        require(bool(s.get('hash_scope')),f'Source hash scope absent:{s["id"]}')
        if s.get('sha256'):
            require(bool(re.fullmatch('[0-9a-f]{64}',s['sha256'])),f'Invalid SHA256:{s["id"]}')
        if s.get('local_repository_path'):
            require(hashlib.sha256((REPO/s['local_repository_path']).read_bytes()).hexdigest()==s['sha256'],'Retained base manual hash mismatch')
    for a in lock['assets']:
        p=ROOT/a['path']
        require(p.exists() and hashlib.sha256(p.read_bytes()).hexdigest()==a['sha256'],f'Missing/changed asset:{a["path"]}')
        require(bool(a.get('license')) and bool(a.get('provenance')),f'Asset license/provenance absent:{a["path"]}')
        if p.suffix=='.svg':
            ET.parse(p)
    require({a['path'] for a in lock['assets']} == {p.relative_to(ROOT).as_posix() for p in (ROOT/'assets').iterdir() if p.is_file()},'Unaccounted asset in lock')
    for x in load('compatibility.json'):
        require(x['status'] in ['verified compatible','conditionally compatible','incompatible','unresolved'],f'Invalid compatibility status:{x}')
        require(bool(x.get('gates')),f'Compatibility missing evidence gate:{x["combination"]}')
    for p in list(ROOT.glob('*.md'))+chapters+sorted((ROOT/'reference').glob('*.md')):
        check_links(p)
    for p in (ROOT/'site').rglob('*.html'):
        counts['html_pages']+=1
        check_links(p)
    require(counts['html_pages']==23,'Expected22 site pages plus print edition')
    pdf=ROOT/'site/custom-build-guide.pdf'
    require(pdf.exists(),'PDF export absent')
    meta=ROOT/'site/pdf-export.json'
    if meta.exists():
        m=json.loads(meta.read_text())
        require(hashlib.sha256((ROOT/'site/print.html').read_bytes()).hexdigest()==m['print_html_sha256'],'PDF stale after source changes')
        require(pdf_input_sha256(ROOT/'site')==m.get('input_sha256'),'PDF stale after HTML, stylesheet or illustration changes')
        require(hashlib.sha256(pdf.read_bytes()).hexdigest()==m['pdf_sha256'],'PDF file hash differs from export record')
    else:
        errors.append('PDF export evidence metadata absent')
    # A few deliberate bad inputs ensure the contradiction checks actually reject them.
    bad=copy.deepcopy(manifest);bad['purchases'].pop()
    require(bool(manifest_errors(bad)),'Negative inventory test failed')
    bad=copy.deepcopy(manifest);bad['purchases'][9]['allocation']['planned_installed_pieces']=4
    require(bool(manifest_errors(bad)),'Negative clamp contradiction test failed')
    bad=copy.deepcopy(manifest);bad['readiness']['ready_to_commission_heaters']=True
    require(bool(manifest_errors(bad)),'Negative readiness test failed')
    require(bool(cfg_errors('# example\n[extruder]\n')),'Negative deployable cfg test failed')
    report={'counts':counts,'purchase_entries':len(manifest['purchases']),'crosswalk_pdf_indices':len(indices),'sources':len(sources),'gates':len(gate_ids),'assets':len(lock['assets']),'printed_parts':len(print_rows),'negative_checks':4,'errors':errors}
    print(json.dumps(report,indent=2))
    if errors:
        raise SystemExit(1)

if __name__=='__main__':
    run()
