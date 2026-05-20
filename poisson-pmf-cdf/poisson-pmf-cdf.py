import numpy as np
import math

def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    """
    # Write code here

    nom = np.exp(-lam)*lam**k
    denom = math.factorial(k)

    pmf = nom/denom ## p(x=k)

    cdf=0
    for i in range(k+1):
        nom_i = np.exp(-lam)*lam**i
        denom_i = math.factorial(i)
        pmf_i = nom_i/denom_i ## p(x=k)
        cdf+= pmf_i


    return pmf,cdf