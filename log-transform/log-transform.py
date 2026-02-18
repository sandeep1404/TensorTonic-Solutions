import numpy as np
def log_transform(values):
    """
    Apply the log1p transformation to each value.
    """
    # Write code here
    values = np.array(values)
    y =np.log(1+values)

    return y.tolist()