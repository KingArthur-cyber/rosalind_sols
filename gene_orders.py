from itertools import permutations
n = 3
lis = []
for i in range(-n,n+1):
    if i == 0:
        pass
    else:
        lis.append(i)

perm = permutations(lis,n)
perm_list = []
for i in list(perm):
    perm_list.append(i)
    #print(i)
count = 0
lis = []
for i in range(0,len(perm_list)):
    if abs(perm_list[i][0]) == abs(perm_list[i][1]) or abs(perm_list[i][0]) == abs(perm_list[i][2]) or abs(perm_list[i][1]) == abs(perm_list[i][2]):
        pass
    else:
        count += 1
        print(perm_list[i][0],perm_list[i][1],perm_list[i][2])
print(count)