def buildPalindrome(s):
    i = -1
    _len = len(s)
    while i < _len - 1:
        i += 1
        if s[i:] == s[i:][::-1]:
            return s + s[:i][::-1]
    return s + s[:i][::-1]
