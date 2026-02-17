import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    # Write code here
    X = np.array(X)
    # if axis==1:
    #     return 
    min_x = np.min(X,axis=axis,keepdims=True)
    max_x= np.max(X,axis=axis,keepdims=True)
    if min_x.all()==max_x.all():
        out =(X-min_x)/((max_x-min_x)+eps)
    else:
        out =(X-min_x)/(max_x-min_x)

    return out
    