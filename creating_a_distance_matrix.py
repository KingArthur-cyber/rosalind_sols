import numpy as np

def fasta_reader(file):
    new_dict = {}
    with open(file) as f:
        for line in f.readlines():
            if line.startswith('>'):
                key = line.rstrip('\n')
                new_dict[key] = []
            else:
                line = line.rstrip('\n')
                new_dict[key].append(line)
    for key,value in new_dict.items():
        value = ''.join(value)
        new_dict[key] = value
    return new_dict

file = 'creating_a_distance_matrix.txt'

def hamming(seq1, seq2):
    res = 0.0
    n = len(seq1)
    for i in range(0, len(seq1)):
        if seq1[i] != seq2[i]:
            res += 1.0

    return res/n

file = 'creating_a_distance_matrix.txt'
seqs = []
for key, value in fasta_reader(file).items():
    
    seqs.append(value)
    


rows = len(seqs)
cols = len(seqs)
size = rows * cols
np.set_printoptions(precision=5, floatmode='fixed')  # Set the precision to 5 decimal places

matrix = np.array([0.00000] * size).reshape(rows, cols)


for i in range(len(seqs)):
    for j in range(len(seqs)):
        score = hamming(seqs[i], seqs[j])
        matrix[j][i] = score
print(matrix)
