#!/usr/bin/env python3
"""Build the offline custom guide from its maintained Markdown and local assets."""
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit
import argparse
import html
import json
import re
import shutil
import markdown
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
CHAPTERS = [ROOT / "index.md"] + sorted((ROOT / "chapters").glob("*.md"))
REFERENCES = sorted((ROOT / "reference").glob("*.md"))
OTHER = [ROOT / n for n in ["README.md", "ATTRIBUTION.md", "VALIDATION.md"]]
PAGES = CHAPTERS + REFERENCES + OTHER

def render(path):
    converter = markdown.Markdown(extensions=["extra", "toc", "sane_lists"])
    body = converter.convert(path.read_text())
    soup = BeautifulSoup(body, "html.parser")
    for tag in soup.select("a[href], img[src]"):
        attr = "href" if tag.name == "a" else "src"
        value = tag[attr]
        parsed = urlsplit(value)
        if not parsed.scheme and parsed.path:
            # Markdown may link to a generated artifact in site/. Its HTML
            # counterpart already lives inside site/, so remove that extra
            # directory without breaking the source Markdown link.
            try:
                generated = (path.parent / parsed.path).resolve().relative_to(SITE)
            except ValueError:
                pass
            else:
                import os
                relative = os.path.relpath(ROOT / generated, path.parent).replace("\\", "/")
                tag[attr] = urlunsplit(("", "", relative, parsed.query, parsed.fragment))
                parsed = urlsplit(tag[attr])
        if not parsed.scheme and parsed.path.lower().endswith(".md"):
            tag[attr] = urlunsplit(("", "", parsed.path[:-3] + ".html", parsed.query, parsed.fragment))
    for table in soup.select("table"):
        wrapper = soup.new_tag("div", attrs={"class": "table-scroll"})
        table.wrap(wrapper)
    for img in soup.select("img"):
        img["loading"] = "lazy"
    title = soup.find("h1").get_text(" ", strip=True) if soup.find("h1") else path.stem
    return title, str(soup), converter.toc

def link(path, current):
    import os
    return os.path.relpath(path.with_suffix(".html"), current.parent).replace("\\", "/")

def build():
    SITE.mkdir(exist_ok=True)
    # Clear generated HTML only; source documents/assets are never deleted.
    for old in SITE.rglob("*.html"):
        old.unlink()
    for folder in ["assets", "data", "config"]:
        source = ROOT / folder
        if source.exists():
            shutil.copytree(source, SITE / folder, dirs_exist_ok=True)
    shutil.copyfile(ROOT / "style.css", SITE / "style.css")
    shutil.copyfile(ROOT.parents[1] / "LICENSE", SITE / "LICENSE.txt")
    titles = {p: render(p)[0] for p in PAGES if p.exists()}
    combined = []
    for path in PAGES:
        if not path.exists():
            raise SystemExit(f"Missing required page: {path}")
        title, body, toc = render(path)
        depth = len(path.relative_to(ROOT).parts) - 1
        prefix = "../" * depth
        nav_parts = []
        for p in PAGES:
            current = 'aria-current="page"' if p == path else ''
            nav_parts.append(f'<li><a {current} href="{html.escape(link(p,path))}">{html.escape(titles[p])}</a></li>')
        nav = ''.join(nav_parts)
        page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} · Custom LDO Voron</title><link rel="stylesheet" href="{prefix}style.css"></head>
<body><a class="skip" href="#content">Skip navigation</a><header><a href="{prefix}index.html">LDO VORON / CUSTOM BUILD</a><span>Unofficial · provisional 350 · gates open</span></header>
<div class="layout"><aside><details open><summary>Build chapters & records</summary><nav aria-label="Guide"><ol>{nav}</ol></nav></details></aside>
<main id="content"><div class="readiness">Hardware checks remain open. A built guide does not certify a built printer.</div>
<details class="page-toc"><summary>On this page</summary>{toc}</details>{body}
<footer>Modified 2026-10-09 · Voron Design attribution retained · <a href="{prefix}ATTRIBUTION.html">GPL-3.0 & sources</a> · <a href="{prefix}print.html">Complete print edition</a></footer></main></div></body></html>'''
        target = SITE / path.relative_to(ROOT).with_suffix(".html")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(page)
        # Prefix local references and all IDs to keep the single-document edition valid.
        fragment = BeautifulSoup(body, "html.parser")
        slug = path.with_suffix("").relative_to(ROOT).as_posix().replace("/", "-")
        for tag in fragment.select("[id]"):
            tag["id"] = slug + "-" + tag["id"]
        for tag in fragment.select("a[href], img[src]"):
            attr = "href" if tag.name == "a" else "src"
            value = tag[attr]
            parsed = urlsplit(value)
            if parsed.scheme or value.startswith("//"):
                continue
            if not parsed.path:
                tag[attr] = "#" + slug + "-" + parsed.fragment
            else:
                import os
                normalized = os.path.relpath((path.parent / parsed.path).resolve(), ROOT)
                tag[attr] = normalized + (("#" + parsed.fragment) if parsed.fragment else "")
        for img in fragment.select("img"):
            img.attrs.pop("loading", None)
        combined.append(f'<article class="print-chapter" id="{slug}">{fragment}</article>')
    toc_links = ''.join(f'<li><a href="#{p.with_suffix("").relative_to(ROOT).as_posix().replace("/","-")}">{html.escape(titles[p])}</a></li>' for p in PAGES)
    (SITE / "print.html").write_text(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Complete custom Voron guide</title><link rel="stylesheet" href="style.css"></head><body class="print-edition"><main><h1>Custom LDO Voron guide — print edition</h1><p>Unofficial. Hardware verification gates remain open. Not a physically validated configuration.</p><ol>{toc_links}</ol>{''.join(combined)}</main></body></html>''')
    # Hosting-independent marker; GitHub Pages must not process these as Jekyll files.
    (SITE / ".nojekyll").write_text("")
    print(f"Built {len(PAGES)} pages + print edition into {SITE}")

if __name__ == "__main__":
    build()
