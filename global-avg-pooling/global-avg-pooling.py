import numpy as np

def global_avg_pool(x):
    """
    Compute global average pooling over spatial dims.
    Supports (C,H,W) => (C,) and (N,C,H,W) => (N,C).
    """
    # Write code here
    x= np.array(x)

    if x.ndim==4:
        hw = (x.shape[2])*(x.shape[3])
        nom = np.sum(x,axis = (2,3))

        return nom/hw
        
    elif x.ndim == 3:
        hw = (x.shape[1])*(x.shape[2])
        nom = np.sum(x,axis = (1,2))

        return nom/hw
    else:
        raise ValueError

    
        
        
        