import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    # Write code here
    A = np.array(A)
    m,n = A.shape
    det_A = np.linalg.det(A)
    if m!=n or det_A==0:
        return None
    else:
        inverse = np.linalg.inv(A)
        return inverse