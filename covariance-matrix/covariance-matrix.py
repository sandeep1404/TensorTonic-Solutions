import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    X= np.array(X)
    mu = np.mean(X,axis=0)
    xmu =X - mu
    samples = xmu.shape[0]
    if samples==1 or X.ndim==1:
        return None
    else:
        out= np.matmul(np.transpose(xmu),xmu)/(samples-1)
        return out
