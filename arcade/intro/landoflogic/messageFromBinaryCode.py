def messageFromBinaryCode(code):
    i = 0
    s = ""
    l = len(code)
    while i < l:
        s = s + chr(int(code[i:i + 8], 2))
        i += 8
    return s
