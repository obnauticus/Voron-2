# Printed-parts matrix

The filenames are exact source members. Current upstream files, including unused sizes and alternatives, are accounted for. Quantity is the planned print/installed-piece count, not number of files. `null` means resolve first; a suffix quantity only applies if that alternative is selected. Included-by-LDO means the supplier BOM says it is provided, not that this carton was counted.

Upstream functional-print guidance: ABS, 0.2 mm layers, forced 0.4 mm extrusion width, 40% infill, 4 walls, and 5 top/bottom layers (manual p4). Honor part-specific translucent/opaque guidance for LEDs and any verified vendor instructions. STEP members are not print-ready STLs. No standard HF cartridge is activated for the UHF purchase.

| Exact filename | Planned qty | Disposition | Pinned source revision | Guidance / gate |
| --- | --- | --- | --- | --- |
| `STLs/Clockwork2/Direct_Drive/main_body.stl` | 1 | required if CW2 confirmed | 8bcb9c246fac19d8ac03931ef97fa07c5e5f0f2b | Use documented source guidance; verify the actual interface before printing. |
| `STLs/Clockwork2/Direct_Drive/motor_plate.stl` | 1 | required if CW2 confirmed | 8bcb9c246fac19d8ac03931ef97fa07c5e5f0f2b | Use documented source guidance; verify the actual interface before printing. |
| `STLs/Clockwork2/Direct_Drive/[a]_guidler_a.stl` | 1 | required if CW2 confirmed | 8bcb9c246fac19d8ac03931ef97fa07c5e5f0f2b | Use documented source guidance; verify the actual interface before printing. |
| `STLs/Clockwork2/Direct_Drive/[a]_guidler_b.stl` | 1 | required if CW2 confirmed | 8bcb9c246fac19d8ac03931ef97fa07c5e5f0f2b | Use documented source guidance; verify the actual interface before printing. |
| `STLs/Clockwork2/Direct_Drive/[a]_latch.stl` | 1 | required if CW2 confirmed | 8bcb9c246fac19d8ac03931ef97fa07c5e5f0f2b | Use documented source guidance; verify the actual interface before printing. |
| `STLs/Clockwork2/Direct_Drive/[a]_latch_shuttle.stl` | 1 | required if CW2 confirmed | 8bcb9c246fac19d8ac03931ef97fa07c5e5f0f2b | Use documented source guidance; verify the actual interface before printing. |
| `STLs/Stealthburner/[a]_stealthburner_main_body.stl` | 1 | conditional UHF fit | 8bcb9c246fac19d8ac03931ef97fa07c5e5f0f2b | Use documented source guidance; verify the actual interface before printing. |
| `STLs/Stealthburner/Printheads/phaetus_rapido_v2/stealthburner_printhead_rapido_v2_front.stl` | 0 | omit; HF mount not verified for purchased UHF | 8bcb9c246fac19d8ac03931ef97fa07c5e5f0f2b | Use documented source guidance; verify the actual interface before printing. |
| `STLs/Stealthburner/Printheads/phaetus_rapido_v2/stealthburner_printhead_rapido_v2_rear_cw2.stl` | 0 | omit; HF mount not verified for purchased UHF | 8bcb9c246fac19d8ac03931ef97fa07c5e5f0f2b | Use documented source guidance; verify the actual interface before printing. |
| `STLs/Clockwork2/cable_door_for_pcb.stl` | Unverified / unset | unresolved board/umbilical variant | 8bcb9c246fac19d8ac03931ef97fa07c5e5f0f2b | Use documented source guidance; verify the actual interface before printing. |
| `STLs/Clockwork2/[a]_pcb_spacer.stl` | Unverified / unset | unresolved board/umbilical variant | 8bcb9c246fac19d8ac03931ef97fa07c5e5f0f2b | Use documented source guidance; verify the actual interface before printing. |
| `STLs/Clockwork2/chain_anchor_2hole.stl` | Unverified / unset | unresolved board/umbilical variant | 8bcb9c246fac19d8ac03931ef97fa07c5e5f0f2b | Use documented source guidance; verify the actual interface before printing. |
| `STLs/Clockwork2/chain_anchor_3hole.stl` | Unverified / unset | unresolved board/umbilical variant | 8bcb9c246fac19d8ac03931ef97fa07c5e5f0f2b | Use documented source guidance; verify the actual interface before printing. |
| `STLs/Stealthburner/[o]_stealthburner_LED_carrier.stl` | 1 | optional lighting | 8bcb9c246fac19d8ac03931ef97fa07c5e5f0f2b | Use documented source guidance; verify the actual interface before printing. |
| `STLs/Stealthburner/[c]_stealthburner_LED_diffuser.stl` | 1 | optional lighting | 8bcb9c246fac19d8ac03931ef97fa07c5e5f0f2b | Use documented source guidance; verify the actual interface before printing. |
| `STLs/Stealthburner/[o]_stealthburner_LED_diffuser_mask.stl` | 1 | optional lighting | 8bcb9c246fac19d8ac03931ef97fa07c5e5f0f2b | Use documented source guidance; verify the actual interface before printing. |
| `STLs/Tools/SB_5015_Cutting_Tool_A.stl` | 1 | optional fan tool | 8bcb9c246fac19d8ac03931ef97fa07c5e5f0f2b | Use documented source guidance; verify the actual interface before printing. |
| `STLs/Tools/SB_5015_Cutting_Tool_B.stl` | 1 | optional fan tool | 8bcb9c246fac19d8ac03931ef97fa07c5e5f0f2b | Use documented source guidance; verify the actual interface before printing. |
| `voron 2.4-Rapido 2/uhf前.stl` | 1 | unresolved exact combined UHF fit | 7401934e28d56844ba4f311e9d588b1e4d0510dd | Use documented source guidance; verify the actual interface before printing. |
| `voron 2.4-Rapido 2/uhf 后.stl` | 1 | unresolved exact combined UHF fit | 7401934e28d56844ba4f311e9d588b1e4d0510dd | Use documented source guidance; verify the actual interface before printing. |
| `STLs/Gantry/AB_Drive_Units/a_drive_frame_upper.stl` | 0 | replaced_omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Purchased CNC replacement from outset. |
| `STLs/Gantry/AB_Drive_Units/a_drive_frame_lower.stl` | 0 | replaced_omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Purchased CNC replacement from outset. |
| `STLs/Gantry/AB_Drive_Units/b_drive_frame_upper.stl` | 0 | replaced_omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Purchased CNC replacement from outset. |
| `STLs/Gantry/AB_Drive_Units/b_drive_frame_lower.stl` | 0 | replaced_omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Purchased CNC replacement from outset. |
| `STLs/Gantry/Front_Idlers/front_idler_left_upper.stl` | 0 | replaced_omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Purchased CNC replacement from outset. |
| `STLs/Gantry/Front_Idlers/front_idler_left_lower.stl` | 0 | replaced_omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Purchased CNC replacement from outset. |
| `STLs/Gantry/Front_Idlers/front_idler_right_upper.stl` | 0 | replaced_omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Purchased CNC replacement from outset. |
| `STLs/Gantry/Front_Idlers/front_idler_right_lower.stl` | 0 | replaced_omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Purchased CNC replacement from outset. |
| `STLs/Gantry/Front_Idlers/[a]_tensioner_left.stl` | 0 | replaced_omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Purchased CNC replacement from outset. |
| `STLs/Gantry/Front_Idlers/[a]_tensioner_right.stl` | 0 | replaced_omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Purchased CNC replacement from outset. |
| `STLs/Gantry/X_Axis/XY_Joints/xy_joint_left_upper_MGN12.stl` | 0 | replaced_omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Purchased CNC replacement from outset. |
| `STLs/Gantry/X_Axis/XY_Joints/xy_joint_left_lower_MGN12.stl` | 0 | replaced_omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Purchased CNC replacement from outset. |
| `STLs/Gantry/X_Axis/XY_Joints/xy_joint_right_upper_MGN12.stl` | 0 | replaced_omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Purchased CNC replacement from outset. |
| `STLs/Gantry/X_Axis/XY_Joints/xy_joint_right_lower_MGN12.stl` | 0 | replaced_omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Purchased CNC replacement from outset. |
| `STLs/Z_Idlers/z_tensioner_bracket_a_x2.stl` | 0 | replaced_omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Purchased CNC replacement from outset. |
| `STLs/Z_Idlers/z_tensioner_bracket_b_x2.stl` | 0 | replaced_omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Purchased CNC replacement from outset. |
| `STLs/Z_Idlers/[a]_z_tensioner_9mm_x4.stl` | 0 | replaced_omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Purchased CNC replacement from outset. |
| `STLs/Gantry/Z_Joints/z_joint_upper_x4.stl` | 0 | replaced_omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Purchased CNC replacement from outset. |
| `STLs/Gantry/Z_Joints/z_joint_lower_x4.stl` | 0 | replaced_omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Purchased CNC replacement from outset. |
| `STLs/Gantry/Z_Joints/z_joint_upper_hall_effect.stl` | 0 | replaced_omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Purchased CNC replacement from outset. |
| `STLs/Gantry/[a]_z_belt_clip_lower_x4.stl` | 0 | replaced_omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Purchased CNC replacement from outset. |
| `STLs/Gantry/[a]_z_belt_clip_upper_x4.stl` | 0 | replaced_omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Metal replacement from the outset; upper stock clip omitted only after M8 confirms four CNC upper interfaces. |
| `Live Shaft XY/Endstop_PCB_Mount_heat_inserts.step` | Unverified / unset | unresolved | Live_Shaft_XY.zip query v=1779734631; hash in sources | Select/export after actual PCB and bump fit; no manufacturer print settings, insert/screw spec or reuse permission established. |
| `Live Shaft XY/2x_PCB_Spacer.step` | Unverified / unset | unresolved | Live_Shaft_XY.zip query v=1779734631; hash in sources | Select/export after actual PCB and bump fit; no manufacturer print settings, insert/screw spec or reuse permission established. |
| `Live Shaft XY/Endstop_Bump.step` | Unverified / unset | unresolved | Live_Shaft_XY.zip query v=1779734631; hash in sources | Select/export after actual PCB and bump fit; no manufacturer print settings, insert/screw spec or reuse permission established. |
| `Live Shaft XY/Endstop_Bump_Deep.step` | Unverified / unset | unresolved | Live_Shaft_XY.zip query v=1779734631; hash in sources | Select/export after actual PCB and bump fit; no manufacturer print settings, insert/screw spec or reuse permission established. |
| `extrusion_backers/STLs/XY_cable_chain_bridge-3hole-3mm_backer.stl` | Unverified / unset | unresolved | 62268ed817878e54d6a1186882060aa8368d4f0f | Candidate only if actual cable-chain routing requires it; 3mm name does not verify 3.2mm backer fit. |
| `extrusion_backers/STLs/XY_cable_chain_bridge-Igus-3mm_backer.stl` | Unverified / unset | unresolved | 62268ed817878e54d6a1186882060aa8368d4f0f | Candidate only if actual cable-chain routing requires it; 3mm name does not verify 3.2mm backer fit. |
| `STLs/Leviathan_bracket_set.stl` | Unverified / unset | unresolved board-dependent | 878c3c4893ea353552c957f574509f9890e1e37a | One bracket set if actual Leviathan matches; RevD BOM claims left/right included; confirm E1 |
| `STLs/usb_adapter_mount_partial_cover.stl` | 1 | required after E1/T1 | 42ae497cfd627acde0f6ad81c8dd26f51efcbb48 | V2 adapter partial cover if exact docs/revision confirmed E1; kit inclusion unverified |
| `STLs/cw2_captive_pcb_cover.stl` | 1 | required after E1/T1 | be93526b948d3339c755cb32116baef221ce1a8d | Reused original source part linked by V2 docs; verify actual board/clearance E1/T1 |
| `STLs/cw2_chain_anchor_tilted.stl` | Unverified / unset | unresolved board-dependent | be93526b948d3339c755cb32116baef221ce1a8d | One if confirmed cable-chain route; USB umbilical/backer/probe cable rating E4/M3 may require different relief |
| `STLs/usb_adapter_mount.stl` | Unverified / unset | unresolved board-dependent | be93526b948d3339c755cb32116baef221ce1a8d | One only for original SB adapter after E1; do not install original/V2 alternate mounts together |
| `STLs/bed_wago_mount.stl` | 1 | included by LDO | 5b0496a5ae8d0d6a3f782dfa7e06eb9e1c102ba5 | RevD includes one; verify actual connector, MRW mounting/strain relief and ratings E3 |
| `STLs/BTT Pi TFT4.3 Mount/[a]_faceplate.stl` | Unverified / unset | unresolved | 5b0496a5ae8d0d6a3f782dfa7e06eb9e1c102ba5 | One for matching actual LDO/BTT4.3 display E1/P2 |
| `STLs/BTT Pi TFT4.3 Mount/mount.stl` | Unverified / unset | unresolved | 5b0496a5ae8d0d6a3f782dfa7e06eb9e1c102ba5 | One standard mount OR thick mount, not both; verify actual panel/display E1/P2 |
| `STLs/BTT Pi TFT4.3 Mount/mount_thick.stl` | Unverified / unset | unresolved | 5b0496a5ae8d0d6a3f782dfa7e06eb9e1c102ba5 | One thick-panel variant if matching actual panel; do not install both alternatives |
| `STLs/Electronics_Bay/Controller_Mounts/BIGDIPPER_bracket_set.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Provisional Leviathan replaces alternate controller and separate 5V PSU mounts. |
| `STLs/Electronics_Bay/Controller_Mounts/BTT_MOT_EXP_bracket.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Provisional Leviathan replaces alternate controller and separate 5V PSU mounts. |
| `STLs/Electronics_Bay/Controller_Mounts/Duet2_Duet3Mini5_bracket_set.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Provisional Leviathan replaces alternate controller and separate 5V PSU mounts. |
| `STLs/Electronics_Bay/Controller_Mounts/GTR_bracket_set.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Provisional Leviathan replaces alternate controller and separate 5V PSU mounts. |
| `STLs/Electronics_Bay/Controller_Mounts/Octopus_bracket_set.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Provisional Leviathan replaces alternate controller and separate 5V PSU mounts. |
| `STLs/Electronics_Bay/Controller_Mounts/S6_bracket_set.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Provisional Leviathan replaces alternate controller and separate 5V PSU mounts. |
| `STLs/Electronics_Bay/Controller_Mounts/SKR_Pro_bracket_set.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Provisional Leviathan replaces alternate controller and separate 5V PSU mounts. |
| `STLs/Electronics_Bay/Controller_Mounts/SKR_bracket_inline_set.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Provisional Leviathan replaces alternate controller and separate 5V PSU mounts. |
| `STLs/Electronics_Bay/Controller_Mounts/Spider_bracket_set.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Provisional Leviathan replaces alternate controller and separate 5V PSU mounts. |
| `STLs/Electronics_Bay/Other_PS_Mounts/UHP_200_Mount_x2.stl` | Unverified / unset | unresolved | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Match actual PSU/host board revision before selecting E1. |
| `STLs/Electronics_Bay/Other_PS_Mounts/UHP_350_Mount_x2.stl` | Unverified / unset | unresolved | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Match actual PSU/host board revision before selecting E1. |
| `STLs/Electronics_Bay/PSU_stabilizer_50mm.stl` | Unverified / unset | unresolved | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Match actual PSU/host board revision before selecting E1. |
| `STLs/Electronics_Bay/lrs_200_psu_bracket_x2.stl` | Unverified / unset | unresolved | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Two brackets if actual LRS-200-24 confirmed; no PSU substitution assumed. |
| `STLs/Electronics_Bay/pcb_din_clip_x3.stl` | 4 | included by LDO | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Rev D BOM claims four clips; verify delivered count and actual board brackets E1. File name x3 is stock count. |
| `STLs/Electronics_Bay/raspberrypi_bracket.stl` | Unverified / unset | unresolved | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Match actual PSU/host board revision before selecting E1. |
| `STLs/Electronics_Bay/rs25_psu_bracket.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Provisional Leviathan replaces alternate controller and separate 5V PSU mounts. |
| `STLs/Electronics_Bay/wago_221-415_mount_3by5.stl` | 1 | required | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | KEEP; upstream filename count and retained manual assembly. ABS guidance p4. |
| `STLs/Exhaust_Filter/[a]_exhaust_fan_grill.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Stock exhaust-fan assembly omitted; its fan ownership is not confirmed. LDO cover closes opening. |
| `STLs/Exhaust_Filter/[a]_exhaust_filter_mount_x2.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Stock exhaust-fan assembly omitted; its fan ownership is not confirmed. LDO cover closes opening. |
| `STLs/Exhaust_Filter/[a]_filter_access_cover.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Stock exhaust-fan assembly omitted; its fan ownership is not confirmed. LDO cover closes opening. |
| `STLs/Exhaust_Filter/exhaust_filter_grill.stl` | 1 | required | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | KEEP; upstream filename count and retained manual assembly. ABS guidance p4. |
| `STLs/Exhaust_Filter/exhaust_filter_housing.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Stock exhaust-fan assembly omitted; its fan ownership is not confirmed. LDO cover closes opening. |
| `STLs/Gantry/AB_Drive_Units/[a]_cable_cover.stl` | Unverified / unset | unresolved | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Confirm retained chain/USB umbilical/backer clearance at M3/M6/E4 before selecting. |
| `STLs/Gantry/AB_Drive_Units/[a]_z_chain_retainer_bracket_x2.stl` | Unverified / unset | unresolved | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Confirm retained chain/USB umbilical/backer clearance at M3/M6/E4 before selecting. |
| `STLs/Gantry/X_Axis/XY_Joints/[a]_endstop_pod_D2F_switch.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | CNC carriage/live joints replace stock geometry, endstop and probe supports. |
| `STLs/Gantry/X_Axis/XY_Joints/[a]_endstop_pod_hall_effect.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | CNC carriage/live joints replace stock geometry, endstop and probe supports. |
| `STLs/Gantry/X_Axis/XY_Joints/[a]_xy_joint_cable_bridge_2hole.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | CNC carriage/live joints replace stock geometry, endstop and probe supports. |
| `STLs/Gantry/X_Axis/XY_Joints/[a]_xy_joint_cable_bridge_3hole.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | CNC carriage/live joints replace stock geometry, endstop and probe supports. |
| `STLs/Gantry/X_Axis/X_Carriage/pinda_adapter.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | CNC carriage/live joints replace stock geometry, endstop and probe supports. |
| `STLs/Gantry/X_Axis/X_Carriage/probe_retainer_bracket.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | CNC carriage/live joints replace stock geometry, endstop and probe supports. |
| `STLs/Gantry/X_Axis/X_Carriage/probe_retainer_bracket_9mm.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | CNC carriage/live joints replace stock geometry, endstop and probe supports. |
| `STLs/Gantry/X_Axis/X_Carriage/x_frame_V2TR_MGN12_left.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | CNC carriage/live joints replace stock geometry, endstop and probe supports. |
| `STLs/Gantry/X_Axis/X_Carriage/x_frame_V2TR_MGN12_right.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | CNC carriage/live joints replace stock geometry, endstop and probe supports. |
| `STLs/Gantry/z_chain_bottom_anchor.stl` | Unverified / unset | unresolved | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Confirm retained chain/USB umbilical/backer clearance at M3/M6/E4 before selecting. |
| `STLs/Gantry/z_chain_guide.stl` | Unverified / unset | unresolved | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Confirm retained chain/USB umbilical/backer clearance at M3/M6/E4 before selecting. |
| `STLs/Panel_Mounting/Front_Doors/door_hinge_x6.stl` | 6 | required | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | KEEP; upstream filename count and retained manual assembly. ABS guidance p4. |
| `STLs/Panel_Mounting/Front_Doors/handle_a_x2.stl` | 2 | required | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | KEEP; upstream filename count and retained manual assembly. ABS guidance p4. |
| `STLs/Panel_Mounting/Front_Doors/handle_b_x2.stl` | 2 | required | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | KEEP; upstream filename count and retained manual assembly. ABS guidance p4. |
| `STLs/Panel_Mounting/Front_Doors/latch_x2.stl` | 2 | required | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | KEEP; upstream filename count and retained manual assembly. ABS guidance p4. |
| `STLs/Panel_Mounting/bottom_panel_clip_x4.stl` | 4 | required | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | KEEP; upstream filename count and retained manual assembly. ABS guidance p4. |
| `STLs/Panel_Mounting/bottom_panel_hinge_x2.stl` | 2 | required | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | KEEP; upstream filename count and retained manual assembly. ABS guidance p4. |
| `STLs/Panel_Mounting/corner_panel_clip_4mm_x8.stl` | Unverified / unset | unresolved | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Choose one clip-thickness family after actual panel measurement F2/P2; filename gives count for chosen family. |
| `STLs/Panel_Mounting/corner_panel_clip_6mm_x8.stl` | Unverified / unset | unresolved | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Choose one clip-thickness family after actual panel measurement F2/P2; filename gives count for chosen family. |
| `STLs/Panel_Mounting/deck_support_3mm_x8.stl` | Unverified / unset | unresolved | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Choose one clip-thickness family after actual panel measurement F2/P2; filename gives count for chosen family. |
| `STLs/Panel_Mounting/deck_support_4mm_x8.stl` | Unverified / unset | unresolved | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Choose one clip-thickness family after actual panel measurement F2/P2; filename gives count for chosen family. |
| `STLs/Panel_Mounting/midspan_panel_clip_4mm_x7.stl` | Unverified / unset | unresolved | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Choose one clip-thickness family after actual panel measurement F2/P2; filename gives count for chosen family. |
| `STLs/Panel_Mounting/midspan_panel_clip_6mm_x8.stl` | Unverified / unset | unresolved | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Choose one clip-thickness family after actual panel measurement F2/P2; filename gives count for chosen family. |
| `STLs/Panel_Mounting/z_belt_cover_a_x2.stl` | 2 | required | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | KEEP; upstream filename count and retained manual assembly. ABS guidance p4. |
| `STLs/Panel_Mounting/z_belt_cover_b_x2.stl` | 2 | required | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | KEEP; upstream filename count and retained manual assembly. ABS guidance p4. |
| `STLs/Skirts/250/front_skirt_a_250.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Wrong size for provisional 350 target; revisit only if I1 changes it. |
| `STLs/Skirts/250/front_skirt_b_250.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Wrong size for provisional 350 target; revisit only if I1 changes it. |
| `STLs/Skirts/250/rear_center_skirt_250.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Wrong size for provisional 350 target; revisit only if I1 changes it. |
| `STLs/Skirts/250/side_skirt_a_250_x2.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Wrong size for provisional 350 target; revisit only if I1 changes it. |
| `STLs/Skirts/250/side_skirt_b_250_x2.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Wrong size for provisional 350 target; revisit only if I1 changes it. |
| `STLs/Skirts/300/front_skirt_a_300.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Wrong size for provisional 350 target; revisit only if I1 changes it. |
| `STLs/Skirts/300/front_skirt_b_300.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Wrong size for provisional 350 target; revisit only if I1 changes it. |
| `STLs/Skirts/300/rear_center_skirt_300.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Wrong size for provisional 350 target; revisit only if I1 changes it. |
| `STLs/Skirts/300/side_skirt_a_300_x2.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Wrong size for provisional 350 target; revisit only if I1 changes it. |
| `STLs/Skirts/300/side_skirt_b_300_x2.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Wrong size for provisional 350 target; revisit only if I1 changes it. |
| `STLs/Skirts/350/front_skirt_a_350.stl` | 1 | required | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | KEEP; upstream filename count and retained manual assembly. ABS guidance p4. |
| `STLs/Skirts/350/front_skirt_b_350.stl` | 1 | required | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | KEEP; upstream filename count and retained manual assembly. ABS guidance p4. |
| `STLs/Skirts/350/rear_center_skirt_350.stl` | 1 | required | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | KEEP; upstream filename count and retained manual assembly. ABS guidance p4. |
| `STLs/Skirts/350/side_skirt_a_350_x2.stl` | 2 | required | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | KEEP; upstream filename count and retained manual assembly. ABS guidance p4. |
| `STLs/Skirts/350/side_skirt_b_350_x2.stl` | 2 | required | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | KEEP; upstream filename count and retained manual assembly. ABS guidance p4. |
| `STLs/Skirts/[a]_belt_guard_a_x2.stl` | 2 | required | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | KEEP; upstream filename count and retained manual assembly. ABS guidance p4. |
| `STLs/Skirts/[a]_belt_guard_b_x2.stl` | 2 | required | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | KEEP; upstream filename count and retained manual assembly. ABS guidance p4. |
| `STLs/Skirts/[a]_btt_knob_light_shield.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Not the provisional LDO D-family display/inlet path; verify actual options E1/P2. |
| `STLs/Skirts/[a]_fan_grill_a_x2.stl` | 2 | required | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | KEEP; upstream filename count and retained manual assembly. ABS guidance p4. |
| `STLs/Skirts/[a]_fan_grill_b_x2.stl` | 2 | required | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | KEEP; upstream filename count and retained manual assembly. ABS guidance p4. |
| `STLs/Skirts/[a]_fan_grill_open_optional_x2.stl` | 2 | optional | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Alternative open grille; not an additional installed pair. |
| `STLs/Skirts/[a]_fan_grill_retainer_x2.stl` | 2 | required | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | KEEP; upstream filename count and retained manual assembly. ABS guidance p4. |
| `STLs/Skirts/[a]_keystone_blank_insert.stl` | 1 | required | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | KEEP; upstream filename count and retained manual assembly. ABS guidance p4. |
| `STLs/Skirts/[a]_mini12864_case_front_insert.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Not the provisional LDO D-family display/inlet path; verify actual options E1/P2. |
| `STLs/Skirts/[a]_mini12864_case_hinge.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Not the provisional LDO D-family display/inlet path; verify actual options E1/P2. |
| `STLs/Skirts/keystone_panel.stl` | 1 | required | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | KEEP; upstream filename count and retained manual assembly. ABS guidance p4. |
| `STLs/Skirts/mini12864_case_front.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Not the provisional LDO D-family display/inlet path; verify actual options E1/P2. |
| `STLs/Skirts/mini12864_case_rear.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Not the provisional LDO D-family display/inlet path; verify actual options E1/P2. |
| `STLs/Skirts/power_inlet_IECGS_1.2mm.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Not the provisional LDO D-family display/inlet path; verify actual options E1/P2. |
| `STLs/Skirts/power_inlet_IECGS_1mm.stl` | Unverified / unset | unresolved | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Required if actual inlet is LDO 1.0mm; verify E1/P2 before print. |
| `STLs/Skirts/power_inlet_filtered.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Not the provisional LDO D-family display/inlet path; verify actual options E1/P2. |
| `STLs/Skirts/side_fan_support_x2.STL` | 2 | required | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | KEEP; upstream filename count and retained manual assembly. ABS guidance p4. |
| `STLs/Spool_Management/bowden_retainer.stl` | 1 | required | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | KEEP; upstream filename count and retained manual assembly. ABS guidance p4. |
| `STLs/Spool_Management/spool_holder.stl` | 1 | required | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | KEEP; upstream filename count and retained manual assembly. ABS guidance p4. |
| `STLs/Superceded_Parts/Frame_Brackets/dual_ramps_bracket_frame.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Superseded upstream alternative; not the R2 main path. |
| `STLs/Superceded_Parts/Frame_Brackets/duet_duex_bracket_frame_x2.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Superseded upstream alternative; not the R2 main path. |
| `STLs/Superceded_Parts/Frame_Brackets/lrs_bracket_frame.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Superseded upstream alternative; not the R2 main path. |
| `STLs/Superceded_Parts/Frame_Brackets/mks_gen_1.4_bracket_frame_x2.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Superseded upstream alternative; not the R2 main path. |
| `STLs/Superceded_Parts/Frame_Brackets/mks_gen_L_bracket_frame_x2.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Superseded upstream alternative; not the R2 main path. |
| `STLs/Superceded_Parts/Frame_Brackets/raspberry_pi_bracket.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Superseded upstream alternative; not the R2 main path. |
| `STLs/Superceded_Parts/Frame_Brackets/rs_25_psu_bracket_frame.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Superseded upstream alternative; not the R2 main path. |
| `STLs/Superceded_Parts/Frame_Brackets/rs_35_bracket_frame.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Superseded upstream alternative; not the R2 main path. |
| `STLs/Superceded_Parts/Frame_Brackets/skr_1.3_bracket_frame.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Superseded upstream alternative; not the R2 main path. |
| `STLs/Superceded_Parts/Frame_Brackets/skr_mini_e3_bracket_frame.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Superseded upstream alternative; not the R2 main path. |
| `STLs/Superceded_Parts/MGN9_X/[a]_belt_clamp_MGN9_x2.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Superseded upstream alternative; not the R2 main path. |
| `STLs/Superceded_Parts/MGN9_X/x_carriage_frame_left_MGN9.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Superseded upstream alternative; not the R2 main path. |
| `STLs/Superceded_Parts/MGN9_X/x_carriage_frame_right_MGN9.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Superseded upstream alternative; not the R2 main path. |
| `STLs/Superceded_Parts/MGN9_X/x_carriage_pivot_block_MGN9.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Superseded upstream alternative; not the R2 main path. |
| `STLs/Superceded_Parts/MGN9_X/xy_joint_left_lower_MGN9.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Superseded upstream alternative; not the R2 main path. |
| `STLs/Superceded_Parts/MGN9_X/xy_joint_left_upper_MGN9.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Superseded upstream alternative; not the R2 main path. |
| `STLs/Superceded_Parts/MGN9_X/xy_joint_right_lower_MGN9.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Superseded upstream alternative; not the R2 main path. |
| `STLs/Superceded_Parts/MGN9_X/xy_joint_right_upper_MGN9.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Superseded upstream alternative; not the R2 main path. |
| `STLs/Superceded_Parts/ZipChain/XY/zipchain2_xy_end.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Superseded upstream alternative; not the R2 main path. |
| `STLs/Superceded_Parts/ZipChain/XY/zipchain2_xy_link_a.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Superseded upstream alternative; not the R2 main path. |
| `STLs/Superceded_Parts/ZipChain/XY/zipchain2_xy_link_b.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Superseded upstream alternative; not the R2 main path. |
| `STLs/Superceded_Parts/ZipChain/Z/zipchain2_z_end.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Superseded upstream alternative; not the R2 main path. |
| `STLs/Superceded_Parts/ZipChain/Z/zipchain2_z_link_a.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Superseded upstream alternative; not the R2 main path. |
| `STLs/Superceded_Parts/ZipChain/Z/zipchain2_z_link_b.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Superseded upstream alternative; not the R2 main path. |
| `STLs/Superceded_Parts/ZipChain/Z/zipchain2_z_link_b_locking.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Superseded upstream alternative; not the R2 main path. |
| `STLs/Superceded_Parts/[a]_stopgap_80T_hubbed_gear.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Superseded upstream alternative; not the R2 main path. |
| `STLs/Superceded_Parts/[a]_z_tensioner_x4_6mm.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Superseded upstream alternative; not the R2 main path. |
| `STLs/Test_Prints/Filament_Card.stl` | 1 | optional | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Calibration or assembly aid; not an installed machine part. |
| `STLs/Test_Prints/Filament_Card_Caddy_25.stl` | 1 | optional | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Calibration or assembly aid; not an installed machine part. |
| `STLs/Test_Prints/Heatset_Practice.stl` | 1 | optional | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Calibration or assembly aid; not an installed machine part. |
| `STLs/Test_Prints/Thread_Test_1_x1_Rev1.STL` | 1 | optional | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Calibration or assembly aid; not an installed machine part. |
| `STLs/Test_Prints/Thread_Test_2_x1_Rev1.STL` | 1 | optional | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Calibration or assembly aid; not an installed machine part. |
| `STLs/Test_Prints/Thread_Test_3_x1_Rev1.STL` | 1 | optional | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Calibration or assembly aid; not an installed machine part. |
| `STLs/Test_Prints/Voron_Design_Cube_v7.stl` | 1 | optional | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Calibration or assembly aid; not an installed machine part. |
| `STLs/Tools/MGN12_rail_guide_x2.stl` | 2 | optional | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Calibration or assembly aid; not an installed machine part. |
| `STLs/Tools/MGN9_rail_guide_x2.stl` | 2 | optional | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Calibration or assembly aid; not an installed machine part. |
| `STLs/Tools/bed_hole_marking_template_x1_Rev2.STL` | 1 | optional | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Calibration or assembly aid; not an installed machine part. |
| `STLs/Tools/bottom_panel_template.stl` | 1 | optional | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Calibration or assembly aid; not an installed machine part. |
| `STLs/Tools/pulley_jig.stl` | 1 | optional | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | Calibration or assembly aid; not an installed machine part. |
| `STLs/Z_Drive/[a]_belt_tensioner_a_x2.stl` | 2 | required | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | KEEP; upstream filename count and retained manual assembly. ABS guidance p4. |
| `STLs/Z_Drive/[a]_belt_tensioner_b_x2.stl` | 2 | required | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | KEEP; upstream filename count and retained manual assembly. ABS guidance p4. |
| `STLs/Z_Drive/[a]_z_drive_baseplate_a_x2.stl` | 2 | required | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | KEEP; upstream filename count and retained manual assembly. ABS guidance p4. |
| `STLs/Z_Drive/[a]_z_drive_baseplate_b_x2.stl` | 2 | required | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | KEEP; upstream filename count and retained manual assembly. ABS guidance p4. |
| `STLs/Z_Drive/z_drive_main_a_x2.stl` | 2 | required | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | KEEP; upstream filename count and retained manual assembly. ABS guidance p4. |
| `STLs/Z_Drive/z_drive_main_b_x2.stl` | 2 | required | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | KEEP; upstream filename count and retained manual assembly. ABS guidance p4. |
| `STLs/Z_Drive/z_drive_retainer_a_x2.stl` | 2 | required | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | KEEP; upstream filename count and retained manual assembly. ABS guidance p4. |
| `STLs/Z_Drive/z_drive_retainer_b_x2.stl` | 2 | required | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | KEEP; upstream filename count and retained manual assembly. ABS guidance p4. |
| `STLs/Z_Drive/z_motor_mount_a_x2.stl` | 2 | required | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | KEEP; upstream filename count and retained manual assembly. ABS guidance p4. |
| `STLs/Z_Drive/z_motor_mount_b_x2.stl` | 2 | required | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | KEEP; upstream filename count and retained manual assembly. ABS guidance p4. |
| `STLs/Z_Endstop/nozzle_probe.stl` | 0 | replaced/omit | a192410e27ea345644ae5c4b29b4c9c40cbe1a73 | CNC tensioners or Cartographer replace this function. |
| `STLs/nozzle_probe_ldo.stl` | 0 | replaced/omit | 8270e8cf6c7ba29a7fd11d143c287bd3af576934 | Cartographer Z homing omits kit nozzle Z endstop; keep supplied piece as surplus. |
| `STLs/led_fan_pcb_spacer_x2.stl` | 2 | included by LDO | 8270e8cf6c7ba29a7fd11d143c287bd3af576934 | Two in Rev D BOM; verify carton and PCB fit. |
| `STLs/cw2_offset_chain_anchor.stl` | Unverified / unset | unresolved | 8270e8cf6c7ba29a7fd11d143c287bd3af576934 | LDO original two-hole chain anchor; verify actual Nitehawk/routing/backer fit. |
| `STLs/exhaust_cover.stl` | 1 | required | 8270e8cf6c7ba29a7fd11d143c287bd3af576934 | Seal unused exhaust with stock grill; no extra filter modification added. |
| `STLs/handlebar_spacer_x4.stl` | 4 | optional | 8270e8cf6c7ba29a7fd11d143c287bd3af576934 | If actual included handles installed; M5x14 + hammerhead per LDO supplement. |
| `STLs/z_rail_stop_x4.stl` | 4 | optional | 8270e8cf6c7ba29a7fd11d143c287bd3af576934 | Captive-rail safety aid; temporary stops needed while handling. |
| `STLs/ldo_bestagon_insert.stl` | 1 | optional | 8270e8cf6c7ba29a7fd11d143c287bd3af576934 | Decorative kit insert only. |
| `STLs/z_belt_cover_a_led.stl` | 2 | optional | 8270e8cf6c7ba29a7fd11d143c287bd3af576934 | Alternative A cover if LED wires route through Z motor opening; not added to stock covers. |
| `STLs/Purge Bucket/brush_holder_sheet_stop.stl` | 0 | replaced/omit | 8270e8cf6c7ba29a7fd11d143c287bd3af576934 | No automatic brass brush route across Cartographer coil; manual initial cleaning. |
| `STLs/Purge Bucket/individual_sheet_stop.stl` | Unverified / unset | unresolved | 8270e8cf6c7ba29a7fd11d143c287bd3af576934 | MRW surface/Wings/probe envelope must determine sheet retention, B1/B5/T4. |
