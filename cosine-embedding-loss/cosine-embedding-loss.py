def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    dotp = sum(a*b for a,b in zip(x1,x2))
    norm1 = math.sqrt(sum(a*a for a in x1))
    norm2 = math.sqrt(sum(a*a for a in x2))
    cossim = dotp / (norm1 * norm2)

    if label==1:
        return 1-cossim
    elif label==-1:
        return max(0,cossim-margin)
    else:
        raise ValueError ("Blah")

    pass