# Stock-to-custom page and step crosswalk

Pinned manual: 2023-07-04, upstream commit a192410e27ea345644ae5c4b29b4c9c40cbe1a73. Every PDF leaf is covered exactly once. Printed pages and zero-based PDF indices are recorded separately; final index 262 is an unnumbered back cover. REPLACE and OMIT instructions are not active in the custom path.

| Printed stock pages | PDF indices | Phase / stock step | Action | Custom replacement |
| --- | --- | --- | --- | --- |
| 1–11 | 0–10 | Inventory/print preparation; Intro, safety, print settings, hardware naming | KEEP | [Procedure](../chapters/02-preparation.md); Identify actual kit before size-dependent printing; no private receipts. |
| 12–19 | 11–18 | Frame; Cube and adjustable bed-support preparation | KEEP | [Procedure](../chapters/03-frame-z.md); 8 cube A pieces; 4 vertical B; bed supports remain adjustable before F1. |
| 20–20 | 19–19 | Frame/bed layout; Stock 130mm bed support spacing | REPLACE | [Procedure](../chapters/03-frame-z.md); F1 requires B2/B3 cold Wings map and deck/DIN-hole agreement before fixing supports. |
| 21–21 | 20–20 | Frame; Square frame | KEEP | [Procedure](../chapters/03-frame-z.md); Compare faces/diagonals before rails and after bed attachments. |
| 22–27 | 21–26 | Z rails; Overview, rail preparation and four Z rails | KEEP | [Procedure](../chapters/03-frame-z.md); Secure carriage stops; verify actual rail lubrication and spacing. |
| 28–29 | 27–28 | Deck/DIN rails; Stock deck and DIN fastening | KEEP / ADD gate | [Procedure](../chapters/03-frame-z.md); F1 closes before final deck: DIN hardware anchors into bed supports; F2 panel thickness discrepancy. |
| 30–31 | 29–30 | Lower Z drives; Orientation and heatsets | KEEP | [Procedure](../chapters/03-frame-z.md); Retained plastic reduction drives only. |
| 32–47 | 31–46 | Lower Z drives; Four stock reduction drives, short loops and feet | KEEP | [Procedure](../chapters/03-frame-z.md); 4 9mm20T shaft pulleys;4 6mm16T motor pulleys;4 6mm188 loops;8 spacer substitution. |
| 48–50 | 47–49 | Upper Z drives; Plastic upper Z idlers/tensioners | REPLACE | [Procedure](../chapters/04-motion.md); Purchase12,9mm top-adjusted CNC; gateM2 frame hardware. |
| 51–51 | 50–50 | Interlude; Historical page | OMIT | [Procedure](../chapters/01-inventory.md); No assembly operation. |
| 52–60 | 51–59 | Bed; Stock plate, adhesive heater/fuse, four-point screws and pass-through | REPLACE | [Procedure](../chapters/05-bed.md); 06/07/08 integrated; new heater/surface ownership unconfirmed; B1-B5 before affected step. |
| 61–61 | 60–60 | Interlude; Historical page | OMIT | [Procedure](../chapters/01-inventory.md); No assembly operation. |
| 62–63 | 61–62 | A/B geometry; Functional A/B orientation | KEEP | [Procedure](../chapters/04-motion.md); Stock topology reference only, not CNC fastener plan. |
| 64–80 | 63–79 | A/B drives/front idlers; Plastic heatsets, smooth idler stacks, motor mounts | REPLACE | [Procedure](../chapters/04-motion.md); 09/11 official PDF1.0; support-bearing shaft engagementM4; opposite single idler levels. |
| 81–81 | 80–80 | Interlude; Historical page | OMIT | [Procedure](../chapters/01-inventory.md); No assembly operation. |
| 82–87 | 81–86 | Gantry rear support; Rear E, A/B attachment and chain supports | REPLACE / ADD | [Procedure](../chapters/04-motion.md); Retain extrusion geometry; CNC screws gated; backers/routing before obstructing ends. |
| 88–88 | 87–87 | Y rails; Underside MGN9 rails | KEEP / ADD | [Procedure](../chapters/04-motion.md); 02 on opposite top surfaces; LDO second-from-end mounting hole note conditional actual rail. |
| 89–95 | 88–94 | Y/front gantry attachments; C extrusions/front plastic idlers and upper clips | REPLACE | [Procedure](../chapters/04-motion.md); CNC fasteners/orientationM5; #10/#11 upper-clamp allocationM8. |
| 96–100 | 95–99 | Live XY joints; Plastic XY stacks | REPLACE | [Procedure](../chapters/04-motion.md); 14 PDF1.1; spring/live-shaft levels; M3x3 versusM3x4 retention conflict. |
| 101–101 | 100–100 | X rail; Single front MGN12 on D | KEEP / ADD | [Procedure](../chapters/04-motion.md); 02 rear backerM3; carriage retained rail type verified. |
| 102–106 | 101–105 | X gantry attachment; Stock XY mounting hardware/endstop nut provisions | REPLACE | [Procedure](../chapters/04-motion.md); Use confirmed CNC mounts; M6 STEP support export/actual PCB; no stock bolt transfer. |
| 107–107 | 106–106 | Interlude; Historical page | OMIT | [Procedure](../chapters/01-inventory.md); No assembly operation. |
| 108–109 | 107–108 | Z suspension; Gantry location overview | KEEP | [Procedure](../chapters/04-motion.md); Supported gantry and independent Z belt widths. |
| 110–116 | 109–115 | Z joints/bottom capture; Stock spherical joints, lower clips, Hall magnet | REPLACE / OMIT | [Procedure](../chapters/04-motion.md); 13 complete rigid joint/bottom capture; separate #10 bottoms surplus; drawingM7. |
| 117–117 | 116–116 | Z tensioning preparation; Plastic top adjuster extension | REPLACE | [Procedure](../chapters/04-motion.md); Use12 documented adjusters; no stock four-turn preparation. |
| 118–121 | 117–120 | Z belt routing; Four loops and captures | KEEP / REPLACE | [Procedure](../chapters/04-motion.md); Keep inward teeth topology; replace capture hardwareM8, verify all9mm planes. |
| 122–122 | 121–121 | Gantry square; Square gantry | KEEP / ADD | [Procedure](../chapters/04-motion.md); Manual alignment and supported whole-Z binding checkM9 before power/QGL. |
| 123–123 | 122–122 | Interlude; Historical page | OMIT | [Procedure](../chapters/01-inventory.md); No assembly operation. |
| 124–127 | 123–126 | A/B belt topology; A/B path drawings | KEEP | [Procedure](../chapters/04-motion.md); Stock reference topology only; verified CNC belt planes before threading. |
| 128–128 | 127–127 | XY tensioners; Plastic idler four-turn prep | REPLACE | [Procedure](../chapters/04-motion.md); CNC front idler range; not stock adjustment counts. |
| 129–131 | 128–130 | Bare X carriage/belt start; Stock printed carriage halves/capture | REPLACE | [Procedure](../chapters/06-toolhead.md); T1 bare CNC carriage preparation executed during04 before belts;6mm width and rail screws. |
| 132–138 | 131–137 | A/B belt routing; Separate belt routes and stock access-bolt tip | KEEP / REPLACE | [Procedure](../chapters/04-motion.md); Preserve topology; do not remove CNC pins/retainers to imitate stock access step. |
| 139–141 | 138–140 | Carriage belt capture; Stock clamp/pivot fasteners | REPLACE | [Procedure](../chapters/06-toolhead.md); T1 two CNC clamps/correct hardware; no stock M3x30 through plastic. |
| 142–142 | 141–141 | Belt inspection; Rubbing check | KEEP / ADD | [Procedure](../chapters/04-motion.md); M10 complete backer/CNC/bed/toolhead/cable sweep and measured safe envelope. |
| 143–145 | 142–144 | Stock Z probe/Hall magnets; Omron retention, stock probe height, Hall magnet | OMIT | [Procedure](../chapters/06-toolhead.md); 05 Cartographer V4 measured heightT4, no contradictory stock probing. |
| 146–147 | 145–146 | StealthBurner; Separate toolhead manual | KEEP / REPLACE | [Procedure](../chapters/06-toolhead.md); Pinned SB/CW2 core; exact03 FiberUHF candidateT2/T3; no HF duct substitution. |
| 148–151 | 147–150 | Electronics/host mounts; Stock electronics location and Pi bracket | REPLACE | [Procedure](../chapters/07-wiring.md); Actual Leviathan/NH revisionsE1 determine integrated host/mount architecture. |
| 152–152 | 151–151 | 5V PSU; Stock separate 5V PSU | OMIT | [Procedure](../chapters/07-wiring.md); LDO board-specific host power; prevent dual supply/backfeed. |
| 153–155 | 152–154 | PSU/controller mounting; PSU frame and controller brackets | KEEP / REPLACE | [Procedure](../chapters/07-wiring.md); Keep confirmed PSU support; use actual Leviathan bracketE1. |
| 156–157 | 155–156 | Inlet/SSR; Stock separate switch inlet/SSR arrangement | REPLACE | [Procedure](../chapters/07-wiring.md); Actual combined LDO inlet and MRW heater circuitE3; qualified mains installation. |
| 158–161 | 157–160 | Stock nozzle Z endstop; Pin/PCB Z endstop assembly | OMIT | [Procedure](../chapters/08-software.md); Selected Cartographer virtual Z home after E5/E7; parts surplus. |
| 162–164 | 161–163 | X/Y endstops; Stock pod/PCB mounting | REPLACE | [Procedure](../chapters/06-toolhead.md); Retain physical X/Y functions; T1 X switch +M6 Vitalii compatible Y support. |
| 165–172 | 164–171 | Electronics bay attachment; Stock AC distribution/5V/supports | REPLACE / OMIT | [Procedure](../chapters/07-wiring.md); Verified board mounts/circuit; no separate5V PSU assumed; no stock Octopus pinout. |
| 173–173 | 172–172 | Interlude; Historical page | OMIT | [Procedure](../chapters/01-inventory.md); No assembly operation. |
| 174–178 | 173–177 | Controller targets/pinout; Octopus MCU/driver/jumpers | REPLACE | [Procedure](../chapters/08-software.md); E1 exact PCB; LeviathanV1.3H743 differs genericF446; SB and SBV2 separate. |
| 179–179 | 178–178 | Interlude; Historical page | OMIT | [Procedure](../chapters/01-inventory.md); No assembly operation. |
| 180–193 | 179–192 | Power/bed/controller wiring; Stock AC/DC/SSR/sensor routes | REPLACE / KEEP safety | [Procedure](../chapters/07-wiring.md); E2/E3 exact heaters/PT1000/fuse/PE; original diagram is not this board pinout. |
| 194–204 | 193–203 | Cable routing; Chains, strain relief and stock toolhead harness | KEEP / REPLACE | [Procedure](../chapters/07-wiring.md); Preserve loose flex routing; new USB pathsE4 and backer/CNC bridgesM3/M6; nonchain-rated probe cable excluded. |
| 205–209 | 204–208 | Motors/hotend/probe/fans; Octopus direct hotend/thermistor/probe wiring | REPLACE | [Procedure](../chapters/07-wiring.md); NH exact revision; USB notCAN;4.5A V2 continuous does not establish Rapido startup fit. |
| 210–213 | 209–212 | Skirt preparation; Printed support removal, inserts and fans | KEEP | [Procedure](../chapters/10-panels-first-print.md); Actual350 and fan voltagesP2. |
| 214–216 | 213–215 | Stock LCD; Mini12864 assembly | REPLACE / OMIT | [Procedure](../chapters/10-panels-first-print.md); Conditional actual LDO DSI touchscreen option; no stock display installed first. |
| 217–219 | 216–218 | Skirts; Frame attachment | KEEP | [Procedure](../chapters/10-panels-first-print.md); Use selected350 parts and serviceable fittings. |
| 220–221 | 219–220 | Stock LCD/EXP; LCD placement and ribbon cables | REPLACE / OMIT | [Procedure](../chapters/10-panels-first-print.md); Actual displayE1/P2; no EXP assumption forDSI. |
| 222–233 | 221–232 | Skirts and bottom panel; Retained panels/fans/hinges | KEEP | [Procedure](../chapters/10-panels-first-print.md); Guard mains/service covers; do not crush PE/cables. |
| 234–236 | 233–235 | Z belt covers; Retained belt covers | KEEP / ADD option | [Procedure](../chapters/10-panels-first-print.md); Conditional LDO LED wire cover; maintain top tensioner access. |
| 237–237 | 236–236 | Interlude; Historical page | OMIT | [Procedure](../chapters/01-inventory.md); No assembly operation. |
| 238–249 | 237–248 | Panels/doors; Foam clips magnets hinges | KEEP | [Procedure](../chapters/10-panels-first-print.md); ThicknessP2 and final travel/cable sweep. |
| 250–256 | 249–255 | Exhaust; Stock fan/filter housing | OMIT / REPLACE | [Procedure](../chapters/10-panels-first-print.md); Fan not confirmed owned; LDO cover+stockgrill, no unrelated filter upgrade. |
| 257–259 | 256–258 | Spool and filament; Spool holder/PTFE retainer | KEEP | [Procedure](../chapters/10-panels-first-print.md); Check retained inlet route with omitted exhaust and probe/cable clearance. |
| 260–261 | 259–260 | Startup/calibration; Generic next steps/help | REPLACE / ADD | [Procedure](../chapters/09-commissioning.md); Detailed prepower, individualmotors/endstops, gated controlled heat and currentCartographer sequence. |
| 262–262 + unnumbered cover | 261–262 | Closing attribution; Closing page and unnumbered back cover | KEEP | [Procedure](../chapters/10-panels-first-print.md); Upstream attribution preserved; index262 back cover has no printed page. |
