import numpy as np
def hamming(string1,string2):
    score = 0
    for i in range(0,len(string1)):
        if string1[i] == string2[i]:
            pass
        else:
            score += 1
    return score

file_name = "edit_distance_alignment.txt"
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
print(value)
new_value = value
matrix = []
while value != []:
    matrix.append(value[:1])
    value = value[1:]
matrix_1 = np.array(matrix)


if len(new_value[1]) > len(new_value[0]):
    new_value[0] += (len(new_value[1])-len(new_value[0]))* '-'
elif len(new_value[0]) == len(new_value[1]):
    new_value[0] = new_value[0]
    new_value[1] = new_value[1]
else:
    new_value[0] += (len(new_value[0])-len(new_value[1]))* '-'
print(new_value[0],new_value[1]) 


    
scoring_matrix = np.zeros((len(new_value[1])+1,len(new_value[0])+1))
backtracing_matrix = np.zeros((len(new_value[1])+1,len(new_value[0])+1))
for i in range(0,len(scoring_matrix[0])):
    scoring_matrix[0][i] = i
for i in range(0,len(new_value[1])+1):
    scoring_matrix[i][0] = i
    
#print(scoring_matrix)
#Filling of Matrix
count1 = 0

for i in range(0,len(new_value[1])):
    count1 += 1
    count2 = 1
    for j in range(0,len(new_value[0])):
        if new_value[1][i] == new_value[0][j]:
            diag = scoring_matrix[count1-1][count2-1]                
            scoring_matrix[i+1][j+1] = diag
            backtracing_matrix[i+1][j+1] = 1.1
            
        else:
            left = scoring_matrix[count1-1][count2]
            diag = scoring_matrix[count1-1][count2-1]
            up = scoring_matrix[count1][count2-1]       
            scoring_matrix[i+1][j+1] = min(left,up,diag) + 1
            previous_box = min(left,diag,up)
            
            if previous_box == left:
                backtracing_matrix[i+1][j+1] = 1.2
            elif previous_box == up:
                backtracing_matrix[i+1][j+1] = 1.3
            else:
                backtracing_matrix[i+1][j+1] = 1.4
            
            
        count2 += 1
for i in range(0,len(new_value[1])):
    print(backtracing_matrix[i][i])
    if backtracing_matrix[i][i] == 1.4:
        new_value[1] = new_value[1][:i-1] + '-' + new_value[1][i-1:]
    else:
        pass
if len(new_value[1]) > len(new_value[0]):
    new_value[0] += (len(new_value[1])-len(new_value[0]))* '-'
elif len(new_value[0]) == len(new_value[1]):
    new_value[0] = new_value[0]
    new_value[1] = new_value[1]
else:
    new_value[0] += (len(new_value[0])-len(new_value[1]))* '-'
print(new_value[0],new_value[1]) 

print(new_value[1])
print(scoring_matrix)
print(backtracing_matrix)
print(new_value[0])
print(new_value[1])
print(hamming(new_value[0],new_value[1]))


