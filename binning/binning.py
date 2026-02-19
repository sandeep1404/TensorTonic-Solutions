import numpy as np
def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here
    min_val = min(values)
    max_val = max(values)
    if min_val==max_val:
        return np.zeros(len(values)).tolist()
    if num_bins==0:
        return 
    width = (max_val - min_val)/num_bins
    res=[]
    for ele in values:
        # if ele< width:
        #     y = ((ele - min_val)/width)
        # else:
        y = int(min(((ele - min_val)/width),num_bins-1))
        res.append(y)

    return res
        