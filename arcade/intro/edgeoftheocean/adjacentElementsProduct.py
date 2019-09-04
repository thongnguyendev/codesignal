def adjacentElementsProduct(inputArray):
    __max = -999999999
    _len = len(inputArray)
    if _len == 2:
        return inputArray[0] * inputArray[1]
    for i in range(_len - 1):
        a = inputArray[i] * inputArray[i + 1]
        __max = max(__max, a)
    return __max


def adjacentElementsProduct2(arr):
    return max([arr[i] * arr[i+1] for i in range(len(arr)-1)])

