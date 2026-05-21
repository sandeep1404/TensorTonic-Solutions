import numpy as np

def clip_gradients(g, max_norm):
    """
    Clip gradients using global norm clipping.
    """
    # Write code here
    
    g = np.array(g)

    if max_norm<=0:
        return g

    norm_g = np.sqrt(np.sum(np.square(g)))

    out = np.where(norm_g<=max_norm,g,g*max_norm/norm_g)

    return out