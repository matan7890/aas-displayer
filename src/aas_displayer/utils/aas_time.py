from __future__ import unicode_literals
import datetime as dt

AAS_TIME_SEPARATOR = ":"


class AASTime(dt.time):
    def __new__(cls, hours="0", minutes="0", seconds="0.0"):
        if "." not in seconds:
            seconds = seconds + ".00"
        seconds = float(seconds)
        # If seconds were 12.34 for example, they will become "1234" and then 34 will be taken:
        hundredths = float(str(seconds * 100)[2:])
        cls.hundredth = hundredths
        super(AASTime, cls).__new__(cls, *map(int, [hours, minutes, seconds, hundredths * 10000]))

    def __str__(self):
        return "{}:{}:{}:{}".format(*map(_fill_number, (self.hour, self.minute, self.second, self.hundredth)))


def _fill_number(number):
    return str.zfill(str(number), 2)
