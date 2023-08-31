import numpy as np
file_name = "creating_a_distance_matrix.txt"
with open(file_name) as f:
    new_dict = {}
    
    for line in f:
        line = line.rstrip('\n')
        if line.startswith('>'):
            
            key = line.lstrip('>')
            new_dict[key] = []
        else:
            
            new_dict[key].append(line)
print(new_dict)
'''
for key,value in new_dict.items():
    value = ''.join(value)
    new_dict[key] = value
value = []
for values in new_dict.values():
    value.append(values)
def backtrace(first, second, matrix):
    f = [char for char in first]
    s = [char for char in second]
    new_f, new_s = [], []
    row = len(f)
    col = len(s)
    trace = [[row, col]]

    while True:
        if f[row - 1] == s[col - 1]:
            cost = 0
        else:
            cost = 2

        r = matrix[row][col]
        a = matrix[row - 1][col]
        b = matrix[row - 1][col - 1]
        c = matrix[row][col - 1]

        if r == b + cost:
            # when diagonal backtrace substitution or no substitution
            trace.append([row - 1, col - 1])
            new_f = [f[row - 1]] + new_f
            new_s = [s[col - 1]] + new_s

            row, col = row - 1, col - 1

        else:
            # either deletion or insertion, find if minimum is up or left
            if r == a + 1:
                trace.append([row - 1, col])
                new_f = [f[row - 1]] + new_f
                new_s = ["-"] + new_s

                row, col = row - 1, col

            elif r == c + 1:
                trace.append([row, col - 1])
                new_f = ["-"] + new_f
                new_s = [s[col - 1]] + new_s

                row, col = row, col - 1

        # Exit the loop
        if row == 0 or col == 0:
            return trace, new_f, new_s
         
def word_edit_distance(x, y):
    rows = len(x) + 1
    cols = len(y) + 1
    distance = np.zeros((rows, cols), dtype=int)

    for i in range(1, rows):
        for k in range(1, cols):
            distance[i][0] = i
            distance[0][k] = k

    for col in range(1, cols):
        for row in range(1, rows):
            if x[row - 1] == y[col - 1]:
                cost = 0
            else:
                cost = 2
            distance[row][col] = min(distance[row - 1][col] + 1,
                                     distance[row][col - 1] + 1,
                                     distance[row - 1][col - 1] + cost)
    seq1 = ''
    seq2 = ''
    align = backtrace(x, y, distance)
    print(align)
        
    print(seq1)
    edit_distance = distance[row][col]
    return edit_distance, distance


result = word_edit_distance(value[0],value[1])
print(result[0])
print(result[1])    
'''