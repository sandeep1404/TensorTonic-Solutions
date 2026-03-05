import numpy as np
def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid.
    """
    # Write code here

    out =[]
    for i in range(len(points)):
        dist=[]
        for j in range(len(centroids)):
            point = points[i]
            centeroid = centroids[j]

            if len(point)==1:
                x= (point[0]-centeroid[0])**2
                distance = np.sqrt(x)
                dist.append(distance)
            else:
                x= (point[0]-centeroid[0])**2
                y = (point[1]-centeroid[1])**2
                distance = np.sqrt(x+y)
                dist.append(distance)
            
            # x= (point[0]-centeroid[0])**2
            # y = (point[1]-centeroid[1])**2
            # distance = np.sqrt(x+y)
            # dist.append(distance)
        
        val = dist.index(min(dist))
        out.append(val)
    
    return out