def frequency_encoding(values):
    """
    Replace each value with its frequency proportion.
    """
    # Write code here

    count= {}
    for ele in values:
        if ele in count.keys():
            count[ele]+=1
        else:
            count[ele]=1
    out =[]
    for ele in values:
        if ele in count.keys():
            val= count[ele]/sum(count.values())
            out.append(val)   
    return out