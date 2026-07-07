def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    x = float(x0)
    for i in range(steps):
        
        d_f = 2*a*x + b
        x -= d_f * lr

    return x