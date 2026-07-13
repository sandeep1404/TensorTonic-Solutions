import numpy as np 

def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    # Write code here

    N = len(actual_tokens)
    p_dist = np.array(prob_distributions)

    final_prob = []
    k=0
    for i in actual_tokens:
        final_prob.append(prob_distributions[k][i])
        k=k+1
    out = np.exp(-1*np.mean(np.log(final_prob)))

    return out 

    
    
    
    
    
    
    

    
    

    
    