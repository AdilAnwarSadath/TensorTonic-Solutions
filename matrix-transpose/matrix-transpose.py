import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    inp = np.asarray(A,dtype=float)

    row = inp.shape[0]
    col = inp.shape[1]

    out = np.ones((col,row),dtype=float)

    for i in range(row):
        for j in range(col):
            out[j][i] = inp[i][j]
    
    
    return out
