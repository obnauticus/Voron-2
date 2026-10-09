#!/usr/bin/env python3
"""Inspect real rendered guide pages at desktop/mobile sizes with installed Chrome."""
from pathlib import Path
import json
import shutil
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
OUT=Path('/tmp/voron-guide-browser-qa')
OUT.mkdir(exist_ok=True)
pages=['index.html','chapters/04-motion.html','chapters/05-bed.html','chapters/06-toolhead.html','chapters/07-wiring.html','chapters/09-commissioning.html','reference/inventory.html','reference/printed-parts.html']
rows=[]
with sync_playwright() as p:
    browser=p.chromium.launch(executable_path=shutil.which('google-chrome'),headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
    for width,height in [(1440,1000),(390,844)]:
        page=browser.new_page(viewport={'width':width,'height':height})
        for name in pages:
            page.goto((ROOT/'site'/name).as_uri(),wait_until='load')
            page.evaluate("document.querySelectorAll('img').forEach(x=>x.loading='eager')")
            page.evaluate("Promise.all([...document.images].map(x=>x.decode().catch(()=>{})))")
            failed=page.evaluate("[...document.images].filter(x=>!x.complete||!x.naturalWidth).map(x=>x.src)")
            overflow=page.evaluate('document.documentElement.scrollWidth>innerWidth')
            assert not failed,(name,failed)
            assert not overflow,(name,width,'horizontal body overflow')
            path=OUT/(str(width)+'-'+name.replace('/','-')+'.png')
            page.screenshot(path=str(path))
            rows.append({'page':name,'width':width,'images_loaded':True,'body_overflow':False,'screenshot':str(path)})
        page.close()
    browser.close()
(OUT/'results.json').write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps({'pages':len(pages),'viewport_checks':len(rows),'failures':0,'output':str(OUT)},indent=2))
