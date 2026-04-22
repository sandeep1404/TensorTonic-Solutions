import numpy as np

def pca_projection(X, k):
    """
    Project data onto the top-k principal components.
    """
    X = np.array(X, dtype=float)
    Xmean = np.mean(X, axis=0)
    Xc = X - Xmean

    covariance_matrix = np.matmul(np.transpose(Xc), Xc)  # use centered Xc, not X
    covariance_matrix = covariance_matrix/(X.shape[0] -1)
    eig_val, eig_vector = np.linalg.eig(covariance_matrix)

    sorted_indices = np.argsort(eig_val)[::-1]
    eig_vector_sorted = eig_vector[:, sorted_indices]

    w = eig_vector_sorted[:, 0:k]

    sub_out = np.matmul(Xc, w)

    out = []
    for i in range(len(sub_out)):
        out.append(sub_out[i].tolist())  # convert numpy array to Python list

    return out
