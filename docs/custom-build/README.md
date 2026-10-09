# Build, check, browse and export

Read [the guide entry point](index.md). The output is a portable static site with
local illustrations, a responsive navigation menu and a complete print edition.
It needs no server, CDN, account or network to browse after building. Manufacturer
manuals linked for uncertain reuse permission still require access to their source.

## Reproducible commands

From repository root with Python 3.10 or newer (validated with 3.10.12):

```sh
python3 -m venv docs/custom-build/.venv
docs/custom-build/.venv/bin/pip install -r docs/custom-build/requirements.txt
docs/custom-build/.venv/bin/python docs/custom-build/tools/build.py
docs/custom-build/.venv/bin/python docs/custom-build/tools/check.py
```

Open `docs/custom-build/site/index.html` in a browser, or serve it locally:

```sh
python3 -m http.server 8000 --directory docs/custom-build/site
```

The data/source Markdown are authoritative. To edit a purchase allocation,
change `data/build-manifest.json` and the corresponding chapter; update the
reference tables with `python3 docs/custom-build/tools/reference.py`, rebuild
and check. Research records retain the evidence behind the lockfile and gates.
Do not refresh a dependency or source commit without reviewing the resulting
changed geometry, instructions and licenses.

## PDF export and visual checks

The base dependency set builds/checks HTML. PDF export and browser QA additionally
use Playwright 1.57.0 and an installed Chrome; no browser download is implicit.

```sh
docs/custom-build/.venv/bin/pip install playwright==1.57.0
docs/custom-build/.venv/bin/python docs/custom-build/tools/export_pdf.py
docs/custom-build/.venv/bin/python docs/custom-build/tools/browser_check.py
```

The PDF is `site/custom-build-guide.pdf`. The export uses print CSS, local fonts
and local images. If Chrome cannot run in the environment, the command fails
explicitly; report export unavailable instead of claiming success. Regenerating
the upstream reference PNGs also needs PyMuPDF 1.27.2.2:

```sh
docs/custom-build/.venv/bin/pip install PyMuPDF==1.27.2.2
docs/custom-build/.venv/bin/python docs/custom-build/tools/render_stock.py
```

To regenerate the separately licensed StealthBurner figures too, supply the
pinned manual downloaded from the source lockfile:
`python3 docs/custom-build/tools/render_stock.py --stealthburner-manual PATH`.
Without that option the committed StealthBurner figures are retained.

See [VALIDATION](VALIDATION.md) for the actual versions, command outcomes and
visual review performed for this revision. Rebuilding unchanged content does
not mean a physical printer was assembled or tested.

## GitHub publication

The actual parent fork is [obnauticus/Voron-2](https://github.com/obnauticus/Voron-2),
branch `Voron2.4`, preserving upstream history. The custom guide and generated
HTML/PDF are committed in that branch. No upstream pull request is part of this
project. GitHub Pages publishes the committed output from `Voron2.4` and `/docs`;
`docs/index.html` points to the complete site and `docs/.nojekyll` preserves it
as static output. Run the documented build, PDF export and checks **before each
push**; this publication mode does not run the custom checker remotely.
Its actual deployment state and URL are recorded in the validation report only
after verified. Do not change repository visibility or account domain settings.

The current GitHub authorization rejected an active Actions workflow because
it lacks `workflow` scope. An optional pinned workflow is retained as
`tools/custom-guide.yml.example`, outside the active workflow directory.
If that grant is available later, install it in `.github/workflows/` and select
GitHub Actions publishing in Pages settings. It installs the pinned dependencies,
builds/checks the committed PDF and HTML, then deploys. For source-branch Pages
configuration, see [GitHub's Pages API documentation](https://docs.github.com/en/rest/pages/pages).

For a local derivative without an authenticated fork, the remaining publication
procedure would be: fork `VoronDesign/Voron-2` in the intended account, set that
fork as `origin`, verify `upstream` points to VoronDesign, push `Voron2.4`, then
enable Pages if desired. This session's actual state supersedes that fallback.
