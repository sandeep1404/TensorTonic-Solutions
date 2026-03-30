import math
def generate_anchors(feature_size, image_size, scales, aspect_ratios):
    """
    Generate anchor boxes for object detection.
    """
    # Write code here

    stride = image_size/feature_size
    

    num_anchor_boxes = len(scales)*len(aspect_ratios)*feature_size*feature_size


    anchors =[]
    for i in range(feature_size):
        for j in range(feature_size):
            cx = (j+0.5)*stride
            cy=(i+0.5)*stride
            for a in range(len(scales)):
                for b in range(len(aspect_ratios)):
                    w = scales[a]*math.sqrt(aspect_ratios[b])
                    h = scales[a]/(math.sqrt(aspect_ratios[b]))
                    anchor_box =[cx - w/2, cy - h/2, cx + w/2, cy + h/2]
                    anchors.append(anchor_box)

    return anchors
                
                