from math import log10

def file_reader(file):
    with open(file) as f:
        lines = f.readlines()
        nums = lines[0].rstrip('\n')
        nums = nums.split(' ')
        gc = lines[1].split(" ")
    return(int(nums[0]),float(nums[1]),gc[0])

def probability_random_strings(n,x,s):
    p = 1
    at = 0
    gc = 0
    for i in s:
        if i == 'A' or i == 'T':
            at = at + 1
        elif i == 'G' or i == 'C':
            gc = gc + 1

    q = ((0.5*x) ** gc) * ((0.5 - 0.5*x) ** at) 
    p = 1 - (1 - q) ** n
    return p


file = "matching_random_motifs.txt"
contents = file_reader(file)
num = contents[0]
gc = contents[1]
string = contents[2]
result = probability_random_strings(num, gc, string)

print(result) 
