import numpy as np

def info_nce_loss(Z1, Z2, temperature=0.1):
    """
    Compute InfoNCE Loss for contrastive learning.
    """
    # Write code here
    Z1 = np.array(Z1)
    Z2 = np.array(Z2)

    N = Z1.shape[0]
    scaled_matrix = np.dot(Z1,np.transpose(Z2))/temperature
    s_stable = scaled_matrix - np.max(scaled_matrix)
    pos_pairs = np.diag(s_stable)
    nom = np.exp(pos_pairs)
    denom = np.sum(np.exp(s_stable),axis=1)

    loss = -(1/N)*np.sum(np.log(nom/denom))

    return loss 