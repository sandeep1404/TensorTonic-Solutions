import numpy as np

def apply_causal_mask(scores, mask_value=-1e9):# -> Any:
    """
    scores: np.ndarray with shape (..., T, T)
    mask_value: float used to mask future positions (e.g., -1e9)
    Return: masked scores (same shape, dtype=float)
    """
    # Write code here
    scores = np.array(scores)
    

    
    rows, cols = np.triu_indices(scores.shape[-1],k=1)

    if scores.ndim ==3:
        scores[:,rows,cols] = mask_value
    elif scores.ndim==2:
        scores[rows,cols] = mask_value
    else:
        scores[:,:,rows,cols] = mask_value
    return scores

    