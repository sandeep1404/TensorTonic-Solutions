import numpy as np

def chi2_independence(C):
    """
    Compute chi-square test statistic and expected frequencies.
    """
    # Write code here
    C = np.array(C)
    row = np.sum(C,axis=1)
    col = np.sum(C,axis=0)
    total = np.sum(C)
    exp = np.outer(row,col)/total
    out = np.sum((C - exp)**2/exp)

    return out,exp 
    
