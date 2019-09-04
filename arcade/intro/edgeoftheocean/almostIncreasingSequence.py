def almostIncreasingSequence(sequence):
    _len = len(sequence)
    if _len <= 2:
        return True
    sequence.insert(0, -100001)
    sequence.append(100001)
    found = 0
    for i in range(1, _len):
        _pre = sequence[i - 1]
        _next = sequence[i + 2]
        a = sequence[i]
        b = sequence[i + 1]
        if b > a: continue
        if found > 0: return False
        if b > _pre or _next > a:
            found = 1
        else:
            return False
    return found <= 1
