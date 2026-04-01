import numpy as np
def label_smoothing_loss(predictions, target, epsilon):
    """
    Compute cross-entropy loss with label smoothing.
    """
    # Write code here

    predictions = np.array(predictions)
    k = len(predictions)
    targets = np.zeros(k)

    targets[target]=1

    smoothed_traget = np.where(targets!=1, epsilon/k, ((1-epsilon)+epsilon/k))

    loss = -smoothed_traget*np.log(predictions)
    final_loss = np.sum(loss)

    return final_loss