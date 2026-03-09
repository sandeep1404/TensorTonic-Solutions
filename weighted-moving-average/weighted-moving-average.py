def weighted_moving_average(values, weights):
    """
    Compute the weighted moving average using the given weights.
    """
    # Write code here

    output =[]
    for i in range(len(values)-len(weights)+1):
        nom=0
        for j in range(len(weights)):
            nom+= weights[j]*values[i+j]
        denom = sum(weights)
        if denom ==0:
            output=[]
        
        val = nom/denom
        output.append(val)
    
    return output