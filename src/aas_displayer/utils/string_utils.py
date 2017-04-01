import re


def camel_case_to_snake_case(camel_string):
    """
    This function converts CamelCase strings to snake_case strings.
    Taken from: https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case

    :param camel_string: the camel cased string that needs to be converted to snake_string
    :type camel_string: str
    :return: a snake_cased string.
    :rtype: str
    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel_string)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
