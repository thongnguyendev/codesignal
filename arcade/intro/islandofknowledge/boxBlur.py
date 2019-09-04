import numpy as np
import math


def boxBlur(image):
    I = len(image)
    J = len(image[0])
    y = np.matrix(image)
    return [[math.floor((y[i - 1:i + 2, j - 1:j + 2]).mean()) for j in range(1, J - 1)] for i in range(1, I - 1)]
