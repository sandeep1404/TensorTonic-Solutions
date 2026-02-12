import numpy as np
def xavier_initialization(W, fan_in, fan_out):
    """
    Scale raw weights to Xavier uniform initialization.
    """
    # Write code here

    l = np.sqrt(6/(fan_in+fan_out))

    w =np.array(W)

    w_ = (w*2*l) - l 

    w_= w_.tolist()
    return w_