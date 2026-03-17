import numpy as np

def streaming_minmax_init(D):
    """
    Initialize state dict with min, max arrays of shape (D,).
    """
    # Write code here

    return {
        "min": np.full(D, np.inf),   # shape (D,), start at +inf
        "max": np.full(D, -np.inf),  # shape (D,), start at -inf
    }


def streaming_minmax_update(state, X_batch, eps=1e-8):
    """
    Update state's min/max with X_batch, return normalized batch.
    """
    # Write code here
    X_batch = np.array(X_batch)
    state["min"] = np.minimum(state["min"], X_batch.min(axis=0))
    state["max"] = np.maximum(state["max"], X_batch.max(axis=0))

    X_norm = (X_batch - state["min"]) / (state["max"] - state["min"] + eps)

    return X_norm


    