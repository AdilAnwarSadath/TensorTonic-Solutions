import numpy as np

def hinge_loss(y_true, y_score, margin=1.0, reduction="mean") -> float:
    """
    y_true: 1D array of {-1,+1}
    y_score: 1D array of real scores, same shape as y_true
    reduction: "mean" or "sum"
    Return: float
    """
    # Write code here
    y = np.asarray(y_true, dtype=float)
    s = np.asarray(y_score, dtype=float)

    if not np.isin(y, [-1.0, 1.0]).all():
        raise ValueError("y_true must only contain labels from the set {-1, +1}.")

    return float(getattr(np,reduction)(np.maximum(0, margin - y*s)))
    
