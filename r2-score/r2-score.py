import numpy as np

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
    """
    # Write code here
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    if np.equal(y_true,y_pred).all():
        return 1.0
    else:
        true_mean = np.mean(y_true)
    
        denom = np.sum(np.square(y_true- true_mean))

        if denom==0:
            return 0.0
    
        nom =  np.sum(np.square(y_true - y_pred))
    
        r2 = 1 - (nom/denom)
    
        return r2