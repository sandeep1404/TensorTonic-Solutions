def interaction_features(X):
    """
    Generate pairwise interaction features and append them to the original features.
    """
    # Write code here
    for liste in X:
        # subout = []
        le = len(liste)
        for i in range(le):
            for j in range(i+1,le):
                val=liste[i]*liste[j]
                print(f'the value of {i} and {j} and mul is {val}')
                liste.append(val)
    
    return X