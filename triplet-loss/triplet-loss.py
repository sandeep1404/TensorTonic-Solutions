# import numpy as np

# def triplet_loss(anchor, positive, negative, margin=1.0):
#     """
#     Compute Triplet Loss for embedding ranking.
#     """
#     # Write code here
#     anchor = np.array(anchor)
#     positive = np.array(positive)
#     negative = np.array(negative)
#     if len(anchor.shape)==0:
#         return 0
                        
#     if len(anchor.shape)==1:
#         anchor = anchor.reshape(1, anchor.shape[0])
#         positive = positive.reshape(1, positive.shape[0])
#         negative = negative.reshape(1, negative.shape[0])



#     dist_ap = np.sum(np.square(np.subtract(positive,anchor)))
#     # dist_ap= int(dist_ap)
#     # print(dist_ap)
#     dist_an = np.sum(np.square(np.subtract(negative,anchor)))
#     # dist_an = int(dist_an)
#     # print(dist_an)
#     loss = np.maximum(0,dist_ap-dist_an+margin)
#     loss = float(loss)

#     return loss

import numpy as np

def triplet_loss(anchor, positive, negative, margin=1.0):
    """
    Compute mean Triplet Loss over a batch of embeddings.
    Supports both single embeddings (1-D) and batches (2-D).
    """
    anchor   = np.array(anchor,   dtype=float)
    positive = np.array(positive, dtype=float)
    negative = np.array(negative, dtype=float)

    if anchor.ndim == 0:
        return 0.0

    if anchor.ndim == 1:
        anchor   = anchor.reshape(1, -1)
        positive = positive.reshape(1, -1)
        negative = negative.reshape(1, -1)

    # Per-sample squared Euclidean distances  (axis=1 keeps one value per row)
    dist_ap = np.sum(np.square(positive - anchor), axis=1)
    print(dist_ap)
    dist_an = np.sum(np.square(negative - anchor), axis=1)
    print(dist_an)

    # Per-sample hinge loss, averaged over the batch
    per_sample_loss = np.maximum(0.0, dist_ap - dist_an + margin)
    return float(np.mean(per_sample_loss))