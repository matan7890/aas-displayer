from aas_displayer.parsers.events.event import Event
from aas_displayer.parsers.sections.base_section import BaseSectionParser

TYPE_SEPARATOR = ":"

FIELDS_SEPARATOR = ","


class EventParser(BaseSectionParser):
    def __init__(self, format_line):
        """
        This object gets the format of the events in the AAS file (the first line of the Event section)
        and then it is able to parse the other lines of the Event section.

        :param format_line:
        :type format_line: str
        """
        field_type, format_fields = self._parse_line(format_line)
        if field_type != "Format":
            raise ValueError("A format line of the Event section should start with the string \"Format: \"!"
                             "\nLine: {line}".format(line=format_line))
        self.format_fields = map(lambda s: s.lower().strip(), format_fields)

    def parse(self, line):
        """
        Parses a line of the ASS file which located

        :param line: the event line that is needed to be parsed.
        :type line: str
        :return: An Event object of the specific event

        """
        line_type, line_fields = self._parse_line(line)
        for event_type in Event.__subclasses__():
            event_fields = self._match_fields(line_fields)
            if event_type._TYPE.lower() == line_type.lower():
                return event_type(**event_fields)
        raise ValueError("Unknown type of event: {type} in the line: {line}".format(type=line_type, line=line))

    @staticmethod
    def _parse_line(line):
        """
        Parses the event line and return the type of the event and the corresponding fields as separated by ", ".
        Be aware that the "text" field might contain many "," chars and so it

        :param line: a line in the event section from the AAS file.
        :return:
        :rtype: tuple[str, list[str]]
        """
        split_format = line.split(TYPE_SEPARATOR)
        type_ = split_format[0]
        splited_fields = TYPE_SEPARATOR.join(split_format[1:]).split(FIELDS_SEPARATOR)
        return type_, splited_fields

    def _match_fields(self, line_fields):
        # The text field might have more then 1 "," so we need to join it back together.
        # Assuming "Text" field is always the last field, as specified in the specification, i'll get the amount of
        # fields in order to understand from where the Text field starts and then join it.
        fields_without_text = self.format_fields[:-1]
        text_field_in_the_line = FIELDS_SEPARATOR.join(line_fields[len(fields_without_text):])
        line_fields = line_fields[:len(fields_without_text)] + [text_field_in_the_line]

        field_to_value = dict(zip(self.format_fields, line_fields))
        return field_to_value




