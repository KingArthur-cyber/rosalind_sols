import numpy as np

file_name = "genome.txt"
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
for i in value:
    print(len(i))

def long_diag(m,n):
    result = [0,0]
    maxdiag = 0
    last = np.unravel_index(np.argmax(m,axis = None),m.shape)
    for i in range (0, len(m)):
        for j in range (0, len(m[i])):
            k = 0;
            while (i+k < len(m) and j+k < len(m[0]) and m[i+k][j+k] != 0):
                k+=1;
                if (k > maxdiag):
                    maxdiag = k;
                    result[0]=i;
                    result[1]=j;
        
    return result[0],result[1],last[0],last[1]

count = 1
run = True
super_seq = ''
while run:
    
    if count == 1:
        seq1 = value[count-1]
        seq2 = value[count]
        scoring_array = np.zeros((len(seq2)+1,len(seq1)+1))
        for i in range(0,len(seq1)):
            for j in range(0,len(seq2)):
                if seq1[i] == seq2[j]:
                    scoring_array[j+1][i+1] = 1 + scoring_array[j][i]
                else:
                    scoring_array[j+1][i+1] = 0
                   
    if count > 1:
        seq1 = super_seq
        seq2 =  value[count]
        scoring_array = np.zeros((len(seq2)+1,len(seq1)+1))
        for i in range(0,len(seq1)):
            for j in range(0,len(seq2)):
                if seq1[i] == seq2[j]:
                    scoring_array[j+1][i+1] = 1 + scoring_array[j][i]
                else:
                    scoring_array[j+1][i+1] = 0
    if count > len(value)-2:
        run = False
        
    index = long_diag(scoring_array,len(scoring_array))
    seq = seq1[0:index[1]-1] + seq1[index[1]-1:index[3]] + seq2[0:index[0]-1] + seq2[index[2]:]       
    super_seq = seq     
    count += 1
    print(index)
    print(scoring_array)
    print("{} done".format(count-1))
    print(len(super_seq))
    print(super_seq)
    #print(count)
    

print(len(super_seq))
print(super_seq)
 
                
                
                
                
                
            
    
    
        
