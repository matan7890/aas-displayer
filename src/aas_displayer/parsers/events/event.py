class Event(object):
    """
    This class represents a base for any event line
    """
    def __init__(self, marked, start, end, style, name, margin_l, margin_r, margin_v, effect, text, **kwargs):
        self.marked = marked
        self.start = start
        self.end = end
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