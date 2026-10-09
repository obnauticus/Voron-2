# 1. Inventory and evidence

**Prerequisites:** unopened or safely disconnected kit and all upgrade packages.
**Tools:** ruler/calipers, camera for private inspection, labels and bins. No power.
**Parts:** one LDO kit (01), one three-pack of backers (02), one each of purchases
03–07, Wings notation `2x` (08), and one purchased set/item each of 09–14.
Use the [manifest](../data/build-manifest.json) for unit distinctions.

## I1 — verify the build target before size-dependent preparation

No order documents, photos, packing lists or relevant printer configurations
were found in the workspace filename/content search. This project did not access
email or past conversations. The six Vitalii selections are purchase evidence
provided by the user; the underlying private receipt is not redistributed.

1. Lay out the extrusions and measure them against the 350 BOM lead: ten
   A=470 mm, four B=530 mm, two C=450 mm, D=430 mm and E=340 mm. The
   [LDO 350 BOM directory](https://docs.ldomotors.com/en/voron/voron2/350_BOM/HOME)
   maps kit serial/batch to its BOM. Select the matching batch using the actual
   label; do not infer a serial from the order date.
2. Record the actual size, LDO revision and batch separately from design 2.4R2.
   If dimensions differ, stop printing 350 skirts and sizing belts. Retain the
   purchased MRW350 bed and resolve its fit before changing the target.
3. Identify rail labels, A/B motor model and shaft projection, X/Y belt width,
   Z belt width, PSU model, mains region, heater/fuse labels, and host options.
4. Read the mainboard and toolboard silkscreen on both sides while disconnected.
   Do not use a current product listing to pick firmware or pinouts. Photograph
   the boards privately and transcribe only technical model/revision fields.
5. Count each CNC package separately. Match the product-linked manual revision
   to the shipped part, and resolve conflicting package/fastener lists at the
   gate in [motion](04-motion.md) before assembling those joints.
6. Identify backer lengths; bed standard versus embedded magnets; heater and
   magnetic-sheet options; Wings pieces versus sets; Rapido revision/UHF/PT1000
   labels; CNC carriage 6/9 mm and UHF-extender contents; Cartographer firmware
   generation/interface. Leave unverified fields `null`.

## Label bins before assembly

**KEEP** the kit frame, rails, four stock Z reduction drives, compatible motion
belts, host/electronics and CW2/SB components after their revision gates.
**REPLACE** printed A/B drives, front idlers, live XY joints, Z upper idlers,
stock rigid-interface Z joint pieces, stock bed assembly, hotend and carriage.
**OMIT** the stock Omron/Klicky/TAP probe path, Hall endstop magnets, stock nozzle
Z endstop and their macros for the Cartographer homing path described later.
Keep unused kit parts in a labeled surplus bin; do not discard them.

**ADD** only requirements documented in the [hardware matrix](../reference/hardware.md).
An extra requirement is not a claimed purchase. Do not peel a bonded heater or
magnetic sheet off the supplied LDO bed for reuse on the MRW plate.

Completion: all fourteen IDs accounted for, package discrepancies recorded,
and no assumed PCB revision or private purchase data entered into Git. Unknown
details remain tracked in [the questions register](../reference/questions.md).

Sources: [West3D kit listing](https://west3d.com/products/ldo-v2-4-kit-in-stock),
[LDO batch BOM](https://docs.ldomotors.com/en/voron/voron2/350_BOM/HOME),
[Rev D BOM lead](https://docs.ldomotors.com/en/voron/voron2/350_BOM/Rev_D).
