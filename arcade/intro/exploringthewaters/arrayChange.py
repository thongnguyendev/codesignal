def arrayChange(inputArray):
    change = 0
    for i in range(1, len(inputArray)):
        if inputArray[i] > inputArray[i - 1]: continue
        change = change + inputArray[i - 1] + 1 - inputArray[i]
        inputArray[i] = inputArray[i - 1] + 1
    return change

