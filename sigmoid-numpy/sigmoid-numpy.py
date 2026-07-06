import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    inp = np.asarray(x, dtype=float)

    res= np.where(
        inp >= 0,
        1 / (1 + np.exp(-inp)),
        np.exp(inp) / (1 + np.exp(x))
    )
    return res
