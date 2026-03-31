import numpy as np
import math

def gelu_scalar(x):
    out = 0.5*x*(1+math.erf(x/math.sqrt(2)))
    return out

def gelu(x):
    """
    Compute the Gaussian Error Linear Unit (exact version using erf).
    x: list or np.ndarray
    Return: np.ndarray of same shape (dtype=float)
    """
    # Write code here
    
    val = gelu_scalar
    print(val)

    z= np.vectorize(val)(x)

    return z