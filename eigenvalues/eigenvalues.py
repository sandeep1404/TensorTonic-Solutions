import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    # Write code here
    try:
        inp = np.array(matrix)
        m,n = inp.shape
    
        if m!=n:
            return None
        else:
            out = np.linalg.eigvals(inp) #.tolist()
            return out
    except:
        return None
        
        
    
    