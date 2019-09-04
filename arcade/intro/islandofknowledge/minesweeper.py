import numpy as np


def minesweeper(matrix):
    matrix = [(list(map(int, s))) for s in matrix]
    I = len(matrix)
    J = len(matrix[0])
    y = np.matrix(matrix)
    return [[((y[max(0, i - 1):min(I, i + 2), max(0, j - 1):min(J, j + 2)]).sum() - matrix[i][j]) for j in range(0, J)]
            for i in range(0, I)]
