import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x = np.array(x)

    nom = np.exp(x) - np.exp(-x)
    denom = np.exp(x) + np.exp(-x)

    out = nom/denom

    return out 

