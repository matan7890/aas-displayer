from aas_displayer.parsers.events.event import Event


class Dialogue(Event):
    TYPE = "DIALOGUE"

    @staticmethod
    def should_display():
        return True
