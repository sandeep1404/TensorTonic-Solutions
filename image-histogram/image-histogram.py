import numpy as np
def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    # Write code here
    image = np.array(image)
    x={}
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            val = image[i][j]
            if val in x.keys():
                x[val]+=1
            else:
                x[val]=1
    
    y = np.zeros((1,256))
    y = y[0].tolist()

    for ele in x.keys():
        y[ele]=x[ele]

    return y