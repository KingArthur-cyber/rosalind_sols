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
