def digitsProduct(p):
    x = -1 if p < 10 else max(-1, *[x for x in range(9, 0, -1) if p % x == 0])
    y = -1 if x < 2 else digitsProduct(p // x)
    return 10 if p == 0 else p if p < 10 else -1 if y == -1 else int(str(y) + str(x))
