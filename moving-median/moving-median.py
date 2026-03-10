import numpy as np
def moving_median(values, window_size):
    """
    Compute the rolling median for each window position.
    """
    output = []
    for i in range(len(values)-window_size+1):
        out=[]
        for j in range(window_size):
            out.append(values[i+j])
        output.append(np.median(out))
        
    return output


