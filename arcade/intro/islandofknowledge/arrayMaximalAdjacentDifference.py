def arrayMaximalAdjacentDifference(inputArray):
    return max(*[abs(x - inputArray[i + 1]) for i, x in enumerate(inputArray[:-1])])
