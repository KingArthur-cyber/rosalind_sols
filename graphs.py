file_name = "file.txt"
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
    length = len(value)
value = []
for values in new_dict.values():
    value.append(values)

#print(value)
print(value[0][-3:],value[1][:3])
for i in range(0,len(value)):
    for j in range(0,len(value)):
        
        if value[i] == value[j]:
            #print(list(new_dict)[i],list(new_dict)[j])
            pass
        elif value[i][-3:] == value[j][:3]:
            print(list(new_dict)[i],list(new_dict)[j])

#print(new_dict)            

