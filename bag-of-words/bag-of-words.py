# import numpy as np

# def bag_of_words_vector(tokens, vocab):
#     """
#     Returns: np.ndarray of shape (len(vocab),), dtype=int
#     """
#     # Your code here
#     # tokens = np.array(tokens)
#     # vocab = np.array(vocab)

#     ## 

#     # out = {}
   
    
#     # for ele in tokens:
#     #     if ele in vocab:
#     #         if ele in  out.keys():
#     #             out[ele]+=1
#     #         else:
#     #             out[ele]=1
#     #     else:
#     #         out[ele] =0
    
#     # return np.array(list(out.values()))


#     out = {}
#     if len(tokens)==0:
#         return np.zeros(len(vocab),dtype=np.int8)
#     values,counts = np.unique_counts(tokens)
#     mapping = dict(zip(values, counts))
#     for ele in (vocab):
#         if ele in tokens:
#             out[ele] = mapping[ele]
#         else:
#             out[ele] =0
    
#     return np.array(list(out.values()))

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int64
    """
    if len(tokens) == 0:
        return np.zeros(len(vocab), dtype=np.int64)

    values, counts = np.unique_counts(tokens)
    mapping = dict(zip(values, counts))

    return np.asarray([mapping.get(word, 0) for word in vocab], dtype=np.int64)