#Preprocessing
filename = "3sum.txt"
with open(filename) as f:
    lines  = f.readlines()
    num_size = lines[0].rstrip("\n").split(" ")
    arrays = []
    for line in lines:
        line = line.rstrip("\n").split(" ")
        arrays.append(line)
arrays = arrays[1:]
num = int(num_size[0])
size = int(num_size[1])
new_arrays = []
for i in range(0,num):
    temp = []
    for j in range(0,size):
        te = int(arrays[i][j])
        temp.append(te)
    new_arrays.append(temp)
       
#print(new_arrays)
#Preprocessing ends here

def three_sum(num,size,array):
    
    copy_array = array.copy()
    min_num = min(copy_array)
    run = True
    answer = []
    answer1 = []
    while run:
        #Negative Approach
        min_num = min(copy_array)
        for i in range(0,len(copy_array)):
            for j in range(0,len(copy_array)):
                if i == j:
                    pass
                elif (copy_array[i] + copy_array[j] == abs(min_num)):
                    run = False
                    num = [array.index(min_num)+1,array.index(copy_array[i])+1,array.index(copy_array[j])+1]
                    if set(num) not in answer:
                        answer.append(set(num))
                if i == size -1:
                    run = False
                    if [-1] not in answer:
                        answer.append([-1])
        copy_array.remove(min_num)
                
        #Positive Approach
        copy_array = array.copy()
        max_num = max(copy_array)
        for i in range(0,len(copy_array)):
            for j in range(0,len(copy_array)):
                if i == j:
                    pass
                elif (abs(copy_array[i] + copy_array[j]) == max_num):
                    run = False
                    num = [array.index(max_num)+1,array.index(copy_array[i])+1,array.index(copy_array[j])+1]
                    if num not in answer1:
                        answer1.append(set(num))
                if i == size -1:
                    run = False
                    if [-1] not in answer1:
                        answer1.append([-1])
        copy_array.remove(max_num)
        
    
    
    return answer,answer1
        
answer =[]        
for i in range(0,num):
    answer.append(three_sum(num,size,new_arrays[i]))
  
print(answer)