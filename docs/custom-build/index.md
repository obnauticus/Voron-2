# LDO Voron 2.4R2 — integrated custom assembly guide

**Unofficial derivative, prepared 2026-10-09. Readiness: documentation complete
with hardware verification gates; not a physically validated machine configuration.**

This is the chronological build path for the fourteen reported purchases. Start
here and follow the chapters in order. The target is provisionally 350-class,
Voron design **2.4R2**, LDO kit **Rev D-family, unverified**. The current West3D
D+ listing is a research lead. It does not establish the size, batch, electronics,
or options in the purchased kit.

The [original Voron assembly manual](https://github.com/VoronDesign/Voron-2/blob/a192410e27ea345644ae5c4b29b4c9c40cbe1a73/Manual/Assembly_Manual_2.4r2.pdf)
remains authoritative for unchanged mechanical details. This guide replaces its
affected steps before assembly. Source figures are labeled **STOCK REFERENCE**;
they do not depict the CNC upgrades. Vendor instructions stay linked where their
redistribution license is unknown. Local original schematics describe relationships,
not unverified dimensions or manufacturing geometry.

## Build in this order

1. [Inventory and evidence](chapters/01-inventory.md): identify the kit and allocate purchases.
2. [Printed parts and preparation](chapters/02-preparation.md): print retained parts and resolve interfaces.
3. [Frame, Z rails, deck and Z drives](chapters/03-frame-z.md).
4. [Modified gantry, titanium backers, Z supports and belts](chapters/04-motion.md).
5. [MRW bed, kinematics and Wings](chapters/05-bed.md).
6. [Rapido 2 Fiber UHF, StealthBurner, CNC carriage and Cartographer](chapters/06-toolhead.md).
7. [Electronics and cable routing](chapters/07-wiring.md).
8. [Software and configuration preparation](chapters/08-software.md).
9. [Pre-power, first start and calibration](chapters/09-commissioning.md).
10. [Enclosure, filament path and first print](chapters/10-panels-first-print.md).

## Gates are part of the procedure

**STOP at a gate before its affected step.** Continue independent chapters when
their prerequisites are satisfied. Closing a gate requires the named receipt
detail, board marking, manufacturer instruction, measurement, or physical check;
an assumption does not close it. No actual installed quantities or measurements
have been supplied. All allocations are plans, not claims of completed assembly.

The most consequential decisions are the bed's magnet arrangement, UHF duct and
mount geometry, clamp overlaps and rigid-joint alignment, actual PCB revisions,
and hotend startup load versus the complete electrical path. A blocked heater
gate prohibits heater commissioning even if other software checks pass.

## Build records

- [All fourteen purchase dispositions](reference/inventory.md) and [machine manifest](data/build-manifest.json).
- [Compatibility decisions](reference/compatibility.md).
- [Printed-parts matrix](reference/printed-parts.md).
- [Hardware and missing requirements](reference/hardware.md).
- [Every stock manual page mapped to this path](reference/crosswalk.md).
- [Unresolved questions and closure evidence](reference/questions.md).
- [Pinned sources and illustration provenance](reference/sources.md), [source lockfile](data/sources.lock.json).
- [Non-deployable configuration examples](reference/configuration.md).
- [Build commands and publication](README.md), [actual validation results](VALIDATION.md).

Upstream design and manual: Voron Design contributors, GPL-3.0. Original custom
Markdown, diagrams and tooling: GPL-3.0, modified 2026-10-09. See [attribution and
reuse terms](ATTRIBUTION.md). This documentation carries no warranty. Static
documentation checks do not validate physical fit, electrical safety, firmware,
or the completed printer.
