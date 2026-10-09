# Hardware, wiring and missing requirements

Purchase inventory stays separate from additional requirements. Package titles are not a delivered-content audit. Exact verified stacks, orientations and warnings are in the phase chapters; unknown fasteners, connector views and ratings block the affected operation.

| System | Parts / quantities | Verification | Ownership | Gates |
| --- | --- | --- | --- | --- |
| Frame / rails / lower Z drives | Kit 01: quantities in chapter 03 | I1 carton audit; 6 mm XY / 9 mm Z / 6 mm reduction loops identified separately | Kit-reported; actual contents unverified | I1 M1 F1 F2 |
| Titanium backers | 02 listing: 22 M3x8 FHCS + 10 M3x6 FHCS; approximately 30 M3 T-nuts separately | Count actual occupied holes; verify counterbores, nut/extrusion fit and clearance | Extra nuts required but not confirmed owned | M3 |
| Double-shear A/B pair | 09: 14 F695; 12 M5 1 mm shims; 2 M5 10 mm sleeves; 6 M3 20 mm sleeves; 8 M3x8 FHCS; 6 M3x35 SHCS; 4 ultra-flat M3x4; 6 cup shims | PDF bearing count conflict; actual motor shaft engagement and motor fasteners unresolved | Purchased set; contents unverified | M1 M4 M5 |
| Front-idler pair | 11: 4 F695; 4 M5 1 mm shims; 2 M5 10 mm sleeves; 4 M3x5 FHCS; 4 M3x45 SHCS; 8 M3x6 BHCS | Extrusion screws/T-nuts and clamp supply differ between live page and PDF | Purchased set; contents unverified | M1 M5 M8 |
| Live-idler XY pair | 14: 8 F695; 4 M5 1 mm shims; 4 M5 8 mm sleeves; 2 M3 20 mm sleeves; 4 springs; 4 M3x8 FHCS; 2 M3x30 FHCS; 6 M5x10 FHCS; 8 M3x8 BHCS | Eight retention screws: PDF M3x3 vs M3x4 conflict; endstop CAD export/hardware unresolved | Purchased set; contents and retention length unverified | M1 M5 M6 |
| Rigid Z joints | 13 listing: four joints; 16 M3x8 + 4 M3x14 + 4 M5x14 | Assembly drawing, head styles and screw assignments unconfirmed | Purchased set; no separate lower clamps installed | M7 M8 M9 |
| Upper Z tensioners | 12: four preassembled units; listing 8 M5x25; PDF internal contents in chapter 04 | Frame M5x16/T-nuts and left/right assignment need exact revision instructions | Purchased set; attachment hardware unverified | M2 |
| Upper Z clamp allocation | 10: two top clamps at rear; 11: two front clamps, conditional | Four integrated lower captures from 13; 10 bottom pair and two of 11 clamps surplus if fit/contents confirmed | Purchased; no physical fit validation | M8 |
| Bed supports | 07: three different contacts; 08: one installed pair of Wings | Resolve 2x packaging; third-seat ~130 mm extrusion excluded; bolt lengths and support map | Third support / attachments conditional requirement, not confirmed owned | B2 B3 F1 |
| Bed thermal system | 06: one MRW350 plate, purchased options unknown | New approved heater, sensor, independent thermal fuse, surface, PE lug and strain relief | Required but not confirmed owned; stock LDO bonded assembly left intact | B1 B4 E3 |
| CW2 / StealthBurner | Kit 01 baseline conditional; 03 exact UHF hotend | Core hardware in chapter 06; UHF cartridge / duct / shell geometry must match | Validated UHF printed cartridge required but not confirmed owned | T1 T2 T3 |
| CNC carriage / probe | 04: one carriage; 05: one V4 Standard | 4 M3x8 rail screws (head by revision); 2 M3x6 clamp screws; X switch 2 M2x10; standard probe 2 M3x6 | 8.5 mm UHF extenders and longer screws conditional requirement, not confirmed owned | T1 T4 |
| Heater output / PT1000 | V2.0.0 only: HE0 PA7, 4.5 A continuous; TH0 PB12, 2200 ohm pull-up | Exact 03 cold/startup load versus MOSFET, contacts, wiring, fuse and shared PSU headroom | Rated ferrules / contacts required but not confirmed owned | E1 E2 |
| Primary USB route | Nitehawk USB + 24 V umbilical; 05 direct host USB proposed | V4 USB requires 5 V; PROBE 24 V prohibited; verify cable rating and connector orientation | Approved direct USB cable / strain relief required but not confirmed owned | E4 |
| Downstream USB alternate | Nitehawk V2 P8 JST-ZH1.5 5P to V4 four-pin Molex Sherlock | Schematic pins 1 VBUS, 2 D-, 3 D+, 4/5 GND; plug-side view reversals, fifth contact and port load need verification | Conditional alternate harness; not claimed purchased | E4 |
| CAN alternate | Only after actual port, firmware, power and cable/termination identification | Leviathan CAN supply 24 V differs USB 5 V; Nitehawk uplinks use USB | Conditional alternate; no CAN adapter purchase claimed | E4 E5 |
| Mains / protective earth | Actual kit inlet, PSU and SSR arrangement plus MRW circuit | Isolation, fuse/SSR/heatsink ratings, dedicated PE, covered terminals, approved circuit | Rated parts required but not confirmed owned; manufacturer requires qualified installer | E1 E3 |
| Nozzle cleaning | No automatic brush macros active | Kit brass brush may be present; keep Cartographer coil away from metal brush | Manual cleaning primary; silicone brush optional and not confirmed owned | T4 E7 |

