import numpy as np
import tabulate as tb 

file_name = "edit_distance_alignment.txt"
with open(file_name) as f:
    new_dict = {}
    
    for line in f:
        line = line.rstrip('\n')
        if line.startswith('>'):
            
            key = line.lstrip('>')
            new_dict[key] = []
        else:
            
            new_dict[key].append(line)

for key,value in new_dict.items():
    value = ''.join(value)
    new_dict[key] = value
value = []
for values in new_dict.values():
    value.append(values)

print(value)

def wagner_fischer(word_1, word_2):
    n = len(word_1) + 1  # counting empty string 
    m = len(word_2) + 1  # counting empty string

    # initialize D matrix
    D = np.zeros(shape=(n, m), dtype=np.int)
    D[:,0] = range(n)
    D[0,:] = range(m)

    # B is the backtrack matrix. At each index, it contains a triple
    # of booleans, used as flags. if B(i,j) = (1, 1, 0) for example,
    # the distance computed in D(i,j) came from a deletion or a
    # substitution. This is used to compute backtracking later.
    B = np.zeros(shape=(n, m), dtype=[("del", 'b'), 
                      ("sub", 'b'),
                      ("ins", 'b')])
    B[1:,0] = (1, 0, 0) 
    B[0,1:] = (0, 0, 1)

    for i, l_1 in enumerate(word_1, start=1):
        for j, l_2 in enumerate(word_2, start=1):
            deletion = D[i-1,j] + 1
            insertion = D[i, j-1] + 1
            substitution = D[i-1,j-1] + (0 if l_1==l_2 else 2)

            mo = np.min([deletion, insertion, substitution])

            B[i,j] = (deletion==mo, substitution==mo, insertion==mo)
            D[i,j] = mo
    return D, B

def naive_backtrace(B_matrix):
    i, j = B_matrix.shape[0]-1, B_matrix.shape[1]-1
    backtrace_idxs = [(i, j)]

    while (i, j) != (0, 0):
        if B_matrix[i,j][1]:
            i, j = i-1, j-1
        elif B_matrix[i,j][0]:
            i, j = i-1, j
        elif B_matrix[i,j][2]:
            i, j = i, j-1
        backtrace_idxs.append((i,j))

    return backtrace_idxs

def align(word_1, word_2, bt):

    aligned_word_1 = []
    aligned_word_2 = []
    operations = []

    backtrace = bt[::-1]  # make it a forward trace

    for k in range(len(backtrace) - 1): 
        i_0, j_0 = backtrace[k]
        i_1, j_1 = backtrace[k+1]

        w_1_letter = None
        w_2_letter = None
        op = None

        if i_1 > i_0 and j_1 > j_0:  # either substitution or no-op
            if word_1[i_0] == word_2[j_0]:  # no-op, same symbol
                w_1_letter = word_1[i_0]
                w_2_letter = word_2[j_0]
                op = " "
            else:  # cost increased: substitution
                w_1_letter = word_1[i_0]
                w_2_letter = word_2[j_0]
                op = "s"
        elif i_0 == i_1:  # insertion
            w_1_letter = " "
            w_2_letter = word_2[j_0]
            op = "i"
        else: #  j_0 == j_1,  deletion
            w_1_letter = word_1[i_0]
            w_2_letter = " "
            op = "d"

    aligned_word_1.append(w_1_letter)
    aligned_word_2.append(w_2_letter)
    operations.append(op)

    return aligned_word_1, aligned_word_2, operations
def make_table(word_1, word_2, D, B, bt):
    w_1 = word_1.upper()
    w_2 = word_2.upper()

    w_1 = "#" + w_1
    w_2 = "#" + w_2

    table = []
    # table formatting in emacs, you probably don't need this line
    table.append(["<r>" for _ in range(len(w_2)+1)])
    table.append([""] + list(w_2))

    max_n_len = len(str(np.max(D)))

    for i, l_1 in enumerate(w_1):
        row = [l_1]
    for j, l_2 in enumerate(w_2):

        v, d, h = B[i,j]
        direction = ("⇑" if v else "") +\
            ("⇖" if d else "") +\
            ("⇐" if h else "")
        dist = str(D[i,j])

        cell_str = "{direction} {star}{dist}{star}".format(
                                     direction=direction,
                                     star=" *"[((i,j) in bt)],
                                     dist=dist)
        row.append(cell_str)
    table.append(row)

    return table
D, B = wagner_fischer(word_1, word_2)
bt = naive_backtrace(B)
word_1 = value[0]
word_2 = value[1]

edit_distance_table = make_table(word_1, word_2, D, B, bt)
alignment_table = align(word_1, word_2, bt)

print("Minimum edit distance with backtrace:")
print("#+ATTR_HTML: :border 2 :rules all :frame border "
      ":style text-align: right")  # org-babel export html properties
print(tb.tabulate(edit_distance_table, stralign="right", tablefmt="orgtbl"))

print("\nAlignment:")
print(tb.tabulate(alignment_table, tablefmt="orgtbl"))
