def fasta_reader(file):
    seq_dict = {}
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith('>'):
                line = line.rstrip('\n')
                key = line
                seq_dict[key] = []
            else:
                line = line.rstrip('\n')
                seq_dict[key].append(line)
    for key,value in seq_dict.items():
        value = ''.join(value)
        seq_dict[key] = value
    seq = []
    for values in seq_dict.values():
        seq.append(values)
    return seq

def prefix_function(pattern):
    p = list(pattern)
    m = len(pattern)
    a = [0] * m
    k = 0
    for q in range(2,m+1):
        while k > 0 and p[k] != p[q-1]:
            k = a[k-1]
        if p[k] == p[q-1]:
           k += 1
        a[q-1] = k
    return a

seq = fasta_reader('speed_motif_finding.txt')     
print(*prefix_function(seq[0]))