## Additional requirements and optional conveniences

Required but not confirmed owned means inventory or acquire only after its interface gate is resolved. Optional alternates are not active main-path requirements and do not add to the fourteen reported purchases.

| Item | Quantity | Classification | Gate |
| --- | --- | --- | --- |
| Compatible new bed heater, sensor, thermal fuse, magnetic sheet/buildsurface if plain plate | Unverified / unset | required-but-not-confirmed-owned | B4 |
| Dedicated PElead, appropriate M5attachment terminal/hardware and bed cable strainrelief | Unverified / unset | required-but-not-confirmed-owned | B4 |
| Thirdseat ~130mm extrusion or manufacturer-supported Wings layout support | Unverified / unset | conditional-required-but-not-confirmed-owned | B3 |
| 2F UHF validated printed cartridge/frontrear and matching shell | Unverified / unset | required-but-not-confirmed-owned | T2 |
| CNC8.5mm UHF extenders and suitable fasteners | Unverified / unset | conditional-required-but-not-confirmed-owned | T4 |
| Exact boardrevision mounts and umbilical cable relief | Unverified / unset | required-but-not-confirmed-owned | T1 |
| Silicone nozzle brush/location | Unverified / unset | optional-not-confirmed-owned; manual initial cleaning permitted | T4 |
| Approved MRW-compatible bed heater and magnetic/spring-steel surface | Unverified / unset | required but not confirmed owned | E3 |
| Correct thermal fuse, attachment materials and approved bed PE lug/hardware | Unverified / unset | required but not confirmed owned | E3 |
| Rated SSR/heatsink, inlet/branch fuses and approved mains harness appropriate to actual bed | Unverified / unset | required but not confirmed owned | E3 |
| Approved direct host USB-to-Cartographer V4 Standard cable/strain relief | 1 | required but not confirmed owned | E4 |
| Exact downstream USB P8-to-Sherlock cable if that route is chosen | 1 | conditional requirement; not confirmed owned | E4 |
| Heater ferrules/connector contacts fitting actual wires and board | Unverified / unset | required but not confirmed owned | E2 |
| Nitehawk static discharge links and revision-correct fan adapter | Unverified / unset | kit contents to verify; not confirmed owned | E1 |
| CAN interface and approved cable/termination if USB is not chosen | Unverified / unset | conditional alternate; not purchased evidence | E4 |
| Nozzle brush/purge bucket | 0 | optional convenience, omitted from primary path | Unverified / unset |
