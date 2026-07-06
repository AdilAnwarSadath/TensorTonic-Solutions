import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    w = np.zeros(X.shape[1])
    b = 0
    N = len(X)

    for i in range(steps):
        
        lin = X @ w + b
        p = _sigmoid(lin)
        error = p-y

        d_w = (X.T @ error)/N
        d_b = error.mean()
        
        w -= lr * d_w
        b -= lr * d_b
    
    
    
    return w,b