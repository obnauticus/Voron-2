# Attribution and asset licenses

This is an **unofficial custom guide**, modified 2026-10-09 for the reported
purchases. Voron Design, LDO, Phaetus, Cartographer, Mandala Rose Works and
Vitalii3D have not reviewed or endorsed the combined assembly.

The upstream repository remains intact at base commit
`a192410e27ea345644ae5c4b29b4c9c40cbe1a73`, branch `Voron2.4`. Its original
CAD, STLs, PDF, README attribution and GPL-3.0 LICENSE are preserved.
There was no editable Markdown/InDesign manual source in the inspected tree;
the custom source is maintained Markdown rather than a modified extracted PDF.

| Local asset family | Author/source | Reuse basis and limits |
| --- | --- | --- |
| `stock-pNNN.png` | Voron Design project, retained `Manual/Assembly_Manual_2.4r2.pdf` | Rendered unmodified reference pages from the GPL-3.0 repository, cited by printed page and zero-based PDF index; original attribution appears in each page. They show STOCK hardware, not the custom CNC assembly. |
| `sb-stock-pNNN.png` | Voron Design project, separate StealthBurner commit `8bcb9c246fac19d8ac03931ef97fa07c5e5f0f2b`, manual version 2023-07-07 | Separately checked GPL-3.0 repository source, rendered stock CW2/SB reference pages. These figures do not establish UHF compatibility. |
| `motion-*.svg`, `bed-*.svg`, `toolhead-*.svg`, `electronics-*.svg` | Original custom documentation schematics, 2026 | GPL-3.0; labeled non-dimensional relationships or conditional plans. They are not manufacturing drawings or proof of fit. |
| Custom Markdown, Python tooling, stylesheet and generated HTML/PDF | Custom guide derivative, 2026 | GPL-3.0 with upstream attribution; no warranty. Maintained source included in this repository. |
| Store photos, Vitalii/MRW/Phaetus PDF diagrams, LDO web images | Their respective manufacturers | No blanket permission inferred. Source PDFs/images remain linked, not redistributed, where reuse terms are unknown or reserved. Private research scratch copies are not committed. |

LDO documentation's retrieved page metadata marks its content license `alr`
(all rights reserved). Its repositories have separately checked licenses.
Repository licenses are recorded per source in [the lockfile](data/sources.lock.json);
they do not extend to other websites. File hashes and each local illustration's
provenance are recorded there as well. New assets must be reviewed individually.

The installed upstream LICENSE is at repository root. The built site includes
an identical `LICENSE.txt`. The complete corresponding custom source is this
directory. Static checks do not certify physical safety, hardware compatibility
or fitness for a particular purpose.
