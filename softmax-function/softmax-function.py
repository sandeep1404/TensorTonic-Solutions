import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    # Write code here
    x = np.array(x)

    if x.ndim ==1 :
        x = np.subtract(x,max(x))
        nom = np.exp(x)
        denom = np.sum(nom)
        ans = nom/denom
        ans= ans.tolist()
    else:
        nom = np.exp(x)
        denom = np.sum(nom,axis=1).reshape(np.sum(nom,axis=1).shape[0],1)
        ans = nom/denom
        ans.tolist()
    
    return ans
