# 09 — Pre-power, first start, calibration and first print

**Readiness:** this chapter is a supervised procedure to be performed later on the physical machine. The documentation project has not flashed firmware, powered a printer, moved motors or heated anything. Static checks cannot validate assembly, ratings, mains safety or print quality.

**Prerequisites:** completed mechanical chapters and closed gates for the next action; actual configuration reviewed against hardware; E2/E3 closed before any heater enable. **Parts:** one assembled printer, approved protective-earth and thermal-protection system, fitted build surface and one intended filament sample for the final print. **Tools:** qualified electrical inspector's appropriate test equipment, multimeter, hex drivers, feeler gauge, ruler/calipers, terminal/UI access and direct emergency-stop/power-isolator access. Do not invent a test-equipment or torque specification from the plastic kit manual.

**KEEP:** Voron startup checks, independent electrical inspection and Klipper thermal safeguards. **REPLACE:** stock probe calibration with chapter 08's gated Cartographer sequence. **OMIT:** stock probe/endstop self-tests for devices that were omitted. **ADD:** rigid-joint binding, modified-bed expansion/clearance, PT1000 and heater-load checks.

## Pre-power checklist — all circuits initially isolated

LDO's mains warning requires certified personnel trained in local regulations and safety standards. The checklist records evidence; it does not certify electrical safety.

- [ ] Inlet unplugged; disconnect/isolator identified; no powered connector changes planned. No loose tools, wires, swarf or fasteners in the electronics compartment.
- [ ] E1 closed for each actual board/adapter/PSU: PCB silkscreen and MCU recorded; correct firmware target; input voltage selection correct; polarity checked; no unintended dual host/5 V supplies or backfeed route.
- [ ] Qualified inspector checks mains isolation/separation, terminal coverage, conductor size, contact/crimp quality, wire retention, fuse and switch ratings, strain relief and local protective requirements. AC switching and SSR orientation match the actual approved diagram.
- [ ] Protective earth verified to inlet, PSU enclosure, conductive frame and MRW bed using the required inspection method. A dedicated bed connection contacts the approved metal surface; anodized Wings/kinematic points are not the sole earth path. LDO static-discharge links are checked separately.
- [ ] E3 closed: actual heater, voltage, watts, sensor, SSR/heatsink and independent thermal fuse identified; heater adhesion/attachment and fuse mounting meet their manufacturer's procedure. Stock bonded heater or magnetic layer was not assumed reusable.
- [ ] E2 closed before hotend enable: exact Rapido2 Fiber voltage/cold/startup/current evidence and complete MOSFET/connector/wire/fuse/PSU path ratings documented. Software power limits are not used to excuse a current mismatch.
- [ ] Heater leads disconnected and individually insulated for initial board/sensor work. No bare terminal can touch frame/PCB. PT1000 and bed sensor leads are separate from heater/mains wiring.
- [ ] E4 closed: probe cable power and signal mapping verified; direct USB or documented downstream USB/CAN route selected; no 24 V applied to USB; no hot-plugging. Cable bends and strain relief meet each cable's rating.
- [ ] Electronics mounted securely and cooled; correct fan voltage/connector mapping; cable lids/covers close without crushing wires.
- [ ] E6 mechanical prerequisites complete: frame and gantry squared, rigid Z joints installed without forcing alignment, belts routed correctly, pulleys/capture checked, axes manually free over measured full travel and gantry supported against falling while unpowered. Kinematic bed retains its intended thermal freedom.
- [ ] Full sweep checked for Rapido UHF/CNC carriage/probe collision, backer screws, XY joints, Wings/bed clamps, belts and all wiring. Conservative provisional travel envelope recorded from measurements, with clearance in reserve.
- [ ] Active config has one endstop authority per axis and one probe generation. Cartographer offsets, mesh/QGL points and safe-home position remain blocked until E7; no automatic home, QGL, brush, heat or print macro runs on connect.

**Completion check:** record inspector, date and actual findings in a private local commissioning record. Failed items remain blocking; a rendered site or passed link check cannot close them.

## First start — sensors and communication before motors/heaters

Only after the qualified inspector permits energization, power the reviewed isolated arrangement with heaters disconnected. Remain at the printer and have immediate isolation available.

1. Confirm expected board status indicators and communications, with no smell, noise, heating connector or unexpected fan/motor motion. Stop if anything differs from the identified circuit.
2. Identify host device paths read-only, one verified device at a time with power off before cable changes. Match paths to mainboard, toolboard and probe; update the private config without fabricated IDs. Confirm E5 version records and host/MCU compatibility before enabling functions.
3. Verify cold hotend, bed and optional chamber readings are plausible for room conditions and consistent with an independent reference. For the reported PT1000, use the actual TH0 pull-up and `sensor_type: PT1000`. Sensor fault, implausible reading or inverted response blocks all heating. Do not bypass `min_temp`, `max_temp` or heater verification to hide an error.
4. Warm only the sensor locally using a safe non-powered method appropriate to its construction and confirm the corresponding channel changes; do not swap sensors while powered. Confirm neither heater can energize at this stage.
5. Check fan identity/direction at a safe setting once fan voltage is confirmed. Verify hotend heatsink cooling starts according to the reviewed heater-fan behavior before any controlled hotend test.

