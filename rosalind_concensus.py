import numpy as np
#Loading of sequences here

file_name = "consensus.txt"
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

#Matrix filling starts here

matrix = []
while value != []:
    matrix.append(value[:1])
    value = value[1:]
matrix_1 = np.array(matrix)


#print(matrix_1[6][0][0])
len_of_seq = len(matrix_1[0][0])
#making of consensus sequence
#Making of matrix here
con_seq = ''
lis = []
for i in range(0,len(matrix_1[0][0])):
    count_a,count_g,count_c,count_t = 0,0,0,0
    temp_lis = []
    for j in range(0,len(matrix_1)):
        
        if matrix_1[j][0][i] == 'A':
            count_a += 1
            
        elif matrix_1[j][0][i] == 'G':
            count_g += 1
            
        elif matrix_1[j][0][i] == 'C':
            count_c += 1
            
        else:
            count_t += 1
    
    if count_a > count_c and count_a > count_g and count_a > count_t:
        con_seq += 'A'
    elif count_c > count_a and count_c > count_g and count_c > count_t:
        con_seq += 'C'
    elif count_g > count_c and count_g > count_a and count_g > count_t:
        con_seq += 'G'
    else:
        con_seq += 'T'
    
        
        
    lis.append(count_a)
    lis.append(count_c)
    lis.append(count_g)
    lis.append(count_t)
m = np.array(lis)
m = m.reshape(len_of_seq,4)
m = m.transpose()
print(con_seq)  

file=open("concensus.txt","w")

fa=""
sa=["A","C","G","T"]

for i in range(4):
    s=np.array_str(m[i])
    n=""
    for i in s:
        if i=="[" or i=="]":
            pass
        else:
            n+=i
    fa+=sa[i]+n+"\n"

print(fa)


'''file.write("A:"+*m[0])
file.write("C:"+*m[1])
file.write("G:"+*m[2])
file.write("T:"+*m[3])

'''

'''with open('out.txt','w') as f:
    f.write(con_seq)
    f.write("A:",m[0])
    f.write("C:",m[1])
    f.write("G:",m[2])
    f.write("T:",m[3])'''
    
