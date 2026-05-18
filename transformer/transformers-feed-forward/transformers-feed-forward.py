import numpy as np

def feed_forward(x: np.ndarray, W1: np.ndarray, b1: np.ndarray,
                 W2: np.ndarray, b2: np.ndarray) -> np.ndarray:
    """
    Apply position-wise feed-forward network.
    """
    # Your code here

    x  = np.array(x)
    W1 = np.array(W1)
    b1 = np.array(b1)
    W2 = np.array(W2)
    b2 = np.array(b2)

    subout1 = np.add(np.dot(x,W1),b1)
    out1 = np.maximum(0, subout1)

    out2 = np.add(np.dot(out1,W2),b2)

    return out2 