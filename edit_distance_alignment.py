import numpy as np
def hamming(string1,string2):
    score = 0
    for i in range(0,len(string1)):
        if string1[i] == string2[i]:
            pass
        else:
            score += 1
    return score
def minimum(num1,num2,num3):
    if (num1 < num2) and (num1 < num3):
        smallest_num = num1
    elif (num2 < num1) and (num2 < num3):
      
        smallest_num = num2
    else:
        smallest_num = num3
    return smallest_num
 
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

new_value = value
matrix = []
while value != []:
    matrix.append(value[:1])
    value = value[1:]
matrix_1 = np.array(matrix)

print(new_value[0])
print(new_value[1])
gap_cost = 3
mismatch_cost = 1

scoring_matrix = np.zeros((len(new_value[1])+1,len(new_value[0])+1))
backtracing_matrix = np.zeros((len(new_value[1])+1,len(new_value[0])+1))
count0 = 0
for i in range(0,len(scoring_matrix[0])):
    scoring_matrix[0][i] = count0
    count0 += gap_cost
count0 = 0
for i in range(0,len(new_value[1])+1):
    scoring_matrix[i][0] = count0
    count0 += gap_cost
    
print(scoring_matrix)
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
            left = scoring_matrix[count1][count2-1]
            diag = scoring_matrix[count1-1][count2-1]
            up = scoring_matrix[count1-1][count2]       
            scoring_matrix[i+1][j+1] = minimum(left,up,diag) + 1
            previous_box = minimum(left,diag,up)
            
            if previous_box == left:
                backtracing_matrix[i+1][j+1] = 1.2
            elif previous_box == up:
                backtracing_matrix[i+1][j+1] = 1.3
            else:
                backtracing_matrix[i+1][j+1] = 1.4
            
            
        count2 += 1
for i in range(0,len(new_value[1])):
    #print(backtracing_matrix[i][i])
    
    if backtracing_matrix[i][i] == 1.3:
        new_value[1] = new_value[1][:i+1] + '-' + new_value[1][i+1:]
    else:
        pass

 
print(scoring_matrix)
print(backtracing_matrix)
print(len(new_value[0]))
print(len(new_value[1]))




