import numpy as np 

def min_max_scaling(data):
    """
    Scale each column of the data matrix to the [0, 1] range.
    """
    # Write code here

    # data = np.array(data)

    # min_data = np.min(data,axis=0)#.reshape(-1,1)
    # max_data = np.max(data,axis=0)#.reshape(-1,1)
    # range_data = max_data-min_data
    
    # out =(data - min_data)/range_data

    data = np.array(data)


    min_data = np.min(data,axis=0)#.reshape(-1,1). axis = 0 across columns 
    max_data = np.max(data,axis=0)#.reshape(-1,1)
    range_data = max_data-min_data
    
    range_ele = range_data.tolist()
    print(range_ele)
    index_0 = [i for i in range(len(range_ele)) if range_ele[i]==0]
    print(index_0)
    if len(index_0)==0:
        out =(data - min_data)/range_data
    
    else:
        out =(data - min_data)/range_data
        for index in index_0:
            out[:,index] = 0

    return out.tolist()
    