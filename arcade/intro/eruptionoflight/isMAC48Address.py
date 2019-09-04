import re


def isMAC48Address(s):
    a = s.split('-')
    return False if len(a) != 6 else len([s for s in a if len(s) == 2 and re.match('[A-F0-9]*$', s)]) == 6
