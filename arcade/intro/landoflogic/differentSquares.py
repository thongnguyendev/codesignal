def differentSquares(m):
    a = set()
    for i in range(len(m) - 1):
        for j in range(len(m[0]) - 1):
            x = str(m[i][j]) + str(m[i][j + 1]) + str(m[i + 1][j]) + str(m[i + 1][j + 1])
            a.add(x)
    return len(a)
