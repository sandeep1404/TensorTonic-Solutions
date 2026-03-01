def target_encoding(categories, targets):
    """
    Replace each category with the mean target value for that category.
    """
    # Write code here
    unique= list(set(categories))
    i=0
    out = {}
    for ele in unique:
        out[ele]=[]
    for ele in categories:
        # if ele in unique:
        categories.index(ele, i,len(categories))
        val = targets[i]
        out[ele].append(val)
        i+=1
    mean_val = {}
    for ele in out.keys():
        val= sum(out[ele])/len(out[ele])
        mean_val[ele]=val
    output=[]
    for ele in categories:
        output.append(mean_val[ele])
    return output
    
        
    