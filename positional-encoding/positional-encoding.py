import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here
    output = []
    for i in range(seq_len):
        subout=[]
        for j in range(d_model):
            if j%2==0:
                pe= np.sin(i/base**(2*(j//2)/d_model))
                # pe = np.round(pe,4)
                subout.append(pe)
            else:
                pe= np.cos(i/base**(2*(j//2)/d_model))
                # pe = np.round(pe,4)
                subout.append(pe)
        output.append(subout)
    return np.array(output)
                