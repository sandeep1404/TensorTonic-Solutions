import numpy as np
import math

def layer_norm(x: np.ndarray, gamma: np.ndarray, beta: np.ndarray, eps: float = 1e-6) -> np.ndarray:
    """
    Returns: Normalized array of same shape as x
    """
    # Your code here

    x= np.array(x)
    gamma = np.array(gamma)
    beta = np.array(beta)
    # beta = beta.reshape(1,beta.shape[0])
    # print(beta.shape)
    mu = np.mean(x,axis=-1)
    mu= mu.reshape(-1,1)
    variance = np.var(x,axis=-1)
    variance= variance.reshape(-1,1)
    norm = (x - mu)/np.sqrt(variance+eps)

    layernorm = gamma*norm+beta #(np.dot(gamma,norm),beta)

    return layernorm 
    