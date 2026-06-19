"""Tests for Universal Remote diagnostics."""

from custom_components.universal_remote.const import (
    CONF_INFRARED_ENTITY_ID,
    CONF_REMOTE_COMMANDS,
    CONF_REMOTE_DEVICE_TYPE,
    CONF_REMOTE_ID,
    CONF_REMOTE_NAME,
    DEVICE_TYPE_GENERIC,
    DOMAIN,
)
from custom_components.universal_remote.diagnostics import (
    async_get_config_entry_diagnostics,
)
from homeassistant.core import HomeAssistant

from pytest_homeassistant_custom_component.common import MockConfigEntry


async def test_diagnostics_supports_single_entry_remote(
    hass: HomeAssistant,
    infrared_entity: str,
) -> None:
    """Test diagnostics supports one universal remote per config entry storage."""
    entry = MockConfigEntry(
        domain=DOMAIN,
        title="TV",
        data={
            CONF_REMOTE_ID: "tv",
            CONF_REMOTE_NAME: "TV",
            CONF_INFRARED_ENTITY_ID: infrared_entity,
            CONF_REMOTE_DEVICE_TYPE: DEVICE_TYPE_GENERIC,
        },
        options={CONF_REMOTE_COMMANDS: {"POWER_ON": "38000:1,2"}},
    )

    diagnostics = await async_get_config_entry_diagnostics(hass, entry)

    assert diagnostics["summary"] == {
        "remote_count": 1,
        "command_count": 1,
        "button_count": 0,
        "media_player_count": 0,
        "missing_infrared_entity_count": 0,
    }
    assert diagnostics["universal_remote"] == {
        "id": "tv",
        "name": "TV",
        "infrared_entity_id": infrared_entity,
        "infrared_entity_exists": True,
        "infrared_entity_available": True,
        "device_type": DEVICE_TYPE_GENERIC,
        "codeset": "__none__",
        "media_player_expected": False,
        "button_count": 0,
        "source_count": 0,
        "command_count": 1,
        "commands": ["POWER_ON"],
    }
    assert "universal_remotes" not in diagnostics
