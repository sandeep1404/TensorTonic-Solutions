def he_initialization(W, fan_in):
    """
    Scale raw weights to He uniform initialization.
    """
    # Write code here

    w = np.array(W)

    L = np.sqrt(6/fan_in)

    w_ = ( w*2*L)-L
    w_ = w_.tolist()
    # W_ = np.where(0<=w<=1,( w*2*L)-L, w).tolist()

    return w_




