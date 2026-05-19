import numpy as np

def batch_norm_forward(x, gamma, beta, eps=1e-5):
    """
    Forward-only BatchNorm for (N,D) or (N,C,H,W).
    """
    # Write code here

    x= np.array(x)

    if x.ndim ==4:
        output  = np.zeros(x.shape)
        mu = np.mean(x,axis=(0,2,3),keepdims=True)
    
        variance = np.var(x,axis=(0,2,3),keepdims=True)
        
        xcap= (x-mu)/np.sqrt(variance+eps)
        
        channels = x.shape[1]
        
        for i in range(channels):
            output[:,i,:] = xcap[:,i,:]*gamma[i]+beta[i]

        return output
            
    else:
        mu = np.mean(x,axis=0,keepdims=True)
        variance = np.var(x,axis=0,keepdims=True)
    
        xcap= (x-mu)/np.sqrt(variance+eps)
    
        out = gamma*xcap+beta
    
        return out


        

    
    