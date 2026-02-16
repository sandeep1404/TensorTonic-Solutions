import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    x = np.array(x)
    mean = np.mean(x)

    var = sum(np.square(x-mean))/(len(x)-1)
    sd = np.sqrt(var)

    return var, sd

    