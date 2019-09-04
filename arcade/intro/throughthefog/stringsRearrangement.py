def countStringDiff(s1, s2):
    return sum([0 if c == s2[i] else 1 for i, c in enumerate(s1)])


def go(current, nexts, indexs, array):
    if set(current) == array:
        return True
    _len = len(current)
    for i in nexts:
        if i in current:
            continue
        current.append(i)
        if go(current, indexs[i], indexs, array):
            return True
        current.pop(_len)
    return False


def stringsRearrangement(a):
    b = [[j for j, s2 in enumerate(a) if j != i and countStringDiff(s1, s2) == 1] for i, s1 in enumerate(a)]
    c = [len(x) for x in b]
    if 0 in c:
        return False
    if c.count(1) > 2:
        return False
    indexs = [i for i in range(len(a))]
    return go(list(), indexs, b, set(indexs))
