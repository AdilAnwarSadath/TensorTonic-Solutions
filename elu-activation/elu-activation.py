import math

def elu(x, alpha):
    # Standard 1D list comprehension using math.exp
    res = [val if val > 0 else alpha * (math.exp(val) - 1) for val in x]
    
    
    return res