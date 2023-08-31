filename = "insertion_sort.txt"
with open(filename) as f:
    lines = f.readlines()
    length = int(lines[0].rstrip("\n"))
    array = lines[1].rstrip("\n").split(" ")
#print(length)
#print(array)
def insertionSort(array,length):
    count  = 0
    for i in range(2,length):
        k = i
        while (k >= 1) and (array[k] < array[k-1]):
            array[k-1],array[k] = array[k],array[k-1]
            count += 1
            k = k - 1
    return array,count

array = [int(x) for x in array]
print(insertionSort(array,length))

            