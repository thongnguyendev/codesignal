def sumDigit(s):
    return sum(map(int, s))


def isLucky(n):
    s = str(n)
    s1 = s[:(len(s) + 1) // 2]
    s2 = s[(len(s) + 1) // 2:]
    return sumDigit(s1) == sumDigit(s2)

