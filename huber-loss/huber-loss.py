import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    # Write code here
    
    if len(y_true)!=len(y_pred):
        return None
    
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    error = y_true - y_pred

    error_sq= np.where(abs(error)<delta, 0.5*error*error , delta*(abs(error)-0.5*delta))

    ans = sum(error_sq).item()/len(y_pred)

    return ans





