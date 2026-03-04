import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here

    if len(y)==0:
        return np.float32(0)

    val, counts = np.unique(y,return_counts=True)
    prob = []
    for i in range(len(counts)):
        pi = counts[i]/sum(counts)
        log = -pi*(np.log2(pi))
        prob.append(log)
    
    out = sum(prob)
    return np.float32(out)

    