sub_seq = 'GTA'
seq = 'ACGTACGTGACG'
int_dict = {}
lis = []
for i in range(0,len(sub_seq)):
    for j in range(0,len(seq)):
        if sub_seq[i] == seq[j]:
            int_dict[sub_seq[i]] = j+1
            
print(int_dict)