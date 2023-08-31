filename = "degree_array.txt"
with open(filename)as f:
    for line in f:
        lines = f.readlines()
    length = lines[-1].rstrip('\n')

    adj_list = []
    count = 0
    while count < len(lines) :
        temp_list = []
        for i in lines[count].split():
            num_int = int(i)
            temp_list.append(num_int)
        adj_list.append(temp_list)
        count += 1
pre_made = [x for x in range(1,1001)]
#print(pre_made)
#print(adj_list)
graph = {}
for i in pre_made:
    graph[i] = [i]
for i in range(1,len(graph.keys()) + 1):
    for j in range(0,len(adj_list)):
        if graph[i][0] == adj_list[j][0]:
            graph[i].append(adj_list[j])
        elif graph[i][0] == adj_list[j][1]:
            graph[i].append(adj_list[j])
answer = []
for i in graph.values():
    answer.append(len(i)-1)
print(*answer)
    