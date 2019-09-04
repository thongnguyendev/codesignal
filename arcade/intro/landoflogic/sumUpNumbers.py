import re


def sumUpNumbers(s):
    return sum(list(map(int, re.findall(r'[0-9]+', s))))
