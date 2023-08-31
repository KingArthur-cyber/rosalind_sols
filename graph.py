data = "completing_a_tree.txt"
with open(data, "r") as f:
    n = int(f.readline())
    adjacency_list = [line.strip().split(" ") for line in f]
# print(n)
print(adjacency_list)

subtrees = [] 
nodes = set() 
for i, j in adjacency_list:
    if i in nodes or j in nodes:
        for st in subtrees:
            if i in st or j in st:
                subtrees[subtrees.index(st)].append(i)
                subtrees[subtrees.index(st)].append(j)
                nodes.add(i), nodes.add(j)
    else
        subtrees.append([i,j])
        nodes.add(i), nodes.add(j)
print(subtrees)
'''
l = len(subtrees)
for i in range(l):
    for j in range(l):
        if i==j:
           break
        if len(set(subtrees[i] + subtrees[j])) < len(subtrees[i]) + len(subtrees[j]):
            subtrees[i] = list(set(subtrees[i] + subtrees[j]))
            subtrees[j] = []
subtrees = [i for i in subtrees if i]
print(len(subtrees))
pre_made_nodes = []
nodes = []
for node1,node2 in adjacency_list:
    if int(node1) not in nodes:
        nodes.append(int(node1))
    if int(node2) not in nodes:
        nodes.append(int(node2))
print(sorted(nodes))
        
for i in range(1,911):
    pre_made_nodes.append(i)
missing_nodes = []
for i in range(0,len(nodes)):
    if nodes[i] not in pre_made_nodes:
        missing_nodes.append(nodes[i])

print(missing_nodes)
'''
    
