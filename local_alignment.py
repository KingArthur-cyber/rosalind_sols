from Bio import Align
file_name = "sequence.fasta"
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
#print(value)

aligner = Align.PairwiseAligner()
target = value[0]
query = value[1]
score = aligner.score(target,query)
print(score)
alignments = aligner.align(target,query)
print(alignments[0])