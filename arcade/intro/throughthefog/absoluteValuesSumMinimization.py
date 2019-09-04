def absoluteValuesSumMinimization(a):
    b = [[sum([abs(y - x) for y in a]), x] for x in a]
    return min(b, key=lambda x: x[0])[1]


def absoluteValuesSumMinimization2(a):
    return a[(len(a) - 1) // 2]
