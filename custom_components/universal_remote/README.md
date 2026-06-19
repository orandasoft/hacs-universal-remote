# Universal Remote

The Universal Remote integration creates infrared-controlled Home Assistant devices backed by existing Home Assistant `infrared` entities.

A universal remote does not communicate with infrared hardware directly. It stores named infrared commands and asks the linked `infrared` entity to transmit them.

This makes it possible to use one infrared transmitter for multiple logical devices, such as TVs, receivers, projectors, or other infrared-controlled equipment.

---

## Requirements

Universal Remote requires at least one Home Assistant `infrared` entity from another integration.

The linked `infrared` entity is responsible for transmitting infrared commands through compatible hardware such as IR blasters or infrared emitters.

---

## Entities

Each configured universal remote creates a `remote` entity.

Depending on the configured device type and commands, it can also create:

- `button` entities for commands where button creation is enabled.
- a `media_player` entity for TV remotes.

The TV media player is assumed-state. Its supported controls are derived from the commands configured for the universal remote.

---

## Device types and codesets

Universal remotes can be configured as a generic remote or as a supported device type such as TV.

Device type controls which device-oriented entities can be created. For example, TV remotes create a TV `media_player` entity.

A codeset is an optional infrared command library profile. Codesets are filtered by device type and can be used to import commands during setup or later from the options flow.

---

## Commands

Commands are named infrared payloads. Command names are normalized to uppercase with underscores.

Supported command payload formats include:

- Pronto Hex
- raw timing lists
- raw timing objects
- text-based timing formats

Commands may also be imported from a supported infrared library codeset.

---

## Buttons

Command button entities are optional. When adding or importing commands, the flow can create button entities for those commands.

Buttons are regular Home Assistant `button` entities. Pressing a button sends the stored infrared command through the linked infrared entity.

---

## TV media player

TV remotes create a `media_player` entity. The media player does not provide real TV state; it exposes supported features based on configured command names.

Examples:

- `POWER_ON` enables turn on.
- `POWER_OFF` enables turn off.
- `VOLUME_UP` and `VOLUME_DOWN` enable volume step.
- `MUTE` enables mute.
- `CHANNEL_UP` and `CHANNEL_DOWN` enable next and previous track.
- `PLAY`, `PAUSE`, and `STOP` enable playback controls.
- source commands such as `HDMI_1`, `TV`, `DTV`, `BS`, or app shortcuts can appear in the source list.

---

## Remote service example

```yaml
action: remote.send_command
target:
  entity_id: remote.living_room_tv
data:
  command: POWER_ON
```

---

## Availability

Universal Remote entities are available when the linked infrared entity exists and is available.

If the linked infrared entity is missing or unavailable, the integration creates a repair issue to help the user update the configuration.

---

## Notes

- Multiple universal remote config entries may share the same infrared entity.
- Existing commands are not deleted automatically when changing device type or codeset.
- Infrared transmission is handled by the linked infrared integration.
