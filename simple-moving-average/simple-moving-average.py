def simple_moving_average(values, window_size):
    """
    Compute the simple moving average of the given values.
    """
    # Write code here

    output=[]
    if window_size==0:
        return []
 
    for i in range(len(values)-window_size+1):
        nom = 0 
        for j in range(window_size):
            nom += values[i+j] ## take this as per window size 
        val = nom/window_size
        output.append(val)
    return output
