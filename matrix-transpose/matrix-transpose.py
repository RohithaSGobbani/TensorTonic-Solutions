import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    A = np.array(A)
    m = A.shape[0]
    n = A.shape[1]
    transposeA = np.zeros((n,m))
    for i in range(n):
        for j in range(m):
            transposeA[i][j] = A[j][i]
    
    return transposeA
