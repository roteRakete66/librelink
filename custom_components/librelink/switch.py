"""Switch platform for librelink."""

from __future__ import annotations

from homeassistant.components.switch import SwitchEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_USERNAME
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import CONF_PATIENT_ID, DOMAIN
from .coordinator import LibreLinkDataUpdateCoordinator
from .sensor import LibreLinkSensorBase


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
):
    """Set up the switch platform."""
    coordinator: LibreLinkDataUpdateCoordinator = hass.data[DOMAIN][
        config_entry.data[CONF_USERNAME]
    ]

    pid = config_entry.data[CONF_PATIENT_ID]

    async_add_entities([LibreLinkPlusSwitch(coordinator, pid)])


class LibreLinkPlusSwitch(LibreLinkSensorBase, SwitchEntity):
    """Switch to add 1 day to expiration timestamp."""

    def __init__(self, coordinator: LibreLinkDataUpdateCoordinator, pid: str) -> None:
        """Initialize the switch."""
        super().__init__(coordinator, pid)
        self._attr_name = "Is Plus"
        self._attr_icon = "mdi:alarm-plus"

    @property
    def is_on(self) -> bool:
        """Return true if switch is on."""
        return self.coordinator.is_plus_map.get(self.id, False)

    async def async_turn_on(self, **kwargs) -> None:
        """Turn the switch on."""
        self.coordinator.is_plus_map[self.id] = True
        self.async_write_ha_state()
        self.coordinator.async_set_updated_data(self.coordinator.data)

    async def async_turn_off(self, **kwargs) -> None:
        """Turn the switch off."""
        self.coordinator.is_plus_map[self.id] = False
        self.async_write_ha_state()
        self.coordinator.async_set_updated_data(self.coordinator.data)
