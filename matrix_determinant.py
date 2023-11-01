def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2:
        a, b = matrix[0]
        c, d = matrix[1]
        return a * d - b * c

    det = 0
    for i in range(len(matrix)):
        minor = [row[:i] + row[i+1:] for row in matrix[1:]]
        det += matrix[0][i] * determinant(minor) * (-1) ** i

    return det

the_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = determinant(the_matrix)
print(result)

#Very simple solution
#import numpy as np
#def determinant(a):
#    return round(np.linalg.det(np.matrix(a)))