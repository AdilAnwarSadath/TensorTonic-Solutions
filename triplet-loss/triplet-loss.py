import numpy as np

def dist(x,y):
    return np.sum((x-y)**2, axis=-1)

def triplet_loss(anchor, positive, negative, margin=1.0):
    """
    Compute Triplet Loss for embedding ranking.
    """
    a = np.asarray(anchor)
    p = np.asarray(positive)
    n = np.asarray(negative)

    loss = np.maximum(0, dist(a,p)-dist(a,n)+margin)

    return np.mean(loss)

    
    