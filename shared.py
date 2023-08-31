#Do this again
file_name = "shared.txt"
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
#print(new_dict)
value = []
for values in new_dict.values():
    value.append(values)
#print(value)
result = []
for i in range(0,len(value)):
    if len(value[0]) == len(value[i]):
        result.append(value[i])
    else:
        add = len(value[0]) - len(value[i])
        result.append(value[i] + add * '-')
        
#print(result) 
'''
n = len(result)
s = result[0]
l = len(s)
res = ''
for i in range(0,l):
    for j in range(i +1,l +1):
        stem = s[i:j]
        k = 0
        for k in range(0,n):
            if stem not in result[k]:
                break
        if (k+1 == n and len(res) < len(stem)):
            res = stem 
print(res)
'''
def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(0,len(data[0])):
            for j in range(0,len(data[0])-i+1):
                if j > len(substr) and is_substr(data[0][i:i+j], data):
                    substr = data[0][i:i+j]
    return substr

def is_substr(find, data):
    if len(data) < 1 and len(find) < 1:
        return False
    for i in range(len(data)):
        if find not in data[i]:
            return False
    return True


print(long_substr(result))