import math
import itertools

def file_reader(file):
    with open(file) as f:
        lines = f.readlines()
        alphabets = lines[0].strip('\n')
        num = int(lines[1].strip('\n'))
    return (alphabets,num)

def arrange(order_lis,lis):
    
    data = lis
    ordering = order_lis
    priorities = {letter: index for index, letter in enumerate(ordering)}
    result = sorted(data, key=lambda x: tuple(map(lambda y: priorities[y], x)))
    
    return result
            
            
file = 'ordering_strings.txt'
content = file_reader(file)
alphabets = content[0].split(" ")
num = content[1]
comb_list = []
final_list = []

for i in range(0,num + 1):
    comb_list.append(itertools.product(alphabets,repeat = i))
for i in comb_list:
    for j in i:
        ans = ''.join(j)
        final_list.append(ans)

for i in arrange(alphabets,final_list): 
    print(i)















