import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    # Write code here
    x= np.array(x)

    output = np.zeros(x.shape)

    x= np.array(x)
    shape_out= np.array(x).shape
    rng_ = np.random.default_rng(rng) 
    random_mat = rng_.random(shape_out)
    out = np.where(random_mat<1-p, x*(1/(1-p)), 0 )
    mask = np.where(out!=0, out/x, 0)

    return (out,mask)