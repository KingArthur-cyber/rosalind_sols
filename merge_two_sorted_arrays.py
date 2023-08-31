#Preprocessing starts here
filename = "merge_two_sorted_arrays.txt"
with open(filename) as f:
    lines = f.readlines()
    size_1 = int(lines[0].rstrip("\n"))
    size_2 = int(lines[2].rstrip("\n"))
    array_1 = lines[1].rstrip("\n").split(" ")
    array_2 = lines[3].rstrip("\n").split(" ")
#print(size_1,size_2)
array_1 = [int(x) for x in array_1]
array_2 = [int(x) for x in array_2]
#print(array_1,array_2)

#Preprocessing ends here

#print(size_1,size_2)
def merger(size1,size2,array1,array2):
    sorted_array = [None] *(size1 + size2)
    i = j = k = 0
    while ((i < size1) and (j < size2)):
        if array1[i] < array2[j]:
            sorted_array[k] = array1[i]
            k += 1
            i += 1
        else:
            sorted_array[k] = array2[j]
            k += 1
            j += 1
    while i < size1:
        sorted_array[k] = array1[i]
        k = k + 1
        i = i + 1
 
    
    while j < size2:
        sorted_array[k] = array2[j]
        k = k + 1
        j = j + 1
        
    return sorted_array
                    
        
temp = merger(size_1,size_2,array_1,array_2)
print(*temp)

        
        
        