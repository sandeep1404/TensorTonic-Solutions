def rank_transform(values):
    """
    Transform values to their ranks using average ranking for ties.
    
    Parameters:
    values: list of numbers
    
    Returns:
    list of ranks (floats)
    
    Examples:
    >>> rank_transform([10, 30, 20])
    [1.0, 3.0, 2.0]
    >>> rank_transform([1, 2, 2, 3])
    [1.0, 2.5, 2.5, 4.0]
    """
    # Create list of (value, original_index) pairs
    indexed_values = [(val, idx) for idx, val in enumerate(values)]
    
    # Sort by value
    sorted_pairs = sorted(indexed_values, key=lambda x: x[0])
    
    # Assign ranks
    ranks = [0.0] * len(values)
    i = 0
    
    while i < len(sorted_pairs):
        # Find all values equal to current value
        current_value = sorted_pairs[i][0]
        j = i
        while j < len(sorted_pairs) and sorted_pairs[j][0] == current_value:
            j += 1
        
        # Calculate average rank for this group
        # Ranks are 1-indexed: positions i to j-1 have ranks (i+1) to j
        avg_rank = sum(range(i + 1, j + 1)) / (j - i)
        
        # Assign average rank to all indices in this group
        for k in range(i, j):
            original_idx = sorted_pairs[k][1]
            ranks[original_idx] = avg_rank
        
        i = j
    
    return ranks