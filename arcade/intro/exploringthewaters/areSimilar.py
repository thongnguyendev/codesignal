def areSimilar(a, b):
    _swap = 0
    a1 = [x for i,x in enumerate(a) if x != b[i]]
    b1 = [x for i,x in enumerate(b) if x != a[i]]
    for i in range(len(a1)):
        x = a1[i]
        if x == b1[i]: continue
        if i == len(a1) - 1: return False
        if x != b1[i + 1] or a1[i + 1] != b1[i]:
            return False
        if _swap > 0:
            return False
        _swap = 1
        a1[i],a1[i + 1] = a1[i + 1], a1[i]
    return _swap <= 1


def areSimilar2(a, b):
    diff = [i for i,x in enumerate(a) if x != b[i]]
    return True if len(diff) == 0 or (len(diff) == 2 and (a[diff[0]],a[diff[1]]) == (b[diff[1]],b[diff[0]])) else False
