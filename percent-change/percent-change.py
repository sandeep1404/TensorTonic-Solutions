def percent_change(series):
    """
    Compute the fractional change between consecutive values.
    """
    # Write code here
    output=[]
    for i in range(len(series)-1):
        nom = series[i+1]- series[i]
        denom = series[i]
        if denom ==0:
            output.append(0)
        else:
            val = nom/denom
            output.append(val)
    return output