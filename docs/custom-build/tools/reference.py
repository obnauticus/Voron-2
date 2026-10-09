#!/usr/bin/env python3
"""Regenerate readable reference tables from maintained JSON evidence records."""
from pathlib import Path
from urllib.parse import quote
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
DATA = ROOT / "data"
REF = ROOT / "reference"
REF.mkdir(exist_ok=True)
BASE = "a192410e27ea345644ae5c4b29b4c9c40cbe1a73"

def dump(name, value):
    (DATA / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")

def cell(value):
    if value is None:
        return "Unverified / unset"
    if isinstance(value, list):
        value = "; ".join(str(x) for x in value)
    if isinstance(value, dict):
        value = json.dumps(value, ensure_ascii=False)
    return str(value).replace("|", "\\|").replace("\n", " ")

def table(head, rows):
    return "\n".join(["| " + " | ".join(head) + " |", "| " + " | ".join(["---"] * len(head)) + " |"] + ["| " + " | ".join(cell(x) for x in row) + " |" for row in rows]) + "\n"

def write(name, text):
    (REF / (name + ".md")).write_text(text)

def generate():
    manifest = json.loads((DATA / "build-manifest.json").read_text())
    records = [json.loads(p.read_text()) for p in sorted(DATA.glob("*-research.json"))]
    sources = {}
    gates = {}
    interactions = []
    printed = {}
    assets = {}
    missing = []
    for record in records:
        for source in record.get("sources", []):
            source = dict(source)
            local_hint = source.get('research_local_path', source.get('local_research_file'))
            if local_hint and source.get('sha256'):
                source.setdefault('hash_scope', 'Exact retrieved file bytes: ' + Path(local_hint).name + '; not repository tree HTML')
            source.setdefault('hash_scope', 'exact retrieved document bytes' if source.get('sha256') else 'repository commit pin')
            if 'retrieved_content_url' not in source:
                url = source['url']
                if '/blob/' in url and url.startswith('https://github.com/'):
                    url = url.replace('https://github.com/', 'https://raw.githubusercontent.com/', 1).replace('/blob/', '/', 1)
                elif '/tree/' in url and local_hint and source.get('sha256'):
                    stem, pin = url.split('/tree/', 1)
                    document = 'README.md' if Path(local_hint).name == 'README.md' else Path(local_hint).name
                    url = stem.replace('https://github.com/', 'https://raw.githubusercontent.com/', 1) + '/' + pin + '/' + quote(document)
                source['retrieved_content_url'] = url
            # Scratch locations are useful privately, but not portable publication inputs.
            source.pop("research_local_path", None)
            source.pop("local_research_file", None)
            source.setdefault("license", source.get("reuse_terms", "Unverified reuse terms; link only"))
            sources[source["id"]] = source
        for gate in record.get("gates", record.get("unresolved", [])):
            gate = dict(gate)
            gate.setdefault("location", gate.get("chapter", "chapters/05-bed.md" if gate["id"].startswith("B") else "chapters/06-toolhead.md"))
            if isinstance(gate.get("blocks"), list):
                gate["blocks"] = "; ".join(gate["blocks"])
            gate["status"] = "open; not physically verified"
            gates[gate["id"]] = gate
        for interaction in record.get("compatibility", record.get("interactions", [])):
            item = dict(interaction)
            item["status"] = item["status"].replace("_", " ")
            item.setdefault("combination", item.get("id", "Unspecified interaction"))
            item.setdefault("sources", item.get("evidence", []))
            item.setdefault("gates", [item['gate']] if item.get('gate') else [])
            item.setdefault("reason", item.get('finding', "See the cited chapter and gate for the physical evidence still required."))
            interactions.append(item)
        for part in record.get("printed_parts", []):
            item = dict(part)
            item.setdefault("quantity", item.get("print_quantity"))
            item.setdefault("source_revision", item.get("commit"))
            if item.get('source_revision') == BASE:
                item.setdefault('source', 'upstream-voron2')
            item.setdefault("guidance", item.get("notes", "Use documented source guidance; verify the actual interface before printing."))
            printed[item["filename"]] = item
        for asset in record.get("original_assets", record.get("assets", [])):
            asset.setdefault('provenance', asset.get('description', 'Original guide relationship schematic; no vendor image traced and no dimensional fit claimed.'))
            assets[asset["path"]] = dict(asset)
        missing.extend(record.get("missing_requirements", []))
        missing.extend(record.get("additional_requirements", []))

    for p in sorted((ROOT / "assets").iterdir()):
        rel = p.relative_to(ROOT).as_posix()
        if rel not in assets:
            name = p.stem
            base = re.fullmatch(r"stock-p(\d+)", name)
            sb = re.fullmatch(r"sb-stock-p(\d+)", name)
            if not base and not sb:
                raise ValueError(f"Unaccounted local illustration: {rel}")
            page = int((base or sb).group(1))
            assets[rel] = {"path": rel, "license": "GPL-3.0", "source_id": "upstream-voron2-manual" if base else "stealthburner-manual", "printed_page": page, "pdf_index": page-1, "provenance": "Unmodified rendered STOCK reference page; does not depict custom upgrades."}
        assets[rel]["sha256"] = hashlib.sha256(p.read_bytes()).hexdigest()
    lock = {"schema_version": 1, "retrieved_at": "2026-10-09", "notes": "Repository commits are immutable pins. Mutable vendor documents are identified by retrieved byte hashes; link-only documents cannot be fully mirrored for offline reproducibility without reuse permission.", "sources": list(sources.values()), "assets": list(assets.values())}
    dump("sources.lock.json", lock)
    dump("questions.json", list(gates.values()))
    dump("compatibility.json", interactions)

    # Enumerate every current upstream print file, even omitted alternatives.
    for p in sorted((REPO / "STLs").rglob("*")):
        if not p.is_file() or p.suffix.lower() != ".stl":
            continue
        name = p.relative_to(REPO).as_posix()
        if name in printed:
            continue
        match = re.search(r"_x(\d+)(?:_|\.)", p.name, re.I)
        count = int(match.group(1)) if match else 1
        status = "required"
        qty = count
        note = "KEEP; upstream filename count and retained manual assembly. ABS guidance p4."
        if "Superceded_Parts/" in name:
            status, qty, note = "replaced/omit", 0, "Superseded upstream alternative; not the R2 main path."
        elif "/Test_Prints/" in name or "/Tools/" in name:
            status, qty, note = "optional", count, "Calibration or assembly aid; not an installed machine part."
        elif "/Z_Idlers/" in name or "/Z_Endstop/" in name:
            status, qty, note = "replaced/omit", 0, "CNC tensioners or Cartographer replace this function."
        elif "/Gantry/X_Axis/X_Carriage/" in name or "/Gantry/X_Axis/XY_Joints/" in name:
            status, qty, note = "replaced/omit", 0, "CNC carriage/live joints replace stock geometry, endstop and probe supports."
        elif "/Gantry/" in name and ("chain" in p.name or "cable" in p.name):
            status, qty, note = "unresolved", None, "Confirm retained chain/USB umbilical/backer clearance at M3/M6/E4 before selecting."
        elif "/Skirts/250/" in name or "/Skirts/300/" in name:
            status, qty, note = "replaced/omit", 0, "Wrong size for provisional 350 target; revisit only if I1 changes it."
        elif "/Skirts/" in name and ("mini12864" in p.name or "btt_knob" in p.name or "power_inlet_filtered" in p.name or "power_inlet_IECGS_1.2" in p.name):
            status, qty, note = "replaced/omit", 0, "Not the provisional LDO D-family display/inlet path; verify actual options E1/P2."
        elif "power_inlet_IECGS_1mm" in name:
            status, qty, note = "unresolved", None, "Required if actual inlet is LDO 1.0mm; verify E1/P2 before print."
        elif "fan_grill_open_optional" in name:
            status, qty, note = "optional", count, "Alternative open grille; not an additional installed pair."
        elif "/Electronics_Bay/Controller_Mounts/" in name or "rs25_psu" in name:
            status, qty, note = "replaced/omit", 0, "Provisional Leviathan replaces alternate controller and separate 5V PSU mounts."
        elif "/Electronics_Bay/Other_PS_Mounts/" in name or "raspberrypi_bracket" in name or "PSU_stabilizer" in name:
            status, qty, note = "unresolved", None, "Match actual PSU/host board revision before selecting E1."
        elif "lrs_200_psu" in name:
            status, qty, note = "unresolved", None, "Two brackets if actual LRS-200-24 confirmed; no PSU substitution assumed."
        elif "pcb_din_clip" in name:
            status, qty, note = "included by LDO", 4, "Rev D BOM claims four clips; verify delivered count and actual board brackets E1. File name x3 is stock count."
        elif "/Exhaust_Filter/" in name and p.name != "exhaust_filter_grill.stl":
            status, qty, note = "replaced/omit", 0, "Stock exhaust-fan assembly omitted; its fan ownership is not confirmed. LDO cover closes opening."
        elif "/Panel_Mounting/" in name and ("4mm" in p.name or "6mm" in p.name or "deck_support" in p.name):
            status, qty, note = "unresolved", None, "Choose one clip-thickness family after actual panel measurement F2/P2; filename gives count for chosen family."
        printed[name] = {"filename": name, "quantity": qty, "stock_quantity": count, "status": status, "source": "upstream-voron2", "source_revision": BASE, "guidance": note}

    # Supplement parts with documented included counts and exact source paths.
    ldo_commit = "8270e8cf6c7ba29a7fd11d143c287bd3af576934"
    for filename,qty,status,note in [
        ("STLs/nozzle_probe_ldo.stl",0,"replaced/omit","Cartographer Z homing omits kit nozzle Z endstop; keep supplied piece as surplus."),
        ("STLs/led_fan_pcb_spacer_x2.stl",2,"included by LDO","Two in Rev D BOM; verify carton and PCB fit."),
        ("STLs/cw2_offset_chain_anchor.stl",None,"unresolved","LDO original two-hole chain anchor; verify actual Nitehawk/routing/backer fit."),
        ("STLs/exhaust_cover.stl",1,"required","Seal unused exhaust with stock grill; no extra filter modification added."),
        ("STLs/handlebar_spacer_x4.stl",4,"optional","If actual included handles installed; M5x14 + hammerhead per LDO supplement."),
        ("STLs/z_rail_stop_x4.stl",4,"optional","Captive-rail safety aid; temporary stops needed while handling."),
        ("STLs/ldo_bestagon_insert.stl",1,"optional","Decorative kit insert only."),
        ("STLs/z_belt_cover_a_led.stl",2,"optional","Alternative A cover if LED wires route through Z motor opening; not added to stock covers."),
        ("STLs/Purge Bucket/brush_holder_sheet_stop.stl",0,"replaced/omit","No automatic brass brush route across Cartographer coil; manual initial cleaning."),
        ("STLs/Purge Bucket/individual_sheet_stop.stl",None,"unresolved","MRW surface/Wings/probe envelope must determine sheet retention, B1/B5/T4.")]:
        printed['ldo:'+filename] = {"filename":filename,"quantity":qty,"status":status,"source":"ldo-supplement-repository","source_revision":ldo_commit,"guidance":note}

    rows = list(printed.values())
    dump("printed-parts.json", rows)
    write("inventory", "# Purchase disposition — all fourteen entries\n\nEvery installed count below is a **conditional plan**. Actual installation and package contents are unset. User-provided purchase verification is independent of installation compatibility.\n\n" + table(["ID / purchase","Evidence / variant","Units / package pieces","Planned installed / surplus","Disposition and gate","Build location"], [[f'**{x["id"]}** {x["name"]}', x['purchase']['evidence_status']+'; '+x['purchase']['technical_variant'], f'{x["purchase"]["reported_units"]} {x["purchase"]["unit"]}; {cell(x["package"]["pieces_per_reported_unit"])} pieces/unit', f'{cell(x["allocation"]["planned_installed_pieces"])} / {cell(x["allocation"]["planned_surplus_pieces"])}; '+ '; '.join(x['allocation']['surplus_notes']), x['disposition']+'; '+ ' '.join(x['unresolved_fields']), f'[Procedure](../{x["guide_location"]})'] for x in manifest['purchases']]) + '\nWings remain `2x` with two possible interpretations (two pieces or two two-piece sets). #10 is two top and two bottom clamps: bottoms surplus under the rigid-joint plan. #11 may include four extra clamps; plan two front uppers and two surplus after package/fit verification M8. The original LDO bonded bed remains intact as surplus. See [machine-readable manifest](../data/build-manifest.json).\n')
    write("compatibility", '# Compatibility register\n\nStatuses apply to the exact named combination. Advertised nominal fit is not physical validation. All actual delivered PCB/product revisions remain unverified unless explicitly identified. No combined machine arrangement is claimed physically tested.\n\n' + table(['Combination','Status','Hardware revision','Evidence / reason','Gates'], [[x['combination'],x['status'],x.get('hardware_revision'),x.get('reason')+' Sources: '+', '.join(x.get('sources',[])),x.get('gates')] for x in interactions]))
    write("questions", '# Unresolved questions and verification gates\n\nAll gates are open at publication because no delivered-hardware inspection or physical measurement was supplied. Close only with the precise evidence, then update the manifest, affected chapter and validation record. Continue independent work; stop before the affected operation.\n\n'+table(['Gate','Evidence needed','Affected operation / block','Procedure'],[[g['id'],g.get('evidence_needed'),g.get('affected_steps',g.get('blocks'))+'; '+g.get('blocks',''),f'[Before step](../{g["location"]})'] for g in gates.values()])+'\nAssembly gaps block only affected subassemblies. Missing board/load/cable/fuse/PE evidence blocks electrical commissioning; missing offsets and travel checks blocks calibration. A software limit is not evidence of safe electrical hardware.\n')
    write("printed-parts", '# Printed-parts matrix\n\nThe filenames are exact source members. Current upstream files, including unused sizes and alternatives, are accounted for. Quantity is the planned print/installed-piece count, not number of files. `null` means resolve first; a suffix quantity only applies if that alternative is selected. Included-by-LDO means the supplier BOM says it is provided, not that this carton was counted.\n\nUpstream functional-print guidance: ABS, 0.2 mm layers, forced 0.4 mm extrusion width, 40% infill, 4 walls, and 5 top/bottom layers (manual p4). Honor part-specific translucent/opaque guidance for LEDs and any verified vendor instructions. STEP members are not print-ready STLs. No standard HF cartridge is activated for the UHF purchase.\n\n'+table(['Exact filename','Planned qty','Disposition','Pinned source revision','Guidance / gate'],[[f'`{x["filename"]}`',x['quantity'],x['status'],str(x.get('source_revision') or x.get('commit') or 'source lock'),x.get('guidance')] for x in rows]))
    write("sources", '# Source lock and illustration provenance\n\nSources retrieved 2026-10-09. Repository links pin exact commits; mutable web/PDF URLs are identified by byte SHA-256 and document version. Third-party link-only material is not vendored. PDF index is **zero-based**; leaf is index+1; printed page may differ or be absent. Full page mappings and inspection records are in [sources.lock.json](../data/sources.lock.json).\n\n'+table(['ID / exact URL','Commit or document version','Retrieved','SHA-256','Reuse terms'],[[f'[{s["id"]}]({s["url"]})',s.get('commit') or s.get('version') or 'Unversioned; snapshot hash',s.get('retrieved_at'),f'`{s.get("sha256","Repository commit pin")}`',s.get('license')] for s in sources.values()])+'\n## Local illustration assets\n\n'+table(['Path','Source / page','License / provenance','SHA-256'],[[f'`{a["path"]}`',a.get('source_id','Original guide schematic')+ (f'; printed p{a["printed_page"]}, PDF index{a["pdf_index"]}' if 'printed_page'in a else ''),str(a.get('license'))+'; '+a.get('provenance',''),f'`{a["sha256"]}`'] for a in assets.values()]))
    configs = sorted((ROOT/'config').glob('*.cfg.example'))
    write("configuration", '# Non-deployable configuration examples\n\nEvery line is commented. Examples document a specific candidate hardware/firmware generation and deliberately omit unknown IDs, offsets, PID and travel values. They cannot be used as printer.cfg. A board-revision gate comes before selecting a sample; an electrical gate comes before connecting or heating.\n\n'+ '\n'.join(f'- [{p.name}](../config/{p.name}) — read its target and prerequisites before selecting.' for p in configs)+'\n\nDo not mix original SB RP2040 pins with SB V2 STM32G0 pins, old Cartographer Classic directives with the new Survey plugin, or F446 firmware headers with Leviathan V1.3 H743. Follow [software](../chapters/08-software.md) after its gates.\n')
    hardware = json.loads((DATA / 'hardware.json').read_text())
    dump('missing-parts.json', missing)
    write('hardware', '# Hardware, wiring and missing requirements\n\nPurchase inventory stays separate from additional requirements. Package titles are not a delivered-content audit. Exact verified stacks, orientations and warnings are in the phase chapters; unknown fasteners, connector views and ratings block the affected operation.\n\n' + table(['System','Parts / quantities','Verification','Ownership','Gates'], [[x[k] for k in ['system','parts_quantities','verification','ownership','gates']] for x in hardware]) + '\n## Additional requirements and optional conveniences\n\nRequired but not confirmed owned means inventory or acquire only after its interface gate is resolved. Optional alternates are not active main-path requirements and do not add to the fourteen reported purchases.\n\n' + table(['Item','Quantity','Classification','Gate'], [[x['item'],x.get('quantity'),x.get('classification',x.get('status')),x.get('gate')] for x in missing]))
    crosswalk = json.loads((DATA / 'crosswalk.json').read_text())
    write('crosswalk', '# Stock-to-custom page and step crosswalk\n\nPinned manual: 2023-07-04, upstream commit a192410e27ea345644ae5c4b29b4c9c40cbe1a73. Every PDF leaf is covered exactly once. Printed pages and zero-based PDF indices are recorded separately; final index 262 is an unnumbered back cover. REPLACE and OMIT instructions are not active in the custom path.\n\n' + table(['Printed stock pages','PDF indices','Phase / stock step','Action','Custom replacement'], [[f'{x["printed_page_start"]}–{x["printed_page_end"]}'+(' + unnumbered cover' if x['unnumbered_indices'] else ''),f'{x["pdf_index_start"]}–{x["pdf_index_end"]}',x['phase']+'; '+x['stock_step'],x['disposition'],f'[Procedure](../{x["custom_location"]}); '+x['replacement']] for x in crosswalk]))
    print(f'Generated references: {len(manifest["purchases"])} purchases, {len(sources)} sources, {len(gates)} gates, {len(interactions)} interactions, {len(rows)} print rows, {len(assets)} assets')

if __name__ == '__main__':
    generate()
