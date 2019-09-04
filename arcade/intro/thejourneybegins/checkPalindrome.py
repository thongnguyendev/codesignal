def checkPalindrome(inputString):
    i = 0
    j = len(inputString) - 1
    while i <= j:
        if inputString[i] != inputString[j]:
            return False
        i += 1
        j -= 1
    return True


def checkPalindrome2(s):
    return s == s[::-1]
