import numpy as np
def k_means_centroid_update(points, assignments, k):
    """
    Compute new centroids as the mean of assigned points.
    """
    # Write code here

    out = [np.zeros((1,k)).tolist()[0] for i in range(k)]

    clusterids, counts = np.unique(assignments,return_counts=True)
    # print(f'the cluster ids are {clusterids}')
    # print(f'the len of the cluster ids are {len(clusterids)}')
    for i in range(len(clusterids)):
        print(f'the cluster now is {clusterids[i]}')
        ## get the indexs of all the common cluster ids
        index_cluster = np.where(assignments==clusterids[i])
        # print(index_cluster)
    
        # for i in index_cluster[0]:
        #     print(i)
        ## get the elements of the correspoding cluster based on the index
    
        points_cluster = np.array([points[i] for i in index_cluster[0]])
    
        if len(points_cluster)==0:
            return 0
            
    
        ### now get the centroid for each point and append it to out
        centroid_cluster = points_cluster.sum(axis=0)/len(points_cluster)
        
        ## append the centroid to clster id 
        out[i]= centroid_cluster.tolist()
    
    return  out
    
        