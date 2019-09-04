import re


def variableName(name):
    if re.match('[a-z_][0-9a-z_]*$', name, re.IGNORECASE):
        return True
    return False


def variableName2(name):
    return name.isidentifier()
