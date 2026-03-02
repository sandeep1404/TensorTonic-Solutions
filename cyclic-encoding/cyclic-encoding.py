def cyclic_encoding(values, period):
    """
    Encode cyclic features as sin/cos pairs.
    """
    # Write code here

    import numpy as np
    import math
    out = []
    for val in values:
        theta = (2*math.pi*val)/period
        encoded = [np.sin(theta), np.cos(theta)]
        out.append(encoded)
    return out