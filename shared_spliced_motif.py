file_name = "shared_spliced_motif.txt"
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

seq1 = value[0]
seq2 = value[1]

# Function to find lcs_algo
def lcs_algo(S1, S2, m, n):
    L = [[0 for x in range(n+1)] for x in range(m+1)]

    # Building the mtrix in bottom-up way
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif S1[i-1] == S2[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    index = L[m][n]

    lcs_algo = [""] * (index+1)
    lcs_algo[index] = ""

    i = m
    j = n
    while i > 0 and j > 0:

        if S1[i-1] == S2[j-1]:
            lcs_algo[index-1] = S1[i-1]
            i -= 1
            j -= 1
            index -= 1

        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1
            
    # Printing the sub sequences
    print("S1 : " + S1 + "\nS2 : " + S2)
    print("LCS: " + "".join(lcs_algo))


m = len(seq1)
n = len(seq2)
lcs_algo(seq1, seq2, m, n)
'''if len(seq1) > len(seq2):
    add = len(seq1) - len(seq2)
    seq2 = seq2 + (add * '_')
else:
    add = len(seq2) - len(seq1)
    seq1 = seq1 + (add * '_')
    
print(seq1,seq2)
print(len(seq1))
result_0 = ''
for i in range(0,len(seq1)):    
    for j in range(0,len(seq2)):
        if seq1[i] == seq2[j]:
            seq2 = seq2[j+1:]
            result_0 += seq1[i]
            #print(i,j)
            break
print(len(result_0))                
seq1 = seq1[1:]
result_1 = ''
for i in range(0,len(seq1)):    
    for j in range(0,len(seq2)):
        if seq1[i] == seq2[j]:
            seq2 = seq2[j+1:]
            result_1 += seq1[i]
            print(i,j)
            break
print(len(result_1))                
seq1 = seq1[2:]
result_2 = ''
for i in range(0,len(seq1)):    
    for j in range(0,len(seq2)):
        if seq1[i] == seq2[j]:
            seq2 = seq2[j+1:]
            result_2 += seq1[i]
            #print(i,j)
            break
print(len(result_2))                
'''