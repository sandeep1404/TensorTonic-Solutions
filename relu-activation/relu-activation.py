import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    # Write code here
    
    x = np.array(x)
    ans = np.where(x>0,x,0)
    
    # Ensure at least 1D array for scalars
    if ans.ndim == 0:
        ans = ans.reshape(1)
    
    return ans