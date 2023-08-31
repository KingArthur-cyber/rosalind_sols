#Preprocessing starts here
filename = "2sum.txt"
with open(filename) as f:
    lines = f.readlines()
    number_size = lines[0].rstrip("\n").split(" ")
    arrays = []
    for line in lines:
        line = line.rstrip("\n")
        line = line.split(" ")
        arrays.append(line)
arrays = arrays[1:]
number = int(number_size[0])
size = int(number_size[1])
#print(arrays)  
#Preprocessing ends here 

def two_sum(number,size,array):
    returns = []
    for i in range(0,size):
        for j in range(0,size):
            if i == j:
                pass
            elif (i < j):
                if (array[i] == ('-' + array[j])):
                    returns.append([i+1,j+1])
            if returns == []:
                returns.append(-1)
    return returns                
    
def min_finder(answer):
    
    if len(answer) > 1:
        temp = []
        for i in range(0,len(answer)):
            temp.append(answer[i][1])
        min_y = min(temp)
        for i in range(0,len(answer)):
            if min_y == answer[i][1]:
                return answer[i]
    else:
        return [-1]
    
#print(len(arrays))
for i in range(0,len(arrays)):
    answer = two_sum(number,size,arrays[i])
    #print(answer)
    print(*min_finder(answer[1:]))
        
    

