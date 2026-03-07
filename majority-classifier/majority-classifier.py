import numpy as np

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    # Write code here
    labels,counts = np.unique(y_train,return_counts=True)
    major_label= labels[counts.tolist().index(counts.max())].tolist()
    out = [major_label for i in range(len(X_test))]

    return out

    
