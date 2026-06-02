import numpy as np

def one_hot(y, num_classes=None):
    """
    Convert integer labels y ∈ {0,...,K-1} into one-hot matrix of shape (N, K).
    """
    # Write code here

    y = np.array(y)

    if num_classes is None or num_classes==None:
        num_classes = np.max(y) + 1

    out = np.zeros((len(y),num_classes))
    out[np.arange(len(y)),y]=1

    return out 
    
        