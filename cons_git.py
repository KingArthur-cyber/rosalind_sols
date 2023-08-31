f= open("consensus.txt","r")

lines  = f.readlines()
seq = []
arr1 =[]
for i in range(len(lines)):
    if i%2==1:
        seq.append(lines[i])

for i in range(len(seq)):
    arr2=[]
    for j in range(len(seq[i])):
        if seq[i][j] == '\n':
            continue
        else:
            arr2.append(seq[i][j])
    arr1.append(arr2)



A = []
C = []
G = []
T = []
Max = []

for i in range(len(arr1[i])):
    a = 0
    c = 0
    g = 0
    t = 0
    temp = []
    for j in range(len(arr1)):
        if arr1[j][i]=="A":
            a+=1
        elif arr1[j][i]=="T":
            t+=1
        elif arr1[j][i]=="G":
            g+=1
        else:
            c+=1
    A.append(a)
    C.append(c)
    G.append(g)
    T.append(t)
    temp.append(a)
    temp.append(c)
    temp.append(g)
    temp.append(t)
    Max.append(temp.index(max(temp)))

count = 0
for ma in Max:
    if ma == 0:
        Max[count] = "A"
        count+=1
    elif ma == 1:
        Max[count] = "C"
        count += 1
    elif ma == 2:
        Max[count] = "G"
        count += 1
    else:
        Max[count] = "T"
        count += 1



print("".join(Max))
A = [str (i) for i in A]
C = [str (i) for i in C]
G = [str (i) for i in G]
T = [str (i) for i in T]

print("A: "+" ".join(A))
print("C: "+" ".join(C))
print("G: "+" ".join(G))
print("T: "+" ".join(T))

