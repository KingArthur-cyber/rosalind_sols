file = "binary_search.txt"
file_contents = []
with open(file) as f:
    for line in f.readlines():
        line = line.rstrip("\n")
        file_contents.append(line)
n = int(file_contents[0])
m = int(file_contents[1])
array =  file_contents[2]
array = list(array.split(" "))

search_items = file_contents[3]
search_items = list(search_items.split(" "))

def binary_search(n,m,array,search_item):
    low = 0
    high = n - 1   
    mid = 0  
        
    while low <= high:

        mid = low + (high - low)//2

        if array[mid] == search_item:
            return mid + 1
        elif array[mid] < search_item:
            low = mid + 1

        else:
            high = mid - 1
         
    return -1
  

searchable_list = []
search_items1 = []
for i in array:
    searchable_list.append(int(i))

for i in search_items:
    search_items1.append(int(i))
#print(searchable_list)
#print(search_items1)
answers = []  
for i in range(0,len(search_items1)):       
    answers.append(binary_search(n,m,searchable_list,search_items1[i]))
print(*answers)
        