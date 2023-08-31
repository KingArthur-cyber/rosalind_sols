file_name = "kmer.txt"
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


s = value[0]
#s = 'TTGATTACCTTATTTGATCATTACACATTGTACGCTTGTGTCAAAATATCACATGTGCCT'
lex = 'ACGT'
n = 4

total = len(lex)**n
count = 0
lexico_list = []
while count < total:
    string = ''

    for i in range(0,len(lex)):
        string = ''
        for j in range(0,len(lex)):
            for x in range(0,len(lex)):
                for k in range(0,len(lex)):
                    string = lex[i] + lex[j] + lex[x] + lex[k]
                    count += 1
                    #print(string)
                    lexico_list.append(string)
                    
#print(lexico_list)


reading_0 = []
reading_1 = []
reading_2 = []
reading_3 = []
for i in range(0,len(s),4):
    reading_0.append(s[i:i+4])
for i in range(1,len(s),4):
    reading_1.append(s[i:i+4])
for i in range(2,len(s),4):
    reading_2.append(s[i:i+4])
for i in range(3,len(s),4):
    reading_3.append(s[i:i+4])
count = 0
for i in reading_3:
    if i == 'AAAA':
        count += 1
print(count)
reading = reading_0 + reading_1 + reading_2 + reading_3
print(reading)
count_list =[]
for i in lexico_list:
    count = 0
    for j in reading:
        if i == j:
            count += 1
    count_list.append(count)
            
print(*count_list, sep = ' ')
