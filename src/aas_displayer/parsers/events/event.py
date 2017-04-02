from __future__ import print_function, unicode_literals

import abc

from aas_displayer.utils.aas_time import AASTime, AAS_TIME_SEPARATOR


class Event(object):
    """
    This class represents a base for any event line in an AAS file.
    """
    __metaclass__ = abc.ABCMeta
    _TYPE = NotImplemented  # type: str

    def __init__(self, start="", end="", style="", name="", margin_l=0, margin_r=0, margin_v=0, effect="", text="", **kwargs):
        self.start = AASTime(*start.split(AAS_TIME_SEPARATOR))
        self.end = AASTime(*end.split(AAS_TIME_SEPARATOR))
        self.style = style
        self.name = name
        self.margin_l = margin_l
        self.margin_r = margin_r
        self.margin_v = margin_v
        self.effect = effect
        self.text = text
        if self.end < self.start:
            raise ValueError("You can't finish an event before starting it! (starting time: {} > ending time: {}"
                             .format(self.start, self.end))

    def amount(self):
        """
        :return: the amount of time passed between start time and end time, in seconds (assumes both are in seconds)
        :rtype: float
        """
        return self.end - self.start

    @staticmethod
    def should_display():
        return False

    def display(self):
        print(self)

    def __str__(self):
        return "{}: start: {}, end: {}, text: {}".format(self._TYPE, self.start, self.end, self.text)