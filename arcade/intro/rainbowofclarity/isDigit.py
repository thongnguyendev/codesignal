import re


def isDigit(symbol):
    return re.match('[0-9]', symbol) is not None
