#!/usr/bin/env python3
"""Export the built print edition using installed Chrome; no printer connection."""
from pathlib import Path
import argparse
import shutil
import hashlib
import json
from playwright.sync_api import sync_playwright
from pdf_inputs import pdf_input_sha256

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--browser", default=shutil.which("google-chrome"))
args = parser.parse_args()
if not args.browser:
    raise SystemExit("PDF export unavailable: install Chrome or pass --browser PATH")
source = ROOT / "site/print.html"
if not source.exists():
    raise SystemExit("Run tools/build.py first")
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=args.browser, headless=True, args=["--no-sandbox", "--disable-dev-shm-usage"])
    page = browser.new_page()
    page.goto(source.as_uri(), wait_until="load")
    page.evaluate("document.querySelectorAll('details').forEach(x => x.open = true)")
    page.evaluate("Promise.all([...document.images].map(x => x.decode().catch(() => {})))")
    failed_images = page.evaluate("[...document.images].filter(x => !x.complete || !x.naturalWidth).map(x => x.src)")
    if failed_images:
        raise SystemExit(f"PDF export aborted: missing illustrations {failed_images}")
    browser_version = browser.version
    page.pdf(path=str(ROOT / "site/custom-build-guide.pdf"), format="A4", print_background=True, display_header_footer=True,
             header_template="<span></span>", footer_template='<div style="font:8px sans-serif;width:100%;text-align:center">Unofficial custom LDO Voron · hardware gates remain open · <span class="pageNumber"></span>/<span class="totalPages"></span></div>')
    browser.close()
(ROOT / 'site/pdf-export.json').write_text(json.dumps({'browser':args.browser,'browser_version':browser_version,'print_html_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'input_sha256':pdf_input_sha256(ROOT/'site'),'pdf_sha256':hashlib.sha256((ROOT/'site/custom-build-guide.pdf').read_bytes()).hexdigest()},indent=2)+'\n')
print(ROOT / "site/custom-build-guide.pdf")
