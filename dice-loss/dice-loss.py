import numpy as np

def dice_loss(p, y, eps=1e-8):
    """
    Compute Dice Loss for segmentation.
    """
    # Write code here
    
    p = np.array(p)
    y = np.array(y)

    dice_nom = 2*np.sum(np.multiply(p,y))+eps
    dice_denom = np.sum(p) + np.sum(y) +eps

    dice_coff = dice_nom/dice_denom

    dice_loss = 1- dice_coff

    return dice_loss