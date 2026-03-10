def cumulative_returns(returns):
    """
    Compute the cumulative return at each time step.
    """
    # Write code here
    out=[]
    subout=[]
    for i in range(len(returns)):
        if i == 0:
            val = 1 + returns[i]
            subout.append(val)
            output = val -1 
            out.append(output)
        else:
            val = subout[i-1]*(1+returns[i])
            subout.append(val)
            output = val -1 
            out.append(output)
    
    return out