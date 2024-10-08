def mat_mult(A, B):
    size = len(A)
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += A[i][k] * B[k][j]
    return result

def identity_matrix(size):
    return [[1 if i == j else 0 for j in range(size)] for i in range(size)]

def matrix_power(A, n):
    size = len(A)
    
    result = identity_matrix(size)
    
    while n > 0:
        if n % 2 == 1:
            result = mat_mult(result, A)  # Multiply if n is odd
        A = mat_mult(A, A)  # Square the matrix
        n //= 2
    
    return result
  
