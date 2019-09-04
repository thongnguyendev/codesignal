def arrayMaxConsecutiveSum(inputArray, k):
    i = 0
    j = len(inputArray) - k
    _max = sum(inputArray[i:k])
    pre = _max
    while i < j:
        i = i + 1
        pre = pre - inputArray[i - 1] + inputArray[i + k - 1]
        _max = max(pre, _max)
    return _max
