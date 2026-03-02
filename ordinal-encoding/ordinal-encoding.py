def ordinal_encoding(values, ordering):
    """
    Encode categorical values using the provided ordering.
    """
    # Write code here

    out = []

    for ele in values:
        print
        ind=ordering.index(ele)
        out.append(ind)

    return out