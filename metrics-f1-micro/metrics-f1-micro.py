import numpy as np 

def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here

    y_pred = np.array(y_pred)
    y_true = np.array(y_true)

    if len(y_pred) != len(y_true):
        return None 


    tp= np.count_nonzero(np.equal(y_true,y_pred))

    neg = len(y_pred) - tp 


    f1micro = (2*tp)/(2*tp + 2*neg)

    return f1micro
    


    
    