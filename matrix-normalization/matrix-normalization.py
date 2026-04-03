import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    """
    Normalize a 2D matrix along specified axis using specified norm.
    Returns None for any invalid input (1D, 0D, 3D+, ragged, bad axis, invalid norm_type, etc.)
    Supported norm_types: 'l1', 'l2', 'linf', 'max'
    """
    try:
        matrix = np.array(matrix, dtype=float)
    except (ValueError, TypeError):
        return None

    # Must be strictly 2D
    if matrix.ndim != 2:
        return None

    # Validate axis — only 0, 1, or None are meaningful for 2D
    if axis is not None and axis not in (0, 1):
        return None

    # Validate norm_type — reject anything not explicitly supported
    valid_norm_types = ('l1', 'l2', 'max')
    if norm_type not in valid_norm_types:
        return None

    try:
        if norm_type == 'l1':
            norm = np.sum(np.abs(matrix), axis=axis, keepdims=True)
            out = np.where(norm != 0, matrix / norm, 0)

        elif norm_type == 'l2':
            norm = np.sqrt(np.sum(np.square(matrix), axis=axis, keepdims=True))
            out = np.where(norm != 0, matrix / norm, 0)

        else:  # 'linf' or 'max' — max norm
            norm = np.max(np.abs(matrix), axis=axis, keepdims=True)
            out = np.where(norm != 0, matrix / norm, 0)

    except Exception:
        return None

    return out
