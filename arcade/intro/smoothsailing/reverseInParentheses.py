def reverseInParentheses(inputString):
    _opens = list()
    j = 0
    _len = len(inputString)
    while j < len(inputString):
        if inputString[j] == '(':
            _opens.append(j)
        elif inputString[j] == ')':
            i = _opens.pop(len(_opens) - 1)
            s = inputString[i + 1:j][::-1]
            inputString = inputString.replace(inputString[i:j + 1], s, 1)
            j = j - 2
        j = j + 1
    return inputString
