import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    # Write code here
    # For a 1D array, axis=-1 evaluates to axis=0.
    # For a 2D array, axis=-1 evaluates to axis=1 (row-wise).
        
    e_x = np.exp(x - np.max(x, axis = -1, keepdims = True))
    sums = np.sum(e_x, axis = -1, keepdims = True)
    return e_x / sums