import numpy as np


def specific_values_matrix():
    result = np.ones((5, 5))
    zeros = np.zeros((3, 3))
    zeros[1, 1] = 9

    result[1:4, 1:4] = zeros

    return result
