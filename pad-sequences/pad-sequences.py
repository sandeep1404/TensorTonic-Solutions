import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here

    L = max_len if max_len else max(len(seq) for seq in seqs)
    if L==0:
        return np.empty(shape=(0, 0))
    output = []
    for i in range(len(seqs)):
        len_seq = seqs[i]
        if len_seq==L:
            output.append(seqs[i])
        else:
            diff = L- len(seqs[i])
            # padding: list[Any] = list(np.zeros(diff,dtype=int))

            if diff>0:
                out_seq = seqs[i] + np.full((1, diff),pad_value)[0].tolist()
                output.append(out_seq)
            else:
                output.append(seqs[i][:L])

    return np.array(output)

