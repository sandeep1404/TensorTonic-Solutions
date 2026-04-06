import numpy as np
import numpy as np
def hinge_loss(y_true, y_score, margin=1.0, reduction="mean") -> float:
    """
    y_true: 1D array of {-1,+1}
    y_score: 1D array of real scores, same shape as y_true
    reduction: "mean" or "sum"
    Return: float
    """
    # Write code here

    y_true = np.array(y_true)
    y_score = np.array(y_score)


    yhat = margin - y_true*y_score

    loss = np.where(yhat<=0,0, yhat)

    if reduction=='mean':
        out = np.mean(loss)
    else:
        out = np.sum(loss)


    return out
    
    

    