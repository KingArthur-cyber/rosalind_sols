filename = "heap.txt"
with open(filename) as f:
    lines = f.readlines()
    size = int(lines[0].rstrip("\n"))
    array = lines[1].rstrip("\n").split(" ")
array = [int(x) for x in array]
print(array)
def heapify(size,array):
    copy_array = array.copy()
    k = 0
    largest = copy_array[k]
    left = copy_array[2*k + 1]
    right = copy_array[2*k + 2]
    if left > largest:
        left,largest = largest,left
    if right > largest:
        right,largest = largest,right
        
    
                
    return copy_array
print(heapify(size,array))
                
        
        
        