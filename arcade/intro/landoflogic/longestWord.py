import re


def longestWord(t):
    a = re.findall(r'[a-zA-Z]+', t)
    return max(a, key=len)
