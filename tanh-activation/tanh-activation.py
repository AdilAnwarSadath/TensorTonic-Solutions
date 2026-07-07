import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    x = np.asarray(x)
    exp = np.exp(x)
    nexp = np.exp(-x)
    
    return (exp - nexp) / (exp + nexp)