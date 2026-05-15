import torch
import torch.nn.functional as F
import math

def scaled_dot_product_attention(Q: torch.Tensor, K: torch.Tensor, V: torch.Tensor) -> torch.Tensor:
    """
    Compute scaled dot-product attention.
    """
    Q = torch.tensor(Q).float()
    K = torch.tensor(K).float()
    V = torch.tensor(V).float()

    nom = torch.matmul(Q, torch.transpose(K, 1, 2)) / math.sqrt(K.shape[-1])

    nom_cal = F.softmax(nom, dim=-1)
    # qk = torch.reshape(nom_cal, (1, 2, 2))

    # print(qk)

    attention = torch.matmul(nom_cal, V)

    return attention
