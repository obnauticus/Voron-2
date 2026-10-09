# Rules for the unofficial custom build guide

Scope: `docs/custom-build/`, its generated site, and the README link. Preserve
upstream history, CAD, STLs, manuals, licenses and attribution. Never submit this
customization to upstream, change visibility, or publish private order material.

## Evidence and maintenance

- Keep Voron design revision, LDO kit revision/batch, PCB revision, product
  revision and firmware generation in separate fields. A current store listing
  does not establish shipped hardware. Purchase evidence does not establish fit.
- Account for all fourteen purchase IDs. Separate sets, pieces per set, planned
  installed pieces, actual installed pieces and surplus. Unknown means `null`.
- Consult official assembly instructions, CAD and printed parts. Pin repository
  commits, document versions, retrieval dates and SHA-256 hashes in the source
  lockfile. Record printed pages separately from zero-based PDF indices.
- Render and inspect diagrams for geometry, belt paths, hardware stacks and
  connector orientation. Text extraction alone is insufficient.
- Do not invent dimensions, torques, pin mappings, current ratings, heater
  limits, device IDs, offsets, travel limits, PID values or tuning results.
- Classify each interaction as verified compatible, conditionally compatible,
  incompatible or unresolved; identify the hardware revision and evidence.
- Put verification gates immediately BEFORE affected steps. Independent phases
  can proceed. Unknown electrical ratings block heater commissioning.
- Keep changes from stock visible with KEEP / REPLACE / OMIT / ADD. Never ask
  readers to build stock hardware that this guide immediately removes.
- Third-party images and PDFs require independent reuse permission. Link when
  unknown; never assume the upstream license covers vendor assets. Original
  schematics must say they are schematic and not dimensional assembly drawings.

## Safety

- Preserve manufacturer mains, protective-earth, thermal and hotend warnings.
  Software tests do not certify electrical safety.
- Identify PCB revisions before firmware targets and pinouts. Nitehawk SB is
  USB, not CAN. Keep original SB and SB V2 configurations separate.
- Do not transfer the historical Rapido/Octopus workaround to another board.
  A software power limit does not resolve instantaneous current overload.
- Rigid Z joints require manual squaring and a full-travel binding inspection
  before motors or quad gantry leveling. Keep the gantry supported when unpowered.
- Example configurations must remain wholly commented and non-deployable until
  evidence and measurements have been resolved. Do not flash, move, or heat a
  printer while validating documentation.

## Validation before publication

Run the documented build/check commands. Check internal links and fragments,
assets, inventory coverage, page crosswalk coverage, safety gate references,
source hashes, printed-part paths and contradictions in dispositions. Inspect
representative desktop, mobile and printed pages. Test PDF export when available.
Report actual failures and distinguish static documentation checks from physical
assembly validation. Update the validation report after changed inputs.
