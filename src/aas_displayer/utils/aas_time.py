from __future__ import unicode_literals
import datetime as dt


class AASTime(dt.time):

    def __init__(self, hours=0, minutes=0, seconds=0, hundredths=0):
        self.hundredth = hundredths
        super(AASTime, self).__init__(hours, minutes, seconds, hundredths * 10000)

    def __str__(self):
        return "{}:{}:{}:{}".format(*map(_fill_number, (self.hour, self.minute, self.second, self.hundredth)))


def _fill_number(number):
    return str.zfill(str(number), 2)
