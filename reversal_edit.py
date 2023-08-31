import numpy as np

file = "reversal_edit.txt"
with open(file) as f:
    lines = f.readlines()
    length = lines[0].rstrip('\n')

    num_list = []
    count = 0
    while count < len(lines) :
        temp_list = []
        for i in lines[count].split():
            num_int = int(i)
            temp_list.append(num_int)
        num_list.append(temp_list)
        count += 1
list_1 = num_list[0:2]
print(list_1)
count = 0 

for i in range(0,len(list_1[0])):
    for j in range(0,len(list_1[1])):
        if list_1[0][i] == list_1[1][j] and i == j:
            
            continue
        elif list_1[0][i] == list_1[1][j] and i != j:
            if ((i -j == 1) or (j - i == 1)):
                print(i,j)
                list_1[1][i],list_1[1][j] = list_1[1][j],list_1[1][i]
                print(list_1[1])
                count += 1
            else:
                print(i,j)
                count += 1
                list_1[1][i:j+1] = list_1[1][i:j+1][::-1]
                print(list_1[1])
print(count)
