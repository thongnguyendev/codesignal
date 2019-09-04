def makeArrayConsecutive2(statues):
    _min = 9999
    _max = -9999
    _len = len(statues)
    for i in range(_len):
        _min = min(statues[i], _min)
        _max = max(statues[i], _max)
    return _max - _min - _len + 1


def makeArrayConsecutive22(statues):
    _min,_max = min(statues),max(statues)
    return _max - _min - len(statues) + 1

