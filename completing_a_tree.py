def read_input(file_path):
    with open(file_path, 'r') as file:
        n = int(file.readline().strip())
        edges = 0
        for line in file:
            u, v = map(int, line.strip().split())
            edges += 1
            print(n,edges)
        return n, edges

def calculate_missing_edges(n, edges):
    missing_edges = n - 1 - edges
    return missing_edges

def minimum_edges_to_tree(file_path):
    n, edges = read_input(file_path)
    missing_edges = calculate_missing_edges(n, edges)
    return missing_edges

# Example usage
file_path = 'completing_a_tree.txt'
result = minimum_edges_to_tree(file_path)
print(result)
