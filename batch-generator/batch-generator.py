import numpy as np

def batch_generator(X, y, batch_size, rng=None, drop_last=False):
    """
    Randomly shuffle a dataset and yield mini-batches (X_batch, y_batch).
    """
    # Write code here

    X= np.array(X)
    y = np.array(y)

    arr_len = len(X)

    num_batches = arr_len//batch_size

    residual = arr_len - num_batches*batch_size

  
    
    indices = np.arange(len(X))

   

    ## shuffle indices

    if rng is None:
          np.random.shuffle(indices)
  
    else:
          rng.shuffle(indices)
  
#     print(indices)
    X = X[indices]
    y = y[indices]

    if drop_last:
        X= X[:arr_len-residual]
        y =y[:arr_len-residual]
#     print(f"x:{X},y:{y}")
    for i in range(0, len(X),batch_size):
          batch_x = X[i:i+batch_size]
          batch_y = y[i:i+batch_size]

          yield batch_x,batch_y