**Completion check:** stable communications, correctly mapped temperature channels and fans, documented actual IDs and no unintended energization.

## E6 — Individual motors/endstops before homing or QGL

The [Voron startup sequence](https://docs.vorondesign.com/build/startup/) and [Klipper configuration checks](https://www.klipper3d.org/Config_checks.html) govern supervised checks. Ensure adequate clearance, correct current limit from the actual motor/board specification, and no tension/binding from the rigid-joint system. Keep hands clear of powered mechanics.

1. Test each physical X/Y switch by hand with `QUERY_ENDSTOPS` while the machine is stationary. Confirm the intended channel changes state and is otherwise open. Repeat for the exact replacement endstop mounts. Do not require omitted Z-switch or Omron states; the Cartographer virtual Z endstop is calibrated later.
2. With a supported, safe gantry position and a reviewed configuration, test **one motor at a time** using Klipper's `STEPPER_BUZZ` procedure. Identify A/B and each Z corner physically. Stop on wrong identity, direction, roughness or unexpected resistance. Correct wiring/config only with the machine powered off and repeat only the affected check.
3. Interpret the individual A/B motor buzz results using the documented CoreXY arrangement: one motor's movement is not an X or Y axis move. Confirm motor identity and direction before homing; do not bypass Klipper's homing requirement with forced moves or invented position values.
4. Establish homing direction and conservative travel limits from measurements. Perform X and Y homing individually with immediate-stop access, then conservative interior moves. If a switch does not stop the intended motion, isolate power and correct the fault before proceeding.
5. Verify the four Z motor signs/identities, unobstructed travel and documented gantry square. Do not perform Z homing or QGL until E5/E7 and the scan-calibration procedure are ready. Fixed joints must not bind at any height; software leveling is not a remedy for forced geometry.

**Completion check:** each motor and endstop has a physical identity and observed expected behavior; travel boundaries were measured and cautiously verified; no cable, bed, probe or hotend collision occurs. Proceed to scan calibration only if the bed magnetic arrangement is compatible and all E7 measurements are recorded.

## Controlled heater tests — only after E2 and E3 close

1. Isolate power, reconnect **one approved heater circuit** at a time and recheck its terminals and sensor. The qualified installer approves any mains circuit changes. Maintain independent thermal protection, direct attendance and power-isolator access.
2. Apply a modest initial setpoint appropriate to that heater and material, observe the correct sensor rising and the other channels staying consistent. Stop immediately for uncontrolled rise, incorrect-channel heating, smell, discolored/hot connectors, cable heating, communication loss or heater verification fault. Never continue to PID tuning to diagnose an unsafe electrical path.
3. Confirm a commanded off-state stops electrical heating and the temperature trends as expected; residual stored heat is normal and must be distinguished from continued energization. Verify the physical isolator stops the system as intended; do not short outputs or deliberately defeat a sensor/fuse to test protection.
4. After the hotend electrical test passes, return to the exact delivered
   Phaetus revision/nozzle instructions. If those instructions require nozzle
   hot-tightening, perform it before first extrusion using the documented
   temperature, torque, support method and burn precautions. Do not disturb a
   factory assembly when its instructions do not require it, and do not copy
   another Rapido revision's values. Reinspect the leads and cartridge after
   this handling.
5. Only after basic behavior passes, follow the hotend/bed limits and Klipper PID-calibration procedure at intended operating conditions. Save **measured** results. Check hotend cooling, thermal expansion, bed seating and cable slack through a full stabilized heating cycle.

**Completion check:** electrical load/path ratings remain within approval, temperatures behave correctly, independent protections remain fitted, and measured PID/limits are saved privately. Both heater circuits must pass independently. A hot connector or unexplained overshoot is a failure, not a tuning target.

## Calibration and the first print

1. Follow [chapter 08](08-software.md) for scan model, conservative Z homing, QGL, rehoming, nozzle cleaning, Survey Touch calibration and bounded mesh. Keep the verified magnetic arrangement and surface fitted. Current touch-mesh support is not a fallback for an embedded-magnet bed.
2. Measure extruder rotation distance, then tune first layer, pressure advance and input shaping using the [Voron setup documentation](https://docs.vorondesign.com/build/startup/) and exact hotend/nozzle/filament limits. Record the actual nozzle included with purchase 03 before selecting slicer parameters. Do not insert someone else's PID, offset, acceleration or pressure-advance numbers.
3. Generate a small first-layer test and modest calibration part entirely inside the verified envelope. Review the slicer's machine size, start sequence and temperature limits. Use the validated scan-home/QGL/mesh/clean-nozzle/Survey-touch sequence; no automatic brush is enabled without purchased hardware and measured coordinates.
4. Attend the whole first print. Stop for scraping, skipped motion, loose joints, warped/rocking bed, unstable temperatures, cable rubbing or changed probe behavior. Inspect the rigid joints, belt capture, UHF/probe mount and bed freedom again after cooling.
5. Record actual results, unresolved faults and measured configuration privately. Update only the technical manifest and evidence statuses in the public repository. Recheck affected clearances and recalibrate when hardware, firmware generation, nozzle/sheet geometry or cable route changes.

**Completion check:** an observed successful first print and recorded configuration are physical commissioning evidence. Until that occurs, this repository remains an illustrated, gated assembly guide with a reproducible website—not a verified build-ready machine configuration.
