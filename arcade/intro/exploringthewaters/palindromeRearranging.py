from collections import Counter


def palindromeRearranging(inputString):
    a = {}
    for c in inputString:
        if c in a:
            a[c] = a[c] + 1
        else:
            a[c] = 1
    b = [x & 1 for k, x in a.items()]
    return sum(b) <= 1


def palindromeRearranging2(inputString):
    a = Counter(inputString)
    b = [x & 1 for k, x in a.items()]
    return sum(b) <= 1
