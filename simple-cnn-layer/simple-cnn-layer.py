import numpy as np

def conv2d(x, W, b):
    """
    Simple 2D convolution layer forward pass.
    Valid padding, stride=1.
    """
    # Write code here
    x= np.array(x)
    W = np.array(W)
    kh = W.shape[2]
    kw = W.shape[3]
    h = x.shape[2]
    w = x.shape[3]
    stride =1 
    N= x.shape[0]
    cout = W.shape[0]
    hout = h-kh+1
    wout = w-kw+1
    cin = x.shape[1]
    out = np.zeros((N,cout,hout,wout))
    for i in range(N):  ## samples or batches
        for j in range(cout): ## channels 
            for p in range(hout):
                for q in range(wout):
                    patch = x[i, :,p:p+kh,q:q+kw]
                    out[i,j,p,q]= np.sum(patch*W[j])
                    out[i,j,p,q] += b[j]


    return out
                    
                    # inp = x[i][j][p:p+kh,q:q+kw]
                    # res = np.sum(np.multiply(inp,W))+b[0]
                    # out[i][j][p][q] = res
   

    