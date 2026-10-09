# Validation results

Reviewed on October 9, 2026. This is a completed, illustrated documentation
project with hardware verification gates. It is **not a physically validated
or heater-ready printer configuration**. No firmware, motion, heating or
physical assembly was performed.

## Actual local results

- `python3 docs/custom-build/tools/reference.py`: passed; generated records for
  all **14 purchases**, **79 sources**, **31 open gates**, **23 compatibility
  interactions**, **200 printed-parts rows**, and **84 licensed local assets**.
- `python3 docs/custom-build/tools/build.py`: passed; **22 navigable pages** and
  a complete print edition, with local assets, responsive layout and print CSS.
- `python3 docs/custom-build/tools/check.py`: passed with **zero errors**;
  **1,260 local links**, **93 image references**, all **263 upstream PDF indices**
  covered once, purchase dispositions and omitted stock parts checked, exact
  source filenames checked against pinned repository/archive inventories,
  asset hashes/licenses checked, and all four configuration examples confirmed
  entirely commented. Four deliberately invalid inventory/allocation/readiness/
  configuration inputs were rejected. Export metadata checks the PDF hash and
  its HTML, stylesheet and local-illustration input hash.
- `python3 docs/custom-build/tools/browser_check.py`: passed; eight representative
  pages at **1440 × 1000** and **390 × 844**, **16 viewport checks, zero failures**.
  Images loaded and the document body had no horizontal overflow. Desktop and
  mobile screenshots were inspected, including the motion and toolhead chapters.
- `python3 docs/custom-build/tools/export_pdf.py`: passed using installed Chrome;
  exported an A4 PDF from the complete local print edition. Representative pages
  were visually inspected: contents, bed, toolhead, wiring and printed-parts
  tables. The PDF opens, every page has text, and images are required to decode
  before export. The current file and input hashes are in
  [the export record](site/pdf-export.json).
- Three independent documentation reviews examined motion, bed/toolhead and
  electrical/software safety interactions. Remaining physical dependencies are
  explicit gates before their affected steps. Final review corrected bed dry-fit
  and toolhead-return ordering, and requires X/Y homing before commanded axis moves.
- Original upstream manual, CAD, STLs and license were retained. Private order
  documents, payment information, addresses and account credentials are excluded.

## Versions and corrected failures

Python **3.10.12**, Python-Markdown **3.3.7**, Beautiful Soup **4.12.2**, Soup Sieve
**2.3.1**, Playwright **1.57.0**, PyMuPDF **1.27.2.2**, and Chrome
**145.0.7632.45** were used. The base dependency versions are pinned in
`requirements.txt`; browser/export dependencies are documented separately.

Initial static validation found two missing original-SVG provenance fields;
the source normalizer was corrected. Initial browser review found mobile
overflow in the toolhead page; wrapping was corrected and all 16 checks passed
on rerun. Adding the report exposed an output-artifact link mapping error;
the builder now maps source Markdown's `site/` links correctly into HTML.
The restricted sandbox prevented Chrome startup; approved browser
execution outside that sandbox completed both browser review and PDF export.
These failures are recorded rather than treated as passing runs.

## Publication

The actual new fork is [obnauticus/Voron-2](https://github.com/obnauticus/Voron-2),
branch `Voron2.4`, derived from upstream commit
`a192410e27ea345644ae5c4b29b4c9c40cbe1a73`.
The first complete guide push was verified at
[`772e80b1752706e63a07fdd9aff8f9bb6e0cea50`](https://github.com/obnauticus/Voron-2/commit/772e80b1752706e63a07fdd9aff8f9bb6e0cea50).
Its [Pages deployment](https://github.com/obnauticus/Voron-2/actions/runs/37896359601)
completed successfully. The served index and PDF downloaded over HTTPS and
matched the local files' SHA-256 hashes. Subsequent documentation edits must
repeat the applicable build/export/check commands before pushing.

The live [HTML guide](https://obnauticus.com/Voron-2/custom-build/site/) and
[PDF](https://obnauticus.com/Voron-2/custom-build/site/custom-build-guide.pdf)
use this account's existing Pages domain. Pages publishes `Voron2.4` and `/docs`;
repository visibility and account domain configuration were not changed.

The initial guide push was rejected because the existing OAuth grant lacks
permission to create an active Actions workflow. The workflow is retained as
an inactive example; publication uses the checked committed `/docs` output.
No broader authorization grant or account-domain change was requested.
This branch-publication process serves committed output; GitHub's successful
deployment is separate from the locally executed custom documentation checks.

## Limits of these results

Static links, screenshots, PDF layout and consistency checks do not prove
physical assembly compatibility, electrical ratings, protective-earth safety,
probe performance or print quality. The delivered kit size/batch/PCB revisions,
Wings package and support map, double-shear shaft engagement, UHF duct/cartridge
geometry, heater startup load and complete electrical path remain unverified.
An embedded-magnet MRW bed is manufacturer-incompatible with the selected
Cartographer scan path; identify the delivered bed before that path proceeds.
All **31 hardware/evidence gates remain open**. Complete independent assembly
work, but stop before each blocked operation. All configuration examples remain
non-deployable until their hardware and measured values are resolved.
