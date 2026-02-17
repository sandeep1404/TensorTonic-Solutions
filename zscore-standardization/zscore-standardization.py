import numpy as np

def zscore_standardize(X, axis=0, eps=1e-12):
    """
    Standardize X: (X - mean)/std. If 2D and axis=0, per column.
    Return np.ndarray (float).
    """
    # Write code here
    x= np.array(X)
    mean = np.mean(x,axis=axis,keepdims=True)
    std = np.std(x,axis=axis,keepdims=True)

    if (std==0).any:
        out = (x-mean)/(std+eps)
    else:
        out = (x-mean)/(std)
    return out