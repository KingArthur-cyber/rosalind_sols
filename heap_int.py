import heapq

filename = "heap.txt"
with open(filename) as f:
    lines = f.readlines()
    size = int(lines[0].rstrip("\n"))
    array = lines[1].rstrip("\n").split(" ")
array = [int(x) for x in array]

heapq._heapify_max(array)
print(*array)