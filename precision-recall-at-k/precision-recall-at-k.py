def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here

    # recommended = np.array(recommended)
    # relevant = np.array(relevant)

    recall_denom = len(relevant)
    out = []
    recommended = recommended[:k]
    recommended = set(recommended)
    relevant = set(relevant)

    nom = len(recommended.intersection(relevant))

    precision= nom/k
    recall = nom/recall_denom

    out.append(precision)
    out.append(recall)

    return out

    
    
    


    