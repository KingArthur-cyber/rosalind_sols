import re
table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                 
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
file_name = "orf.txt"
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

s = value[0]
rvrs_compl = ''
for i in s:
    if i == 'A':
        rvrs_compl += 'T'
    elif i == 'C':
        rvrs_compl += 'G'
    elif i == 'G':
        rvrs_compl += 'C'
    else:
        rvrs_compl += 'A'


codons = []
translated = ''
final_list = []

for i in range(2,len(s),3):
    codons.append(s[i:i+3])
    if s[i:i+3] in table.keys():
        translated += table.get(s[i:i+3])
  
print("Translated: ",translated)  
        
protein = []
search = re.findall(r'(M[A-Z]*\_)',translated)
#print(search)
empty_lis = []
for i in range(0,len(search)):
    if search[i].count('M') > 1:
        for j in range(1,len(search[i])):
            if search[i][j] == 'M':
                empty_lis.append(search[i][j:])
    
#print(empty_lis)
concat = empty_lis + search

for i in concat:
    final_list.append(i)
    print("First: ",i)



rvrs_compl = rvrs_compl[::-1]

codons = []
translated = ''
for i in range(2,len(rvrs_compl),3):
    codons.append(rvrs_compl[i:i+3])
    if rvrs_compl[i:i+3] in table.keys():
        translated += table.get(rvrs_compl[i:i+3])
 
print("Reverse_Translated: ",translated)        

search = re.findall(r'(M[A-Z]*\_)',translated)
#print(search)
empty_lis = []
for i in range(0,len(search)):
    if search[i].count('M') > 1:
        for j in range(1,len(search[i])):
            if search[i][j] == 'M':
                empty_lis.append(search[i][j:])
    
   
#print(empty_lis)
concat = empty_lis + search
for i in concat:
    final_list.append(i)
    print("Reverse: ",i)
for i in set(final_list):
    print(i[:-1])





