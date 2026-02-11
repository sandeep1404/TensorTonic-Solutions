import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    # Write code here
    x = np.array(x)
    sig = 1/(1+np.exp(-x))

    out = x*sig

    return out
