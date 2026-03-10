def exponential_moving_average(values, alpha):
    """
    Compute the exponential moving average of the given values.
    """
    out = []
    if len(values)==1:
        out.append(values[0])
        return out
    # out =0
  
    for i in range(len(values)):
        if i ==0:
            out.append(values[0])
        else:
            output = alpha*values[i] + (1-alpha)*out[i-1]
            out.append(output)
    
    return out 