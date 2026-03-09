def differencing(series, order):
    """
    Apply d-th order differencing to the time series.
    """
    # Write code here
    for k in range(order):
        subout =[]
        for i in range(len(series)-1):
            out = series[i+1]- series[i]
            subout.append(out)
        series = subout
        # print(series)
    return subout