from __future__ import print_function, unicode_literals

import abc

from aas_displayer.utils.aas_time import AASTime, AAS_TIME_SEPARATOR


class Event(object):
    """
    This class represents a base for any event line in an AAS file.
    """
    __metaclass__ = abc.ABCMeta
    _TYPE = NotImplemented  # type: str

    def __init__(self, original_line, layer=0, start="", end="", style="", name="", marginl=0, marginr=0, marginv=0, effect="", text="", **kwargs):
        self._original_line = original_line  # for debugging purposes.
        self.layer = int(layer)
        self.start = AASTime(*start.split(AAS_TIME_SEPARATOR))
        self.end = AASTime(*end.split(AAS_TIME_SEPARATOR))
        self.style = style
        self.name = name
        self.margin_l = int(marginl)
        self.margin_r = int(marginr)
        self.margin_v = int(marginv)
        self.effect = effect
        self.text = text
        if self.end < self.start:
            raise ValueError("You can't finish an event before starting it! (starting time: {} > ending time: {}"
                             .format(self.start, self.end))

    @staticmethod
    def should_display():
        return False

    def display(self):
        print(self)

    def __str__(self):
        return "{}: start: {}, end: {}, text: {}".format(self._TYPE, self.start.isoformat(), self.end.isoformat(), self.text)