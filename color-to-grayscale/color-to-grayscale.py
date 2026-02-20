import numpy as np
def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    # Write code here

    image = np.array(image)
    final_out = []
    for i in range(image.shape[0]):
        output = []
        for j in range(image.shape[1]):
            y = 0.299*image[i][j][0]+0.587*image[i][j][1]+0.114*image[i][j][2]
            
            output.append(y)
        final_out.append(output)
    return final_out