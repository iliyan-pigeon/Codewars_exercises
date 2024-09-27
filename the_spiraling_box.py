def create_box(m, n):
    # Create an empty n x m matrix filled with 0s
    matrix = [[0] * m for _ in range(n)]
    
    # Number of layers to fill depends on the minimum of height and width
    layers = (min(n, m) + 1) // 2  # Number of layers
    
    for k in range(layers):
        # Fill the top and bottom rows of the current layer
        for i in range(k, m - k):
            matrix[k][i] = k + 1  # Top row
            matrix[n - k - 1][i] = k + 1  # Bottom row
        
        # Fill the left and right columns of the current layer
        for i in range(k, n - k):
            matrix[i][k] = k + 1  # Left column
            matrix[i][m - k - 1] = k + 1  # Right column
    
    return matrix
