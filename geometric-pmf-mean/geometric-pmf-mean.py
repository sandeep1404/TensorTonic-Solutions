import numpy as np

def geometric_pmf_mean(k, p):
    """
    Compute Geometric PMF and Mean.
    """
    # Write code here

    mean = 1/p
    k = np.array(k)

    k1= k-1

    pmf =((1-p)**k1)*p

    return (pmf,mean)
    