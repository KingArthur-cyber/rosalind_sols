import math

def file_reader(file):
    with open(file) as f:
        line = f.readlines()
        num = int(line.rstrip('\n'))
    return num

def combinations(num):
    res = 0
    for i in range(1,num+1):
        comb_form = (math.factorial(num))/(math.factorial(i) * math.factorial(num - i)) 
        res += comb_form
    return res + 1

#num = file_reader('counting_subsets.txt')
num = 941
ans = (combinations(num)) % 1000000
print(ans)
