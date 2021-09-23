"""Represent a light."""
from pytradfri.color import supported_features
from pytradfri.const import (
    ATTR_DEVICE_STATE,
    ATTR_LIGHT_COLOR_HEX,
    ATTR_LIGHT_COLOR_HUE,
    ATTR_LIGHT_COLOR_SATURATION,
    ATTR_LIGHT_COLOR_X,
    ATTR_LIGHT_COLOR_Y,
    ATTR_LIGHT_CONTROL,
    ATTR_LIGHT_DIMMER,
    ATTR_LIGHT_MIREDS,
    SUPPORT_BRIGHTNESS,
    SUPPORT_COLOR_TEMP,
    SUPPORT_HEX_COLOR,
    SUPPORT_XY_COLOR,
)


class Light:
    """Represent a light.

    https://github.com/IPSO-Alliance/pub/blob/master/docs/IPSO-Smart-Objects.
    pdf
    """

    def __init__(self, device, index):
        """Setup object of class."""
        self.device = device
        self.index = index

    @property
    def supported_features(self):
        """Return supported features."""
        return supported_features(self.raw)

    @property
    def state(self):
        """Return device state."""
        return self.raw.get(ATTR_DEVICE_STATE) == 1

    @property
    def dimmer(self):
        """Return dimmer if present."""
        if self.supported_features & SUPPORT_BRIGHTNESS:
            return self.raw.get(ATTR_LIGHT_DIMMER)

    @property
    def color_temp(self):
        """Return color temperature."""
        if self.supported_features & SUPPORT_COLOR_TEMP:
            if self.raw.get(ATTR_LIGHT_MIREDS) != 0:
                return self.raw.get(ATTR_LIGHT_MIREDS)

    @property
    def hex_color(self):
        """Return hex color."""
        if self.supported_features & SUPPORT_HEX_COLOR:
            return self.raw.get(ATTR_LIGHT_COLOR_HEX)

    @property
    def xy_color(self):
        """Return xy color."""
        if self.supported_features & SUPPORT_XY_COLOR:
            return (self.raw.get(ATTR_LIGHT_COLOR_X), self.raw.get(ATTR_LIGHT_COLOR_Y))

    @property
    def hsb_xy_color(self):
        """Return hsb xy color."""
        return (
            self.raw.get(ATTR_LIGHT_COLOR_HUE),
            self.raw.get(ATTR_LIGHT_COLOR_SATURATION),
            self.raw.get(ATTR_LIGHT_DIMMER),
            self.raw.get(ATTR_LIGHT_COLOR_X),
            self.raw.get(ATTR_LIGHT_COLOR_Y),
        )

    @property
    def raw(self):
        """Return raw data that it represents."""
        return self.device.raw[ATTR_LIGHT_CONTROL][self.index]

    def __repr__(self):
        """Return representation of class object."""
        state = "on" if self.state else "off"
        return (
            "<Light #{} - "
            "name: {}, "
            "state: {}, "
            "dimmer: {}, "
            "hex_color: {}, "
            "xy_color: {}, "
            "hsb_xy_color: {}, "
            "supported features: {} "
            ">".format(
                self.index,
                self.device.name,
                state,
                self.dimmer,
                self.hex_color,
                self.xy_color,
                self.hsb_xy_color,
                self.supported_features,
            )
        )
