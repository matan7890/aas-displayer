from aas_displayer.consts import section_types
from aas_displayer.parsers.events.parser import EventParser


class ASSFile(object):
    def __init__(self, file_text):
        """
        This object will handle all the AAS file format parsing.
        It gives a simple api to read information about the AAS file

        :param file_text: the text of the file
        :type file_text: str
        """
        self._file_text_lines = file_text.splitlines()
        # TODO: Better OOP handling of the sections parsing, so parsing all the sections will be done with one iteration.
        self.events = self._parse_events()

    def _parse_events(self):
        """
        Reads the lines of the file and parses only the Events section from it.
        """
        event_lines = get_section_lines(self._file_text_lines, section_types.EVENTS)
        format_line = event_lines[0]
        event_lines = event_lines[1:]
        parser = EventParser(format_line)
        return [parser.parse(line) for line in event_lines]


def get_section_lines(file_lines, wanted_section):
    """
    This function gets the lines

    :param file_lines: list of the text lines in the AAS function
    :type file_lines: list[str]
    :param wanted_section: the name of the section you want the lines from, probably constant from
           aas_displayer.consts.section_types
    :type wanted_section: str
    :return: the list of lines inside the section
    :rtype: list[str]
    """
    start_line = None
    for idx, line in enumerate(file_lines):
        section = get_section(line)
        if section is not None:
            if section == wanted_section:
                start_line = idx + 1
            elif start_line is not None:
                return file_lines[start_line], file_lines[start_line:idx]
    assert start_line is not None, "Didn't find any event line!"
    return file_lines[start_line:]


def get_section(line):
    """
    Return the section name of a line (without the []) if the line is a section or else None

    :param line: the line to get the section from
    :type line: str
    :return: True if it
    """
    if line.startswith("[") and line.endswith("]"):
        return line[1:-1]
    return None
