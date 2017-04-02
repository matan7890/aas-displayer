section_parsers = {}


class MetaSectionParser(type):
    def __init__(cls, name, bases, d):
        super(MetaSectionParser, cls).__init__(name, bases, d)
        if "SECTION_NAME" in d and d["SECTION_NAME"] is not NotImplemented:
            section_name = d["SECTION_NAME"]
            section_parsers[section_name] = cls


class BaseSectionParser(object):
    """
    This class can be used in the future for parsing all the sections of the AAS file. 
    """
    __metaclass__ = MetaSectionParser

    SECTION_NAME = NotImplemented

    def parse(self, section_line):
        raise NotImplementedError()


