import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here

    x = np.array(x)
    if sum(p)!=1:
        raise ValueError
    p = np.array(p)
    mul_ = x*p

    res = sum(list(mul_))

    return res
