def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    # Write code here
    out=[]
    for value in values:
        val=[]
        for i in range(degree+1):
            val.append(value**i)
        out.append(val)

    return out