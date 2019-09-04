import numpy as np


def sudoku(g):
    m = np.matrix(g)
    for i in range(9):
        if len(set(g[i])) != 9:
            return False
        if len(set(m[:, i].A1)) != 9:
            return False
        if i % 3 == 0:
            if any(len(set(m[i:i + 3, 3 * x:3 * x + 3].A1)) != 9 for x in range(3)):
                return False
    return True
