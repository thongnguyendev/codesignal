def isBeautifulString(inputString):
    a = [inputString.count(chr(i)) for i in range(97, 123)]
    return len([i for i in range(len(a) - 1) if a[i] < a[i + 1]]) == 0
