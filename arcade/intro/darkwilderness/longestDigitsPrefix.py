def longestDigitsPrefix(inputString):
    a = [i for i in range(len(inputString)) if not inputString[i].isdigit()]
    return inputString[:a[0]] if len(a) > 0 else inputString
