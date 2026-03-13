import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def binary_cross_entropy(y_hat, y):
    y_hat = np.clip(y_hat, 0, 1)
    loss = -(np.mean(y*np.log(y_hat)+(1-y)*np.log(1-y_hat)))
    return loss 

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """

    X= np.array(X)
    y = np.array(y)

    ## initilaize w and b 

    n, d = X.shape # n sample d features 

    w = np.zeros(d) ##
    b = 0
    losses = []

    for i in range(steps):
        ## fwd pass 
    
        z =  X@w +b
        y_hat = _sigmoid(z)
    
        ## loss 
    
        loss = binary_cross_entropy(y_hat,y)
        losses.append(loss)

        ## update w and b 
    
        error = y_hat - y 
        dw = X.T@error/n
        db = np.mean(error)

        w = w - lr*dw
        b = b - lr*db

    return (w,b)
        
    
        
        
    

        
        
        

        