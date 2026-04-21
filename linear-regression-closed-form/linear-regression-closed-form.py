def linear_regression_closed_form(X, y):
    """
    Compute the optimal weight vector using the normal equation.
    """
    # Write code here
    X= np.array(X)
    y = np.array(y)

    X_t = np.transpose(X)

    inv_val = np.linalg.inv(np.matmul(X_t,X))
    other_val = np.matmul(X_t,y)

    # w = inv_val*other_val
    w = np.matmul(inv_val,other_val)

    return list(w)