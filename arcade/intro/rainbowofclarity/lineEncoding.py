def lineEncoding(s):
    r = ""
    i = j = 0
    l = len(s)
    while j < l:
        if s[j] == s[i]:
            j += 1
        else:
            r = r + str("" if j - i == 1 else j - i) + s[i]
            i, j = j, j + 1
    r = r + str("" if j - i == 1 else j - i) + s[i]
    return r
