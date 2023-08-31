filename = "2way_partition.txt"
with open(filename) as f:
    lines = f.readlines()
    size = int(lines[0].rstrip("\n"))
    array = lines[1].rstrip("\n").split(" ")
    
array = [int(x) for x in array]
#print(array)
def two_way_partition(size,array):
    middle = size//2
    min_el = min(array)
    min_el_in = array.index(min_el)
    array[middle],array[min_el_in] = array[min_el_in],array[middle]
    print(min_el)
    print(array.index(min_el))
    for i in range(0,size):
        if array[i] == min_el:
            pass
        elif array[i] > min_el:
            array[i],array[0] = array[0],array[i]
        elif array[i] < min_el:
            array[i],array[-1] = array[-1],array[i]
         
    return array
    
two_way_partition(size,array)  
