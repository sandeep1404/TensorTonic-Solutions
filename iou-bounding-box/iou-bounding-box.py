def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    """
    # Write code here
    boxa_area = (box_a[2]-box_a[0])*(box_a[3]-box_a[1])
    boxb_area = (box_b[2]-box_b[0])*(box_b[3]-box_b[1])
    intersect_cord = []
    if ((box_a[0]<=box_b[0]<=box_a[2]) & (box_a[1]<=box_b[1]<=box_a[3]) & (box_a[0]<=box_b[2]<=box_a[2]) &(box_a[1]<=box_b[3]<=box_a[3])):
        intersect_cord.append(box_b[0])
        intersect_cord.append(box_b[1])
        intersect_cord.append(box_b[2])
        intersect_cord.append(box_b[3])
            
    elif ((box_a[0]<=box_b[0]<=box_a[2]) & (box_a[1]<=box_b[1]<=box_a[3])):
        intersect_cord.append(box_b[0])
        intersect_cord.append(box_b[1])
        intersect_cord.append(box_a[2])
        intersect_cord.append(box_a[3])
    elif ((box_a[0]>box_b[0]>box_a[2]) & (box_a[1]>box_b[1]>box_a[3])):
        intersect_cord.append(box_a[0])
        intersect_cord.append(box_a[1])
        intersect_cord.append(box_b[2])
        intersect_cord.append(box_b[3])

    else:
        return 0
        

    intersection_area = (intersect_cord[2]-intersect_cord[0])*(intersect_cord[3]-intersect_cord[1])

    union= boxa_area+ boxb_area - intersection_area

    iou = intersection_area/union

    return iou