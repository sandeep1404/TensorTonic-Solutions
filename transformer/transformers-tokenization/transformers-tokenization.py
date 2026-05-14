import numpy as np
from typing import List, Dict

class SimpleTokenizer:
    """
    A word-level tokenizer with special tokens.
    """
    
    def __init__(self):
        self.word_to_id: Dict[str, int] = {}
        self.id_to_word: Dict[int, str] = {}
        self.vocab_size = 0
        
        # Special tokens
        self.pad_token = "<PAD>"
        self.unk_token = "<UNK>"
        self.bos_token = "<BOS>"
        self.eos_token = "<EOS>"
    
    def build_vocab(self, texts: List[str]) -> None:
        """
        Build vocabulary from a list of texts.
        Add special tokens first, then unique words.
        """
        # YOUR CODE HERE

        vocab = []
        for ele in texts:
            words = (ele.split())
            for word in words:
                vocab.append(word)

        special_tokens =  [self.pad_token,self.unk_token,self.bos_token,self.eos_token]

        vocabulary = special_tokens + sorted(list(set((vocab))))
        self.vocab_size = len(vocabulary)


        vocab = np.array(vocabulary)
        # print(vocab)

        # ele_text = text.split(' ')
        # ele_text = sorted(ele_text)
        i=0
        for ele in vocabulary:
            self.word_to_id[ele] = i
            self.id_to_word[i]=ele
            i+=1
        return vocabulary
        
    
    def encode(self, text: str) -> List[int]:
        """
        Convert text to list of token IDs.
        Use UNK for unknown words.
        """
        # YOUR CODE HERE
        texts =  ["hello world", "this is a test", "hello test"]
        vocab = self.build_vocab(texts=texts)
        self.vocab_size = len(vocab)
        vocab = np.array(vocab)
        # print(vocab)

        if text=='':
            return []
        
        ele_text = text.split(' ')
        ele_text = sorted(ele_text)
        i=0
        for ele in vocab:

            self.word_to_id[ele] = i
            self.id_to_word[i]=ele
            i+=1

        tokens = []


        
        for ele in ele_text:
            ele = ele.lower()
            if ele in vocab:
                index = self.word_to_id[ele]
                index = int(index)
                # print(index)
                tokens.append(index)
                # self.word_to_id[ele] = index
                # self.id_to_word[index]=ele
            else:
                index = np.where(vocab=='<UNK>')[0][0]
                index = int(index)
                tokens.append(index)
                # self.word_to_id['<UNK>'] = index
                # self.id_to_word[index]='<UNK>'

        return tokens


    
    def decode(self, ids: List[int]) -> str:
        """
        Convert list of token IDs back to text.
        """
        # YOUR CODE HERE
        words =''
        # print(self.id_to_word)
        i=0
        for id in ids:
            if i< len(ids)-1:
                if id in self.id_to_word.keys():
                    words+= self.id_to_word[id] + ' '
                else:
                    words+="<UNK>" + ' '
            else:
                if id in self.id_to_word.keys():
                    words+= self.id_to_word[id] 
                else:
                    words+="<UNK>"
                    # words += ' '
            i+=1
        return words

