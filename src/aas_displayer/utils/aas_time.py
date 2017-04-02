from __future__ import unicode_literals
import datetime as dt

AAS_TIME_SEPARATOR = ":"


class AASTime(dt.time):
    def __new__(cls, hours="0", minutes="0", seconds="0.0"):
        if "." not in seconds:
            seconds = seconds + ".00"
        seconds = float(seconds)
        # If seconds were 12.34 for example, they will become 1234 - 1200 = 34
        hundredths = float(seconds) * 100 - int(float(seconds)) * 100
        cls.hundredth = hundredths
        return super(AASTime, cls).__new__(cls, *map(int, [hours, minutes, seconds, hundredths * 10000]))

    def to_milliseconds(self):
        return self.to_seconds() * 1000

    def to_seconds(self):
        return float(self.hour) * 60 * 60 + float(self.minute) * 60 + self.second + float(self.hundredth) / 100

    def __str__(self):
        return "{}:{}:{}:{}".format(*map(_fill_number, (self.hour, self.minute, self.second, self.hundredth)))


def _fill_number(number):
    return str.zfill(str(number), 2)
