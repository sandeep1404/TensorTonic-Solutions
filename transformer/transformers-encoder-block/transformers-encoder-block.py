import numpy as np
import math 

def softmax(x, axis=-1):
    """Provided: Softmax function."""
    e_x = np.exp(x - np.max(x, axis=axis, keepdims=True))
    return e_x / np.sum(e_x, axis=axis, keepdims=True)

def layer_norm(x: np.ndarray, gamma: np.ndarray, beta: np.ndarray, eps: float = 1e-6) -> np.ndarray:
    """
    Apply layer normalization.
    """
    # Your code here

    x= np.array(x)
    gamma = np.array(gamma)
    beta = np.array(beta)
    # beta = beta.reshape(1,beta.shape[0])
    # print(beta.shape)
    mu = np.mean(x,axis=-1,keepdims=True)
    # mu= mu.reshape(-1,1)
    variance = np.var(x,axis=-1,keepdims=True)
    # variance= variance.reshape(-1,1)
    norm = (x - mu)/np.sqrt(variance+eps)

    layernorm = gamma*norm+beta #(np.dot(gamma,norm),beta)

    return layernorm 
    

def multi_head_attention(Q: np.ndarray, K: np.ndarray, V: np.ndarray,
                         W_q: np.ndarray, W_k: np.ndarray, W_v: np.ndarray,
                         W_o: np.ndarray, num_heads: int) -> np.ndarray:
    """
    Multi-head attention.
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

    query = query.reshape(query.shape[0], query.shape[1], num_heads, head_dim).transpose(0, 2, 1, 3) ## shape (1,3,4) --> (1,3,2,2) ---> transpose --> (1,2,3,2) (across each head dimenstion split the vector across 2 heads)
    key = key.reshape(key.shape[0], key.shape[1], num_heads, head_dim).transpose(0, 2, 1, 3)  ## 
    value = value.reshape(value.shape[0], value.shape[1], num_heads, head_dim).transpose(0, 2, 1, 3) ##(1,2,3,2)

    scores = np.matmul(query, key.transpose(0, 1, 3, 2)) / math.sqrt(head_dim) ## (1,2,3,2) --> (1,2,2,3)
    attention_weights = softmax(scores, axis=-1) ## (1,2,3,3)
    attention_output = np.matmul(attention_weights, value).transpose(0, 2, 1, 3).reshape(Q.shape[0], Q.shape[1], -1) ## (1,2,3,3) values (1,2,3,2) --->(1,2,3,2) --> (1,3,2,2)-->(1,3,4)
    output = np.matmul(attention_output, W_o) ##(1,3,4) --> (4,4) -->(1,3,4)

    return output
    

def feed_forward(x: np.ndarray, W1: np.ndarray, b1: np.ndarray,
                 W2: np.ndarray, b2: np.ndarray) -> np.ndarray:
    """
    Position-wise feed-forward network.
    """
    # Your code here
    x  = np.array(x)
    W1 = np.array(W1)
    b1 = np.array(b1)
    W2 = np.array(W2)
    b2 = np.array(b2)

    subout1 = np.add(np.dot(x,W1),b1)
    out1 = np.maximum(0, subout1)

    out2 = np.add(np.dot(out1,W2),b2)

    return out2 

def encoder_block(x: np.ndarray, W_q: np.ndarray, W_k: np.ndarray, W_v: np.ndarray,
                  W_o: np.ndarray, W1: np.ndarray, b1: np.ndarray, W2: np.ndarray,
                  b2: np.ndarray, gamma1: np.ndarray, beta1: np.ndarray,
                  gamma2: np.ndarray, beta2: np.ndarray, num_heads: int) -> np.ndarray:
    """
    Complete encoder block: MHA + FFN with residuals and layer norms.
    """
    # Your code here

    mha = multi_head_attention(x, x, x, W_q, W_k, W_v, W_o,num_heads)

    layernorm1 = layer_norm(mha+x,gamma1,beta1,eps=1e-6)

    output = layer_norm(layernorm1+feed_forward(layernorm1,W1,b1,W2,b2),gamma2,beta2,eps=1e-6)

    return output
    

    
    
    
    

    