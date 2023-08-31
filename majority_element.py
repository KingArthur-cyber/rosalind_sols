#Preprocessing starts here

filename = "majority_element.txt"
with open(filename) as f:
    lines = f.readlines()
    no_size = lines[0].rstrip("\n")
    lis = no_size.split(" ")
    arrays = []
    for line in lines:
        line = line.rstrip("\n").split(" ")
        
        arrays.append(line)
number,size = int(lis[0]),int(lis[1])
print(number,size)
arrays = arrays[1:]
list_of_array = []
for i in range(0,len(arrays)):
    temp = []
    for j in range(0,len(arrays[i])):
        number = int(arrays[i][j])
        temp.append(number)
    list_of_array.append(temp)
print(list_of_array)

#Preprocessing ends here and we get three imp things size,number,list_of_array

def majority(k,n,array):
    count = 0
    while count < k:
        for i in range(0,len(array)):
            counter = array.count(array[i])
            if (counter > n/2):
                return array[i]
            
        return -1
        count += 1
answers = []
for i in range(0,len(list_of_array)):
    temp = majority(number,size,list_of_array[i])
    answers.append(temp)
print(*answers)


            
        