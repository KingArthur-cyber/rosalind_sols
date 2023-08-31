file_name = "tree_of_life.txt"
with open(file_name) as f:
    no_of_nodes = f.readline()
    print(no_of_nodes)
    edges = []
    for i in f.readlines():
        i = i.rstrip('\n')
        edges.append(i)    
#print(edges)
edge1 = []
edge2 = []
for i in range(0,len(edges)):
    for j in range(0,len(edges[i])):
        temp1 = ''
        temp2 = ''
        if edges[i][j] == ' ':
            temp1 = edges[i][:j]
            edge1.append(temp1)
            temp2 = edges[i][j+1:]
            edge2.append(temp2)
no_of_nodes = int(no_of_nodes)     
temp_edges = [] 
node_list = [x for x in range(1,no_of_nodes)]
for i in range(0,len(edge1)):
    for j in range(0,len(edge2)):
        if edge1[i] == edge2[j]:
            continue
        
class Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def print_tree(self):
        print(self.data)
        
root = Tree(10)
