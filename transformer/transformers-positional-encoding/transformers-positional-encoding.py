import numpy as np

def positional_encoding(seq_length: int, d_model: int) -> np.ndarray:
    """
    Generate sinusoidal positional encodings.
    """
    out = np.zeros((seq_length, d_model))

    for i in range(seq_length):
        for j in range(d_model):
            index = j // 2  # pair index: (0,1)->0, (2,3)->1, ...
            theta_val = 1 / (10000 ** ((2 * index) / d_model))
            if j % 2 == 0:
                out[i, j] = np.sin(i * theta_val)
            else:
                out[i, j] = np.cos(i * theta_val)
    return out
