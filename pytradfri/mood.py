"""Represent a mood on the gateway."""
from .const import ROOT_MOODS
from .resource import ApiResource


class Mood(ApiResource):
    """Mood."""

    def __init__(self, raw, parent):
        """Setup object of class."""
        super().__init__(raw)
        self._parent = parent

    @property
    def path(self):
        """Path."""
        return [ROOT_MOODS, self._parent, self.id]

    def __repr__(self):
        """Return representation of class object."""
        return "<Mood {} {}>".format(self._parent, self.name)
