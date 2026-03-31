import numpy as np
def binary_focal_loss(predictions, targets, alpha, gamma):
    """
    Compute the mean binary focal loss.
    """
    # Write code here

    predictions = np.array(predictions)
    targets = np.array(targets)

    predictions = np.where(predictions!=0,predictions,np.clip(predictions,1e-15,1-1e-15))
    prob = np.where(targets!=0,predictions,1-predictions)

    loss = -1*alpha*((1-prob)**gamma)*(np.log(prob))

    out = np.mean(loss)

    return out