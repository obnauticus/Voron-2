# Non-deployable configuration examples

Every line is commented. Examples document a specific candidate hardware/firmware generation and deliberately omit unknown IDs, offsets, PID and travel values. They cannot be used as printer.cfg. A board-revision gate comes before selecting a sample; an electrical gate comes before connecting or heating.

- [cartographer-v4-survey-usb.cfg.example](../config/cartographer-v4-survey-usb.cfg.example) — read its target and prerequisites before selecting.
- [leviathan-v1.3-usb.cfg.example](../config/leviathan-v1.3-usb.cfg.example) — read its target and prerequisites before selecting.
- [nitehawk-sb-original-pt1000.cfg.example](../config/nitehawk-sb-original-pt1000.cfg.example) — read its target and prerequisites before selecting.
- [nitehawk-sb-v2-pt1000.cfg.example](../config/nitehawk-sb-v2-pt1000.cfg.example) — read its target and prerequisites before selecting.

Do not mix original SB RP2040 pins with SB V2 STM32G0 pins, old Cartographer Classic directives with the new Survey plugin, or F446 firmware headers with Leviathan V1.3 H743. Follow [software](../chapters/08-software.md) after its gates.
