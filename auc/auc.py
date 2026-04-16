import numpy as np

def auc(fpr, tpr):
    """
    Compute AUC (Area Under ROC Curve) using trapezoidal rule.
    """
    # Write code here
    fpr = np.array(fpr)
    tpr = np.array(tpr)

    out = np.trapezoid(tpr,fpr)

    return out
    