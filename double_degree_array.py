filename = "double_degree_array.txt"
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

pre_made = [x for x in range(1,5)]
#print(pre_made)
#print(adj_list)
graph = {}
for i in pre_made:
    graph[i] = [i]
for i in range(1,len(graph.keys()) + 1):
    for j in range(0,len(adj_list)):
        if graph[i][0] == adj_list[j][0]:
            graph[i] += adj_list[j]
        elif graph[i][0] == adj_list[j][1]:
            graph[i] += adj_list[j]
print(graph)
branch = []
for value in graph.values():
    temp = list(set(value))
    branch.append(temp)
#print(branch)
graph_deg = {}
for i in range(1,len(branch)+1):
    graph_deg[i] = 0
for i in range(0,len(branch)):
    graph_deg[i+1] =  len(branch[i]) -1
print(graph_deg)
count = 0 
new_graph = {}
for i in pre_made:
    branch[count].remove(i)
    count += 1
#print(branch)
for i in range(1,len(branch)+1):
    new_graph[i] = branch[i-1]
print(new_graph)
answer = []
for i in range(1,len(graph)):
    for j in range(0,len(new_graph.values()[i])):
        

    
    
        
        



    