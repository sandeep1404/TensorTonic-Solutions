import numpy as np

def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    # Write code here
    rater1 = np.array(rater1)
    rater2 = np.array(rater2)

    out = np.equal(rater1,rater2)
    agree = np.count_nonzero(out)
    po = agree/len(rater1)

    if po ==1:
        return 1
    ele = np.unique(rater1) 
    pe_out = []
    for i in ele:
        pe_1 = np.count_nonzero(np.equal(rater1,i))/len(rater1)
        pe_2 = np.count_nonzero(np.equal(rater2,i))/len(rater1)
    
        pe_res = pe_1* pe_2
        pe_out.append(pe_res)
    
    pe= np.sum(pe_out)
    result = (po -pe)/(1-pe)

    return result
    