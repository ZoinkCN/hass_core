"""Base class for Rituals Perfume Genie diffuser entity."""
from __future__ import annotations

from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import RitualsDataUpdateCoordinator

MANUFACTURER = "Rituals Cosmetics"
MODEL = "The Perfume Genie"
MODEL2 = "The Perfume Genie 2.0"


class DiffuserEntity(CoordinatorEntity[RitualsDataUpdateCoordinator]):
    """Representation of a diffuser entity."""

    def __init__(
        self,
        coordinator: RitualsDataUpdateCoordinator,
    ) -> None:
        """Init from config, hookup diffuser and coordinator."""
        super().__init__(coordinator)
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, coordinator.diffuser.hublot)},
            manufacturer=MANUFACTURER,
            model=MODEL if coordinator.diffuser.has_battery else MODEL2,
            name=coordinator.diffuser.name,
            sw_version=coordinator.diffuser.version,
        )

    @property
    def available(self) -> bool:
        """Return if the entity is available."""
        return super().available and self.coordinator.diffuser.is_online
