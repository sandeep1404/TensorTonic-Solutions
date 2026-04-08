import numpy as np

def pearson_correlation(X):
    """
    Calculates the Pearson correlation matrix for a 2D array.
    
    Parameters:
    X (np.ndarray): Input data of shape (N, D) where N is the number of samples 
                    and D is the number of features.
                    
    Returns:
    np.ndarray: Correlation matrix of shape (D, D), or None if input is invalid.
    """
    # 1. Validate input constraints (must be 2D and N >= 2)
    if not isinstance(X, np.ndarray):
        X = np.array(X)
        
    if X.ndim != 2:
        return None
        
    N, D = X.shape
    if N < 2:
        return None
        
    # Cast to float64 to ensure numerical precision (relative tolerance <= 1e-8)
    X = np.asarray(X, dtype=np.float64)
    
    # 2. Vectorized Centering
    # Subtract the mean of each column (feature) from the data
    # Shape of X_centered: (N, D)
    X_centered = X - np.mean(X, axis=0)
    
    # 3. Calculate numerator: Covariance-like matrix (without dividing by N-1)
    # Using matrix multiplication (dot product) to avoid loops
    # Shape of num: (D, D)
    num = X_centered.T @ X_centered
    
    # 4. Calculate denominator: Product of standard deviations
    # Sum of squared deviations for each feature. Shape: (D,)
    ss = np.sum(X_centered**2, axis=0)
    std = np.sqrt(ss)
    
    # Outer product gives the combination of std_i * std_j for all pairs
    # Shape of denom: (D, D)
    denom = np.outer(std, std)
    
    # 5. Handle zero-variance features and calculate correlation
    # Initialize the correlation matrix with NaNs
    R = np.full((D, D), np.nan, dtype=np.float64)
    
    # Create a mask where the denominator is not zero
    mask = denom != 0
    
    # Perform division only on valid pairs (avoids RuntimeWarning: divide by zero)
    R[mask] = num[mask] / denom[mask]
    
    # 6. Clip values to [-1.0, 1.0] to handle minor floating point inaccuracies
    # Note: np.clip preserves the NaNs for zero-variance features
    R = np.clip(R, -1.0, 1.0)
    
    return R
