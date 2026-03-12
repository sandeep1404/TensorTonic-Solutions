import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    # Write code here
    out_loss= []
    for i in range(len(y_true)):
        index = y_true[i]
        y_pred_val = y_pred[i][index]
        loss = -(np.log(y_pred_val))
        out_loss.append(loss)
    output = sum(out_loss)/len(out_loss)
    return output
        
        