import numpy as np

def focal_loss(p, y, gamma=2.0):
    """
    Compute Focal Loss for binary classification.
    """
    # Write code here
    p = np.array(p)
    y = np.array(y)

    p = np.where(p!=0,p,np.clip(p,1e-15,1-1e-15))
    # print(p)
    term1 = ((1-p)**gamma)*y*(np.log(p))
    # print(term1)
    term2 = (p**gamma)*(1-y)*(np.log(1-p))
    # print(term2)
    loss = -(term1+term2)
    # print(loss)
    out = np.mean(loss)

    return out
