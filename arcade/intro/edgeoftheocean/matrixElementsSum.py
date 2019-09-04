def matrixElementsSum(matrix):
    _max = sum(matrix[0])
    for i in range(1, len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i - 1][j] == 0:
                matrix[i][j] = 0
            _max += matrix[i][j]
    return _max


