import itertools
import numpy as np

def fasta_reader(file_name):
    with open(file_name) as f:
        new_dict = {}
        
        for line in f:
            line = line.rstrip('\n')
            if line.startswith('>'):
                
                key = line.lstrip('>')
                new_dict[key] = []
            else:
                
                new_dict[key].append(line)
    for key,value in new_dict.items():
        value = ''.join(value)
        new_dict[key] = value
    value = []
    for values in new_dict.values():
        value.append(values)
    return value[0]

def matrix(a, b, match_score=3, gap_cost=2):
    H = np.zeros((len(a) + 1, len(b) + 1), np.int)

    for i, j in itertools.product(range(1, H.shape[0]), range(1, H.shape[1])):
        match = H[i - 1, j - 1] + (match_score if a[i - 1] == b[j - 1] else - match_score)
        delete = H[i - 1, j] - gap_cost
        insert = H[i, j - 1] - gap_cost
        H[i, j] = max(match, delete, insert, 0)
    return H
def traceback(H, b, b_='', old_i=0):
    # flip H to get index of **last** occurrence of H.max() with np.argmax()
    H_flip = np.flip(np.flip(H, 0), 1)
    i_, j_ = np.unravel_index(H_flip.argmax(), H_flip.shape)
    i, j = np.subtract(H.shape, (i_ + 1, j_ + 1))  # (i, j) are **last** indexes of H.max()
    if H[i, j] == 0:
        return b_, j
    b_ = b[j - 1] + '-' + b_ if old_i - i > 1 else b[j - 1] + b_
    return traceback(H[0:i, 0:j], b, b_, i)

def smith_waterman(a, b, match_score=3, gap_cost=2):
    a, b = a.upper(), b.upper()
    H = matrix(a, b, match_score, gap_cost)
    b_, pos = traceback(H, b)
    return pos, pos + len(b_)

a,b = fasta_reader('sequence.fasta'),fasta_reader('mupirocin.fasta')
H = matrix(a,b)
print(traceback(H,b))
