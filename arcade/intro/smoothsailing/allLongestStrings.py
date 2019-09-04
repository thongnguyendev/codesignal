def allLongestStrings(inputArray):
    _max = 0
    result = list()
    for s in inputArray:
        _len = len(s)
        if _len > _max:
            _max = _len
            result = list()
            result.append(s)
        elif _len == _max:
            result.append(s)
    return result


def allLongestStrings2(arr):
    _max = max([len(s) for s in arr])
    return [s for s in arr if len(s) == _max]
