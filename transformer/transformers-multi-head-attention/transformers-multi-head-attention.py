import numpy as np
import math 

def softmax(x, axis=-1):
    e_x = np.exp(x - np.max(x, axis=axis, keepdims=True))
    return e_x / np.sum(e_x, axis=axis, keepdims=True)

def multi_head_attention(Q: np.ndarray, K: np.ndarray, V: np.ndarray,
                         W_q: np.ndarray, W_k: np.ndarray, W_v: np.ndarray,
                         W_o: np.ndarray, num_heads: int) -> np.ndarray:
    """
    Compute multi-head attention.
    """
    
    # Your code here

    Q = np.array(Q)
    K = np.array(K)
    V = np.array(V)

    W_q = np.array(W_q)
    W_k = np.array(W_k)
    W_v = np.array(W_v)

    W_o = np.array(W_o)


    query = np.matmul(Q, W_q)
    key = np.matmul(K, W_k)
    value = np.matmul(V, W_v)

    head_dim = query.shape[-1] // num_heads
    query = query.reshape(query.shape[0], query.shape[1], num_heads, head_dim).transpose(0, 2, 1, 3)
    key = key.reshape(key.shape[0], key.shape[1], num_heads, head_dim).transpose(0, 2, 1, 3)
    value = value.reshape(value.shape[0], value.shape[1], num_heads, head_dim).transpose(0, 2, 1, 3)

    scores = np.matmul(query, key.transpose(0, 1, 3, 2)) / math.sqrt(head_dim)
    attention_weights = softmax(scores, axis=-1)
    attention_output = np.matmul(attention_weights, value).transpose(0, 2, 1, 3).reshape(Q.shape[0], Q.shape[1], -1)
    output = np.matmul(attention_output, W_o)
    return output


    

    