import requests as r
import urllib
from io import StringIO
import re

file_name = 'protein_motif.txt'
cID = []
with open(file_name) as f:
    lines = f.readlines()
    for i in lines:
        item = i.rstrip('\n')
        cID.append(item)
print(cID)
acc_lis = []
for i in range(0,len(cID)):
    for j in range(0,len(cID[i])):
        if cID[i][j] == '_':
            acc_lis.append(cID[i][:j])
            break
    if len(cID[i]) == len(cID[0]):
        acc_lis.append(cID[i])
     
        
print(acc_lis)
     
lis = []

for i in range(0,len(cID)):
        
    baseUrl="http://www.uniprot.org/uniprot/"
    currentUrl=baseUrl+acc_lis[i]+".fasta"
    response = r.post(currentUrl)
    cData=''.join(response.text) 
    lis.append(cData)

with open('output.txt','w+') as f:
    f.writelines(x for x in lis)

file_name = 'output.txt'
with open(file_name) as f:
    new_dict = {}
    
    for line in f:
        line = line.rstrip('\n')
        if line.startswith('>'):
            key = line.lstrip('>')
            new_dict[key] = []
        else:
            new_dict[key].append(line)
#print(new_dict)
for key,value in new_dict.items():
    value = ''.join(value)
    new_dict[key] = value
value = []
for values in new_dict.values():
    value.append(values)
#print(value)

pattern = '(?=(N[^P][ST][^P]))'

regex =  re.search(pattern,value[0])
res_dict = dict(zip(cID,value))
print(res_dict)
some_dict = {}
for key,value in res_dict.items():
    for match in re.finditer(pattern,value):
        start = match.start() + 1
        if key not in some_dict.keys():
            some_dict[key] = []
        some_dict[key].append(start)
print(some_dict)

for key,value in some_dict.items():
    print(key,"\n",*value,sep = " ")
    
