from aas_displayer.parsers.events.event import Event


class Dialogue(Event):
    @staticmethod
    def should_display():
        return True
