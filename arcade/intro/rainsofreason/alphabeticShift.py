def alphabeticShift(inputString):
    return ''.join([chr((ord(x) - 96) % 26 + 97) for x in inputString])

