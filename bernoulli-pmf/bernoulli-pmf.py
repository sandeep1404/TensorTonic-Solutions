import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    # Write code here
    mean = p 
    x= np.array(x)
    var = p*(1-p)
    
    pmf = np.where(x==1,p,1-p)

    return pmf, mean,var