def chessKnight(c):
    a = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]
    b = [[ord(c[0]) + x[0], int(c[1]) + x[1]] for x in a]
    return len([x for x in b if 97 <= x[0] <= 104 and 1 <= x[1] <= 8])
