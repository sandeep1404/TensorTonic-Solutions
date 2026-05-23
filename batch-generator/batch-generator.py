import numpy as np

def batch_generator(X, y, batch_size, rng=None, drop_last=False):
    """
    Randomly shuffle a dataset and yield mini-batches (X_batch, y_batch).
    """
    X = np.array(X)
    y = np.array(y)

    n = len(X)
    assert n == len(y)

    # 1. make indices for all samples
    indices = np.arange(n)

    # 2. shuffle indices
    if rng is not None:
        rng.shuffle(indices)
    else:
        np.random.shuffle(indices)

    # 3. apply permutation
    X = X[indices]
    y = y[indices]

    # 4. if drop_last, cut off only after shuffling
    if drop_last:
        n_full = (n // batch_size) * batch_size
        X = X[:n_full]
        y = y[:n_full]
        n = n_full

    # 5. iterate over batches
    for start in range(0, n, batch_size):
        end = start + batch_size
        batch_x = X[start:end]
        batch_y = y[start:end]
        yield batch_x, batch_y