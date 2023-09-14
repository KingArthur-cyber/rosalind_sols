def file_reader(file):
    with open(file) as f:
        lines = f.readlines()
        num = int(lines[0].rstrip('\n'))
        set_a = lines[1].rstrip('\n')[1:-1]
        set_b = lines[2].rstrip('\n')[1:-1]
        set_a = set_a.split(',')
        set_b = set_b.split(',')
    ans =  [num,set_a,set_b]   
    return ans

def set_union(set1,set2):
    
    union_set = set(set1 + set2)
    return union_set

def set_intersection(set_1,set_2):
    ans_set = []
    if len(set_1) > len(set_2):
        for i in range(0,len(set_1)):
            for j in range(0,len(set_2)):
                if set_1[i] == set_2[j]:
                    ans_set.append(set_1[i])
                    break
    else:
        for i in range(0,len(set_2)):
            for j in range(0,len(set_1)):
                if set_1[i] == set_2[j]:
                    ans_set.append(set_1[i])
                    break
                    
    
    return set(ans_set)
 
def set_subtraction(set_1,set_2):
    set_1_minus_set_2 = []
    set_2_minus_set_1 = []
    for i in range(0,len(set_1)):
        if set_1[i] not in set_2:
            set_1_minus_set_2.append(set_1[i])
    for i in range(0,len(set_2)):
        if set_2[i] not in set_1:
            set_2_minus_set_1.append(set_2[i])
    return set(set_1_minus_set_2),set(set_2_minus_set_1)

def set_complement(set_1,num):
    complement_set = []
    num_set = [x for x in range(1,num+1)]
    for i in range(0,len(num_set)):
        if num_set[i] not in set_1:
            complement_set.append(num_set[i])
    return set(complement_set)
    
    
sets = file_reader('set_operations.txt')
num = sets[0]
set_a = [int(x) for x in sets[1]]
set_b = [int(x) for x in sets[2]]
print(set_union(set_a,set_b))
print(set_intersection(set_a,set_b))
print(set_subtraction(set_a,set_b)[0])
print(set_subtraction(set_a,set_b)[1])
print(set_complement(set_a,num))
print(set_complement(set_b,num))
    
    
        