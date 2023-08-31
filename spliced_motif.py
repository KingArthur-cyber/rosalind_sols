file_name = "spliced_motif.txt"
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
print(value)

seq = value[0]
sub_seq = value[1]

lis = []
count = 0
i = 0
while count < len(sub_seq):
    if seq[i] == sub_seq[count]:
        print(i+1)
        count += 1
    i += 1
   
  
            
            
